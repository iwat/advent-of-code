use core::fmt;
use std::{
    collections::{HashMap, VecDeque},
    error::Error,
    fs,
};

use z3::{Optimize, SatResult, ast::Int};

#[allow(dead_code)]
struct BinaryVec<'a> {
    data: &'a Vec<u32>,
    bits: usize,
}

impl<'a> fmt::Debug for BinaryVec<'a> {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        f.write_str("[")?;

        for (i, item) in self.data.iter().enumerate() {
            write!(f, "{:0w$b}", item, w = self.bits)?;
            if i < self.data.len() - 1 {
                f.write_str(", ")?;
            }
        }
        f.write_str("]")
    }
}

#[allow(dead_code)]
struct Machine {
    bits: u8,
    goal: u32,
    buttons: Vec<u32>,
    joltages: Vec<u32>,
}

impl fmt::Debug for Machine {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        f.debug_struct("Machine")
            .field(
                "goal",
                &format_args!("{:0w$b}", self.goal, w = self.bits as usize),
            )
            .field(
                "buttons",
                &BinaryVec {
                    data: &self.buttons,
                    bits: self.bits as usize,
                },
            )
            .field("joltages", &self.joltages)
            .finish()
    }
}

#[allow(dead_code)]
impl Machine {
    fn new(goal_str: &str) -> Self {
        let mut goal = 0u32;
        for c in goal_str[1..goal_str.len() - 1].chars() {
            if c == '#' {
                goal = goal << 1;
                goal |= 1;
            } else {
                goal = goal << 1;
            }
        }

        Machine {
            bits: goal_str.len() as u8 - 2,
            goal: goal,
            buttons: Vec::new(),
            joltages: Vec::new(),
        }
    }

    fn add_button(&mut self, b: &str) {
        let mut button = 0u32;
        for c in b[1..b.len() - 1].split(',') {
            let c8 = c.parse::<u8>().unwrap();
            button |= 1 << (self.bits - c8 - 1);
        }
        self.buttons.push(button);
    }

    fn set_joltages(&mut self, v: &str) {
        self.joltages = v[1..v.len() - 1]
            .split(',')
            .map(|vv| vv.parse().unwrap())
            .collect();
    }

    fn solve(&self) -> Result<u32, Box<dyn Error>> {
        let mut known_states = HashMap::<u32, u32>::new();
        let mut queue = VecDeque::<(u32, u32)>::new();
        known_states.insert(0, 0);
        queue.push_front((0, 0));
        while !queue.is_empty() {
            let (state, depth) = queue.pop_front().unwrap();
            if state == self.goal {
                continue;
            }
            for b in &self.buttons {
                let new_state = state ^ b;
                let new_depth = depth + 1;
                println!(
                    "State: {:b}, Button {:b}, New {:b}, Depth: {}",
                    state, b, new_state, new_depth
                );
                if let Some(known_depth) = known_states.get(&new_state) {
                    if new_depth < *known_depth {
                        known_states.insert(new_state, new_depth);
                        queue.push_back((new_state, new_depth));
                    }
                } else {
                    known_states.insert(new_state, new_depth);
                    queue.push_back((new_state, new_depth));
                }
            }
        }
        if let Some(depth) = known_states.get(&self.goal) {
            Ok(*depth)
        } else {
            Err("No path found".into())
        }
    }
}

#[allow(dead_code)]
fn read_input() -> Result<Vec<Machine>, Box<dyn Error>> {
    let file = fs::read_to_string("input.txt")?;
    let mut machines = Vec::<Machine>::new();

    for line in file.lines() {
        let line = line.trim();
        if line == "" {
            continue;
        }
        let parts = line.split_whitespace().collect::<Vec<_>>();
        let mut m = Machine::new(parts[0]);
        for i in 1..parts.len() - 1 {
            m.add_button(parts[i]);
        }
        m.set_joltages(parts[parts.len() - 1]);
        machines.push(m);
    }

    Ok(machines)
}

#[allow(dead_code)]
fn part1() -> Result<(), Box<dyn Error>> {
    let mut sum_depth = 0;
    let machines = read_input()?;
    for m in machines {
        let depth = m.solve()?;
        println!("{:?} = {}", m, depth);
        sum_depth += depth;
    }
    println!("Total depth: {}", sum_depth);
    Ok(())
}

fn solve_v2(line: &str) -> Result<u64, &'static str> {
    println!("line: {}", line);
    let parts = line.split_whitespace().collect::<Vec<_>>();
    let mut buttons = Vec::<Vec<u8>>::new();
    for part in parts[1..parts.len() - 1].iter() {
        let indexes = part[1..part.len() - 1]
            .split(',')
            .map(|s| s.parse::<u8>().unwrap())
            .collect::<Vec<_>>();
        //println!("button {:?}", indexes);
        buttons.push(indexes);
    }
    let last_line = parts[parts.len() - 1];
    let joltages = last_line[1..last_line.len() - 1]
        .split(',')
        .map(|s| s.parse::<u16>().unwrap())
        .collect::<Vec<_>>();
    //println!("joltages {:?}", joltages);

    let consts = (1..=buttons.len())
        .map(|i| Int::new_const(format!("b{}", i)))
        .collect::<Vec<_>>();
    //println!("consts {:?}", consts);
    let opt = Optimize::new();
    for j in 0..joltages.len() {
        let mut exp = Int::from_u64(0);
        for (i, cols) in buttons.iter().enumerate() {
            if cols.contains(&(j as u8)) {
                exp += &consts[i];
            }
        }
        opt.assert(&exp.eq(&Int::from_u64(joltages[j] as u64)));
    }

    let mut minimize = Int::from_u64(0);
    for c in &consts {
        opt.assert(&c.ge(&Int::from_u64(0)));
        minimize += c;
    }
    opt.minimize(&minimize);

    //println!("optimizer {:?}", opt);

    match opt.check(&[]) {
        SatResult::Sat => {
            let model = opt.get_model().ok_or("Optimizer should have a model")?;

            println!("Found optimal solution:");
            let mut total = 0;
            for c in &consts {
                let val = model
                    .get_const_interp(c)
                    .ok_or("Should get value")?
                    .as_u64()
                    .ok_or("Value should be u64")?;
                println!("{}: {}", c, val);
                total += val;
            }
            println!("Presses: {}", total);
            Ok(total)
        }
        SatResult::Unsat => Err("The constraints are unsatisfiable."),
        SatResult::Unknown => Err("The solver returned unknown."),
    }
}

fn part2() -> Result<(), Box<dyn Error>> {
    let mut sum_depth = 0u64;

    let file = fs::read_to_string("input.txt")?;
    for line in file.lines() {
        let line = line.trim();
        if line == "" {
            continue;
        }
        let depth = solve_v2(line);
        sum_depth += depth?;
    }

    println!("Total presses: {}", sum_depth);
    Ok(())
}

fn main() -> Result<(), Box<dyn Error>> {
    part2()
}

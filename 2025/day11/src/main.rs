use std::{
    collections::{HashMap, VecDeque},
    fs::File,
    io::{BufRead, BufReader},
    ops::AddAssign,
};

#[allow(dead_code)]
fn read_input() -> Result<HashMap<String, Vec<String>>, std::io::Error> {
    let file = File::open("input.txt")?;
    let buf = BufReader::new(file);
    let mut map = HashMap::<String, Vec<String>>::new();
    for line in buf.lines() {
        let line = line?;
        let line = line.trim();
        let parts = line.split(" ").collect::<Vec<_>>();

        let parent_id = parts[0][0..3].to_string();
        let child_ids = parts[1..parts.len()]
            .iter()
            .map(|part| part.to_string())
            .collect::<Vec<String>>();

        for child_id in &child_ids {
            map.entry(child_id.clone()).or_insert(Vec::new());
        }

        map.entry(parent_id.clone())
            .or_insert(Vec::new())
            .extend(child_ids);

        println!("line: {}", line);
    }
    println!("map: {:?}", map);
    Ok(map)
}

#[allow(dead_code)]
fn solve1(map: &HashMap<String, Vec<String>>) {
    let mut queue = VecDeque::<&str>::new();
    queue.push_front("you");

    let mut ways = 0;
    while !queue.is_empty() {
        let next = queue.pop_front().unwrap();
        if next == "out" {
            println!("out");
            ways += 1;
            continue;
        }
        for child_id in map.get(next).unwrap() {
            queue.push_back(child_id);
        }
    }
    println!("ways: {}", ways);
}

#[allow(dead_code)]
fn part1() -> Result<(), std::io::Error> {
    let map = read_input()?;
    solve1(&map);
    Ok(())
}

fn solve2(map: &HashMap<String, Vec<String>>) {
    let mut counter = HashMap::<(&str, bool, bool), usize>::new();
    let mut queue = VecDeque::<(&str, bool, bool)>::new();
    queue.push_front(("svr", false, false));

    while let Some((next, seen_fft, seen_dac)) = queue.pop_back() {
        // println!("Processing {} {} {}", next, seen_fft, seen_dac);
        if next == "out" {
            let c = counter.entry((next, seen_fft, seen_dac)).or_insert(0);
            if seen_fft && seen_dac {
                c.add_assign(1);
            }
            // println!("set counter: {:?} = {}", (next, seen_fft, seen_dac), c);
            continue;
        }
        if let Some(_c) = counter.get(&(next, seen_fft, seen_dac)) {
            // println!("mem counter: {:?} = {}", (next, seen_fft, seen_dac), c);
            continue;
        }
        let children = map.get(next).unwrap();

        let mut res = 0;
        let mut all_children = true;
        for child in children {
            match counter.get(&(
                child,
                seen_fft || child == "fft",
                seen_dac || child == "dac",
            )) {
                Some(child_res) => res += child_res,
                None => all_children = false,
            }
        }
        if all_children {
            let c = counter.entry((next, seen_fft, seen_dac)).or_insert(0);
            c.add_assign(res);
            // println!("set counter: {:?} = {}", (next, seen_fft, seen_dac), c);
            continue;
        } else {
            queue.push_back((next, seen_fft, seen_dac));
        }
        for child in children {
            queue.push_back((
                child,
                seen_fft || child == "fft",
                seen_dac || child == "dac",
            ));
        }
    }

    println!("counter: {:?}", counter[&("svr", false, false)]);
}

fn part2() -> Result<(), std::io::Error> {
    let map = read_input()?;
    solve2(&map);
    Ok(())
}

fn main() -> Result<(), std::io::Error> {
    part2()
}

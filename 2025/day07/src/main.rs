use std::{collections::HashMap, error::Error, fs};

#[allow(dead_code)]
fn part1() -> Result<(), Box<dyn Error>> {
    let input = fs::read_to_string("input.txt")?;
    let input = input.trim();
    let mut lines = input
        .lines()
        .map(|line| line.to_string())
        .collect::<Vec<String>>();

    let mut splits = 0;
    for line_idx in 0..lines.len() {
        if line_idx == 0 {
            println!("{}", lines[line_idx]);
            continue;
        }
        for char_idx in 0..lines[line_idx].len() {
            let prev_char = lines[line_idx - 1].chars().nth(char_idx).unwrap();
            let char = lines[line_idx].chars().nth(char_idx).unwrap();
            if prev_char == 'S' || prev_char == '|' {
                if char == '.' {
                    lines[line_idx].replace_range(char_idx..=char_idx, "|");
                } else if char == '^' {
                    if let Some(idx) = char_idx.checked_sub(1) {
                        lines[line_idx].replace_range(idx..=idx, "|");
                    }
                    if char_idx + 1 < lines[line_idx].len() {
                        lines[line_idx].replace_range(char_idx + 1..=char_idx + 1, "|");
                    }
                    splits += 1;
                }
            }
        }
        println!("{}", lines[line_idx]);
    }

    print!("Number of splits: {}", splits);

    Ok(())
}

fn part2() -> Result<(), Box<dyn Error>> {
    let input = fs::read_to_string("input.txt")?;
    let input = input.trim();
    let lines = input.lines().collect::<Vec<&str>>();

    let mut visited = HashMap::<(usize, usize), u64>::new();

    for line_idx in (0..lines.len()).rev() {
        for char_idx in 0..lines[line_idx].len() {
            let c = lines[line_idx].chars().nth(char_idx).unwrap();
            if visited.contains_key(&(line_idx + 1, char_idx)) {
                if c == '.' {
                    visited.insert((line_idx, char_idx), visited[&(line_idx + 1, char_idx)]);
                } else if c == '^' {
                    let mut sum_score = 0;
                    if let Some(score) = visited.get(&(line_idx + 1, char_idx + 1)) {
                        sum_score += score;
                    }
                    if let Some(score) = visited.get(&(line_idx + 1, char_idx - 1)) {
                        sum_score += score;
                    }
                    visited.insert((line_idx, char_idx), sum_score);
                } else if c == 'S' {
                    println!("S = {:?}", visited[&(line_idx + 1, char_idx)]);
                }
            } else {
                visited.insert((line_idx, char_idx), 1);
            }
        }
        println!("{}", lines[line_idx]);
    }

    Ok(())
}

fn main() -> Result<(), Box<dyn Error>> {
    part2()
}

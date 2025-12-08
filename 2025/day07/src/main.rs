use std::{error::Error, fs};

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

fn main() -> Result<(), Box<dyn Error>> {
    part1()
}

use std::{
    fs::File,
    io::{BufRead, BufReader},
};

#[allow(dead_code)]
fn part1() -> Result<(), std::io::Error> {
    let file = File::open("input.txt")?;
    let file = BufReader::new(file);
    let mut sum: u32 = 0;
    for line in file.lines() {
        let line = line?;
        let line = line.trim();

        let vals: Vec<u8> = line
            .chars()
            .filter_map(|c| c.to_digit(10).map(|d| d as u8))
            .collect();

        let first_digit = vals[0..vals.len() - 1]
            .iter()
            .enumerate()
            .max_by_key(|(idx, val)| (*val, -(*idx as i32)))
            .unwrap();
        println!("first {:?}", first_digit);
        let second_digit = vals[first_digit.0 + 1..vals.len()]
            .iter()
            .enumerate()
            .max_by_key(|(idx, val)| (*val, -(*idx as i32)))
            .unwrap();
        println!("second {:?}", second_digit);

        let old_sum = sum;
        let joltage = *first_digit.1 as u32 * 10 + *second_digit.1 as u32;
        sum += joltage;
        println!("Sum {} + {} = {}", old_sum, joltage, sum);
    }
    Ok(())
}

fn part2() -> Result<(), std::io::Error> {
    let file = File::open("input.txt")?;
    let file = BufReader::new(file);
    let mut sum: u64 = 0;
    for line in file.lines() {
        let line = line?;
        let line = line.trim();

        let vals: Vec<u8> = line
            .chars()
            .filter_map(|c| c.to_digit(10).map(|d| d as u8))
            .collect();
        println!("line {:?}", vals);

        let mut joltage: u64 = 0;
        let mut digit: (i32, &u8) = (-1, &0);
        for exp in (0..=11).rev() {
            let next_digit = vals[(digit.0 + 1) as usize..vals.len() - exp]
                .iter()
                .enumerate()
                .max_by_key(|(idx, val)| (*val, -(*idx as i32)))
                .unwrap();
            digit = (digit.0 + 1 + next_digit.0 as i32, next_digit.1);
            println!("exp {} digit {:?}", exp, digit);
            joltage += *digit.1 as u64 * 10u64.pow(exp as u32);
        }

        let old_sum = sum;
        sum += joltage;
        println!("Sum {} + {} = {}", old_sum, joltage, sum);
    }
    Ok(())
}

fn main() -> Result<(), std::io::Error> {
    part2()
}

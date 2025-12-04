use std::{
    fs::File,
    io::{BufRead, BufReader},
};

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
fn main() -> Result<(), std::io::Error> {
    part1()
}

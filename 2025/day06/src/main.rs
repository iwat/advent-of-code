use std::fs;

fn part1() -> Result<(), Box<dyn std::error::Error>> {
    let input = fs::read_to_string("input.txt")?;
    let input = input.trim();
    let mut rows = Vec::<Vec<u16>>::new();
    let mut symbols = Vec::<&str>::new();
    for line in input.lines() {
        let line = line.trim();
        if &line[0..1] == "*" || &line[0..1] == "+" {
            for symb in line.split_whitespace() {
                symbols.push(symb);
            }
        } else {
            let mut row = Vec::<u16>::new();
            for num in line.split_whitespace() {
                row.push(num.parse::<u16>()?);
            }
            rows.push(row);
        }
    }
    let mut grand_sum = 0u64;
    for i in 0..symbols.len() {
        let mut result = rows[0][i] as u64;
        for row in &rows[1..] {
            if symbols[i] == "*" {
                result *= row[i] as u64;
            } else {
                result += row[i] as u64;
            }
        }
        println!("{}", result);
        grand_sum += result;
    }
    println!("Grand sum: {}", grand_sum);
    Ok(())
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    part1()
}

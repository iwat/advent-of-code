use std::fs;

#[allow(dead_code)]
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

fn part2() -> Result<(), Box<dyn std::error::Error>> {
    let input = fs::read_to_string("input.txt")?;
    let input = input.trim();
    let rows = input.lines().collect::<Vec<&str>>();

    let mut cols = Vec::<(char, usize, usize)>::new();
    for (i, c) in rows.last().unwrap().chars().enumerate() {
        if c == '*' || c == '+' {
            if cols.len() > 0 {
                let len = cols.len();
                cols[len - 1].2 = i - 2;
            }
            cols.push((c, i, std::usize::MAX));
        }
    }
    println!("Columns: {:?}", cols);

    let mut grand_sum = 0;
    for col in cols {
        println!("Column: {:?}", col);
        let mut entries = Vec::<u32>::new();
        for row in &rows[0..rows.len() - 1] {
            let last = col.2.min(row.len() - 1);
            println!("Row: {} @ {} {}", row, col.1, last);
            let chars = row[col.1..=last].chars().collect::<Vec<char>>();
            for (i, c) in chars.iter().enumerate() {
                if entries.len() <= i {
                    entries.push(0);
                }
                match c.to_digit(10) {
                    Some(digit) => entries[i] = entries[i] * 10 + digit,
                    None => {}
                }
                print!("{} ", entries[i]);
            }
            println!();
        }

        println!("Entries: {:?}", entries);
        let mut result = entries[0] as u128;
        for entry in &entries[1..entries.len()] {
            if col.0 == '+' {
                result += *entry as u128;
            } else {
                result *= *entry as u128;
            }
        }
        println!("Result: {}", result);
        grand_sum += result;
    }
    println!("Grand Sum: {}", grand_sum);
    Ok(())
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    part2()
}

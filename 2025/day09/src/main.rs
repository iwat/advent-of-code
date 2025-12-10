use std::{
    error::Error,
    fs::File,
    io::{BufRead, BufReader},
};

fn read_input() -> Result<Vec<(u32, u32)>, Box<dyn Error>> {
    let file = File::open("input.txt")?;
    let buf = BufReader::new(file);
    let mut coords = Vec::<(u32, u32)>::new();
    for line in buf.lines() {
        if let Ok(line) = line {
            let line = line.trim();
            if line.is_empty() {
                break;
            }
            let parts: Vec<&str> = line.split(',').collect();
            if parts.len() != 2 {
                return Err(format!("Invalid input format: {}", line).into());
            }
            let x = parts[0].parse::<u32>()?;
            let y = parts[1].parse::<u32>()?;
            coords.push((x, y));
        }
    }

    Ok(coords)
}

fn part1() -> Result<(), Box<dyn Error>> {
    let mut coords = read_input()?;
    coords.sort_by_key(|&(x, _y)| x);
    let mut best_size = 0u64;
    for i in 0..coords.len() {
        for j in i..coords.len() {
            let coord1 = coords[i];
            let coord2 = coords[j];
            if coord2.0 < coord1.0 || coord2.1 < coord1.1 {
                continue;
            }
            let size = (coord2.0 as i32 - coord1.0 as i32 + 1) as u64
                * (coord2.1 as i32 - coord1.1 as i32 + 1) as u64;
            if size > best_size {
                println!(
                    "New best size: {} ({}, {})-({}, {})",
                    size, coord1.0, coord1.1, coord2.0, coord2.1
                );
                best_size = size;
            }
        }
    }
    Ok(())
}

fn main() -> Result<(), Box<dyn Error>> {
    part1()
}

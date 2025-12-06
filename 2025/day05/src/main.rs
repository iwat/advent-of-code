use std::fs;

#[allow(dead_code)]
fn part1() -> Result<(), Box<dyn std::error::Error>> {
    let input = fs::read_to_string("input.txt")?;
    let input = input.trim();
    let lines = input.split("\n");

    let mut ranges = Vec::<(u64, u64)>::new();
    let mut ingredients = Vec::<u64>::new();

    for line in lines {
        let line = line.trim();
        if line == "" {
            continue;
        }
        if line.contains("-") {
            let parts = line.split("-").collect::<Vec<&str>>();
            let start = parts[0].parse::<u64>()?;
            let end = parts[1].parse::<u64>()?;
            ranges.push((start, end));
        } else {
            let ingredient = line.parse::<u64>()?;
            ingredients.push(ingredient);
        }
    }
    ranges.sort();
    println!("ranges: {:?}", ranges);

    let mut fresh_items = 0;
    for ingredient in ingredients {
        println!("test ingredient {}", ingredient);
        let mut spoiled = true;
        for range in &ranges {
            println!("  test range {:?}", range);
            if ingredient >= range.0 && ingredient <= range.1 {
                println!("  fresh");
                spoiled = false;
                break;
            }
        }
        if spoiled {
            println!("  spoiled");
        } else {
            fresh_items += 1;
        }
    }

    println!("fresh items: {}", fresh_items);

    Ok(())
}

fn part2() -> Result<(), Box<dyn std::error::Error>> {
    let input = fs::read_to_string("input.txt")?;
    let input = input.trim();
    let lines = input.split("\n");

    let mut ranges = Vec::<(u64, u64)>::new();

    for line in lines {
        let line = line.trim();
        if line == "" {
            continue;
        }
        if line.contains("-") {
            let parts = line.split("-").collect::<Vec<&str>>();
            let start = parts[0].parse::<u64>()?;
            let end = parts[1].parse::<u64>()?;
            ranges.push((start, end));
        }
    }
    ranges.sort();
    println!("ranges: {:?}", ranges);

    let mut merged_ranges = Vec::<(u64, u64)>::new();
    for range in &ranges {
        match merged_ranges.last() {
            None => {
                println!("initializing with {:?}", range);
                merged_ranges.push(*range);
            }
            Some(last) if last.1 >= range.0 => {
                println!("modifying last {:?} with {:?}", last, range);
                let last = merged_ranges.last_mut().unwrap();
                last.1 = last.1.max(range.1);
                println!("modified last {:?}", last);
            }
            Some(_) => {
                println!("new range {:?}", range);
                merged_ranges.push(*range);
            }
        }
    }
    println!("merged ranges: {:?}", merged_ranges);

    let mut total_size = 0;
    for range in &merged_ranges {
        println!("range {:?} size {}", range, range.1 - range.0 + 1);
        total_size += range.1 - range.0 + 1;
    }

    println!("total size {}", total_size);

    Ok(())
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    part2()
}

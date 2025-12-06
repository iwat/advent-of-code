use std::fs;

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

fn main() -> Result<(), Box<dyn std::error::Error>> {
    part1()
}

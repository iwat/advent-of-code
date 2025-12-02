use std::fs;
use std::io;

const MAX_POSITION: i32 = 100;

#[allow(dead_code)]
fn part1() -> io::Result<()> {
    let contents = fs::read_to_string("input.txt")?;
    let lines = contents.lines();

    let mut position = 50;
    let mut code = 0;
    for line in lines {
        let direction = line.chars().next().unwrap();
        let distance = line[1..].parse::<i32>().unwrap();
        let before = position;

        if direction == 'R' {
            position = (position + distance) % MAX_POSITION;
        } else if direction == 'L' {
            position = (position - distance) % MAX_POSITION;
            if position < 0 {
                let rounds = -position / MAX_POSITION;
                position += MAX_POSITION * (rounds + 1);
            }
        }

        println!("{} {}{} {}", before, direction, distance, position);
        if position == 0 {
            code += 1;
        }
    }
    println!("Code: {}", code);
    Ok(())
}

fn part2() -> io::Result<()> {
    let contents = fs::read_to_string("input.txt")?;
    let lines = contents.lines();

    let mut position = 50;
    let mut clicks = 0;
    for line in lines {
        let direction = line.chars().next().unwrap();
        let distance = line[1..].parse::<i32>().unwrap();
        let before = position;

        if direction == 'R' {
            position += distance;
            clicks += position / MAX_POSITION;
        } else if direction == 'L' {
            position -= distance;
            if before > 0 && position <= 0 {
                clicks += 1;
            }
            clicks += -position / MAX_POSITION;
            if position < 0 {
                position += MAX_POSITION * (-position / MAX_POSITION + 1);
            }
        }
        position %= MAX_POSITION;

        println!(
            "{} {}{} {} {}",
            before, direction, distance, position, clicks
        );
    }
    println!("Clicks: {}", clicks);
    Ok(())
}

fn main() -> io::Result<()> {
    part2()
}

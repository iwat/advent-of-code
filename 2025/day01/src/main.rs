use std::fs;
use std::io;

const MAX_POSITION: i32 = 100;

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

fn main() -> io::Result<()> {
    part1()
}

use std::fs;

fn count_neighbors(x: usize, y: usize, grid: &Vec<Vec<char>>) -> u8 {
    let mut count = 0;
    for dx in -1..=1 {
        for dy in -1..=1 {
            if dx == 0 && dy == 0 {
                continue;
            }
            let nx = x as i32 + dx;
            let ny = y as i32 + dy;
            if nx >= 0 && nx < grid[0].len() as i32 && ny >= 0 && ny < grid.len() as i32 {
                if grid[ny as usize][nx as usize] == '@' || grid[ny as usize][nx as usize] == 'x' {
                    count += 1;
                }
            }
        }
    }
    count
}

#[allow(dead_code)]
fn part1() -> Result<(), std::io::Error> {
    let file = fs::read_to_string("input.txt")?;
    let file = file.trim();
    let mut grid = file
        .split("\n")
        .map(|line| line.chars().collect())
        .collect::<Vec<Vec<char>>>();
    let width = grid[0].len();
    let height = grid.len();
    let mut accessibles = 0;
    println!("WxH {}x{}", width, height);
    for y in 0..height {
        for x in 0..width {
            if grid[y][x] == '@' {
                if count_neighbors(x, y, &grid) <= 3 {
                    grid[y][x] = 'x';
                    accessibles += 1;
                }
            }
            print!("{}", grid[y][x]);
        }
        println!();
    }
    println!("Accessible cells: {}", accessibles);
    Ok(())
}

fn part2() -> Result<(), std::io::Error> {
    let file = fs::read_to_string("input.txt")?;
    let file = file.trim();
    let mut grid = file
        .split("\n")
        .map(|line| line.chars().collect())
        .collect::<Vec<Vec<char>>>();
    let width = grid[0].len();
    let height = grid.len();
    let mut removed = 0;
    println!("WxH {}x{}", width, height);
    loop {
        println!("---");
        let mut removed_in_loop = 0;
        for y in 0..height {
            for x in 0..width {
                if grid[y][x] == '@' {
                    if count_neighbors(x, y, &grid) <= 3 {
                        grid[y][x] = 'x';
                        removed_in_loop += 1;
                    }
                }
                print!("{}", grid[y][x]);
            }
            println!();
        }
        for y in 0..height {
            for x in 0..width {
                if grid[y][x] == 'x' {
                    grid[y][x] = '.';
                }
            }
        }
        removed += removed_in_loop;
        if removed_in_loop == 0 {
            break;
        }
    }
    println!("Removed cells: {}", removed);
    Ok(())
}

fn main() -> Result<(), std::io::Error> {
    part2()
}

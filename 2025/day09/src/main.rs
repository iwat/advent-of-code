use core::fmt;
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

#[allow(dead_code)]
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

struct Edge {
    x1: u32,
    y1: u32,
    x2: u32,
    y2: u32,
}

impl Edge {
    fn min_x(&self) -> u32 {
        self.x1.min(self.x2)
    }
    fn max_x(&self) -> u32 {
        self.x1.max(self.x2)
    }
    fn min_y(&self) -> u32 {
        self.y1.min(self.y2)
    }
    fn max_y(&self) -> u32 {
        self.y1.max(self.y2)
    }

    fn new(x1: u32, y1: u32, x2: u32, y2: u32) -> Self {
        Self {
            x1: x1.min(x2),
            y1: y1.min(y2),
            x2: x1.max(x2),
            y2: y1.max(y2),
        }
    }
}

impl fmt::Debug for Edge {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "({}, {}) - ({}, {})", self.x1, self.y1, self.x2, self.y2)
    }
}

fn part2() -> Result<(), Box<dyn Error>> {
    let coords = read_input()?;
    let mut edges = Vec::<Edge>::new();
    for i in 0..coords.len() {
        let cur = coords[i];
        let prev = match i {
            0 => coords[coords.len() - 1],
            _ => coords[i - 1],
        };
        edges.push(Edge::new(prev.0, prev.1, cur.0, cur.1));
    }
    println!("Edges: {:?}", edges);

    let mut best_size = 0u64;
    for i in 0..coords.len() {
        for j in i..coords.len() {
            let coord1 = coords[i];
            let coord2 = coords[j];
            let min_x = coord1.0.min(coord2.0);
            let max_x = coord1.0.max(coord2.0);
            let min_y = coord1.1.min(coord2.1);
            let max_y = coord1.1.max(coord2.1);

            let size = (max_x - min_x + 1) as u64 * (max_y - min_y + 1) as u64;
            if size > best_size {
                // TODO: I think I'm missing something here.
                // Do I need to implement ray casting?
                let mut intersect = false;
                for edge in &edges {
                    if min_x < edge.max_x()
                        && max_x > edge.min_x()
                        && min_y < edge.max_y()
                        && max_y > edge.min_y()
                    {
                        // Edge intersects with rectangle
                        intersect = true;
                        break;
                    }
                }
                if intersect {
                    continue;
                }
                println!(
                    "New best size: {} ({}, {}) - ({}, {})",
                    size, min_x, min_y, max_x, max_y
                );
                best_size = size;
            }
        }
    }
    Ok(())
}

fn main() -> Result<(), Box<dyn Error>> {
    env_logger::init();
    part2()
}

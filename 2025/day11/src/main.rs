use std::{
    collections::{HashMap, VecDeque},
    fs::File,
    io::{BufRead, BufReader},
};

fn read_input() -> Result<HashMap<String, Vec<String>>, std::io::Error> {
    let file = File::open("input.txt")?;
    let buf = BufReader::new(file);
    let mut map = HashMap::<String, Vec<String>>::new();
    for line in buf.lines() {
        let line = line?;
        let line = line.trim();
        let parts = line.split(" ").collect::<Vec<_>>();

        let parent_id = parts[0][0..3].to_string();
        let child_ids = parts[1..parts.len()]
            .iter()
            .map(|part| part.to_string())
            .collect::<Vec<String>>();

        for child_id in &child_ids {
            map.entry(child_id.clone()).or_insert(Vec::new());
        }

        map.entry(parent_id.clone())
            .or_insert(Vec::new())
            .extend(child_ids);

        println!("line: {}", line);
    }
    println!("map: {:?}", map);
    Ok(map)
}

fn solve1(map: &HashMap<String, Vec<String>>) {
    let mut queue = VecDeque::<&str>::new();
    queue.push_front("you");

    let mut ways = 0;
    while !queue.is_empty() {
        let next = queue.pop_front().unwrap();
        if next == "out" {
            println!("out");
            ways += 1;
            continue;
        }
        for child_id in map.get(next).unwrap() {
            queue.push_back(child_id);
        }
    }
    println!("ways: {}", ways);
}

fn part1() -> Result<(), std::io::Error> {
    let map = read_input()?;
    solve1(&map);
    Ok(())
}

fn main() -> Result<(), std::io::Error> {
    part1()
}

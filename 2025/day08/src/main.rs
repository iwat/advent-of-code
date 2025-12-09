use std::{
    collections::HashMap,
    error::Error,
    fs::File,
    io::{BufRead, BufReader},
};

fn part1() -> Result<(), Box<dyn Error>> {
    let f = File::open("input.txt")?;
    let bufreader = BufReader::new(f);
    let mut boxes = Vec::<(u32, u32, u32)>::new();
    for line in bufreader.lines() {
        if let Ok(line) = line {
            let parts = line
                .trim()
                .split(",")
                .map(|p| p.parse::<u32>().unwrap())
                .collect::<Vec<u32>>();
            boxes.push((parts[0], parts[1], parts[2]));
        }
    }
    let mut distance = HashMap::<(u32, u32, u32, u32, u32, u32), u64>::new();
    for i in 0..boxes.len() {
        for j in i + 1..boxes.len() {
            let distance_sq = ((boxes[i].0 as i64 - boxes[j].0 as i64).pow(2)
                + (boxes[i].1 as i64 - boxes[j].1 as i64).pow(2)
                + (boxes[i].2 as i64 - boxes[j].2 as i64).pow(2))
                as u64;
            let key: (u32, u32, u32, u32, u32, u32);
            if boxes[i] < boxes[j] {
                key = (
                    boxes[i].0, boxes[i].1, boxes[i].2, boxes[j].0, boxes[j].1, boxes[j].2,
                );
            } else {
                key = (
                    boxes[j].0, boxes[j].1, boxes[j].2, boxes[i].0, boxes[i].1, boxes[i].2,
                );
            }
            distance.insert(key, distance_sq);
        }
    }

    let mut sorted_distance = distance.into_iter().collect::<Vec<_>>();
    sorted_distance.sort_by(|a, b| a.1.cmp(&b.1));
    //println!("Sorted distances: {:?}", sorted_distance);

    let mut next_circuit_id = 1;
    let mut circuits = HashMap::<(u32, u32, u32), u16>::new();

    let mut connections = 1000u16;
    for (key, _distance) in sorted_distance {
        let box1 = (key.0, key.1, key.2);
        let box2 = (key.3, key.4, key.5);

        let circuit1 = circuits.get(&box1).copied();
        let circuit2 = circuits.get(&box2).copied();
        match (circuit1, circuit2) {
            (Some(c1), Some(c2)) => {
                if c1 == c2 {
                    println!(
                        "Box {:?} and {:?} are already in the same circuit {}",
                        box1, box2, c1
                    );
                    connections -= 1;
                } else {
                    println!(
                        "Connecting two circuits {:?} ({}) + {:?} ({})",
                        box1, c1, box2, c2
                    );
                    let c2_boxes = circuits
                        .iter()
                        .filter(|(_k, v)| *v == &c2)
                        .map(|(k, _v)| k)
                        .cloned()
                        .collect::<Vec<_>>();
                    for box2 in c2_boxes {
                        circuits.entry(box2).and_modify(|c| *c = c1);
                    }
                    connections -= 1;
                }
            }
            (Some(c1), None) => {
                println!(
                    "Connecting box {:?} to circuit {} through {:?}",
                    box2, c1, box1
                );
                circuits.insert(box2, c1);
                connections -= 1;
            }
            (None, Some(c2)) => {
                println!(
                    "Connecting box {:?} to circuit {} through {:?}",
                    box1, c2, box2
                );
                circuits.insert(box1, c2);
                connections -= 1;
            }
            (None, None) => {
                println!(
                    "Connecting box {:?} and box {:?} to new circuit {}",
                    box1, box2, next_circuit_id
                );
                circuits.insert(box1, next_circuit_id);
                circuits.insert(box2, next_circuit_id);
                connections -= 1;
                next_circuit_id += 1;
            }
        };
        if connections == 0 {
            println!("Out of connections");
            break;
        }
    }

    let mut circuit_group = HashMap::<u16, Vec<(u32, u32, u32)>>::new();
    for (junction_box, circuit) in &circuits {
        circuit_group
            .entry(*circuit)
            .or_insert(Vec::new())
            .push(*junction_box);
    }
    println!("Final circuit configuration: {:?}", circuit_group);

    let mut circuit_size = HashMap::<u16, i32>::new();
    for (_junction_box, circuit) in &circuits {
        circuit_size
            .entry(*circuit)
            .and_modify(|size| *size += 1)
            .or_insert(1);
    }
    println!("Circuit sizes: {:?}", circuit_size);

    let mut circuit_vec = circuit_size.iter().collect::<Vec<_>>();
    circuit_vec.sort_by_key(|&(_, size)| -size);
    println!("Sorted by circuit size: {:?}", circuit_vec);

    println!(
        "Top 3: {:?} {:?} {:?} = {}",
        circuit_vec[0],
        circuit_vec[1],
        circuit_vec[2],
        circuit_vec[0].1 * circuit_vec[1].1 * circuit_vec[2].1,
    );

    Ok(())
}

fn main() -> Result<(), Box<dyn Error>> {
    part1()
}

use std::{
    error::Error,
    fs::File,
    io::{BufRead, BufReader},
};

#[derive(Debug)]
struct Requirement {
    width: u8,
    length: u8,
    shape_types: [u8; 6],
}

#[derive(Debug)]
struct Input {
    shapes: Vec<[[char; 3]; 3]>,
    requirements: Vec<Requirement>,
}

#[derive(PartialEq)]
enum ReadMode {
    None,
    ShapeTitle,
    ShapeLine1,
    ShapeLine2,
}

fn str_to_char_array(input: &str, output: &mut [char; 3]) {
    let mut chars = input.chars();
    output[0] = chars.next().unwrap();
    output[1] = chars.next().unwrap();
    output[2] = chars.next().unwrap();
}

fn read_input() -> Result<Input, Box<dyn Error>> {
    let mut input = Input {
        shapes: vec![],
        requirements: vec![],
    };
    let file = File::open("simple-input.txt")?;
    let buf = BufReader::new(file);

    let mut read_mode = ReadMode::None;
    let mut shape = [[char::default(); 3]; 3];

    for line in buf.lines() {
        let line = line?;
        let line = line.trim();
        if line.ends_with(":") {
            read_mode = ReadMode::ShapeTitle;
            shape = [[char::default(); 3]; 3];
            continue;
        }
        if read_mode == ReadMode::ShapeTitle {
            read_mode = ReadMode::ShapeLine1;
            str_to_char_array(line, &mut shape[0]);
            continue;
        }
        if read_mode == ReadMode::ShapeLine1 {
            read_mode = ReadMode::ShapeLine2;
            str_to_char_array(line, &mut shape[1]);
            continue;
        }
        if read_mode == ReadMode::ShapeLine2 {
            str_to_char_array(line, &mut shape[2]);
            input.shapes.push(shape);
            read_mode = ReadMode::None;
            continue;
        }
        if line.contains("x") {
            //
        }
    }
    Ok(input)
}

fn part1() -> Result<(), Box<dyn Error>> {
    let input = read_input()?;
    println!("Input: {:?}", input);
    Ok(())
}

fn main() -> Result<(), Box<dyn Error>> {
    part1()
}

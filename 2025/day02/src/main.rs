use env_logger;
use ilog::IntLog;
use log;
use std::fs;

#[allow(dead_code)]
fn part1() -> Result<(), Box<dyn std::error::Error>> {
    env_logger::init();

    let input = fs::read_to_string("input.txt")?;
    let ranges = input.trim().split(",");
    let mut invalid_sum = 0;
    for range in ranges {
        if let Some((start, end)) = range.split_once("-") {
            let start = start.parse::<u64>()?;
            let end = end.parse::<u64>()?;
            log::debug!("# {} - {}", start, end);
            for i in start..=end {
                let digits = i.log10() + 1;
                log::debug!("## {} {}", i, digits);
                if digits % 2 == 0 {
                    let half_digits = digits / 2;
                    let left = i / (10u64.pow(half_digits as u32));
                    let right = i % (10u64.pow(half_digits as u32));
                    if left == right {
                        log::info!("{} {} {}", i, left, right);
                        invalid_sum += i;
                    } else {
                        log::debug!("{} {} {}", i, left, right);
                    }
                }
            }
        }
    }

    println!("Invalid sum: {}", invalid_sum);
    Ok(())
}

fn part2() -> Result<(), Box<dyn std::error::Error>> {
    env_logger::init();

    let input = fs::read_to_string("input.txt")?;
    let ranges = input.trim().split(",");
    let mut invalid_sum = 0;
    for range in ranges {
        if let Some((start, end)) = range.split_once("-") {
            let start = start.parse::<u64>()?;
            let end = end.parse::<u64>()?;
            log::debug!("# range {} - {}", start, end);
            for i in start..=end {
                let digits = i.log10() + 1;
                log::debug!("## id {} - digits {}", i, digits);
                for d in 1..=digits / 2 {
                    if digits % d != 0 {
                        continue;
                    }
                    log::debug!("### id {} group size {}", i, d);

                    let mut first_part: Option<u64> = None;
                    let mut remainder: u64 = i;
                    let mut invalid: bool = true;
                    while remainder > 0 {
                        let part = remainder % 10u64.pow(d as u32);
                        remainder = remainder / 10u64.pow(d as u32);
                        log::debug!("### id {} part {} remainder {}", i, part, remainder);

                        match first_part {
                            None => {
                                first_part = Some(part);
                            }
                            Some(first) => {
                                if part != first {
                                    log::debug!("{} is valid, {} != {}", i, part, first);
                                    invalid = false;
                                    break;
                                }
                            }
                        }
                    }
                    if invalid {
                        log::info!("{} is invalid", i);
                        invalid_sum += i;
                        break;
                    }
                }
            }
        }
    }

    println!("Invalid sum: {}", invalid_sum);
    Ok(())
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    return part2();
}

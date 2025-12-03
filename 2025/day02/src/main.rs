use env_logger;
use ilog::IntLog;
use log;
use std::fs;

fn main() -> Result<(), Box<dyn std::error::Error>> {
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

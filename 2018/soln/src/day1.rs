#[warn(unused_must_use)]
use std::{collections::BTreeSet,iter};

static INPUT: &str =include_str!("./day1input.txt");

type Error = Box<dyn std::error::Error>;
type Result<T,E=Error> = std::result::Result<T,E>;

pub fn part1() -> Result<()> {
    let sum: Result<i128,_> =INPUT.lines().map(str::parse::<i128>).sum();
    println!("Sum: {:?}",sum?);
    
    Ok(())
}

pub fn part2() -> Result<()> {

    let changes: Result<Vec<i128>, _> = INPUT.lines().map(str::parse::<i128>).collect();
    let changes = changes?;

    let mut seen = BTreeSet::new();
    let infinite_changes = iter::repeat(changes.iter()).flatten();
    let cumulative_frequency = infinite_changes.scan(0, |freq, i| {
        *freq += i;
        Some(*freq)
    });

    for freq in cumulative_frequency {
        if !seen.insert(freq) {
            println!("Seen {} twice", freq);
            break;
        }
    }
    Ok(())
}




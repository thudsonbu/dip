use std::collections::HashMap;

fn num_good_pairs(nums: Vec<i32>) -> i32 {
    let mut counts = HashMap::new();
    let mut ans = 0;

    for &num in nums.iter() {
        ans += counts.get(&num).cloned().unwrap_or(0);
        *counts.entry(num).or_insert(0) += 1;
    }

    ans
}

fn main() {
    assert_eq!(num_good_pairs(vec![1, 2, 3, 1, 1, 3]), 4);
    assert_eq!(num_good_pairs(vec![1, 1, 1, 1]), 6);
    assert_eq!(num_good_pairs(vec![1, 2, 3]), 0);
}

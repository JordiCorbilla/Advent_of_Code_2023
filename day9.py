from itertools import pairwise

def seq(ints):
    if all(ints == 0 for ints in ints):
        return 0
    diffs = [b - a for a, b in pairwise(ints)]
    return ints[-1] + seq(diffs)

def load_and_calculate_sum2(filename):
    try:
        with open(filename, 'r') as file:
            return sum(seq([int(x) for x in line.split()[::-1]]) for line in file)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None

filename = "day9_part1_input.txt"
total_sum = load_and_calculate_sum2(filename)

if total_sum is not None:
    print(f"Total sum of extracted digits: {total_sum}")
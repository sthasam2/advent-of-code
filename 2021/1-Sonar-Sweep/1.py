# --- Day 1: Sonar Sweep ---

depths = [int(line) for line in open("1_input.txt", "r").readlines()]

def part_one():
    print(sum(1 for i in range(1, len(depths)) if depths[i] > depths[i-1]))

def part_two():
    print(sum(1 for i in range(3, len(depths)) if depths[i] > depths[i-3]))


part_one()
part_two()

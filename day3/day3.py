# Open file for reading
file = open("input.txt", "r")
rows = []
for line in file:
    rows.append(line.strip())
file.close()


def check_tree_hit(line: str, index: int):
    index = index % len(line)
    return line[index] == "#"


def get_tree_count(right: int, down: int):
    """
    Get number of hit trees following path strategy given by params
    :param right: Number of spaces to move right after each loops
    :param down: Number of spaces to move down after each loop
    """
    count = 0
    row = 0
    shift = 0
    while row < len(rows):
        if check_tree_hit(rows[row], shift):
            count += 1
        shift += right
        row += down
    return count


r1_d1 = get_tree_count(1, 1)
r3_d1 = get_tree_count(3, 1)
r5_d1 = get_tree_count(5, 1)
r7_d1 = get_tree_count(7, 1)
r1_d2 = get_tree_count(1, 2)
print(r3_d1)
print(r1_d1 * r3_d1 * r5_d1 * r7_d1 * r1_d2)

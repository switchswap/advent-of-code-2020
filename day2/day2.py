def parse_line(line: str) -> tuple:
    tokens = line.split(" ")
    bounds = tokens[0].split("-")
    return int(bounds[0]), int(bounds[1]), tokens[1][:-1], tokens[2].strip()


def validate_entry(entry: tuple) -> bool:
    count = entry[3].count(entry[2])
    return entry[0] <= count <= entry[1]


def validate_entry_2(entry: tuple) -> bool:
    return (entry[3][entry[0] - 1] == entry[2]) ^ (entry[3][entry[1] - 1] == entry[2])


# Open file for reading
file = open("input.txt", "r")

# Append all numbers from file to array
count = 0
for line in file:
    # Comment/Uncomment based on which part you're solving
    if validate_entry(parse_line(line)):
        count += 1
    # if validate_entry_2(parse_line(line)):
    #     count += 1
file.close()
print(count)

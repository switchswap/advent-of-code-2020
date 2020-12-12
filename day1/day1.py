# Open file for reading
file = open("input.txt", "r")

# Append all numbers from file to array
numbers = []
for line in file:
    numbers.append(int(line.strip()))
file.close()

# Sort numbers to solve via 2-sum or 3-sum
numbers.sort()

# 2-sum
p1 = 0
p2 = len(numbers) - 1
while p1 != p2:
    # If we found our answer, return it and break
    if numbers[p1] + numbers[p2] == 2020:
        print(numbers[p1], numbers[p2], numbers[p1]*numbers[p2])
        break
    elif numbers[p1] + numbers[p2] < 2020:
        p1 += 1
    elif numbers[p1] + numbers[p2] > 2020:
        p2 -= 1


# 3-sum
for i in range(len(numbers) - 1):
    p1 = i + 1
    p2 = len(numbers) - 1
    while p1 != p2:
        # If we found our answer, return it and break
        if numbers[i] + numbers[p1] + numbers[p2] == 2020:
            print(numbers[i], numbers[p1], numbers[p2], numbers[i] * numbers[p1] * numbers[p2])
            break
        elif numbers[i] + numbers[p1] + numbers[p2] < 2020:
            p1 += 1
        elif numbers[i] + numbers[p1] + numbers[p2] > 2020:
            p2 -= 1


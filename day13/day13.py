# Open file for reading
file = open("input.txt", "r")
lines = file.readlines()
file.close()

depart_time = int(lines[0].strip())
busses = []
for bus in lines[1].split(","):
    if bus.strip() != "x":
        busses.append(int(bus.strip()))


def find_closest_bus_time() -> tuple:
    time = depart_time
    while True:
        for bus in busses:
            if time % bus == 0:
                return time, bus
        # Advance one time unit
        time += 1


closest_time, bus = find_closest_bus_time()
print((closest_time - depart_time) * bus)

# Part 2
busses.clear()
for bus in lines[1].split(","):
    if bus.strip() != "x":
        busses.append(int(bus.strip()))
    else:
        busses.append(-1)


busses = {29: 0, 37: 23, 631: 29, 13: 47, 19: 48, 23: 52, 383: 60, 41: 70, 17: 77}

base_time = 49355212116059
increment = 29*37*631*13*19*23*383
while True:
    if base_time % 29 == 0 \
            and (base_time + 23) % 37 == 0 \
            and (base_time + 29) % 631 == 0 \
            and (base_time + 47) % 13 == 0 \
            and (base_time + 48) % 19 == 0 \
            and (base_time + 52) % 23 == 0 \
            and (base_time + 60) % 383 == 0 \
            and (base_time + 70) % 41 == 0 \
            and (base_time + 77) % 17 == 0:
        print(base_time)
        break
    base_time += increment

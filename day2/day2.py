
input = open("input.txt", "r")
#input = open("testinput.txt", "r")


#Part 1 

def calculateLocation():
    position = 0
    depth = 0
    for line in input:
        if "forward" in line:
            position += int(line.split()[1])
        elif "up" in line:
            depth -= int(line.split()[1])
        else:
            depth += int(line.split()[1])

    return position*depth

#print(calculateLocation())

#Part 2

def calculateLocationAndAim():
    position = 0
    depth = 0
    aim = 0
    for line in input:
        value = int(line.split()[1])
        if "forward" in line:
            position += value
            depth += aim*value
        elif "up" in line:
            aim -= value
        else:
            aim += value

    return position*depth

print(calculateLocationAndAim())

input.close()
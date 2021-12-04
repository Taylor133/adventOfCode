
import sys
input = open("input.txt", "r")

sys.setrecursionlimit(5000)
    
# PART A
def count(line):
    value = input.readline()
    if value == "":
        return 0
    elif int(value)> int(line):
        return 1 + count(value)
    else:
        return count(value)
    
print(count(input.readline()))

#PART B

def slidingSums(a,b,c):
    nextValue = input.readline()
    if(nextValue) == "":
        return 0
    prevWindow = int(a) + int(b) + int(c)
    nextWindow = int(b) + int(c) + int(nextValue)

    if nextWindow > prevWindow:
        return 1 + slidingSums(b,c,nextValue)
    else:
        return slidingSums(b,c,nextValue)

#print(slidingSums(input.readline(),input.readline(),input.readline()))

input.close()
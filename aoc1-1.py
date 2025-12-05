with open("Documents\AdventOfCode\input1-1.txt", "r") as file:
    lines = file.readlines()

dial = 50
count = 0
for line in lines:
    if line[0] == "R":
        dial += int(line[1:len(line)])
        dial = dial%100
    else:
        dial -= int(line[1:len(line)])
        dial = dial%100
    if dial == 0:
        count += 1
        
print(count)
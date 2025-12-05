with open("input1-1.txt", "r") as file:
    lines = file.readlines()

#lines = ['L68', 'L30', 'R48', 'L5', 'R60', 'L55', 'L1', 'L99', 'R14', 'L82']


dial = 50
count = 0
for line in lines:
    #print(line)
    if line[0] == "R":
        dial += int(line[1:])
        while dial > 99:
            dial -= 100
            count += 1
            
    else:
        if dial == 0:
            dial = 100
        dial -= int(line[1:])
        while dial < 0:
            count += 1
            dial += 100
        if dial == 0:
            count += 1
    #print(dial)
    #print(count)
        
print(count)
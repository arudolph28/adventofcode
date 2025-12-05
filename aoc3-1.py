ratings = '''987654321111111
811111111111119
234234234234278
818181911112111'''

with open('input3.txt','r') as file:
    ratings = file.read()

ratings = ratings.split('\n')

tot = 0

for line in ratings:
    
    digits = [int(digit) for digit in line]
    maxdig = max(digits)
    maxidx = digits.index(maxdig)
    if maxidx == len(digits) - 1:
        maxdig = max(digits[:len(digits)-1])
        maxidx = digits.index(maxdig)
    nextdig = max(digits[ maxidx+1: ])
    joltage = 10*maxdig + nextdig
    tot = tot + joltage

print(tot)
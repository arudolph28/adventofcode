ids = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

with open('Documents\AdventOfCode\input2.txt', 'r') as file:
    ids = file.read()
print(ids)

ids = ids.split(',')
invalids = []

def isinvalid(num):
    dig = str(num)
    if len(dig) % 2 == 1:
        return False
    half = int(len(dig) / 2)
    if dig[:half] == dig[half:]:
        return True
    return False

for i in ids:
    givenrange = i.split('-')
    for j in range(int(givenrange[0]), int(givenrange[1])+1):
        if isinvalid(j):
            invalids.append(j)

print(sum(invalids))
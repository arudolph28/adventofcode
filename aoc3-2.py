# ratings = '''987654321111111
# 811111111111119
# 234234234234278
# 818181911112111'''

with open('input3.txt','r') as file:
    ratings = file.read()

ratings = ratings.split('\n')

for i in range(len(ratings)):
    ratings[i] = [int(digit) for digit in ratings[i]]


tot = 0

for i in range(len(ratings)):
    
    lastidx = -1
    curjolt = ''
    temp = ratings[i]

    for j in reversed(range(0,12)):
        # print( 'range', ratings[i][lastidx + 1: len(ratings[i])-j])
        # bestdig = max( ratings[i][lastidx + 1: len(ratings[i])-j])
        # print('range', temp[:len(temp)-j])
        bestdig = max(temp[:len(temp)-j])
        curjolt = curjolt + str(bestdig)
        lastidx = temp.index(bestdig)
        temp = temp[lastidx+1:]
        

    newjoltage = int(curjolt)
    # print(newjoltage)
    tot += newjoltage

print(tot)
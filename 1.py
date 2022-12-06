biggest = 0 
curr = 0
i = 0
with open('input.txt', 'r') as w:
    for line in w:
        if line is not "\n" and line is not '':
            curr += int(line)
        else:
            if biggest < curr:
                biggest = curr
            curr = 0
        

print(biggest)


biggest0 = biggest1 = biggest2 = 0 
curr = 0
i = 0
with open('input.txt', 'r') as w:
    for line in w:
        if line is not "\n" and line is not '':
            curr += int(line)
        else:
            if biggest0 < curr:
                biggest2 = biggest1
                biggest1 = biggest0
                biggest0 = curr
            elif biggest1 < curr:
                biggest2 = biggest1
                biggest1 = curr
            elif biggest2 < curr:
                biggest2 = curr
            curr = 0
        

print(biggest0+biggest1+biggest2)
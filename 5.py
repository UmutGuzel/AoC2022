stacks = {1: ['G','T','R','W'],
2: ['G','C','H','p','M','S','V','W'],
3: ['C','L','T','S','G','M'],
4: ['J','H','D','M','W','R','F'],
5: ['P','Q','L','H','S','W','F','J'],
6: ['P','J','D','N','F','M','S'],
7: ['Z','B','D','F','G','C','S','J'],
8: ['R','T','B'],
9: ['H','N','W','L','C']}

with open('input05.txt', 'r') as w:
    for line in w:
        line = line.strip('\n')
        line_list = line.split()
        n1 = int(line_list[1])
        n2 = int(line_list[3])
        n3 = int(line_list[5])
        stacks[n3]+=(stacks[n2][-n1:])
        for i in range(n1):
            if stacks[n2]:
                stacks[n2].pop()
            
print(stacks)
for i in range(1,10):
    print(stacks[i][-1])
    
#JCMHLVGMG
LVMRWSSPZ
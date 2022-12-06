
move = {
    "A":{"X":3, "Y":6, "Z":0},
    "B":{"X":0, "Y":3, "Z":6},
    "C":{"X":6, "Y":0, "Z":3}
}
addition = {"X":1, "Y":2, "Z":3}
total = 0
with open('input2.txt', 'r') as f:
    for line in f:
        line = line.strip('\n')
        p1, p2 = line.split(' ')
        total += move[p1][p2] + addition[p2]
        
        
print(total)

print('#'*50)
move = {
    "A":{"X":3, "Y":4, "Z":8},
    "B":{"X":1, "Y":5, "Z":9},
    "C":{"X":2, "Y":6, "Z":7}
}
addition = {"X":1, "Y":2, "Z":3}
total = 0
with open('input2.txt', 'r') as f:
    for line in f:
        line = line.strip('\n')
        p1, p2 = line.split(' ')
        total += move[p1][p2]
        
        
print(total)
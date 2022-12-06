total = 0
group = {}
count = 0
pre_line = ""
with open('input03.txt', 'r') as w:
    for line in w:
        s = set()
        line = line.strip("\n")
        len_line = len(line)
        if count%3 == 0:
            pre_line=line
            group = {}
        else:
            for i in range(len_line):
                if line[i] in pre_line and line[i] not in s:
                    s.add(line[i])
                    if line[i] in group.keys():
                        group[line[i]] += 1
                    else:
                        group[line[i]] = 2
            print(pre_line)
            print(group)
            for key in group:
                if group[key] == 3:
                    if key.islower():
                        total += ord(key) - 96
                    else:
                        total += ord(key) - 38
        count += 1
                    
                
print(total)
        


with open('input06.txt', 'r') as w:
    line = w.readline()
    line = line.strip('\n')
    start = 0
    distinct_characters=14
    for i in range(len(line)-distinct_characters):
        if len(set(line[start:start+distinct_characters])) == distinct_characters:
            print(start+distinct_characters)
            break
        else:
            start +=1
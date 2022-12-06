total = 0
with open('input04.txt', 'r') as w:
    for line in w:
        line = line.strip('\n')
        e1, e2 = line.split(',')
        e1s, e1e = e1.split('-')
        e2s, e2e = e2.split('-')
        e1_list = range(int(e1s), int(e1e)+1)
        e2_list = range(int(e2s), int(e2e)+1)
        
        overlap_list = {x in e1_list for x in e2_list}
        for i in overlap_list:
            if i:
                total+=1
                break
        # if(all(x in e1_list for x in e2_list)):
        #     total += 1
        # elif(all(x in e2_list for x in e1_list)):
        #     total += 1
        
print(total)
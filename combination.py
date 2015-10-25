def solve(list_num):
    s = []
    len_list = len(list_num)
    for i in range(len_list): 
        s.append([list_num[i]])
        start_idx = len(s)-1

        for j in range(len_list-1):
            sub_list = list_num[i+j+1:]
            started = False
            while sub_list:
                if started:
                    curr_idx = len(s)-1;                    
                else:
                    curr_idx = start_idx
                    started = True

                s.append([])
                new_entry = s[len(s)-1]
                for item in s[curr_idx]:
                    new_entry.append(item)
            
                new_entry.append(sub_list.pop(0))            
    return s

result = solve([1, 2, 3, 4, 5, 7])
for r in result:
    print(r)
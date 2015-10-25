def solve(list_num):
    s = []
    for item in list_num:
        s.append([item])
        sub_list = s[:len(s)-1]
        if sub_list:
            for sub_item in sub_list:
                s.append([])
                new_entry = s[len(s)-1]
                for ssub_item in sub_item:
                    new_entry.append(ssub_item)
                new_entry.append(item)
    return s

result = solve([1, 2, 3])
for r in result:
    print(r)
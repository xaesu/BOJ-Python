str = input().upper()

dic = {}
for i in str:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

max_count = max(dic.values())
most_common = [k for k, v in dic.items() if v == max_count]

if len(most_common) == 1:
    print(most_common[0])
else:
    print('?')
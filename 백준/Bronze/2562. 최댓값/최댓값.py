nums = []
for i in range(9):
    a = int(input())
    nums.append(a)
    
max_num = max(nums)
print(max_num)
print(nums.index(max_num) + 1)

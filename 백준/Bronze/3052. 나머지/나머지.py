nums = []
remain = []

for i in range(10):
    a = int(input())
    nums.append(a)
    
for i in range(10) :
    remain.append(nums[i] % 42)
    
remain = set(remain)
print(len(remain))
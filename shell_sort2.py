#shell_sort2.py
import math

def shell_sort2(nums):
    for gap in A083318(len(nums)):
        for i in range (gap, len(nums)):
            temp = nums[i]
            j = i
            while (j >= gap and temp < nums[j - gap]):
                nums[j] = nums[j - gap]
                j -= gap
            nums[j] = temp        
def A083318(n):
    seq = []
    k = math.log2(n)
    while k >= 1:
        seq.append(int(2 ** k + 1))
        k -= 1
    seq.append(1)
    return seq


# nums = [2,5,7,1,8,3] 
# shell_sort2(nums)
# print(nums)
#shell_sort3.py
import math

def shell_sort3(nums):
    for gap in A003586(len(nums)):
        for i in range (gap, len(nums)):
            temp = nums[i]
            j = i
            while (j >= gap and temp < nums[j - gap]):
                nums[j] = nums[j - gap]
                j -= gap
            nums[j] = temp        

def A003586(n):
    seq = [1]
    i, j = 0, 0
    k = 0
    while True:
        val = min(seq[i] * 2, seq[j] * 3)
        if val > n:
            break 
        seq.append(val)
        k += 1

        if val == seq[i] * 2:
            i += 1

        if val == seq[j] * 3:
            j += 1
    return seq[::-1]



# nums = [2,5,7,1,8,3] 
# shell_sort3(nums)
# print(nums)
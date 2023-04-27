#shell_sort1.py
def shell_sort1(nums):
    gap = len(nums)//2
    while (gap > 0):
        for i in range (gap, len(nums)):
            temp = nums[i]
            j = i
            while (j >= gap and temp < nums[j - gap]):
                nums[j] = nums[j - gap]
                j -= gap
            nums[j] = temp
        gap = gap//2


# nums = [2,5,7,1,8,3] 
# shell_sort1(nums)
# print(nums)
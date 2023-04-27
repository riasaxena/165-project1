# insertion_sort.py
def insertion_sort(nums):
        for i in range (1, len(nums)):
                temp = nums[i]
                j = i
                while j > 0 and nums[j - 1] > temp:
                        nums[j] = nums[j - 1]
                        j -= 1
                nums[j] = temp
# nums = [2,5,7,1,8,3] 
# insertion_sort(nums)
# print(nums)
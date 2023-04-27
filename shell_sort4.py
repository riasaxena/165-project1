#shell_sort4.py

def shell_sort4(nums):
    for gap in A033622(len(nums)):
        for i in range (gap, len(nums)):
            temp = nums[i]
            j = i
            while (j >= gap and temp < nums[j - gap]):
                nums[j] = nums[j - gap]
                j -= gap
            nums[j] = temp

def A033622(n):
    result = []
    val = 0 
    while True:
        if val%2 == 0:
            check = int(9*(2**val) - 9*(2**(val/2)) + 1)
        else:
            check = int(8*(2**val) - 6*(2**((val+1)/2)) + 1)

        print(check)
        if check > n:
            break

        result.append(check)
        val += 1
    return result[::-1]

# print(A033622(20))

# nums = [2,5,7,1,8,3] 
# shell_sort4(nums)
# print(nums)
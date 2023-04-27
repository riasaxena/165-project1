#merge_sort.py


def merge_sort(nums):
    if len(nums) > 1:

        # partition (S, n/2) -> (S1, S2) 
        middle = len(nums) // 2
        S1 = nums[:middle]
        S2 = nums[middle:]

        merge_sort(S1)
        merge_sort(S2)

        # merge(S1, S2) -> S 
        merge(nums, S1, S2)

def merge(S, S1, S2):
    i = 0
    j = 0
    while i < len(S1) and j < len(S2):
        if S1[i] < S2[j]:
            S[i+j] = S1[i]
            i+=1

        else:
            S[i+j] = S2[j]
            j +=1
    while i < len(S1):
        S[i+j] = S1[i]
        i+=1
    while j < len(S2):
        S[i+j] = S2[j]
        j+=1

# def merge_sort(nums):
#     if len(nums) > 1:
#         # partition (S, n/2) -> (S1, S2) 
#         middle = len(nums) // 2
#         S1 = merge_sort(nums[:middle])
#         S2 = merge_sort(nums[middle:])
#         # merge(S1, S2) -> S 
#         merge(nums, S1, S2)

# def merge(S, S1, S2):
#     S = []
#     i = 0
#     j = 0
#     while i < len(S1) and j < len(S2):
#         if S1[i] < S2[j]:
#             S.append(S1[i])
#             i+=1

#         else:
#             S.append(S2[j])
#             j +=1
#     S += S1[i:]
#     S += S2[j:]
#     return S

# nums = [2,5,7,1,8,3] 
# merge_sort(nums)
# print(nums)
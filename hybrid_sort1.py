#hybrid_sort1.py
from insertion_sort import insertion_sort
from merge_sort import merge
def hybrid_sort1 (nums):
    HybridMergeSort(nums, int(len(nums)**(1/2)))
def HybridMergeSort(S, H):
    n = len (S)
    if n > H:
        middle = n // 2
        S1 = S[:middle]
        S2 = S[middle:]
        HybridMergeSort(S1, H)
        HybridMergeSort(S2, H)
        merge(S, S1, S2)
    else:
        insertion_sort(S)


# Algorithm HybridMergeSort(S, H): Input array S of n
# elements
# Output array S sorted
# if n > H then
# (S1, S2) ← partition(S, n/2) HybridMergeSort(S1, H) HybridMergeSort(S2, H) S ← merge(S1, S2)
# else InsertionSort(S)

# nums = [2,5,7,1,8,3] 
# hybrid_sort1(nums)
# print(nums)
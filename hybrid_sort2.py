#hybrid_sort2.py 
from hybrid_sort1 import HybridMergeSort
def hybrid_sort2(nums):
    HybridMergeSort(nums, int(len(nums) ** (1/4)))

# nums = [2,5,7,1,8,3] 
# hybrid_sort2(nums)
# print(nums)
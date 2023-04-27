#hybrid_sort3.py 
from hybrid_sort1 import HybridMergeSort
def hybrid_sort3(nums):
    HybridMergeSort(nums, int(len(nums) ** (1/6)))

# nums = [2,5,7,1,8,3] 
# hybrid_sort3(nums)
# print(nums)
import argparse
import requirements
import random
from enum import Enum
from re import S
import time
class PermutationType(Enum):
    UNIFORMLY_DISTRIBUTED = 'random'
    REVERSE_SORTED = 'reverse'

SORTING_ALGORITHMS = {
    'insertion_sort' : requirements.insertion_sort,
}
parser = argparse.ArgumentParser(description='Benchmark several algorithms')
parser.add_argument('size', metavar = 'S', type = int, help= 'the input size for the sorting algorithm')

parser.add_argument('--permutation', choices = [e.value for e in PermutationType ], help = 'the input permutation type to be used', default = 'random')

parser.add_argument ('--algorithm', dest='algorithm_name', choices = SORTING_ALGORITHMS.keys(), help = 'the sorting algorithm to use', required = True)

args = parser.parse_args()
args.permutation = PermutationType(args.permutation)
args.algorithm = SORTING_ALGORITHMS[args.algorithm_name]

# print(args.size, type(args.size))
# print(args.permutation, type(args.permutation))
# print(args.algorithm, type(args.algorithm))


def generate_list(permutation: PermutationType, size: int) -> list[int]:
    nums = list (range (size))

    match permutation:
        case PermutationType.UNIFORMLY_DISTRIBUTED:
            random.shuffle(nums)
        case PermutationType.REVERSE_SORTED:
            nums.sort(reverse=True)
    return nums

def benchmark(permutation: PermutationType, algorithm: 'function',  size: int):
    nums =  generate_list(permutation, size)
    start_time = time.process_time()
    algorithm(nums)
    end_time = time.process_time()
    elapsed_time = end_time - start_time
    print(nums, elapsed_time)

    



if __name__ == '__main__':
    benchmark(args.permutation, args.algorithm, args.size)
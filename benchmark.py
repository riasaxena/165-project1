import argparse
from enum import Enum
import requirements
import random
import time
from pathlib import Path
import csv


DATA_DIRECTORY = Path('data')

class PermutationType(Enum):
    UNIFORMLY_DISTRIBUTED = 'random'
    REVERSE_SORTED = 'reverse'

SORTING_ALGORITHMS = {
    'insertion_sort' : requirements.insertion_sort,
    'merge_sort' : requirements.merge_sort,
    'shell_sort1': requirements.shell_sort1,
    'shell_sort2': requirements.shell_sort2,
    'shell_sort3': requirements.shell_sort3,
    'shell_sort4': requirements.shell_sort4,
    'hybrid_sort1': requirements.hybrid_sort1,
    'hybrid_sort2': requirements.hybrid_sort2,
    'hybrid_sort3': requirements.hybrid_sort3,
}

parser = argparse.ArgumentParser(description = "Benchmark several algorithms. ")

parser.add_argument('size', metavar = 'S', help = 'the input size for the sorting algorithm', type = int)
parser.add_argument('--permutation', choices = [e.value for e in PermutationType ], help = 'the input permutation type to be used', default = 'random')
parser.add_argument ('--algorithm', dest='algorithm_name', choices = SORTING_ALGORITHMS.keys(), help = 'the sorting algorithm to use', required = True)

def generate_list(permutation: PermutationType, size: int) -> list[int]:
    nums = list (range (size))
    match permutation:
        case PermutationType.UNIFORMLY_DISTRIBUTED:
            random.shuffle(nums)
        case PermutationType.REVERSE_SORTED:
            nums.sort(reverse=True)
    return nums
def get_data_path(permutation: PermutationType, algorithm_name: str) -> Path:
    directory = DATA_DIRECTORY/ algorithm_name
    directory.mkdir(parents = True, exist_ok = True)

    return(directory / permutation.value).with_suffix('.csv')

def save_data(size: int, elapsed_time: int):
    path = get_data_path(args.permutation, args.algorithm_name)
    with path.open('a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([size, elapsed_time])

def benchmark(permutation: PermutationType, algorithm: 'function',  size: int):
    nums =  generate_list(permutation, size)
    start_time = time.process_time_ns()
    algorithm(nums)
    end_time = time.process_time_ns()
    elapsed_time = end_time - start_time
    # print(nums, elapsed_time)
    save_data(size, elapsed_time)

if __name__ == '__main__':
    args = parser.parse_args()
    args.permutation = PermutationType(args.permutation)
    args.algorithm = SORTING_ALGORITHMS[args.algorithm_name]
    benchmark(args.permutation, args.algorithm, args.size)
from itertools import permutations
import matplotlib.pyplot as plt

from pathlib import Path
from collections import defaultdict

import numpy as np
import csv
from enum import Enum


class PermutationType(Enum):
    UNIFORMLY_DISTRIBUTED = 'random'
    REVERSE_SORTED = 'reverse'

DATA_DIRECTORY = Path('data')

def get_data_path(permutation:PermutationType, algorithm_name: str) -> Path:
    directory = DATA_DIRECTORY/algorithm_name
    directory.mkdir(parents = True, exist_ok = True)

    return (directory / permutation.value).with_suffix('.csv')

def load_data(algorithm_name: str, permutation:PermutationType):
    path = get_data_path(permutation, algorithm_name)
    data = defaultdict(list)
    with path.open() as csvfile:
        reader = csv.reader(csvfile)

        for row in reader:
            data[int(row[0])].append(int(row[1]))
        
    return data
def load_avg_data(algorithm_name: str, permutation: PermutationType):
    data = load_data(algorithm_name, permutation)
    sizes, avg_times = list(), list()

    for size, elapsed_time in sorted(data.items()):
        sizes.append(size)
        avg_times.append(sum(elapsed_time)/ len (elapsed_time))

    return sizes, avg_times
def add_to_plot(algorithm_name: str, permutation: PermutationType):
    sizes, avg_times = load_avg_data(algorithm_name, permutation)
    plt.loglog(sizes, avg_times, '.', basex=2, basey=2)

if __name__ == '__main___':
    add_to_plot('insertion_sort', PermutationType.UNIFORMLY_DISTRIBUTED)
    plt.show()
# print(load_data('insertion_sort', PermutationType.UNIFORMLY_DISTRIBUTED))
# print(load_avg_data('insertion_sort', PermutationType.UNIFORMLY_DISTRIBUTED))
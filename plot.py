from itertools import permutations
import matplotlib as plt

from pathlib import Path
from benchmark import PermutationType
from collections import defaultdict

import numpy as np
import csv

def get_data_path(permutation:PermutationType, algorithm_name: str) -> Path:
    directory = DATA_DIRECTORY/algorithm_name
    directory.mkdir(parents = True)

    return (directory / permutation.value).with_suffix('.csv')

def load_data(algorithm_name: str, permutation:PermutationType):
    path = get_data_path(permutation, algorithm_name)

    data = defaultdict(list)
    with path.open() as csvfile:
        reader = csv.reader(csvfile)

        for row in reader:
            data[int(row[0])].append(int(row[1]))
        
    return data

print(load_data('insertion_sort', PermutationType.UNIFORMLY_DISTRIBUTED))
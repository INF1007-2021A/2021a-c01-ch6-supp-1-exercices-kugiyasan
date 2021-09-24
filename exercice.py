#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math
import copy
import itertools
from typing import List, Optional


def get_maximums(numbers: List[List[int]]) -> List[int]:
    return [max(n) for n in numbers]


def join_integers(numbers: List[int]) -> int:
    return int("".join(str(n) for n in numbers))


def generate_prime_numbers(limit: int) -> List[int]:
    primes = []
    numbers = list(range(2, limit + 1))
    while numbers != []:
        number = numbers.pop(0)
        primes.append(number)
        numbers = [n for n in numbers if n % number != 0]

    return primes


def combine_strings_and_numbers(
    strings: List[str], num_combinations: int, excluded_multiples: Optional[int]
):
    excluded_multiples = excluded_multiples or 1
    return [
        f"{c}{n}"
        for n in range(1, num_combinations + 1, excluded_multiples)
        for c in strings
    ]


if __name__ == "__main__":
    print(get_maximums([[1, 2, 3], [6, 5, 4], [10, 11, 12], [8, 9, 7]]))
    print("")
    print(join_integers([111, 222, 333]))
    print(join_integers([69, 420]))
    print("")
    print(generate_prime_numbers(17))
    print("")
    print(combine_strings_and_numbers(["A", "B"], 2, None))
    print(combine_strings_and_numbers(["A", "B"], 5, 2))

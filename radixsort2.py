#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Date   : 2022-07-13
Purpose: Radix sort (LSD)
"""

import argparse
import sys
from collections import defaultdict
from typing import Dict, List, NamedTuple


class Args(NamedTuple):
    """ Command-line arguments """
    vals: List[int]
    debug: bool


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Radix sort (LSD)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('vals',
                        metavar='INT',
                        nargs='+',
                        type=int,
                        help='Input values')

    parser.add_argument('-d',
                        '--debug',
                        help='Print debug messages',
                        action='store_true')

    args = parser.parse_args()

    return Args(args.vals, args.debug)


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()
    print(' '.join(map(str, radixsort(args.vals, args.debug))))


# --------------------------------------------------
def radixsort(vals: List[int], debug: bool = False) -> List[int]:
    """ Radix sort """

    # Find longest number of places in numbers (most-significant digit)
    max_places = find_longest(vals)

    def warn(msg: str) -> None:
        if debug:
            print(msg, file=sys.stderr)

    # Start with least-significant digit (LSD)
    for r in range(0, max_places):
        warn(f'>>> r {r} {vals}')

        # Place each value into a bucket using the current radix position
        groups = group(r, vals)
        warn(groups)

        # Create a new list with the values of the sorted buckets
        tmp = []
        for key in mysort(list(groups.keys())):
            tmp.extend(groups[key])

        vals = tmp

    # Turn values back to integers
    return vals


# --------------------------------------------------
def find_longest(nums: List[int]) -> int:
    """ Find longest number position in a list """

    return max(map(num_places, nums))


# --------------------------------------------------
def test_find_longest() -> None:
    """ Test find_longest """

    assert find_longest([1]) == 1
    assert find_longest([12, 1]) == 2
    assert find_longest([12, 123, 1]) == 3


# --------------------------------------------------
def num_places(num: int) -> int:
    """ Find number of places in a digit """

    x = 0
    while True:
        x += 1
        if num // 10**x == 0:
            break

    return x


# --------------------------------------------------
def test_num_places() -> None:
    """ Test num_places """

    assert num_places(9) == 1
    assert num_places(99) == 2
    assert num_places(999) == 3
    assert num_places(9999) == 4


# --------------------------------------------------
def get_digit(number: int, pos: int) -> int:
    """ Get a digit at a radix position """

    return number // (10**pos) % 10


# --------------------------------------------------
def test_get_digit() -> None:
    """ Test get_digit """

    assert get_digit(103, 0) == 3
    assert get_digit(103, 1) == 0
    assert get_digit(103, 2) == 1


# --------------------------------------------------
def group(pos: int, vals: List[str]) -> Dict[str, List[str]]:
    """ Group values by radix position """

    groups = defaultdict(list)
    for val in vals:
        groups[get_digit(val, pos)].append(val)

    return groups


# --------------------------------------------------
def test_group() -> None:
    """ Test group """

    vals = [170, 45, 75, 90, 2, 802, 2, 66]

    assert group(0, vals) == {
        0: [170, 90],
        5: [45, 75],
        2: [2, 802, 2],
        6: [66]
    }

    assert group(1, vals) == {
        7: [170, 75],
        4: [45],
        9: [90],
        0: [2, 802, 2],
        6: [66]
    }

    assert group(2, vals) == {1: [170], 0: [45, 75, 90, 2, 2, 66], 8: [802]}


# --------------------------------------------------
def test_radixsort() -> None:
    """ Test radixsort """

    given = [170, 45, 75, 90, 2, 802, 2, 66]
    assert radixsort(given) == [2, 2, 45, 66, 75, 90, 170, 802]


# --------------------------------------------------
def mysort(vals: List[str]) -> List[str]:
    """ An inefficient sorter """

    for i in range(0, len(vals) - 1):
        for j in range(i + 1, len(vals)):
            cur = vals[i]
            nxt = vals[j]
            if cur > nxt:
                vals[i], vals[j] = nxt, cur

    return vals


# --------------------------------------------------
def test_mysort() -> None:
    """ Test mysort """

    given = [2, 1, 3, 6, 4]
    assert mysort(given) == [1, 2, 3, 4, 6]


# --------------------------------------------------
if __name__ == '__main__':
    main()

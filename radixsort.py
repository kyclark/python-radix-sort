#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@dnanexus.com>
Date   : 2022-07-13
Purpose: Radix sort (LSD)
"""

import argparse
from collections import defaultdict
from typing import List, NamedTuple


class Args(NamedTuple):
    """ Command-line arguments """
    vals: List[int]


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

    args = parser.parse_args()

    return Args(args.vals)


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()
    print(' '.join(map(str, radixsort(args.vals))))


# --------------------------------------------------
def radixsort(vals: List[int]) -> List[int]:
    """ Radix sort """

    # Convert values to strings
    strs = list(map(str, vals))

    # Find the longest string
    longest = max(map(len, strs))

    # Format the string versions left-padded with zeros
    strs = list(map(lambda v: f'{v:0{longest}d}', vals))

    # Start with least-significant digit (LSD)
    for r in reversed(range(0, longest)):
        print(f'>>r {r} {strs}')

        # Place each value into a bucket using the current radix position
        groups = defaultdict(list)
        for v in strs:
            groups[v[r]].append(v)
        print(groups)

        # Create a new list with the values of the sorted buckets
        tmp = []
        for key in mysort(list(groups.keys())):
            tmp.extend(groups[key])

        strs = tmp

    # Turn values back to integers
    return list(map(int, strs))


# --------------------------------------------------
def test_radixsort() -> None:
    """ Test radixsort """

    given = [170, 45, 75, 90, 2, 802, 2, 66]
    expected = [2, 2, 45, 66, 75, 90, 170, 802]
    assert radixsort(given) == expected


# --------------------------------------------------
def mysort(vals: List[str]) -> List[str]:
    """ A sorter """

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
    expected = [1, 2, 3, 4, 6]
    assert mysort(given) == expected


# --------------------------------------------------
if __name__ == '__main__':
    main()

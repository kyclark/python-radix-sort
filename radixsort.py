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
def radixsort(vals: List[int], debug: bool) -> List[int]:
    """ Radix sort """

    # Convert to padded strings, find number of places/digits
    vals = pad(vals)
    places = len(vals[0])

    def warn(msg: str) -> None:
        if debug:
            print(msg, file=sys.stderr)

    # Start with least-significant digit (LSD)
    for r in reversed(range(0, places)):
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
    return list(map(int, vals))


# --------------------------------------------------
def pad(vals: List[int]) -> List[str]:
    """ Turn list of ints into left-padded strings """

    # Convert values to strings to find the longest
    longest = max(map(len, list(map(str, vals))))

    # Format the string versions left-padded with zeros
    return list(map(lambda v: f'{v:0{longest}d}', vals))


# --------------------------------------------------
def test_pad() -> None:
    """ Test pad """

    assert pad([5]) == ['5']
    assert pad([5, 73]) == ['05', '73']

    vals = [170, 45, 75, 90, 2, 802, 2, 66]
    assert pad(vals) == [
        '170', '045', '075', '090', '002', '802', '002', '066'
    ]


# --------------------------------------------------
def group(pos: int, vals: List[str]) -> Dict[str, List[str]]:
    """ Group values by chars at a position """

    groups = defaultdict(list)
    for val in vals:
        groups[val[pos]].append(val)

    return groups


# --------------------------------------------------
def test_group() -> None:
    """ Test group """

    vals = ['170', '045', '075', '090', '002', '802', '002', '066']

    assert group(0, vals) == {
        '1': ['170'],
        '0': ['045', '075', '090', '002', '002', '066'],
        '8': ['802']
    }

    assert group(1, vals) == {
        '7': ['170', '075'],
        '4': ['045'],
        '9': ['090'],
        '0': ['002', '802', '002'],
        '6': ['066']
    }

    assert group(2, vals) == {
        '0': ['170', '090'],
        '5': ['045', '075'],
        '2': ['002', '802', '002'],
        '6': ['066']
    }


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

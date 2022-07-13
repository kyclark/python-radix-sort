#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@dnanexus.com>
Date   : 2022-07-13
Purpose: Radix sort
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
        description='Radix sort',
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
    vals = args.vals
    strs = list(map(str, vals))
    longest = max(map(len, strs))
    strs = list(map(lambda v: f'{v:0{longest}d}', vals))

    for r in reversed(range(0, longest)):
        print(f'>>r {r} {strs}')
        groups = defaultdict(list)
        for v in strs:
            groups[v[r]].append(v)

        print(groups)

        tmp = []
        for key in sorted(groups.keys()):
            tmp.extend(groups[key])

        strs = tmp

    print(f'Final: {strs}')


# --------------------------------------------------
if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@dnanexus.com>
Date   : 2022-07-14
Purpose: Rock the Casbah
"""

import argparse
import sys
from random import randint
from typing import NamedTuple, TextIO


class Args(NamedTuple):
    """ Command-line arguments """
    num: int
    outfile: TextIO


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--num',
                        help='Number of inputs',
                        metavar='int',
                        type=int,
                        default=1000)

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    args = parser.parse_args()

    return Args(args.num, args.outfile)


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()
    for num in (randint(0, 1_000_000) for _ in range(0, args.num)):
        args.outfile.write(f'{num} ')

    args.outfile.write('\n')


# --------------------------------------------------
if __name__ == '__main__':
    main()

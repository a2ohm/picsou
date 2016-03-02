#! /usr/bin/python3
# -*- coding:utf-8 -*-

import argparse
import readline

# Sub-command functions
def add(args):
    """Add a gain or a spending.
    """
    if args.spend:
        print("spend: -%.2f €" % args.spend)
    elif args.gain:
        print("gain:  +%.2f €" % args.gain)

# Parse arguments
# Create the top-level parser
parser = argparse.ArgumentParser(prog="picsou")
subparsers = parser.add_subparsers()

# Create the parser for the "add" command
parser_add = subparsers.add_parser("add",
        help="add a gain or a spending")
parser_add.set_defaults(func=add)

group_add_SG = parser_add.add_mutually_exclusive_group()
group_add_SG.add_argument('-s', '--spend', type=float,
        help="amount of the spending")
group_add_SG.add_argument('-g', '--gain', type=float,
        help="amount of the gain")

args = parser.parse_args()
args.func(args)

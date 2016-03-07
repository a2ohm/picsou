#! /usr/bin/python3
# -*- coding:utf-8 -*-

import argparse

from sub.add import add
from sub.commit import commit

# Parse arguments
# Create the top-level parser
parser = argparse.ArgumentParser(prog="picsou")
subparsers = parser.add_subparsers()

# Create the parser for the "add" command
parser_add = subparsers.add_parser("add",
        help="add a transaction")
parser_add.set_defaults(func=add)

group_add_SG = parser_add.add_mutually_exclusive_group()
group_add_SG.add_argument('-s', '--spend', type=float,
        help="amount of the spending")
group_add_SG.add_argument('-g', '--gain', type=float,
        help="amount of the gain")

# Create the parser for the "commit" command
parser_commit = subparsers.add_parser("commit",
        help="commit staging transactions")
parser_commit.set_defaults(func=commit)

args = parser.parse_args()

# Call the right module only if some some arguments are parsed
# else print the help
if vars(args):
    args.func(args)
else:
    parser.print_help()

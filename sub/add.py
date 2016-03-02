#! /usr/bin/python3
# -*- coding:utf-8 -*-

"""
Define the "add" sub-command.
"""

def add(args):
    """Add a gain or a spending in the balance sheet.
    """
    if args.spend:
        print("spend: -%.2f €" % args.spend)
    elif args.gain:
        print("gain:  +%.2f €" % args.gain)


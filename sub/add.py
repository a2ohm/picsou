#! /usr/bin/python3
# -*- coding:utf-8 -*-

"""
Define the "add" sub-command.
"""

import readline
from lib.Completer import Completer

# Define completers
valid_methods = ['cb', 'cash']
completer_method = Completer(valid_methods)

def add(args):
    """Add a gain or a spending in the balance sheet.
    """
    if args.spend:
        sum = -args.spend
        print("Add a spending of:  %.2f €" % sum)
    else:
        sum = args.gain
        print("Add a gain of:  %.2f €" % sum)

    # Get the paying method
    readline.set_completer(completer_method.complete)
    readline.parse_and_bind("tab: complete")

    method = input("\tpaying method: ")

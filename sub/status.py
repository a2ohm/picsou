#! /usr/bin/python3
# -*- coding:utf-8 -*-

"""
Define the "status" sub-command.
"""

from lib.transaction import *
from lib.color import color

import sys
import yaml

def status(conf, args):
    """Print staging transactions.
    """

    if not conf:
        # The account book is not inited
        print("There is no account book here.", end=' ')
        print("Create one with: picsou init.")
        sys.exit()

    # Print basic information
    print(color.BOLD + "%s" % conf['name'] + color.END)
    if conf['description'] != '.':
        print(color.ITALIC + "  (%s)" % conf['description'] + color.END)


    # Try to open and load the staging file
    try:
        with open("picsou.stage", 'r') as f:
            stage = yaml.load(f)

    except IOError:
        print("Nothing to commit.")
        sys.exit()

    if stage:
        if len(stage) == 1:
            print("A transaction is waiting to be comited.")
        else:
            print("Some transactions are waiting to be comited.")

        # List transactions to be commited
        transactions = \
                [transaction._make(map(t.get, transaction._fields)) 
                for t in stage]

        # Print those transactions
        print()
        printTransactions(transactions)
    else:
        print("Nothing to commit.")
        sys.exit()

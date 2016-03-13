#! /usr/bin/python3
# -*- codinf:utf-8 -*-

"""
Define the "report" sub-command.
"""

import sys

from lib.accountBook import accountBook
from lib.color import color
from datetime import date


def report(conf, args):
    """Print a report of the current month.
    """

    if not conf:
        # The account book is not inited.
        print("There is no account book there.", end=' ')
        print("Create one with: picsou init.")
        sys.exit()

    today = date.today()

    print(color.BOLD + "%s" % today.strftime("%B") + color.END)
    print("-"*49)

    with accountBook() as a:
        currentDate = ""
        sum = 0
        for t in a.getSince(today.strftime("%Y/%m/01")):
            # Print the transaction
            if t.timestamp == currentDate:
                print("%12s %-24s %+8.2f €" % (
                    '', t.payee, t.sum))
            else:
                currentDate = t.timestamp
                print("%12s %-24s %+8.2f €" % (
                    t.timestamp, t.payee, t.sum))

            # Sum transactions
            sum += t.sum

        print("-"*49)
        print("%12s %-24s %+8.2f €" % ('', 'TOTAL', sum))

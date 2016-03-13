#! /usr/bin/python3
# -*- codinf:utf-8 -*-

"""
Define the "report" sub-command.
"""

import sys

from lib.accountBook import accountBook
from lib.color import color
from datetime import date

months = ['January', 'February', 'March', 'April', 'May', 'June',
            'July', 'August', 'September', 'October', 'November',
            'December']

def report(conf, args):
    """Print a report of the current month.
    """

    if not conf:
        # The account book is not inited.
        print("There is no account book there.", end=' ')
        print("Create one with: picsou init.")
        sys.exit()

    today = date.today()
    if args.since:
        y = int(args.since[:4])
        m = int(args.since[-2:])
        while m <= today.month and y <= today.year:
            monthReport("%04d/%02d" % (y, m))
            m += 1

            if m >= 13:
                m = 1
                y += 1
    if args.payee:
        payeeReport(args.payee)
    else:
        monthReport(today.strftime("%Y/%m"))


def monthReport(month):
    """Print a month report.

    input:
        month: "%Y/%m"
    """
    
    month_nb = int(month[-2:])

    print()
    print(color.BOLD + "%s" % months[month_nb -1] + color.END)
    print("-"*49)

    with accountBook() as a:
        printTransactions(
                a.getFromTo("%s/01" % month, "%s/31" % month))


def payeeReport(payee):
    """Print a payee report.
    """

    print(color.BOLD + "%s" % payee + color.END)
    print("-"*49)

    with accountBook() as a:
        printTransactions(
                a.getFromPayee(payee))



def printTransactions(transactions):
        currentDate = ""
        sum = 0
        for t in transactions:
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

        # Print the TOTAL
        print("-"*49)
        print("%12s %-24s %+8.2f €" % ('', 'TOTAL', sum))

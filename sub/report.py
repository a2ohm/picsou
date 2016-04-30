#! /usr/bin/python3
# -*- codinf:utf-8 -*-

"""
Define the "report" sub-command.
"""

import sys

from lib.accountBook import accountBook
from lib.color import color
from lib.transaction import *

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

    # Deal with verbosity
    if args.verbose:
        verbose = True
    else:
        verbose = False

    today = date.today()
    if args.since:
        y = int(args.since[:4])
        m = int(args.since[-2:])
        while m <= today.month and y <= today.year:
            monthReport("%04d/%02d" % (y, m), verbose=verbose)
            m += 1

            if m >= 13:
                m = 1
                y += 1
    elif args.payee:
        payeeReport(args.payee, verbose=verbose)
    elif args.tag:
        tagReport(args.tag, verbose=verbose)
    else:
        monthReport(today.strftime("%Y/%m"), verbose=verbose)


def monthReport(month, verbose=False):
    """Print a month report.

    input:
        month: "%Y/%m"
    """
    
    month_nb = int(month[-2:])

    print()
    print(color.BOLD + "%s" % months[month_nb -1] + color.END)
    print("-"*54)

    with accountBook() as a:
        printTransactions(
                a.getFromTo("%s/01" % month, "%s/31" % month),
                verbose=verbose)


def payeeReport(payee, verbose = False):
    """Print a payee report.
    """

    print(color.BOLD + "%s" % payee + color.END)
    print("-"*54)

    with accountBook() as a:
        printTransactions(
                a.getFromPayee(payee),
                verbose=verbose)

def tagReport(tag, verbose):
    """Print a tag report.
    """

    print(color.BOLD + "%s" % tag + color.END)
    print("-"*54)

    with accountBook() as a:
        printTransactions(
                a.getFromTag(tag),
                verbose=verbose)


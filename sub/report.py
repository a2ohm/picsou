#! /usr/bin/python3
# -*- codinf:utf-8 -*-

"""
Define the "report" sub-command.
"""

import sys
from lib.accountBook import accountBook


def report(conf, args):
    """Print a report of the current month.
    """

    if not conf:
        # The account book is not inited.
        print("There is no account book there.", end=' ')
        print("Create one with: picsou init.")
        sys.exit()

    with accountBook() as a:
        pass

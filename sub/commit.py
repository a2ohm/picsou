#! /usr/bin/python3
# -*- coding:utf-8 -*-

"""
Define the "commit" sub-command.
"""

from lib.accountBook import accountBook
from datetime import date

import sys
import yaml

def commit(args):
    """Commit staging transactions.
    """

    # Try to open the staging file
    try:
        with open("picsou.stage", 'r') as f:
            stage = yaml.load(f)

    except IOError:
        print("Nothing to commit.")
        sys.exit()

    with accountBook() as a:
        for transaction in stage:
            a.add(transaction)

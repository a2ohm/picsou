#! /usr/bin/python3
# -*- coding:utf-8 -*-

"""
Define the "commit" sub-command.
"""

from lib.accountBook import accountBook
from lib.transaction import *
from datetime import date

import sys
import yaml

def commit(args):
    """Commit staging transactions.
    """

    # Try to open and load the staging file
    try:
        with open("picsou.stage", 'r') as f:
            stage = yaml.load(f)

    except IOError:
        print("Nothing to commit.")
        sys.exit()

    if stage:
        with accountBook() as a:
            # Add each transaction in the account book
            for i, t in enumerate(stage):
                print("\rCommit [%d/%d]" % (i+1, len(stage)), end='')

                tt = map(t.get, transaction._fields)
                a.add(transaction._make(tt))

            # Commit modifications in the database
            a.commit()
            print('\rCommit done.')

        # Reset the staging file
        with open("picsou.stage", 'w') as f:
            pass
    else:
        print("Nothing to commit.")
        sys.exit()


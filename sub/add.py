#! /usr/bin/python3
# -*- coding:utf-8 -*-

"""
Define the "add" sub-command.
"""

from lib.reinput import reinput
from lib.cinput import cinput
from lib.pinput import pinput
from lib.stager import stager
from lib.transaction import *
from lib.accountBook import accountBook

from datetime import date

import sys


def add(conf, args):
    """Add a transaction (gain or spending) in the balance sheet.
    """
    
    if not conf:
        # The account book is not inited
        print("There is no account book there.", end=' ')
        print("Create one with: picsou init.")
        sys.exit()

    # Get the list a known payees
    with accountBook() as a:
        payees = a.getPayees()

    if args.spend:
        sum = -args.spend
        print("Add a spending of:  %.2f €" % sum)
    else:
        sum = args.gain
        print("Add a gain of:  %.2f €" % sum)

    # Get the paying method
    default_method = 'cb'
    valid_methods = ['cb', 'cash']
    method = reinput("\tpaying method",
            valid = valid_methods, default = default_method,
            func=cinput, complete=valid_methods)

    # Get the date
    today = date.today().strftime("%Y/%m/%d")
    ddate = reinput("\tdate", default=today, func=pinput, pre=today)

    # Get the payee
    payee = reinput("\tpayee", func=cinput, complete=payees)

    # Get a description
    desc = reinput("\tdescription", default='.')

    # Save the transaction
    t = transaction(sum=sum, timestamp=ddate, payee=payee, desc=desc,
            method=method)
    stager().add(t)

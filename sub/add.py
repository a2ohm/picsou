#! /usr/bin/python3
# -*- coding:utf-8 -*-

"""
Define the "add" sub-command.
"""

from lib.reinput import reinput
from datetime import date

valid_methods = ['cb', 'cash', '']
default_method = 'cb'

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
    method = reinput("\tpaying method",
            valid = valid_methods, default = default_method)

    # Get the date
    today = date.today().strftime("%Y/%m/%d")
    ddate = reinput("\tdate", default=today)

    # Get the payee
    payee = reinput("\tpayee")

    # Get a description
    desc = reinput("\tdescription", default='-')

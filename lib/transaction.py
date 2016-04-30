#! /usr/bin/python3
# -*- coding:utf-8 -*-

"""
Define structures and function to manipulate transactions.
"""

from collections import namedtuple

transaction = namedtuple("transaction",
    "sum timestamp payee desc method tags")

meth = {    "cb": "CB",
            "cb_web": "CBW",
            "paypal": "P",
            "transfer": "T",
            "cash": "C",
            "cheque": "Q"}

def printTransactions(transactions, verbose=False):
        currentDate = ""
        sum = 0 

        for t in transactions:
            # Print the transaction

            # Format the payee
            if len(t.payee) >= 24:
                payee = t.payee[0:21] + '...'
            else:
                payee = t.payee

            # Format the timestamp
            # (it is only print once)
            if t.timestamp == currentDate:
                timestamp = ''
            else:
                timestamp = t.timestamp
                currentDate = t.timestamp

            # Format a suffix depending of the verbosity
            if verbose and t.tags:
                suffix = "(%s)" % t.tags
            else:
                suffix = ''

            # Print the transaction
            print("%12s %-24s %+8.2f € [%3s] %s" % ( 
                timestamp, payee, t.sum, meth[t.method], suffix))

            # For a more verbose output
            # print the description
            if verbose and t.desc:
                print("%12s  (%s)" % ('', t.desc))

            # Sum transactions
            sum += t.sum

        # Print the TOTAL
        print("-"*54)
        print("%12s %-24s %+8.2f €" % ('', 'TOTAL', sum))


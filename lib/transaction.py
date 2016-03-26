#! /usr/bin/python3
# -*- coding:utf-8 -*-

"""
Define structures and function to manipulate transactions.
"""

from collections import namedtuple

transaction = namedtuple("transaction",
    "sum timestamp payee desc method")

meth = {    "cb": "CB",
            "cash": "C"}

def printTransactions(transactions):
        currentDate = ""
        sum = 0 

        for t in transactions:
            # Print the transaction
            if t.timestamp == currentDate:
                print("%12s %-24s %+8.2f € [%s]" % ( 
                    '', t.payee, t.sum, meth[t.method]))
            else:
                currentDate = t.timestamp
                print("%12s %-24s %+8.2f € [%s]" % ( 
                    t.timestamp, t.payee, t.sum, meth[t.method]))

            # Sum transactions
            sum += t.sum

        # Print the TOTAL
        print("-"*54)
        print("%12s %-24s %+8.2f €" % ('', 'TOTAL', sum))


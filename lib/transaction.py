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

def printTransactions(transactions):
        currentDate = ""
        sum = 0 

        for t in transactions:
            # Print the transaction
            if len(t.payee) >= 24:
                payee = t.payee[0:21] + '...'
            else:
                payee = t.payee

            if t.timestamp == currentDate:
                print("%12s %-24s %+8.2f € [%s]" % ( 
                    '', payee, t.sum, meth[t.method]))
            else:
                currentDate = t.timestamp
                print("%12s %-24s %+8.2f € [%s]" % ( 
                    t.timestamp, payee, t.sum, meth[t.method]))

            # Sum transactions
            sum += t.sum

        # Print the TOTAL
        print("-"*54)
        print("%12s %-24s %+8.2f €" % ('', 'TOTAL', sum))


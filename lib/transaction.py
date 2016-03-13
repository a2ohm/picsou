#! /usr/bin/python3
# -*- coding:utf-8 -*-

"""
Define structures and function to manipulate transactions.
"""

from collections import namedtuple

transaction = namedtuple("transaction", "sum timestamp payee desc")

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


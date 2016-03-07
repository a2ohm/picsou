#! /usr/bin/python3
# -*- coding:utf-8 -*-

"""
Define a named tuple for transactions.
"""

from collections import namedtuple

transaction = namedtuple("transaction", "sum timestamp payee desc")

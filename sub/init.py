#! /usr/bin/python3
# -*- coding:utf-8 -*-

"""
Define the "init" sub-command.
"""

from lib.reinput import reinput
from lib.loadConf import loadConf

def init(args):
    """Init the account book.
    """

    # Try to open the lock file
    conf = loadConf()

    if conf:
        print("An account book already exist here: %s (%s)."
                % (conf['name'], conf['description']))

    else:
        with open(".picsou", 'w') as f:
            print("Create a new account book.")

            # Get the name of the account book
            name = reinput("\tname")

            # Get a description of the account book
            desc = reinput("\tdescription", default='.')

            # Save these information
            f.write("name: %s\n" % name)
            f.write("description: %s" % desc)

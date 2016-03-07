#! /usr/bin/python3
# -*- coding:utf-8 -*-

"""
Define the "init" sub-command.
"""

from lib.reinput import reinput
from lib.loadConf import loadConf

def init(conf, args):
    """Init the account book.
    """

    # If a lock file exists...
    if conf:
        # ... inform the user.
        print("An account book already exist here: %s (%s)."
                % (conf['name'], conf['description']))
    
    else:
        # ... else, create it.
        with open(".picsou", 'w') as f:
            print("Create a new account book.")

            # Get the name of the account book
            name = reinput("\tname")

            # Get a description of the account book
            desc = reinput("\tdescription", default='.')

            # Save these information
            f.write("name: %s\n" % name)
            f.write("description: %s" % desc)

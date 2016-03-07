#! /usr/bin/python3
# -*- coding:utf-8 -*-

"""
Load the configuration of the account book from the lock file.
"""

import yaml

def loadConf():
    try:
        with open(".picsou", 'r') as f:
            return yaml.load(f)

    except IOError:
        return None

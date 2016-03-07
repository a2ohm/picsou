#! /usr/bin/python3
# -*- coding:utf-8 -*-

import yaml

class stager():
    """Handle the stage file.

    New spending are added in a stage file. They have to be commited to
    be pulled in the database.
    """

    def __init__(self):
        pass

    def add(self, t):
        """Add a gain/spending in the stage file.
        """

        with open('picsou.stage', 'a') as f:
            f.write(' - sum: %.2f\n' % t.sum)
            f.write('   timestamp: %s\n' % t.timestamp)
            f.write('   payee: %s\n' % t.payee)
            f.write('   description: %s\n\n' % t.desc)

if __name__ == '__main__':
    s = stager()
    s.add(50, '2016', 'foo', 'bar')

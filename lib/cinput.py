#! /usr/bin/python3
# -*- coding:utf-8 -*-

"""
Input with autocompletion.
Base on sys.stdout, sys.stdin and select.
"""

import sys
import tty
import termios

def cinput(prompt = '', complete = []):
    sys.stdout.write(prompt)
    sys.stdout.flush()

    cin = ''
    buff = ''

    # Get the file descriptor of stdin
    fd = sys.stdin.fileno()
    # Save the settings of stdin
    old_settings = termios.tcgetattr(fd)

    try:
        # Switch stdin in the raw mode
        tty.setraw(sys.stdin.fileno())

        # Read stdin char by char
        reading = True
        complete_rank = 0
        while reading:
            c = sys.stdin.read(1)

            if c == '\t':
                # Complete
                opt = [x for x in complete if x.startswith(cin)]

                if opt:
                    if complete_rank >= len(opt):
                        complete_rank = 0

                    sys.stdout.write('\r')
                    sys.stdout.write(' '*(len(prompt)+len(buff)))

                    buff = opt[complete_rank]

                    sys.stdout.write('\r')
                    sys.stdout.write(prompt)
                    sys.stdout.write(buff)
                    sys.stdout.flush()

                    complete_rank += 1

            elif c == '\r':
                sys.stdout.write('\r\n')
                sys.stdout.flush()
                cin = buff
                reading = False
            else:
                sys.stdout.write(c)
                sys.stdout.flush()
                complete_rank = 0
                buff += c
                cin = buff
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    return cin

if __name__ == '__main__':
    cin = cinput("> ", ['food', 'form', 'automatique', 'automate',
        'aussitot', 'bar'])
    print("cin: %s" % cin)

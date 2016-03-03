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

    root = ''
    buff = ''
    size = 0

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
                opt = [x for x in complete if x.startswith(root)]

                if opt:
                    if complete_rank >= len(opt):
                        complete_rank = 0

                    sys.stdout.write('\r')
                    sys.stdout.write(' '*(len(prompt)+len(buff)))

                    buff = opt[complete_rank]

                    sys.stdout.write('\r')
                    sys.stdout.write(prompt)
                    sys.stdout.write(buff)

                    complete_rank += 1

            elif c == '\r':
                sys.stdout.write('\r\n')
                reading = False
            elif c == '\x7f':
                sys.stdout.write('\b \b')
                complete_rank = 0
                buff = buff[:-1]
                root = buff
            else:
                sys.stdout.write(c)
                complete_rank = 0
                buff += c
                root = buff

            sys.stdout.flush()
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    return buff

if __name__ == '__main__':
    cin = cinput("> ", ['food', 'form', 'automatique', 'automate',
        'aussitot', 'bar'])
    print("cin: %s" % cin)

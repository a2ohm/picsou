#! /usr/bin/python3
# -*- coding:utf-8 -*-

"""
Input with a pre-completed value.
"""

import sys
import tty
import termios

def pinput(prompt = '', pre = ''):
    sys.stdout.write(prompt)
    sys.stdout.write(pre)
    sys.stdout.flush()

    root = pre
    buff = pre
    size = len(pre)

    # Get the file descriptor of stdin
    fd = sys.stdin.fileno()
    # Save the settings of stdin
    old_settings = termios.tcgetattr(fd)

    try:
        # Switch stdin in the raw mode
        tty.setraw(sys.stdin.fileno())

        # Read stdin char by char
        reading = True
        while reading:
            c = sys.stdin.read(1)

            if c == '\r':
                sys.stdout.write('\r\n')
                reading = False
            elif c == '\x7f':
                sys.stdout.write('\b \b')
                buff = buff[:-1]
                root = buff
            else:
                sys.stdout.write(c)
                buff += c
                root = buff

            sys.stdout.flush()
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    return buff

if __name__ == '__main__':
    cin = pinput("> ", "2016/02/26")

    print("cin: %s" % cin)

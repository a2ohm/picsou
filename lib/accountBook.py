#! /usr/bin/python3
# -*- coding:utf-8 -*-

class accountBook():

    def __init__(self):
        pass

    def add(self, t):
        print(t)

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        pass

if __name__ == "__main__":
    pass

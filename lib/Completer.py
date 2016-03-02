#! /usr/bin/python3
# -*- coding:utf-8 -*-

class Completer:
    def __init__(self, voc):
        self.voc = voc 

    def complete(self, text, state):
        results =  [x for x in self.voc if x.startswith(text)] + [None]
        return results[state]

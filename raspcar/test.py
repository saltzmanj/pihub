#! /usr/bin/python3

from raspcar import PiSocket

p = PiSocket()
p.exec("Hello", [1, 2])
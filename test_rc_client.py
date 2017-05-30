#! /usr/bin/python3

from raspcar import PiSocket

import unittest
import json
import time
import random

class ClientUnittests(unittest.TestCase):

    def test_connection(self):
        p = PiSocket()
        t0 = time.time()

        for x in range(0, 10000):
            a = random.randint(0, 9999)
            b = random.randint(0, 9999)

            r = p.exec("pi_add", [a, b])
            self.assertEqual(r['return'], a+b)

        t1 = time.time()
        
        print(t1 - t0)

        for x in range(0, 10000):
            a = random.randint(0, 9999)
            b = random.randint(0, 9999)
            self.assertEqual(a+b, a+b)
            # r = p.exec("pi_add", [a, b])
            # self.assertEqual(r['return'], a+b)

        t2 = time.time()
        
        print(t2 - t1)


if __name__=="__main__":
    unittest.main()
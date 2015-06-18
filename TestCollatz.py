#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2015
# Glenn P. Downing
# -------------------------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io       import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, cycle_length, find_max

# -----------
# TestCollatz
# -----------

class TestCollatz (TestCase) :
    # ----
    # read
    # ----

    def test_read_1 (self) :
        s    = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)

    def test_read_2 (self) :
        s = "200 100\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 200)
        self.assertEqual(j, 100)

    def test_read_3 (self) :
        s = "-1 0\n"
        i, j = collatz_read(s)
        self.assertEqual(i, -1)
        self.assertEqual(j, 0)

    def test_read_3 (self) :
        s = "426141 571096\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 426141)
        self.assertEqual(j, 571096)

    
    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        v = collatz_eval(1, 10)
        self.assertEqual(v, 20)

    def test_eval_2 (self) :
        v = collatz_eval(634624, 516142)
        self.assertEqual(v, 509)

    def test_eval_3 (self) :
        v = collatz_eval(200, 100)
        self.assertEqual(v, 125)

    def test_eval_4 (self) :
        v = collatz_eval(1, 1000)
        self.assertEqual(v, 179)
    
    def test_eval_5 (self) :
        v = collatz_eval(527716, 631046)  
        self.assertEqual(v, 509)

    def test_eval_6 (self) :
        v = collatz_eval(1, 1)      
        self.assertEqual(v, 1)

    def test_eval_7 (self) :
        v = collatz_eval(1000, 2000)
        self.assertEqual(v, 182)
    


    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_2 (self) :
        w = StringIO()
        collatz_print(w, 0, 0, 0)
        self.assertEqual(w.getvalue(), "0 0 0\n")

    def test_print_3 (self) :
        w = StringIO()
        collatz_print(w, 1, 2, 10000)
        self.assertEqual(w.getvalue(), "1 2 10000\n")

    def test_print_4 (self) :
        w = StringIO()
        collatz_print(w, 'a', 'b', 'c')
        self.assertEqual(w.getvalue(), "a b c\n")

    # -----
    # solve
    # -----


    def test_solve_1 (self) :
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2 (self) :
        r = StringIO("1 1000\n2 1000\n3 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 1000 179\n2 1000 179\n3 1000 179\n")
    
    def test_solve_3 (self) :
        r = StringIO("3001 4000\n3001 4001\n1000 5000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "3001 4000 238\n3001 4001 238\n1000 5000 238\n")

    def test_solve_4 (self) :
        r = StringIO("356547 38536\n425767 735410\n825243 111801\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "356547 38536 443\n425767 735410 509\n825243 111801 509\n")

    def test_solve_5 (self) :
        r = StringIO("1 1000\n2 1000\n3 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 1000 179\n2 1000 179\n3 1000 179\n")

    

    # ------------
    # cycle
    # ------------
    
    def test_cycle_1 (self) :
        i = cycle_length(1)
        self.assertEqual(i, 1)

    def test_cycle_2 (self) :
        i = cycle_length(2)
        self.assertEqual(i, 2)

    def test_cycle_3 (self) :
        i = cycle_length(10)
        self.assertEqual(i, 7)


    # --------
    # max
    # --------

    def test_max_1 (self) :
        m = find_max(1, 1, 5)
        self.assertEqual(m, 5)

    def test_max_2 (self) :
        m = find_max(1000, 2000, 1)
        self.assertEqual(m, 182)

    def test_max_3 (self) :
        m = find_max(200, 100, 125)
        self.assertEqual(m, 125)

  
# ----
# main
# ----

if __name__ == "__main__" :
    main()

"""
% coverage3 run --branch TestCollatz.py >  TestCollatz.out 2>&1



% coverage3 report -m                   >> TestCollatz.out



% cat TestCollatz.out
.......
----------------------------------------------------------------------
Ran 7 tests in 0.001s

OK
Name          Stmts   Miss Branch BrMiss  Cover   Missing
---------------------------------------------------------
Collatz          18      0      6      0   100%
TestCollatz      33      1      2      1    94%   79
---------------------------------------------------------
TOTAL            51      1      8      1    97%
"""

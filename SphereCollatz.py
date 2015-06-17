#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2015
# Glenn P. Downing
# ---------------------------

import sys
cache = []
 # meta cache. has elements of max cycle length in range of
 # 1-1000, 1001-2000, 2001-3000.....99001-10000
cache2 = [179 , 182 , 217 , 238 , 215 , 236 , 262 , 252 , 247 , 
260 , 268 , 250 , 263 , 276 , 271 , 271 , 266 , 279 , 261 , 274 , 
256 , 269 , 269 , 282 , 264 , 264 , 308 , 259 , 259 , 272 , 272 , 
285 , 267 , 267 , 311 , 324 , 249 , 306 , 244 , 306 , 288 , 257 , 
288 , 270 , 270 , 314 , 283 , 314 , 296 , 296 , 278 , 309 , 340 , 
322 , 260 , 260 , 322 , 304 , 273 , 304 , 335 , 317 , 286 , 330 , 
299 , 268 , 268 , 312 , 312 , 299 , 312 , 325 , 263 , 294 , 325 , 
307 , 307 , 351 , 338 , 307 , 320 , 320 , 320 , 289 , 320 , 302 , 
302 , 333 , 333 , 315 , 315 , 333 , 315 , 284 , 315 , 328 , 297 , 
297 , 284 , 328 ]


# ------------
# collatz_read
# ------------
def collatz_read (s) :
    """
    read two ints
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    a = s.split()
    return [int(a[0]), int(a[1])]

# ------------
# collatz_eval
# ------------

def collatz_eval (i, j) :
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """
    assert i > 0
    assert j > 0
    if i < j :
        min = i
        max = j
    else :
        min = j
        max = i

    max_cycle_length = 0
    length = 0
    global cache
    global cache2
    # See if the range is in cache for 1000 range.
    minMo = min%1000
    maxMo = max%1000
    # to use the meta cache, find the start and end range that can
    # be used from meta cache 
    if max-min >=999 :
        if minMo != 1 :
            cStart = (min//1000)+1
        else :
            cStart = min//1000        
        cEnd = max//1000

        for i in range(cStart,cEnd) :
            length = cache2[i]
            if length > max_cycle_length :
                max_cycle_length = length 

        # if min is not 1, 1001, 2001
        if minMo != 1 :
            minMax = cStart*1000
            for n in range(min, minMax+1) :
                length = cycle_length(n, cache)
                if length > max_cycle_length :
                    max_cycle_length = length
        # if maxMo > 1
        if maxMo != 0 :
            maxMin = cEnd*1000+1
            for n in range(maxMin, max+1) :
                length = cycle_length(n, cache)
                if length > max_cycle_length :
                    max_cycle_length = length

        return max_cycle_length
    else :
        for n in range(min, max+1) :
            length = cycle_length(n, cache)
            if length > max_cycle_length :
                max_cycle_length = length

        return max_cycle_length


# ------------
# cycle_length
# ------------
def cycle_length (n, cache) :
    assert n > 0
    c = 1
    # check if n is already has cycle length
    #if len(cache) >= n:
    #    return cache[n-1]
    while n > 1 :
        if (n % 2) == 0 :
            n = n >> 1
        else :
            n = (3 * n) + 1
        c += 1
    #if(n > 1) :
    #    c = c -1 + cache[n-1]
    #cache.append(c)
    assert c > 0
    return c

# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    r a reader
    w a writer
    """
    for s in r :
        i, j = collatz_read(s)
        v    = collatz_eval(i, j)
        collatz_print(w, i, j, v)

# ----
# main
# ----

if __name__ == "__main__" :
    collatz_solve(sys.stdin, sys.stdout)
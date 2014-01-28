#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2014
# Glenn P. Downing
# ---------------------------
max_cycle_length_cache = []

# ------------
# collatz_read
# ------------

def collatz_read (r, a) :
    """
    reads two ints into a[0] and a[1]
    r is a  reader
    a is an array of int
    return true if that succeeds, false otherwise
    """
    s = r.readline()
    if s == "" :
        return False
    l = s.split()
    a[0] = int(l[0])
    a[1] = int(l[1])
    return True
# ------------
# collatz_eval_startLength
# ------------

def collatz_eval_startLength(i, j):
    """
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    return the start length for range [i,j]
    """
    m = j >> 1

    if i < m:
        start_length = m
    else:
        start_length = i

    assert(start_length > 0)
    return start_length

# ------------
# collatz_eval_helper
# ------------

def collatz_eval_helper (i,j):
    """
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    return the max cycle length in the range [i, j]
    """

    max_cycle_list = []
    cycle_length = 0

    for x in range(i, j):
            while x:
                if x == 1:
                    cycle_length += 1
                    assert(cycle_length > 0)
                    max_cycle_list.append(cycle_length)
                    cycle_length = 0
                    break
                elif x % 2 == 1:
                    cycle_length += 2
                    x = x + (x >> 1) + 1
                else:
                    cycle_length += 1
                    x >>= 1

    return max_cycle_list


# ------------
# collatz_eval
# ------------

def collatz_eval(i, j):
    """
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    return the max cycle length in the range [i, j] using cache
    """
    assert(i > 0)
    assert(j > 0)
    counter = None
    reduced_cache_list = []
    max_cycle_list = []

    if j < i:
        i, j = j, i

    start_length = collatz_eval_startLength(i, j)

    for a in max_cycle_length_cache:
        if (start_length < a[0]) and (start_length > a[1]):
            counter = True
            reduced_cache_list.append([a[0],a[1],a[2]])

    if counter:
        reduced_list = max(reduced_cache_list,key=lambda item: item[1] - item[0])
        max_cycle_list + reduced_list[2]
        max_cycle_list + collatz_eval_helper(i, reduced_list[0])
        max_cycle_list + collatz_eval_helper(reduced_list[1] + 1, j+1)
        v = (max(max_cycle_list))
        max_cycle_length_cache.append([i, j, v])
        assert(v > 0)
        return v

    else:
        v = (max(collatz_eval_helper(start_length, j+1)))
        max_cycle_length_cache.append([i, j, v])
        assert(v > 0)
        return v


# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    prints the values of i, j, and v
    w is a writer
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    v is the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")
  

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    read, eval, print loop
    r is a reader
    w is a writer
    """
    a = [0, 0]
    while collatz_read(r, a) :
        i, j = a
        v = collatz_eval(i, j)
        collatz_print(w, i, j, v)

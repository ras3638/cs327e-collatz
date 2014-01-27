#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2014
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------

def collatz_read (r, a) :
    """
reads two ints into a[0] and a[1]
r is a reader
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
# collatz_eval
# ------------

def collatz_eval (i, j) :
    """
i is the beginning of the range, inclusive
j is the end of the range, inclusive
return the max cycle length in the range [i, j]
"""
    assert(i > 0)
    assert(j > 0)
    if j<i:
        i,j = j,i

    max_cycle = []
    cycle_length = 0
    start_length = j>>1

    if i < start_length :
        for x in range(start_length ,j+1):
            while (x):
                if x ==1:
                    cycle_length +=1
                    max_cycle.append(cycle_length)
                    cycle_length = 0
                    break
                elif x%2 ==1:
                    cycle_length += 2
                    x = x + (x>>1) + 1
                else:
                    cycle_length += 1
                    x=x>>1
    else:
        for x in range(i,j+1):
            while (x):
                if x ==1:
                    cycle_length +=1
                    max_cycle.append(cycle_length)
                    cycle_length = 0
                    break
                elif x%2 ==1:
                    cycle_length += 2
                    x = x + (x>>1) + 1
                else:
                    cycle_length += 1
                    x=x>>1


    v = (max(max_cycle))

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
j is the end of the range, inclusive
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



# ----
# main
# ----

collatz_solve(sys.stdin, sys.stdout)
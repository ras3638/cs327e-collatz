#!/usr/bin/env python3

import sys

from Collatz import collatz_solve


def collatz_read (r, a) :

    s = r.readline()
    if s == "" :
        return False
    l = s.split()
    a[0] = int(l[0])
    a[1] = int(l[1])
    return True



def collatz_eval (i, j) :
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


def collatz_print (w, i, j, v) :

    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

def collatz_solve (r, w) :

    a = [0, 0]
    while collatz_read(r, a) :
        i, j = a
        v = collatz_eval(i, j)
        collatz_print(w, i, j, v)

collatz_solve(sys.stdin, sys.stdout)



#!/usr/bin/env python

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2011
# Glenn P. Downing
# ---------------------------

# -------
# imports
# -------

import sys

# ------------
# collatz_read
# ------------

def collatz_read (r, a) :
	"""
	reads two ints into a[0] and a[1]
	r is a  reader
	a is an array on int
	return true if that succeeds, false otherwise
	"""
	s = r.readline()
	if s == "" :
		return False
	l = s.split()
	a[0] = int(l[0])
	a[1] = int(l[1])
	assert a[0] > 0
	assert a[1] > 0
	return True

# --------------
# collatz_cycles
# --------------

def collatz_cycles (cache, cachelen, n) :
	"""
    returns the cycle length of n
    taken from assertion.py example
    """

	assert n > 0
	c = 1
	while n > 1 :
		if n < cachelen and cache[n] != 0 :
			c += cache[n] - 1
			break		
		if (n % 2) == 0 :
			n = (n / 2)
			c += 1
		else :
			n = n + (n >> 1) + 1
			c += 2
	assert c > 0
	return c

# ------------------
# collatz_cache_init
# ------------------
	"""
	high is the end of the range, inclusive
	cache
	Initializes and returns a cache by pre-setting all powers of 2
	"""

def collatz_cache_init (cachelen) :
	
	cache = [0] * cachelen	# Cache of size inclusive range
	
	twos = 1	
	twoscnt = 1
	while twos < cachelen :	# Introduce powers of two into cache
		cache[twos] = twoscnt
		twos *= 2
		twoscnt += 1		
	return cache

# ------------
# collatz_eval
# ------------

def collatz_eval (i, j) :
	"""
	i is the beginning of the range, inclusive
	j is the end       of the range, inclusive
	return the max cycle length in the range [i, j]
	"""
	assert i > 0
	assert j > 0
    
	# <your code>
	if i < j :
		low = i
		high = j
	else :
		low = j
		high = i
	v = 1

	cachelen = 100 * high 
	cache = collatz_cache_init(cachelen)

	while low < high :
		n = collatz_cycles(cache, cachelen, low)
		if cache[low] != 0 :
			assert n == cache[low]		
		else :		
			cache[low] = n	# Save cycle length
		if n > v :
			v = n
		low += 1
    
	assert v > 0
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
		v = collatz_eval(a[0], a[1])
		collatz_print(w, a[0], a[1], v)

#
# ----
# main
# ----

collatz_solve(sys.stdin, sys.stdout)        
        
        

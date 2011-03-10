#!/usr/bin/env python

# From http://projecteuler.net/index.phph?section=problems

# #2
# By considering the term int eh Fibonacci sequence whose values do not
# exceed four million, find the sum of the even-valued terms.

a = 1
b = 1

evens_sum = 0

while b <= 4000000:
    a, b = b, a + b
    if a % 2 == 0:
	evens_sum += a

print evens_sum 

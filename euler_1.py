#!/usr/bin/env python

# From http://projecteuler.net/index.phph?section=problems

# #1
# Add all the natural numbers below one thousand that are multiples of
# 3 or 5.

sum = 0

for i in xrange(0, 1000, 3):
    sum += i

for i in xrange(0, 1000, 5):
    sum += i

for i in xrange(0, 1000, 15):
    sum -= i

print sum 

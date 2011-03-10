#!/usr/bin/env python

# From http://projecteuler.net/index.phph?section=problems

# #6
# Find the difference between the sum of the squares of the first one
# hundered natural numbers and the square of the sum.

sum_squares_total = 0
squares_sum_total = 0

# second endpoint exclusive, not inclusive
for i in xrange(1,101):
    sum_squares_total += i**2 

for i in xrange(1,101):
    squares_sum_total += i 

squares_sum_total *= squares_sum_total

print squares_sum_total - sum_squares_total

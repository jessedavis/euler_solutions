#!/usr/bin/env python

# From http://projecteuler.net/index.phph?section=problems

# #20
# Find the sum of digits in 100!

total = 1         # 1!
digit_total = 0

# second endpoint exclusive, not inclusive
for i in xrange(1,101):
    total *= i

for c in str(total):
    digit_total += int(c)

print digit_total

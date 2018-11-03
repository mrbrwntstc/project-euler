"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def gcd(a, b):
  # return greatest common divisor using Euclid's algorithm (finding GCD of 3 or more numbers)
  while b:
    a, b = b, a%b
  return a

def lcm(a, b):
  # return lowest common mutiple
  return a*b // gcd(a,b)

print(reduce(lcm, range(1,20)))
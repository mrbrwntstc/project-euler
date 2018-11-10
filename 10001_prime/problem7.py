#!/usr/bin/python

import sys

# basic primality test using 6k +/- 1 optimization method
def is_prime(num):
  if num <= 1:
    return False
  elif num <= 3:
    print("%d is prime" % num)
    return True
  elif (num%2==0) or (num%3==0):
    return False
  i = 5
  while (i*i) <= num:
    j = i + 2 # catch other odd numbers
    if ((num%i)==0) or (num%j==0):
      return False
    i = i + 6
  print("%d is prime" % num)
  return True

def main(nth_prime):
  i = 0
  num = 1
  while True:
    if is_prime(num):
      i += 1
      if i == nth_prime:
        break
    num = num + 1

  print("%d prime number is %d" % (nth_prime, num))

if __name__ == '__main__':
  main(int(sys.argv[1]))
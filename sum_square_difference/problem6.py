#!/usr/bin/python

import sys

def main(num):
  sum_of_squares = sum(x**2 for x in range(1, num+1))
  square_of_sums = sum(x for x in range(1,num+1))**2

  print("%d - %d = %d" % (square_of_sums, sum_of_squares, (square_of_sums - sum_of_squares)))

if __name__ == '__main__':
  main(int(sys.argv[1]))
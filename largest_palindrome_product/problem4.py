"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91*99

Find the largest palindrome made from the product of two 3-digit numbers.
"""
largest = 0
for x in range(100,1000):
  for y in range(x,1000):
    num = x*y
    if num > largest:
      num_array = [int(i) for i in str(num)]
      if num_array == num_array[::-1]:
        print("New largest palindrome is %d" % num)
        largest = num

print("Largest palindrome product from 2 3-digit numbers is %d" % largest)
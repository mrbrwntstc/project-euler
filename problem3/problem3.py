"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

magic_number = 600851475143

# if it's divisible by any even number, it's also divisible by 2
while magic_number % 2 == 0:
  magic_number /= 2
  print("magic_number is now %d" % magic_number)

# now, handle all of the odd numbers
i = 3
while i < magic_number:
  while magic_number%i == 0:
    magic_number /= i
    print("magic_number is %d, i is %d" % (magic_number, i))
  i += 1

print("Largest prime factor of 600851475143 is %d " % magic_number)
# Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. No floats or non-positive integers will be passed.
# For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.
import math

def sum_two_smallest_numbers(*args):  # allowing to insert as many numbers I need
  mylist = list(args)                   # transforming tuple to list
  mylist.sort()                         # sorting list
  return mylist[0] + mylist[1]          # sum of 2 lowest integeers


print(sum_two_smallest_numbers(444,123,1,4,5))   # test

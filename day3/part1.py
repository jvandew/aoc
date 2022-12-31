# coding=utf-8

from math import ceil, sqrt
from os import path

def odd_ceil(num):
  '''
  Like ceil, but rounds up to the next odd number.
  '''
  rounded = ceil(num)
  if rounded % 2 == 1:
    return rounded
  else:
    return rounded + 1

def main():
  '''
  NOTE(jacob): There is a bit of magic math happening here, which I derived by staring at
      this square for a while.

      37  36  35  34  33  32  31
      38  17  16  15  14  13  30
      39  18   5   4   3  12  29
      40  19   6   1   2  11  28   .
      41  20   7   8   9  10  27   .
      42  21  22  23  24  25  26   .
      43  44  45  46  47  48  49  50

      This formula could probably be proven by induction, but I will not do that here.
  '''

  with open(path.join('day3', 'input'), 'r') as input_file:
    target = int(input_file.readline().strip())

    if target == 1:
      return 0

    square_size = odd_ceil(sqrt(target))
    side_length = square_size - 1
    square_offset = (square_size ** 2) - target

    side_offset = square_offset % side_length
    min_distance = side_length / 2

    distance = int(min_distance + abs(side_offset - min_distance))
    print(distance)

if __name__ == '__main__':
  main()

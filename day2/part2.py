# coding=utf-8

from os import path

def main():
  with open(path.join('day2', 'input'), 'r') as input_file:
    checksum = 0
    # TODO(jacob): There's probably a better than O(m*n^2) solution to this?
    for row in input_file:
      seq = [float(num) for num in row.strip().split('\t')]
      seq.sort(reverse=True)

      found = False
      for i in range(len(seq) - 1):
        for j in range(i + 1, len(seq)):
          quotient = seq[i] / seq[j]
          floored_quotient = int(quotient)
          if floored_quotient == quotient:
            checksum += floored_quotient
            found = True
            break

        if found:
          break

    print(checksum)

if __name__ == '__main__':
  main()

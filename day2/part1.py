# coding=utf-8

from os import path

def main():
  with open(path.join('day2', 'input'), 'r') as input_file:
    checksum = 0
    for row in input_file:
      seq = [int(num) for num in row.strip().split('\t')]
      checksum += max(seq) - min(seq)

    print(checksum)

if __name__ == '__main__':
  main()

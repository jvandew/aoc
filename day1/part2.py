# coding=utf-8

from os import path

def main():
  with open(path.join('day1', 'input'), 'r') as input_file:
    seq = input_file.readline().strip()
    offset = len(seq) / 2
    sum = 0
    for i in range(len(seq)):
      if seq[i] == seq[i - offset]:
        sum += int(seq[i])

    print(sum)

if __name__ == '__main__':
  main()

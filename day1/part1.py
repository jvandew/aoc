# coding=utf-8

from os import path

def main():
  with open(path.join('day1', 'input'), 'r') as input_file:
    seq = input_file.readline().strip()
    sum = 0
    for i in range(len(seq)):
      if seq[i] == seq[i-1]:
        sum += int(seq[i])

    print(sum)

if __name__ == '__main__':
  main()

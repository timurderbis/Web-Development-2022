import math


def A():
  a = int(input())
  b = int(input())
  print(math.sqrt(a * a + b * b))


def B():
  x = int(input())

  print('The next number for the number {} is {}.'.format(x, x + 1))
  print('The previous number for the number {} is {}.'.format(x, x - 1))


def C():
  n = int(input())
  k = int(input())

  print(int(k / n))


def D():
  n = int(input())
  k = int(input())

  print(int(k % n))


def E():
  v = int(input())
  t = int(input())

  print((v*t) % 109)

E()

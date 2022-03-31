import math

def A():
  a = int(input())
  b = int(input())
  for x in range(a, b + 1):
    if x % 2 == 0:
      print(x)

def B():
  a = int(input())
  b = int(input())
  c = int(input())
  d = int(input())
  for x in range(a, b + 1):
    if x % d == c:
      print(x)

def C():
  a = int(input())
  b = int(input())
  for i in range(a, b + 1):
    j = int(math.sqrt(i))
    if j * j == i:
      print(i)

# def D():
#
#
# def E():
#
#
# def F():


def G():
  import math
  a = int(input())
  for x in range(2, int(math.sqrt(a)) + 1):
    if a % x == 0:
      print(x)
      break
  else:
    print(a)

def H():
  a = int(input())
  for x in range(1, a + 1):
    if a % x == 0:
      print(x)

def I():
  a = int(input())
  b = 0
  for x in range(1, int(math.sqrt(a))):
    if a % x == 0:
      b += 2
  с = int(math.sqrt(a))
  с *= с
  if с == a:
    b += 1
  print(b)

def J():
  a = 0
  for x in range(1, 101):
    b = int(input())
    a += b
  print(a)

def K():
  n = int(input())
  a = 0
  for i in range(1, n + 1):
    b = int(input())
    a += b
  print(a)

# def L():


def M():
  n = int(input())
  a = 0
  for i in range(1, n + 1):
    b = int(input())
    if b == 0:
      a += 1
  print(a)

M()

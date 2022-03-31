def A():
  a = int(input())
  b = int(input())

  if (a >= b):
    print(a)
  else:
    print(b)


def B():
  year = int(input())

  if (year % 4 == 0 and year % 100 != 0):
    print('YES')
  elif (year % 400 == 0):
    print('YES')
  else:
    print('NO')

def C():
  a = int(input())
  b = int(input())
  if b == 1 and a == 1:
    print('YES')
  elif a != 1 and b != 1:
    print('YES')
  else:
    print('NO')

def D():
  a = int(input())
  if a > 0:
    print(1)
  elif a < 0:
    print(-1)
  else:
    print(0)

def E():
  a = int(input())
  b = int(input())
  if a > b:
    print(1)
  elif a < b:
    print(2)
  else:
    print(0)


E()

def A():
  n = int(input())
  arr = [int(i) for i in input().split()]

  for x in range(n):
    if x % 2 == 0:
      print(arr[x], end=' ')

def B():
  n = int(input())
  arr = [int(i) for i in input().split()]

  for x in range(n):
    if arr[x] % 2 == 0:
      print(arr[x], end=' ')

def C():
  n = int(input())
  arr = [int(i) for i in input().split()]
  k = 0
  for x in arr:
    if x > 0:
      k += 1
  print(k)

def D():
  n = int(input())
  k = 0
  arr = [int(i) for i in input().split()]
  for x in range(1, n):
    if arr[x] > arr[x - 1]:
      k += 1

  print(k)

def E():
  n = int(input())
  arr = [int(i) for i in input().split()]
  for x in range(1, n):
    if arr[x] > 0 and arr[x - 1] > 0:
      print('YES')
      break
    elif arr[x] < 0 and arr[x - 1] < 0:
      print('YES')
      break
  else:
    print('NO')

def F():
  n = int(input())
  arr = [int(i) for i in input().split()]
  k = 0
  for x in range(1, n - 1):
    if arr[x] > arr[x - 1] and arr[x] > arr[x + 1]:
      k += 1
  print(k)

def G():
  n = int(input())
  arr = [int(i) for i in input().split()]
  i = 1
  for x in range(0, int(n / 2)):
    c = arr[x]
    arr[x] = arr[n - i]
    arr[n - i] = c
    i += 1
  for x in arr:
    print(x)

G()

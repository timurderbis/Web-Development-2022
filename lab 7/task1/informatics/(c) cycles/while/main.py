def A():
  n = int(input())
  i = 1
  while i * i <= n:
    print(i * i)
    i += 1

def B():
  a = int(input())
  i = a
  nod = a
  while i > 1:
    if a % i == 0:
      nod = i
    i -= 1
  print(nod)

def C():
  n = int(input())
  pow2 = 1
  while pow2 <= n:
    print(pow2)
    pow2 *= 2

def D():
  n = int(input())
  pow2 = 1
  while pow2 < n:
    pow2 *= 2
  if pow2 == n:
    print('YES')
  else:
    print('NO')

def E():
  n = int(input())
  pow2 = 1
  a = 0
  while pow2 <= n:
    if pow2 == n:
      break
    else:
      pow2 *= 2
      a += 1
  print(a)

E()

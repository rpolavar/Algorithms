from math import *

def factorial(n):
 if n <= 1:
  return 1
 return factorialInternal(n, 1)

def factorialInternal(n, resultSoFar):
 if n<= 1:
  return resultSoFar
 return factorialInternal(n-1, resultSoFar*n)

ms = 1000000
times = []
times.append(ms * 1)
times.append(times[-1] * 60)
times.append(times[-1] * 60)
times.append(times[-1] * 24)
times.append(times[-1] * 30)
times.append(times[3] * 365)
times.append(times[3] * 365 * 100 + 25)

fs = []
fs.append(lambda n: log(n,2))
fs.append(lambda n: sqrt(n))
fs.append(lambda n: n)
fs.append(lambda n: n*log(n,2))
fs.append(lambda n: n**2)
fs.append(lambda n: n**3)
fs.append(lambda n: 2**n)
fs.append(lambda n: factorial(n))

def approximate(n, f):
 prev = 0
 current = 1
 while n > f(current):
  prev = current
  current *= 2
 if f(current) == n:
  return current
 low = prev
 high = current
 while abs(high - low) > 1:
  current = (low + high)/2
  if f(current) > n:
   high = current
  else:
   low = current  
 return current

for f in fs:
 for t in times:
  print( approximate(t, f), end = ' ')
 print()


#fibonacci series 0 1 1 2 3 5 8
                 #0 1 2 3 4 5 6
'''
fib(0) = 0
fib(1) = 1
fib(2) = fib(0) + fib(1)
fib(3) = fib(1) + fib(2)
fib(4) = fib(3) + fib(2)
'''
'''
def fib(n):
 if (n==0 or n==1):
  return n
 return fib(n-1) + fib(n-2)
print(fib(6))
'''
#factorial
n = int(input())
def fact(n):
 if n==1:
  return 1
 return n * fact(n-1)
print(fact(n)) 
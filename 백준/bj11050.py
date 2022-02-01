'''
(a+b)^n 전개하면 a^r * b^(n-r)
이항계수는?
# (n)   n!
#       _______
# (r) = r!(n-r)!
'''
import math

N,K = map(int,input().split())

print(math.factorial(N)//(math.factorial(K) * math.factorial(N-K)))

import math

"""
comb(n, k)
factorial(n)
gcd(*integers)
isqrt(n)
lcm(*integers)
perm(n, k)
"""

# Number of ways to choose k items from n items without repetitions and without order
n = 6
k = 2

res1 = math.comb(n, k)
print(f"The number of ways to choose {k} items from {n} items is {res1}")

# Number of ways to choose k items from n items without repetition and with order
res1_1 = math.perm(n, k)
print(f"The number of ways to choose {k} items from {n} items with order is {res1_1}")


# n factorial

a1 = 5
a2 = 6
a3 = 7

res2 = math.factorial(a1)
res3 = math.factorial(a2)
res4 = math.factorial(a3)

print(f" {a1}! = {res2}; {a2}! = {res3}; {a3}! = {res4}")

# Greatest common divisor of the integer arguments

a, b, c = 4, 8, 12

res5 = math.gcd(a, b, c)
print(f"The GDC of {a}, {b}, {c} is {res5}")

# Least common multiple of the integer arguments
res6 = math.lcm(a, b, c)
print(f"The LCM of {a}, {b}, {c} is {res6}")

# Integer square root of a nonnegative integer n

n = 4096

res7 = math.isqrt(n)
print(f"The integer square root of {n} is {res7}")


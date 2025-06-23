import math


# Euclidean distance and norm

p = [1, 1]
q = [2, 2]
dist = math.dist(p, q)

a = 3
b = 4
hypot = math.hypot(a, b)

print(f"Distance from {p} to {q} is {dist}")
print(f"The h of c {a} and {b} is {hypot}")




# Sum of values and sum of products

iterable = [2, 4, 6, 8]
subject1 = [9.7, 72]
subject2 = [8.9, 60]

fsum = math.fsum(iterable)
prod = math.prod(iterable)
sumprod = math.sumprod(subject1, subject2)

print(f"Sum of values - {iterable} = {fsum}")
print(f"Product of elements - {iterable} = {prod}")
print(f"The sum of products from {subject1} and {subject2} is {sumprod}")

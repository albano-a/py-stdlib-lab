import math

z = 3

exp = math.exp(z)  # e ** x
exp2 = math.exp2(z)  # 2 ** x
expm1 = math.expm1(z)  # e**x - 1

print(f"e^{z} = {exp}; 2^{z} = {exp2} ; e^{z} - 1 = {expm1}")

a = 5
b = 500
c = 5000

ln = math.log(a)  # ln(10)
log = math.log(b, a)  # log base 10
log1p = math.log1p(a)  # log(1 + x)
log2 = math.log2(a)  # log base 2
log10 = math.log10(c)  # log base 10

print(f"The ln of 10 is {ln:.4f}")
print(f"log base {a} of {b} is {log:.4f}")
print(f"log(1 + {a}) = {log1p:.4f}")
print(f"log base 2 of {a} is {log2:.4f}")
print(f"log base 10 of {a} is {log10:.4f}")


a, b, c = 4, 6, 8

pow = math.pow(b, a)
sqrt = math.sqrt(a)
cbrt = math.cbrt(c)

print(
    f"{b} to the power of {a} is {pow}; sqrt of {a} is {sqrt} ; cbrt of {c} is {cbrt}"
)

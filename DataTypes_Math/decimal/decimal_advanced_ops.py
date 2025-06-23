from decimal import Decimal, getcontext

getcontext().prec = 10

# Exponentiation with fractional powers
exp1 = Decimal("9") ** Decimal("0.5")  # square root
exp2 = Decimal("27") ** (Decimal("1") / Decimal("3"))  # cube root

# Quantize (rounding to fixed decimal places)
q1 = Decimal("3.14159").quantize(Decimal("0.01"))  # -> 3.14
q2 = Decimal("2.71828").quantize(Decimal("0.000"))  # -> 2.718

# Normalize (remove trailing zeros)
n1 = Decimal("5.60000").normalize()
n2 = Decimal("0.00050000").normalize()

# Scaleb (shift decimal point)
s1 = Decimal("1.23").scaleb(2)  # -> 123
s2 = Decimal("123").scaleb(-2)  # -> 1.23

# FMA (fused multiply-add: (x * y) + z)
fma1 = Decimal("2").fma(Decimal("3"), Decimal("4"))  # -> 10

# Copy sign
cs1 = Decimal("5").copy_sign(Decimal("-1"))  # -> -5

# Output
print("Exponentiation:", exp1, exp2)
print("Quantize:", q1, q2)
print("Normalize:", n1, n2)
print("Scaleb:", s1, s2)
print("FMA:", fma1)
print("Copy sign:", cs1)

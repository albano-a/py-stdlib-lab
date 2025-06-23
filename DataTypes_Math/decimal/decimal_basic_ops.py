from decimal import Decimal, getcontext

# Returns the current context for the active thread
print(getcontext())
getcontext().prec = 7  # Set a new precision

# Decimal creation from strings, integers, floats
d1 = Decimal("0.1")
d2 = Decimal("0.2")
d3 = Decimal(3)
d4 = Decimal(0.3)  # float input (inaccurate)

add1 = d1 + d2
sub1 = d2 - d1
mul1 = d1 * d3
div1 = d1 / d2
mod1 = d1 % d2
floordiv1 = d1 // d2
pow1 = d1 ** 3

print(f"{d1} + {d2} = {add1}")
print(f"{d1} - {d2} = {sub1}")
print(f"{d1} * {d3} = {mul1}")
print(f"{d1} / {d2} = {div1}")
print(f"{d1} % {d2} = {mod1}")
print(f"{d1} // {d2} = {floordiv1}")
print(f"{d1} ** {3} = {pow1}")
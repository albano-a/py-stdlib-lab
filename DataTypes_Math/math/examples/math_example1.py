import math

# Final amount with compounding interest
P = 1000
r = 0.05
t = 10
A = P * math.exp(r * t)

print(
    f"The final amount after {t} years with a principal of ${P}, an interest rate of {r*100}%, and continuous compounding is: ${A:.2f}"
)

from decimal import getcontext, Decimal

# Inspect current global context
ctx = getcontext()
print("Default precision:", ctx.prec)
print("Default rounding:", ctx.rounding)

# Set custom precision
ctx.prec = 10
ctx.rounding = 'ROUND_HALF_UP'

# Apply with operations
a = Decimal('1.123456789')
b = Decimal('2.987654321')
result = a / b

print("Custom precision result:", result)

# Show other context attributes
print("Emin:", ctx.Emin)
print("Emax:", ctx.Emax)
print("Capitals:", ctx.capitals)
print("Flags:", ctx.flags)
print("Traps:", ctx.traps)

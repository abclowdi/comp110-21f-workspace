"""Numeric operators."""

__author__ = 730390434

lhs: int = int(input("Left-hand side: "))
rhs: int = int(input("Right-hand side: "))

exponent: int = int(lhs ** (rhs))
print(str(lhs) + " ** " + str(rhs) + " is " + str(exponent))

division: float = float((lhs) / (rhs))
print(str(lhs) + " / " + str(rhs) + " is " + str(division))

integer_division: int = int(lhs) // (rhs)
print(str(lhs) + " // " + str(rhs) + " is " + str(integer_division))

remainder: int = int(lhs) % (rhs)
print(str(lhs) + " % " + str(rhs) + " is " + str(remainder))
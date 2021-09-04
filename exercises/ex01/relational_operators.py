"""Relational operators."""

__author__ = "730390434"

lhs: int = int(input("Left-hand side: "))
rhs: int = int(input("Right-hand side: "))

less_than: bool = bool((lhs) < (rhs))
print(str(lhs) + " < " + str(rhs) + " is " + str(less_than))

greater_than_or_equal_to: bool = bool((lhs) >= (rhs))
print(str(lhs) + " >= " + str(rhs) + " is " + str(greater_than_or_equal_to))

equal_to: bool = bool((lhs) == (rhs))
print(str(lhs) + " == " + str(rhs) + " is " + str(equal_to))

not_equal_to: bool = bool((lhs) != (rhs))
print(str(lhs) + " != " + str(rhs) + " is " + str(not_equal_to))
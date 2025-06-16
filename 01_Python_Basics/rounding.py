# Rounding in Python means adjusting a number to its nearest whole number or to a specific number of decimal places.
# round() function is used to round a number.
# Example: round(3.6) → 4, round(3.14159, 2) → 3.14

#  Syntax: round(number, ndigits)

print(round(3.6)) # Output: 4
print(round(3.4)) # Output: 3
print(round(3.5)) # Output: 4
print(round(3.14159, 2)) # Output: 3.14
print(round(2.675, 2)) # Output: 2.67 (due to floating-point representation issues)

# Note: Rounding behavior python follows the "round half to even" strategy, also known as "bankers' rounding".
# This means that when the number is exactly halfway between two integers, it rounds to the nearest even integer.
# Example of rounding half to even
print(round(2.5))  # Output: 2 (even)
print(round(3.5))  # Output: 4 (even) 
# Example of rounding with negative ndigits
print(round(123.4567, -2))  # Output: 100 (rounds to the nearest hundred)
# Example of rounding with negative ndigits
print(round(123.4567, -1))  # Output: 120 (rounds to the nearest ten)
# Example of rounding with negative ndigits
print(round(123.4567, -3))  # Output: 0 (rounds to the nearest thousand)
# Example of rounding with negative numbers
print(round(-2.5567,2))  # Output: -2.56 (rounds to two decimal places)

import math
# Using math.ceil() and math.floor() for rounding
print(math.ceil(3.4))  # Output: 4 (rounds up to the nearest integer)
print(math.floor(3.6))  # Output: 3 (rounds down to the nearest integer)
# Using math.trunc() to truncate the decimal part
print(math.trunc(3.945))  # Output: 3 (removes the decimal part without rounding)
# Using math.isclose() to compare floating-point numbers
print(math.isclose(0.1 + 0.2, 0.3))  # Output: True (checks if two floating-point numbers are close to each other)
# Using math.fsum() for precise floating-point summation
print(math.fsum([0.1, 0.2, 0.3]))  # Output: 0.6 (more accurate than sum due to floating-point precision)



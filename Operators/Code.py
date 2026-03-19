# --------------------------------Page 1------------------------

a = 12
b = 5

# Addition (+)
print("Addition:", a + b)        # Output: 17

# Subtraction (-)
print("Subtraction:", a - b)     # Output: 7

# Multiplication (*)
print("Multiplication:", a * b)  # Output: 60

# Division (/) - Always returns a float
print("Division:", a / b)        # Output: 2.4

# Floor Division (//) - Rounds down to the nearest whole number
print("Floor Division:", a // b) # Output: 2

# Modulus (%) - Returns the remainder of the division
print("Modulus:", a % b)         # Output: 2 (because 12 divided by 5 leaves a remainder of 2)

# Exponentiation (**) - a to the power of b
print("Exponentiation:", a ** b) # Output: 248832



# -----------------------Page 2-------------------------

# Basic Assignment
x = 10 
print("Initial x:", x)

# Compound Addition (+=) is the same as x = x + 5
x += 5  
print("After += 5:", x) # Output: 15

# Compound Subtraction (-=) is the same as x = x - 3
x -= 3
print("After -= 3:", x) # Output: 12

# Compound Multiplication (*=) is the same as x = x * 2
x *= 2
print("After *= 2:", x) # Output: 24

# Compound Division (/=) is the same as x = x / 4
x /= 4
print("After /= 4:", x) # Output: 6.0


# -----------------------------Page 3----------------------------

x = 10
y = 20

print("Is x equal to y?", x == y)                  # Output: False
print("Is x not equal to y?", x != y)              # Output: True
print("Is x greater than y?", x > y)               # Output: False
print("Is x less than y?", x < y)                  # Output: True
print("Is x greater than or equal to 10?", x >= 10)# Output: True
print("Is y less than or equal to 15?", y <= 15)   # Output: False

# String Comparison Example
# 'a' comes before 'b' in the alphabet (ASCII), so 'apple' is considered "less than" 'banana'
print("Is apple < banana?", "apple" < "banana")    # Output: True

# -------------------------Page 4---------------------------


a = 5

# 'and' example: Is 'a' greater than 3 AND less than 10?
print(a > 3 and a < 10)  # Output: True (Both conditions are met)

# 'or' example: Is 'a' greater than 10 OR less than 6?
print(a > 10 or a < 6)   # Output: True (The second condition is met)

# 'not' example: Reverse the result of the 'and' statement above
print(not(a > 3 and a < 10)) # Output: False



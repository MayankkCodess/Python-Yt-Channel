# SYNTAX ERROR EXAMPLE (Will not run)
# print("Hello World"  <-- Missing closing parenthesis

# INDENTATION ERROR EXAMPLE (Will not run)
# def func():
# print("Hello")       <-- Needs to be indented!



print("Start of program")

# This is mathematically impossible and raises a 'ZeroDivisionError'
result = 10 / 0 

# The program crashes on the line above, so this line NEVER prints.
print("End of program")


try:
    print("1. Trying to do some math...")
    # Change '0' to '2' to see the 'else' block run instead of 'except'!
    result = 10 / 0 
    
except ZeroDivisionError:
    # This runs because we hit a ZeroDivisionError
    print("2. Oops! You cannot divide by zero. We caught the error!")

else:
    # This ONLY runs if the 'try' block was 100% successful
    print(f"2. Success! The result is {result}")

finally:
    # This ALWAYS runs, period.
    print("3. Finally block: Cleaning up and moving on.")

print("4. Program finished naturally (It didn't crash!)")



def check_age(age):
    if age < 0:
        # We manually throw an exception here
        raise ValueError("Age cannot be a negative number!")
    else:
        print("Age is valid.")

# Calling the function with a bad value to see our custom error
check_age(-5)
# Defining a simple function
def say_hello():
    print("Hello, welcome to Python!")
    print("Learning functions is fun.")

# Calling the function (You can do this as many times as you want!)
say_hello()
say_hello()


# Here, 'user_name' is the PARAMETER (the placeholder)
def greet(user_name): 
    print(f"Hello, {user_name}!")

# Here, "Alice" and "Bob" are the ARGUMENTS (the actual values)
greet("Alice") 
greet("Bob")


def add_numbers(a, b):
    return a + b

# 3 goes to 'a', 5 goes to 'b'. They are assigned based on their position.
result = add_numbers(3, 5) 
print("Positional result:", result)


def introduce(name, age):
    print(f"I am {name} and I am {age} years old.")

# Even though 'age' is second in the definition, we can pass it first 
# by using the keyword 'age='
introduce(age=25, name="John")



# "Guest" is the default value for 'name'
def welcome(name="Guest"):
    print(f"Welcome to the party, {name}!")

# We provide an argument, so it uses "Sarah"
welcome("Sarah") 

# We don't provide an argument, so it falls back to the default "Guest"
welcome()
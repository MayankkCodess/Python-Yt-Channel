# Create a dictionary
student = {"name": "John", "age": 20, "grade": "A"}

# READ: Accessing a value using its key
print(student["name"])  # Output: John

# UPDATE: Changing an existing value
student["age"] = 21 

# CREATE: Adding a brand new key-value pair
student["city"] = "New York"

# DELETE: Removing a key-value pair using the 'del' keyword
del student["grade"]

print(student) 
# Output: {'name': 'John', 'age': 21, 'city': 'New York'}





numbers = {1: 10, 2: 20, 3: 30, 4: 40}

# Method 1: The way shown in your slide
for i in numbers:
    # 'i' is the key, 'numbers[i]' is the value
    print(i, ":", numbers[i]) 

print("-" * 15)

# Method 2: The more "Pythonic" way using .items()
# This grabs both the key and the value at the same time!
for key, value in numbers.items():
    print(f"{key} : {value}")



user = {"username": "coder123", "score": 95}

# .keys() -> Returns a view of just the keys
print(user.keys())     # dict_keys(['username', 'score'])

# .values() -> Returns a view of just the values
print(user.values())   # dict_values(['coder123', 95])

# .get() -> Safely gets a value. Prevents errors if the key doesn't exist!
print(user.get("score"))       # Output: 95
print(user.get("level", 1))    # Output: 1 (Returns default '1' because 'level' isn't there)

# .pop() -> Removes a specific key and returns its value
score = user.pop("score")
# Creating a heterogeneous tuple with duplicates
my_tuple = (10, "Python", True, 10, 3.14)

print("Original Tuple:", my_tuple)

# Accessing an element by its index (Ordered)
print("Element at index 1:", my_tuple[1])  # Output: Python

# PROVING IMMUTABILITY: 
# If you try to run the line below, Python will throw a TypeError!
# my_tuple[1] = "Java"  <-- THIS WILL CRASH YOUR PROGRAM



colors = ("red", "green", "blue")

# Method 1: Iterating directly over the items
print("Direct Iteration:")
for color in colors:
    print(color)

print("-" * 15)

# Method 2: Iterating using Index values
print("Index Iteration:")
for i in range(len(colors)):
    print(f"Index {i}: {colors[i]}")



# Initial tuple
t = (5, 2, 9, 1, 5, 6)
print("Tuple:", t)

# 1. Using count()
# How many times does the number '5' appear?
count_5 = t.count(5)
print(f"The number 5 appears {count_5} times.")

# 2. Using index()
# At what index position is the number '9' located?
index_9 = t.index(9)
print(f"The number 9 is located at index {index_9}.")
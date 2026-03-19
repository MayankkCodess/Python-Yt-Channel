# A heterogeneous list with duplicates
my_list = [10, "apple", True, 10, 3.14]
print(my_list)



# Define a list
numbers = [10, 20, 30, 40]
print("Original list:", numbers)

# Accessing an element (Slicing also works exactly like strings: numbers[1:3])
print("Element at index 1:", numbers[1]) # Output: 20

# Mutating (Changing) the value at index 1
numbers[1] = 99
print("Updated list:", numbers) # Output: [10, 99, 30, 40]



fruits = ["apple", "banana", "cherry"]

# Method 1: Iterating directly (The Pythonic Way)
for fruit in fruits:
    print(fruit)

print("-" * 15)

# Method 2: Iterating using Index values and range()
for i in range(len(fruits)):
    print(f"Index {i} holds: {fruits[i]}")




numbers = [5, 2, 9, 1, 5, 6]
print("Initial:", numbers)

# --- ADDING ELEMENTS ---
numbers.append(10)        # Adds 10 to the very end
numbers.insert(2, 15)     # Inserts 15 specifically at index 2 (pushes others back)
numbers.extend([20, 30])  # Merges another list onto the end

# --- REMOVING ELEMENTS ---
numbers.remove(5)         # Removes the FIRST occurrence of the value 5
popped = numbers.pop(3)   # Removes AND returns the element at index 3

# --- FINDING & COUNTING ---
idx = numbers.index(6)    # Finds the index position of the value 6
count_5 = numbers.count(5)# Counts how many times 5 appears in the list

# --- REORGANIZING ---
numbers.sort()            # Sorts the list in ascending order (modifies original)
numbers.reverse()         # Reverses the current order of the list

# --- COPYING & CLEARING ---
new_numbers = numbers.copy() # Creates a separate, independent copy of the list
numbers.clear()              # Empties the list completely: []
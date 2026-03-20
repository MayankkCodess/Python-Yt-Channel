# Creating a set with duplicates and mixed types
my_set = {1, 2, 2, 3, "apple", (4, 5)}

# Notice the duplicate '2' is automatically removed!
print(my_set) # Output might be: {1, 2, 3, (4, 5), 'apple'}



fruits = {"apple", "banana", "cherry"}

# You can only traverse directly:
for fruit in fruits:
    print(fruit)



s = {1, 2, 3}
print("Initial Set:", s)

# --- ADDING ---
s.add(4)
print("After add(4):", s)

# --- REMOVING ---
s.remove(2) # Removes 2. (Note: If 2 wasn't in the set, this would crash the program)

s.discard(5) # Removes 5. (Note: If 5 isn't there, it does NOTHING. No error!)

popped_item = s.pop() # Removes and returns a completely random element
print("Popped:", popped_item)

s.clear() # Empties the set entirely
print("After clear:", s) # Output: set()



A = {1, 2, 3}
B = {3, 4, 5}

# 1. UNION (Everything combined)
print("Union:", A.union(B))      # OR use: A | B 
# Output: {1, 2, 3, 4, 5}

# 2. INTERSECTION (What they have in common)
print("Intersection:", A.intersection(B)) # OR use: A & B
# Output: {3}

# 3. DIFFERENCE (In A, but not in B)
print("Difference:", A.difference(B))   # OR use: A - B
# Output: {1, 2}

# 4. SYMMETRIC DIFFERENCE (Unique to each, excluding overlap)
print("Sym Difference:", A.symmetric_difference(B)) # OR use: A ^ B
# Output: {1, 2, 4, 5}
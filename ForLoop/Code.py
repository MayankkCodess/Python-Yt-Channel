# Practice Operators , if-else , for loops till now 
# with complexity handling question don't focus on syntax try to build complex logic by your own 

# Starts at 1, goes up to (but does not include) 6
for i in range(1, 6):
    print(i)


a = "Nature"
# len(a) is 6. range(6) gives 0, 1, 2, 3, 4, 5.
for i in range(len(a)):
    print(a[i]) # Accesses the character at position 'i'


a = "Nature"
for char in a:
    print(char)




# Break Example
for lap in range(1, 21):
    if lap == 16:
        print("Rain started! Race cancelled.")
        break  # Stops the loop entirely
    print(f"Completed lap {lap}")

print("-" * 20)

# Continue Example
for lap in range(1, 6):
    if lap == 3:
        print("Skipping lap 3 due to a hurdle!")
        continue # Skips printing lap 3, moves to 4
    print(f"Completed lap {lap}")

print("-" * 20)

# Else with Loop Example
for number in range(1, 4):
    print(number)
else:
    print("Loop finished successfully without breaking!")
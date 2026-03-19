# A simple while loop example
counter = 1

# The loop runs as long as counter is less than or equal to 5
while counter <= 5:
    print(f"Current count is: {counter}")
    
    # We MUST update the condition variable, or it will loop forever
    counter += 1 

print("Loop finished!")
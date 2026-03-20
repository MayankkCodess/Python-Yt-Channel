# 1. Open the file in Read ('r') mode
file = open("myfile.txt", "r")

# 2. Read the contents
# .read() reads the entire file as one giant string
content = file.read() 
print(content)

# Other reading methods you can use instead of .read():
# line = file.readline()    --> Reads just the very first line
# lines = file.readlines()  --> Reads all lines and puts them into a List

# 3. CRUCIAL: You must manually close the file when done!
# If you don't, it wastes memory and can corrupt the file.
file.close()



# --- STEP 1: CREATE & WRITE TO A FILE ---
# We use 'w' to create the file and write initial data
with open("data.txt", "w") as f:
    f.write("Hello, this is my first file.\n")
    f.write("Python file handling is easy!\n")
# The file is automatically closed here!

# --- STEP 2: APPEND TO THE FILE ---
# We use 'a' so we don't erase the lines we just wrote above
with open("data.txt", "a") as f:
    f.write("This line is appended to the end.\n")
# The file is automatically closed here!

# --- STEP 3: READ THE FILE ---
# We use 'r' to read and print everything
with open("data.txt", "r") as f:
    final_content = f.read()
    
print("--- File Contents ---")
print(final_content)
# The file is automatically closed here!




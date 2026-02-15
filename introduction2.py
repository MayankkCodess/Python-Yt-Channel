#String Slicing and Type Conversion

a = "hello"; 
b = "SHER CODER"; 
print(a[1:4:1]); #output - "ell"
print(b[0:4]); #output - "SHER"
print(b[:4]); #- SHER
print(b[::]); #- SHER CODER
print(b[0::-1]); # - S
print(b[::-1]); # - REDOC REHS
print(b[0:8:2]); # - SE O 
# so here , a[start:stop:steps] 
"""start: The index where the slice begins (inclusive). If omitted, it defaults to the beginning of the string (index 0).
stop: The index where the slice ends (exclusive). The character at this index is not included in the result. If omitted, it defaults to the end of the string.
step: The interval between characters (stride). If omitted, it defaults to 1, which includes every character. A negative step value allows slicing in reverse. """

#Type Conversion - Implicit & Explicit 

# Explicit

a = 12; 
a = str(a); 
print(type(a)); # type - str 

# There are some Falsy Values and Except them all are True
# 1. False 2. 0 3. 0.0 4. "" 5. [] 6. () 7. {} 

a = 0.0; b = []; 
print(bool(a)); # boolean - false
print(bool(b)); 

# Implicit 

a = 12; 
print(type(12/3)); 


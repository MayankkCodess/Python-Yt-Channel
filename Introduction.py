print("Namaste Youtube , We are learning Python");  #Hello this semicolon is not mandatory

#----------------Variables Declaration-----------------------
age = 12; 
name = "mayank"; 

#Declaring Ways of Variable
SheriyansSchool = "students"; #PascalCase
sheriyansSchool = "students"; #CamelCase
sheriyans_school = "students"; #SnakeCase

#-------------------DataTypes--------------------------
#There are many types of variables in python like :- 1. Integer 2. Float 
# 3. Complex 4. Strings 5. Boolean 

print(type(age)); 
print(type(name)); 

a = -34; 
b = 56.8; 
c = 12/3; 

v = 12j; 

print(type(a))
print(type(b))
print(type(c)); #Float Data Type
print(type(v)); #Complex Data Type

st = '1234567890 dsagailqpurewrtyoiryzmvn !@#$%^&*()'; 
print(type(st)); #String Data Type - str

b = True; 
t = False; 
print(type(b)); #Boolean - bool 


#--------------String and Type Conversion----------------

a = "a"; 
print(ord(a)); #ord- converts chr to unicode 
b = 65; 
print(chr(b)); #chr- converts unicode to chr

# String Indexing

a = "SHER"; 

print(a[1]); 
print(a[1] , a[-1]); 
print(a[-3]); 
print(a[-5]); #this shows- IndexError- string index out of range
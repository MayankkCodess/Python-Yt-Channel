#How to work with input and output in python 
name = "akarsh"; 
age= "23"; 

print(name,age); 

# this is one way of writing 
print("hello , my name is ",name ,"and what about your",age);
# another way of writing !!! - formated string - we call it
print(f"hello, {name}! Welcome to our family!"); 


#Input -- 

# input("hello what is your age!!");  # now this is in garbage untill var declaration
# think if we donot commment out above then what is the output of print(age);


age = int(input("hello what is your age!!")); # now it is in variable to store
print(age); 

# for only demanding type input use type conversion of by default string input into int 



#now Operators -------------------------


#Arithmetic Operators 
a = 5; 
b = 20; 

print(b/a); #untill above age input works it does not print this (thought why);

#Use Floor division for convert divide output to int data type 

print(b//a); 

print(5**100); #python does not find any problem with memory limit


#Assignment Operator 
a = 24; 
b = 4; 

a %= b; # output - 0 // Here assigning and print does work in same step.
print(a); 

# Comparsion Operators 
print (a>= b); 

print(ord('a')); #order of a means ascii value
print("A">"B"); 
# Logical Operators 

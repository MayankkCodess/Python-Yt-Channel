# #Loops 
# for i in range(1,100,2):
#     print(i); 


# # (start,stop/condition,steps); 

# n = int(input("Enter the no of which table you want??")); 

# for i in range(n,n*10+1,n):
#     print(i); 


# a = "where is my party"; 

# for i in range(len(a)):
#     print(a[i]); 



# for i in range(1,38,2):
#     if i==25:
#         break; 
#     else:
#         print(i); 


# Practice for loop 

n = int(input("Enter n to print hello")); 

for i in range (n):
    print("hello world"); 

#Question 2 - natural numbers 

n = int(input("Enter n to print natural numbers")); 

for i in range(1,n+1):
    print(i); 

#Question 3 - reverse number - test

n = int(input("Enter n to print numbers in reverse")); 

for i in range(n,0,-1):
    print(i); 


#Question 4 - Sum up to n terms 

n = int(input("Enter n to do sum up to digit n")); 
sum = 0; 
for i in range(1,n+1,1): 
    sum += i; 

print(sum); 

# Question 5 - print all factors of a number 

n = int(input("Enter n to print its all factors")); 

for i in range(1,n+1):
    if(n%i==0):
        print(f"this {i} is factor of {n}"); 


#Question 6 - factorial of a number 

# write logic only

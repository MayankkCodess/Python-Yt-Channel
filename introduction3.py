
#----------------Conditional Statements----------------

money = int(input("give me some money")); 

if money>10:
    print("you can eat chocolate."); 
else:
    print("you need more money!"); 



# Some questions - Error   1 chr 2 ''  3 
gender = (input("give the first letter of your gender!")); 

if gender == 'M':
    print("Good Morning Sir!"); 
elif gender == 'F':
    print("Good Morning Ma'am"); 
else:
    print("i thought you are transgender"); 


# Leap year Program 

year = int(input("enter the year")); 

if year%100==0 and year%400==0:
    print("this is a leap year"); 
elif year%4==0 :
    print("this is leap year"); 
else:
    print("it is not a leap year"); 
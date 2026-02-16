# Some For loop Questions and While Loop 

import random; 

num = random.randint(1,10); 

while True:
    guess = int(input("Enter the no you are guessing...")); 

    if num == guess:
     print("you guess right"); 
    else:
     print("you are wrong"); 
 


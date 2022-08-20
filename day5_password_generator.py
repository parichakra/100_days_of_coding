#password generator project

import random

letters= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers =['0','1','2','3','4','5','6','7','8','9']
symbols =['!','@','#','$','%','&']

print("welcome to the passport generator:")
nletter= int(input("enter the number of letter do you want : "))
nsymbol= int(input("enter the number of symbol do you want : "))
nnumber= int(input("enter the number of numbers you want : "))

password =[]
for let in range(1,nletter+1):
     password.append(random.choice(letters))
     
newnumber=""
for num in range(1,nnumber+1):
     password+= random.choice(numbers)
     
newsymbol=""
for sym in range(1,nsymbol+1):
     password+= random.choice(symbols)

 
random.shuffle(password) 


final_password=""
for char in password:
    final_password+=char

print(f"the final password is {final_password}")

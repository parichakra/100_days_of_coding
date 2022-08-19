#rock paper sisor
import random
rock= "👊"
paper="🖐"
scisor="🤞"
game_images= [rock, paper, scisor]
user = int(input("what do you want to choose \n 0 for rock,1 for paper or 2 for scissor ="))
print(game_images[user])

computer =int(random.randint(0,2))

print(f"Computer choose :")
print(game_images[computer])

if user >=3 or user<0:
    print("invalid input")
elif user==0 and computer==2:
    print("you win!!")
elif computer==0 and user==2:
    print("computer win")    
elif computer >user:
    print("computer win!!")
elif user>computer:
    print("you win")    
elif computer ==user:
    print("draw")    
 


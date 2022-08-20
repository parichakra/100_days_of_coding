#tresure island
print("welcome to Tresure island ")
print("your mission is to find the treasure")

guess=input("choose left or right")
lguess=guess.lower()

if lguess=="right":
    againguess=input("choose swim or wall")
    lagain=againguess.lower()
    if lagain=="wall":
        color=input("choose which door red\blue\yellow")
        lcolor=color.lower()
        if lcolor=="yellow":
            print("you win!!")
        elif lcolor=="red":
            print("fire!! \n game over")
        else:
            print("crocodile!! \n game over")        
    else:
        print("crocodile!! \n game over!!")    
else:
    print("fire!! \n game over")    




#checking number  of cans needed  to paint a wall
import math

def paint_calc(height, width, cover):
    can_num= math.ceil((height*width)/cover)
    
    print(f"You'll need  {can_num} cans of paints.")


test_h = int(input("Height of wall:"))
test_w = int(input("width of wall: "))

coverage =5
paint_calc(height=test_h,width =test_w,cover =coverage)



#prime number checker
def prime_checker(number):
    is_prime =True
    for i in range(2 ,number-1)
        if number %i==0:
            is_prime = False

    if is_prime:
        print(f"  {number} is a prime number")
    else:
        print(f"  {number} is not  a prime number")    


n=int(input("enter a number"))
prime_checker(number= n)

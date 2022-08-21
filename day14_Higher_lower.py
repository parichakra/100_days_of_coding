
import random
from turtle import clear


logo ="""
 _     _       _                 _                        
 | |   (_)     | |               | |                       
 | |__  _  __ _| |__   ___ _ __  | | _____      _____ _ __ 
 | '_ \| |/ _` | '_ \ / _ \ '__| | |/ _ \ \ /\ / / _ \ '__|
 | | | | | (_| | | | |  __/ |    | | (_) \ V  V /  __/ |   
 |_| |_|_|\__, |_| |_|\___|_|    |_|\___/ \_/\_/ \___|_|   
           __/ |                                           
          |___/                         """

vs="""
 \ \ / / __|
  \ V /\__ -
   \_/ |___/ """


data=[
    {
        'name':'sagarmatha',
        'height': 8848,
        'description':'mountain from solukhumbu'
    },
    {
        'name':'makalu',
        'height': 8481,
        'description':'mountain from sankwasawa'
    },
    {
        'name':'lotese',
        'height': 8516,
        'description':'mountain from solukhumbu'
    },
    {
        'name':'kanchanjunga',
        'height': 8586,
        'description':'mountain from taplejumg'
    },
    {
        'name':'cho oyo',
        'height': 8188,
        'description':'mountain from solukhumbu'
    },
    {
        'name':'k 2',
        'height': 8611,
        'description':'mountain from pakistan'
    },
    {
        'name':'dhaulagiri',
        'height': 8167,
        'description':'mountain from mustang'
    },
    {
        'name':'Annapurna',
        'height': 8091,
        'description':'mountain from mustang'
    }
]

def format_data(mount):
    """format the data into printable format"""
    mountain_name= mount["name"]
    mountain_height= mount["height"]
    mountain_location= mount["description"]
    return(f"{mountain_name},{mountain_location}")

def check_answer(guess,a_height, b_height):
    """take user guess andcheck hieghtand return if they got right"""
    if a_height > b_height:
        return guess=="a"
    else:
        return guess=="b"            
#display logo
print(logo)
score=0
should_repeatable=True
mountain_b=random.choice(data)

#make a game repeatable
while should_repeatable:

    #generate random mountain from data

    #making mountain the mountain at position B to A
    mountain_a=mountain_b
    mountain_b=random.choice(data)

    if mountain_a==mountain_b:
        mountain_b= random.choice(data)



    #format the data into printable format
    print(f"compare A:{format_data(mountain_a)}")
    print(vs)
    print(f"Against B:{format_data(mountain_b)}")



    #ask user for a guess
    guess = input("Which one is highest mountain(A\B) :").lower()

    #check if the user is correct 
    #figure out height of each mountain 
    a_height =mountain_a["height"]
    b_height = mountain_b["height"]

    #check if staement by user is corrent
    is_correct =check_answer(guess,a_height,b_height)
    
   
    #give user feedback on their guess
    #score keepig
    if is_correct:
        score+=1
        print(f"You'r right! current score is {score}")
    else:
        should_repeatable= False
        print(f"You'r wrong! current score is {score}")

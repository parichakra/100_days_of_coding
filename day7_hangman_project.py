
import random 
stages = [

"""
    ________
    |/   |     
    |   (_)    
    |   /|\           
    |    |        
    |   / \        
    |               
    |___           
    HANGMAN"""

"""
  ________                   
    |/   |                         
    |   (_)                      
    |   /|\                             
    |    |                          
    |   /                            
    |                                  
    |___                              
    HANGMA""",   


"""
  _________              
    |/   |                     
    |   (_)                     
    |   /|\                    
    |    |                       
    |                             
    |                            
    |___                          
    HANGM""",
"""
   ________               
    |/   |                   
    |   (_)                  
    |   /|\                    
    |    |                    
    |                           
    |                            
    |___                    
    HAN""",


"""
   _________             
    |/   |               
    |   (_)                   
    |    |                     
    |    |                    
    |                        
    |                          
    |___                          
    HANG""",


"""
   _________              
    |/   |                     
    |   (_)                     
    |                       
    |                          
    |                             
    |                            
    |___                          
    HANGM""",



"""
   _________
    |/   |      
    |              
    |                
    |                 
    |               
    |                   
    |___                 
    H""",


"""
   _________
    |/        
    |              
    |                
    |                 
    |               
    |                   
    |___                 
    """]

 
word_list = [
'arrangement',
'attempt',
'border',
'brick',
'customs',
'discussion',
'essential',
'exchange',
'explanation',
'fireplace',
'floating',
'garage',
'grabbed',
'grandmother',
'heading',
'independent',
'instant',
'manufacturing',
'mathematics',
'memory',
'mysterious',
'neighborhood',
'occasionally',
'official',
'policeman',
'positive',
'possibly',
'practical',
'promised',
'remarkable',
'require',
'satisfied',
'scared',
'selection',
'shaking',
'shallow',
'simplest',
'slight',
'slope',
'species',
'thumb',
'tobacco'
'treated',
'vessels',
]
choosen_word =random.choice(word_list)

print(f"the word is {choosen_word}")

wordlen =len(choosen_word) 

lives = 6
display = []
for letter in range(wordlen):
    display += "_"
print(display)      


end_of_game = False
while not end_of_game:
    guess = input("Guess a letter:").lower()

   

    if guess in display:
        print(f"you've already guessed{guess}")

    for position in range(wordlen):
        letter =choosen_word[position]
        #print(f"your current position:{position} and current letter:{letter} and guess{guess}")
        if letter ==guess:
            display[position] =letter

    if guess not in choosen_word:
        print(f"you guess {guess},that is not in the word, you lose a life")
        lives -=1
        if lives ==0:
            end_of_game = True
            print("you lose") 



    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("you win..")    


    print(stages[lives])        

#A game about revenge, choices and survival 

class Game:
    def __init__(self):
        self.state = {
            'Helped_Twin_A': False,
            'Stay_with_Twins': False,
            'Knows_about_other_villages': False,
            'Suspect1_Friend': False,
            'Suspect2_Enemy': False,            
        }
    def clear_screen(self):
        print("\n" * 30) # Simple way to clear the screen  
    
    def display_text (self, text):
        print ("\n" + "=" * 50)
        print(text)
        print("\n" + "=" * 50) # just making space and cleaning up the screen 
        
    def get_choice(self, choices):
        for i, choice in enumerate(choices,1):
            print (f"{i}. {choice}")
        
        while True: 
            try: 
                choice = int(input("\nChoose wisely:" ))
                if 1 <= choice <= len(choices):
                    return choice
                else: 
                    print("The choice is unavailable. Try again")
            except ValueError:
                print("Enter a number please")
                
                
#opening scene. Screen lights up in a way as in one opening their eyes. 
#MC slowly opens eyes to see leaves on trees and sunshine pouring through.
#MC gets up and looks around while narration is played. 

    def opening(self):
        self.clear_screen()
        self.display_text("""

You have been in the woods for 264 days.

264 days since you have seen your family.
264 days since you were banished from your home.

264 days hunting for the beast.

The forest is your prison. One you cannot escape. One you cannot leave until you have completed your challenge.

The village elder's words echo in your mind:
"Return with the heart of the beast, or do not return at all.

You hate the forest. 
It's damp moss covered paths that always snag on your boots, 
Its huge trees that sometimes block out the sunlight,
and most of all
You hate that you have no idea where the beast that has haunted your village is hiding

But today is different.
because leading down a path you haven't yet explored, you've found tracks. Fresh ones.
        """)
        
        choices = [
            "Follow the tracks...",
            "Remember the trials...",
        ]
        
        choices = self.get_choice(choices)
        
        if choices == 1:
            self.get_attacked_by_wolves()
        elif choices == 2:
            self.flashback_trials()
        
        
    def get_attacked_by_wolves(self):
        self.clear_screen()
        self.display_text("""
                          
You follow the tracks deeper into the forest. The air grows colder as you feel the hairs on your neck stand up. 
You're close. You feel it. 
 
You continue down the path, not daring to breathe. 
For the first time you thank the moss that conceals the sound of your footsteps. 

All is quiet... until you hear something. It sounds like water. Rushing water. 
As you look ahead you notice a cliff that drops down. You step closer and look down. 
Its a massive ravine with a giant rushing river.

The beast probably doesn't live down there-

Suddenly a howl pierces the air. The another one. Then six more. You freeze. 

6 humoungous wolves emerge from the forest. 6 pairs of yellow eyes pin you down and surround you from each side.
A chill runs down your spine. 

You have no path for escape. 
Behind you is the ravine. In front of you...the wolves.

This is the end... 
You close your eyes and wait for the imminent attack 

                          
        """)
#after the words "imminent attack" the screen should go dark and make it seem like the game ended but it doesn't because Renn save the day huzzah



        choices = [
            "Rush in to help fight"
            "Stand back. You'll both die if you help"
        ]
        
        choices= self.get_choice(choices)
        
        if choices == 1 :
            self.state ['Helped_Twin_A'] = True
        else:
            self.state ['Helped_Twin_A'] = False
            
    def fight_together(self):
        self.clear_screen()
        #fight with the wolves: choosing to help the twin version
        self.display_text ("""
                           
HEREERHEHREHHEHERE
                           
                           
            """)
        
        input("\nPress enter to continue...")
        self.journey_to_treehouse()
        
    def stand_back(self):
        self.clear_screen()
        self.display_text("""
    DONT HELP THE TWIN AND JUST WATCH THEM GET HURT LOLOLOL
           
                          
                          """)
        
        input("\n Press Enter to continue...")
        self.journey_to_treehouse()
        
    def journey_to_treehouse(self):
        self.clear_screen()
        self.display_text(""" 
                          
    JOURNEY TO TREEHOUSE. INTRODUCTION TO RENN'S PERSONALITY
                          """)
        
        
        
        
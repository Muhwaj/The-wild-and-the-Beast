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
                choice = int(input("Choose wisely:"))
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
            "Remember when you almost died..." #mught change this option later or take it out i have no idea 
            
        ]
        
        choices = self.get_choice(choices)
        
        if choices == 1:
            self.get_attacked_by_wolves()
        elif choices == 2:
            self.flashback_trials()
        elif choices == 3:
            ############ flashback to something else maybe??
        
    def get_attacked_by_wolves(self):
        self.clear_screen()
        self.display_text("""
                          
You follow the tracks deeper into the forest. The air grows colder as you feel the hairs on your neck stand up. 
You're close. You feel it. 
 
You continue down the path, not daring to breathe. 
For the first time you thank the moss that conceals the sound of your footsteps. 
                          
                          
                          """)
#########RAH I DONT WANNA WORK ON THIS FOR NOW I WANNA MAKE THE ARRTTTT okAY nvm lock in 
        
        
        
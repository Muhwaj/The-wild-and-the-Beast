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

The sound of flesh tearing racked your ears. But that sound wasn't yours. You opened your eyes and...

Someone was there. A stranger in worn leather, moving with impossible grace. A sword flashed. 

You weren't going to die today you realised. Someone was helping you. 

"RUN!" he shouted 

The shout immediately knocked some sense into you. There were still too many wolves for one person to deal with. 
The stranger would surely be injured if you didn't help. But you would definetly be killed if you did. 

You looked towards the edge of the forest and saw a chance to escape. The wolves were distracted. 

But when you looked back a wolf clamped down it's teeth stranger's leg. 
He cried out in pain, stumbling to regain his footing.

You had two options now...

                          
        """)
#after the words "imminent attack" the screen should go dark and make it seem like the game ended but it doesn't because Renn save the day huzzah



        choices = [
            "Rush in to help. He saved your life after all"
            "Stand back and escape. You will die if you help"
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
                           
You pick up your weapon and gather your courage as you charge into battle. 

Your training for the trials kick in as you calm your beating heart and shaky hands. 

You attack one wolf with your dagger. Another with your sword. You're winning. The pack is moving back. 

The stranger looks at you with surprised but is pleased. 

"Duck!" he yells as you drop low and he slashes the tendons of the wolf that would have definietely killed you. 

As the last wolf disappears, the stranger collapses, breathing hard. 

"Thank you," he gasps, clutching his injured leg. Blood seeps between his fingers. "I was going to...just thanks"

You nod in acknowledgment, too busy catching your breath to form a proper reply. 

Up close he looks around your age, with short dark hair and sharp features. A huge scar runs from his right ear down his face towards his chin. 
Wonder how that happened....

"Can you walk?" you ask.

He tries to stand but immediately stumbles. 

"Guess not then". You wrap his wound with a spare cloth to stop the bleeding and support his weight as you start walking....
        
            """)
        
        input("\nPress enter to continue...")
        self.journey_to_treehouse()
        
    def stand_back(self):
        self.clear_screen()
        self.display_text("""
You freeze. Every instinct screams at you to help, but another firmer more logical voice that sounds awfully like your father says:
Don't. You'll get killed.. Always put your survival above others. No matter what it takes. 

The stranger sees you standing there and your eyes meet. He seems to understand. 

"Smart", he grunts, and then hes moving again. Injured, desperate and fighting with the fury of someone who's not used to losing. 

"Get out of the way!" he yells and then you're running. Running towards your freedom. 

The stranger tricks the wolves to leap towards the ravine, drowning them all. 

By the time each wolf is either dead or drowned, the stranger is barely standing. 

He collapses against a tree, breathing hard. Bloodstreaming from his leg. Too much blood. 

"Well", he says with a bitter laugh, examining his leg "at least one of us will live"

A mixture of shame and anger burn your chest. 

"I would have died if I helped", you manage

"You're right. I don't blame you that you didn't". He tries to stand and fails. "But are you willing to help now?"

"How do I know you won't kill me if I step closer?" you say but you're already grabbing spare cloth to bandage his leg. 

           
                          
                          """)
        
        input("\n Press Enter to continue...")
        self.journey_to_treehouse()
        
    def journey_to_treehouse(self):
        self.clear_screen()
        self.display_text(""" 
                          
    JOURNEY TO TREEHOUSE. INTRODUCTION TO RENN'S PERSONALITY
                          """)
        

#A game about revenge, choices and survival 

#Balancing storytelling and player choice 
#it's actually so much bigger than i thought lol
# i need to lock in 
#how do i draw what do i draw? 
#incomplete information and your decisions change the stuff 
#maybe add a little animation lol
#figure out how to use RenPy
#wait hold on a name like "The Beast Remembers"
#okay so name ideas are: 
# The Wild and the Beast
# The Beast Remembers
# Slay the Beast...or Not 






class Game:
    def __init__(self):
        self.state = {
            'Helped_Twin_A': False,
            'did_not_help_twin': False,
            'Stay_with_Twins': False,
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
#writing appears on the screen and little illustrations. the following text is displayed 

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

You attack one wolf with your dagger. Another with your sword. The pack is moving back. 

The stranger looks at you with surprise but is pleased. 

"Behind you!" he yells but you react too late.

Sharp, blinding pain shoots through your shoulder. Your vision goes white and your head hits the ground. 

The wolf with its teeth in your shoulder drags you closer, intending to rip you apart. Another one grabs your leg. 

You're going to die. "You should have stayed back", your father voice echoes. Maybe you should have. 

You lock eyes with the stranger. At least you did some good before you died. 

The pain is blinding, searing through your body. You're losing blood faster than you can fight back. 

Your head collides with a sharp piece of rock and your vision goes black. 

A small mercy. 

            """)
        
        input("\nPress enter to continue...")
        self.journey_to_treehouse()
        
    def stand_back(self):
        self.clear_screen()
        self.display_text("""
                          
You freeze. Every instinct screams at you to help, but another firmer more logical voice that sounds awfully like your father says:
Don't. Always put your survival above others. No matter what it takes. 

The stranger sees you standing there and your eyes meet. He seems to understand. 

"Smart", he grunts, and then hes moving again. Injured, desperate and fighting with the fury of someone who's not used to losing. 

"Get out of the way!" he yells and then you're running. Running towards your freedom. 

You're almost there when you hear a scream. 

You turn to see that wolves have grabbed his shoulder and leg. Theyre going to rip him apart. 
    
        """)
        
        

        
        choices = [
            "Keep running. Take your freedom while you still have it"
            "Go back and help. He saved your life didn't he?"
        ]
        
        choices= self.get_choice(choices)
        
        if choices == 1 :
            self.state ['did_not_help_twin'] = True
        else:
            self.state ['did_not_help_twin'] = False
         
        input("\n Press Enter to continue...")
        self.save_twin_or_no()
        
    def save_twin_or_no(self):
        self.clear_screen()
        self.display_text(""" 
                          
        Go back and save twin lol. You're gonna get badly hurt lol. 
        Basically pass out and be incapabale for weeks.
        Very much delaying your time for finding the beast so sad. very inconveneient. 
        twin b doesn't like you btw. she hatesss your guts but you saved twin a's life so she simply has to deal with it.
        if twin a dies tho it will be a very dark character arc i dont know if i can write that 
                          

                          """)    
            
            
        input("\n Press Enter to continue...")
        self.save_twin_or_no()
        
    def save_twin_or_no(self):
        self.clear_screen()
        self.display_text("""   
                          
           did not save twin lol
           btw if you don't save twin A twin B will find you instead and you'll become friends but they will find out that you left the twinnnnn with the wolves and will want revenge               
                          """)  
            
        
     
        input("\n Press Enter to continue...")
        self.journey_to_treehouse()
        
    def journey_to_treehouse(self):
        self.clear_screen()
        self.display_text(""" 
                          
    JOURNEY TO TREEHOUSE. INTRODUCTION TO RENN'S PERSONALITY
                          """)         
        
 
 
#define revenge_arc for twin B orrrr also add a reconcilaiton option ?
#define define fighting the beast or not option
#fight_beast: ignore his bullshit, kill him, take his heart, return to village. you will not become the beast like him
#dont_fight_beast: you listen to his amazing wisdom, decide to never go back, build a community with him instead. huzzah       
    
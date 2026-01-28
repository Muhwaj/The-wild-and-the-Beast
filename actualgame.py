#A game about revenge, choices and survival 

#okay so name ideas are: 
# The Wild and the Beast
# The Beast Remembers

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
        print("\n" * 30)
    
    def display_text(self, text):
        print("\n" + "=" * 50)
        print(text)
        print("=" * 50 + "\n")  
        
    def get_choice(self, choices):
        for x, choice in enumerate(choices, 1):
            print(f"{x}. {choice}") 
            
        while True: 
            try: 
                choice = int(input("\nChoose wisely: "))
                if 1 <= choice <= len(choices):
                    return choice
                else: 
                    print("The choice is unavailable. Try again")
            except ValueError:
                print("Enter a number please")

    def opening(self):
        self.clear_screen()
        self.display_text("""
You have been in the woods for 264 days.

264 days since you have seen your family.
264 days since you were banished from your home.

264 days hunting for the beast.

The forest is your prison. One you cannot escape. One you cannot leave until you have completed your challenge.

The village elder's words echo in your mind:"Return with the heart of the beast, or do not return at all."

You hate the forest. 
It's damp moss covered paths that always snag on your boots, 
Its huge trees that sometimes block out the sunlight,
and most of all
You hate that you have no idea where the beast that has haunted your village is hiding

But today is different.

because leading down a path you haven't yet explored, you've found tracks. Fresh ones.
        """)
        
        choice = self.get_choice([
            "Follow the tracks...",
            "Remember the trials...",
        ])
        
        if choice == 1:
            self.get_attacked_by_wolves()
        else:
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

Suddenly a howl pierces the air. Then another one. Then six more. You freeze. 

6 humongous wolves emerge from the forest. 6 pairs of yellow eyes pin you down and surround you from each side. A chill runs down your spine. 

You have no path for escape. 

Behind you is the ravine. In front of you...the wolves.

This is the end... 

You close your eyes and wait for the imminent attack. 

--------THE END------------




====================================================================================================================================================
























---lol sike---



The sound of flesh tearing racked your ears. But that sound wasn't yours. You opened your eyes and...

Someone was there. A stranger in worn leather, moving with impossible grace. A sword flashed. 

You weren't going to die today you realised. Someone was helping you. 

"RUN!" he shouted 

The shout immediately knocked some sense into you. There were still too many wolves for one person to deal with. 

The stranger would surely be injured if you didn't help. But you would definitely be killed if you did. 

You looked towards the edge of the forest and saw a chance to escape. The wolves were distracted. 

But when you looked back a wolf clamped down its teeth on the stranger's leg. He cried out in pain, stumbling to regain his footing.

You had two options now...
        """)

        choice = self.get_choice([
            "Rush in to help. He saved your life after all",
            "Stand back and escape. You will die if you help"
        ])
        
        if choice == 1:
            self.state['Helped_Twin_A'] = True
            self.fight_together() 
        else:
            self.stand_back()
            
    def fight_together(self):
        self.clear_screen()
        self.display_text("""
You pick up your weapon and gather your courage as you charge into battle. 

Your training for the trials kick in as you calm your beating heart and shaky hands. 

You attack one wolf with your dagger. Another with your sword. The pack is moving back. 

The stranger looks at you with surprise but is pleased. 

"Behind you!" he yells but you react too late.

Sharp, blinding pain shoots through your shoulder. Your vision goes white and your head hits the ground. 

The wolf with its teeth in your shoulder drags you closer, intending to rip you apart. Another one grabs your leg. 

You're going to die. "You should have stayed back", your father's voice echoes. Maybe you should have. 

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

"Smart", he grunts, and then he's moving again. Injured, desperate and fighting with the fury of someone who's not used to losing. 

"Get out of the way!" he yells and then you're running. Running towards your freedom. 

You're almost there when you hear a scream. 

You turn to see that wolves have grabbed his shoulder and leg. They're going to rip him apart.
        """) 
        
        choice = self.get_choice([
            "Keep running. Take your freedom while you still have it",
            "Go back and help. He saved your life, didn't he?"
        ])
        
        if choice == 1:
            self.state['did_not_help_twin'] = True
            self.did_not_save_twin() 
        else:
            self.state['Helped_Twin_A'] = True
            self.save_twin() 
         
    def save_twin(self):
        self.clear_screen()
        self.display_text(""" 
Your conscience wars with your practicality. 
        
Choosing to go back could get you killed but leaving will definitely get him killed. 
        
You pick up your weapon and charge towards the wolves, intending to distract them long enough for the stranger to get back up. 
        
You manage to injure the wolf holding him by flinging your dagger. The stranger looks at you gratefully and manages to crawl towards a safer distance. 

He leans on a tree but gets back up, intending to finish this fight with you.

For a moment his eyes meet yours, expressing gratitude and respect but they suddenly change to fear. 

"Behind you!" he yells but you react too late.

Sharp, blinding pain shoots through your shoulder. Your vision goes white and your head hits the ground. 

The wolf with its teeth in your shoulder drags you closer, intending to rip you apart. Another one grabs your leg. 

You're going to die. "You should have stayed back", your father's voice echoes. Maybe you should have. 

You lock eyes with the stranger. At least you did some good before you died. 

The pain is blinding, searing through your body. You're losing blood faster than you can fight back. 

Your head collides with a sharp piece of rock and your vision goes black.            
        """)    
            
        input("\nPress Enter to continue...")
        self.journey_to_treehouse()
        
    def did_not_save_twin(self):
        self.clear_screen()
        self.display_text("""   
It's too risky to go back. It's too risky to save him. There are too many wolves and even if you interfered now you won't be able to save him and get out alive.

You take a deep breath and run away. 

Screams. Screams of pure human agony as the wolves tear the stranger apart. Limb for limb.

Still you don't turn back. You can't. 

You run as far as your legs can take you. The screaming has long since ceased yet it still echoes in your brain. It will haunt you forever. 
        """)  
            
        input("\nPress Enter to continue...")
        self.twin_dies()
        
    def twin_dies(self):
        self.clear_screen()
        self.display_text(""" 



You continue through the forest alone.

The stranger's screams haunt your dreams. You tell yourself it was the right choice. Survival above all else. 

That's what your father always said.

But deep down, you wish you'd gone back. 

You're alone. You're tired. And you're angry. 

What good is your life above his?

200 days later you still have not found the beast

You are different now. Harder. Colder. More alone than ever. Someone who would give up the life of anybody to save your own. 

Your father would be proud. 

You've become the hardened soldier he'd always wished for you to be. 

You wonder if you can ever face your family again...

[TO BE CONTINUED: Need to add beast encounter and final choice]

        """)         
                
        input("\nPress Enter to restart...")
        self.__init__()
        self.start()

    def journey_to_treehouse(self):
        self.clear_screen()
        self.display_text(""" 
Pain.

Throbbing, searing, all-consuming pain.

Your shoulder feels like it's on fire. Your leg throbs with every heartbeat. Even breathing hurts.

You try to remember. The wolves. The stranger. Fighting. Teeth. Claws. Blood.

Darkness.

You should be dead.

Slowly, you force your eyes open. Everything is blurry at first. 

Wooden walls. Rope. Sunlight filtering through gaps.

You have absolutely no clue where you are. 

"You're awake."

The stranger. The stranger you risked your life to save. The very same stranger now eyeing you with concern and relief. 

He's sitting nearby, his leg bandaged.

"How are you feeling?" he asks, voice warm despite his obvious exhaustion. 

Exhausted. Frustrated. Confused. You try to reply but your throat is dry as a bone. 

Despite his injury, he moves swiftly to provide you with a flask of water. 

You gulp down the fresh, sweet water as if its your first time drinking. He patiently waits for you to finish to introduce himself

"I'm Renn, by the way" he pauses as if expecting your name in return but you simply stare back. Who is this guy? 

He continued, undeterred "I- I wanted to thank you for saving my life. You could have saved yourself but you chose to fight beside me instead." 

"That's a debt I can never repay". The idea of someone's life being indebted to you made your already throbbing head start pounding. 

You still cannot form the words nor the coherent thoughts to have a conversation. 

He seems to understand and gestures towards your shoulder, wrapped in clean bandages. "You've been out for five days. We weren't sure you'd make it."
        """)
        
        input("\nPress Enter to continue...")
        self.talk_with_renn()

    def talk_with_renn(self):
        asked_questions = {
            'where': False,
            'how_here': False,
            'how_long': False,
            'who_are_you': False
        }
        
        while True:
            self.clear_screen()
            print("\n" + "="*50)
            print("Renn sits nearby, watching you with concern.")
            print("="*50 + "\n")
            
            choices = []
            
            if not asked_questions['where']:
                choices.append(("Where am I?", 'where'))
            
            if not asked_questions['how_here']:
                choices.append(("How am I here?", 'how_here'))
            
            if not asked_questions['how_long']:
                choices.append(("Five days? I've been out for five days???", 'how_long'))
            
            if not asked_questions['who_are_you']:
                choices.append(("Who are you? Why are you out here?", 'who_are_you'))
            
            choices.append(("Say nothing more.", 'continue'))
            
            for i, (text, _) in enumerate(choices, 1):
                print(f"{i}. {text}")
            
            while True:
                try:
                    choice = int(input("\nChoose wisely: "))
                    if 1 <= choice <= len(choices):
                        break
                    else:
                        print("The choice is unavailable. Try again")
                except ValueError:
                    print("Enter a number please")
            
            question_key = choices[choice - 1][1]
        
            if question_key == 'continue':
                break
            
            asked_questions[question_key] = True
            
            self.clear_screen()
            
            if question_key == 'where':
                self.display_text("""
"Where am I?"

Renn gestures around the small space. "My home. Well, our home. My sister and I built this treehouse two years ago when we first came to these woods."

He notices your confusion. "We live here. The forest is... safer than you'd think. Once you learn its patterns."

Two years in the woods? By choice?
                """)
            
            elif question_key == 'how_here':
                self.display_text("""
"How am I here? How did you get me here?"

"After you passed out?" Renn looks down at his bandaged leg. "I managed to drive the wolves off. Barely. They don't like fire, and I always carry flint."

He pauses. "You bought me the time I needed. If you hadn't come back... I'd be dead. We'd both be dead."

"I dragged you here. Took most of the night. My sister wasn't happy about it."

There's weight in his words. Gratitude. Something deeper.
                """)
            
            elif question_key == 'how_long':
                self.display_text("""
"Five days?! I've been unconscious for five days?"

"Five and a half, technically," Renn says. "You lost a lot of blood. My sister had to stitch your shoulder. Your leg too. The wolves really did a number on you."

He gestures to a clay bowl nearby filled with water. "You should drink. You're dehydrated."

Five days. Five days lost. The beast could be anywhere by now. And you had no idea where you were.
                """)
            
            elif question_key == 'who_are_you':
                self.display_text("""
"Who are you? Why are you out here in the middle of the forest?"

Renn's expression shifts. Guarded. Careful.

"That's... complicated," he says after a moment. "I'm Renn. My sister is Kira. We've been living out here for two years."

"But why—"

"It's not by choice," he interrupts, then stops himself. "Well. Not entirely. Look, it's complicated. And it's not just my story to tell."

He glances upward, as if expecting someone. "Kira will be back soon. She's the one who patched you up. She's... let's just say she's going to have questions."

There's something he's not saying. Something important.
                """)
            
            input("\nPress Enter to continue...")
        
        self.kira_arrives()

    def kira_arrives(self):
        self.clear_screen()
        self.display_text("""
A sharp whistle cuts through the air. Three short bursts.

Renn's entire body tenses. "That's Kira. She's back."

Before you can ask what that means, a figure climbs through the trap door.

She looks like Renn. Same sharp features, same dark hair, similar build. But where Renn's eyes hold warmth and concern, hers are ice.

Cold. Calculating. Dangerous.

"You're awake," she says. Her hand rests casually on the knife at her belt.

"Kira, this is—" Renn starts.

"I know enough about who she is" Her eyes never leave you. "A stranger. A danger."

"She saved my life!"

"And I saved hers." Kira's voice is flat. "Tit for tat. Five days of supplies. Five days of medicine. I think we're pretty even."

The accusation hangs in the air.
        """)
        
        input("\nPress Enter to continue...")
        self.talk_with_kira()
    
    def talk_with_kira(self):
        self.clear_screen()
        self.display_text("""
[TO BE WRITTEN: Conversation with Kira]

Kira watches you with cold eyes, waiting for you to speak...

        """)
        
        input("\nPress Enter to continue...")
        print("\n[STORY CONTINUES NEED TO WRITE MORE rahhhhhhh]")
        self.opening()
    
    def flashback_trials(self):
        self.clear_screen()
        self.display_text("""
[TO BE WRITTEN: Flashback to the trials]

The village square. The trials. Kael. Mira. The sabotage. Who did what 


        """)
        
        input("\nPress Enter to continue...")
        self.opening()
    
    def start(self):
        print("\n" + "="*60)
        print("          THE WILD AND THE BEAST")
        print("     A game about revenge, choices, and survival")
        print("="*60)
        input("\nPress Enter to begin...")
        self.opening()

# Run the game
if __name__ == "__main__":
    game = Game()
    game.start()
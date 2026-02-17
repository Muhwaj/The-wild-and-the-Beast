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
    asked_questions = {
        'why_hostile': False,
        'why_save': False,
        'who_are_you': False,
        'not_danger': False
    }
    
    while True:
        self.clear_screen()
        print("\n" + "="*50)
        print("Kira stands near the door, hand close to her belt where her knife is")
        print("Her eyes never leave you.")
        print("="*50 + "\n")
        
        choices = []
        
        if not asked_questions['why_hostile']:
            choices.append(("Why are you so hostile?", 'why_hostile'))
        
        if not asked_questions['why_save']:
            choices.append(("If you didn't trust me, why save me?", 'why_save'))
        
        if not asked_questions['who_are_you']:
            choices.append(("Who are you? What are you even doing here?", 'who_are_you'))
        
        if not asked_questions['not_danger']:
            choices.append(("I'm not a danger to you.", 'not_danger'))
        
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
        
        if question_key == 'why_hostile':
            self.display_text("""
                              
"Why are you so hostile? You don't know me. I haven't even done anything besides save your brother's life" you say, albeit a little pointedly

Kira's mistrust negativity and mistrust towards you was making you a little defensive.

Her expression doesn't change. "Three people have found us before you." she says "And each time we've lived to regret ever helping them"

She counts on her fingers. "One tried to steal our supplies while we slept. One attacked Renn when he was gathering water. One seemed friendly for two weeks, then tried to kill us both."

Her hand tightens on her knife. "So forgive me if I'm not exactly chummy with you at the moment. You saved Renn's life and I saved yours. This should be end of discussion and I would prefer if you left"

Renn shifts uncomfortably. "Kira—"

"No." Her voice is steel. "Trust gets you killed out here and I'm not done trusting."
            """)
        
        elif question_key == 'why_save':
            self.display_text("""
"If you didn't trust me, why bother savnig me?"

For the first time, Kira's expression shifts. Something flickers in her eyes. Regret? Anger?

"Because Renn begged me to." Her voice is flat. "He dragged you back here half-dead, bleeding everywhere. Said you saved his life."

She glances at her brother. "And I was in a position to say no to him. So I helped you"

"Kira, you didn't have to—"

"Yes, I did." She cuts him off. "You're all I have left. If saving some stranger keeps you alive, fine. But that doesn't mean I have to trust them and"

The weight of her words hangs heavy. She's not protecting you. She's protecting Renn.
            """)
        
        elif question_key == 'who_are_you':
            self.display_text("""
"Who are you? What are even you doing out here?"

Kira's jaw tightens. "That's none your business."

"Kira," Renn says softly. "They're going to find out eventually. They're injured. They'll be here for days."

"Then they can leave in days. They don't need to know our life story."

But Renn continues anyway. "We're from a village east of here. We were banished two years ago."

You freeze. Banished. Just like you.

"For what?"

"For asking questions we shouldn't have asked," Kira says bitterly. "For noticing things we weren't supposed to notice. For threatening the order of things."

"Just like you're doing now"

Her eyes bore into you. "Sound familiar?"
            """)
        
        elif question_key == 'not_danger':
            self.display_text("""
"I'm not a danger to you. I'm alone. Banished. Just trying to survive."

Kira studies you for a long moment. 

"Banished," she repeats. "From where?"

You tell her about your village. The trials. The impossible task.

Something shifts in her expression. Not quite softening, but... understanding.

"Banished for being inconvenient," she says quietly. "They do that. Villages. Get rid of people who don't fit. Who ask too many questions. Who threaten their precious order."

Renn nods. "We were banished for questioning our elders. For noticing they hoarded knowledge and resources while others suffered."

"Different villages," Kira continues. "Different methods. Same cruelty."

For the first time, she doesn't look at you like a threat. She looks at you like someone who understands.
            """)
        
        input("\nPress Enter to continue...")
    
    # After all questions, offer the choice
    self.twins_offer_choice()
    
    def twins_offer_choice(self):
        self.clear_screen()
        self.display_text("""
The tension in the room has shifted. Kira still watches you carefully.

Renn speaks first. "You're injured. You need time to heal. You can stay here. With us. Until you're strong enough to continue."

Kira's jaw tightens but she doesn't object.

"It's not much," Renn continues. "But we have shelter. Food. Medicine. You have better chances with us than out there alone"

"For now," Kira adds pointedly.

You think about it. Five days unconscious. You're weak. Injured. The beast could be anywhere by now.

And you weren't big on strangers either. Especially not how Kira kept her knife always ready.

But these two... they were starting to understand. They were cast out just like you. And maybe they won't kill you in your sleep. Not after all that trouble of saving your life and all.



    """)
    
    choice = self.get_choice([
        "Accept their offer. Stay and heal.",
        "Decline. Leave as soon as you can walk."
    ])
    
    if choice == 1:
        self.state['Stay_with_Twins'] = True
        self.stay_with_twins()
    else:
        self.state['Stay_with_Twins'] = False
        self.leave_twins()

def stay_with_twins(self):
    self.clear_screen()
    self.display_text("""


You decide to stay.

Over the next two months, you heal. Your shoulder knits back together. Your leg grows strong again.

Renn teaches you fighting techniques not taught in your village. Maneuvering a blade in ways you didn't think was possible. 

Kira, slowly warming to you, shows you the forest. Which plants are edible. How to track. How to move silently. How to avoid the giant creatures that roam the deeper woods.

You learn about them too. Renn's optimism. His belief that people can change. His hope.

Kira's pragmatism. Her caution. Her fierce protection of her brother. Her survival instinct.

They become something akin to friends. Not quite. But you can rely on them. 

The weight never leaves you however. The beast. Your village. Your family. Your mission.

"I need to keep moving," you tell them one morning, "I need to find the beast."

Renn's face falls slightly. Kira just nods, as if she expected this.

"Be careful," Renn says. "And... if you need shelter again, you know where to find us."

Kira adds quietly: "You're welcome back."

You leave them each with a small parting gift. It's not much, just a sharp stone you carved for Kira and a leather pouch for Renn. A token of thanks for letting you stay with them and heal.

You leave, carrying their lessons. Now your one job was to find the beast.

You're a different person than the one they saved.
    """)
    
    input("\nPress Enter to continue...")
    print("\n[TO BE WRITTEN: Finding the beast's cave]")
    self.opening()  # Temporary - replace with beast encounter

def leave_twins(self):
    self.clear_screen()
    self.display_text("""
PARTING WAYS

"I appreciate the offer," you say. "But I have a task. I can't afford to waste time. I want to get back to my family as soon as possible"

Kira's expression doesn't change, but you see a question in her eyes. The same curiosity is etched on Renn's face

"Why on earth would you want to go back after they banished you so unfairly?" Kira asks

"Whatever the village elders banished me for doesn't erase the fact I still have a family I want to go back to. They assigned me an impossible mission but I will complete it and prove them wrong"

"Stubborn," Kira says. "But honest. I respect that."

Renn hands you supplies. Dried meat. Bandages. A whetstone.

"For the road. And good luck finding your beast."

You leave three days later, when you can walk without wincing.

You momentarily wonder if you should have stayed considering your state. But never mind that you 

[WRITEEEEEEEEEEEEE MOTREEEEEEEEEEEEEEEEEEEEEEEEEEEEEE]

    """)
    
    input("\nPress Enter to continue...")
    print("\n[TO BE WRITTEN: Finding the beast's cave]")
    self.opening()  # Temporary - replace with beast encounter
    
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
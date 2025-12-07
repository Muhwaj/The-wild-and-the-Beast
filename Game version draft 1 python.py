#A game about revenge, choices and survival 

class Game:
    def _init_(self):
        self.state = {
            'Helped_Twin_A': False,
            'Stay_with_Twins': False,
            'Knows_about_other_villages': False,
            'Suspect1_Friend': False,
            'Suspect2_Enemy': False,            
        }
    def clear_screen(self):
        print("\n" * 50) # Simple way to clear the screen
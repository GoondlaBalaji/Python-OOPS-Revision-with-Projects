from character import Character

class Archer(Character):
    def __init__(self, name, health,arrows):
        super().__init__(name, health)
        self.arrows = arrows
        
    # here we are overriding the function that is present in parent class    
    def attack(self):
        print(f"{self.name} shoots {self.arrows}")
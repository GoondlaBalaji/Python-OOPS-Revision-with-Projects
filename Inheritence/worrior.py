from character import Character

class Warrior(Character):
    def __init__(self, name, health, sword):
        super().__init__(name, health)
        self.sword = sword
        
    def attack(self):
        print(f"{self.name} attacks with {self.sword}")
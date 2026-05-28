from character import Character

class Mage(Character):
    def __init__(self, name, health, magic):
        super().__init__(name, health)
        self.magic= magic
    
    def attack(self):
        print(f"{self.name} uses {self.magic} power")
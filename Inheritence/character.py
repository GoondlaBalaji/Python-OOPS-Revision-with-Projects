class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        
    def status(self):
        print("\n---CHARACTER STATUS---")
        print(f"Name: {self.name}")
        print(f"health: {self.health}")
        
    def attack(self):
        print(f"{self.name} atacks enemy")
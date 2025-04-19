class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5         # Mid-point starting value
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} eats happily. 🍖")

    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} curls up and sleeps peacefully. 💤")

    def play(self):
        if self.energy == 0:
            print(f"{self.name} is too tired to play. 😴")
        else:
            self.energy = max(0, self.energy - 2)
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print(f"{self.name} plays fetch and runs in circles! 🎾")

    def train(self, trick):
        if trick.lower() not in [t.lower() for t in self.tricks]:
            self.tricks.append(trick)
            self.happiness = min(10, self.happiness + 1)
            self.energy = max(0, self.energy - 1)
            print(f"{self.name} has learned a new trick: {trick}! 🏆")
        else:
            print(f"{self.name} already knows how to {trick}. 🤓")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name}'s Tricks:")
            for trick in self.tricks:
                print(f"✨ {trick}")
        else:
            print(f"{self.name} hasn’t learned any tricks yet. 🐾")

    def get_status(self):
        print(f"\n📋 Status of {self.name}:")
        print(f"  🥗 Hunger: {self.hunger}")
        print(f"  ⚡ Energy: {self.energy}")
        print(f"  😊 Happiness: {self.happiness}")
class Pokemon:
    def __init__(self, entry, name, types, description, is_caught=False):
        self.entry = entry
        self.name = name
        self.types = types
        self.description = description
        self.is_caught = is_caught

    def speak(self):
        return f"{self.name * 2}"
    
    def display_detail(self):
        details = f"Entry number : {self.entry}\nName : {self.name}\nType : {self.types}\nDescription : {self.description}\n"
        if self.is_caught:
            details += f"{self.name} has been caught"
        else:
            details += f"{self.name} has not been caught"
        return details

# Create Pokemon objects
pokemon1 = Pokemon(1, "Bulbasaur", ["Grass", "Poison"], "A strange seed was planted on its back at birth. The plant sprouts and grows with this Pokémon.")
pokemon2 = Pokemon(4, "Charmander", ["Fire"], "It has a preference for hot things. When it rains, steam is said to spout from the tip of its tail.", True)
pokemon3 = Pokemon(7, "Squirtle", ["Water"], "After birth, its back swells and hardens into a shell. Powerfully sprays foam from its mouth.")

# Demonstrate instance methods
print(pokemon1.speak())
print(pokemon2.display_detail())
print(pokemon3.display_detail())
print(pokemon1.display_detail()) # Example of calling display_detail on a not caught Pokemon

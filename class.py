class Superhero:
    def __init__(self, name, secret_identity, powers, universe="Marvel"):
        # Encapsulation with public and "private" attributes
        self.name = name
        self._secret_identity = secret_identity  # Protected attribute
        self.powers = powers
        self.universe = universe
        self._energy_level = 100  # Private attribute
        
    # Instance method
    def use_power(self, power_index):
        if power_index < len(self.powers):
            print(f"{self.name} uses {self.powers[power_index]}!")
            self._energy_level -= 10
        else:
            print("Power not available!")
    
    # Getter method for encapsulation
    def get_energy(self):
        return self._energy_level
    
    # Static method
    @staticmethod
    def multiverse_theory():
        print("Infinite universes mean infinite possibilities!")
    
    def __str__(self):
        return f"{self.name} ({self._secret_identity}) from {self.universe}"

# Inheritance example
class Avenger(Superhero):
    def __init__(self, name, secret_identity, powers, team_role):
        super().__init__(name, secret_identity, powers, "Marvel")
        self.team_role = team_role  # New attribute
        
    # Polymorphic method
    def use_power(self, power_index):
        if self.get_energy() > 20:  # Avengers have more stamina
            super().use_power(power_index)
        else:
            print("Avenger needs rest!")
    
    # New method specific to Avengers
    def assemble(self):
        print(f"{self.name} answers the call to assemble!")

# Creating objects
iron_man = Superhero("Iron Man", "Tony Stark", ["Repulsor Beams", "Flight"])
cap = Avenger("Captain America", "Steve Rogers", ["Super Strength", "Shield Throw"], "Leader")

print(iron_man)  # Uses __str__
iron_man.use_power(0)  # Uses Superhero's method
cap.assemble()  # Uses Avenger's special method
cap.use_power(1)  # Polymorphic behavior
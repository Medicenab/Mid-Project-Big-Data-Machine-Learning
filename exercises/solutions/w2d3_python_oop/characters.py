import numpy as np

class Human:
    def __init__(self, name, health, power, accuracy=50):
        self.name = name
        self.health = health
        self.power = power
        self.accuracy = accuracy

    def shoot(self):
        aleatorio = np.random.randint(1,101)

        if aleatorio <= self.accuracy:
            return self.power
        else:
            return 0

    def takeDamage(self, damage):
        self.health -= damage
        if damage == 0:
            return "Shot missed."
        elif self.health <= 0:
            return f"{self.name} died."
        else:
            return f"{self.name} lost {damage} health."
'''        
class Sniper(Human):
    def __init__(self, name, health, power, accuracy=50):
        super().__init__(name, health, power, accuracy+15)

    def shoot(self):
        resultado_1=super().shoot()
        if resultado_1 == 0:
            return super().shoot()
        else:
            return resultado_1
'''
class Sniper:
    def __init__(self, name, health, power, accuracy=50):
        self.name = name
        self.health = health
        self.power = power
        self.accuracy = accuracy +15

    def shoot(self):
        aleatorio = np.random.randint(1,101)

        if aleatorio <= self.accuracy:
            return self.power
        else:
            aleatorio2 = np.random.randint(1,101)

            if aleatorio2 <= self.accuracy:
                return self.power
            else:
                return 0
    def takeDamage(self, damage):
        self.health -= damage
        if damage == 0:
            return "Shot missed."
        elif self.health <= 0:
            return f"{self.name} died."
        else:
            return f"{self.name} lost {damage} health."

class Alien:
    def __init__(self, health, power, accuracy=65):
        self.health = health
        self.power = power
        self.accuracy = accuracy

    def shoot(self):
        aleatorio = np.random.randint(1,101)

        if aleatorio <= self.accuracy:
            return self.power
        else:
            return 0

    def takeDamage(self, damage):
        self.health -= damage
        if damage == 0:
            return "Shot missed."
        elif self.health <= 0:
            return "Alien scum destroyed."
        else:
            return f"Alien lost {damage} health."

class Squad:
    def __init__(self, *fighters):
        self.fighters = list(fighters)

    def add(self,fighter):
        self.fighters.append(fighter)

    def remove(self, fighter):
        self.fighters.remove(fighter)

    def __len__(self):
        return len(self.fighters)

    def __iter__(self):
        return iter(self.fighters)

class Battle:
    def __init__(self, aliens, humans):
        self.aliens = aliens
        self.humans = humans
    
    def attack(self, attackingArmy, defendingArmy):
        log = {"shots_missed":0,
                "shots_hit":0,
                "enemies_killed":0
                }
        for attacker in attackingArmy:
            damage = attacker.shoot()
            chosen_one = np.random.randint(0, len(defendingArmy))
            chosen_one = defendingArmy.fighters[chosen_one]
            resultado = chosen_one.takeDamage(damage)
            if damage == 0:
                log["shots_missed"] += 1
            elif "died" in resultado or "destroyed" in resultado:
                defendingArmy.remove(chosen_one)
                log["enemies_killed"] += 1
            else:
                log["shots_hit"] += 1
        return log

    def status(self):
        if self.aliens and self.humans:
            return "The battle goes on. Our planet depends on it."
        if self.humans:
            return "Humans saved the Earth. The planet is still ours, for now."
        if self.aliens:
            return "The human race failed. Aliens conquered the Earth."


import random
from datetime import datetime


# Game Object
class GameObject:
    def __init__(self, created_at, name, dimensions):
        super().__init__()
        self.created_at = created_at
        self.name = name
        self.dimensions = dimensions

    def destroy(self):
        return f'{self.name} was removed from the game.'


# Character
class Character(GameObject):
    def __init__(self, created_at, name, dimensions, health_points):
        super().__init__(created_at, name, dimensions)
        self.health_points = health_points

    def take_damage(self, i):
        self.health_points = self.health_points - i
        if self.health_points > 0:
            return f'{self.name} took {i} damage!\nHealth Points: {self.health_points}'
        elif self.health_points <= 0:
            return self.destroy()


# Humans
class Humanoid(Character):
    def __init__(self, created_at, name, dimensions, health_points, team, weapons, language):
        super().__init__(created_at, name, dimensions, health_points)
        self.team = team
        self.weapons = weapons
        self.language = language

    def greet(self):
        return f'{self.name} offers a greeting in {self.language}.'


# Heros
class Hero(Humanoid):
    def __init__(self, created_at, name, dimensions, health_points, team, weapons, language, armor):
        super().__init__(created_at, name, dimensions,
                         health_points, team, weapons, language)
        self.armor = armor

    def heroic_slash(self, target):
        i = random.randint(1, 6)
        return target.take_damage(i)


# Villains
class Villian(Humanoid):
    def __init__(self, created_at, name, dimensions, health_points, team, weapons, language, magic):
        super().__init__(created_at, name, dimensions,
                         health_points, team, weapons, language)
        self.magic = magic

    def frostbolt(self, target):
        i = random.randint(1, 3)
        return target.take_damage(i)


mage = Humanoid(created_at=datetime.today(), name="Ray", dimensions=[
                2, 1, 1], health_points=10, team="Horde", weapons=["Staff of Shamalama"], language="Common Tongue")


archer = Humanoid(created_at=datetime.today(), name="Brad", dimensions=[
    2, 1, 1], health_points=9, team="Forest Kingdom", weapons=["Bow", "Dagger"], language="Elvish")


hero = Hero(created_at=datetime.today(), name="Ragnar", dimensions=[
    2, 1, 3], health_points=18, team="Northumbria", weapons=["Storm Breaker", "Axe"], language="Danish", armor=8)


villian = Villian(created_at=datetime.today(), name="Loki", dimensions=[
    2, 1, 3], health_points=18, team="Asgard", weapons=["Dagger", "Magic"], language="God", magic=15)


print(mage.name)
print(archer.name)
print(hero.name)
print(villian.name)
print(archer.greet())
print(hero.heroic_slash(villian))

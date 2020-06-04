import random
import datetime
# Game Object


class GameObject:
    def __init__(self, created_at, name, dimensions):
        super().__init__()
        self.created_at = created_at
        self.name = name
        self.dimensions = dimensions

    def destroy(self):
        return 'f{self.name} was removed from the game.'


# Character
class Character(GameObject):
    def __init__(self, created_at, name, dimensions, health_points):
        super().__init__(created_at, name, dimensions)
        self.health_points = health_points

    def take_damage(self, i):
        self.health_points = self.health_points - i
        if self.health_points > 0:
            return 'f{self.name} took {i} damage!\nHealth Points: {self.health_points}'
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
        return 'f{self.name} offers a greeting in {self.language}.'


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

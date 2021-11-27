import random
import numpy as np

class Unit:
    def __init__(self, name, persons):
        self.name = name
        self.persons = persons

class Person:
    def __init__(self, name, weapons):
        self.name = name
        self.weapons = weapons

class Weapon:
    def __init__(self, damage, max_shots):
        self.damage = damage
        self.max_shots = max_shots  # not is use

w0 = Weapon(0, 1)  # attributes by position
w1 = Weapon(max_shots=4, damage=3)  # attributes by name
w2 = Weapon(1, 2)

p1weapons = [w1, w0]
p1 = Person("p1", p1weapons)

p2weapons = w2
p2 = Person("p2", w1)

my_unit_persons = [p1, p2]  # currently units can only have two members
my_unit = Unit("My Unit", my_unit_persons)

# combat
num_fights = 1000
winners = np.zeros(len(my_unit_persons))
for i in range(num_fights):
    if p1weapons[random.randint(0, len(p1weapons) - 1)].damage > p2weapons.damage:
        winners[0] += 1
    else:
        winners[1] += 1

# show result
print(f"p1 has {winners[0]:n} wins")
print(f"p2 has {winners[1]:n} wins")

'''
To Do:
Remove the restriction that there can only be two persons.
Can there be more than two persons in a combat?
If not need to do permutations to get combat opponents
Get rid of names like p1 and make them arrays, i.e. p[1]
Then there will be a two dimensional array - persons by weapons'''
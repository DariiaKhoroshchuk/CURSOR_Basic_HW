"""Survival

1. In the Forest (Iterable) lives Predators and Herbivores (abstract class of animal and two offspring).
Each animal is born with the following parameters (by using random):
- strength (from 25 to 100 points)
- speed (from 25 to 100 points)
The force cannot be greater than it was at birth (initialization).

At each step of the game we take 1 animal from the forest (iteration):
- If it is herbivorous, then it eats (restores its strength by 50%).
- If it is a predator, it hunts - randomly chooses an animal from the forest and:
    - pulled himself out, he was unlucky and he was left without a dinner;
    - pulled out another animal, then tries to catch up;
    - if he can catch up, he catches up and attacks;
    - if attacked and is stronger, then eats and restores 50% of strength;
    - did not catch up or did not have enough strength, then he and the lucky prey lose 30% of strength (Because both
     either ran, or fought, or all together)



An animal whose power has expired dies. (You can check the strength at the time of food search)

The game continues as long as predators are present in the forest.
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Dict, Any
import random
import uuid
import time


class Animal(ABC):

    def __init__(self, power: int, speed: int):
        self.id = None
        self.max_power = power
        self.current_power = power
        self.speed = speed

    @abstractmethod
    def eat(self, forest: Forest):
        raise NotImplementedError


class Predator(Animal):
    # def __init__(self, power: int, speed: int):
    #     super().__init__(power, speed)
    #     self.id = None
    #     self.max_power = power
    #     self.current_power = power
    #     self.speed = speed

    def eat(self, forest: Forest):
        if self.current_power == 0:
            forest.remove_animal(self)
            return
        prey = random.choice(list(forest.animals.values()))
        print(f'Predator {animal.id} is hunting...')
        print(f'The prey is {animal.__class__.__name__} and id is {prey.id}')
        if prey.id == self.id:
            print('Predator pulled himself out, he was unlucky and he was left without a dinner:(')
        else:
            if (self.speed > prey.speed) and (self.current_power > prey.current_power):
                p_current_power = self.current_power
                self.current_power = min(self.current_power + self.max_power * 0.5, self.max_power)
                print(f'Predator {animal.id} has already eaten. Its restores '
                      f'{self.current_power - p_current_power} strength. And its power is {self.current_power}')
                forest.remove_animal(prey.id)
            else:
                print('Predator did not catch up or did not have enough strength...')
                self.current_power = self.current_power - self.max_power * 0.3
                prey.current_power = prey.current_power - prey.max_power * 0.3
                print(f'And now predators power is {self.current_power}, preys power is {prey.current_power}')
                if prey.current_power <= 0:
                    forest.remove_animal(prey.id)
                if self.current_power <= 0:
                    forest.remove_animal(self)
                    print('The predator run out of strength and it died...')


class Herbivorous(Animal):
    # def __init__(self, power: int, speed: int):
    #     super().__init__(power, speed)
    #     self.id = None
    #     self.max_power = power
    #     self.current_power = power
    #     self.speed = speed

    def eat(self, forest: Forest):
        if self.current_power <= 0:
            forest.remove_animal(self)
            return
        if self.current_power > 0:
            print('Herbivorous is eating...')
            herb_current_power = self.current_power
            self.current_power = min(self.current_power + self.max_power * 0.5, self.max_power)
            print(f'Herbivorous {animal.id} has already eaten. Its restores '
                  f'{self.current_power - herb_current_power} strength. '
                  f'And its power is {self.current_power}.')


AnyAnimal: Any[Herbivorous, Predator]


class Forest:

    def __init__(self):
        self.animals: Dict[str, AnyAnimal] = dict()
        self.number = 0

    def add_animal(self, animal: AnyAnimal):
        print(f'Adding a new animal {animal.__class__.__name__} to the forest.'
              f'Its power is {animal.current_power} and its speed is {animal.speed}.')
        self.animals.update({animal.id: animal})

    def remove_animal(self, animal: AnyAnimal):
        print(f'Removing the animal {animal} from the forest.')
        self.animals.pop(animal)

    def any_predator_left(self):
        return not all(isinstance(animal, Herbivorous) for animal in self.animals.values())

    def __iter__(self):
        return self

    def __next__(self):
        self.number += 1
        return self.number


def animal_generator():
    while True:
        generate_animal = random.choice((Predator(random.randint(25, 100), random.randint(25, 100)),
                                         Herbivorous(random.randint(25, 100), random.randint(25, 100))))
        generate_animal.id = uuid.uuid4()
        yield generate_animal


"""if __name__ == "__main__":
    # Create forest
    # Create few animals
    # Add animals to forest
    # Iterate throw forest and force animals to eat until no predators left
    # animal_generator to create a random animal
    pass

Tips:
When a predator hunts, an animal is accidentally taken from the forest.
This animal may be the predator itself. To check this and distinguish two animals with the same characteristics,
use the uuid library. But when creating an animal, assign its id a unique value.

You can use the random library to work with random numbers

If you do not know how to create a forest and look at the survival process, 
here is an example of code that can be used for debugging"""

if __name__ == "__main__":
    nature = animal_generator()

    forest = Forest()
    for i in range(10):
        animal = next(nature)
        forest.add_animal(animal)

    while True:
        if not forest.any_predator_left():
            print('There are no predators in the forest...')
            break
        for animal in list(forest.animals.values()): # adding list()
            animal.eat(forest=forest)
        time.sleep(1)
    print(f'The animals remained in the forest {list(forest.animals.values())}')

# output:
# Adding a new animal Predator to the forest.Its power is 34 and its speed is 40.
# Adding a new animal Herbivorous to the forest.Its power is 51 and its speed is 28.
# Adding a new animal Herbivorous to the forest.Its power is 45 and its speed is 84.
# Adding a new animal Herbivorous to the forest.Its power is 83 and its speed is 60.
# Adding a new animal Herbivorous to the forest.Its power is 76 and its speed is 71.
# Adding a new animal Herbivorous to the forest.Its power is 43 and its speed is 72.
# Adding a new animal Herbivorous to the forest.Its power is 100 and its speed is 62.
# Adding a new animal Herbivorous to the forest.Its power is 36 and its speed is 38.
# Adding a new animal Predator to the forest.Its power is 95 and its speed is 48.
# Adding a new animal Herbivorous to the forest.Its power is 48 and its speed is 29.
# Predator 580f8d93-f6b2-4674-bbad-844184a8621f is hunting...
# The prey is Predator and id is 2f649a85-dda4-4b8e-9d74-09c6b0e6b42b
# Predator did not catch up or did not have enough strength...
# And now predators power is 23.8, preys power is 58.1
# Herbivorous is eating...
# Herbivorous 682e6333-4f8e-443d-a3f8-f67120c89c34 has already eaten. Its restores 0 strength. And its power is 51.
# Herbivorous is eating...
# Herbivorous 6c42ec7a-1af0-449d-98f5-4e954e160a8f has already eaten. Its restores 0 strength. And its power is 45.
# Herbivorous is eating...
# Herbivorous 2f649a85-dda4-4b8e-9d74-09c6b0e6b42b has already eaten. Its restores 24.9 strength. And its power is 83.
# Herbivorous is eating...
# Herbivorous 641bf559-c2a5-4914-997b-ee1751f5373e has already eaten. Its restores 0 strength. And its power is 76.
# Herbivorous is eating...
# Herbivorous f3cdc764-5a49-42de-ac53-9076cf72759d has already eaten. Its restores 0 strength. And its power is 43.
# Herbivorous is eating...
# Herbivorous a39c2b9e-cd2e-475c-9fc5-6a84b2108b0d has already eaten. Its restores 0 strength. And its power is 100.
# Herbivorous is eating...
# Herbivorous a09b25ab-7831-447d-a60b-addc40d33112 has already eaten. Its restores 0 strength. And its power is 36.
# Predator 25429807-cb45-433f-a950-68cdcb2a5eb7 is hunting...
# The prey is Predator and id is 682e6333-4f8e-443d-a3f8-f67120c89c34
# Predator 25429807-cb45-433f-a950-68cdcb2a5eb7 has already eaten. Its restores 0 strength. And its power is 95
# Removing the animal 682e6333-4f8e-443d-a3f8-f67120c89c34 from the forest.
# Herbivorous is eating...
# Herbivorous e4f8297a-5f84-43eb-9333-17a2c2d788d7 has already eaten. Its restores 0 strength. And its power is 48.
# Predator 580f8d93-f6b2-4674-bbad-844184a8621f is hunting...
# The prey is Predator and id is 641bf559-c2a5-4914-997b-ee1751f5373e
# Predator did not catch up or did not have enough strength...
# And now predators power is 13.600000000000001, preys power is 53.2
# Herbivorous is eating...
# Herbivorous 6c42ec7a-1af0-449d-98f5-4e954e160a8f has already eaten. Its restores 0 strength. And its power is 45.
# Herbivorous is eating...
# Herbivorous 2f649a85-dda4-4b8e-9d74-09c6b0e6b42b has already eaten. Its restores 0 strength. And its power is 83.
# Herbivorous is eating...
# Herbivorous 641bf559-c2a5-4914-997b-ee1751f5373e has already eaten. Its restores 22.799999999999997 strength. And its power is 76.
# Herbivorous is eating...
# Herbivorous f3cdc764-5a49-42de-ac53-9076cf72759d has already eaten. Its restores 0 strength. And its power is 43.
# Herbivorous is eating...
# Herbivorous a39c2b9e-cd2e-475c-9fc5-6a84b2108b0d has already eaten. Its restores 0 strength. And its power is 100.
# Herbivorous is eating...
# Herbivorous a09b25ab-7831-447d-a60b-addc40d33112 has already eaten. Its restores 0 strength. And its power is 36.
# Predator 25429807-cb45-433f-a950-68cdcb2a5eb7 is hunting...
# The prey is Predator and id is 2f649a85-dda4-4b8e-9d74-09c6b0e6b42b
# Predator did not catch up or did not have enough strength...
# And now predators power is 66.5, preys power is 58.1
# Herbivorous is eating...
# Herbivorous e4f8297a-5f84-43eb-9333-17a2c2d788d7 has already eaten. Its restores 0 strength. And its power is 48.
# Predator 580f8d93-f6b2-4674-bbad-844184a8621f is hunting...
# The prey is Predator and id is 580f8d93-f6b2-4674-bbad-844184a8621f
# Predator pulled himself out, he was unlucky and he was left without a dinner:(
# Herbivorous is eating...
# Herbivorous 6c42ec7a-1af0-449d-98f5-4e954e160a8f has already eaten. Its restores 0 strength. And its power is 45.
# Herbivorous is eating...
# Herbivorous 2f649a85-dda4-4b8e-9d74-09c6b0e6b42b has already eaten. Its restores 24.9 strength. And its power is 83.
# Herbivorous is eating...
# Herbivorous 641bf559-c2a5-4914-997b-ee1751f5373e has already eaten. Its restores 0 strength. And its power is 76.
# Herbivorous is eating...
# Herbivorous f3cdc764-5a49-42de-ac53-9076cf72759d has already eaten. Its restores 0 strength. And its power is 43.
# Herbivorous is eating...
# Herbivorous a39c2b9e-cd2e-475c-9fc5-6a84b2108b0d has already eaten. Its restores 0 strength. And its power is 100.
# Herbivorous is eating...
# Herbivorous a09b25ab-7831-447d-a60b-addc40d33112 has already eaten. Its restores 0 strength. And its power is 36.
# Predator 25429807-cb45-433f-a950-68cdcb2a5eb7 is hunting...
# The prey is Predator and id is 641bf559-c2a5-4914-997b-ee1751f5373e
# Predator did not catch up or did not have enough strength...
# And now predators power is 38.0, preys power is 53.2
# Herbivorous is eating...
# Herbivorous e4f8297a-5f84-43eb-9333-17a2c2d788d7 has already eaten. Its restores 0 strength. And its power is 48.
# Predator 580f8d93-f6b2-4674-bbad-844184a8621f is hunting...
# The prey is Predator and id is 25429807-cb45-433f-a950-68cdcb2a5eb7
# Predator did not catch up or did not have enough strength...
# And now predators power is 3.400000000000002, preys power is 9.5
# Herbivorous is eating...
# Herbivorous 6c42ec7a-1af0-449d-98f5-4e954e160a8f has already eaten. Its restores 0 strength. And its power is 45.
# Herbivorous is eating...
# Herbivorous 2f649a85-dda4-4b8e-9d74-09c6b0e6b42b has already eaten. Its restores 0 strength. And its power is 83.
# Herbivorous is eating...
# Herbivorous 641bf559-c2a5-4914-997b-ee1751f5373e has already eaten. Its restores 22.799999999999997 strength. And its power is 76.
# Herbivorous is eating...
# Herbivorous f3cdc764-5a49-42de-ac53-9076cf72759d has already eaten. Its restores 0 strength. And its power is 43.
# Herbivorous is eating...
# Herbivorous a39c2b9e-cd2e-475c-9fc5-6a84b2108b0d has already eaten. Its restores 0 strength. And its power is 100.
# Herbivorous is eating...
# Herbivorous a09b25ab-7831-447d-a60b-addc40d33112 has already eaten. Its restores 0 strength. And its power is 36.
# Predator 25429807-cb45-433f-a950-68cdcb2a5eb7 is hunting...
# The prey is Predator and id is 25429807-cb45-433f-a950-68cdcb2a5eb7
# Predator pulled himself out, he was unlucky and he was left without a dinner:(
# Herbivorous is eating...
# Herbivorous e4f8297a-5f84-43eb-9333-17a2c2d788d7 has already eaten. Its restores 0 strength. And its power is 48.
# Predator 580f8d93-f6b2-4674-bbad-844184a8621f is hunting...
# The prey is Predator and id is a09b25ab-7831-447d-a60b-addc40d33112
# Predator did not catch up or did not have enough strength...
# And now predators power is -6.799999999999997, preys power is 25.200000000000003
# Removing the animal 580f8d93-f6b2-4674-bbad-844184a8621f from the forest.
# The predator run out of strength and it died...
# Herbivorous is eating...
# Herbivorous 6c42ec7a-1af0-449d-98f5-4e954e160a8f has already eaten. Its restores 0 strength. And its power is 45.
# Herbivorous is eating...
# Herbivorous 2f649a85-dda4-4b8e-9d74-09c6b0e6b42b has already eaten. Its restores 0 strength. And its power is 83.
# Herbivorous is eating...
# Herbivorous 641bf559-c2a5-4914-997b-ee1751f5373e has already eaten. Its restores 0 strength. And its power is 76.
# Herbivorous is eating...
# Herbivorous f3cdc764-5a49-42de-ac53-9076cf72759d has already eaten. Its restores 0 strength. And its power is 43.
# Herbivorous is eating...
# Herbivorous a39c2b9e-cd2e-475c-9fc5-6a84b2108b0d has already eaten. Its restores 0 strength. And its power is 100.
# Herbivorous is eating...
# Herbivorous a09b25ab-7831-447d-a60b-addc40d33112 has already eaten. Its restores 10.799999999999997 strength. And its power is 36.
# Predator 25429807-cb45-433f-a950-68cdcb2a5eb7 is hunting...
# The prey is Predator and id is 25429807-cb45-433f-a950-68cdcb2a5eb7
# Predator pulled himself out, he was unlucky and he was left without a dinner:(
# Herbivorous is eating...
# Herbivorous e4f8297a-5f84-43eb-9333-17a2c2d788d7 has already eaten. Its restores 0 strength. And its power is 48.
# Herbivorous is eating...
# Herbivorous 6c42ec7a-1af0-449d-98f5-4e954e160a8f has already eaten. Its restores 0 strength. And its power is 45.
# Herbivorous is eating...
# Herbivorous 2f649a85-dda4-4b8e-9d74-09c6b0e6b42b has already eaten. Its restores 0 strength. And its power is 83.
# Herbivorous is eating...
# Herbivorous 641bf559-c2a5-4914-997b-ee1751f5373e has already eaten. Its restores 0 strength. And its power is 76.
# Herbivorous is eating...
# Herbivorous f3cdc764-5a49-42de-ac53-9076cf72759d has already eaten. Its restores 0 strength. And its power is 43.
# Herbivorous is eating...
# Herbivorous a39c2b9e-cd2e-475c-9fc5-6a84b2108b0d has already eaten. Its restores 0 strength. And its power is 100.
# Herbivorous is eating...
# Herbivorous a09b25ab-7831-447d-a60b-addc40d33112 has already eaten. Its restores 0 strength. And its power is 36.
# Predator 25429807-cb45-433f-a950-68cdcb2a5eb7 is hunting...
# The prey is Predator and id is f3cdc764-5a49-42de-ac53-9076cf72759d
# Predator did not catch up or did not have enough strength...
# And now predators power is -19.0, preys power is 30.1
# Removing the animal 25429807-cb45-433f-a950-68cdcb2a5eb7 from the forest.
# The predator run out of strength and it died...
# Herbivorous is eating...
# Herbivorous e4f8297a-5f84-43eb-9333-17a2c2d788d7 has already eaten. Its restores 0 strength. And its power is 48.
# There are no predators in the forest...
# The animals remained in the forest [<__main__.Herbivorous object at 0x7fac22d6e310>, <__main__.Herbivorous object at 0x7fac22d1d310>, <__main__.Herbivorous object at 0x7fac22d1d670>, <__main__.Herbivorous object at 0x7fac22d1d640>, <__main__.Herbivorous object at 0x7fac22d1d700>, <__main__.Herbivorous object at 0x7fac22d29130>, <__main__.Herbivorous object at 0x7fac22d29250>]
#
# Process finished with exit code 0

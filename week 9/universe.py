from planet import Planet
from robot import Robot
from human import Human
import matplotlib.pyplot as plt

import random


class Universe:

    def __init__(self):
        self.planets = []

    def __repr__(self):
        return f"universe(planets={self.planets})"

    def __str__(self):
        return f"The universe contains {len(self.planets)} planets."

    def generate(self):
        for generated_num in range(random.randint(1, 10)):
            # create a new planet using the number from the above for loop as a name
            planet = Planet(f"planet {generated_num}")

            # populate with random humans and robots
            for index in range(random.randint(1, 10)):
                robot = Robot(f"Robot{index}")
                planet.add_robot(robot)

            for index in range(random.randint(1, 10)):
                human = Human(f"Human{index}")
                planet.add_human(human)

            # add to list of planets
            self.planets.append(planet)

    def show_populations(self, selection):
        x_values = []
        y_values = []

        for planet in self.planets:
            x_values.append(planet.name)

            if selection == "humans":
                y_values.append(len(planet.inhabitants['humans']))
            else:
                y_values.append(len(planet.inhabitants['robots']))

        plt.bar(x_values, y_values)
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    universe = Universe()
    universe.generate()
    universe.show_populations("humans")
    universe.show_populations("robots")
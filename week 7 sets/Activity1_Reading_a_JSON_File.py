import json


def read(file_path):
    with open(file_path) as file:
        data = json.load(file)

        place_name = data["location"]
        print(f"Place Name: {place_name}")

        population_size = data["population"]
        print(f"Population Size: {population_size}")

        for bot in data["bots"]:
            name = bot["name"]
            stats = bot["stats"]
            print(f"{name} has the following stats: {stats}")


def run():
    read("futurama.json")


if __name__ == "__main__":
    run()

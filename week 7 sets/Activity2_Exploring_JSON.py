import json


def read_task2(file_path):
    print("Reading...", end="")
    with open(file_path) as file:
        data = json.load(file)
    print("Done!")
    return data


def save(file_path, data):
    print("Exporting...", end="")
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)
    print("Done!")


def run_task2():
    json_data = read_task2("futurama.json")
    save("exported.json", json_data)


if __name__ == "__main__":
    run_task2()


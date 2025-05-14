def observed_items():
    observations = []
    for i in range(7):
        observation=input("Please enter an observation: \n")
        observations.append(observation)
    return observations

def run_task2():
    print("Counting observations...")
    data = observed_items()
    counted_observations = set()
    for item in data:
        counted_observations.add((item, data.count(item)))
    for item, count in counted_observations:
        print(f"{item}: {count}")

run_task2()


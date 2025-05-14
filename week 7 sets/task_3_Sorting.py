def observed_items():
    observations = []
    for i in range(5):
        item = input("Please enter an observation:\n")
        observations.append(item)
    return observations

def remove_observations(observations, responce=None):
    while True:
        response = input("\nDo you wish to remove an observation (yes/no)?\n").strip().lower()
        if response == "yes":
            to_remove = input("\nWhat observation do you wish to remove?\n")
            if to_remove == "yes":
                observations.remove(to_remove)
                print("Done!")
            else:
                print(f"{to_remove} not found in observations.")
                
        elif responce == "no":
            break
        else:
            print("Please enter 'yes' or 'no'")

def run_task3():
    print("Counting observations...")
    observations = observed_items()
    remove_observations(observations)
    unique_items = set(observations)
    sorted_items = sorted(unique_items)
    print("\nObservations:")
    for item in sorted_items:
        count = observations.count(item)
        print(f"{item}: {count}")

run_task3()
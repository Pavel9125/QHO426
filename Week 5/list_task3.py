def directions():
    steps = ["Move Forward","Move Backward", "Turn Left","Turn Right",]
    return steps
def menu():
    print("Please select a direction:")
    step_list = directions()
    for i, direction in enumerate(step_list):
        print(f"{i}: {direction}")
def run_task3():
    menu()

if __name__ == "__main__":
    run_task3()
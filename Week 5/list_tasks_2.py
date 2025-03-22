def movements():
    path = ["Move Forward",10, "Move Backward",5, "Turn Left",3, "Turn Right",1,]
    return path
def run_task2():
    print("Moving... ")
    m=movements()
    print(f"{m[0]} for {m[1]} steps")
    print(f"{m[2]} for {m[3]} steps")
    print(f"{m[4]} for {m[5]} steps")
    print(f"{m[6]} for {m[7]} steps")

if __name__ == "__main__":
    run_task2()

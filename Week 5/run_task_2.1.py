def movements():
    path = ["Move Forward",10, "Move Backward",5, "Turn Left",3, "Turn Right",1,]
    return path
def run_task2():
    print("Moving... ")
    path1=movements()
    for i in range(0,len(path1),2):
        print(f"{path1[i]} for {path1[i+1]} , steps")
if __name__ == "__main__":
    run_task2()

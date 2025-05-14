import matplotlib.pyplot as plt

def coordinate():
    #print ("X Coordinate Value: ")
    #x_coordinate = int(input())
    x_coordinate = int(input("X Coordinate Value: "))
    y_coordinate = int(input("Y Coordinate Value: "))
    return x_coordinate, y_coordinate

def path():
    print("Retrieving path...")

    x_values =[]
    y_values =[]

    for each_time in range(4):
        data = coordinate()
        x_values.append(data[0])
        y_values.append(data[1])

    return[x_values, y_values]

def run_task3():
    values = path()
    value = [[2,10,10,2], [3,3,15,15]]
    values[0].append(value[0][0])
    values[1].append(value[1][0])

    plt.xlabel = "X Coordinate"
    plt.ylabel("Y Coordinate")

    plt.plot(values[0], values[1], "r^--")
    plt.show()

run_task3()
import matplotlib.pyplot as plt
import random as rnd

def data():
    paths = {}

    line_type = input("""Line type: 
    
                :
                -
                --
                        """)
    marker_type = input("""Marker type: 
    
                o
                s
                ^
                        """)

    color_type = input("""Color type: 
                            
                r
                g
                b
                        """)
    paths["line_type"] = line_type
    paths["marker_type"] = marker_type
    paths["color_type"] = color_type

    return paths



def generate():
    number_lines = int(input("Number of lines: "))

    for each_line in range(number_lines):
        values = data() # dictionary

        x_values = rnd.sample(range(1,10), 5)
        y_values = rnd.sample(range(1,10), 5)

        plt.plot(x_values, y_values, f"{values['color_type']}{values['marker_type']}{values['line_type']}")




def run():
    print("Running...")
    generate()
    print("Done")

run()
plt.show()
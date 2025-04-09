import os

def cwd():
    path = os.getcwd()
    print(f"Current working directory: {path}")
    print(f"The directory contains the following files:")
    for file in os.listdir(path):
        print(file)


def run():
    print(dir(os))
    print("Processing.....")
    cwd()

run()

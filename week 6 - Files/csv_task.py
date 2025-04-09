import csv

def read(file_path):
    with open(file_path) as file:
        csv_reader = csv.reader(file)

        headings = next(csv_reader)
        print(f"Headings:\n{headings}")

        print("Values: ")
        for values in csv_reader:
            print(values)

    print("Task Completed")

def run():
    read("clothing.csv")

run()

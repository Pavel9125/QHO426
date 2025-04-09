def search(file_path):
    print("Searching...")
    with open(file_path) as file:
        for location in file:
            print(f"Looked in {location}")
    print("Done")

def run_task():
    search("library.txt")



run_task()

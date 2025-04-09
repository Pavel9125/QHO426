def display_chars(file_path, no_of_characters):
    with open(file_path) as file:
        data = file.read(no_of_characters)
        print("Print from display_chars Function:")
        print(data)


def display_line(file_path):
    with open(file_path) as file:
        data = file.readline().strip()
        print(data)

def display_text (file_path):
    with open(file_path) as file:
        data = file.read()
        print("\nPrint from display_text Function:")
        print(data)

def run_task():
    display_chars("library.txt", no_of_characters=8)
    display_line("library.txt")
    display_text("library.txt")

if __name__ == "__main__":
    run_task()
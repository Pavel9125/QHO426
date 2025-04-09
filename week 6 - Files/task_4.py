def search_books(file_path):
    print("Searching...", end='')
    sections = ""
    books = "Books:\n"
    with open(file_path) as file:
        for line in file:
            if line.startswith("Section"):
                sections += line
            else:
                books += line


    print("Done!")

    return f"{sections}\n\n{books}"

def save(file_path, data):
    print("Saving...", end='')
    with open(file_path, "w") as file:
        file.write(data)
    print("Done.")

def run_task():
    data = search_books("books.txt")
    save("section-books.txt",data)
run_task()



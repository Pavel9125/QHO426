def greeting(name="Guest"):
    print("Hello from my function", name)
greeting("")
greeting()
greeting("Ivan")
greeting("Guest")

def ask_name():
    name = input("What is your name? ")
    return name
user_name = ask_name()
print(f"Hello, {user_name}!")
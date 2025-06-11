def show_title():
    print("=" * 50)
    print("   Disneyland Reviews Analysis System")
    print("=" * 50)

def main_menu():
    print("\nMain Menu:")
    print("A - View Data")
    print("B - View Graphs")
    print("C - Export Data (OOP Task)")
    print("X - Exit")
    return input("Please select an option: ").strip().upper()

def submenu_a():
    print("\nView Data Submenu:")
    print("1 - See all reviews for a specific park")
    print("2 - Number of reviews for park & location")
    print("3 - Average rating for park & year")
    print("4 - Average score per park by reviewer location")
    print("B - Back to main menu")
    return input("Please select an option: ").strip().upper()

def submenu_b():
    print("\nGraphs Submenu:")
    print("1 - Pie chart: number of reviews per park")
    print("2 - Bar chart: average review scores per park")
    print("3 - Top 10 locations for a park")
    print("4 - Average rating per month for a park")
    print("B - Back to main menu")
    return input("Please select an option: ").strip().upper()

def export_menu():
    print("\nExport Menu:")
    print("1 - Export to TXT")
    print("2 - Export to CSV")
    print("3 - Export to JSON")
    print("B - Back to Main Menu")
    return input("Please select an option: ").strip().upper()

def ask_park_name():
    return input("Enter the name of the park: ")

def ask_location():
    return input("Enter the reviewer location: ")

def ask_year():
    return input("Enter the year (e.g. 2018): ")
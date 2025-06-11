from process import load_data, get_reviews_by_park, count_reviews_by_park_and_location, average_rating_by_park_and_year, average_score_per_park_by_location
from visual import pie_chart_reviews_by_park, bar_chart_avg_scores_per_park, top_10_locations_for_park, avg_rating_per_month_for_park
from export import Export
import tui

def main():
    tui.show_title()

    file_path = 'data/Disneyland_reviews.csv'
    data = load_data(file_path)

    if not data:
        print("No data loaded. Exiting program.")
        return

    while True:
        choice = tui.main_menu()

        if choice == 'A':
            submenu_a_loop(data)
        elif choice == 'B':
            submenu_b_loop(data)
        elif choice == 'C':
            exporter = Export(data)
            while True:
                export_choice = tui.export_menu()
                if export_choice == '1':
                    exporter.export_txt("export.txt")
                    print("Exported to export.txt")
                elif export_choice == '2':
                    exporter.export_csv("export.csv")
                    print("Exported to export.csv")
                elif export_choice == '3':
                    exporter.export_json("export.json")
                    print("Exported to export.json")
                elif export_choice == 'B':
                    break
                else:
                    print("Invalid option, please try again.")
        elif choice == 'X':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

def submenu_a_loop(data):
    while True:
        choice = tui.submenu_a()

        if choice == '1':
            park = tui.ask_park_name()
            reviews = get_reviews_by_park(data, park)
            if reviews:
                for r in reviews:
                    print(f"ID:{r['Review_ID']}, Rating:{r['Rating']}, Date:{r['Year_Month']}, Location:{r['Reviewer_Location']}")
            else:
                print("No reviews found for that park.")

        elif choice == '2':
            park = tui.ask_park_name()
            location = tui.ask_location()
            count = count_reviews_by_park_and_location(data, park, location)
            print(f"{count} reviews found for {park} from {location}")

        elif choice == '3':
            park = tui.ask_park_name()
            year = tui.ask_year()
            avg = average_rating_by_park_and_year(data, park, year)
            if avg is not None:
                print(f"Average rating for {park} in {year}: {round(avg, 2)}")
            else:
                print("No data found for that park and year combination.")

        elif choice == '4':
            averages = average_score_per_park_by_location(data)
            for park in averages:
                print(f"\n{park}")
                for location, avg_rating in averages[park].items():
                    print(f"{location}: {avg_rating}")

        elif choice == 'B':
            break
        else:
            print("Invalid option, please try again.")

def submenu_b_loop(data):
    while True:
        choice = tui.submenu_b()

        if choice == '1':
            pie_chart_reviews_by_park(data)

        elif choice == '2':
            bar_chart_avg_scores_per_park(data)

        elif choice == '3':
            park = tui.ask_park_name()
            top_10_locations_for_park(data, park)

        elif choice == '4':
            park = tui.ask_park_name()
            avg_rating_per_month_for_park(data, park)

        elif choice == 'B':
            break
        else:
            print("Invalid option, please try again.")

if __name__ == '__main__':
    main()
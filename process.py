import csv

def load_data(file_path):
    data = []
    try:
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    row['Rating'] = int(row['Rating'])  # convert valid rating
                except ValueError:
                    row['Rating'] = None  # handle missing or invalid rating
                data.append(row)
        print(f"Dataset loaded successfully. Total rows: {len(data)}")
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return data

def get_reviews_by_park(data, park_name):
    reviews = [review for review in data if review['Branch'].lower() == park_name.lower()]
    return reviews

def count_reviews_by_park_and_location(data, park_name, location):
    count = sum(1 for review in data if review['Branch'].lower() == park_name.lower() and review['Reviewer_Location'].lower() == location.lower())
    return count

def average_rating_by_park_and_year(data, park_name, year):
    year = str(year)
    ratings = [
        review['Rating']
        for review in data
        if review['Branch'].lower() == park_name.lower() and review['Year_Month'].startswith(year) and review['Rating'] is not None
    ]
    if ratings:
        return sum(ratings) / len(ratings)
    else:
        return None

def average_score_per_park_by_location(data):
    result = {}
    for review in data:
        park = review['Branch']
        location = review['Reviewer_Location']
        rating = review['Rating']

        if rating is None:
            continue  # skip invalid ratings

        if park not in result:
            result[park] = {}

        if location not in result[park]:
            result[park][location] = []

        result[park][location].append(rating)

    averages = {}
    for park in result:
        averages[park] = {}
        for location in result[park]:
            avg = sum(result[park][location]) / len(result[park][location])
            averages[park][location] = round(avg, 2)

    return averages
import matplotlib.pyplot as plt
from collections import defaultdict
import calendar

def pie_chart_reviews_by_park(data):
    park_counts = defaultdict(int)
    for review in data:
        park_counts[review['Branch']] += 1

    labels = list(park_counts.keys())
    sizes = list(park_counts.values())

    plt.figure(figsize=(8, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title("Number of Reviews per Park")
    plt.show()

def bar_chart_avg_scores_per_park(data):
    park_ratings = defaultdict(list)

    for review in data:
        if review['Rating'] is not None:
            park_ratings[review['Branch']].append(review['Rating'])

    parks = []
    averages = []

    for park, ratings in park_ratings.items():
        parks.append(park)
        averages.append(sum(ratings) / len(ratings))

    plt.figure(figsize=(8, 6))
    plt.bar(parks, averages)
    plt.title("Average Review Scores per Park")
    plt.ylabel("Average Rating")
    plt.xticks(rotation=30)
    plt.ylim(0, 5)
    plt.show()

def top_10_locations_for_park(data, park_name):
    location_ratings = defaultdict(list)

    for review in data:
        if review['Branch'].lower() == park_name.lower() and review['Rating'] is not None:
            location_ratings[review['Reviewer_Location']].append(review['Rating'])

    location_averages = {
        location: sum(ratings) / len(ratings)
        for location, ratings in location_ratings.items()
    }

    top_10 = sorted(location_averages.items(), key=lambda x: x[1], reverse=True)[:10]
    locations, averages = zip(*top_10) if top_10 else ([], [])

    plt.figure(figsize=(10, 6))
    plt.bar(locations, averages)
    plt.title(f"Top 10 Locations for {park_name}")
    plt.ylabel("Average Rating")
    plt.xticks(rotation=45)
    plt.ylim(0, 5)
    plt.show()

def avg_rating_per_month_for_park(data, park_name):
    from collections import defaultdict
    import calendar

    monthly_ratings = defaultdict(list)

    for review in data:
        if review['Branch'].lower() == park_name.lower() and review['Rating'] is not None:
            year_month = review['Year_Month']
            try:
                parts = year_month.split('-')
                if len(parts) < 2:
                    continue
                month = int(parts[1])
                monthly_ratings[month].append(review['Rating'])
            except (ValueError, IndexError):
                continue

    months = range(1, 13)
    averages = [
        sum(monthly_ratings[m]) / len(monthly_ratings[m]) if monthly_ratings[m] else 0
        for m in months
    ]

    month_labels = [calendar.month_abbr[m] for m in months]

    plt.figure(figsize=(10, 6))
    plt.bar(month_labels, averages)
    plt.title(f"Average Rating per Month for {park_name}")
    plt.ylabel("Average Rating")
    plt.ylim(0, 5)
    plt.show()
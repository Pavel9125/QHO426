import csv
import json

class Export:
    def __init__(self, data):
        self.data = data
        self.aggregated_data = self.aggregate_data()

    def aggregate_data(self):
        result = {}

        for review in self.data:
            park = review['Branch']
            location = review['Reviewer_Location']
            rating = review['Rating']

            if rating is None:
                continue

            if park not in result:
                result[park] = {
                    'total_reviews': 0,
                    'positive_reviews': 0,
                    'total_rating': 0,
                    'countries': set()
                }

            result[park]['total_reviews'] += 1
            if rating >= 4:
                result[park]['positive_reviews'] += 1
            result[park]['total_rating'] += rating
            result[park]['countries'].add(location)

        for park in result:
            total = result[park]['total_reviews']
            result[park]['average_rating'] = round(result[park]['total_rating'] / total, 2)
            result[park]['countries'] = len(result[park]['countries'])

        return result

    def export_txt(self, filename):
        with open(filename, 'w', encoding='utf-8') as f:
            for park, stats in self.aggregated_data.items():
                f.write(f"Park: {park}\n")
                for key, value in stats.items():
                    f.write(f"  {key.replace('_', ' ').title()}: {value}\n")
                f.write("\n")

    def export_csv(self, filename):
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            header = ['Park', 'Total Reviews', 'Positive Reviews', 'Average Rating', 'Countries']
            writer.writerow(header)

            for park, stats in self.aggregated_data.items():
                writer.writerow([
                    park,
                    stats['total_reviews'],
                    stats['positive_reviews'],
                    stats['average_rating'],
                    stats['countries']
                ])

    def export_json(self, filename):
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.aggregated_data, f, indent=4)
import json


# Print the statistics as a table
def print_stats(stats: dict):
    print("+-----------------------------+---------+")
    print("| Metric                      | Value   |")
    print("+-----------------------------+---------+")
    for key, value in stats.items():
        print(f"| {key:<27} | {value:>7} |")
    print("+-----------------------------+---------+")


# Save the statistics in JSON format
def save_stats_to_json(stats, filename='output/result.json'):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            # Write the statistics in JSON format with indentation for readability
            json.dump(stats, file, ensure_ascii=False, indent=4)

        print(f"\nResults saved to file: {filename}")
    except Exception as e:
        print(f"Error while saving JSON: {e}")

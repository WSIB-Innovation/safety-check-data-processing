import os
import json
import pandas as pd

BUSINESS_ACTIVITY = "A"


def convert_json_to_csv(folder_path, output_csv_file):
    combined_data = []

    for file_name in os.listdir(folder_path):
        if file_name.endswith("-InjuryStatistics.json"):
            with open(os.path.join(folder_path, file_name), 'r') as file:
                data = json.load(file)
                injury_rates = data.get("injuryRates", [])
                combined_data.extend(injury_rates)

    df = pd.DataFrame(combined_data)

    df = df[['orgId', 'InjuryYear', 'LT_Rate', 'NLT_Rate']]
    df.to_csv(output_csv_file, index=False)
    print(f"CSV file created at {output_csv_file}")


def main():
    convert_json_to_csv(f'business_activities/{BUSINESS_ACTIVITY}', f'{BUSINESS_ACTIVITY}_injury_rates.csv')


if __name__ == "__main__":
    main()

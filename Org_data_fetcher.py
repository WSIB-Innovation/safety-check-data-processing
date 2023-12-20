import requests
import os
import json
import re

BASE_URL = "https://safetycheck.onlineservices.wsib.on.ca/api"
BUSINESS_ACTIVITIES = ["E1", "E2", "E3", "E4", "E5", "E6", "F1", "F2", "G1", "G2",
                       "G3", "G4", "G5", "G6", "H1", "H2", "I1", "I2", "I3", "I4", "J", "K", "L", "M", "N1", "N2", "N3",
                       "O", "P"]


def sanitize_filename(filename):
    """
    Sanitize the filename by removing or replacing characters that are not allowed in file names.
    """
    return re.sub(r'[<>:"/\\|?*]', '_', filename)  # Replace disallowed characters with underscore


def create_directories():
    main_directory = "business_activities"
    os.makedirs(main_directory, exist_ok=True)
    for activity in BUSINESS_ACTIVITIES:
        os.makedirs(os.path.join(main_directory, activity), exist_ok=True)


def fetch_companies(business_activity):
    response = requests.get(
        f"{BASE_URL}/org/search?name=&page=0&size=10&businessActivity={business_activity}&employerSize=Large%20Business")
    if response.status_code != 200:
        return []

    data = response.json()
    total_elements = data['totalElements']

    if total_elements == 0:
        return []

    response = requests.get(
        f"{BASE_URL}/org/search?name=&page=0&size={total_elements}&businessActivity={business_activity}&employerSize=Large%20Business")
    if response.status_code != 200:
        return []

    return response.json()['content']


def fetch_company_data(company_id, company_name, business_activity):
    sanitized_company_name = sanitize_filename(company_name)
    activity_path = os.path.join("business_activities", business_activity)
    os.makedirs(activity_path, exist_ok=True)

    response = requests.get(f"{BASE_URL}/stats/getInjuryStatistics?orgid={company_id}")
    if response.status_code == 200 and response.json():
        with open(os.path.join(activity_path, f"{sanitized_company_name}-InjuryStatistics.json"), 'w') as file:
            json.dump(response.json(), file)

    response = requests.get(f"{BASE_URL}/org/getOrgProfile?lang=en&orgid={company_id}")
    if response.status_code == 200 and response.json():
        with open(os.path.join(activity_path, f"{sanitized_company_name}-OrgProfile.json"), 'w') as file:
            json.dump(response.json(), file)


def main():
    create_directories()
    for activity in BUSINESS_ACTIVITIES:
        companies = fetch_companies(activity)
        if companies:
            for company_id, company_name in companies:
                fetch_company_data(company_id, company_name, activity)


if __name__ == "__main__":
    main()

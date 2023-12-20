# Organization Data Fetcher and Injury Statistics Handler

## Overview
This project consists of two main components designed to fetch and handle data related to injury statistics of different business activities :

1. **Org_data_fetcher.py**: This script is designed to fetch data from a specified API endpoint. It focuses on retrieving companies' information from  various business activities.

2. **Injury_statistics_data_handler.py**: This script handles injury statistics data. It's capable of converting JSON data into a CSV format for easier analysis and manipulation and focuses on injury rates related to a specific business activity.

## Requirements
- Python 3.x
- Libraries: `requests`, `os`, `json`, `re` (for `Org_data_fetcher.py`)
- Libraries: `os`, `json`, `pandas` (for `Injury_statistics_data_handler.py`)

## Installation
To run these scripts, you need to have Python installed on your system. Additionally, install the required libraries using pip:
pip install requests pandas

```
pip install requests pandas
```
## Usage


### Step 1: Fetch Data
Run the **Org_data_fetcher.py** script to fetch the data from the API:
```
python Org_data_fetcher.py
```
### Step 2: Handle Injury Rates
After fetching the data, use **Injury_statistics_data_handler.py** to process the injury statistics for a predefined business activity. The script is currently set up for business activity 'A'.

To change the business activity, modify the `BUSINESS_ACTIVITY` variable in the script to the desired code. Then, run the script:
```
python Injury_statistics_data_handler.py
```

This will process data for the specified business activity and create a CSV file named `{BUSINESS_ACTIVITY}_injury_rates.csv` in the script's directory.
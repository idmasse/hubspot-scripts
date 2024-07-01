# Hubspot API Scripts

These scripts utilize the Hubspot API to fetch all the companies from a HubSpot account and then use those returned company names to find the duplicates that exist. 

## Installation

// clone the repository:

git clone https://github.com/idmasse/hubspot-scripts.git

// cd into the new directory:

cd hubspot-scripts

// install the required packages

pip install -r requirements.txt

// you will need to create a .env file in the same directory and add your HubSpot access token ACCESS_TOKEN = 'access-token-for-hubspot' as a variable

## Usage

// print all hubspot companies
python3 hs_print_companies.py

// print hubspot duplicate company names
python3 hs_dupes.py
from hs_get_all_companies import *

# call the get all companies function and store its result
companies = get_hs_companies()

# iterate over company names and print based on results
if companies:
    print(len(companies), "Company names found in HubSpot:")
    for company in companies:
        print(company.properties.get('name', 'No name property'))
else:
    print("No company names found.")
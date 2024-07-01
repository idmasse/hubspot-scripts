from hs_get_all_companies import *

def find_duplicate_company_names(companies):
    # initalize an empty dict for key : value company data and an empty list for dupes
    name_count = {}
    duplicates = []

    for company in companies:
        name = company.properties.get('name') #loop over companies and extract company names
        if name:
            if name in name_count: # loop over extracted company names
                name_count[name] += 1   
            else:
                name_count[name] = 1

    for name, count in name_count.items():
        if count > 1:
            duplicates.append(name)

    return duplicates

# get all companies and store them in variable
all_companies = get_hs_companies()

# find duplicates and print them
duplicate_company_names = find_duplicate_company_names(all_companies)

if duplicate_company_names:
    print(len(duplicate_company_names), "duplicate company names found:")
    for name in duplicate_company_names:
        print(name)
else:
    print("No duplicate company names found.")

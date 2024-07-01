from hs_auth import *
from hubspot.crm.companies import ApiException

# change these property names for what you need from your hubspot account
PROPERTIES = ["flip_margin", "magicos_status", "name", "magicos_vendor_id", "website", "business_type"]

def get_hs_companies():
    all_companies_list = []
    after_key = None

    try:
        while True:
            # get a page of 100 companies
            response = hs_auth_token().crm.companies.basic_api.get_page(
                limit=100,
                properties=PROPERTIES,
                archived=False,
                after=after_key
            )
            all_companies_list.extend(response.results)  # add the results to the all_companies_list

            # check if theres another page (if paging is true and if it contains a truthy "after" value)
            if response.paging and response.paging.next.after:
                after_key = response.paging.next.after  # update the after_key for the next page
            else:
                break  # exit the loop if no more pages

    except ApiException as e:
        # handle any exceptions that occur during the API call
        print(f"exception when calling companies api: {e}\n")

    return all_companies_list
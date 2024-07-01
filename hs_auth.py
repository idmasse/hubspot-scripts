from hubspot import HubSpot
from hubspot.crm.companies import ApiException
from dotenv import load_dotenv
import os

load_dotenv()

ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')

# authenticate and instantiate a hubspot api client
def hs_auth_token():
    return HubSpot(access_token=ACCESS_TOKEN)
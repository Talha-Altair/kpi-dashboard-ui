import requests
from settings import BACKEND_URL

def get_dashboard_data(username):

    res = requests.get(f"{BACKEND_URL}/dashboard/{username}")

    if res.status_code == 200:

        print(res.json())

        return res.json()
    
    
    else:

        return {}
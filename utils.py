import requests
from settings import BACKEND_URL

def get_dashboard_data(username) -> dict:

    res = requests.get(f"{BACKEND_URL}/dashboard/{username}")

    if res.status_code == 200:

        return res.json()
    
    else:

        return {}
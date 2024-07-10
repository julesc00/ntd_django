import requests
from http import HTTPStatus

from helpers import APIClient
from queries import planets_query


URL = "https://swapi-graphql.netlify.app/.netlify/functions/index"
PLANETS_API_URL = "http://127.0.0.1:8000/api/planets/batch_create/"
TERRAINS_API_URL = "http://127.0.0.1:8000/api/terrains/"
CLIMATES_API_URL = "http://127.0.0.1:8000/api/climates/"


def get_api_data():
    client = APIClient(url=URL, query=planets_query())
    data = client.get()
    return data['data']['allPlanets']['planets']


def add_terrains_or_climates_to_db(url, api_data, field):
    headers = {'Content-Type': 'application/json'}

    # Get current terrains or climates from the API
    try:
        response = requests.get(url)
        json_res = response.json()
        current_db_items = {item["name"] for item in json_res}
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] {e}")
        return

    tmp = {item for planet in api_data for item in planet[field]}  # Using set to remove duplicates
    merged_items = current_db_items ^ tmp  # Get the difference between the two sets
    final_data = [{"name": item} for item in merged_items if merged_items]

    singular_field = field[:-1]
    if not final_data:
        print(f"[INFO] No new {singular_field} to add")
        return
    try:
        for planet in final_data:
            res = requests.post(url, json=planet, headers=headers)
            if res.status_code == HTTPStatus.CREATED:
                print(f"[INFO] {singular_field} Created: {res.json()}")
            else:
                print(f"[INFO] Failed to {singular_field}: {res.json()}")
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] {e}")


def add_planets_to_db(url, query, field):
    client = APIClient(url=URL, query=query)
    temp_planet_data = client.get()
    data = temp_planet_data['data']['allPlanets'][field]
    res = requests.post(url, json=data)
    if res.status_code == HTTPStatus.CREATED:
        print(f"[INFO] Batch Created: {res.json()}")
    else:
        print(f"[INFO] Failed to create batch: {res.json()}")


if __name__ == "__main__":
    # add_terrains_or_climates_to_db(url=TERRAINS_API_URL, api_data=get_api_data(), field="terrains")
    add_terrains_or_climates_to_db(url=CLIMATES_API_URL, api_data=get_api_data(), field="climates")

import concurrent.futures
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
    """
    Add terrains or climates to the database.
    :param url: The URL to post the data to.
    :param api_data: Imported data from GraphQL API to be compared and added.
    :param field: The field to be compared and added.
    :return: None

    """
    headers = {'Content-Type': 'application/json'}

    tmp = {item for planet in api_data for item in planet[field]}  # Using set to remove duplicates
    final_data = [{"name": item} for item in tmp if tmp]

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


def run_task(task):
    url, data, field = task
    add_terrains_or_climates_to_db(url=url, api_data=data, field=field)


if __name__ == "__main__":
    api_data2 = get_api_data()
    tasks = [
        (TERRAINS_API_URL, api_data2, "terrains"),
        (CLIMATES_API_URL, api_data2, "climates")
    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(run_task, task) for task in tasks]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as err:
                print(f"Task raised an exception: {err}")

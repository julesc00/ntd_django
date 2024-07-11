import concurrent.futures
from http import HTTPStatus
from typing import List

import requests

from helpers import APIClient
from queries import planets_query


URL = "https://swapi-graphql.netlify.app/.netlify/functions/index"
PLANETS_API_URL = "http://127.0.0.1:8000/api/api/planets/batch_create/"
TERRAINS_API_URL = "http://127.0.0.1:8000/api/terrains/"
CLIMATES_API_URL = "http://127.0.0.1:8000/api/climates/"


def get_api_data() -> List:
    """
    Get data from the GraphQL API.
    """
    client = APIClient(url=URL, query=planets_query())
    data = client.get()
    return data['data']['allPlanets']['planets']


def add_terrains_or_climates_to_db(url: str, api_data: List, field: str):
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


def add_planets_to_db(url: str, query: str, field: str) -> None:
    """
    Add planets to the database.
    """
    headers = {'Content-Type': 'application/json'}
    client = APIClient(url=URL, query=query)
    temp_planet_data = client.get()
    data = temp_planet_data['data']['allPlanets'][field]
    try:
        for planet in data:
            res = requests.post(url, json=planet, headers=headers)
            if res.status_code != HTTPStatus.CREATED:
                print(f"[INFO] Failed to create batch: {planet['name']}, item already exists.")
            else:
                print(f"[INFO] Created planet: {planet['name']}")
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] {e}")


def run_task(task: tuple) -> None:
    """
    Run the task concurrently.
    """
    url, data, field = task
    add_terrains_or_climates_to_db(url=url, api_data=data, field=field)


if __name__ == "__main__":
    """
    Adding terrains and climates to the database don't depend of each other, 
    so we can run them concurrently.
    """
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

    # Process planets
    add_planets_to_db(url=PLANETS_API_URL, query=planets_query(), field="planets")

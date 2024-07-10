import requests
from http import HTTPStatus

from helpers import APIClient
from queries import planets_query, climates_query, terrains_query


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
    tmp = set()
    for planet in api_data:
        for item in planet[field]:
            tmp.add(item)
    cleaned_data = list(tmp)

    final_data = []

    for item in cleaned_data:
        obj = {"name": item}
        final_data.append(obj)
    for planet in final_data:
        res = requests.post(url, json=planet, headers=headers)
        if res.status_code == HTTPStatus.CREATED:
            print(f"{field[:-1]} Created: {res.json()}")
        else:
            print(f"Failed to {field[:-1]}: {res.json()}")


def add_planets_to_db(url, query, field):
    client = APIClient(url=URL, query=query)
    temp_planet_data = client.get()
    data = temp_planet_data['data']['allPlanets'][field]
    res = requests.post(url, json=data)
    if res.status_code == HTTPStatus.CREATED:
        print(f"Batch Created: {res.json()}")
    else:
        print(f"Failed to create batch: {res.json()}")


if __name__ == "__main__":
    add_terrains_or_climates_to_db(url=TERRAINS_API_URL, api_data=get_api_data(), field="terrains")
    # add_terrains_or_climates_to_db(url=CLIMATES_API_URL, api_data=get_api_data(), field="climates")

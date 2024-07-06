import requests
from http import HTTPStatus

from helpers import APIClient
from queries import planets_query


URL = "https://swapi-graphql.netlify.app/.netlify/functions/index"
API_URL = "http://127.0.0.1:8000/api/planets/batch_create/"

QUERY = planets_query()
# List of records to create

client = APIClient(url=URL, query=QUERY)
data = client.get()
planets_data = data['data']['allPlanets']['planets']

# Make a POST request to the batch_create endpoint with the list of records
response = requests.post(API_URL, json=planets_data)
breakpoint()
if response.status_code == HTTPStatus.CREATED:
    print(f"Batch Created: {response.json()}")
else:
    print(f"Failed to create batch: {response.json()}")

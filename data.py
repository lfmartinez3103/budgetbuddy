import json
import requests
from dotenv import load_dotenv
import os

load_dotenv()

tripadvisor_token = os.getenv("TRIADVISOR_TOKEN")

class Location:
    def __init__(self, location_id, name, address_obj):
        self.location_id = location_id
        self.name = name
        self.address_obj = address_obj

class Address:
    def __init__(self, street1="", street2="", city="", country="", postalcode="", address_string=""):
        self.street1 = street1
        self.street2 = street2
        self.city = city
        self.country = country
        self.postalcode = postalcode
        self.address_string = address_string

def find_search_by_query(query: str, category: str) -> list[Location]:
    query = query.replace(" ", "%20")
    category = category.replace(" ", "%20")
    url = f"https://api.content.tripadvisor.com/api/v1/location/search?key={tripadvisor_token}&searchQuery={query}&category={category}&language=en"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = json.loads(response.text)
        locations = []
        for item in data['data']:
            address_data = item.get('address_obj', {})
            address = Address(**address_data)
            location = Location(item['location_id'], item['name'], address)
            locations.append(location)
        
        return locations
    else:
        print("Error al obtener los datos:", response.status_code)
        return []

result = find_search_by_query("villa de leyva", "hotel")

for loc in result:
    print(f"Location ID: {loc.location_id}")
    print(f"Name: {loc.name}")
    print("Address:")
    print(f"  Street 1: {loc.address_obj.street1}")
    print(f"  City: {loc.address_obj.city}")
    print(f"  Country: {loc.address_obj.country}")
    print()

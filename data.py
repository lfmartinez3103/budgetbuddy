import json
import requests
import models
import models.tripadvisor_response.location_details
import models.tripadvisor_response.location_search
import config
from models.tripadvisor_response.location_details import Location


def find_search_by_query(query: str, category: str) -> list[models.tripadvisor_response.location_search.Location]:
    query = query.replace(" ", "%20")
    category = category.replace(" ", "%20")
    url = f"https://api.content.tripadvisor.com/api/v1/location/search?key={config.tripadvisor_token}&searchQuery={query}&category={category}&language=en"
    headers = {
        "accept": "application/json"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = json.loads(response.text)
        locations = []
        for item in data['data']:
            address_data = item.get('address_obj', {})
            address = models.tripadvisor_response.location_search.Address(**address_data)
            location = models.tripadvisor_response.location_search.Location(item['location_id'], item['name'], address)
            locations.append(location)

        return locations
    else:
        print("Error al obtener los datos: ", response.status_code)
        return []


def get_location_details_by_id(location_id: int) -> Location | None:
    url = f"https://api.content.tripadvisor.com/api/v1/location/{location_id}/details?key={config.tripadvisor_token}&language=en&currency=COP"
    headers = {
        "accept": "application/json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = json.loads(response.text)

        name = data.get("name")
        description = data.get("description")
        web_url = data.get("web_url")
        web_photos = data.get("web_photos")
        address = data.get("address")
        category = data.get("category")
        
        if isinstance(category, dict) and 'localized_name' in category:
            category = category['localized_name']
        
        location_instance = Location(name, description, web_url, web_photos, address, category)
        return location_instance
    else:
        print("Error al obtener los detalles de la ubicación:", response.status_code)
        return None


result = find_search_by_query("villa de leyva", "hotels")

for loc in result:
    print(f"Location ID: {loc.location_id}")
    print(f"Name: {loc.name}")
    print("Address:")
    print(f"  Street 1: {loc.address_obj.street1}")
    print(f"  City: {loc.address_obj.city}")
    print(f"  Country: {loc.address_obj.country}")
    print()

    location_details = get_location_details_by_id(loc.location_id)
    if location_details:
        print("Details:")
        print(f"  Name: {location_details.name}")
        print(f"  Description: {location_details.description}")
        print(f"  Web Url: {location_details.web_url}")
        print(f"  Address: {location_details.address}")
        print(f"  Category: {location_details.category}")
        print()
    else:
        print("No se pudieron obtener los detalles de la ubicación.")

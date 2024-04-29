import json
import requests
import models
import models.tripadvisor_response.location_details
import models.tripadvisor_response.location_search
import config
from models.tripadvisor_response.location_details import Location
from typing import Optional


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


def get_location_details_by_id(location_id: int) -> Optional[Location]:
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
        address = data.get("address_obj", {}).get("address_string")
        category_data = data.get("category")
        category = {"name": category_data.get("name"), "localized_name": category_data.get("localized_name")}
        ranking_data = data.get("ranking_data")
        if ranking_data is not None:
            ranking_instance = models.tripadvisor_response.location_details.RankingData(
                geo_location_id=ranking_data.get("geo_location_id"),
                ranking_string=ranking_data.get("ranking_string"),
                geo_location_name=ranking_data.get("geo_location_name"),
                ranking_out_of=int(ranking_data.get("ranking_out_of")),
                ranking=int(ranking_data.get("ranking")),
            )
        else:
            ranking_instance = None
        rating = data.get("rating")
        if isinstance(rating, (float, int)):
            rating = float(rating)
        else:
            rating = 0.0  # Asigna un valor predeterminado si no se puede convertir a float
        num_reviews = int(data.get("num_reviews"))
        ratings = data.get("review_rating_count")
        subrating_data = data.get("subratings")
        subrating_value = subrating_data.get("0", {}).get("value")
        sub_rating_instance = models.tripadvisor_response.location_details.SubRating(
            name=subrating_data.get("0", {}).get("name"),
            localized_name=subrating_data.get("0", {}).get("localized_name"),
            rating_image_url=subrating_data.get("0", {}).get("rating_image_url"),
            value=float(subrating_value) if subrating_value else 0.0,
        )
        price_level = data.get("price_level")
        amenities = data.get("amenities", [])
        styles = data.get("styles", [])
        trip_types_data = data.get("trip_types", [])
        trip_types = [models.tripadvisor_response.location_details.TripType(trip_data["name"], trip_data["localized_name"], trip_data["value"]) for trip_data in trip_types_data]

        location_instance = Location(
            name=name,
            description=description,
            web_url=web_url,
            web_photos=web_photos,
            address=address,
            category=category,
            ranking_data=ranking_instance,
            rating=rating,
            num_reviews=num_reviews,
            ratings=ratings,
            sub_rating=sub_rating_instance,
            price_level=price_level,
            amenities=amenities,
            styles=styles,
            trip_type=trip_types,
        )
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
    print(f"  Category: {location_details.category['localized_name']}")
    print(f"  Ranking Data:")
    print(f"    Ranking String: {location_details.ranking_data.ranking_string}")
    print(f"    Geo Location Name: {location_details.ranking_data.geo_location_name}")
    print(f"    Ranking Out Of: {location_details.ranking_data.ranking_out_of}")
    print(f"    Ranking: {location_details.ranking_data.ranking}")
    print(f"  Rating: {location_details.rating}")
    print(f"  Number of Reviews: {location_details.num_reviews}")
    print("  Ratings:")
    for rating, count in location_details.ratings.items():
        print(f"    {rating} stars: {count} reviews")
    print("  Sub Ratings:")
    print(f"    Name: {location_details.sub_rating.name}")
    print(f"    Localized Name: {location_details.sub_rating.localized_name}")
    print(f"    Rating Image URL: {location_details.sub_rating.rating_image_url}")
    print(f"    Value: {location_details.sub_rating.value}")
    print(f"  Price Level: {location_details.price_level}")
    print("  Amenities:")
    for amenity in location_details.amenities:
        print(f"    - {amenity}")
    print("  Styles:")
    for style in location_details.styles:
        print(f"    - {style}")
    print("  Trip Types:")
    for trip_type in location_details.trip_type:
        print(f"    - {trip_type.localized_name} ({trip_type.value})")
    print()
else:
    print("No se pudieron obtener los detalles de la ubicación.")

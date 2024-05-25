import json
import requests
import models
import models.tripadvisor_response.location_details
import models.tripadvisor_response.location_search
import config
from models.tripadvisor_response.location_details import Location
from typing import Optional


def find_search_by_query(query: str, category: str) -> list[models.tripadvisor_response.location_search.Location] | ValueError:
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
            location = models.tripadvisor_response.location_search.Location(
                location_id=int(item.get("location_id", -1)),
                name=item.get("name", "Name not found"),
                address_obj=models.tripadvisor_response.location_search.Address(
                    street1=item.get("address_obj", {}).get("street1", "Street1 not found"),
                    street2=item.get("address_obj", {}).get("street2", "Street2 not found"),
                    city=item.get("address_obj", {}).get("city", "City not found"),
                    country=item.get("address_obj", {}).get("country", "Country not found"),
                    postalcode=item.get("address_obj", {}).get("postalcode", "Postalcode not found"),
                    address_string=item.get("address_obj", {}).get("address_string", "Address not found")
                ))

            locations.append(location)

        return locations
    else:
        return ValueError("Error at finding search by query: ", response.status_code)

def get_location_details_by_id(location_id: int) -> Location | ValueError:
    url = f"https://api.content.tripadvisor.com/api/v1/location/{location_id}/details?key={config.tripadvisor_token}&language=en&currency=COP"
    headers = {
        "accept": "application/json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = json.loads(response.text)
        
        location_obj = models.tripadvisor_response.location_details.Location(
            name=data.get("name", "Name not found"),
            description=data.get("description", "Description not found"),
            web_url=data.get("web_url", "Web Url not found"),
            web_photos=data.get("web_photos", " Web Photos not found"),
            address=data.get("address_obj", {}).get("address_string", "Address not found"),
            category=data.get("category", {}).get("localized_name", "Category not found"),
            ranking_data=models.tripadvisor_response.location_details.RankingData(
                geo_location_id=data.get("ranking_data", {}).get("geo_location_id", -1),
                ranking_string=data.get("ranking_data", {}).get("ranking_string", "Ranking String not found"),
                geo_location_name=data.get("ranking_data", {}).get("geo_location_name", "Geo Location Name not found"),
                ranking_out_of=data.get("ranking_data", {}).get("ranking_out_of", -1),
                ranking=data.get("ranking_data", {}).get("ranking", -1)
            ),
            rating=float(data.get("rating", -1.0)),
            num_reviews=int(data.get("num_reviews", -1)),
            review_rating_count=models.tripadvisor_response.location_details.ReviewRatingCount( 
                one=int(data.get("review_rating_count", {}).get("1", -1)),
                two=int(data.get("review_rating_count", {}).get("2", -1)),
                three=int(data.get("review_rating_count", {}).get("3", -1)),
                four=int(data.get("review_rating_count", {}).get("4", -1)),
                five=int(data.get("review_rating_count", {}).get("5", -1))
            ),
            sub_rating=models.tripadvisor_response.location_details.SubRating(
                name=data.get("sub_rating", {}).get("name", "Name not found"),
                localized_name=data.get("sub_rating", {}).get("localized_name", "Localized Name not found"),
                rating_image_url=data.get("sub_rating", {}).get("rating_image_url", "Rating Image Url not found"),
                value=float(data.get("sub_rating", {}).get("value", -1.0))
            ),
            price_level=data.get("price_level", "Price Level not found"),
            amenities=data.get("amenities", ["Amentities not found"]),
            features=data.get("features", ["Features not found"]),
            styles=data.get("styles", ["Styles not found"]),
            trip_type=models.tripadvisor_response.location_details.TripType(
                name=data.get("trip_type", {}).get("name", "Name not found"),
                localized_name=data.get("trip_type", {}).get("localized_name", "Localized Name not found"),
                value=data.get("trip_type", {}).get("value", "Value not found")
            )
        )

        return location_obj

    else:
        return ValueError("Error at getting location details: ", response.status_code)
    
def search_best_hotel_and_restaurant(destination: str, budget: str, trip_type: str ="") -> list[str] | ValueError:
    # TODO: Validar dependiendo del  tipo de viaje
    # DONE: Filtrar por presupuesto (supongo)
    hotels: list[Location] = find_search_by_query(destination, "hotels")
    restaurants = find_search_by_query(destination, "restaurants")
    
    hotels_full_details = [get_location_details_by_id(x.location_id) for x in hotels]
    restaurants_full_details = [get_location_details_by_id(x.location_id) for x in restaurants]

    if hotels and restaurants:
        
        hotels_matching_price = list(filter(   
            lambda x: x.price_level == budget, hotels_full_details
        ))

        restaurants_matching_price = list(filter(
            lambda x: x.price_level == budget, restaurants_full_details
        ))

        if hotels_matching_price and restaurants_matching_price:
           
            return hotels_matching_price[0].name, restaurants_matching_price[0].name
        else:
            return hotels[0].name , restaurants[0].name
    else:
        return ValueError("Error at searching best hotel and restaurant")    

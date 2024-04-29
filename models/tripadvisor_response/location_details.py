from typing import List

class RankingData:
    def __init__(self,
                 geo_location_id: int,
                 ranking_string: str,
                 geo_location_name: str,
                 ranking_out_of: int,
                 ranking: int,
                ):
        self.geo_location_id = geo_location_id
        self.ranking_string = ranking_string
        self.geo_location_name = geo_location_name
        self.ranking_out_of = ranking_out_of
        self.ranking = ranking

class SubRating:
    def __init__(self,
                 name: str, 
                 localized_name: str, 
                 rating_image_url: str, 
                 value: float | None
                ):
        self.name = name
        self.localized_name = localized_name
        self.rating_image_url = rating_image_url
        self.value = value

class TripType:
    def __init__(self, name: str, localized_name: str, value: str):
        self.name = name
        self.localized_name = localized_name
        self.value = value

class Location:
    def __init__(self,
                 name: str,
                 description: str,
                 web_url: str,
                 web_photos: str,
                 address: str,
                 category: dict,
                 ranking_data: RankingData,
                 rating: float,
                 num_reviews: int,
                 ratings: dict,
                 sub_rating: SubRating,
                 price_level: str,
                 amenities: List[str],
                 styles: List[str],
                 trip_type: TripType
                ):
        self.name = name
        self.description = description
        self.web_url = web_url
        self.web_photos = web_photos
        self.address = address
        self.category = category
        self.ranking_data = ranking_data
        self.rating = rating
        self.num_reviews = num_reviews
        self.ratings = ratings
        self.sub_rating = sub_rating
        self.price_level = price_level
        self.amenities = amenities
        self.styles = styles
        self.trip_type = trip_type
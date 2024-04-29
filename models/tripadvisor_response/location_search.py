class Address:
    def __init__(self, 
                 street1: str="",
                 street2: str="",
                 city: str="",
                 country: str="",
                 postalcode: str="",
                 address_string: str=""):
        self.street1 = street1
        self.street2 = street2
        self.city = city
        self.country = country
        self.postalcode = postalcode
        self.address_string = address_string


class Location:
    def __init__(self,
                 location_id: int,
                 name: str,
                 address_obj: Address):
        self.location_id = location_id
        self.name = name
        self.address_obj = address_obj




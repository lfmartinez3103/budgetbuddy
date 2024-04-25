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


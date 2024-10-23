from app.models.baseModel import BaseModel

class Place(BaseModel):
    def __init__(self, title, description, price, latitude, longitude, owner_id):
        super().__init__()
        valid_place_description = self.place_length(description)
        if isinstance(valid_place_description, tuple):
            raise ValueError(valid_place_description[0])
        if price <= 0:
            raise ValueError("Price must be positive")
        if not (-90.0 <= latitude <= 90.0):
            raise ValueError("Latitude must be between -90 and 90")
        if not (-180.0 <= longitude <= 180.0):
            raise ValueError("Longitude must be between -180 and 180")

        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner_id = owner_id
        self.reviews = []
        self.amenities = []

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'price': self.price,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'owner_id': self.owner_id,
            'reviews': [review.to_dict() for review in self.reviews],
            'amenities': self.amenities
        }

    def add_review(self, review):
        if review.user and review.place:
            self.reviews.append(review)


    def add_amenity(self, amenity):
        if amenity not in self.amenities:
            self.amenities.append(amenity)

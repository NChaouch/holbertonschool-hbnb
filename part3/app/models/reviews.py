from app.models.baseModel import BaseModel

class Review(BaseModel):
    def __init__(self, text, rating, owner_id, place_id):
        super().__init__()
        if not (1 <= rating <= 5):
            raise ValueError("Rating must be between 1 and 5")

        self.text = text
        self.rating = rating
        self.owner_id = owner_id
        self.place_id = place_id

    def to_dict(self):
        return {
            'id': self.id,
            'text': self.text,
            'rating': self.rating,
            'owner_id': self.owner_id,
            'place_id': self.place_id
        }

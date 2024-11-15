from app.models.baseModel import BaseModel
from app import db
import uuid

class Amenity(BaseModel):
    __tablename__ = 'amenities'
    
    id = id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(50), nullable=False)

    def update(self, data):
        if 'name' in data:
            # Vérification que le nom n'est pas vide
            if not data['name'] or not data['name'].strip():
                raise ValueError("Field 'name' cannot be empty.")
            valid_name = self.name_length('name', data['name'], 50)
            if isinstance(valid_name, tuple):
                raise ValueError(valid_name[0])
            self.name = data['name']

    def to_dict(self):
        """Convert the Amenity object into a dictionary."""
        return {
            'name': self.name
        }

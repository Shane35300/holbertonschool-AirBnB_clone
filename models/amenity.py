from models.base_model import BaseModel

class Amenity(BaseModel):
    """
    Amenity class that inherits from BaseModel.
    """

    # Public class attributes
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialization of Amenity"""
        super().__init__(*args, **kwargs)

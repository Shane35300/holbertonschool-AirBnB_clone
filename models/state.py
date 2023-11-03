from models.base_model import BaseModel

class State(BaseModel):
    """
    State class that inherits from BaseModel.
    """

    # Public class attributes
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialization of State"""
        super().__init__(*args, **kwargs)

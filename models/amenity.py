#!/usr/bin/python3
# -*- coding: utf-8 -*-

from models.base_model import BaseModel

class Amenity(BaseModel):
    """
    Amenity class that inherits from BaseModel

    Attributes:
        name (str): Public class attribute for Amenity name
    """
    name = ""


    def __init__(self, *args, **kwargs):
        """
        init method for Amenity class

        Attributes:
            args (list): The list with arguments
            kwargs (dict): A dictionary with arguments
        """
        super().__init__(*args, **kwargs)
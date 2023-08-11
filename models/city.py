#!/usr/bin/python3
# -*- coding: utf-8 -*-

from models.base_model import BaseModel

class City(BaseModel):
    """
    city class that inherits from BaseModel

    Attributes:
        state_id (str): Public class attribute for city id
        name (str): Public class attribute for City name
    """
    state_id = ""
    name = ""


    def __init__(self, *args, **kwargs):
        """
        init method for User class

        Attributes:
            args (list): The list with arguments
            kwargs (dict): A dictionary with arguments
        """
        super().__init__(*args, **kwargs)
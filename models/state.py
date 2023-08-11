#!/usr/bin/python3
# -*- coding: utf-8 -*-

from models.base_model import BaseModel


class State(BaseModel):
    """
    State class that inherits from BaseModel

    Attributes:
        name (str): Public class attribute for States name
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
        init method for User class

        Attributes:
            args (list): The list with arguments
            kwargs (dict): A dictionary with arguments
        """
        super().__init__(*args, **kwargs)
from abc import ABC, abstractmethod


class Businessobject(ABC):

    def __init__(self):
        self.id = 0

    def set_id(self, value):
        """Setzen der ID."""
        self.id = value

    def get_id(self):
        """Auslesen der ID."""
        return self.id
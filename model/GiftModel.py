class Gift:
    def __init__(self, gift_id, name):
        self._gift_id = gift_id
        self._name = name

    @property
    def gift_id(self):
        return self._gift_id

    @gift_id.setter
    def gift_id(self, gift_id):
        self._gift_id = gift_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def __str__(self):
        return (f"Gift ID: {self.gift_id}\n"
                f"  Name: {self.name}\n")
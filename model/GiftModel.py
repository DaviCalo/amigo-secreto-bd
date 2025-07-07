class Gift(object):
    @property
    def gift_id(self):
        return self._gift_id

    @gift_id.setter
    def gift_id(self, gift_id):
        self._gift_id = gift_id

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, name):
        self._name = name
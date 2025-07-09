class Group:
    def __init__(self, group_id, name, description, status_group,
                 maximum_value, minimum_value, draw_date,
                 meet_date, location, created_user_id):
        self._group_id = group_id
        self._name = name
        self._description = description
        self._status_group = status_group
        self._maximum_value = maximum_value
        self._minimum_value = minimum_value
        self._draw_date = draw_date
        self._meet_date = meet_date
        self._location = location
        self._created_user_id = created_user_id

    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        self._group_id = group_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def status_group(self):
        return self._status_group

    @status_group.setter
    def status_group(self, status_group):
        self._status_group = status_group

    @property
    def maximum_value(self):
        return self._maximum_value

    @maximum_value.setter
    def maximum_value(self, maximum_value):
        self._maximum_value = maximum_value

    @property
    def minimum_value(self):
        return self._minimum_value

    @minimum_value.setter
    def minimum_value(self, minimum_value):
        self._minimum_value = minimum_value

    @property
    def draw_date(self):
        return self._draw_date

    @draw_date.setter
    def draw_date(self, draw_date):
        self._draw_date = draw_date

    @property
    def meet_date(self):
        return self._meet_date

    @meet_date.setter
    def meet_date(self, meet_date):
        self._meet_date = meet_date

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, location):
        self._location = location

    @property
    def created_user_id(self):
        return self._created_user_id

    @created_user_id.setter
    def created_user_id(self, created_user_id):
        self._created_user_id = created_user_id

    def __str__(self):
        return (f"Group ID: {self.group_id}\n"
                f"  Name: {self.name}\n"
                f"  Description: {self.description}\n"
                f"  Status: {self.status_group}\n"
                f"  Max Value: {self.maximum_value}\n"
                f"  Min Value: {self.minimum_value}\n"
                f"  Draw Date: {self.draw_date}\n"
                f"  Meet Date: {self.meet_date}\n"
                f"  Location: {self.location}\n"
                f"  Created By User ID: {self.created_user_id}")
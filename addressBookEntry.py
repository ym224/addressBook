class Entry():
    def __init__(self, sid, first_name, last_name, address, city, state, zip_code, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone = phone

    def sid(self):
        return self.sid

    def sid(self, value):
        self.sid = value


    def first_name(self):
        return self.first_name

    def first_name(self, value):
        self.first_name = value

    def last_name(self):
        return self.last_name

    def last_name(self, value):
        self.last_name = value

    def address(self):
        return self.address

    def address(self, value):
        self.address = value

    def city(self):
        return self.city

    def city(self, value):
        self.city = value

    def state(self):
        return self.state

    def state(self, value):
        self.state = value

    def zip_code(self):
        return self.zip_code

    def zip_code(self, value):
        self.zip_code = value

    def phone_number(self):
        return self.phone_number

    def phone_number(self, value):
        self.phone_number = value

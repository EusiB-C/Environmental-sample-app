class Sample:
    def __init__(self, name, location, ph_value):
        self.name = name
        self.location = location
        self.ph_value = ph_value

    def set_ph_value(self, amount):
        if amount < 0:
            print("pH value cannot be below 0")
        else:
            self.ph_value = amount

    def display_info(self):
        print(f"Sample Name: {self.name}")
        print(f"Location: {self.location}")
        print(f"pH Value: {self.ph_value}")




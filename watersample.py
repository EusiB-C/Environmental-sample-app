from sample import Sample
class WaterSample(Sample):
    def __init__(self, name, location, ph_value, salinity):
        super().__init__(name, location, ph_value)
        self.salinity = salinity

    def set_salinity(self, amount):
        if amount < 0:
            print("Salinity cannot be below 0")
        else:
            self.salinity = amount

    def display_info(self):
        super().display_info()
        print(f"Salinity: {self.salinity}")


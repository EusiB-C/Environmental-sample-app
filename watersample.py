from sample import Sample
class WaterSample(Sample): #creates water samples as a subclass of Sample, adding salinity as an additional attribute
    def __init__(self, name, location, ph_value, salinity):
        super().__init__(name, location, ph_value) #super() calls the parent class Sample to use name, location, and ph_value attributes
        self.salinity = salinity

    def set_salinity(self, amount):
        if amount < 0:
            print("Salinity cannot be below 0")
        else:
            self.salinity = amount

    def display_info(self):
        super().display_info()
        print(f"Salinity: {self.salinity} mg/L")


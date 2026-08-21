from sample import Sample
class SoilSample(Sample):
    def __init__(self, name, location, ph_value, pb_value):
        super().__init__(name, location, ph_value)
        self.pb_value = pb_value

    def set_pb_value(self, amount):
        if amount < 0:
            print("Lead content cannot be below 0")
        else:
            self.pb_value = amount
    

    def display_info(self):
        super().display_info()
        print(f"Lead Content: {self.pb_value} ppm")
        
        if self.pb_value >= 80:
            print("Warning: Lead content exceeds safe levels!")


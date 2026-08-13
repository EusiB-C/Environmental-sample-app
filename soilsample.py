from sample import Sample
class SoilSample(Sample):
    def __init__(self, name, location, ph_value, pb_value):
        super().__init__(name, location, ph_value)
        self.pb_value = pb_value
    
    def display_info(self):
        super().display_info()
        print(f"Lead Content: {self.pb_value}")


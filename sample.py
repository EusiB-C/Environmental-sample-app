class Sample:
    def __init__(self, name, location, ph_value):
        self.name = name
        self.location = location
        self.ph_value = ph_value

    def display_info(self):
        print(f"Sample Name: {self.name}")
        print(f"Location: {self.location}")
        print(f"pH Value: {self.ph_value}")

sample1 = Sample("Water Sample A", "Berkeley Marina", 7.2)
sample2 = Sample("Soil Sample A", "Joaquin Miller Park", 6.5)
sample1.display_info()
print()
sample2.display_info()


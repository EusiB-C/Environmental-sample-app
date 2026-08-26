from soilsample import SoilSample
from watersample import WaterSample




class Lab:
    def __init__(self):
        self.samples = [] # creates an empty list to store samples

    def add_sample(self, sample):
        self.samples.append(sample)

    def display_all_samples(self):
        for sample in self.samples:
            sample.display_info()
            print()
    
    def sample_count(self):
        return len(self.samples)


    def flagged_count(self):
        count = 0

        for sample in self.samples:
            if isinstance(sample, SoilSample) and sample.pb_value >= 80: #if the sample is a soil sample and its pb > or = 80, increase the count
                count += 1

        return count

    
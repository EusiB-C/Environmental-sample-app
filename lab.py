from soilsample import SoilSample
from watersample import WaterSample




class Lab:
    def __init__(self):
        self.samples = []

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
            if isinstance(sample, SoilSample) and sample.pb_value >= 80:
                count += 1

        return count

    
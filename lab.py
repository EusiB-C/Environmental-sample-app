from soilsample import SoilSample
from watersample import WaterSample

sample1 = WaterSample("Water Sample A", "Berkeley Marina", 7.2, 0.5)
sample2 = SoilSample("Soil Sample A", "Joaquin Miller Park", 6.5, 0.3)
sample3 = WaterSample("Water Sample B", "Lake Merritt", 8.1, 0.7)
sample4 = SoilSample("Soil Sample B", "Bella Vista Park", 5.8, 0.2)

samples = [sample1, sample2, sample3, sample4]

for sample in samples:
    sample.display_info()
    print()
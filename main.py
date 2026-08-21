from soilsample import SoilSample
from watersample import WaterSample
from lab import Lab

def main():
    print("Welcome to your environmental sample manager!")
    
    lab = Lab()
    
    while True:
        print("\nWhat would you like to do?")
        print("1. Add a sample")
        print("2. Display all samples")
        print("3. Display sample count")
        print("4. Display flagged soil samples")
        print("5. Quit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            sample_type = input("Enter sample type (soil/water) or 'done' to finish: ").lower()
        

            if sample_type == "soil":
                name = input("Enter sample name: ")
                location = input("Enter sample location: ")
                try:
                    ph_value = float(input("Enter pH value: "))
                except ValueError:
                    print("Please enter a valid number.")
                    continue

                try:
                    pb_value = float(input("Enter lead content: "))
                except ValueError:
                    print("Please enter a valid number.")
                    continue
                
                new_sample = SoilSample(name, location, ph_value, pb_value)
                lab.add_sample(new_sample)


            elif sample_type == "water":
                name = input("Enter sample name: ")
                location = input("Enter sample location: ")
                try:
                    ph_value = float(input("Enter pH value: "))
                except ValueError:
                    print("Please enter a valid number.")
                    continue

                try:
                    salinity = float(input("Enter salinity: "))
                except ValueError:
                    print("Please enter a valid number.")
                    continue

                new_sample = WaterSample(name, location, ph_value, salinity)
                lab.add_sample(new_sample)
            
            elif sample_type == "done":
                print("Finished adding samples. Returning to main menu.")


            else:
                print("Invalid sample type. Please enter 'soil', 'water', or 'done'.")
        
        elif choice == "2":
            lab.display_all_samples()
            if lab.sample_count() == 0:
                print("No samples to display.")
        
        elif choice == "3":
            print(f"Total number of samples: {lab.sample_count()}")
            if lab.sample_count() == 0:
                print("No samples have been added yet.")
        
        elif choice == "4":
            print(f"Number of flagged soil samples: {lab.flagged_count()}")
            if lab.flagged_count() == 0:
                print("No flagged soil samples to display.")
        
        elif choice == "5" or choice == "quit":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-5.")
    


main()
from soilsample import SoilSample
from watersample import WaterSample
from lab import Lab

def main():
    print("Welcome to your environmental sample manager!")
    print()
    lab = Lab() #creates an empty lab object to store samples
    
    while True:
        print("What would you like to do?")
        print()
        print("1. Add a sample")
        print("2. Display all samples")
        print("3. Display sample count")
        print("4. Display flagged soil samples")
        print("5. Quit")
        print()
        choice = input("Enter your choice: ")

        if choice == "1":
            print()
            sample_type = input("Enter sample type (soil/water) or 'done' to finish: ").lower()
        

            if sample_type == "soil":
                print()
                name = input("Enter sample name: ")
                print()
                location = input("Enter sample location: ")
                print()
                while True: #if the user enters a  value for pH that isnt a number, this prompts them to enter a valid number
                    try:
                        ph_value = float(input("Enter pH value: "))
                        break
                    except ValueError:
                        print("Please enter a valid number.")
                print()
                while True: #same here, but for lead content
                    try:
                        pb_value = float(input("Enter lead content: "))
                        break
                    except ValueError:
                        print("Please enter a valid number.")
                
                new_sample = SoilSample(name, location, ph_value, pb_value)
                lab.add_sample(new_sample)


            elif sample_type == "water":
                print()
                name = input("Enter sample name: ")
                print()
                location = input("Enter sample location: ")
                print()
                while True: #same here
                    try:
                        ph_value = float(input("Enter pH value: "))
                        break
                    except ValueError:
                        print("Please enter a valid number.")
                print()
                while True: #same here, but for salinity
                    try:
                        salinity = float(input("Enter salinity: "))
                        break
                    except ValueError:
                        print("Please enter a valid number.")

                new_sample = WaterSample(name, location, ph_value, salinity)
                lab.add_sample(new_sample)
            
            elif sample_type == "done":
                print("Finished adding samples. Returning to main menu.")


            else:
                print("Invalid sample type. Please enter 'soil', 'water', or 'done'.")
        
        elif choice == "2":
            print()
            lab.display_all_samples()
            if lab.sample_count() == 0:
                print("No samples to display.")
        
        elif choice == "3":
            print()
            if lab.sample_count() == 0:
                print("No samples have been added yet.")
            else:
                print(f"Total number of samples: {lab.sample_count()}")
        
        elif choice == "4":
            print()
            print(f"Number of flagged soil samples: {lab.flagged_count()}")
            if lab.flagged_count() == 0:
                print("No flagged soil samples to display.")
        
        elif choice == "5" or choice == "quit":
            print()
            print("Exiting the app. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-5.")
    


main()
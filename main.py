import functions

def main():
    while True:
        print("\n--- 💪 GYM TRACKER MENU ---")
        print("1. Add Workout")
        print("2. View All Workouts")
        print("3. Filter by Day")
        print("4. Delete Workout")
        print("5. Weekly Summary")
        print("6. Exit")
        
        choice = input("\nSelect an option (1-6): ")

        if choice == '1':
            day = input("Enter Day (Mon-Sun): ")
            name = input("Exercise Name: ")
            try:
                sets = int(input("Number of Sets: "))
                reps = int(input("Number of Reps: "))
                weight = float(input("Weight (kg): "))
                functions.add_workout(day, name, sets, reps, weight)
            except ValueError:
                print("❌ Invalid input! Sets, reps, and weight must be numbers.")

        elif choice == '2':
            functions.view_workouts()

        elif choice == '3':
            day = input("Enter day to filter by: ")
            functions.view_workouts(filter_day=day)

        elif choice == '4':
            functions.view_workouts()
            try:
                idx = int(input("\nEnter the ID number to delete: "))
                functions.delete_workout(idx)
            except ValueError:
                print("❌ Please enter a valid number.")

        elif choice == '5':
            functions.get_weekly_summary()

        elif choice == '6':
            print("👋 Goodbye! Keep up the hard work!")
            break
        
        else:
            print("❌ Invalid selection, please try again.")

if __name__ == "__main__":
    main()

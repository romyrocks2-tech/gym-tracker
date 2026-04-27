import json
import os

FILE_NAME = "workouts.json"

def load_data():
    """Loads the workout data from the JSON file."""
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError):
        return []

def save_data(workouts):
    """Saves the workout list to the JSON file."""
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(workouts, file, indent=4)
    except IOError as e:
        print(f"❌ Error saving data: {e}")

def add_workout(day, exercise, sets, reps, weight):
    """Adds a new workout entry."""
    workouts = load_data()
    new_entry = {
        "day": day.capitalize(),
        "exercise": exercise,
        "sets": sets,
        "reps": reps,
        "weight": weight
    }
    workouts.append(new_entry)
    save_data(workouts)
    print("\n✅ Workout added successfully!")

def format_workout(index, workout):
    """Returns a formatted string for a single workout."""
    return f"{index}. [{workout['day']}] {workout['exercise']} | {workout['sets']} sets x {workout['reps']} reps @ {workout['weight']}kg"

def view_workouts(filter_day=None):
    """Displays workouts, optionally filtered by day."""
    workouts = load_data()
    if not workouts:
        print("\n📅 No workouts found. Time to hit the gym!")
        return

    print("\n--- 🏋️ Your Workout Log ---")
    found = False
    for i, w in enumerate(workouts, 1):
        if filter_day is None or w['day'].lower() == filter_day.lower():
            print(format_workout(i, w))
            found = True
    
    if not found and filter_day:
        print(f"No workouts found for {filter_day}.")

def delete_workout(index):
    """Deletes a workout by its list index."""
    workouts = load_data()
    try:
        # Convert 1-based index to 0-based
        removed = workouts.pop(index - 1)
        save_data(workouts)
        print(f"\n🗑️ Deleted: {removed['exercise']} on {removed['day']}")
    except (IndexError, ValueError):
        print("\n❌ Invalid ID. Please check the 'View Workouts' list for the correct number.")

def get_weekly_summary():
    """Calculates and displays workout statistics."""
    workouts = load_data()
    if not workouts:
        print("\n📊 No data available for summary.")
        return

    total_count = len(workouts)
    
    # Calculate most frequent exercise
    exercise_counts = {}
    for w in workouts:
        ex = w['exercise'].lower()
        exercise_counts[ex] = exercise_counts.get(ex, 0) + 1
    
    # Find the key with the maximum value
    most_frequent = max(exercise_counts, key=exercise_counts.get)

    print("\n--- 📈 Weekly Summary ---")
    print(f"Total Workouts logged: {total_count}")
    print(f"Most frequent exercise: {most_frequent.capitalize()} ({exercise_counts[most_frequent]} times)")
    print("-------------------------")

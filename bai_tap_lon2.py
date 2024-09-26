# Initialize a dictionary to store events
schedule = {}

def main_menu():
    print("\nSelect an option:")
    print("1. Add event")
    print("2. View schedule")
    print("3. Edit event")
    print("4. Exit")
    return int(input("Enter the number corresponding to your choice: "))

def validate_input(value, name):
    if not value.isdigit():
        print(f"Invalid input for {name}. Please enter a number.")
        return False
    return True

def add_event():
    while True:
        month = input("Enter the month (as a number): ")
        if validate_input(month, "month") and 1 <= int(month) <= 12:
            break

    while True:
        week = input("Enter the week (as a number): ")
        if validate_input(week, "week") and 1 <= int(week) <= 5:
            break

    while True:
        day = input("Enter the day (as a number): ")
        if validate_input(day, "day") and 1 <= int(day) <= 7:
            break

    task = input("Enter the task to add: ")

    # Create a key for the specific date
    key = (month, week, day)
    
    if key not in schedule:
        schedule[key] = []
    schedule[key].append(task)
    
    print(f"Task '{task}' added to Month {month}, Week {week}, Day {day}.")

def view_schedule():
    if not schedule:
        print("No events scheduled.")
    else:
        for key, tasks in schedule.items():
            month, week, day = key
            print(f"\nMonth: {month}, Week: {week}, Day: {day}")
            for i, task in enumerate(tasks, start=1):
                print(f"  {i}. {task}")

def edit_event():
    while True:
        month = input("Enter the month (as a number): ")
        if validate_input(month, "month") and 1 <= int(month) <= 12:
            break

    while True:
        week = input("Enter the week (as a number): ")
        if validate_input(week, "week") and 1 <= int(week) <= 5:
            break

    while True:
        day = input("Enter the day (as a number): ")
        if validate_input(day, "day") and 1 <= int(day) <= 7:
            break
    
    key = (month, week, day)
    
    if key not in schedule or not schedule[key]:
        print(f"No tasks found for Month {month}, Week {week}, Day {day}.")
        return
    
    while True:
        print(f"\nEditing schedule for Month {month}, Week {week}, Day {day}:")
        print("1. Add task")
        print("2. Edit task")
        print("3. Delete task")
        print("4. Back to main menu")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            task = input("Enter the task to add: ")
            schedule[key].append(task)
            print(f"Task '{task}' added to Month {month}, Week {week}, Day {day}.")
        elif choice == 2:
            view_tasks(key)
            task_index = int(input("Enter the number of the task to edit: ")) - 1
            if 0 <= task_index < len(schedule[key]):
                new_task = input("Enter the new task: ")
                schedule[key][task_index] = new_task
                print(f"Task updated to '{new_task}'.")
            else:
                print("Invalid task number.")
        elif choice == 3:
            view_tasks(key)
            task_index = int(input("Enter the number of the task to delete: ")) - 1
            if 0 <= task_index < len(schedule[key]):
                deleted_task = schedule[key].pop(task_index)
                print(f"Task '{deleted_task}' deleted.")
                if not schedule[key]:  # Remove the key if no tasks left
                    del schedule[key]
            else:
                print("Invalid task number.")
        elif choice == 4:
            break
        else:
            print("Invalid choice, please try again.")

def view_tasks(key):
    month, week, day = key
    print(f"Tasks for Month: {month}, Week: {week}, Day: {day}:")
    for i, task in enumerate(schedule[key], start=1):
        print(f"  {i}. {task}")

def run_program():
    while True:
        choice = main_menu()
        if choice == 1:
            add_event()
        elif choice == 2:
            view_schedule()
        elif choice == 3:
            edit_event()
        elif choice == 4:
            print("Exiting program.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    run_program()
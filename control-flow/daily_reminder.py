# daily_reminder.py

# Prompt user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Generate reminder using match-case and conditional logic
match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task. Try to complete it as soon as possible.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that should be completed today.")
        else:
            print(f"Reminder: '{task}' is a medium priority task. Schedule time for it soon.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a low priority but time-sensitive task. Complete it by today if possible.")
        else:
            print(f"Reminder: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print(f"Reminder: Invalid priority level entered for the task: '{task}'.")

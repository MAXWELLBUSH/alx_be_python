# File: control-flow/daily_reminder.py

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Note: '{task}' is a high priority task. Try to get it done soon.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that requires attention today.")
        else:
            print(f"Note: '{task}' is a medium priority task. Plan to do it within the week.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a low priority task that still requires attention today.")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Unknown priority level.")

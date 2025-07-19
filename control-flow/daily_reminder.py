  # Personal Daily Reminder :
# daily_reminder.py

# Prompt for task details
task = input("Enter your task: ")
priority = input("Enter the priority level (high, medium, low): ")
time_bound = input("Is the task time-bound? (yes or no): ")

# Generate the base reminder based on priority
match priority:
    case "high":
        reminder = f"REMINDER: '{task}' is a HIGH priority task"
    case "medium":
        reminder = f"REMINDER: '{task}' is a MEDIUM priority task"
    case "low":
        reminder = f"REMINDER: '{task}' is a LOW priority task"
    case _:
        reminder = f"REMINDER: '{task}' has an UNKNOWN priority"

# Modify reminder if the task is time-sensitive
if time_bound == "yes":
    reminder += " That requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."
    print(reminder)
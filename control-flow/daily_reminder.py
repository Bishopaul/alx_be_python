# daily_reminder.py

# Prompt for user input
task = input("Enter your task for today: ")
priority = input("Set the priority (high/medium/low): ").lower()
time_bound = input("Is this task time-bound? (yes/no): ").lower()

# Loop to ensure valid priority input
while priority not in ["high", "medium", "low"]:
    print("Invalid priority. Please enter high, medium, or low.")
    priority = input("Set the priority (high/medium/low): ").lower()

# Match Case for priority-based messaging
match priority:
    case "high":
        message = f"🔴 High Priority: {task}"
    case "medium":
        message = f"🟠 Medium Priority: {task}"
    case "low":
        message = f"🟢 Low Priority: {task}"
    case _:
        message = f"⚪ Task: {task}"

# Add time-sensitive note if applicable
if time_bound == "yes":
    message += " — that requires immediate attention today!"

# Output the reminder
print("\n📌 Daily Reminder:")
print(message)

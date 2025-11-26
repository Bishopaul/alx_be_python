from datetime import datetime, timedelta

def display_current_datetime():
    """
    Displays the current date and time in the format YYYY-MM-DD HH:MM:SS.
    Saves the current date inside current_date variable.
    """
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date

def calculate_future_date(current_date, days_to_add: int):
    """
    Calculates the future date after adding the specified number of days.
    Saves the future date inside future_date variable.
    """
    future_date = current_date + timedelta(days=days_to_add)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")
    return future_date

def main():
    # Part 1: Display current date and time
    current_date = display_current_datetime()

    # Part 2: Prompt user for number of days
    try:
        days_input = input("Enter the number of days to add to the current date: ").strip()
        if not days_input.isdigit() and not (days_input.startswith('-') and days_input[1:].isdigit()):
            raise ValueError("Invalid input. Please enter an integer value.")
        
        days_to_add = int(days_input)
        calculate_future_date(current_date, days_to_add)

    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()


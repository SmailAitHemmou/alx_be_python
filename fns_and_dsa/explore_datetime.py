  # Explore `datetime` Module :

def display_current_datetime():
    import datetime
    now = datetime.datetime.now()
    def calculate_future_date():
        from datetime import timedelta
        number_of_days = int(input("Enter the number of days to add to the current date: "))
        future_date = now + timedelta(days=number_of_days)
        formatted_future_date = future_date.strftime("%Y-%m-%d")
        print("Future date: ", formatted_future_date)
    current_date = now.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time: ", current_date)
    calculate_future_date()
display_current_datetime()

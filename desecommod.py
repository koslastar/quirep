def append_date(date):
    """
    Appends a date to the list of events.
    
    :param date: The date to append.
    :type date: datetime.date
    """
    # Your code to append the date
    print(f"Date appended: {date}")

# Example usage:
from datetime import date
today = date.today()
append_date(today)

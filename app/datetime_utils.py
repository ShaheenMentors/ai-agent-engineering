from datetime import datetime
def show_current_year():
    current = datetime.today()
    print(f"Current year is: {current.strftime("%Y")}")

def show_current_datetime():
    current = datetime.today()
    print(current)
    print("Today is: " + current.strftime("%A %d-%m-%Y"))
    print("Current Time is: " + current.strftime("%H:%M:%S"))

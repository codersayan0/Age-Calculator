from tkinter import *
from tkinter import messagebox
from datetime import datetime

# Function to clear all input fields
def clearAll():
    for field in [dayField, monthField, yearField, givenDayField, givenMonthField, givenYearField, rsltYearField, rsltMonthField, rsltDayField, totalDaysField, totalMonthsField, totalWeeksField, totalHoursField, totalMinutesField, totalSecondsField]:
        field.delete(0, END)

# Function to check for errors in input
def checkError():
    fields = [dayField, monthField, yearField]

    # If the given date is not provided, use today's date
    if givenDayField.get() == "" or givenMonthField.get() == "" or givenYearField.get() == "":
        today = datetime.today()
        givenDayField.insert(0, today.day)
        givenMonthField.insert(0, today.month)
        givenYearField.insert(0, today.year)

    # Check if any birth date field is empty
    if any(field.get() == "" for field in fields):
        messagebox.showerror("Input Error", "Please enter your complete birth date.")
        clearAll()
        return -1
    return 0

# Function to calculate age
def calculateAge():
    if checkError() == -1:
        return

    try:
        # Get values from entry fields
        birth_day, birth_month, birth_year = int(dayField.get()), int(monthField.get()), int(yearField.get())
        given_day, given_month, given_year = int(givenDayField.get()), int(givenMonthField.get()), int(givenYearField.get())

        # Convert to datetime objects
        birth_date = datetime(birth_year, birth_month, birth_day)
        given_date = datetime(given_year, given_month, given_day)

        if given_date < birth_date:
            messagebox.showerror("Error", "Given date must be after birth date!")
            return

        # Calculate the difference in years, months, and days
        age_years = given_date.year - birth_date.year
        age_months = given_date.month - birth_date.month
        age_days = given_date.day - birth_date.day

        if age_days < 0:
            given_month -= 1
            age_days += (datetime(given_date.year, given_date.month, 1) - datetime(given_date.year, given_date.month - 1, 1)).days

        if age_months < 0:
            age_years -= 1
            age_months += 12

        # Calculate total days and months lived
        total_days = (given_date - birth_date).days
        total_months = (age_years * 12) + age_months
        
        # Additional Calculations
        total_weeks = total_days // 7
        total_hours = total_days * 24
        total_minutes = total_hours * 60
        total_seconds = total_minutes * 60

        # Display results
        rsltYearField.insert(0, age_years)
        rsltMonthField.insert(0, age_months)
        rsltDayField.insert(0, age_days)
        totalDaysField.insert(0, total_days)
        totalMonthsField.insert(0, total_months)
        totalWeeksField.insert(0, total_weeks)
        totalHoursField.insert(0, total_hours)
        totalMinutesField.insert(0, total_minutes)
        totalSecondsField.insert(0, total_seconds)

    except ValueError:
        messagebox.showerror("Error", "Invalid date input!")

# GUI Setup
if __name__ == "__main__":
    gui = Tk()
    gui.configure(background="light blue")
    gui.title("Age Calculator")
    gui.geometry("600x400")

    # Labels
    Label(gui, text="Date Of Birth", bg="blue", fg="white").grid(row=0, column=1)
    Label(gui, text="Given Date", bg="blue", fg="white").grid(row=0, column=3)
    
    for i, text in enumerate(["Day", "Month", "Year"]):
        Label(gui, text=text, bg="light blue").grid(row=i+1, column=0)
        Label(gui, text=f"Given {text}", bg="light blue").grid(row=i+1, column=2)

    # Entry fields
    dayField, monthField, yearField = Entry(gui), Entry(gui), Entry(gui)
    givenDayField, givenMonthField, givenYearField = Entry(gui), Entry(gui), Entry(gui)
    rsltYearField, rsltMonthField, rsltDayField = Entry(gui), Entry(gui), Entry(gui)
    totalDaysField, totalMonthsField = Entry(gui), Entry(gui)
    totalWeeksField, totalHoursField = Entry(gui), Entry(gui)
    totalMinutesField, totalSecondsField = Entry(gui), Entry(gui)

    fields = [dayField, monthField, yearField, givenDayField, givenMonthField, givenYearField, rsltYearField, rsltMonthField, rsltDayField, totalDaysField, totalMonthsField, totalWeeksField, totalHoursField, totalMinutesField, totalSecondsField]
    positions = [(1,1), (2,1), (3,1), (1,3), (2,3), (3,3), (6,1), (7,1), (8,1), (10,1), (11,1), (12,1), (13,1), (14,1), (15,1)]
    
    for field, pos in zip(fields, positions):
        field.grid(row=pos[0], column=pos[1])

    # Result Labels
    Label(gui, text="Years", bg="light blue").grid(row=6, column=0)
    Label(gui, text="Months", bg="light blue").grid(row=7, column=0)
    Label(gui, text="Days", bg="light blue").grid(row=8, column=0)
    Label(gui, text="Total Days Lived", bg="light blue").grid(row=10, column=0)
    Label(gui, text="Total Months Lived", bg="light blue").grid(row=11, column=0)
    Label(gui, text="Total Weeks Lived", bg="light blue").grid(row=12, column=0)
    Label(gui, text="Total Hours Lived", bg="light blue").grid(row=13, column=0)
    Label(gui, text="Total Minutes Lived", bg="light blue").grid(row=14, column=0)
    Label(gui, text="Total Seconds Lived", bg="light blue").grid(row=15, column=0)

    # Buttons
    Button(gui, text="Calculate Age", fg="black", bg="green", command=calculateAge).grid(row=4, column=2)
    Button(gui, text="Clear All", fg="black", bg="red", command=clearAll).grid(row=16, column=2)

    # Start the GUI
    gui.mainloop()

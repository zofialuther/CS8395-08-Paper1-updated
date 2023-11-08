from constraint import *

def time_conversion(time_value):
    # Define constraints and variables
    problem = Problem()
    weeks, days, hours, minutes, seconds = (IntVar(0, 10080), IntVar(0, 6), IntVar(0, 23), IntVar(0, 59), IntVar(0, 59))
    
    # Add constraints
    problem.add(weeks * 10080 + days * 1440 + hours * 60 + minutes + seconds == time_value)
    
    # Solve the problem
    problem.solve()
    
    # Output the result in the special format
    print(f"{weeks.value()} weeks, {days.value()} days, {hours.value()} hours, {minutes.value()} minutes, {seconds.value()} seconds")
    
# Example usage
time_conversion(123456)
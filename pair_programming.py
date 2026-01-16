hours_worked = 0
hourly_rate = 0 
salary = 0
print("How many hours did you work?")
hours_worked = float(input())
print("What is your hourly rate?")
hourly_rate = float(input())
salary = hours_worked * hourly_rate
print(f"Your salary is: ${salary}")
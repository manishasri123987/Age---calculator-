from datetime import date

def calculate_age(birth_year, birth_month, birth_day):
    today = date.today()
    birth_date = date(birth_year, birth_month, birth_day)
    
    age_years = today.year - birth_date.year
    age_months = today.month - birth_date.month
    age_days = today.day - birth_date.day

    if age_days < 0:
        age_months -= 1
        age_days += 30

    if age_months < 0:
        age_years -= 1
        age_months += 12

    return age_years, age_months, age_days

print("=== Age Calculator ===")
birth_year = int(input("Enter birth year: "))
birth_month = int(input("Enter birth month (1-12): "))
birth_day = int(input("Enter birth day: "))

years, months, days = calculate_age(birth_year, birth_month, birth_day)

print(f"\nYour Age is: {years} years, {months} months, {days} days")

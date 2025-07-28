from datetime import date,datetime
# today = date.today()
# print("today : ",today)
# dob=input("Enter your date of birth (in the format yyyy-mm-dd) :")
# birth_date=datetime.strptime(dob,"%Y-%m-%d").date()
# print(birth_date)
# year=today.year-birth_date.year
# month=today.month - birth_date.month
# days=today.day-birth_date.day

# if days < 0:
#     month-=1
#     days+=( date(today.year,today.month,1)-date(today.year,today.month-1,1)).days

# if month < 0:
#     year-=1
#     month+=12

# print(f"your are {year} year {month} month {days} days old")

current_time=datetime.now()
print("current_time : ",current_time)
birth_time=input("Enter your date of birth (in the format yyyy-mm-dd  hr-min-sec) :")
timeOfBirth = datetime.strptime(birth_time,"%Y-%m-%d %H:%M:%S ")
age=current_time-timeOfBirth
print("age : ",age)
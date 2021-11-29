import datetime

user_input = input("Enter your goal and deadline:\n ")
user_input_list = user_input.split(": ")
print(user_input_list)

goal = user_input_list[0]
date = user_input_list[1]

deadline = datetime.datetime.strptime(date, "%m-%d-%Y")
today_date = datetime.datetime.today()
time = deadline - today_date

print(f"Time remaining for your goal: {goal} is {time.total_seconds() / 60 / 60 / 24} days")


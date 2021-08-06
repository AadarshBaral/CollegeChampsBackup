import os

# from datetime import datetime, timezone


# date = datetime.now(timezone.utc)
# month  = date.strftime('%B')
# day = date.strftime('%a')
# year = date.year
# day_num = date.weekday()

# date = f"{day_num} {month} {year}"
# print(date)



user= os.environ.get('DB_USERNAME')
pw = os.environ.get('DB_PASSWORD')


print(user)
print(pw)
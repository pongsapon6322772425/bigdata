import requests
import datetime
import csv
import time

province_list = []
# Read province from csv
with open('ThailandProvince.csv', 'r', encoding='utf-8', errors='replace') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        province_list.append(row[0])

# Date format = YYYY-MM-DD with current datetime
date = datetime.datetime.now().date()   
# Token for authentication
bearer_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjhjMmM5M2ZlNjRmYzQxMWM0YjdjYmY1ZTc3OGNmOWY0MmQ4ZDBmNDg5YjBhMTI0MDY1ZWE1MDJiOTAyYjhmNGM0ZDQ0NmQwMzBlMzQ0OTZkIn0.eyJhdWQiOiIyIiwianRpIjoiOGMyYzkzZmU2NGZjNDExYzRiN2NiZjVlNzc4Y2Y5ZjQyZDhkMGY0ODliMGExMjQwNjVlYTUwMmI5MDJiOGY0YzRkNDQ2ZDAzMGUzNDQ5NmQiLCJpYXQiOjE2OTY5NDYzNTEsIm5iZiI6MTY5Njk0NjM1MSwiZXhwIjoxNzI4NTY4NzUxLCJzdWIiOiIyODE0Iiwic2NvcGVzIjpbXX0.W2jtRgGfKBgCW7E6tVwlE81FvYLrbfo5gD-dJecwvMvJhNN8tPRolP42IjT-U0acDjihBAShLggnMyVJ0Rhfee0lhsoOS51bRsszqka5ILVna1c-XkQvqSi_TiE4tHiklm4wE98digNxc-5JzNxkcThCoTJz0K_ca9HC6945uGWm3mU3vzdNlSal6E8BEeJQbgQQUaREQXEznTwEemyNufqtRk2KgPGsKhCf9vcYtMqP0pM4ABxAlu9BKew3UMF2Iq9iMaYsnNiV75Qxo70qlE6oLWKsnLmlxvvIPpOtwqtYnlSm2_88q46-YsnD6KspDbIGUjfMjNXO8HLbKqCjvmlcHArsBroxxKkG0qs7qN2x7j5Bi7pWdlIwJSwQaSZDBTH_YPdFraMKDwEqx-wMYGRbEZCsAerhm8nUoRygo9xyo-zg0N0abuFRdXglgl3OdWSgcHJF00vvFiJ-J1HPajndndYoJG42mCCf9iNayjGxlkmRsvGeqMMX9rciJNjZ0Y2PtSQgBKOA3LaGRhdjG-dX9gjy55Y_-Lsw70Zve6tgFwtft_FfRXbUI9QmxW24KQe4u65wKioL8BXdTvwoR5GDnbz85VkslctHZ1M5LNw_D8iEiw2zJCB6H3dkjPL-XTI0M3KB-rrrQm2Qiw-A1oGb8Fj61Sp9U284OdukT20"
# Query parameters
fields = "tc,rh,slp,rain,ws10m,wd10m,cloudlow,cloudmed,cloudhigh,cond"
# Start request
for province in province_list:
    api_url = f"https://data.tmd.go.th/nwpapi/v1/forecast/location/hourly/place?province={province}&fields={fields}&date={date}"
    headers = {"Authorization": f"Bearer {bearer_token}"}
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print(f"Request failed with status code {response.status_code}")
    # Wait 2 second because limited request at 60 times/min/token
    time.sleep(2)
    
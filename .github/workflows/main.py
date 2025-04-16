import requests
from persiantools.jdatetime import JalaliDate
import datetime
import os

# تاریخ شمسی امروز
today_gregorian = datetime.datetime.today()
today_jalali = JalaliDate(today_gregorian).strftime('%Y/%m/%d')

# اطلاعات API از Secrets
base_id = os.getenv("AIRTABLE_BASE_ID")
table_name = os.getenv("AIRTABLE_TABLE_NAME")
token = os.getenv("AIRTABLE_TOKEN")

url = f"https://api.airtable.com/v0/{base_id}/{table_name}"
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}
payload = {
    "records": [
        {
            "fields": {
                "تاریخ شمسی": today_jalali
            }
        }
    ]
}

response = requests.post(url, json=payload, headers=headers)
if response.status_code in [200, 201]:
    print("تاریخ شمسی با موفقیت ثبت شد:", today_jalali)
else:
    print("خطا در ثبت:", response.status_code)
    print(response.text)

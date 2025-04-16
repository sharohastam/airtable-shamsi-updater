import requests
from persiantools.jdatetime import JalaliDate
import datetime
import os

# گرفتن تاریخ شمسی
today_gregorian = datetime.datetime.today()
today_jalali = JalaliDate(today_gregorian).strftime('%Y/%m/%d')

# گرفتن اطلاعات از سکرت‌ها
base_id = os.environ["AIRTABLE_BASE_ID"]
table_name = os.environ["AIRTABLE_TABLE_NAME"]
api_key = os.environ["AIRTABLE_TOKEN"]
field_name = "تاریخ شمسی"

# آماده‌سازی آدرس API
url = f"https://api.airtable.com/v0/{base_id}/{table_name}"

# آماده‌سازی Header
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# آماده‌سازی داده‌ها
payload = {
    "records": [
        {
            "fields": {
                field_name: today_jalali
            }
        }
    ]
}

# ارسال درخواست به Airtable
response = requests.post(url, json=payload, headers=headers)

# بررسی نتیجه
if response.status_code in [200, 201]:
    print("تاریخ شمسی با موفقیت ثبت شد:", today_jalali)
else:
    print("خطا در ثبت:", response.status_code)
    print(response.text)
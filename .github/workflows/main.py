import json
import requests
from flask import Flask, request
from persiantools.jdatetime import JalaliDate
import os

app = Flask(__name__)

AIRTABLE_TOKEN = os.environ["AIRTABLE_TOKEN"]
AIRTABLE_BASE_ID = os.environ["AIRTABLE_BASE_ID"]
AIRTABLE_TABLE_NAME = os.environ["AIRTABLE_TABLE_NAME"]

@app.route("/", methods=["POST"])
def update_date():
    data = request.get_json()
    record_id = data.get("record_id")

    if not record_id:
        return {"error": "record_id not provided"}, 400

    today_jalali = str(JalaliDate.today())

    url = f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_NAME}/{record_id}"
    headers = {
        "Authorization": f"Bearer {AIRTABLE_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "fields": {
            "تاریخ شمسی": today_jalali
        }
    }

    res = requests.patch(url, headers=headers, json=payload)
    return res.text, res.status_code

# مخصوص اجرا در Vercel
app.run()
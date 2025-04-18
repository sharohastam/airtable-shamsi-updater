from flask import Flask, request, jsonify
import requests
import jdatetime

app = Flask(__name__)

# مشخصات Airtable
AIRTABLE_TOKEN = "patGp0SNiIQsvaHrw.a875fefe22ba313abc03cc4f3acafbd573a0a1072354a493049fbcd17630292c"
base_id = "appNNY7mUzJrjbwlv"
table_name = "Currencylog"
field_name = "تاریخ شمسی"

@app.route("/", methods=["POST"])
def update_record():
    try:
        data = request.get_json()
        record_id = data.get("record_id")

        if not record_id:
            return jsonify({"error": "No record_id provided"}), 400

        # گرفتن تاریخ شمسی امروز
        today_shamsi = jdatetime.date.today().strftime('%Y/%m/%d')

        # ساخت URL برای PATCH
        url = f"https://api.airtable.com/v0/{base_id}/{table_name}/{record_id}"
        headers = {
            "Authorization": f"Bearer {AIRTABLE_TOKEN}",
            "Content-Type": "application/json"
        }
        payload = {
            "fields": {
                field_name: today_shamsi
            }
        }

        # ارسال درخواست به Airtable
        response = requests.patch(url, headers=headers, json=payload)
        response.raise_for_status()

        return jsonify({"message": "تاریخ شمسی ثبت شد", "date": today_shamsi}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run()

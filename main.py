from flask import Flask, request, jsonify
import requests
import jdatetime

app = Flask(__name__)

# تنظیمات Airtable
AIRTABLE_TOKEN = "patgPqSNi0vQahrw.a875fe2b233a38c3c0c4f3acafbd573aa1872354a9394f9bc417639292c"
base_id = "appNY7MuZrJiplv"
table_name = "Currencylog"
field_name = "Tarikh"  # تاریخ

@app.route("/", methods=["POST"])
def update_record():
    try:
        data = request.get_json()
        record_id = data.get("record_id")

        if not record_id:
            return jsonify({"error": "No record_id provided"}), 400

        today_shamsi = jdatetime.date.today().strftime("%Y/%m/%d")

        url = f"https://api.airtable.com/v0/{base_id}/{table_name}/{record_id}"
        headers = {
            "Authorization": f"Bearer {AIRTABLE_TOKEN}",
            "Content-Type": "application/json",
        }
        payload = {
            "fields": {
                field_name: today_shamsi
            }
        }

        response = requests.patch(url, headers=headers, json=payload)
        response.raise_for_status()

        return jsonify({"message": "رکورد به‌روز شد", "date": today_shamsi}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/favicon.ico")
def favicon():
    return "", 204  # پاسخ بدون محتوا

if __name__ == "__main__":
    app.run()

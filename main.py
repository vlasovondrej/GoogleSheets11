from flask import Flask, request, jsonify
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
import json

app = Flask(__name__)

# Google Sheets setup
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

json_key = os.environ.get('GOOGLE_APPLICATION_CREDENTIALS_JSON')
if not json_key:
    raise ValueError("Missing environment variable: GOOGLE_APPLICATION_CREDENTIALS_JSON")

info = json.loads(json_key)
creds = ServiceAccountCredentials.from_json_keyfile_dict(info, scope)
client = gspread.authorize(creds)
sheet = client.open("AiGRO Core Infrastructure").sheet1

@app.route('/rows', methods=['GET'])
def get_rows():
    data = sheet.get_all_values()
    return jsonify(data)

@app.route('/add_row', methods=['POST'])
def add_row():
    # Expects JSON like {"row": ["A", "B", "C"]}
    row = request.json.get('row')
    if not row:
        return jsonify({"error": "Missing 'row' in request"}), 400
    sheet.append_row(row)
    return jsonify({"status": "success", "row_added": row})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)


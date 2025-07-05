import os
from flask import Flask, request, jsonify
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

# Path to the secret file inside the container
secret_path = "/etc/secrets/aigro-464708-credentials.json"

creds = ServiceAccountCredentials.from_json_keyfile_name(secret_path, scope)
client = gspread.authorize(creds)
sheet = client.open("AiGRO Core Infrastructure").sheet1

# your routes here...

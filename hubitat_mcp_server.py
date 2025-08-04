#!/usr/bin/env python3
import os
import requests
from flask import Flask, jsonify
from dotenv import load_dotenv

load_dotenv()

HUBITAT_TOKEN = os.getenv("HUBITAT_TOKEN")
HUBITAT_BASE_URL = os.getenv("HUBITAT_BASE_URL")  # Example: https://cloud.hubitat.com/api/{CLOUD_ID}/apps/{APP_ID}/devices

app = Flask(__name__)

@app.route("/devices", methods=["GET"])
def list_devices():
    """Return a list of devices from Hubitat Maker API."""
    url = f"{HUBITAT_BASE_URL}/all?access_token={HUBITAT_TOKEN}"
    r = requests.get(url)
    return jsonify(r.json())

@app.route("/device/<device_id>/<command>", methods=["POST"])
def control_device(device_id, command):
    """Send a command to a Hubitat device."""
    url = f"{HUBITAT_BASE_URL}/{device_id}/{command}?access_token={HUBITAT_TOKEN}"
    r = requests.post(url)
    return jsonify({"status": "ok" if r.status_code == 200 else "error"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005)

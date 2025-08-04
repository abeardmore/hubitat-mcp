#!/usr/bin/env python3
import os
import requests
from flask import Flask, jsonify
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Example: http://192.168.1.50/apps/api/<APP_ID>/devices
HUBITAT_TOKEN = os.getenv("HUBITAT_TOKEN")
HUBITAT_BASE_URL = os.getenv("HUBITAT_BASE_URL")

app = Flask(__name__)

@app.route("/devices", methods=["GET"])
def list_devices():
    """Return a list of devices from Hubitat Maker API and log them nicely."""
    url = f"{HUBITAT_BASE_URL}/all?access_token={HUBITAT_TOKEN}"
    r = requests.get(url)
    devices = r.json()

    print("\n=== Hubitat Devices ===")
    for d in devices:
        name = d.get("label") or d.get("name", "Unknown")
        device_id = d.get("id", "?")
        device_type = d.get("type", "?")
        print(f"- {name} (ID: {device_id}, Type: {device_type})")
    print("=======================\n")

    return jsonify(devices)

@app.route("/device/<device_id>/<command>", methods=["POST"])
def control_device(device_id, command):
    """Send a command to a Hubitat device."""
    url = f"{HUBITAT_BASE_URL}/{device_id}/{command}?access_token={HUBITAT_TOKEN}"
    r = requests.post(url)
    status = "ok" if r.status_code == 200 else "error"
    print(f"Command '{command}' sent to device ID {device_id} - Status: {status}")
    return jsonify({"status": status})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005)

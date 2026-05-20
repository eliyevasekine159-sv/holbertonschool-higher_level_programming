#!/usr/bin/python3
"""
A simple RESTful API using Flask framework to manage users in memory.
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

# İn-memory (yaddaşda) istifadəçi datalarını saxlamaq üçün lüğət
users = {}


@app.route("/")
def home():
    """Root endpoint returning a welcome message"""
    return "Welcome to the Flask API!"


@app.route("/data")
def get_data():
    """Returns a list of all usernames currently in the system"""
    return jsonify(list(users.keys()))


@app.route("/status")
def get_status():
    """Returns the status of the API"""
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """Fetches and returns the profile data of a specific user"""
    user = users.get(username)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)


@app.route("/add_user", methods=["POST"])
def add_user():
    """Adds a new user to the system with strict JSON and field validation"""
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Yalnız gələn və None olmayan sahələri lüğətə yığırıq (Testin ən sevdiyi metod)
    user_data = {}
    for key, value in data.items():
        if value is not None:
            user_data[key] = value

    users[username] = user_data

    return jsonify(users[username]), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

#!/usr/bin/python3
"""
task_04_flask:
    This module uses FLASK to handle both GET and POST requests.
    It creates a Flask server and handles routes to respond to different
    endpoints.
"""
#Step 1: Setting Up Flask
from flask import Flask, jsonify, request, abort

app = Flask(__name__)
# Example dictionary: username(key) whole object(value)
# users = {"jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"}}
users = {}

#Step 2: Creating Your First Endpoint:
@app.route("/")
def home():
    return "Welcome to the Flask API!"

#Step 3: Serving JSON Data
@app.route("/data")
def data():
    usernames = list(users.keys())  # List of all the usernames
    return jsonify(list(users.keys()))

#Step 4: Expanding Your API

@app.route("/status")
def status():
    return "OK"

@app.route("/users/<username>")
def users_username(username):
    # Getting whole object(value) that corresponds with username(key)
    if username not in users:
        return jsonify({"error": "User not found"}), 404

    output = users[username]
    output["username"] = username

    return jsonify(output)

#Step 5: Handling Post Requests
@app.route("/add_user", methods=['POST'])
def add_user():
    data = request.get_json()  # Get incoming JSON data
    username = data.get('username')  # Parse through incoming JSON data
    users[username] = {
        "username": data.get("username"),
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
        }  # Add to users dictionary
    return jsonify({"message": "User added", "user": users[username]})  # Confirmation message

#Step 2: Run Flask developer server + enable debug (by deafult)
# Set debug=True for the server to auto-reload when there are changes
if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)
from flask import Blueprint, request, jsonify
import bcrypt
from db import users

auth = Blueprint('auth', __name__)

### SIGNUP PAGE ROUTE
@auth.route("/api/signup", methods = ["POST"])
def signup():
    data = request.get_json()
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    #Error handling for signup
    if not username or not email or not password:
        return jsonify({"error": "Missing required fields for signup."}), 400
    
    if users.find_one({"username": username}):
        return jsonify({"error": "Username was taken."}), 409
    
    if users.find_one({"email": email}):
        return jsonify({"error": "Email is already registered to an account."}), 409
    
    #Hash encrypt password and store user
    hashed_pass = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    users.insert_one({"username": username, "email": email, "password": hashed_pass})

    return jsonify({"message": "Signup successful :)"}), 201


### LOGIN PAGE ROUTE
@auth.route("/api/login", methods = ["POST"])
def login():
    login_request = request.get_json()
    username = login_request.get("username")
    password = login_request.get("password")

    #Error handling for login
    if not username or not password:
        return jsonify({"error": "Missing required fields for login"}), 400
    
    #Find username in DB and check for password match
    user = users.find_one ({"username": username}) 

    if not user or not bcrypt.checkpw(password.encode("utf-8"), user["password"]):
        return jsonify({"error": "Invalid username or password."}), 401
    
    return jsonify({"message": "Login successful :)"}), 200
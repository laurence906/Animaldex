from flask import Blueprint, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
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
    users.insert_one({"username": username, "email": email, "password": hashed_pass, "dex_entries": 0, "isadmin": False})

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
    
    #Successful login, access token provided
    token = create_access_token(identity = username)
    return jsonify({"message": "Login successful :)", "token": token}), 200


@auth.route("/api/adminlogin", methods = ["POST"])
def adminlogin():
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
    
    if not user["isadmin"]:
        return jsonify({"error": "You do not have admin permissions"}), 403
    
    #Successful login, access token provided
    token = create_access_token(identity = username, additional_claims = {"adminpermissions": True})
    return jsonify({"message": "Login successful :)", 
                    "token": token,
                    "adminpermissions": True}), 200


### ACCOUNT INFO
@auth.route("/api/account", methods = ["GET"])
@jwt_required()
def account():
    try:
        username = get_jwt_identity()
        user = users.find_one({"username": username})

        if not user:
            return jsonify({"error": "User info could not be found."}), 404
        
        return jsonify({
            "username": user["username"],
            "email": user["email"],
            "dex_entries": user.get("dex_entries", 0)
        }), 200
    except Exception as e:
        return jsonify({"error": f"Error processing JWT and getting user data: {str(e)}"}), 422
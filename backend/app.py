from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from routes.userauth import auth
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
jwt = JWTManager(app)

CORS(app, origins = ["http://localhost:5173"])

app.register_blueprint(auth)

if __name__ == "__main__":
    app.run(debug = True)
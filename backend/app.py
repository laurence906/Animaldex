from speciesnet import SpeciesNet
from flask import Flask, request, jsonify     # adds flask commands
from flask_cors import CORS
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity
from routes.userauth import auth
from dotenv import load_dotenv
from speciesnet_api import *
import os
from db import users


load_dotenv()
app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
jwt = JWTManager(app)

CORS(app, origins = ["http://localhost:5173"])

app.register_blueprint(auth)


# #constants
# model_name = 'kaggle:google/speciesnet/pyTorch/v4.0.2a/1' 
# model = SpeciesNet(model_name=model_name)
# #image_path moved inside function``


@app.route('/api/backToFrontTest')
def useModelInWebpageTest():
    image_path = "testImages/squirrel.jpeg" # Relative path starts from Animaldex
    # print(f"Current working directory: {os.getcwd()}")

    if not os.path.exists(image_path):
        print(f"File not found: {image_path}")
    else:
        print("Hacking mainframe.")
        print("Running machine learning model.")
        print("Examining DNA cells.")

        resultTuple = process_single_image(image_path, safety=True, debug=False) # returns list of 1 tuple

        firstInResultTuple = resultTuple[0]
        return {'modelResult': firstInResultTuple} # must be formatted as dict entry for React to pick up
        

@app.route('/api/frontToBackTest', methods=['POST'])
def recieveFromFrontendExample():
    recievedData = request.get_json()
    print(recievedData)

    return jsonify({"status": "success", "received": recievedData}), 200

@app.route('/api/upload', methods=['POST'])
def processUpload():
    # Put the file object in temporary folder imgProcessingTemp
    # Validate and grab the file from the request
    if 'image' not in request.files:
        return jsonify({"status": "error", "message": "No file part in the request"}), 400
    file = request.files['image']
    if file.filename == '':
        return jsonify({"status": "error", "message": "No file selected for uploading"}), 400
    filename = file.filename
    tempPath = os.path.join('imgProcessingTemp', filename)
    file.save(tempPath)


    # Plug it into the model
    if not os.path.exists(tempPath):
        print(f"File not found: {tempPath}") # Should never run; a file was just created at this temp_path
        return jsonify({"status": "error", "message": "Something went wrong internally."}), 400
    else:
        # print("Hacking mainframe.")
        # print("Running machine learning model.")
        # print("Examining DNA cells.")

        resultTuple = process_single_image(tempPath, safety=True, debug=False) # returns list of 1 tuple

        firstInResultTuple = resultTuple[0]
    
    # Clean up the temporary file
    os.remove(tempPath)

    return jsonify({"status": "success", "modelResult": resultTuple}), 200 # must be formatted as dict entry for React to pick up


@app.route('/api/updateDexEntries', methods=['POST'])
def updateDexCount():
    # This route will handle updating the user's dex count
    recievedData = request.get_json()
    
    
    # mongodb.user.dexentries += data


    return jsonify({"status": "success", "message": "Dex count updated."}), 200
    
    
@app.route('/api/incrementDexEntries',  methods=['POST'])
@jwt_required()
def incrementDex():

    username = get_jwt_identity()
    user = users.find_one({"username": username})

    if not user:
        return jsonify({"status": "error", "message": "User to update not found."}), 400
    else:
        users.update_one({"username": username}, {"$inc": {"dex_entries": 1}})
        return jsonify({"status": "success", "message": "Dex entry count incremented."}), 200
    
    


if __name__ == "__main__":
    app.run(debug = True)
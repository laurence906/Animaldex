from speciesnet import SpeciesNet
from flask import Flask, request, jsonify     # adds flask commands
from flask_cors import CORS
from routes.userauth import auth
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

CORS(app, origins = ["http://localhost:5173"])

app.register_blueprint(auth)


#constants
model_name = 'kaggle:google/speciesnet/pyTorch/v4.0.2a/1' 
model = SpeciesNet(model_name=model_name)
#image_path moved inside function


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
        
        # use run_mode='single_thread' to avoid multiprocessing (bad!!!!!)
        # python -c "from speciesnet import SpeciesNet; help(SpeciesNet.predict)" ||||| dumps function signature for all inputs
        resultdict = model.predict(
            filepaths=[image_path], 
            run_mode='single_thread'
        )
        print(type(resultdict)) # type <class 'dict'>

        # print(resultdict) # RAW OUTPUT

        # FORMAT: Predictions is an array of predictions (multi image input), each index has an inner dict.
        #print(resultdict.get('predictions')[0].get('classifications').get('classes')) # gets entire list
        firstInResultDict = resultdict.get('predictions')[0].get('classifications').get('classes')[0]
        return {'modelResult': firstInResultDict} # must be formatted as dict entry for React to pick up
        

@app.route('/api/frontToBackTest', methods=['POST'])
def recieveFromFrontendExample():
    recievedData = request.get_json()
    print(recievedData)

    return jsonify({"status": "success", "received": recievedData}), 200



if __name__ == "__main__":
    app.run(debug = True)
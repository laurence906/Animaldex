# see requirements.txt
from speciesnet import SpeciesNet
from flask import Flask, request, jsonify     # adds flask commands
import os



#constants
model_name = 'kaggle:google/speciesnet/pyTorch/v4.0.2a/1' 
model = SpeciesNet(model_name=model_name)
app = Flask(__name__) # initializes Flask object
#image_path moved inside function




# These are decorators, which modify the following function. This route decorator specifies to run
#   the following function when it's called, like a tag.
# In this case, this decorator corresponds to requests and its arguments are formatted like the end 
#   of a URL, like in this case, example.com/api/frontToBackTest
@app.route('/api/backToFrontTest')
def useModelInWebpageTest():
    image_path = "backend/testImages/squirrel.jpg" # Relative path starts from Animaldex

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
# see requirements.txt
from speciesnet import SpeciesNet
import os

model_name = 'kaggle:google/speciesnet/pyTorch/v4.0.2a/1' 
model = SpeciesNet(model_name=model_name)

image_path = "/Users/dolandeering/Pictures/squirrel.jpeg"

if not os.path.exists(image_path):
    print(f"File not found: {image_path}")
else:
    print("Hacking mainframe.")
    print("Running machine learning model.")
    print("Examining DNA cells.")
    
    # use run_mode='single_thread' to avoid multiprocessing (bad!!!!!)
    # python -c "from speciesnet import SpeciesNet; help(SpeciesNet.predict)" ||||| dumps function signature for all inputs
    results = model.predict(
        filepaths=[image_path], 
        run_mode='single_thread'
    )

    print(results) # RAW OUTPUT
    data = results['predictions'] # PARSE JSON
    print(data)
# see requirements.txt
from speciesnet import SpeciesNet
import os
from parser import *

#constants
model_name = 'kaggle:google/speciesnet/pyTorch/v4.0.2a/1' 
model = SpeciesNet(model_name=model_name)
image_path = "test_images"
#----------------------------------------------------------

if not os.path.exists(image_path):
        print(f"File not found: {image_path}")
else:
    # use run_mode='single_thread' to avoid multiprocessing (bad!!!!!)
    # python -c "from speciesnet import SpeciesNet; help(SpeciesNet.predict)" ||||| dumps function signature for all inputs
    files = os.listdir(image_path)
    for filename in files:
        # reconstruct the full path
        full_path = os.path.join(image_path, filename)
        if full_path == "test_images/.DS_Store":
             continue
        result_dict = model.predict(
            filepaths = [full_path],
            run_mode = 'single_thread'
        )
        # type <class 'dict'>
        # format dict<array<dict>> |||| every index in array is a file, every dict inside is the examination of that file
        # print(f"RAW OUTPUT:\n{result_dict}") # RAW OUTPUT

        # FORMAT: Predictions is an array of predictions (multi image input), each index has an inner dict.
        #print(result_dict.get('predictions')[0].get('classifications').get('classes'))
        print(f"IDENTIFIED: {get_highest_result(result_dict)} FROM: {full_path}")
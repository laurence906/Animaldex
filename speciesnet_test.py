# see requirements.txt
from speciesnet import SpeciesNet
import os
from parser import *

#constants
model_name = 'kaggle:google/speciesnet/pyTorch/v4.0.2a/1' 
model = SpeciesNet(model_name=model_name)
image_path = ["/Users/dolandeering/Pictures/squirrel.jpeg"]
#----------------------------------------------------------

for x in image_path:
    if not os.path.exists(x):
        print(f"File not found: {x}")
else:
    # use run_mode='single_thread' to avoid multiprocessing (bad!!!!!)
    # python -c "from speciesnet import SpeciesNet; help(SpeciesNet.predict)" ||||| dumps function signature for all inputs
    result_dict = model.predict(
        filepaths = image_path,
        run_mode = 'single_thread'
    )
    # type <class 'dict'>
    # format dict<array<dict>> |||| every index in array is a file, every dict inside is the examination of that file
    print(f"RAW OUTPUT:\n{result_dict}") # RAW OUTPUT

    # FORMAT: Predictions is an array of predictions (multi image input), each index has an inner dict.
    #print(result_dict.get('predictions')[0].get('classifications').get('classes'))
    print(f"IDENTIFIED: {get_highest_result(result_dict)}")

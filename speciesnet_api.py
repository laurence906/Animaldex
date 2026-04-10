### This file contains the api to efficiently call the model. It is a simplified version of directly accessing the base API.
### see requirements.txt if encountering any errors/issues
from speciesnet import SpeciesNet
import os
from parser import *

#constants
model_name = 'kaggle:google/speciesnet/pyTorch/v4.0.2a/1' 
model = SpeciesNet(model_name=model_name)
accepted_filetypes = {".png", ".jpg", ".jpeg"}
#----------------------------------------------------------

# ARGUMENTS KEY:
# image(s)_path <- self explanitory, either a folder of images or a path to a single image
# safety (default = True) <- When True, ensures that an animal is either fully identified or not identified at all.
#       Expected usage would be to filter out all returning instances where only "animal" or "human" is detected.
#       If safety mode is off, you may get a 'partially identified' animal in which there is some level of accuracy.
# debug (default = False) <- When True, the function will simply print out the entire raw dictionary, this has no purpose beyond debugging.

# processes an entire queue (folder) of images
# input: filepath of folder (relative or exact)
# output: list of <tuple(animal name, score)>
def process_image_queue(images_path: str, safety: bool = True, debug:bool = False):
    if not os.path.exists(images_path):
        print(f"File not found: {images_path}")
    else:
        files = os.listdir(images_path)
        output = []
        for filename in files:
            # reconstruct the full path
            full_path = os.path.join(images_path, filename)

            #sanitization
            if full_path == "test_images/.DS_Store": # clean hidden macOS files
                continue
            elif not any(sub in full_path for sub in accepted_filetypes):
                print(f"File is of an unsupported filetype: {full_path}")
                continue
            
            # running model
            result_dict = model.predict(
                filepaths = [full_path],
                run_mode = 'single_thread' # use run_mode='single_thread' or it just wont work!
            )

            # output handling
            if not debug:
                if not safety: # safety is OFF, return whatever is actually identified
                    curr = get_highest_result(result_dict)
                if safety:
                    curr = get_prediction(result_dict)
                print(f"IDENTIFIED: {curr} FROM: {full_path}")
                output.append(curr)
            if debug:
                print(f"RAW OUTPUT:\n{result_dict}")
        if not debug: return output
            


# processes a single image
# input: filepath of image (relative or exact)
# output: tuple(animal name, score)
def process_single_image(image_path: str, safety:bool = True, debug:bool = False):
    if not os.path.exists(image_path):
        print(f"File not found: {image_path}")
    elif not any(sub in image_path for sub in accepted_filetypes):
        print(f"File is of an unsupported filetype: {image_path}")
    else:
        result_dict = model.predict(
                filepaths = [image_path],
                run_mode = 'single_thread'
            )
        
        if not debug:
            if not safety: # safety is OFF, return whatever is actually identified
                print(f"IDENTIFIED: {get_highest_result(result_dict)} FROM: {image_path}")
                return get_highest_result(result_dict)
            if safety:
                print(f"IDENTIFIED: {get_prediction(result_dict)} FROM: {image_path}")
                return get_prediction(result_dict)
        if debug:
            print(f"RAW OUTPUT:\n{result_dict}")
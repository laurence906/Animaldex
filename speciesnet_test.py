# see requirements.txt
from speciesnet_api import * # <- the idea is to have minimal interaction with the api in the real code, for readability

#constants
images_path = "test_images"
armadillo_image = "test_images/IMG_8872.jpg"
#----------------------------------------------------------

process_image_queue(images_path)
process_single_image(armadillo_image)
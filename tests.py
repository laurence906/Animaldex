import unittest
from speciesnet import SpeciesNet
import os
from parser import *


class ModelTest(unittest.TestCase):
    def setUp(self):
        # code that runs before each test method
        model_name = 'kaggle:google/speciesnet/pyTorch/v4.0.2a/1' 
        self.model = SpeciesNet(model_name=model_name)
        self.path = 'test_images'

    def test_normal_squirrel_image(self):
        """Test that some image of a squirrel is detected."""
        result_dict = self.model.predict(
        filepaths = [f"{self.path}/squirrel_baseline.jpg"],
        run_mode = 'single_thread'
        )
        result = get_highest_result(result_dict)
        self.assertTrue("squirrel" in f"{result}") # assert

    def test_blank_image(self):
        """Test that a blank image detects nothing."""
        result_dict = self.model.predict(
        filepaths = [f"{self.path}/empty_room.jpg"],
        run_mode = 'single_thread'
        )
        result = get_highest_result(result_dict)
        self.assertTrue("blank" in f"{result}") # assert

    def test_low_light(self):
        """Test predefined low light image."""
        result_dict = self.model.predict(
        filepaths = [f"{self.path}/flying_squirrel_lowlight.jpg"],
        run_mode = 'single_thread'
        )
        result = get_highest_result(result_dict)
        self.assertTrue("rodent" in f"{result}") # assert 
        # BE WARNED THAT MODEL CANNOT FULLY IDENTIFY THIS IMAGE IN CURRENT ITERATION

    def test_high_light(self):
        """Test predefined high light image."""
        result_dict = self.model.predict(
        filepaths = [f"{self.path}/squirrel_highlight.jpg"],
        run_mode = 'single_thread'
        )
        result = get_highest_result(result_dict)
        self.assertTrue("squirrel" in f"{result}") # assert

if __name__ == '__main__':
    unittest.main(verbosity=2)
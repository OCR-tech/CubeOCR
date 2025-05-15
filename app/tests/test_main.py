import unittest
from unittest.mock import patch

# Import the main module and the py_main_gui module
import sys
from pathlib import Path
# sys.path.append(str(Path(__file__).resolve().parent.parent / 'src'))
sys.path.append(str(Path(__file__).resolve().parent.parent))

# import module.py_window_main as py_window_main
import main



# //========================================================//
# Test Cases:
# //========================================================//
# 1. Test the main function to ensure it calls the setup_system function exactly once.
# 2. Test the main function to ensure it calls the launch_gui function exactly once.
# 3. Verify that the main function integrates both setup_system and launch_gui correctly.




# # Test cases for the main application and py_main_gui module
# //========================================================//
class TestMain(unittest.TestCase):
    @patch('src.module.py_window_main.setup_system')
    @patch('src.module.py_window_main.launch_gui')
    def test_main_function(self, mock_launch_gui, mock_setup_system):
        """
        Test the main function to ensure it calls setup_system and launch_gui.
        """
        # Call the main function
        main.main()

        # Assert that setup_system was called once
        mock_setup_system.assert_called_once()

        # Assert that launch_gui was called once
        mock_launch_gui.assert_called_once()


if __name__ == '__main__':
    unittest.main()

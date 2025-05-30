# //===================================================//
# Tesseract-OCR is an open-source OCR engine used to extract text from images.
# Ensure that Tesseract-OCR is installed in the default Tesseract-OCR installation path.
# If Tesseract-OCR is not installed, please visit for download and installation instructions:
# https://github.com/UB-Mannheim/tesseract/wiki



# //===================================================//
# If the Tesseract-OCR installation path is different from the default path: please follow the steps below:
# 1) set the `flag_user_path` variable to `True`.
# 2) set the `tesseract_user_path` variable to the full path of the `tesseract.exe` executable file.

# Step 1:
flag_user_path = False        # Use the default Tesseract installation path
# flag_user_path = True       # Use the user-defined Tesseract installation path

# Step 2:
tesseract_user_path = r'C:/Program Files/Tesseract-OCR/tesseract.exe'   # Change this to the user-defined Tesseract installation path



# //===================================================//
# For Tesseract-OCR executable file:
# import os
# flag_user_path = True
# tesseract_user_path = os.path.join(os.getcwd(), "_internal", "tesseract", "tesseract.exe")



# //===================================================//
# Import necessary libraries and modules
import os
import sys
import subprocess

# Import the Tesseract-OCR path from the main GUI module.
def check_tesseract():
    """
    Searches for the Tesseract-OCR installation path.
    This function scans common installation directories and all available drives
    to locate the Tesseract executable on the system.
    """

    global tesseract_path, path_tesseract_cmd
    print("=== check_tesseract ===")

    # Check if the Tesseract path is set in the environment variables
    env_vars = os.environ  # Get system environment variables
    # print("Environment variables:", env_vars)

    if "TESSERACT_PATH" in env_vars:
        # If Tesseract path is set in environment variables, use it
        # print("Tesseract path is set in environment variables:", env_vars["TESSERACT_PATH"])
        pass
    else:
        # If Tesseract path is not set in environment variables, search for Tesseract-OCR installation
        # print("Tesseract path is not set in environment variables. Searching for Tesseract-OCR installation...")

        # Check flag_user_path to determine which Tesseract path to use
        if flag_user_path:
            # If the user-defined Tesseract path is valid with tesseract.exe, use it
            if os.path.exists(tesseract_user_path) and tesseract_user_path.endswith("tesseract.exe"):
                # print("Using user-defined Tesseract path:", tesseract_user_path)
                tesseract_path = tesseract_user_path
            else:
                print("User-defined Tesseract path does not exist.")
                print("Please check the path and try again.")
                sys.exit(1)

        else:
            # Check for common installation paths for Tesseract-OCR
            tesseract_path = None  # Initialize tesseract_path to None
            if os.path.exists(os.path.join(os.environ["ProgramFiles"], "Tesseract-OCR", "tesseract.exe")):  # 64-bit systems
                tesseract_path = os.path.join(os.environ["ProgramFiles"], "Tesseract-OCR", "tesseract.exe")
            elif os.path.exists(os.path.join(os.environ["ProgramFiles(x86)"], "Tesseract-OCR", "tesseract.exe")):  # 32-bit systems
                tesseract_path = os.path.join(os.environ["ProgramFiles(x86)"], "Tesseract-OCR", "tesseract.exe")
            elif os.path.exists(os.path.join(os.environ["ProgramW6432"], "Tesseract-OCR", "tesseract.exe")):  # 32-bit systems on 64-bit OS
                tesseract_path = os.path.join(os.environ["ProgramW6432"], "Tesseract-OCR", "tesseract.exe")
            elif os.path.exists(os.path.join(os.environ["LOCALAPPDATA"], "Microsoft", "WindowsApps", "Tesseract-OCR", "tesseract.exe")):  # Windows Store apps
                tesseract_path = os.path.join(os.environ["LOCALAPPDATA"], "Microsoft", "WindowsApps", "Tesseract-OCR", "tesseract.exe")
            elif os.path.exists(os.path.join(os.environ["ProgramData"], "Tesseract-OCR", "tesseract.exe")):  # shared data
                tesseract_path = os.path.join(os.environ["ProgramData"], "Tesseract-OCR", "tesseract.exe")
            else:

                # If Tesseract path is not found in common installation directories, print a message
                print("Tesseract-OCR not found or not installed in the default Tesseract installation path.")
                print("For installation with user-defined path, please set the 'tesseract_user_path' variable in config file.")
                print("Please visit: https://github.com/UB-Mannheim/tesseract/wiki")
                sys.exit(1)


        # Set the Tesseract path in the environment variables
        os.environ["TESSERACT_PATH"] = tesseract_path
        path_tesseract_cmd = tesseract_path
        # print("Tesseract-OCR path:", tesseract_path)
        # print("path_tesseract_cmd:", path_tesseract_cmd)

        # Check if Tesseract path and version are valid
        if tesseract_path and os.path.exists(tesseract_path):
            try:
                subprocess.check_output([tesseract_path, "--version"], stderr=subprocess.STDOUT)
                # print("Tesseract-OCR full version:", subprocess.check_output([tesseract_path, "--version"]).decode().split()[1])  # Extract the version number
                full_version = subprocess.check_output([tesseract_path, "--version"]).decode().split()[1]
                version = full_version.split('v')[1].split('.')[0:2]  # Extract the first two digits of the version number
                # print('full version := ', full_version)
                # print('version := ', version)
                # Convert version to a tuple of integers
                version = tuple(map(int, version))
                # print("Tesseract-OCR version:", version)  # Print the version tuple

                # Check if the version is below the minimum required version (5.0)
                if version < (5, 0):
                    print("Tesseract version is below the minimum required version (5.0 ).")
                    sys.exit(1)
                else:
                    print("Tesseract-OCR is compatible.")

            except subprocess.CalledProcessError as e:
                print("Error:", e.output.decode())
                sys.exit(1)
        else:
            # If Tesseract path is not found in environment variables, print a message
            print("Tesseract-OCR not found or not installed correctly.")
            print("Please visit: https://github.com/UB-Mannheim/tesseract/wiki")
            sys.exit(1)

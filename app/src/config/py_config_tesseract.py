# //===================================================//
# Tesseract-OCR is an open-source OCR engine used to extract text from images.
# Ensure that Tesseract-OCR is installed in the default Tesseract-OCR installation path.
# If Tesseract-OCR is not installed, please visit the following link to download and install it:
# https://github.com/UB-Mannheim/tesseract/wiki


# //===================================================//
# If the Tesseract-OCR installation path is different from the default path: please follow the steps below:
# 1) set the `flag_user_path` variable to `True`.
# 2) set the `tesseract_user_path` variable to the full path of the `tesseract.exe` executable file.

# Step 1:
# flag_user_path = False      # Use the default Tesseract-OCR installation path
flag_user_path = True     # Use the user Tesseract-OCR installation path

# Step 2:
tesseract_user_path = r'C:/Program Files/Tesseract-OCR/tesseract.exe'           # Change this to your Tesseract-OCR installation path
# tesseract_user_path = r'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'   # Change this to your Tesseract-OCR installation path



# //===================================================//
# Import necessary libraries and modules
import sys
import os
import subprocess

# Import the Tesseract-OCR path from the main GUI module.
def check_tesseract():
    """
    Searches for the Tesseract OCR installation path.
    This function scans common installation directories and all available drives
    to locate the Tesseract executable on the system.
    """

    global tesseract_path, path_tesseract_cmd
    print("=== check_tesseract ===")

    # Check if the Tesseract path is set in the environment variables
    env_vars = os.environ  # Get system environment variables
    # print("Environment variables:", env_vars)

    if "TESSERACT_PATH" in env_vars:
        print("Tesseract path is set in environment variables:", env_vars["TESSERACT_PATH"])
    else:
        # print("Tesseract path is not set in environment variables.")
        # print("Searching for Tesseract OCR installation...")

        # Check for common installation paths for Tesseract OCR
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
            print("Tesseract OCR path not found or not installed correctly.")
            print("Please install Tesseract OCR in the default installation path.")
            print("Visit: https://github.com/UB-Mannheim/tesseract/wiki")
            sys.exit(1)

        # Set the Tesseract path in the environment variables
        os.environ["TESSERACT_PATH"] = tesseract_path
        path_tesseract_cmd = tesseract_path
        # print("Tesseract path:", tesseract_path)

        # Check flag_user_path to determine which Tesseract path to use
        if flag_user_path:
            path_tesseract_cmd = tesseract_user_path
        else:
            path_tesseract_cmd = tesseract_path
        # print("path_tesseract_cmd:", path_tesseract_cmd)


        # Check if Tesseract path is valid
        if tesseract_path and os.path.exists(tesseract_path):
            try:
                subprocess.check_output([tesseract_path, "--version"], stderr=subprocess.STDOUT)
                # print("Tesseract OCR full version:", subprocess.check_output([tesseract_path, "--version"]).decode().split()[1])  # Extract the version number
                full_version = subprocess.check_output([tesseract_path, "--version"]).decode().split()[1]
                version = full_version.split('v')[1].split('.')[0:2]  # Extract the first two digits of the version number
                # print('full version := ', full_version)
                # print('version := ', version)
                # Convert version to a tuple of integers
                version = tuple(map(int, version))
                # print("Tesseract OCR version:", version)  # Print the version tuple

                # Check if the version is below the minimum required version (5.0)
                if version < (5, 0):
                    print("Tesseract version is below the minimum required version (5.0 ).")
                    sys.exit(1)
                else:
                    print("Tesseract OCR is compatible.")

            except subprocess.CalledProcessError as e:
                print("Error:", e.output.decode())
                sys.exit(1)
        else:
            # If Tesseract path is not found in environment variables, print a message
            print("Tesseract OCR not found or not installed correctly.")
            print("Please visit: https://github.com/UB-Mannheim/tesseract/wiki")
            sys.exit(1)

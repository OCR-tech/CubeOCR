# This file contains configuration settings and flags for the CubeOCR application.
# It includes settings for the GUI, text editor, and window settings.

# //===================================================//
# Flags and configurations related to the GUI module (`py_main_gui.py`).
FLAG_SETTING_INIT = True        # Indicates whether the settings are initialized.
FLAG_IMAGE_ROTATE0 = False      # Flag for no image rotation.
FLAG_IMAGE_ROTATE90 = False     # Flag for rotating the image by 90 degrees.
FLAG_IMAGE_ROTATE180 = False    # Flag for rotating the image by 180 degrees.

# Folder and file names used in the application.
FOLDERNAME1 = "CubeOCR"         # Name of the main folder for storing OCR-related data.
FOLDERNAME2 = "data"            # Subfolder for storing data files.
FILENAME2 = "temp.txt"          # Temporary file for storing intermediate data.
FILENAME3 = "data1"             # Data file 1.
FILENAME4 = "data2"             # Data file 2.
FILENAME5 = "data3"             # Data file 3.
FILENAME6 = "data4"             # Data file 4.

# Default folder names for user directories.
DESKTOP_FOLDER = 'Desktop'      # Name of the desktop folder.
DOCUMENTS_FOLDER = 'Documents'  # Name of the documents folder.

# Lock file configuration.
LOCK_FILE_NAME = 'app.lock'     # Name of the lock file used for application state management.

# //===================================================//
# Flags and configurations related to the text editor module (`py_main_function_editor.py`).
FLAG_SELECTALL = False          # Flag to indicate whether "Select All" is enabled.
FLAG_SAVEPATH_INIT = True       # Indicates whether the save path is initialized.
FLAG_MAXIMIZE = False           # Flag to indicate whether the window is maximized.
FLAG_FONT_INIT = True           # Indicates whether the font settings are initialized.

# File-related configurations.
FILENUM = 1                     # Default file number for saving files.
FILENAME1 = "text"              # Default file name for text files.

# Font size configurations.
FONT_TEXT_SIZE_MAX = 48         # Maximum font size for text.
FONT_TEXT_SIZE_MIN = 6          # Minimum font size for text.
FONT_TEXT_SIZE_INIT = 10        # Initial font size for text.

# Font family and index configurations.
FONT_TEXT_FAMILY_INIT = 'Arial' # Default font family for text.
FONT_TEXT_INDEX_MAX = 10        # Maximum font index.
FONT_TEXT_INDEX_MIN = 0         # Minimum font index.

# Opacity configurations for text.
OPACITY_TEXT_MAX = 1            # Maximum opacity for text.
OPACITY_TEXT_MIN = 0.005        # Minimum opacity for text.

# //===================================================//
# Flags and configurations related to the window settings module (`py_window_setting.py`).
FLAG_COMBOBOX_SELECT_ALL = False    # Indicates whether "Select All" is selected in a combobox.
FLAG_SELECT_ALL_INIT = True         # Indicates whether "Select All" is initialized.

# Flags for light theme settings.
FLAG_TBTHEMELIGHT = False       # Toolbar theme (light).
FLAG_FGTHEMELIGHT = False       # Foreground theme (light).
FLAG_BGTHEMELIGHT = False       # Background theme (light).
FLAG_FONTTHEMELIGHT = False     # Font theme (light).
FLAG_BTTHEMELIGHT = False       # Button theme (light).
FLAG_BDTHEMELIGHT = False       # Border theme (light).

# Flags for dark theme settings.
FLAG_TBTHEMEDARK = False        # Toolbar theme (dark).
FLAG_FGTHEMEDARK = False        # Foreground theme (dark).
FLAG_BGTHEMEDARK = False        # Background theme (dark).
FLAG_FONTTHEMEDARK = False      # Font theme (dark).
FLAG_BTTHEMEDARK = False        # Button theme (dark).
FLAG_BDTHEMEDARK = False        # Border theme (dark).

# Import necessary libraries and modules
import sys
import locale
import re
import time
import ctypes
import cv2
import os
import glob
import subprocess
import platform
from pynput import keyboard
from pathlib import Path
import numpy as np

# Import PyQt5 modules for GUI development
from PyQt5 import QtCore, QtGui, QtPrintSupport
from PyQt5.QtCore import Qt

from PyQt5.QtCore import Qt, pyqtSignal as Signal
from PyQt5.QtCore import pyqtSignal

from PyQt5.QtCore import pyqtSlot as Slot

from PyQt5.QtGui import qRgb, QColor, QCursor, QFont, QIcon, QKeySequence, QPixmap, QImage, QPalette, QPainterPath, \
                        QPainter, QPen, QBrush, QRegion, QTransform, QFontMetrics, QTextOption, QCloseEvent, QStandardItemModel, \
                        QTextCharFormat, QTextCursor, QTextListFormat, QTextDocument

from PyQt5.QtCore import QSize, Qt, QLocale, QTimer, QRectF, QMetaObject, QFile, QIODevice, QTextStream, QRect, QLockFile

from PyQt5.QtWidgets import qApp, QApplication, QMainWindow, QWidget, QMessageBox, QAction, QMenu, QShortcut, QComboBox, \
                            QSystemTrayIcon, QRubberBand, QGraphicsColorizeEffect, QSpacerItem, QSizePolicy, QGridLayout, \
                            QFrame, QLabel, QTextEdit, QHBoxLayout, QVBoxLayout, QStatusBar, QToolBar, QToolButton, \
                            QFontComboBox, QTabWidget, QGroupBox, QCheckBox, QRadioButton, QPushButton, QSlider, QDialog, \
                            QFormLayout, QFontDialog, QScrollArea, QLineEdit, QColorDialog, QFileDialog, QGraphicsDropShadowEffect, \
                            QTableWidget, QTableWidgetItem, QAbstractItemView, QHeaderView

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt

# from PyQt5.QtWidgets import QAction

# Import custom configurations and resources
# from py_config import FOLDERNAME1, FOLDERNAME2
# from py_config import FLAG_IMAGE_ROTATE0, FLAG_IMAGE_ROTATE90, FLAG_IMAGE_ROTATE180
# from py_config import FILENAME2, FILENAME3, FILENAME4, FILENAME5, FILENAME6
# from py_config import FLAG_SETTING_INIT

from src.resource.resources_rc import *

# global WIDTH, HEIGHT

########################################################################
class MainGuiWindow(QMainWindow):
    """
    Main GUI window class for the application.
    """
    doubleClicked = Signal()    # Custom signal for double-click events

    def __init__(self):
        """
        Initializes the main GUI window.
        """
        super().__init__()
        self.initUI()           # Call the method to set up the UI

    def initUI(self):
        """
        Sets up the user interface for the main window.
        """
        global WIDTH, HEIGHT, WIDTH1, HEIGHT1
        global WIDTH1_MAX, HEIGHT1_MIN, HEIGHT1_MAX
        global x0Pos, y0Pos, x1Pos, y1Pos

        # Initialize secondary windows
        self.window2 = None                 # Setting window
        self.window3 = None                 # ColorPicker window
        self.window4 = None                 # FindReplace window
        self.window5 = None                 # Tutorial window
        self.window6 = None                 # Help window
        self.window7 = None                 # About window

        # WIDTH = 1920
        # HEIGHT = 1080

        # Flag to track window resizing
        MainGuiWindow.flag_resize_window = False

        print('=== MainGuiWindow (begin) ===')
        # Get screen dimensions
        screen_size = QApplication.primaryScreen()
        if screen_size is not None:
            WIDTH1 = screen_size.geometry().width()
            HEIGHT1 = screen_size.geometry().height()
            WIDTH = WIDTH1
            HEIGHT = HEIGHT1 - 40
        # print('geometry1 :=', screen_size.geometry())  # Print screen geometry for debugging
        # print('WIDTH1 :=', WIDTH1)  # Print width for debugging
        # print('HEIGHT1 :=', HEIGHT1)  # Print height for debugging

        # Set initial positions for the window
        x1Pos = int(WIDTH/2)
        y1Pos = int(HEIGHT/2)
        x0Pos = int(WIDTH/2)
        y0Pos = int(HEIGHT/2)

        # Define minimum and maximum dimensions for the window
        MainGuiWindow.WIDTH1_MIN = int(0.235*WIDTH1)
        WIDTH1_MAX = int(0.985*WIDTH1)
        HEIGHT1_MIN = int(0.035*HEIGHT1)
        HEIGHT1_MAX = int(0.9*HEIGHT1)

        # Set window properties
        self.setObjectName("MainGuiWindow")
        self.setGeometry(0, 0, WIDTH, HEIGHT)              # Set window size and position
        self.setWindowOpacity(1)                        # Set full opacity
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)      # Remove window frame

        # Add a keyboard shortcut for exiting the application
        self.shortcut = QShortcut(QKeySequence("Ctrl+q"), self)
        self.shortcut.activated.connect(self.exitKeyPressed_ShortCut)

        # Set application ID for Windows taskbar icon
        myappid = 'mycompany.myproduct.subproduct.version'                      # arbitrary string
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)  # show taskbar icon for Windows

        # Initialize system tray, locale, and configurations
        self.createSystemTray()
        self.setSystemLocale()
        self.LoadConfigFile()
        self.setFlagOCR()
        self.setRubberBand()
        self.setCursorShape()

        # Set the system font size
        font_system = QFont()
        font_system.setPointSize(MainGuiWindow.FontSystemSizeVar1)
        QApplication.setFont(font_system)

        print('=== MainGuiWindow (end) ===')
        self.show()     # Display the main window

    #//===================================================//
    def hotkeyFcn(self):
        """
        Sets up global hotkeys for the application.
        This function uses the `pynput` library to listen for global hotkeys.
        """

        def on_activate_ctrl_command():
            """
            Callback for `<ctrl>+<cmd>` or `<ctrl>+<alt>` hotkeys. Updates the status combo box and cursor.
            """
            print('=== on_activate_ctrl_command ===')
            self.statusComboBox.setCurrentIndex(1)
            self.updateCursor()

        def on_activate_ctrl_q():
            """
            Callback for `<ctrl>+q` hotkey. Exits the application.
            """
            print('=== on_activate_ctrl_q ===')
            self.exitKeyPressed_Hotkey()

        # Define global hotkeys and their corresponding callbacks
        listener = keyboard.GlobalHotKeys({
                '<ctrl>+<cmd>': on_activate_ctrl_command,
                '<ctrl>+<alt>': on_activate_ctrl_command,
                '<ctrl>+q': on_activate_ctrl_q})
        listener.start()        # Start listening for hotkeys

    #//===================================================//
    def exitKeyPressed_Hotkey(self):
        """
        Handles the exit operation triggered by a hotkey.
        """
        print('=== exitKeyPressed ===')
        self.close()
        MainGuiWindow.exitProgram(self)

    #//===================================================//
    def exitKeyPressed_ShortCut(self):
        """
        Handles the exit operation triggered by a keyboard shortcut.
        """
        print('=== exitKeyPressed ===')
        QTimer.singleShot(150,self.exitProgram)

    #//===================================================//
    def setSystemLocale(self):
        """
        Sets the system locale for the application.
        - Sets the default locale to `en_US`.
        - Detects the system's language and maps it to a corresponding flag.
        - Supports a wide range of languages.
        """
        global flag_language_system_locale
        # global flag_language_all, flag_language_system_locale

        print("=== setSystemLocale ===")
        QLocale.setDefault(QLocale('en_US'))        # Set default locale to English (US)

        # Define all supported languages as a concatenated string
        # flag_language_all =  'afr'+'+'+'sqi'+'+'+'amh'+'+'+'ara'+'+'+'hye'+'+'+'asm'+'+'+'aze'+'+'+'aze_cyrl'+'+'+ \
        #                      'eus'+'+'+'bel'+'+'+'ben'+'+'+'bos'+'+'+'bre'+'+'+'bul'+'+'+'mya'+'+'+ \
        #                      'spa_old'+'+'+'cat'+'+'+'ceb'+'+'+'chi_sim'+'+'+'chi_tra'+'+'+'chi_sim_vert'+'+'+'chi_tra_vert'+'+'+'chr'+'+'+'cos'+'+'+ \
        #                      'hrv'+'+'+'ces'+'+'+'dan'+'+'+'div'+'+'+'nld'+'+'+'dzo'+'+'+'epo'+'+'+ \
        #                      'est'+'+'+'fao'+'+'+'fil'+'+'+'fin'+'+'+'fra'+'+'+'fry'+'+'+'gla'+'+'+ \
        #                      'glg'+'+'+'kat'+'+'+'deu'+'+'+'ell'+'+'+'guj'+'+'+'hat'+'+'+'heb'+'+'+ \
        #                      'hin'+'+'+'hun'+'+'+'isl'+'+'+'ind'+'+'+'iku'+'+'+'gle'+'+'+'ita'+'+'+ \
        #                      'jpn'+'+'+'jpn_vert'+'+'+'jav'+'+'+'kan'+'+'+'kaz'+'+'+'khm'+'+'+'kor'+'+'+ \
        #                      'kmr'+'+'+'kir'+'+'+'lao'+'+'+'lat'+'+'+'lav'+'+'+'lit'+'+'+'ltz'+'+'+ \
        #                      'mkd'+'+'+'msa'+'+'+'mal'+'+'+'mlt'+'+'+'mri'+'+'+'mar'+'+'+'mon'+'+'+ \
        #                      'nep'+'+'+'nor'+'+'+'oci'+'+'+'ori'+'+'+'pan'+'+'+'pus'+'+'+'fas'+'+'+ \
        #                      'pol'+'+'+'por'+'+'+'que'+'+'+'ron'+'+'+'rus'+'+'+'san'+'+'+'srp'+'+'+'srp_latn'+'+'+ \
        #                      'snd'+'+'+'sin'+'+'+'slk'+'+'+'slv'+'+'+'spa'+'+'+'sun'+'+'+'swa'+'+'+ \
        #                      'swe'+'+'+'syr'+'+'+'tgk'+'+'+'tam'+'+'+'tat'+'+'+'tel'+'+'+'tha'+'+'+ \
        #                      'bod'+'+'+'tir'+'+'+'ton'+'+'+'tur'+'+'+'ukr'+'+'+'urd'+'+'+'uig'+'+'+ \
        #                      'uzb'+'+'+'uzb_cyrl'+'+'+'vie'+'+'+'cym'+'+'+'yid'+'+'+'yor'

        # Maps a locale code to a corresponding language flag.
        locale_map = {
            'af_': 'afr', 'am_': 'amh', 'ar_': 'ara', 'as_': 'asm', 'az_': 'aze+aze_cyrl',
            'be_': 'bel', 'bg_': 'bul', 'bn_': 'ben', 'bo_': 'bod', 'br_': 'bre',
            'bs_': 'bos', 'ca_': 'cat', 'chr_': 'chr', 'cs_': 'ces', 'cy_': 'cym',
            'da_': 'dan', 'de_': 'deu', 'dv_': 'div', 'dz_': 'dzo', 'el_': 'ell',
            'en_': 'eng', 'eo_': 'epo', 'es_': 'spa', 'et_': 'est', 'eu_': 'eus',
            'fa_': 'fas', 'fi_': 'fin', 'fil_': 'fil', 'fo_': 'fao', 'fr_': 'fra',
            'fy_': 'fry', 'ga_': 'gle', 'gd_': 'gla', 'gl_': 'glg', 'gu_': 'guj',
            'he_': 'heb', 'hi_': 'hin', 'hr_': 'hrv', 'ht_': 'hat', 'hu_': 'hun',
            'hy_': 'hye', 'id_': 'ind', 'is_': 'isl', 'it_': 'ita', 'iu_': 'iku',
            'ja_': 'jpn+jpn_vert', 'jv_': 'jav', 'ka_': 'kat', 'kk_': 'kaz', 'km_': 'khm',
            'kn_': 'kan', 'ko_': 'kor', 'ku_': 'kmr', 'ky_': 'kir', 'la_': 'lat',
            'lb_': 'ltz', 'lo_': 'lao', 'lt_': 'lit', 'lv_': 'lav', 'mi_': 'mri',
            'mk_': 'mkd', 'ml_': 'mal', 'mn_': 'mon', 'mr_': 'mar', 'ms_': 'msa',
            'mt_': 'mlt', 'my_': 'mya', 'ne_': 'nep', 'nl_': 'nld', 'no_': 'nor',
            'nn_': 'nor', 'nb_': 'nor', 'oc_': 'oci', 'pa_': 'pan', 'pl_': 'pol',
            'ps_': 'pus', 'pt_': 'por', 'quz_': 'que', 'ro_': 'ron', 'ru_': 'rus',
            'sa_': 'san', 'sd_': 'snd', 'si_': 'sin', 'sk_': 'slk', 'sl_': 'slv',
            'sq_': 'sqi', 'sr_': 'srp+srp_latn', 'su_': 'sun', 'sw_': 'swa', 'sv_': 'swe',
            'ta_': 'tam', 'te_': 'tel', 'tg_': 'tgk', 'th_': 'tha', 'ti_': 'tir',
            'to_': 'ton', 'tr_': 'tur', 'tt_': 'tat', 'uk_': 'ukr', 'ug_': 'uig',
            'ur_': 'urd', 'uz_': 'uzb+uzb_cyrl', 'vi_': 'vie', 'yi_': 'yid', 'yo_': 'yor',
            'zh_': 'chi_tra+chi_tra_vert+chi_sim+chi_sim_vert'
        }

        # Detect the system's locale and map it to a language flag
        locale_lang, _ = locale.getdefaultlocale()
        if locale_lang is not None:
            flag_language_system_locale = locale_map.get(locale_lang[:3], 'eng')
        else:
            print("Error: locale_map is not initialized.")
        print('System locale language :', flag_language_system_locale)

    # //===========================================//
    def LoadConfigFile(self):
        """
        Loads configuration files and initializes global variables for the application.

        - Reads or creates configuration files for themes, settings, whitelist, and blacklist.
        - Sets up paths for configuration files and directories.
        - Initializes global variables for UI settings, themes, and OCR configurations.
        """
        from src.config.py_config import FOLDERNAME1, FOLDERNAME2, FILENAME2, FILENAME3, FILENAME4, FILENAME5, FILENAME6, DESKTOP_FOLDER, DOCUMENTS_FOLDER

        # Define global variables for folder and file paths
        global FOLDERNAME1_new, FOLDERNAME2_new, foldername3_new
        global path_foldernew1, path_foldernew2, path_FILENAME3, path_FILENAME4, path_FILENAME5, path_FILENAME6

        print('=== LoadConfigFile ===')

        # Set paths for desktop and documents directories
        MainGuiWindow.path_desktop = str(Path.home()/DESKTOP_FOLDER).replace('\\','/')
        MainGuiWindow.path_documents = self.path_desktop.replace(DESKTOP_FOLDER,DOCUMENTS_FOLDER)

        # Create necessary directories for configuration files
        FOLDERNAME1_new = self.path_documents + '/' + FOLDERNAME1
        FOLDERNAME2_new = str(Path(FOLDERNAME1_new)) + '/' + FOLDERNAME2
        Path(FOLDERNAME2_new).mkdir(parents=True,exist_ok=True)

        # Define paths for configuration files
        path_foldernew1 = str(Path(FOLDERNAME1_new))
        path_foldernew2 = str(Path(FOLDERNAME2_new)).replace('\\','/')
        path_FILENAME3 = str(path_foldernew2) + '/' + str(FILENAME3)
        path_FILENAME4 = str(path_foldernew2) + '/' + str(FILENAME4)
        path_FILENAME5 = str(path_foldernew2) + '/' + str(FILENAME5)
        path_FILENAME6 = str(path_foldernew2) + '/' + str(FILENAME6)

        # Store file paths in the MainGuiWindow class
        MainGuiWindow.file3 = Path(path_FILENAME3)
        MainGuiWindow.file4 = Path(path_FILENAME4)
        MainGuiWindow.file5 = Path(path_FILENAME5)
        MainGuiWindow.file6 = Path(path_FILENAME6)

        # Define global variables for theme and UI settings
        global FontTextFamilyLightVar1InitEnc, FontTextFamilyDarkVar1InitEnc
        global FontTextColorLightVar1InitEnc, FontTextColorDarkVar1InitEnc
        global FontTextSizeLightVar1InitEnc, FontTextSizeDarkVar1InitEnc
        global ThemeVar1InitEnc, OpacityTextLightVar1InitEnc, OpacityTextDarkVar1InitEnc
        global DirectionTextVar1InitEnc, ParagraphTextLightVar1InitEnc, ParagraphTextDarkVar1InitEnc, DockingVar1InitEnc
        global FlagToolbarVar1InitEnc, FlagFormatbarVar1InitEnc, FlagStatusbarVar1InitEnc

        try:
            # Check if the theme configuration file exists
            if (self.file3.exists()):
                # Read theme settings from the file
                with open(self.file3, "r") as f_obj:
                    ThemeVar1InitEnc, OpacityTextLightVar1InitEnc, OpacityTextDarkVar1InitEnc, \
                    DirectionTextVar1InitEnc, ParagraphTextLightVar1InitEnc, ParagraphTextDarkVar1InitEnc, DockingVar1InitEnc, \
                    FlagToolbarVar1InitEnc, FlagFormatbarVar1InitEnc, FlagStatusbarVar1InitEnc, FontTextSizeLightVar1InitEnc, FontTextSizeDarkVar1InitEnc, \
                    FontTextColorLightVar1InitEnc, FontTextColorDarkVar1InitEnc, FontTextFamilyLightVar1InitEnc, FontTextFamilyDarkVar1InitEnc = f_obj.readlines()
            else:
                # Create a new theme configuration file with default values
                print('=== create new config_setup.txt ===')
                with open(self.file3, "w") as f_obj:
                    f_obj.write(f"1011\n")                                      # THEME
                    f_obj.write(f"0111\n")                                      # OPACITY_TEXT_LIGHT
                    f_obj.write(f"0010\n")                                      # OPACITY_TEXT_DARK
                    f_obj.write(f"0101\n")                                      # DIRECTION_TEXT
                    f_obj.write(f"1011\n")                                      # PARAGRAPH_TEXT_LIGHT
                    f_obj.write(f"0110\n")                                      # PARAGRAPH_TEXT_DARK
                    f_obj.write(f"0000\n")                                      # DOCKING
                    f_obj.write(f"1101\n")                                      # FLAG_TOOLBAR
                    f_obj.write(f"0101\n")                                      # FLAG_FORMATBAR
                    f_obj.write(f"1011\n")                                      # FLAG_STATUSBAR
                    f_obj.write(f"00010000\n")                                  # FONT_TEXT_SIZE_LIGHT
                    f_obj.write(f"00010000\n")                                  # FONT_TEXT_SIZE_DARK
                    f_obj.write(f"000000000000000000000000\n")                  # FONT_TEXT_COLOR_LIGHT
                    f_obj.write(f"111111111111111111111111\n")                  # FONT_TEXT_COLOR_DARK
                    f_obj.write(f"1010000111010010110010011100000111001100\n")  # FONT_TEXT_FAMILY_LIGHT
                    f_obj.write(f"1010000111010010110010011100000111001100")    # FONT_TEXT_FAMILY_DARK

                # Re-read the newly created theme configuration file
                with open(self.file3, "r") as f_obj:
                    ThemeVar1InitEnc, OpacityTextLightVar1InitEnc, OpacityTextDarkVar1InitEnc, \
                    DirectionTextVar1InitEnc, ParagraphTextLightVar1InitEnc, ParagraphTextDarkVar1InitEnc, DockingVar1InitEnc, \
                    FlagToolbarVar1InitEnc, FlagFormatbarVar1InitEnc, FlagStatusbarVar1InitEnc, FontTextSizeLightVar1InitEnc, FontTextSizeDarkVar1InitEnc, \
                    FontTextColorLightVar1InitEnc, FontTextColorDarkVar1InitEnc, FontTextFamilyLightVar1InitEnc, FontTextFamilyDarkVar1InitEnc = f_obj.readlines()
        except:
            print('=== Error ===')

        # Define global variables for additional settings
        global LanguageVar1Init, LanguageVar1InitEnc
        global ThemeLightColorTBVar1InitEnc, ThemeLightColorFGVar1InitEnc, ThemeLightColorBGVar1InitEnc, ThemeLightColorFontVar1InitEnc, ThemeLightColorBTVar1InitEnc, ThemeLightColorBDVar1InitEnc
        global ThemeDarkColorTBVar1InitEnc, ThemeDarkColorFGVar1InitEnc, ThemeDarkColorBGVar1InitEnc, ThemeDarkColorFontVar1InitEnc, ThemeDarkColorBTVar1InitEnc, ThemeDarkColorBDVar1InitEnc
        global RBBColorVar1InitEnc, LanguageSystemVar1InitEnc, MathEquationVar1InitEnc, TextLayoutVar1InitEnc
        global DetectedTextVar1InitEnc, DetectedTextLetterVar1InitEnc, DetectedTextLowerVar1InitEnc, DetectedTextUpperVar1InitEnc
        global DetectedTextNumberVar1InitEnc, DetectedTextPuncVar1InitEnc, DetectedTextMiscVar1InitEnc, OutputFormatVar1InitEnc, OptimizationVar1InitEnc
        global PageLayoutAutoRotatePageVar1InitEnc, PageLayoutDeskewVar1InitEnc, PageLayoutDecolumnizeVar1InitEnc, PageLayoutRemoveTableVar1InitEnc
        global PageLayoutRemoveWatermarkVar1InitEnc, PageLayoutRemoveUnderlineVar1InitEnc, PageLayoutRemoveSpaceVar1InitEnc, PageLayoutRemoveLineVar1InitEnc
        global LayoutDespeckleVar1InitEnc, LayoutThresholdVar1InitEnc, LayoutInvertColorVar1InitEnc, LayoutThresholdAdaptiveVar1InitEnc, LayoutSharpenVar1InitEnc, LayoutContrastVar1InitEnc
        global FilteringBackgroundNoiseVar1InitEnc, FilteringBackgroundNoiseIntVar1InitEnc, FilteringTextNoiseVar1InitEnc, FilteringTextNoiseIntVar1InitEnc
        global FilteringTextErosionVar1InitEnc, FilteringTextErosionIntVar1InitEnc, FilteringTextDilationVar1InitEnc, FilteringTextDilationIntVar1InitEnc
        global FilteringThresholdVar1InitEnc, FilteringThresholdLowerIntVar1InitEnc, FilteringThresholdUpperIntVar1InitEnc
        global DisplayColorImageVar1InitEnc, DisplayGrayImageVar1InitEnc, DisplayProcessedImageVar1InitEnc, DisplayProcessedAllImageVar1InitEnc
        global WhitelistVar1InitEnc, Whitelist1Var1InitEnc, Whitelist2Var1InitEnc, Whitelist3Var1InitEnc, Whitelist4Var1InitEnc, Whitelist5Var1InitEnc
        global BlacklistVar1InitEnc, Blacklist1Var1InitEnc, Blacklist2Var1InitEnc, Blacklist3Var1InitEnc, Blacklist4Var1InitEnc, Blacklist5Var1InitEnc
        global ThemeLightColorVar1InitEnc, ThemeDarkColorVar1InitEnc, CursorShapeVar1InitEnc, RBBThicknessVar1InitEnc, RBBOpacityVar1InitEnc
        global FontSystemSizeVar1InitEnc, BorderStyleVar1InitEnc, TextEditorIconSizeVar1InitEnc, TextEditorStatusBarVar1InitEnc, TextEditorModeVar1InitEnc, SystemTrayIconVar1InitEnc

        try:
            # Check if the general settings file exists
            if (self.file4.exists()):
                # Read general settings from the file
                with open(self.file4, "r") as f_obj:
                    LanguageSystemVar1InitEnc, MathEquationVar1InitEnc, TextLayoutVar1InitEnc, \
                    DetectedTextVar1InitEnc, DetectedTextLetterVar1InitEnc, DetectedTextLowerVar1InitEnc, DetectedTextUpperVar1InitEnc, \
                    DetectedTextNumberVar1InitEnc, DetectedTextPuncVar1InitEnc, DetectedTextMiscVar1InitEnc, OutputFormatVar1InitEnc, OptimizationVar1InitEnc, \
                    PageLayoutAutoRotatePageVar1InitEnc, PageLayoutDeskewVar1InitEnc, PageLayoutDecolumnizeVar1InitEnc, PageLayoutRemoveTableVar1InitEnc, \
                    PageLayoutRemoveWatermarkVar1InitEnc, PageLayoutRemoveUnderlineVar1InitEnc, PageLayoutRemoveSpaceVar1InitEnc, PageLayoutRemoveLineVar1InitEnc, \
                    LayoutDespeckleVar1InitEnc, LayoutThresholdVar1InitEnc, LayoutInvertColorVar1InitEnc, LayoutThresholdAdaptiveVar1InitEnc, LayoutSharpenVar1InitEnc, LayoutContrastVar1InitEnc, \
                    FilteringBackgroundNoiseVar1InitEnc, FilteringBackgroundNoiseIntVar1InitEnc, FilteringTextNoiseVar1InitEnc, FilteringTextNoiseIntVar1InitEnc, \
                    FilteringTextErosionVar1InitEnc, FilteringTextErosionIntVar1InitEnc, FilteringTextDilationVar1InitEnc, FilteringTextDilationIntVar1InitEnc, FilteringThresholdVar1InitEnc, \
                    DisplayColorImageVar1InitEnc, DisplayGrayImageVar1InitEnc, DisplayProcessedImageVar1InitEnc, DisplayProcessedAllImageVar1InitEnc, \
                    WhitelistVar1InitEnc, Whitelist1Var1InitEnc, Whitelist2Var1InitEnc, Whitelist3Var1InitEnc, Whitelist4Var1InitEnc, Whitelist5Var1InitEnc, \
                    BlacklistVar1InitEnc, Blacklist1Var1InitEnc, Blacklist2Var1InitEnc, Blacklist3Var1InitEnc, Blacklist4Var1InitEnc, Blacklist5Var1InitEnc, \
                    ThemeLightColorVar1InitEnc, ThemeDarkColorVar1InitEnc, CursorShapeVar1InitEnc, RBBThicknessVar1InitEnc, RBBOpacityVar1InitEnc, \
                    FontSystemSizeVar1InitEnc, BorderStyleVar1InitEnc, TextEditorIconSizeVar1InitEnc, TextEditorStatusBarVar1InitEnc, TextEditorModeVar1InitEnc, SystemTrayIconVar1InitEnc, \
                    FilteringThresholdLowerIntVar1InitEnc, FilteringThresholdUpperIntVar1InitEnc, \
                    ThemeLightColorTBVar1InitEnc, ThemeLightColorFGVar1InitEnc, ThemeLightColorBGVar1InitEnc, ThemeLightColorFontVar1InitEnc, ThemeLightColorBTVar1InitEnc, ThemeLightColorBDVar1InitEnc, \
                    ThemeDarkColorTBVar1InitEnc, ThemeDarkColorFGVar1InitEnc, ThemeDarkColorBGVar1InitEnc, ThemeDarkColorFontVar1InitEnc, ThemeDarkColorBTVar1InitEnc, ThemeDarkColorBDVar1InitEnc, \
                    RBBColorVar1InitEnc,  LanguageVar1InitEnc = f_obj.readlines()
            else:
                # Create a new general settings file with default values
                print('=== create new config_setting.txt ===')
                with open(self.file4, "w") as f_obj:
                    f_obj.write(f"10010\n")       # LanguageSystemVar1InitEnc
                    f_obj.write(f"01011\n")       # MathEquationVar1InitEnc
                    f_obj.write(f"01001\n")       # TextLayoutVar1InitEnc
                    f_obj.write(f"11011\n")       # DetectedTextVar1InitEnc
                    f_obj.write(f"00110\n")       # DetectedTextLetterVar1InitEnc
                    f_obj.write(f"10100\n")       # DetectedTextLowerVar1InitEnc
                    f_obj.write(f"11101\n")       # DetectedTextUpperVar1InitEnc
                    f_obj.write(f"01100\n")       # DetectedTextNumberVar1InitEnc
                    f_obj.write(f"11011\n")       # DetectedTextPuncVar1InitEnc
                    f_obj.write(f"01100\n")       # DetectedTextMiscVar1InitEnc
                    f_obj.write(f"11101\n")       # OutputFormatVar1InitEnc
                    f_obj.write(f"01001\n")       # OptimizationVar1InitEnc
                    f_obj.write(f"01011\n")       # PageLayoutAutoRotatePageVar1InitEnc
                    f_obj.write(f"10010\n")       # PageLayoutDeskewVar1InitEnc
                    f_obj.write(f"11001\n")       # PageLayoutDecolumnizeVar1InitEnc
                    f_obj.write(f"01100\n")       # PageLayoutRemoveTableVar1InitEnc
                    f_obj.write(f"11011\n")       # PageLayoutRemoveWatermarkVar1InitEnc
                    f_obj.write(f"01011\n")       # PageLayoutRemoveUnderlineVar1InitEnc
                    f_obj.write(f"11011\n")       # PageLayoutRemoveSpaceVar1InitEnc
                    f_obj.write(f"11001\n")       # PageLayoutRemoveLineVar1InitEnc
                    f_obj.write(f"00100\n")       # LayoutDespeckleVar1InitEnc
                    f_obj.write(f"01010\n")       # LayoutThresholdVar1InitEnc
                    f_obj.write(f"10100\n")       # LayoutInvertColorVar1InitEnc
                    f_obj.write(f"11001\n")       # LayoutThresholdAdaptiveVar1InitEnc
                    f_obj.write(f"01010\n")       # LayoutSharpenVar1InitEnc
                    f_obj.write(f"00110\n")       # LayoutContrastVar1InitEnc
                    f_obj.write(f"11011\n")       # FilteringBackgroundNoiseVar1InitEnc
                    f_obj.write(f"01101\n")       # FilteringBackgroundNoiseIntVar1InitEnc
                    f_obj.write(f"11100\n")       # FilteringTextNoiseVar1InitEnc
                    f_obj.write(f"11001\n")       # FilteringTextNoiseIntVar1InitEnc
                    f_obj.write(f"01101\n")       # FilteringTextErosionVar1InitEnc
                    f_obj.write(f"10100\n")       # FilteringTextErosionIntVar1InitEnc
                    f_obj.write(f"10110\n")       # FilteringTextDilationVar1InitEnc
                    f_obj.write(f"10010\n")       # FilteringTextDilationIntVar1InitEnc
                    f_obj.write(f"01010\n")       # FilteringThresholdVar1InitEnc
                    f_obj.write(f"11001\n")       # DisplayColorImageVar1InitEnc
                    f_obj.write(f"10110\n")       # DisplayGrayImageVar1InitEnc
                    f_obj.write(f"01010\n")       # DisplayProcessedImageVar1InitEnc
                    f_obj.write(f"10100\n")       # DisplayProcessedAllImageVar1InitEnc
                    f_obj.write(f"11100\n")       # WhitelistVar1Init
                    f_obj.write(f"01110\n")       # Whitelist1Var1Init
                    f_obj.write(f"01101\n")       # Whitelist2Var1Init
                    f_obj.write(f"11010\n")       # Whitelist3Var1Init
                    f_obj.write(f"10100\n")       # Whitelist4Var1Init
                    f_obj.write(f"10110\n")       # Whitelist5Var1Init
                    f_obj.write(f"11001\n")       # BlacklistVar1Init
                    f_obj.write(f"01110\n")       # Blacklist1Var1Init
                    f_obj.write(f"11011\n")       # Blacklist2Var1Init
                    f_obj.write(f"01101\n")       # Blacklist3Var1Init
                    f_obj.write(f"10100\n")       # Blacklist4Var1Init
                    f_obj.write(f"10100\n")       # Blacklist5Var1Init
                    f_obj.write(f"10100\n")       # ThemeLightColorVar1Init
                    f_obj.write(f"10011\n")       # ThemeDarkColorVar1Init
                    f_obj.write(f"11001\n")       # CursorShapeVar1Init
                    f_obj.write(f"10101\n")       # RBBThicknessVar1Init
                    f_obj.write(f"01111\n")       # RBBOpacityVar1Init
                    f_obj.write(f"11001\n")       # FontSystemSizeVar1Init
                    f_obj.write(f"01100\n")       # BorderStyleVar1Init
                    f_obj.write(f"11000\n")       # TextEditorIconSizeVar1Init
                    f_obj.write(f"01110\n")       # TextEditorStatusBarVar1Init
                    f_obj.write(f"10110\n")       # TextEditorModeVar1Init
                    f_obj.write(f"01101\n")       # SystemTrayIconVar1Init
                    f_obj.write(f"0000\n")        # FilteringThresholdLowerIntVar1InitEnc
                    f_obj.write(f"0000\n")        # FilteringThresholdUpperIntVar1InitEnc
                    f_obj.write(f"101010100101010100000000\n")   # ThemeLightColorTBVar1InitEnc
                    f_obj.write(f"111111111111101110101010\n")   # ThemeLightColorFGVar1InitEnc
                    f_obj.write(f"111111111111111110101010\n")   # ThemeLightColorBGVar1InitEnc
                    f_obj.write(f"010101010000000000000000\n")   # ThemeLightColorFontVar1InitEnc
                    f_obj.write(f"010101010011001100110011\n")   # ThemeLightColorBTVar1InitEnc
                    f_obj.write(f"101010100101010100000000\n")   # ThemeLightColorBDVar1InitEnc
                    f_obj.write(f"001110100011101010010101\n")   # ThemeDarkColorTBVar1InitEnc
                    f_obj.write(f"001110100011101001011010\n")   # ThemeDarkColorFGVar1InitEnc
                    f_obj.write(f"001100110011001101001111\n")   # ThemeDarkColorBGVar1InitEnc
                    f_obj.write(f"111111111111111111111111\n")   # ThemeDarkColorFontVar1InitEnc
                    f_obj.write(f"000100011010101011111111\n")   # ThemeDarkColorBTVar1InitEnc
                    f_obj.write(f"001111110011111111001100\n")   # ThemeDarkColorBDVar1InitEnc
                    f_obj.write(f"000000001100110000000000\n")   # RBBColorVar1InitEnc
                    f_obj.write(f"111110110110110110110110110110110110110110110110110110110110110110110110110110110110110\
110110110110110110110110110110110110110110110110110110110110110110110110110110110110110110110110110110110110110110110110\
110110110110110110110110110110110110110110110110110110110110110110110110110110110110110110110110110110110110110110110110110110110110110110")

                # Read multiple configuration settings from the file.
                with open(self.file4, "r") as f_obj:
                    LanguageSystemVar1InitEnc, MathEquationVar1InitEnc, TextLayoutVar1InitEnc, \
                    DetectedTextVar1InitEnc, DetectedTextLetterVar1InitEnc, DetectedTextLowerVar1InitEnc, DetectedTextUpperVar1InitEnc, \
                    DetectedTextNumberVar1InitEnc, DetectedTextPuncVar1InitEnc, DetectedTextMiscVar1InitEnc, OutputFormatVar1InitEnc, OptimizationVar1InitEnc, \
                    PageLayoutAutoRotatePageVar1InitEnc, PageLayoutDeskewVar1InitEnc, PageLayoutDecolumnizeVar1InitEnc, PageLayoutRemoveTableVar1InitEnc, \
                    PageLayoutRemoveWatermarkVar1InitEnc, PageLayoutRemoveUnderlineVar1InitEnc, PageLayoutRemoveSpaceVar1InitEnc, PageLayoutRemoveLineVar1InitEnc, \
                    LayoutDespeckleVar1InitEnc, LayoutThresholdVar1InitEnc, LayoutInvertColorVar1InitEnc, LayoutThresholdAdaptiveVar1InitEnc, LayoutSharpenVar1InitEnc, LayoutContrastVar1InitEnc, \
                    FilteringBackgroundNoiseVar1InitEnc, FilteringBackgroundNoiseIntVar1InitEnc, FilteringTextNoiseVar1InitEnc, FilteringTextNoiseIntVar1InitEnc, \
                    FilteringTextErosionVar1InitEnc, FilteringTextErosionIntVar1InitEnc, FilteringTextDilationVar1InitEnc, FilteringTextDilationIntVar1InitEnc, FilteringThresholdVar1InitEnc, \
                    DisplayColorImageVar1InitEnc, DisplayGrayImageVar1InitEnc, DisplayProcessedImageVar1InitEnc, DisplayProcessedAllImageVar1InitEnc, \
                    WhitelistVar1InitEnc, Whitelist1Var1InitEnc, Whitelist2Var1InitEnc, Whitelist3Var1InitEnc, Whitelist4Var1InitEnc, Whitelist5Var1InitEnc, \
                    BlacklistVar1InitEnc, Blacklist1Var1InitEnc, Blacklist2Var1InitEnc, Blacklist3Var1InitEnc, Blacklist4Var1InitEnc, Blacklist5Var1InitEnc, \
                    ThemeLightColorVar1InitEnc, ThemeDarkColorVar1InitEnc, CursorShapeVar1InitEnc, RBBThicknessVar1InitEnc, RBBOpacityVar1InitEnc, \
                    FontSystemSizeVar1InitEnc, BorderStyleVar1InitEnc, TextEditorIconSizeVar1InitEnc, TextEditorStatusBarVar1InitEnc, TextEditorModeVar1InitEnc, SystemTrayIconVar1InitEnc, \
                    FilteringThresholdLowerIntVar1InitEnc, FilteringThresholdUpperIntVar1InitEnc, \
                    ThemeLightColorTBVar1InitEnc, ThemeLightColorFGVar1InitEnc, ThemeLightColorBGVar1InitEnc, ThemeLightColorFontVar1InitEnc, ThemeLightColorBTVar1InitEnc, ThemeLightColorBDVar1InitEnc, \
                    ThemeDarkColorTBVar1InitEnc, ThemeDarkColorFGVar1InitEnc, ThemeDarkColorBGVar1InitEnc, ThemeDarkColorFontVar1InitEnc, ThemeDarkColorBTVar1InitEnc, ThemeDarkColorBDVar1InitEnc, \
                    RBBColorVar1InitEnc,  LanguageVar1InitEnc = f_obj.readlines()
        except:
            print('=== Error ===')

        #//====================================//
        # Decode settings from the configuration file
        self.decode_Setting()

        try:
            # Decode settings from the configuration file
            if (self.file5.exists()):
                # Decode settings from the configuration file
                with open(self.file5, "r") as f_obj:
                    WhitelistCharVar1Init = f_obj.readlines()
            else:
                # Create a new whitelist file if it doesn't exist
                print('=== create new whitelist.txt ===')
                with open(self.file5, "w") as f_obj:
                    f_obj.write(f"")                    # Initialize with an empty whitelist (WhitelistCharVar1Init)
                with open(self.file5, "r") as f_obj:
                    WhitelistCharVar1Init = f_obj.readlines()
        except:
            print('=== Error ===')

        try:
            # Check if the blacklist file exists
            if (self.file6.exists()):
                # Read the blacklist characters from the file
                with open(self.file6, "r") as f_obj:
                    BlacklistCharVar1Init = f_obj.readlines()
            else:
                # Create a new blacklist file if it doesn't exist
                print('=== create new blacklist.txt ===')
                with open(self.file6, "w") as f_obj:
                    f_obj.write(f"")                    # Initialize with an empty blacklist ( BlacklistCharVar1Init)

                with open(self.file6, "r") as f_obj:
                    BlacklistCharVar1Init = f_obj.readlines()
        except:
            print('=== Error ===')

        # Convert the whitelist and blacklist character lists into strings
        WhitelistCharVar1Init = ''.join(WhitelistCharVar1Init)
        BlacklistCharVar1Init = ''.join(BlacklistCharVar1Init)

        # Check if the language variable is uninitialized (all zeros)
        if (LanguageVar1Init == "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0"):
            LanguageVar1Init = "1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0"

        # Assign decoded settings to the GUI window's attributes
        MainGuiWindow.ThemeVar1 = int(ThemeVar1Init)
        MainGuiWindow.FontTextSizeLightVar1 = int(FontTextSizeLightVar1Init)
        MainGuiWindow.FontTextSizeDarkVar1 = int(FontTextSizeDarkVar1Init)
        MainGuiWindow.FontTextFamilyLightVar1 = str(FontTextFamilyLightVar1Init)
        MainGuiWindow.FontTextFamilyDarkVar1 = str(FontTextFamilyDarkVar1Init)
        MainGuiWindow.FontTextColorLightVar1 = str(FontTextColorLightVar1Init)
        MainGuiWindow.FontTextColorDarkVar1 = str(FontTextColorDarkVar1Init)
        MainGuiWindow.OpacityTextLightVar1 = float(OpacityTextLightVar1Init)
        MainGuiWindow.OpacityTextDarkVar1 = float(OpacityTextDarkVar1Init)
        MainGuiWindow.DirectionTextVar1 = bool(int(DirectionTextVar1Init))
        MainGuiWindow.ParagraphTextLightVar1 = bool(int(ParagraphTextLightVar1Init))
        MainGuiWindow.ParagraphTextDarkVar1 = bool(int(ParagraphTextDarkVar1Init))
        MainGuiWindow.DockingVar1 = int(DockingVar1Init)
        MainGuiWindow.FlagToolbarVar1 = bool(int(FlagToolbarVar1Init))
        MainGuiWindow.FlagFormatbarVar1 = bool(int(FlagFormatbarVar1Init))
        MainGuiWindow.FlagStatusbarVar1 = bool(int(FlagStatusbarVar1Init))

        # Parse and assign language settings
        MainGuiWindow.LanguageVar1 = LanguageVar1Init
        LanguageVarList1 = LanguageVar1Init.split(',')
        MainGuiWindow.LanguageVarList1 = [eval(i) for i in LanguageVarList1]
        MainGuiWindow.LanguageSystemVar1 = int(LanguageSystemVar1Init)
        MainGuiWindow.MathEquationVar1 = int(MathEquationVar1Init)
        MainGuiWindow.TextLayoutVar1 = int(TextLayoutVar1Init)
        MainGuiWindow.DetectedTextVar1 = int(DetectedTextVar1Init)
        MainGuiWindow.DetectedTextLetterVar1 = int(DetectedTextLetterVar1Init)
        MainGuiWindow.DetectedTextLowerVar1 = int(DetectedTextLowerVar1Init)
        MainGuiWindow.DetectedTextUpperVar1 = int(DetectedTextUpperVar1Init)
        MainGuiWindow.DetectedTextNumberVar1 = int(DetectedTextNumberVar1Init)
        MainGuiWindow.DetectedTextPuncVar1 = int(DetectedTextPuncVar1Init)
        MainGuiWindow.DetectedTextMiscVar1 = int(DetectedTextMiscVar1Init)
        MainGuiWindow.OutputFormatVar1 = int(OutputFormatVar1Init)
        MainGuiWindow.OptimizationVar1 = int(OptimizationVar1Init)
        MainGuiWindow.PageLayoutAutoRotatePageVar1 = int(PageLayoutAutoRotatePageVar1Init)
        MainGuiWindow.PageLayoutDeskewVar1 = int(PageLayoutDeskewVar1Init)
        MainGuiWindow.PageLayoutDecolumnizeVar1 = int(PageLayoutDecolumnizeVar1Init)
        MainGuiWindow.PageLayoutRemoveTableVar1 = int(PageLayoutRemoveTableVar1Init)
        MainGuiWindow.PageLayoutRemoveWatermarkVar1 = int(PageLayoutRemoveWatermarkVar1Init)
        MainGuiWindow.PageLayoutRemoveUnderlineVar1 = int(PageLayoutRemoveUnderlineVar1Init)
        MainGuiWindow.PageLayoutRemoveSpaceVar1 = int(PageLayoutRemoveSpaceVar1Init)
        MainGuiWindow.PageLayoutRemoveLineVar1 = int(PageLayoutRemoveLineVar1Init)
        MainGuiWindow.LayoutDespeckleVar1 = int(LayoutDespeckleVar1Init)
        MainGuiWindow.LayoutThresholdVar1 = int(LayoutThresholdVar1Init)
        MainGuiWindow.LayoutInvertColorVar1 = int(LayoutInvertColorVar1Init)
        MainGuiWindow.LayoutThresholdAdaptiveVar1 = int(LayoutThresholdAdaptiveVar1Init)
        MainGuiWindow.LayoutSharpenVar1 = int(LayoutSharpenVar1Init)
        MainGuiWindow.LayoutContrastVar1 = int(LayoutContrastVar1Init)
        MainGuiWindow.FilteringBackgroundNoiseVar1 = int(FilteringBackgroundNoiseVar1Init)
        MainGuiWindow.FilteringBackgroundNoiseIntVar1 = int(FilteringBackgroundNoiseIntVar1Init)
        MainGuiWindow.FilteringTextNoiseVar1 = int(FilteringTextNoiseVar1Init)
        MainGuiWindow.FilteringTextNoiseIntVar1 = int(FilteringTextNoiseIntVar1Init)
        MainGuiWindow.FilteringTextErosionVar1 = int(FilteringTextErosionVar1Init)
        MainGuiWindow.FilteringTextErosionIntVar1 = int(FilteringTextErosionIntVar1Init)
        MainGuiWindow.FilteringTextDilationVar1 = int(FilteringTextDilationVar1Init)
        MainGuiWindow.FilteringTextDilationIntVar1 = int(FilteringTextDilationIntVar1Init)
        MainGuiWindow.FilteringThresholdVar1 = int(FilteringThresholdVar1Init)
        MainGuiWindow.FilteringThresholdLowerIntVar1 = int(FilteringThresholdLowerIntVar1Init)
        MainGuiWindow.FilteringThresholdUpperIntVar1 = int(FilteringThresholdUpperIntVar1Init)
        MainGuiWindow.DisplayColorImageVar1 = int(DisplayColorImageVar1Init)
        MainGuiWindow.DisplayGrayImageVar1 = int(DisplayGrayImageVar1Init)
        MainGuiWindow.DisplayProcessedImageVar1 = int(DisplayProcessedImageVar1Init)
        MainGuiWindow.DisplayProcessedAllImageVar1 = int(DisplayProcessedAllImageVar1Init)
        MainGuiWindow.WhitelistVar1 = int(WhitelistVar1Init)
        MainGuiWindow.Whitelist1Var1 = int(Whitelist1Var1Init)
        MainGuiWindow.Whitelist2Var1 = int(Whitelist2Var1Init)
        MainGuiWindow.Whitelist3Var1 = int(Whitelist3Var1Init)
        MainGuiWindow.Whitelist4Var1 = int(Whitelist4Var1Init)
        MainGuiWindow.Whitelist5Var1 = int(Whitelist5Var1Init)
        MainGuiWindow.WhitelistCharVar1 = str(WhitelistCharVar1Init)
        MainGuiWindow.BlacklistVar1 = int(BlacklistVar1Init)
        MainGuiWindow.Blacklist1Var1 = int(Blacklist1Var1Init)
        MainGuiWindow.Blacklist2Var1 = int(Blacklist2Var1Init)
        MainGuiWindow.Blacklist3Var1 = int(Blacklist3Var1Init)
        MainGuiWindow.Blacklist4Var1 = int(Blacklist4Var1Init)
        MainGuiWindow.Blacklist5Var1 = int(Blacklist5Var1Init)
        MainGuiWindow.BlacklistCharVar1 = str(BlacklistCharVar1Init)
        MainGuiWindow.ThemeLightColorVar1 = int(ThemeLightColorVar1Init)
        MainGuiWindow.ThemeLightColorTBVar1 = str(ThemeLightColorTBVar1Init)
        MainGuiWindow.ThemeLightColorFGVar1 = str(ThemeLightColorFGVar1Init)
        MainGuiWindow.ThemeLightColorBGVar1 = str(ThemeLightColorBGVar1Init)
        MainGuiWindow.ThemeLightColorFontVar1 = str(ThemeLightColorFontVar1Init)
        MainGuiWindow.ThemeLightColorBTVar1 = str(ThemeLightColorBTVar1Init)
        MainGuiWindow.ThemeLightColorBDVar1 = str(ThemeLightColorBDVar1Init)
        MainGuiWindow.ThemeDarkColorVar1 = int(ThemeDarkColorVar1Init)
        MainGuiWindow.ThemeDarkColorTBVar1 = str(ThemeDarkColorTBVar1Init)
        MainGuiWindow.ThemeDarkColorFGVar1 = str(ThemeDarkColorFGVar1Init)
        MainGuiWindow.ThemeDarkColorBGVar1 = str(ThemeDarkColorBGVar1Init)
        MainGuiWindow.ThemeDarkColorFontVar1 = str(ThemeDarkColorFontVar1Init)
        MainGuiWindow.ThemeDarkColorBTVar1 = str(ThemeDarkColorBTVar1Init)
        MainGuiWindow.ThemeDarkColorBDVar1 = str(ThemeDarkColorBDVar1Init)
        MainGuiWindow.CursorShapeVar1 = int(CursorShapeVar1Init)
        MainGuiWindow.RBBThicknessVar1 = int(RBBThicknessVar1Init)
        MainGuiWindow.RBBOpacityVar1 = int(RBBOpacityVar1Init)
        MainGuiWindow.RBBColorVar1 = str(RBBColorVar1Init)
        MainGuiWindow.FontSystemSizeVar1 = int(FontSystemSizeVar1Init)
        MainGuiWindow.BorderStyleVar1 = int(BorderStyleVar1Init)
        MainGuiWindow.TextEditorIconSizeVar1 = int(TextEditorIconSizeVar1Init)
        MainGuiWindow.TextEditorStatusBarVar1 = int(TextEditorStatusBarVar1Init)
        MainGuiWindow.TextEditorModeVar1 = int(TextEditorModeVar1Init)
        MainGuiWindow.SystemTrayIconVar1 = int(SystemTrayIconVar1Init)
        MainGuiWindow.THICKNESS_RBB = int(MainGuiWindow.RBBThicknessVar1)
        MainGuiWindow.OPACITY_RBB_BG = int(MainGuiWindow.RBBOpacityVar1)

        # Determine the theme (light or dark) based on the theme variable
        if (MainGuiWindow.ThemeVar1 == 0):
            MainGuiWindow.THEME = 'light'
        elif (MainGuiWindow.ThemeVar1 == 1):
            MainGuiWindow.THEME = 'dark'

        # Determine the light theme color based on the theme light color variable
        if (MainGuiWindow.ThemeLightColorVar1 == 0):
            MainGuiWindow.THEME_LIGHT = 'Default'
        elif (MainGuiWindow.ThemeLightColorVar1 == 1):
            MainGuiWindow.THEME_LIGHT = 'Yellow'
        elif (MainGuiWindow.ThemeLightColorVar1 == 2):
            MainGuiWindow.THEME_LIGHT = 'Green'
        elif (MainGuiWindow.ThemeLightColorVar1 == 3):
            MainGuiWindow.THEME_LIGHT = 'Blue'
        elif (MainGuiWindow.ThemeLightColorVar1 == 4):
            MainGuiWindow.THEME_LIGHT = 'Pink'
        elif (MainGuiWindow.ThemeLightColorVar1 == 5):
            MainGuiWindow.THEME_LIGHT = 'Orange'
        elif (MainGuiWindow.ThemeLightColorVar1 == 6):
            MainGuiWindow.THEME_LIGHT = 'Custom'

        # Determine the dark theme color based on the theme dark color variable
        if (MainGuiWindow.ThemeDarkColorVar1 == 0):
            MainGuiWindow.THEME_DARK = 'Default'
        elif (MainGuiWindow.ThemeDarkColorVar1 == 1):
            MainGuiWindow.THEME_DARK = 'Yellow'
        elif (MainGuiWindow.ThemeDarkColorVar1 == 2):
            MainGuiWindow.THEME_DARK = 'Green'
        elif (MainGuiWindow.ThemeDarkColorVar1 == 3):
            MainGuiWindow.THEME_DARK = 'Blue'
        elif (MainGuiWindow.ThemeDarkColorVar1 == 4):
            MainGuiWindow.THEME_DARK = 'Pink'
        elif (MainGuiWindow.ThemeDarkColorVar1 == 5):
            MainGuiWindow.THEME_DARK = 'Orange'
        elif (MainGuiWindow.ThemeDarkColorVar1 == 6):
            MainGuiWindow.THEME_DARK = 'Custom'

        # Assign custom theme colors for light and dark themes
        MainGuiWindow.TB_COLOR_LIGHT_CUSTOM = MainGuiWindow.ThemeLightColorTBVar1
        MainGuiWindow.FG_COLOR_LIGHT_CUSTOM = MainGuiWindow.ThemeLightColorFGVar1
        MainGuiWindow.BG_COLOR_LIGHT_CUSTOM = MainGuiWindow.ThemeLightColorBGVar1
        MainGuiWindow.FONT_COLOR_LIGHT_CUSTOM = MainGuiWindow.ThemeLightColorFontVar1
        MainGuiWindow.BT_COLOR_LIGHT_CUSTOM = MainGuiWindow.ThemeLightColorBTVar1
        MainGuiWindow.BD_COLOR_LIGHT_CUSTOM = MainGuiWindow.ThemeLightColorBDVar1

        MainGuiWindow.TB_COLOR_DARK_CUSTOM = MainGuiWindow.ThemeDarkColorTBVar1
        MainGuiWindow.FG_COLOR_DARK_CUSTOM = MainGuiWindow.ThemeDarkColorFGVar1
        MainGuiWindow.BG_COLOR_DARK_CUSTOM = MainGuiWindow.ThemeDarkColorBGVar1
        MainGuiWindow.FONT_COLOR_DARK_CUSTOM = MainGuiWindow.ThemeDarkColorFontVar1
        MainGuiWindow.BT_COLOR_DARK_CUSTOM = MainGuiWindow.ThemeDarkColorBTVar1
        MainGuiWindow.BD_COLOR_DARK_CUSTOM = MainGuiWindow.ThemeDarkColorBDVar1

        # Assign font and text-related settings
        MainGuiWindow.FONT_TEXT_SIZE_LIGHT = MainGuiWindow.FontTextSizeLightVar1
        MainGuiWindow.FONT_TEXT_SIZE_DARK = MainGuiWindow.FontTextSizeDarkVar1
        MainGuiWindow.FONT_TEXT_FAMILY_LIGHT = MainGuiWindow.FontTextFamilyLightVar1
        MainGuiWindow.FONT_TEXT_FAMILY_DARK = MainGuiWindow.FontTextFamilyDarkVar1
        MainGuiWindow.FONT_TEXT_COLOR_LIGHT = MainGuiWindow.FontTextColorLightVar1
        MainGuiWindow.FONT_TEXT_COLOR_DARK = MainGuiWindow.FontTextColorDarkVar1
        MainGuiWindow.OPACITY_TEXT_LIGHT = MainGuiWindow.OpacityTextLightVar1
        MainGuiWindow.OPACITY_TEXT_DARK = MainGuiWindow.OpacityTextDarkVar1
        MainGuiWindow.DIRECTION_TEXT = MainGuiWindow.DirectionTextVar1
        MainGuiWindow.PARAGRAPH_TEXT_LIGHT = MainGuiWindow.ParagraphTextLightVar1
        MainGuiWindow.PARAGRAPH_TEXT_DARK = MainGuiWindow.ParagraphTextDarkVar1
        MainGuiWindow.DOCKING = MainGuiWindow.DockingVar1
        MainGuiWindow.FLAG_TOOLBAR = MainGuiWindow.FlagToolbarVar1
        MainGuiWindow.FLAG_FORMATBAR = MainGuiWindow.FlagFormatbarVar1
        MainGuiWindow.FLAG_STATUSBAR = MainGuiWindow.FlagStatusbarVar1

    # //===========================================//
    def decode_Setting(self):
        """
        Decodes various application settings from encoded values.
        This function is responsible for converting encoded configuration values
        into their respective decoded formats for use in the application.
        """

        # Declare global variables for settings (encoded and decoded)
        global FontTextFamilyLightVar1InitEnc, FontTextFamilyLightVar1Init, FontTextFamilyDarkVar1InitEnc, FontTextFamilyDarkVar1Init
        global FontTextColorLightVar1Init, FontTextColorLightVar1InitEnc, FontTextColorDarkVar1Init, FontTextColorDarkVar1InitEnc
        global FontTextSizeLightVar1InitEnc, FontTextSizeLightVar1Init, FontTextSizeDarkVar1InitEnc, FontTextSizeDarkVar1Init, DockingVar1InitEnc, DockingVar1Init
        global ThemeVar1InitEnc, OpacityTextLightVar1InitEnc, OpacityTextDarkVar1InitEnc, DirectionTextVar1InitEnc, ParagraphTextLightVar1InitEnc, ParagraphTextDarkVar1InitEnc
        global ThemeVar1Init, OpacityTextLightVar1Init, OpacityTextDarkVar1Init, DirectionTextVar1Init, ParagraphTextLightVar1Init, ParagraphTextDarkVar1Init
        global FlagToolbarVar1InitEnc, FlagFormatbarVar1InitEnc, FlagStatusbarVar1InitEnc
        global FlagToolbarVar1Init, FlagFormatbarVar1Init, FlagStatusbarVar1Init
        global LanguageVar1InitEnc, LanguageSystemVar1InitEnc, MathEquationVar1InitEnc, TextLayoutVar1InitEnc
        global LanguageVar1Init, LanguageSystemVar1Init, MathEquationVar1Init, TextLayoutVar1Init
        global RBBColorVar1InitEnc, RBBColorVar1Init
        global ThemeLightColorTBVar1InitEnc,ThemeLightColorFGVar1InitEnc, ThemeLightColorBGVar1InitEnc, ThemeLightColorFontVar1InitEnc, ThemeLightColorBTVar1InitEnc, ThemeLightColorBDVar1InitEnc
        global ThemeLightColorTBVar1Init, ThemeLightColorFGVar1Init, ThemeLightColorBGVar1Init, ThemeLightColorFontVar1Init, ThemeLightColorBTVar1Init, ThemeLightColorBDVar1Init
        global ThemeDarkColorTBVar1InitEnc,ThemeDarkColorFGVar1InitEnc, ThemeDarkColorBGVar1InitEnc, ThemeDarkColorFontVar1InitEnc, ThemeDarkColorBTVar1InitEnc, ThemeDarkColorBDVar1InitEnc
        global ThemeDarkColorTBVar1Init, ThemeDarkColorFGVar1Init, ThemeDarkColorBGVar1Init, ThemeDarkColorFontVar1Init, ThemeDarkColorBTVar1Init, ThemeDarkColorBDVar1Init
        global DetectedTextVar1InitEnc, DetectedTextLetterVar1InitEnc, DetectedTextLowerVar1InitEnc, DetectedTextUpperVar1InitEnc, DetectedTextNumberVar1InitEnc, DetectedTextPuncVar1InitEnc, DetectedTextMiscVar1InitEnc
        global DetectedTextVar1Init, DetectedTextLetterVar1Init, DetectedTextLowerVar1Init, DetectedTextUpperVar1Init, DetectedTextNumberVar1Init, DetectedTextPuncVar1Init, DetectedTextMiscVar1Init
        global OutputFormatVar1InitEnc, OptimizationVar1InitEnc, OutputFormatVar1Init, OptimizationVar1Init
        global PageLayoutAutoRotatePageVar1InitEnc, PageLayoutDeskewVar1InitEnc, PageLayoutDecolumnizeVar1InitEnc, PageLayoutRemoveTableVar1InitEnc
        global PageLayoutRemoveWatermarkVar1InitEnc, PageLayoutRemoveUnderlineVar1InitEnc, PageLayoutRemoveSpaceVar1InitEnc, PageLayoutRemoveLineVar1InitEnc
        global PageLayoutAutoRotatePageVar1Init, PageLayoutDeskewVar1Init, PageLayoutDecolumnizeVar1Init, PageLayoutRemoveTableVar1Init
        global PageLayoutRemoveWatermarkVar1Init, PageLayoutRemoveUnderlineVar1Init, PageLayoutRemoveSpaceVar1Init, PageLayoutRemoveLineVar1Init
        global LayoutDespeckleVar1InitEnc, LayoutThresholdVar1InitEnc, LayoutInvertColorVar1InitEnc, LayoutThresholdAdaptiveVar1InitEnc, LayoutSharpenVar1InitEnc, LayoutContrastVar1InitEnc
        global LayoutDespeckleVar1Init, LayoutThresholdVar1Init, LayoutInvertColorVar1Init, LayoutThresholdAdaptiveVar1Init, LayoutSharpenVar1Init, LayoutContrastVar1Init
        global FilteringBackgroundNoiseVar1InitEnc, FilteringBackgroundNoiseIntVar1InitEnc, FilteringTextNoiseVar1InitEnc, FilteringTextNoiseIntVar1InitEnc
        global FilteringBackgroundNoiseVar1Init, FilteringBackgroundNoiseIntVar1Init, FilteringTextNoiseVar1Init, FilteringTextNoiseIntVar1Init
        global FilteringTextErosionVar1InitEnc, FilteringTextErosionIntVar1InitEnc, FilteringTextDilationVar1InitEnc, FilteringTextDilationIntVar1InitEnc
        global FilteringTextErosionVar1Init, FilteringTextErosionIntVar1Init, FilteringTextDilationVar1Init, FilteringTextDilationIntVar1Init
        global FilteringThresholdVar1InitEnc, FilteringThresholdLowerIntVar1InitEnc, FilteringThresholdUpperIntVar1InitEnc
        global FilteringThresholdVar1Init, FilteringThresholdLowerIntVar1Init, FilteringThresholdUpperIntVar1Init
        global DisplayColorImageVar1InitEnc, DisplayGrayImageVar1InitEnc, DisplayProcessedImageVar1InitEnc, DisplayProcessedAllImageVar1InitEnc
        global DisplayColorImageVar1Init, DisplayGrayImageVar1Init, DisplayProcessedImageVar1Init, DisplayProcessedAllImageVar1Init
        global WhitelistVar1InitEnc, Whitelist1Var1InitEnc, Whitelist2Var1InitEnc, Whitelist3Var1InitEnc, Whitelist4Var1InitEnc, Whitelist5Var1InitEnc
        global WhitelistVar1Init, Whitelist1Var1Init, Whitelist2Var1Init, Whitelist3Var1Init, Whitelist4Var1Init, Whitelist5Var1Init
        global BlacklistVar1InitEnc, Blacklist1Var1InitEnc, Blacklist2Var1InitEnc, Blacklist3Var1InitEnc, Blacklist4Var1InitEnc, Blacklist5Var1InitEnc
        global BlacklistVar1Init, Blacklist1Var1Init, Blacklist2Var1Init, Blacklist3Var1Init, Blacklist4Var1Init, Blacklist5Var1Init
        global ThemeLightColorVar1InitEnc, ThemeDarkColorVar1InitEnc, CursorShapeVar1InitEnc, RBBThicknessVar1InitEnc, RBBOpacityVar1InitEnc
        global ThemeLightColorVar1Init, ThemeDarkColorVar1Init, CursorShapeVar1Init, RBBThicknessVar1Init, RBBOpacityVar1Init
        global FontSystemSizeVar1InitEnc, BorderStyleVar1InitEnc, TextEditorIconSizeVar1InitEnc, TextEditorStatusBarVar1InitEnc, TextEditorModeVar1InitEnc, SystemTrayIconVar1InitEnc
        global FontSystemSizeVar1Init, BorderStyleVar1Init, TextEditorIconSizeVar1Init, TextEditorStatusBarVar1Init, TextEditorModeVar1Init, SystemTrayIconVar1Init
        global WhitelistCharVar1Init, BlacklistCharVar1Init

        print('=== decode_Setting ===')

        # Decode theme settings
        ThemeVar1InitEnc = ThemeVar1InitEnc.rstrip()
        if (ThemeVar1InitEnc == '1011'):
            ThemeVar1Init = 0  # Light theme
        elif (ThemeVar1InitEnc == '1110'):
            ThemeVar1Init = 1  # Dark theme

        # Decode opacity settings for light theme
        OpacityTextLightVar1InitEnc = OpacityTextLightVar1InitEnc.rstrip()
        if (OpacityTextLightVar1InitEnc == '0011'):
            OpacityTextLightVar1Init = 0.005
        elif (OpacityTextLightVar1InitEnc == '1010'):
            OpacityTextLightVar1Init = 0.2
        elif (OpacityTextLightVar1InitEnc == '1011'):
            OpacityTextLightVar1Init = 0.4
        elif (OpacityTextLightVar1InitEnc == '0110'):
            OpacityTextLightVar1Init = 0.6
        elif (OpacityTextLightVar1InitEnc == '1001'):
            OpacityTextLightVar1Init = 0.8
        elif (OpacityTextLightVar1InitEnc == '0111'):
            OpacityTextLightVar1Init = 1.0

        # Decode opacity settings for dark theme
        OpacityTextDarkVar1InitEnc = OpacityTextDarkVar1InitEnc.rstrip()
        if (OpacityTextDarkVar1InitEnc == '0111'):
            OpacityTextDarkVar1Init = 0.005
        elif (OpacityTextDarkVar1InitEnc == '0100'):
            OpacityTextDarkVar1Init = 0.2
        elif (OpacityTextDarkVar1InitEnc == '1001'):
            OpacityTextDarkVar1Init = 0.4
        elif (OpacityTextDarkVar1InitEnc == '1100'):
            OpacityTextDarkVar1Init = 0.6
        elif (OpacityTextDarkVar1InitEnc == '1011'):
            OpacityTextDarkVar1Init = 0.8
        elif (OpacityTextDarkVar1InitEnc == '0010'):
            OpacityTextDarkVar1Init = 1.0

        # Decode text direction settings
        DirectionTextVar1InitEnc = DirectionTextVar1InitEnc.rstrip()
        if (DirectionTextVar1InitEnc == '0101'):
            DirectionTextVar1Init = 0  # Left-to-right
        elif (DirectionTextVar1InitEnc == '1010'):
            DirectionTextVar1Init = 1  # Right-to-left

        # Decode paragraph settings for light theme
        ParagraphTextLightVar1InitEnc = ParagraphTextLightVar1InitEnc.rstrip()
        if (ParagraphTextLightVar1InitEnc == '1011'):
            ParagraphTextLightVar1Init = 0  # Disabled
        elif (ParagraphTextLightVar1InitEnc == '1010'):
            ParagraphTextLightVar1Init = 1  # Enabled

        # Decode paragraph settings for dark theme
        ParagraphTextDarkVar1InitEnc = ParagraphTextDarkVar1InitEnc.rstrip()
        if (ParagraphTextDarkVar1InitEnc == '0110'):
            ParagraphTextDarkVar1Init = 0  # Disabled
        elif (ParagraphTextDarkVar1InitEnc == '1010'):
            ParagraphTextDarkVar1Init = 1  # Enabled

        # Decode docking settings
        DockingVar1InitEnc = DockingVar1InitEnc.replace('\n','')
        DockingVar1Init = ''
        DockingVar1Init = format(hex(int(DockingVar1InitEnc,2)))[2]
        DockingVar1Init = DockingVar1Init

        # Decode toolbar flag
        FlagToolbarVar1InitEnc = FlagToolbarVar1InitEnc.rstrip()
        if (FlagToolbarVar1InitEnc == '1101'):
            FlagToolbarVar1Init = 0  # Disabled
        elif (FlagToolbarVar1InitEnc == '1010'):
            FlagToolbarVar1Init = 1  # Enabled

        # Decode format bar flag
        FlagFormatbarVar1InitEnc = FlagFormatbarVar1InitEnc.rstrip()
        if (FlagFormatbarVar1InitEnc == '0101'):
            FlagFormatbarVar1Init = 0  # Disabled
        elif (FlagFormatbarVar1InitEnc == '1110'):
            FlagFormatbarVar1Init = 1  # Enabled

        # Decode status bar flag
        FlagStatusbarVar1InitEnc = FlagStatusbarVar1InitEnc.rstrip()
        if (FlagStatusbarVar1InitEnc == '1011'):
            FlagStatusbarVar1Init = 0  # Disabled
        elif (FlagStatusbarVar1InitEnc == '1100'):
            FlagStatusbarVar1Init = 1  # Enabled

        # # Decode font size for light theme
        # FontTextSizeLightVar1InitEnc = FontTextSizeLightVar1InitEnc.replace('\n', '')
        # FontTextSizeLightVar1InitEnc = [FontTextSizeLightVar1InitEnc[i:i + 4] for i in range(0, len(FontTextSizeLightVar1InitEnc), 4)]
        # FontTextSizeLightVar1Init = ''.join([format(hex(int(chunk, 2)))[2] for chunk in FontTextSizeLightVar1InitEnc])

        # Decode font size for light theme
        FontTextSizeLightVar1InitEnc = FontTextSizeLightVar1InitEnc.replace('\n','')
        FontTextSizeLightVar1InitEnc = [FontTextSizeLightVar1InitEnc[i:i+4] for i in range(0,len(FontTextSizeLightVar1InitEnc),4)]
        FontTextSizeLightVar1Init = ''
        for i in range(len(FontTextSizeLightVar1InitEnc)):
            FontTextSizeLightVar1Init = FontTextSizeLightVar1Init + format(hex(int(FontTextSizeLightVar1InitEnc[i],2)))[2]
        FontTextSizeLightVar1Init = FontTextSizeLightVar1Init

        # Decode font size for dark theme
        FontTextSizeDarkVar1InitEnc = FontTextSizeDarkVar1InitEnc.replace('\n','')
        FontTextSizeDarkVar1InitEnc = [FontTextSizeDarkVar1InitEnc[i:i+4] for i in range(0,len(FontTextSizeDarkVar1InitEnc),4)]
        FontTextSizeDarkVar1Init = ''
        for i in range(len(FontTextSizeDarkVar1InitEnc)):
            FontTextSizeDarkVar1Init = FontTextSizeDarkVar1Init + format(hex(int(FontTextSizeDarkVar1InitEnc[i],2)))[2]
        FontTextSizeDarkVar1Init = FontTextSizeDarkVar1Init

        # Decode font color for light theme
        FontTextColorLightVar1InitEnc = FontTextColorLightVar1InitEnc.replace('\n','')
        FontTextColorLightVar1InitEnc = [FontTextColorLightVar1InitEnc[i:i+4] for i in range(0,len(FontTextColorLightVar1InitEnc),4)]
        FontTextColorLightVar1Init = ''
        for i in range(len(FontTextColorLightVar1InitEnc)):
            FontTextColorLightVar1Init = FontTextColorLightVar1Init + format(hex(int(FontTextColorLightVar1InitEnc[i],2)))[2]
        FontTextColorLightVar1Init = '#'+FontTextColorLightVar1Init

        # Decode font color for dark theme
        FontTextColorDarkVar1InitEnc = FontTextColorDarkVar1InitEnc.replace('\n','')
        FontTextColorDarkVar1InitEnc = [FontTextColorDarkVar1InitEnc[i:i+4] for i in range(0,len(FontTextColorDarkVar1InitEnc),4)]
        FontTextColorDarkVar1Init = ''
        for i in range(len(FontTextColorDarkVar1InitEnc)):
            FontTextColorDarkVar1Init = FontTextColorDarkVar1Init + format(hex(int(FontTextColorDarkVar1InitEnc[i],2)))[2]
        FontTextColorDarkVar1Init = '#'+FontTextColorDarkVar1Init

        # Decode font family for light theme
        FontTextFamilyLightVar1InitEnc = FontTextFamilyLightVar1InitEnc.replace('\n','')
        FontTextFamilyLightVar1InitEnc = FontTextFamilyLightVar1InitEnc.replace(' ','')
        FontTextFamilyLightVar1InitEnc = [FontTextFamilyLightVar1InitEnc[i:i+8] for i in range(0,len(FontTextFamilyLightVar1InitEnc),8)]
        FontTextFamilyLightVar1Init = ''
        for i in range(len(FontTextFamilyLightVar1InitEnc)):
            FontTextFamilyLightVar1Init = FontTextFamilyLightVar1Init + chr(int(FontTextFamilyLightVar1InitEnc[i],2)-96)

        # Decode font family for dark theme
        FontTextFamilyDarkVar1InitEnc = FontTextFamilyDarkVar1InitEnc.replace('\n','')
        FontTextFamilyDarkVar1InitEnc = FontTextFamilyDarkVar1InitEnc.replace(' ','')
        FontTextFamilyDarkVar1InitEnc = [FontTextFamilyDarkVar1InitEnc[i:i+8] for i in range(0,len(FontTextFamilyDarkVar1InitEnc),8)]
        FontTextFamilyDarkVar1Init = ''
        for i in range(len(FontTextFamilyDarkVar1InitEnc)):
            FontTextFamilyDarkVar1Init = FontTextFamilyDarkVar1Init + chr(int(FontTextFamilyDarkVar1InitEnc[i],2)-96)

        # Decode language system settings
        LanguageSystemVar1InitEnc = LanguageSystemVar1InitEnc.rstrip()
        if (LanguageSystemVar1InitEnc == '10010'):
            LanguageSystemVar1Init = 0  # Default language
        elif (LanguageSystemVar1InitEnc == '10110'):
            LanguageSystemVar1Init = 1  # System language

        # Decode math equation settings
        MathEquationVar1InitEnc = MathEquationVar1InitEnc.rstrip()
        if (MathEquationVar1InitEnc == '01011'):
            MathEquationVar1Init = 0  # Disabled
        elif (MathEquationVar1InitEnc == '11100'):
            MathEquationVar1Init = 1  # Enabled

        # Decode text layout settings
        TextLayoutVar1InitEnc = TextLayoutVar1InitEnc.rstrip()
        if (TextLayoutVar1InitEnc == '01001'):
            TextLayoutVar1Init = 0  # Auto
        elif (TextLayoutVar1InitEnc == '01101'):
            TextLayoutVar1Init = 1  # Single Character
        elif (TextLayoutVar1InitEnc == '00110'):
            TextLayoutVar1Init = 2  # Single Word
        elif (TextLayoutVar1InitEnc == '10101'):
            TextLayoutVar1Init = 3  # Single Line
        elif (TextLayoutVar1InitEnc == '11000'):
            TextLayoutVar1Init = 4  # Sparse Text
        elif (TextLayoutVar1InitEnc == '11001'):
            TextLayoutVar1Init = 5  # Vertical Text
        elif (TextLayoutVar1InitEnc == '10010'):
            TextLayoutVar1Init = 6  # Single Column
        elif (TextLayoutVar1InitEnc == '00011'):
            TextLayoutVar1Init = 7  # Multiple Columns

        # Decode the detected text variable from its encoded value
        DetectedTextVar1InitEnc = DetectedTextVar1InitEnc.rstrip()
        if (DetectedTextVar1InitEnc == '11011'):
            DetectedTextVar1Init = 0  # No detected
        elif (DetectedTextVar1InitEnc == '00101'):
            DetectedTextVar1Init = 1  # Detected

        # Decode the detected text letter variable (e.g., letters a-z or A-Z)
        DetectedTextLetterVar1InitEnc = DetectedTextLetterVar1InitEnc.rstrip()
        if (DetectedTextLetterVar1InitEnc == '00110'):
            DetectedTextLetterVar1Init = 0  # No detected
        elif (DetectedTextLetterVar1InitEnc == '00101'):
            DetectedTextLetterVar1Init = 1  # Detected

        # Decode the detected lowercase text variable
        DetectedTextLowerVar1InitEnc = DetectedTextLowerVar1InitEnc.rstrip()
        if (DetectedTextLowerVar1InitEnc == '10100'):
            DetectedTextLowerVar1Init = 0  # No detected
        elif (DetectedTextLowerVar1InitEnc == '11001'):
            DetectedTextLowerVar1Init = 1  # Detected

        # Decode the detected uppercase text variable
        DetectedTextUpperVar1InitEnc = DetectedTextUpperVar1InitEnc.rstrip()
        if (DetectedTextUpperVar1InitEnc == '11101'):
            DetectedTextUpperVar1Init = 0  # No detected
        elif (DetectedTextUpperVar1InitEnc == '01001'):
            DetectedTextUpperVar1Init = 1  # Detected

        # Decode the detected numeric text variable
        DetectedTextNumberVar1InitEnc = DetectedTextNumberVar1InitEnc.rstrip()
        if (DetectedTextNumberVar1InitEnc == '01100'):
            DetectedTextNumberVar1Init = 0  # No detected
        elif (DetectedTextNumberVar1InitEnc == '10110'):
            DetectedTextNumberVar1Init = 1  # Detected

        # Decode the detected punctuation variable
        DetectedTextPuncVar1InitEnc = DetectedTextPuncVar1InitEnc.rstrip()
        if (DetectedTextPuncVar1InitEnc == '11011'):
            DetectedTextPuncVar1Init = 0  # No detected
        elif (DetectedTextPuncVar1InitEnc == '10110'):
            DetectedTextPuncVar1Init = 1  # Detected

        # Decode the detected miscellaneous text variable (e.g., special characters)
        DetectedTextMiscVar1InitEnc = DetectedTextMiscVar1InitEnc.rstrip()
        if (DetectedTextMiscVar1InitEnc == '01100'):
            DetectedTextMiscVar1Init = 0  # No detected
        elif (DetectedTextMiscVar1InitEnc == '01001'):
            DetectedTextMiscVar1Init = 1  # Detected

        # Decode the output format variable (e.g., text, PDF, or other formats)
        OutputFormatVar1InitEnc = OutputFormatVar1InitEnc.rstrip()
        if (OutputFormatVar1InitEnc == '11101'):
            OutputFormatVar1Init = 0  # Text format
        elif (OutputFormatVar1InitEnc == '11010'):
            OutputFormatVar1Init = 1  # PDF format
        elif (OutputFormatVar1InitEnc == '10111'):
            OutputFormatVar1Init = 2  # Other format

        # Decode the optimization variable (e.g., standard, speed, or accuracy)
        OptimizationVar1InitEnc = OptimizationVar1InitEnc.rstrip()
        if (OptimizationVar1InitEnc == '01001'):
            OptimizationVar1Init = 0  # Standard optimization
        elif (OptimizationVar1InitEnc == '01110'):
            OptimizationVar1Init = 1  # Speed optimization
        elif (OptimizationVar1InitEnc == '01010'):
            OptimizationVar1Init = 2  # Accuracy optimization

        # Decode the auto-rotate page layout variable
        PageLayoutAutoRotatePageVar1InitEnc = PageLayoutAutoRotatePageVar1InitEnc.rstrip()
        if (PageLayoutAutoRotatePageVar1InitEnc == '01011'):
            PageLayoutAutoRotatePageVar1Init = 0  # Disabled
        elif (PageLayoutAutoRotatePageVar1InitEnc == '10110'):
            PageLayoutAutoRotatePageVar1Init = 1  # Enabled

        # Decode the deskew page layout variable
        PageLayoutDeskewVar1InitEnc = PageLayoutDeskewVar1InitEnc.rstrip()
        if (PageLayoutDeskewVar1InitEnc == '10010'):
            PageLayoutDeskewVar1Init = 0  # Disabled
        elif (PageLayoutDeskewVar1InitEnc == '11011'):
            PageLayoutDeskewVar1Init = 1  # Enabled

        # Decode the decolumnize page layout variable
        PageLayoutDecolumnizeVar1InitEnc = PageLayoutDecolumnizeVar1InitEnc.rstrip()
        if (PageLayoutDecolumnizeVar1InitEnc == '11001'):
            PageLayoutDecolumnizeVar1Init = 0  # Disabled
        elif (PageLayoutDecolumnizeVar1InitEnc == '01011'):
            PageLayoutDecolumnizeVar1Init = 1  # Enabled

        # Decode the remove table page layout variable
        PageLayoutRemoveTableVar1InitEnc = PageLayoutRemoveTableVar1InitEnc.rstrip()
        if (PageLayoutRemoveTableVar1InitEnc == '01100'):
            PageLayoutRemoveTableVar1Init = 0  # Disabled
        elif (PageLayoutRemoveTableVar1InitEnc == '01010'):
            PageLayoutRemoveTableVar1Init = 1  # Enabled

        # Decode the remove watermark page layout variable
        PageLayoutRemoveWatermarkVar1InitEnc = PageLayoutRemoveWatermarkVar1InitEnc.rstrip()
        if (PageLayoutRemoveWatermarkVar1InitEnc == '11011'):
            PageLayoutRemoveWatermarkVar1Init = 0  # Disabled
        elif (PageLayoutRemoveWatermarkVar1InitEnc == '10110'):
            PageLayoutRemoveWatermarkVar1Init = 1  # Enabled

        # Decode the remove underline page layout variable
        PageLayoutRemoveUnderlineVar1InitEnc = PageLayoutRemoveUnderlineVar1InitEnc.rstrip()
        if (PageLayoutRemoveUnderlineVar1InitEnc == '01011'):
            PageLayoutRemoveUnderlineVar1Init = 0  # Disabled
        elif (PageLayoutRemoveUnderlineVar1InitEnc == '10011'):
            PageLayoutRemoveUnderlineVar1Init = 1  # Enabled

        # Decode the remove space page layout variable
        PageLayoutRemoveSpaceVar1InitEnc = PageLayoutRemoveSpaceVar1InitEnc.rstrip()
        if (PageLayoutRemoveSpaceVar1InitEnc == '11011'):
            PageLayoutRemoveSpaceVar1Init = 0  # Disabled
        elif (PageLayoutRemoveSpaceVar1InitEnc == '11010'):
            PageLayoutRemoveSpaceVar1Init = 1  # Enabled

        # Decode the remove line page layout variable
        PageLayoutRemoveLineVar1InitEnc = PageLayoutRemoveLineVar1InitEnc.rstrip()
        if (PageLayoutRemoveLineVar1InitEnc == '11001'):
            PageLayoutRemoveLineVar1Init = 0  # Disabled
        elif (PageLayoutRemoveLineVar1InitEnc == '01110'):
            PageLayoutRemoveLineVar1Init = 1  # Enabled

        # Decode the remove line page layout variable
        LayoutDespeckleVar1InitEnc = LayoutDespeckleVar1InitEnc.rstrip()
        if (LayoutDespeckleVar1InitEnc == '00100'):
            LayoutDespeckleVar1Init = 0  # Disabled
        elif (LayoutDespeckleVar1InitEnc == '11010'):
            LayoutDespeckleVar1Init = 1  # Enabled

        # Decode the remove line page layout variable
        LayoutThresholdVar1InitEnc = LayoutThresholdVar1InitEnc.rstrip()
        if (LayoutThresholdVar1InitEnc == '01010'):
            LayoutThresholdVar1Init = 0  # Disabled
        elif (LayoutThresholdVar1InitEnc == '01110'):
            LayoutThresholdVar1Init = 1  # Enabled

        # Decode the remove line page layout variable
        LayoutInvertColorVar1InitEnc = LayoutInvertColorVar1InitEnc.rstrip()
        if (LayoutInvertColorVar1InitEnc == '10100'):
            LayoutInvertColorVar1Init = 0  # Disabled
        elif (LayoutInvertColorVar1InitEnc == '11101'):
            LayoutInvertColorVar1Init = 1  # Enabled

        # Decode the remove line page layout variable
        LayoutThresholdAdaptiveVar1InitEnc = LayoutThresholdAdaptiveVar1InitEnc.rstrip()
        if (LayoutThresholdAdaptiveVar1InitEnc == '11001'):
            LayoutThresholdAdaptiveVar1Init = 0  # Disabled
        elif (LayoutThresholdAdaptiveVar1InitEnc == '01101'):
            LayoutThresholdAdaptiveVar1Init = 1  # Enabled

        # Decode sharpen layout variable
        LayoutSharpenVar1InitEnc = LayoutSharpenVar1InitEnc.rstrip()
        if (LayoutSharpenVar1InitEnc == '01010'):
            LayoutSharpenVar1Init = 0  # Disabled
        elif (LayoutSharpenVar1InitEnc == '11001'):
            LayoutSharpenVar1Init = 1  # Enabled

        # Decode contrast layout variable
        LayoutContrastVar1InitEnc = LayoutContrastVar1InitEnc.rstrip()
        if (LayoutContrastVar1InitEnc == '00110'):
            LayoutContrastVar1Init = 0  # Disabled
        elif (LayoutContrastVar1InitEnc == '11101'):
            LayoutContrastVar1Init = 1  # Enabled

        # Decode background noise filtering variable
        FilteringBackgroundNoiseVar1InitEnc = FilteringBackgroundNoiseVar1InitEnc.rstrip()
        if (FilteringBackgroundNoiseVar1InitEnc == '11011'):
            FilteringBackgroundNoiseVar1Init = 0  # Disabled
        elif (FilteringBackgroundNoiseVar1InitEnc == '10110'):
            FilteringBackgroundNoiseVar1Init = 1  # Enabled

        # Decode background noise intensity variable
        FilteringBackgroundNoiseIntVar1InitEnc = FilteringBackgroundNoiseIntVar1InitEnc.rstrip()
        if (FilteringBackgroundNoiseIntVar1InitEnc == '01101'):
            FilteringBackgroundNoiseIntVar1Init = 3  # Low intensity
        elif (FilteringBackgroundNoiseIntVar1InitEnc == '01110'):
            FilteringBackgroundNoiseIntVar1Init = 7  # Medium intensity
        elif (FilteringBackgroundNoiseIntVar1InitEnc == '11100'):
            FilteringBackgroundNoiseIntVar1Init = 11  # High intensity
        elif (FilteringBackgroundNoiseIntVar1InitEnc == '11001'):
            FilteringBackgroundNoiseIntVar1Init = 15  # Very high intensity
        elif (FilteringBackgroundNoiseIntVar1InitEnc == '01100'):
            FilteringBackgroundNoiseIntVar1Init = 19  # Maximum intensity

        # Decode text noise filtering variable
        FilteringTextNoiseVar1InitEnc = FilteringTextNoiseVar1InitEnc.rstrip()
        if (FilteringTextNoiseVar1InitEnc == '11100'):
            FilteringTextNoiseVar1Init = 0  # Disabled
        elif (FilteringTextNoiseVar1InitEnc == '01101'):
            FilteringTextNoiseVar1Init = 1  # Enabled

        # Decode text noise intensity variable
        FilteringTextNoiseIntVar1InitEnc = FilteringTextNoiseIntVar1InitEnc.rstrip()
        if (FilteringTextNoiseIntVar1InitEnc == '11001'):
            FilteringTextNoiseIntVar1Init = 2  # Low intensity
        elif (FilteringTextNoiseIntVar1InitEnc == '01101'):
            FilteringTextNoiseIntVar1Init = 3  # Medium intensity
        elif (FilteringTextNoiseIntVar1InitEnc == '11100'):
            FilteringTextNoiseIntVar1Init = 4  # High intensity
        elif (FilteringTextNoiseIntVar1InitEnc == '01110'):
            FilteringTextNoiseIntVar1Init = 5  # Very high intensity
        elif (FilteringTextNoiseIntVar1InitEnc == '10111'):
            FilteringTextNoiseIntVar1Init = 6  # Maximum intensity

        # Decode text erosion filtering variable
        FilteringTextErosionVar1InitEnc = FilteringTextErosionVar1InitEnc.rstrip()
        if (FilteringTextErosionVar1InitEnc == '01101'):
            FilteringTextErosionVar1Init = 0  # Disabled
        elif (FilteringTextErosionVar1InitEnc == '10110'):
            FilteringTextErosionVar1Init = 1  # Enabled

        # Decode text erosion intensity variable
        FilteringTextErosionIntVar1InitEnc = FilteringTextErosionIntVar1InitEnc.rstrip()
        if (FilteringTextErosionIntVar1InitEnc == '10100'):
            FilteringTextErosionIntVar1Init = 2  # Low intensity
        elif (FilteringTextErosionIntVar1InitEnc == '11011'):
            FilteringTextErosionIntVar1Init = 3  # Medium intensity
        elif (FilteringTextErosionIntVar1InitEnc == '01110'):
            FilteringTextErosionIntVar1Init = 4  # High intensity
        elif (FilteringTextErosionIntVar1InitEnc == '01101'):
            FilteringTextErosionIntVar1Init = 5  # Very high intensity
        elif (FilteringTextErosionIntVar1InitEnc == '10111'):
            FilteringTextErosionIntVar1Init = 6  # Maximum intensity

        # Decode text dilation filtering variable
        FilteringTextDilationVar1InitEnc = FilteringTextDilationVar1InitEnc.rstrip()
        if (FilteringTextDilationVar1InitEnc == '10110'):
            FilteringTextDilationVar1Init = 0  # Disabled
        elif (FilteringTextDilationVar1InitEnc == '10011'):
            FilteringTextDilationVar1Init = 1  # Enabled

        # Decode text dilation intensity variable
        FilteringTextDilationIntVar1InitEnc = FilteringTextDilationIntVar1InitEnc.rstrip()
        if (FilteringTextDilationIntVar1InitEnc == '10010'):
            FilteringTextDilationIntVar1Init = 2  # Low intensity
        elif (FilteringTextDilationIntVar1InitEnc == '00100'):
            FilteringTextDilationIntVar1Init = 3  # Medium intensity
        elif (FilteringTextDilationIntVar1InitEnc == '10111'):
            FilteringTextDilationIntVar1Init = 4  # High intensity
        elif (FilteringTextDilationIntVar1InitEnc == '01100'):
            FilteringTextDilationIntVar1Init = 5  # Very high intensity
        elif (FilteringTextDilationIntVar1InitEnc == '01110'):
            FilteringTextDilationIntVar1Init = 6  # Maximum intensity

        # Decode threshold filtering variable
        FilteringThresholdVar1InitEnc = FilteringThresholdVar1InitEnc.rstrip()
        if (FilteringThresholdVar1InitEnc == '01010'):
            FilteringThresholdVar1Init = 0  # Disabled
        elif (FilteringThresholdVar1InitEnc == '10100'):
            FilteringThresholdVar1Init = 1  # Enabled

        # Decode display color image variable
        DisplayColorImageVar1InitEnc = DisplayColorImageVar1InitEnc.rstrip()
        if (DisplayColorImageVar1InitEnc == '11001'):
            DisplayColorImageVar1Init = 0  # Disabled
        elif (DisplayColorImageVar1InitEnc == '10100'):
            DisplayColorImageVar1Init = 1  # Enabled

        # Decode display grayscale image variable
        DisplayGrayImageVar1InitEnc = DisplayGrayImageVar1InitEnc.rstrip()
        if (DisplayGrayImageVar1InitEnc == '10110'):
            DisplayGrayImageVar1Init = 0  # Disabled
        elif (DisplayGrayImageVar1InitEnc == '11100'):
            DisplayGrayImageVar1Init = 1  # Enabled

        # Decode display processed image variable
        DisplayProcessedImageVar1InitEnc = DisplayProcessedImageVar1InitEnc.rstrip()
        if (DisplayProcessedImageVar1InitEnc == '01010'):
            DisplayProcessedImageVar1Init = 0  # Disabled
        elif (DisplayProcessedImageVar1InitEnc == '00111'):
            DisplayProcessedImageVar1Init = 1  # Enabled

        # Decode display all processed images variable
        DisplayProcessedAllImageVar1InitEnc = DisplayProcessedAllImageVar1InitEnc.rstrip()
        if (DisplayProcessedAllImageVar1InitEnc == '10100'):
            DisplayProcessedAllImageVar1Init = 0  # Disabled
        elif (DisplayProcessedAllImageVar1InitEnc == '01011'):
            DisplayProcessedAllImageVar1Init = 1  # Enabled

        # Decode whitelist variable
        WhitelistVar1InitEnc = WhitelistVar1InitEnc.rstrip()
        if (WhitelistVar1InitEnc == '11100'):
            WhitelistVar1Init = 0  # Disabled
        elif (WhitelistVar1InitEnc == '10100'):
            WhitelistVar1Init = 1  # Enabled

        # Decode first whitelist variable
        Whitelist1Var1InitEnc = Whitelist1Var1InitEnc.rstrip()
        if (Whitelist1Var1InitEnc == '01110'):
            Whitelist1Var1Init = 0  # Disabled
        elif (Whitelist1Var1InitEnc == '01101'):
            Whitelist1Var1Init = 1  # Enabled

        # Decode second whitelist variable
        Whitelist2Var1InitEnc = Whitelist2Var1InitEnc.rstrip()
        if (Whitelist2Var1InitEnc == '01101'):
            Whitelist2Var1Init = 0  # Disabled
        elif (Whitelist2Var1InitEnc == '01110'):
            Whitelist2Var1Init = 1  # Enabled

        # Decode third whitelist variable
        Whitelist3Var1InitEnc = Whitelist3Var1InitEnc.rstrip()
        if (Whitelist3Var1InitEnc == '11010'):
            Whitelist3Var1Init = 0  # Disabled
        elif (Whitelist3Var1InitEnc == '10111'):
            Whitelist3Var1Init = 1  # Enabled

        # Decode fourth whitelist variable
        Whitelist4Var1InitEnc = Whitelist4Var1InitEnc.rstrip()
        if (Whitelist4Var1InitEnc == '10100'):
            Whitelist4Var1Init = 0  # Disabled
        elif (Whitelist4Var1InitEnc == '01110'):
            Whitelist4Var1Init = 1  # Enabled

        # Decode fifth whitelist variable
        Whitelist5Var1InitEnc = Whitelist5Var1InitEnc.rstrip()
        if (Whitelist5Var1InitEnc == '10110'):
            Whitelist5Var1Init = 0  # Disabled
        elif (Whitelist5Var1InitEnc == '01011'):
            Whitelist5Var1Init = 1  # Enabled

        # Decode blacklist variable
        BlacklistVar1InitEnc = BlacklistVar1InitEnc.rstrip()
        if (BlacklistVar1InitEnc == '11001'):
            BlacklistVar1Init = 0  # Disabled
        elif (BlacklistVar1InitEnc == '01001'):
            BlacklistVar1Init = 1  # Enabled

        # Decode first blacklist variable
        Blacklist1Var1InitEnc = Blacklist1Var1InitEnc.rstrip()
        if (Blacklist1Var1InitEnc == '01110'):
            Blacklist1Var1Init = 0  # Disabled
        elif (Blacklist1Var1InitEnc == '11011'):
            Blacklist1Var1Init = 1  # Enabled

        # Decode second blacklist variable
        Blacklist2Var1InitEnc = Blacklist2Var1InitEnc.rstrip()
        if (Blacklist2Var1InitEnc == '11011'):
            Blacklist2Var1Init = 0  # Disabled
        elif (Blacklist2Var1InitEnc == '11011'):
            Blacklist2Var1Init = 1  # Enabled

        # Decode third blacklist variable
        Blacklist3Var1InitEnc = Blacklist3Var1InitEnc.rstrip()
        if (Blacklist3Var1InitEnc == '01101'):
            Blacklist3Var1Init = 0  # Disabled
        elif (Blacklist3Var1InitEnc == '10110'):
            Blacklist3Var1Init = 1  # Enabled

        # Decode fourth blacklist variable
        Blacklist4Var1InitEnc = Blacklist4Var1InitEnc.rstrip()
        if (Blacklist4Var1InitEnc == '10100'):
            Blacklist4Var1Init = 0  # Disabled
        elif (Blacklist4Var1InitEnc == '11101'):
            Blacklist4Var1Init = 1  # Enabled

        # Decode fifth blacklist variable
        Blacklist5Var1InitEnc = Blacklist5Var1InitEnc.rstrip()
        if (Blacklist5Var1InitEnc == '10100'):
            Blacklist5Var1Init = 0  # Disabled
        elif (Blacklist5Var1InitEnc == '10101'):
            Blacklist5Var1Init = 1  # Enabled

        # Decode theme light color variable
        ThemeLightColorVar1InitEnc = ThemeLightColorVar1InitEnc.rstrip()
        if (ThemeLightColorVar1InitEnc == '10100'):
            ThemeLightColorVar1Init = 0  # Default light theme
        elif (ThemeLightColorVar1InitEnc == '01011'):
            ThemeLightColorVar1Init = 1  # Yellow light theme
        elif (ThemeLightColorVar1InitEnc == '01101'):
            ThemeLightColorVar1Init = 2  # Green light theme
        elif (ThemeLightColorVar1InitEnc == '11010'):
            ThemeLightColorVar1Init = 3  # Blue light theme
        elif (ThemeLightColorVar1InitEnc == '11001'):
            ThemeLightColorVar1Init = 4  # Pink light theme
        elif (ThemeLightColorVar1InitEnc == '10011'):
            ThemeLightColorVar1Init = 5  # Orange light theme
        elif (ThemeLightColorVar1InitEnc == '01101'):
            ThemeLightColorVar1Init = 6  # Custom light theme

        # Decode theme dark color variable
        ThemeDarkColorVar1InitEnc = ThemeDarkColorVar1InitEnc.rstrip()
        if (ThemeDarkColorVar1InitEnc == '10011'):
            ThemeDarkColorVar1Init = 0  # Default dark theme
        elif (ThemeDarkColorVar1InitEnc == '11001'):
            ThemeDarkColorVar1Init = 1  # Yellow dark theme
        elif (ThemeDarkColorVar1InitEnc == '11100'):
            ThemeDarkColorVar1Init = 2  # Green dark theme
        elif (ThemeDarkColorVar1InitEnc == '01011'):
            ThemeDarkColorVar1Init = 3  # Blue dark theme
        elif (ThemeDarkColorVar1InitEnc == '00110'):
            ThemeDarkColorVar1Init = 4  # Pink dark theme
        elif (ThemeDarkColorVar1InitEnc == '11011'):
            ThemeDarkColorVar1Init = 5  # Orange dark theme
        elif (ThemeDarkColorVar1InitEnc == '01001'):
            ThemeDarkColorVar1Init = 6  # Custom dark theme

        # Decode cursor shape variable
        CursorShapeVar1InitEnc = CursorShapeVar1InitEnc.rstrip()
        if (CursorShapeVar1InitEnc == '11001'):
            CursorShapeVar1Init = 0  # Cross cursor
        elif (CursorShapeVar1InitEnc == '10110'):
            CursorShapeVar1Init = 1  # Arrow cursor
        elif (CursorShapeVar1InitEnc == '01101'):
            CursorShapeVar1Init = 2  # Target cursor
        elif (CursorShapeVar1InitEnc == '01110'):
            CursorShapeVar1Init = 3  # Pointer cursor
        elif (CursorShapeVar1InitEnc == '10011'):
            CursorShapeVar1Init = 4  # Hand cursor

        # Decode rubber band thickness variable
        RBBThicknessVar1InitEnc = RBBThicknessVar1InitEnc.rstrip()
        if (RBBThicknessVar1InitEnc == '11100'):
            RBBThicknessVar1Init = 0  # Thin rubber band
        elif (RBBThicknessVar1InitEnc == '10100'):
            RBBThicknessVar1Init = 2  # Medium rubber band
        elif (RBBThicknessVar1InitEnc == '10101'):
            RBBThicknessVar1Init = 6  # Thick rubber band
        elif (RBBThicknessVar1InitEnc == '01111'):
            RBBThicknessVar1Init = 8  # Very thick rubber band
        elif (RBBThicknessVar1InitEnc == '10111'):
            RBBThicknessVar1Init = 12  # Maximum thickness

        # Decode rubber band opacity variable
        RBBOpacityVar1InitEnc = RBBOpacityVar1InitEnc.rstrip()
        if (RBBOpacityVar1InitEnc == '01110'):
            RBBOpacityVar1Init = 0  # Fully transparent
        elif (RBBOpacityVar1InitEnc == '11100'):
            RBBOpacityVar1Init = 50  # Semi-transparent
        elif (RBBOpacityVar1InitEnc == '01111'):
            RBBOpacityVar1Init = 100  # Medium opacity
        elif (RBBOpacityVar1InitEnc == '11001'):
            RBBOpacityVar1Init = 150  # High opacity
        elif (RBBOpacityVar1InitEnc == '11101'):
            RBBOpacityVar1Init = 200  # Fully opaque

        # Decode font system size variable
        FontSystemSizeVar1InitEnc = FontSystemSizeVar1InitEnc.rstrip()
        if (FontSystemSizeVar1InitEnc == '00111'):
            FontSystemSizeVar1Init = 7  # Small font size
        elif (FontSystemSizeVar1InitEnc == '11001'):
            FontSystemSizeVar1Init = 8  # Medium font size
        elif (FontSystemSizeVar1InitEnc == '01101'):
            FontSystemSizeVar1Init = 9  # Large font size

        # Decode border style variable
        BorderStyleVar1InitEnc = BorderStyleVar1InitEnc.rstrip()
        if (BorderStyleVar1InitEnc == '11011'):
            BorderStyleVar1Init = 0  # No border
        elif (BorderStyleVar1InitEnc == '01100'):
            BorderStyleVar1Init = 1  # Solid border

        # Decode text editor icon size variable
        TextEditorIconSizeVar1InitEnc = TextEditorIconSizeVar1InitEnc.rstrip()
        if (TextEditorIconSizeVar1InitEnc == '10110'):
            TextEditorIconSizeVar1Init = 16  # Small icons
        elif (TextEditorIconSizeVar1InitEnc == '11000'):
            TextEditorIconSizeVar1Init = 18  # Medium icons
        elif (TextEditorIconSizeVar1InitEnc == '11111'):
            TextEditorIconSizeVar1Init = 22  # Large icons

        # Decode text editor status bar variable
        TextEditorStatusBarVar1InitEnc = TextEditorStatusBarVar1InitEnc.rstrip()
        if (TextEditorStatusBarVar1InitEnc == '01110'):
            TextEditorStatusBarVar1Init = 0  # Status bar disabled
        elif (TextEditorStatusBarVar1InitEnc == '00011'):
            TextEditorStatusBarVar1Init = 1  # Status bar enabled

        # Decode text editor mode variable
        TextEditorModeVar1InitEnc = TextEditorModeVar1InitEnc.rstrip()
        if (TextEditorModeVar1InitEnc == '10110'):
            TextEditorModeVar1Init = 0  # Basic mode
        elif (TextEditorModeVar1InitEnc == '11101'):
            TextEditorModeVar1Init = 1  # Advanced mode

        # Decode system tray icon variable
        SystemTrayIconVar1InitEnc = SystemTrayIconVar1InitEnc.rstrip()
        if (SystemTrayIconVar1InitEnc == '01101'):
            SystemTrayIconVar1Init = 0  # System tray icon disabled
        elif (SystemTrayIconVar1InitEnc == '11101'):
            SystemTrayIconVar1Init = 1  # System tray icon enabled


        # # Decode filtering threshold lower intensity variable
        # FilteringThresholdLowerIntVar1InitEnc = FilteringThresholdLowerIntVar1InitEnc.replace('\n', '')
        # FilteringThresholdLowerIntVar1InitEnc = [FilteringThresholdLowerIntVar1InitEnc[i:i+4] for i in range(0, len(FilteringThresholdLowerIntVar1InitEnc), 4)]
        # FilteringThresholdLowerIntVar1Init = ''
        # for i in range(len(FilteringThresholdLowerIntVar1InitEnc)):
        #     FilteringThresholdLowerIntVar1Init = FilteringThresholdLowerIntVar1Init + format(hex(int(FilteringThresholdLowerIntVar1InitEnc[i], 2)))[2]

        # Decode filtering threshold lower intensity variable
        FilteringThresholdLowerIntVar1InitEnc = FilteringThresholdLowerIntVar1InitEnc.replace('\n','')
        FilteringThresholdLowerIntVar1InitEnc = [FilteringThresholdLowerIntVar1InitEnc[i:i+4] for i in range(0,len(FilteringThresholdLowerIntVar1InitEnc),4)]
        FilteringThresholdLowerIntVar1Init = ''
        for i in range(len(FilteringThresholdLowerIntVar1InitEnc)):
            FilteringThresholdLowerIntVar1Init = FilteringThresholdLowerIntVar1Init + format(hex(int(FilteringThresholdLowerIntVar1InitEnc[i],2)))[2]

        # Decode filtering threshold upper intensity variable
        FilteringThresholdUpperIntVar1InitEnc = FilteringThresholdUpperIntVar1InitEnc.replace('\n','')
        FilteringThresholdUpperIntVar1InitEnc = [FilteringThresholdUpperIntVar1InitEnc[i:i+4] for i in range(0,len(FilteringThresholdUpperIntVar1InitEnc),4)]
        FilteringThresholdUpperIntVar1Init = ''
        for i in range(len(FilteringThresholdUpperIntVar1InitEnc)):
            FilteringThresholdUpperIntVar1Init = FilteringThresholdUpperIntVar1Init + format(hex(int(FilteringThresholdUpperIntVar1InitEnc[i],2)))[2]

        # Decode theme light color toolbar variable
        ThemeLightColorTBVar1InitEnc = ThemeLightColorTBVar1InitEnc.replace('\n','')
        ThemeLightColorTBVar1InitEnc = [ThemeLightColorTBVar1InitEnc[i:i+4] for i in range(0,len(ThemeLightColorTBVar1InitEnc),4)]
        ThemeLightColorTBVar1Init = ''
        for i in range(len(ThemeLightColorTBVar1InitEnc)):
            ThemeLightColorTBVar1Init = ThemeLightColorTBVar1Init + format(hex(int(ThemeLightColorTBVar1InitEnc[i],2)))[2]
        ThemeLightColorTBVar1Init = '#'+ThemeLightColorTBVar1Init

        # Decode theme light color foreground variable
        ThemeLightColorFGVar1InitEnc = ThemeLightColorFGVar1InitEnc.replace('\n','')
        ThemeLightColorFGVar1InitEnc = [ThemeLightColorFGVar1InitEnc[i:i+4] for i in range(0,len(ThemeLightColorFGVar1InitEnc),4)]
        ThemeLightColorFGVar1Init = ''
        for i in range(len(ThemeLightColorFGVar1InitEnc)):
            ThemeLightColorFGVar1Init = ThemeLightColorFGVar1Init + format(hex(int(ThemeLightColorFGVar1InitEnc[i],2)))[2]
        ThemeLightColorFGVar1Init = '#'+ThemeLightColorFGVar1Init

        # Decode theme light color background variable
        ThemeLightColorBGVar1InitEnc = ThemeLightColorBGVar1InitEnc.replace('\n','')
        ThemeLightColorBGVar1InitEnc = [ThemeLightColorBGVar1InitEnc[i:i+4] for i in range(0,len(ThemeLightColorBGVar1InitEnc),4)]
        ThemeLightColorBGVar1Init = ''
        for i in range(len(ThemeLightColorBGVar1InitEnc)):
            ThemeLightColorBGVar1Init = ThemeLightColorBGVar1Init + format(hex(int(ThemeLightColorBGVar1InitEnc[i],2)))[2]
        ThemeLightColorBGVar1Init = '#'+ThemeLightColorBGVar1Init

        # Decode theme light color font variable
        ThemeLightColorFontVar1InitEnc = ThemeLightColorFontVar1InitEnc.replace('\n','')
        ThemeLightColorFontVar1InitEnc = [ThemeLightColorFontVar1InitEnc[i:i+4] for i in range(0,len(ThemeLightColorFontVar1InitEnc),4)]
        ThemeLightColorFontVar1Init = ''
        for i in range(len(ThemeLightColorFontVar1InitEnc)):
            ThemeLightColorFontVar1Init = ThemeLightColorFontVar1Init + format(hex(int(ThemeLightColorFontVar1InitEnc[i],2)))[2]
        ThemeLightColorFontVar1Init = '#'+ThemeLightColorFontVar1Init

        # Decode theme light color button variable
        ThemeLightColorBTVar1InitEnc = ThemeLightColorBTVar1InitEnc.replace('\n','')
        ThemeLightColorBTVar1InitEnc = [ThemeLightColorBTVar1InitEnc[i:i+4] for i in range(0,len(ThemeLightColorBTVar1InitEnc),4)]
        ThemeLightColorBTVar1Init = ''
        for i in range(len(ThemeLightColorBTVar1InitEnc)):
            ThemeLightColorBTVar1Init = ThemeLightColorBTVar1Init + format(hex(int(ThemeLightColorBTVar1InitEnc[i],2)))[2]
        ThemeLightColorBTVar1Init = '#'+ThemeLightColorBTVar1Init

        # Decode theme light color border variable
        ThemeLightColorBDVar1InitEnc = ThemeLightColorBDVar1InitEnc.replace('\n','')
        ThemeLightColorBDVar1InitEnc = [ThemeLightColorBDVar1InitEnc[i:i+4] for i in range(0,len(ThemeLightColorBDVar1InitEnc),4)]
        ThemeLightColorBDVar1Init = ''
        for i in range(len(ThemeLightColorBDVar1InitEnc)):
            ThemeLightColorBDVar1Init = ThemeLightColorBDVar1Init + format(hex(int(ThemeLightColorBDVar1InitEnc[i],2)))[2]
        ThemeLightColorBDVar1Init = '#'+ThemeLightColorBDVar1Init

        # Decode theme dark color toolbar variable
        ThemeDarkColorTBVar1InitEnc = ThemeDarkColorTBVar1InitEnc.replace('\n','')
        ThemeDarkColorTBVar1InitEnc = [ThemeDarkColorTBVar1InitEnc[i:i+4] for i in range(0,len(ThemeDarkColorTBVar1InitEnc),4)]
        ThemeDarkColorTBVar1Init = ''
        for i in range(len(ThemeDarkColorTBVar1InitEnc)):
            ThemeDarkColorTBVar1Init = ThemeDarkColorTBVar1Init + format(hex(int(ThemeDarkColorTBVar1InitEnc[i],2)))[2]
        ThemeDarkColorTBVar1Init = '#'+ThemeDarkColorTBVar1Init

        # Decode theme dark color foreground variable
        ThemeDarkColorFGVar1InitEnc = ThemeDarkColorFGVar1InitEnc.replace('\n','')
        ThemeDarkColorFGVar1InitEnc = [ThemeDarkColorFGVar1InitEnc[i:i+4] for i in range(0,len(ThemeDarkColorFGVar1InitEnc),4)]
        ThemeDarkColorFGVar1Init = ''
        for i in range(len(ThemeDarkColorFGVar1InitEnc)):
            ThemeDarkColorFGVar1Init = ThemeDarkColorFGVar1Init + format(hex(int(ThemeDarkColorFGVar1InitEnc[i],2)))[2]
        ThemeDarkColorFGVar1Init = '#'+ThemeDarkColorFGVar1Init

        # Decode theme dark color background variable
        ThemeDarkColorBGVar1InitEnc = ThemeDarkColorBGVar1InitEnc.replace('\n','')
        ThemeDarkColorBGVar1InitEnc = [ThemeDarkColorBGVar1InitEnc[i:i+4] for i in range(0,len(ThemeDarkColorBGVar1InitEnc),4)]
        ThemeDarkColorBGVar1Init = ''
        for i in range(len(ThemeDarkColorBGVar1InitEnc)):
            ThemeDarkColorBGVar1Init = ThemeDarkColorBGVar1Init + format(hex(int(ThemeDarkColorBGVar1InitEnc[i],2)))[2]
        ThemeDarkColorBGVar1Init = '#'+ThemeDarkColorBGVar1Init

        # Decode theme dark color font variable
        ThemeDarkColorFontVar1InitEnc = ThemeDarkColorFontVar1InitEnc.replace('\n','')
        ThemeDarkColorFontVar1InitEnc = [ThemeDarkColorFontVar1InitEnc[i:i+4] for i in range(0,len(ThemeDarkColorFontVar1InitEnc),4)]
        ThemeDarkColorFontVar1Init = ''
        for i in range(len(ThemeDarkColorFontVar1InitEnc)):
            ThemeDarkColorFontVar1Init = ThemeDarkColorFontVar1Init + format(hex(int(ThemeDarkColorFontVar1InitEnc[i],2)))[2]
        ThemeDarkColorFontVar1Init = '#'+ThemeDarkColorFontVar1Init

        # Decode theme dark color button variable
        ThemeDarkColorBTVar1InitEnc = ThemeDarkColorBTVar1InitEnc.replace('\n','')
        ThemeDarkColorBTVar1InitEnc = [ThemeDarkColorBTVar1InitEnc[i:i+4] for i in range(0,len(ThemeDarkColorBTVar1InitEnc),4)]
        ThemeDarkColorBTVar1Init = ''
        for i in range(len(ThemeDarkColorBTVar1InitEnc)):
            ThemeDarkColorBTVar1Init = ThemeDarkColorBTVar1Init + format(hex(int(ThemeDarkColorBTVar1InitEnc[i],2)))[2]
        ThemeDarkColorBTVar1Init = '#'+ThemeDarkColorBTVar1Init

        # Decode theme dark color border variable
        ThemeDarkColorBDVar1InitEnc = ThemeDarkColorBDVar1InitEnc.replace('\n','')
        ThemeDarkColorBDVar1InitEnc = [ThemeDarkColorBDVar1InitEnc[i:i+4] for i in range(0,len(ThemeDarkColorBDVar1InitEnc),4)]
        ThemeDarkColorBDVar1Init = ''
        for i in range(len(ThemeDarkColorBDVar1InitEnc)):
            ThemeDarkColorBDVar1Init = ThemeDarkColorBDVar1Init + format(hex(int(ThemeDarkColorBDVar1InitEnc[i],2)))[2]
        ThemeDarkColorBDVar1Init = '#'+ThemeDarkColorBDVar1Init

        # Decode the rubber band color variable
        RBBColorVar1InitEnc = RBBColorVar1InitEnc.replace('\n','')
        RBBColorVar1InitEnc = [RBBColorVar1InitEnc[i:i+4] for i in range(0,len(RBBColorVar1InitEnc),4)]
        RBBColorVar1Init = ''
        for i in range(len(RBBColorVar1InitEnc)):
            RBBColorVar1Init = RBBColorVar1Init + format(hex(int(RBBColorVar1InitEnc[i],2)))[2]

        RBBColorVar1Init = '#'+RBBColorVar1Init

        # Decode the language variable
        LanguageVar1InitEnc = LanguageVar1InitEnc.replace('\n','')
        LanguageVar1InitEnc = [LanguageVar1InitEnc[i:i+3] for i in range(0,len(LanguageVar1InitEnc),3)]
        LanguageVar1Init = ''

        for i in range(len(LanguageVar1InitEnc)):
            if (LanguageVar1InitEnc[i] == '111'):
                LanguageVar1Init = LanguageVar1Init + '1'
            elif (LanguageVar1InitEnc[i] == '110'):
                LanguageVar1Init = LanguageVar1Init + '0'

        LanguageVar1Init = str(list(LanguageVar1Init)).replace("'",'').replace(' ','').replace('[','').replace(']','')

        # Initialize page layout variables
        PageLayoutAutoRotatePageVar1Init = 0
        PageLayoutDeskewVar1Init = 0
        PageLayoutDecolumnizeVar1Init = 0
        PageLayoutAutoRotatePageVar1Init = 0
        PageLayoutDeskewVar1Init = 0
        PageLayoutDecolumnizeVar1Init = 0
        PageLayoutRemoveTableVar1Init = 0
        PageLayoutRemoveWatermarkVar1Init = 0
        PageLayoutRemoveUnderlineVar1Init = 0
        PageLayoutRemoveSpaceVar1Init = 0
        PageLayoutRemoveLineVar1Init = 0
        LayoutDespeckleVar1Init = 0
        LayoutThresholdVar1Init = 0
        LayoutInvertColorVar1Init = 0
        LayoutThresholdAdaptiveVar1Init = 0
        LayoutSharpenVar1Init = 0
        LayoutContrastVar1Init = 0
        FilteringBackgroundNoiseVar1Init = 0
        FilteringBackgroundNoiseIntVar1Init = 3
        FilteringTextNoiseVar1Init = 0
        FilteringTextNoiseIntVar1Init = 2
        FilteringTextErosionVar1Init = 0
        FilteringTextErosionIntVar1Init = 2
        FilteringTextDilationVar1Init = 0
        FilteringTextDilationIntVar1Init = 2
        FilteringThresholdVar1Init = 0
        FilteringThresholdLowerIntVar1Init = 0
        FilteringThresholdUpperIntVar1Init = 0
        DisplayColorImageVar1Init = 0
        DisplayGrayImageVar1Init = 0
        DisplayProcessedImageVar1Init = 0
        DisplayProcessedAllImageVar1Init = 0
        WhitelistVar1Init = 0
        Whitelist1Var1Init = 0
        Whitelist2Var1Init = 0
        Whitelist3Var1Init = 0
        Whitelist4Var1Init = 0
        Whitelist5Var1Init = 0
        WhitelistCharVar1Init = ''
        BlacklistVar1Init = 0
        Blacklist1Var1Init = 0
        Blacklist2Var1Init = 0
        Blacklist3Var1Init = 0
        Blacklist4Var1Init = 0
        Blacklist5Var1Init = 0
        BlacklistCharVar1Init = ''

    #//===================================================//
    def setFlagOCR(self):
        """
        Sets global flags and configurations for OCR (Optical Character Recognition).
        """

        # Declare global variables for OCR settings
        global LanguageVarList1, LanguageSystemVar1, MathEquationVar1, TextLayoutVar1
        global DetectedTextVar1, DetectedTextLetterVar1, DetectedTextLowerVar1, DetectedTextUpperVar1, DetectedTextNumberVar1, DetectedTextPuncVar1, DetectedTextMiscVar1
        global PageLayoutAutoRotatePageVar1, PageLayoutDeskewVar1, PageLayoutDecolumnizeVar1, PageLayoutRemoveTableVar1
        global PageLayoutRemoveWatermarkVar1, PageLayoutRemoveUnderlineVar1, PageLayoutRemoveSpaceVar1, PageLayoutRemoveLineVar1
        global OutputFormatVar1, OptimizationVar1
        global LayoutDespeckleVar1, LayoutThresholdVar1, LayoutInvertColorVar1, LayoutThresholdAdaptiveVar1, LayoutSharpenVar1, LayoutContrastVar1
        global FilteringBackgroundNoiseVar1, FilteringBackgroundNoiseIntVar1, FilteringTextNoiseVar1, FilteringTextNoiseIntVar1
        global FilteringTextErosionVar1, FilteringTextErosionIntVar1, FilteringTextDilationVar1, FilteringTextDilationIntVar1
        global FilteringThresholdVar1, FilteringThresholdLowerIntVar1, FilteringThresholdUpperIntVar1
        global DisplayColorImageVar1, DisplayGrayImageVar1, DisplayProcessedImageVar1, DisplayProcessedAllImageVar1
        global WhitelistVar1, Whitelist1Var1, Whitelist2Var1, Whitelist3Var1, Whitelist4Var1, Whitelist5Var1, WhitelistCharVar1
        global BlacklistVar1, Blacklist1Var1, Blacklist2Var1, Blacklist3Var1, Blacklist4Var1, Blacklist5Var1, BlacklistCharVar1
        global ThemeLightColorVar1, ThemeLightColorTBVar1, ThemeLightColorFGVar1, ThemeLightColorBGVar1, ThemeLightColorFontVar1, ThemeLightColorBTVar1, ThemeLightColorBDVar1
        global ThemeDarkColorVar1, ThemeDarkColorTBVar1, ThemeDarkColorFGVar1, ThemeDarkColorBGVar1, ThemeDarkColorFontVar1, ThemeDarkColorBTVar1, ThemeDarkColorBDVar1
        global CursorShapeVar1, RBBThicknessVar1, RBBOpacityVar1, RBBColorVar1
        global FontSystemSizeVar1, BorderStyleVar1, TextEditorIconSizeVar1, TextEditorStatusBarVar1, TextEditorModeVar1, SystemTrayIconVar1
        global flag_config, flag_language, FLAG_SETTING_INIT
        # global flag_config, flag_language, FLAG_SETTING_INIT, flag_language_all

        print('=== setFlagOCR ===')

        # Assign global variables from the MainGuiWindow class
        LanguageVarList1 = MainGuiWindow.LanguageVarList1
        LanguageSystemVar1 = MainGuiWindow.LanguageSystemVar1
        MathEquationVar1 = MainGuiWindow.MathEquationVar1
        TextLayoutVar1 = MainGuiWindow.TextLayoutVar1
        DetectedTextVar1 = MainGuiWindow.DetectedTextVar1
        DetectedTextLetterVar1 = MainGuiWindow.DetectedTextLetterVar1
        DetectedTextLowerVar1 = MainGuiWindow.DetectedTextLowerVar1
        DetectedTextUpperVar1 = MainGuiWindow.DetectedTextUpperVar1
        DetectedTextNumberVar1 = MainGuiWindow.DetectedTextNumberVar1
        DetectedTextPuncVar1 = MainGuiWindow.DetectedTextPuncVar1
        DetectedTextMiscVar1 = MainGuiWindow.DetectedTextMiscVar1
        PageLayoutAutoRotatePageVar1 = MainGuiWindow.PageLayoutAutoRotatePageVar1
        PageLayoutDeskewVar1 = MainGuiWindow.PageLayoutDeskewVar1
        PageLayoutDecolumnizeVar1 = MainGuiWindow.PageLayoutDecolumnizeVar1
        PageLayoutRemoveTableVar1  = MainGuiWindow.PageLayoutRemoveTableVar1
        PageLayoutRemoveWatermarkVar1  = MainGuiWindow.PageLayoutRemoveWatermarkVar1
        PageLayoutRemoveUnderlineVar1  = MainGuiWindow.PageLayoutRemoveUnderlineVar1
        PageLayoutRemoveSpaceVar1 = MainGuiWindow.PageLayoutRemoveSpaceVar1
        PageLayoutRemoveLineVar1 = MainGuiWindow.PageLayoutRemoveLineVar1
        OutputFormatVar1 = MainGuiWindow.OutputFormatVar1
        OptimizationVar1 = MainGuiWindow.OptimizationVar1
        LayoutDespeckleVar1 = MainGuiWindow.LayoutDespeckleVar1
        LayoutThresholdVar1 = MainGuiWindow.LayoutThresholdVar1
        LayoutInvertColorVar1 = MainGuiWindow.LayoutInvertColorVar1
        LayoutThresholdAdaptiveVar1 = MainGuiWindow.LayoutThresholdAdaptiveVar1
        LayoutSharpenVar1 = MainGuiWindow.LayoutSharpenVar1
        LayoutContrastVar1 = MainGuiWindow.LayoutContrastVar1
        FilteringBackgroundNoiseVar1 = MainGuiWindow.FilteringBackgroundNoiseVar1
        FilteringBackgroundNoiseIntVar1 = MainGuiWindow.FilteringBackgroundNoiseIntVar1
        FilteringTextNoiseVar1 = MainGuiWindow.FilteringTextNoiseVar1
        FilteringTextNoiseIntVar1 = MainGuiWindow.FilteringTextNoiseIntVar1
        FilteringTextErosionVar1 = MainGuiWindow.FilteringTextErosionVar1
        FilteringTextErosionIntVar1 = MainGuiWindow.FilteringTextErosionIntVar1
        FilteringTextDilationVar1 = MainGuiWindow.FilteringTextDilationVar1
        FilteringTextDilationIntVar1 = MainGuiWindow.FilteringTextDilationIntVar1
        FilteringThresholdVar1 = MainGuiWindow.FilteringThresholdVar1
        FilteringThresholdLowerIntVar1 = MainGuiWindow.FilteringThresholdLowerIntVar1
        FilteringThresholdUpperIntVar1 = MainGuiWindow.FilteringThresholdUpperIntVar1
        DisplayColorImageVar1 = MainGuiWindow.DisplayColorImageVar1
        DisplayGrayImageVar1 = MainGuiWindow.DisplayGrayImageVar1
        DisplayProcessedImageVar1 = MainGuiWindow.DisplayProcessedImageVar1
        DisplayProcessedAllImageVar1 = MainGuiWindow.DisplayProcessedAllImageVar1
        WhitelistVar1 = MainGuiWindow.WhitelistVar1
        Whitelist1Var1 = MainGuiWindow.Whitelist1Var1
        Whitelist2Var1 = MainGuiWindow.Whitelist2Var1
        Whitelist3Var1 = MainGuiWindow.Whitelist3Var1
        Whitelist4Var1 = MainGuiWindow.Whitelist4Var1
        Whitelist5Var1 = MainGuiWindow.Whitelist5Var1
        WhitelistCharVar1 = MainGuiWindow.WhitelistCharVar1
        BlacklistVar1 = MainGuiWindow.BlacklistVar1
        Blacklist1Var1 = MainGuiWindow.Blacklist1Var1
        Blacklist2Var1 = MainGuiWindow.Blacklist2Var1
        Blacklist3Var1 = MainGuiWindow.Blacklist3Var1
        Blacklist4Var1 = MainGuiWindow.Blacklist4Var1
        Blacklist5Var1 = MainGuiWindow.Blacklist5Var1
        BlacklistCharVar1 = MainGuiWindow.BlacklistCharVar1
        ThemeLightColorVar1 = MainGuiWindow.ThemeLightColorVar1
        ThemeLightColorTBVar1 = MainGuiWindow.ThemeLightColorTBVar1
        ThemeLightColorFGVar1 = MainGuiWindow.ThemeLightColorFGVar1
        ThemeLightColorBGVar1 = MainGuiWindow.ThemeLightColorBGVar1
        ThemeLightColorFontVar1 = MainGuiWindow.ThemeLightColorFontVar1
        ThemeLightColorBTVar1 = MainGuiWindow.ThemeLightColorBTVar1
        ThemeLightColorBDVar1 = MainGuiWindow.ThemeLightColorBDVar1
        ThemeDarkColorVar1 = MainGuiWindow.ThemeDarkColorVar1
        ThemeDarkColorTBVar1 = MainGuiWindow.ThemeDarkColorTBVar1
        ThemeDarkColorFGVar1 = MainGuiWindow.ThemeDarkColorFGVar1
        ThemeDarkColorBGVar1 = MainGuiWindow.ThemeDarkColorBGVar1
        ThemeDarkColorFontVar1 = MainGuiWindow.ThemeDarkColorFontVar1
        ThemeDarkColorBTVar1 = MainGuiWindow.ThemeDarkColorBTVar1
        ThemeDarkColorBDVar1 = MainGuiWindow.ThemeDarkColorBDVar1
        CursorShapeVar1 = MainGuiWindow.CursorShapeVar1
        RBBThicknessVar1 = MainGuiWindow.RBBThicknessVar1
        RBBOpacityVar1 = MainGuiWindow.RBBOpacityVar1
        RBBColorVar1 = MainGuiWindow.RBBColorVar1
        FontSystemSizeVar1 = MainGuiWindow.FontSystemSizeVar1
        BorderStyleVar1 = MainGuiWindow.BorderStyleVar1
        TextEditorIconSizeVar1 = MainGuiWindow.TextEditorIconSizeVar1
        TextEditorStatusBarVar1 = MainGuiWindow.TextEditorStatusBarVar1
        TextEditorModeVar1 = MainGuiWindow.TextEditorModeVar1
        SystemTrayIconVar1 = MainGuiWindow.SystemTrayIconVar1
        flag_config = ''
        flag_language = ''



        # Generate the language flag based on the selected languages
        # https://tesseract-ocr.github.io/tessdoc/Data-Files-in-different-versions.html

        # Optimized language mapping using a dictionary
        LANGUAGE_MAP = {
            0: 'eng', 2: 'afr', 3: 'sqi', 4: 'amh', 5: 'ara', 6: 'hye', 7: 'asm',
            8: 'aze+aze_cyrl', 9: 'eus', 10: 'bel', 11: 'ben', 12: 'bos', 13: 'bre',
            14: 'bul', 15: 'mya', 16: 'spa_old', 17: 'cat', 18: 'ceb', 19: 'chi_sim+chi_tra',
            20: 'chi_sim_vert+chi_tra_vert', 21: 'chr', 22: 'cos', 23: 'hrv', 24: 'ces',
            25: 'dan', 26: 'div', 27: 'nld', 28: 'dzo', 29: 'epo', 30: 'est', 31: 'fao',
            32: 'fil', 33: 'fin', 34: 'fra', 35: 'fry', 36: 'gla', 37: 'glg', 38: 'kat',
            39: 'deu', 40: 'ell', 41: 'guj', 42: 'hat', 43: 'heb', 44: 'hin', 45: 'hun',
            46: 'isl', 47: 'ind', 48: 'iku', 49: 'gle', 50: 'ita', 51: 'jpn', 52: 'jpn_vert',
            53: 'jav', 54: 'kan', 55: 'kaz', 56: 'khm', 57: 'kor', 58: 'kmr', 59: 'kir',
            60: 'lao', 61: 'lat', 62: 'lav', 63: 'lit', 64: 'ltz', 65: 'mkd', 66: 'msa',
            67: 'mal', 68: 'mlt', 69: 'mri', 70: 'mar', 71: 'mon', 72: 'nep', 73: 'nor',
            74: 'oci', 75: 'ori', 76: 'pan', 77: 'pus', 78: 'fas', 79: 'pol', 80: 'por',
            81: 'que', 82: 'ron', 83: 'rus', 84: 'san', 85: 'srp+srp_latn', 86: 'snd',
            87: 'sin', 88: 'slk', 89: 'slv', 90: 'spa', 91: 'sun', 92: 'swa', 93: 'swe',
            94: 'syr', 95: 'tgk', 96: 'tam', 97: 'tat', 98: 'tel', 99: 'tha', 100: 'bod',
            101: 'tir', 102: 'ton', 103: 'tur', 104: 'ukr', 105: 'urd', 106: 'uig',
            107: 'uzb+uzb_cyrl', 108: 'vie', 109: 'cym', 110: 'yid', 111: 'yor', 113: ''
        }

        # Generate the language flag based on the selected languages
        flag_language = flag_language + ''.join('+' + LANGUAGE_MAP[i] for i, val in enumerate(LanguageVarList1) if val == 1)
        flag_language = flag_language.rstrip('+')

        # Add system locale language if enabled
        if (LanguageSystemVar1 == 1):
            flag_language = flag_language+'+'+flag_language_system_locale

        # Set text layout configuration based on the selected option
        # https://tesseract-ocr.github.io/tessdoc/ImproveQuality.html
        if (TextLayoutVar1 == 0):       # Auto
            flag_config = '--psm 6'
        elif (TextLayoutVar1 == 1):     # Single Character
            flag_config = '--psm 10'
        elif (TextLayoutVar1 == 2):     # Single Word
            flag_config = '--psm 8'
        elif (TextLayoutVar1 == 3):     # Single Line
            flag_config = '--psm 7'
        elif (TextLayoutVar1 == 4):     # Sparse Text
            flag_config = '--psm 11'
        elif (TextLayoutVar1 == 5):     # Vertical Text
            flag_config = '--psm 5'
        elif (TextLayoutVar1 == 6):     # Single Column
            flag_config = '--psm 4'
        elif (TextLayoutVar1 == 7):     # Multiple Columns
            flag_config = '--psm 6'

        # Add additional configurations for math equations and vertical text
        # https://tesseract-ocr.github.io/tessdoc/ImproveQuality.html#math-equations
        if (MathEquationVar1 == 1):
            flag_language = flag_language+'+'+'equ'  # Add math equation language
            flag_config = '--psm 11'
        if (bool(re.search('chi_sim_vert',flag_language,)) or bool(re.search('chi_tra_vert',flag_language,)) or bool(re.search('jpn_vert',flag_language,))):
            flag_config = '--psm 5'
        if (PageLayoutDecolumnizeVar1 == 1):
            flag_config = '--psm 3'

        # Configure interword spacing
        if (PageLayoutRemoveSpaceVar1 == 0):
            flag_config = flag_config+' '+'-c preserve_interword_spaces=1'
        elif  (PageLayoutRemoveSpaceVar1 == 1):
            flag_config = flag_config+' '+'-c preserve_interword_spaces=0'

        # Generate whitelist and blacklist characters based on detected text settings
        char_letter_a_to_z = ' abcdefghijklmnopqrstuvwxyz'
        char_letter_A_to_Z = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        char_digit = ' 0123456789'
        char_punctuation = " '.,:;_=++-*/\\|^%?!()[]{}<>—‘’“”'" + "\'\"\'" + '\"\'\"'
        char_special = " &#$~§@©®°™¥£¢«»€"
        # char_space = "' '"
        char_whitelist = ''
        char_blacklist = ''

        if (DetectedTextVar1 == 0):
            # If no text detection is enabled, clear all character-related settings
            # char_space = "' '"
            char_whitelist = ''
            char_blacklist = ''
        else:
            # Check combinations of detected text settings and build the whitelist accordingly
            if ((DetectedTextLetterVar1 == 0) and (DetectedTextLowerVar1 == 1) and (DetectedTextUpperVar1 == 1) and (DetectedTextNumberVar1 == 1) and (DetectedTextPuncVar1 == 1) and (DetectedTextMiscVar1 == 1)):
                char_whitelist = char_letter_a_to_z + char_letter_A_to_Z + char_digit + char_punctuation + char_special
            elif ((DetectedTextLetterVar1 == 0) and (DetectedTextLowerVar1 == 1) and (DetectedTextUpperVar1 == 1) and (DetectedTextNumberVar1 == 1) and (DetectedTextPuncVar1 == 1) and (DetectedTextMiscVar1 == 0)):
                char_whitelist = char_letter_a_to_z + char_letter_A_to_Z + char_digit + char_punctuation
            elif ((DetectedTextLetterVar1 == 0) and (DetectedTextLowerVar1 == 1) and (DetectedTextUpperVar1 == 1) and (DetectedTextNumberVar1 == 1) and (DetectedTextPuncVar1 == 0) and (DetectedTextMiscVar1 == 1)):
                char_whitelist = char_letter_a_to_z + char_letter_A_to_Z + char_digit + char_special
            elif ((DetectedTextLetterVar1 == 0) and (DetectedTextLowerVar1 == 1) and (DetectedTextUpperVar1 == 1) and (DetectedTextNumberVar1 == 1) and (DetectedTextPuncVar1 == 0) and (DetectedTextMiscVar1 == 0)):
                char_whitelist = char_letter_a_to_z + char_letter_A_to_Z + char_digit
            elif ((DetectedTextLetterVar1 == 0) and (DetectedTextLowerVar1 == 1) and (DetectedTextUpperVar1 == 1) and (DetectedTextNumberVar1 == 0) and (DetectedTextPuncVar1 == 1) and (DetectedTextMiscVar1 == 1)):
                char_whitelist = char_letter_a_to_z + char_letter_A_to_Z + char_punctuation + char_special
            elif ((DetectedTextLetterVar1 == 0) and (DetectedTextLowerVar1 == 1) and (DetectedTextUpperVar1 == 1) and (DetectedTextNumberVar1 == 0) and (DetectedTextPuncVar1 == 1) and (DetectedTextMiscVar1 == 0)):
                char_whitelist = char_letter_a_to_z + char_letter_A_to_Z + char_punctuation
            elif ((DetectedTextLetterVar1 == 0) and (DetectedTextLowerVar1 == 1) and (DetectedTextUpperVar1 == 1) and (DetectedTextNumberVar1 == 0) and (DetectedTextPuncVar1 == 0) and (DetectedTextMiscVar1 == 1)):
                char_whitelist = char_letter_a_to_z + char_letter_A_to_Z +  char_special
            elif ((DetectedTextLetterVar1 == 0) and (DetectedTextLowerVar1 == 1) and (DetectedTextUpperVar1 == 1) and (DetectedTextNumberVar1 == 0) and (DetectedTextPuncVar1 == 0) and (DetectedTextMiscVar1 == 0)):
                char_whitelist = char_letter_a_to_z + char_letter_A_to_Z

            elif ((DetectedTextLetterVar1 == 0) and (DetectedTextLowerVar1 == 1) and (DetectedTextUpperVar1 == 0) and (DetectedTextNumberVar1 == 1) and (DetectedTextPuncVar1 == 1) and (DetectedTextMiscVar1 == 1)):
                char_whitelist = char_letter_a_to_z + char_digit + char_punctuation + char_special
            elif ((DetectedTextLetterVar1 == 0) and (DetectedTextLowerVar1 == 1) and (DetectedTextUpperVar1 == 0) and (DetectedTextNumberVar1 == 1) and (DetectedTextPuncVar1 == 1) and (DetectedTextMiscVar1 == 0)):
                char_whitelist = char_letter_a_to_z + char_digit + char_punctuation
            elif ((DetectedTextLetterVar1 == 0) and (DetectedTextLowerVar1 == 1) and (DetectedTextUpperVar1 == 0) and (DetectedTextNumberVar1 == 1) and (DetectedTextPuncVar1 == 0) and (DetectedTextMiscVar1 == 1)):
                char_whitelist = char_letter_a_to_z + char_digit + char_special
            elif ((DetectedTextLetterVar1 == 0) and (DetectedTextLowerVar1 == 1) and (DetectedTextUpperVar1 == 0) and (DetectedTextNumberVar1 == 1) and (DetectedTextPuncVar1 == 0) and (DetectedTextMiscVar1 == 0)):
                char_whitelist = char_letter_a_to_z + char_digit
            elif ((DetectedTextLetterVar1 == 0) and (DetectedTextLowerVar1 == 1) and (DetectedTextUpperVar1 == 0) and (DetectedTextNumberVar1 == 0) and (DetectedTextPuncVar1 == 1) and (DetectedTextMiscVar1 == 1)):
                char_whitelist = char_letter_a_to_z + char_punctuation + char_special
            elif ((DetectedTextLetterVar1 == 0) and (DetectedTextLowerVar1 == 1) and (DetectedTextUpperVar1 == 0) and (DetectedTextNumberVar1 == 0) and (DetectedTextPuncVar1 == 1) and (DetectedTextMiscVar1 == 0)):
                char_whitelist = char_letter_a_to_z + char_punctuation
            elif ((DetectedTextLetterVar1 == 0) and (DetectedTextLowerVar1 == 1) and (DetectedTextUpperVar1 == 0) and (DetectedTextNumberVar1 == 0) and (DetectedTextPuncVar1 == 0) and (DetectedTextMiscVar1 == 1)):
                char_whitelist = char_letter_a_to_z + char_special
            elif ((DetectedTextLetterVar1 == 0) and (DetectedTextLowerVar1 == 1) and (DetectedTextUpperVar1 == 0) and (DetectedTextNumberVar1 == 0) and (DetectedTextPuncVar1 == 0) and (DetectedTextMiscVar1 == 0)):
                char_whitelist = char_letter_a_to_z

            if ((DetectedTextLetterVar1 == 0) and (DetectedTextLowerVar1 == 0) and (DetectedTextUpperVar1 == 1) and (DetectedTextNumberVar1 == 1) and (DetectedTextPuncVar1 == 1) and (DetectedTextMiscVar1 == 1)):
                char_whitelist = char_letter_A_to_Z + char_digit + char_punctuation + char_special
            elif ((DetectedTextLetterVar1 == 0) and (DetectedTextLowerVar1 == 0) and (DetectedTextUpperVar1 == 1) and (DetectedTextNumberVar1 == 1) and (DetectedTextPuncVar1 == 1) and (DetectedTextMiscVar1 == 0)):
                char_whitelist = char_letter_A_to_Z + char_digit + char_punctuation
            elif ((DetectedTextLetterVar1 == 0) and (DetectedTextLowerVar1 == 0) and (DetectedTextUpperVar1 == 1) and (DetectedTextNumberVar1 == 1) and (DetectedTextPuncVar1 == 0) and (DetectedTextMiscVar1 == 1)):
                char_whitelist = char_letter_A_to_Z + char_digit + char_special
            elif ((DetectedTextLetterVar1 == 0) and (DetectedTextLowerVar1 == 0) and (DetectedTextUpperVar1 == 1) and (DetectedTextNumberVar1 == 1) and (DetectedTextPuncVar1 == 0) and (DetectedTextMiscVar1 == 0)):
                char_whitelist = char_letter_A_to_Z + char_digit
            elif ((DetectedTextLetterVar1 == 0) and (DetectedTextLowerVar1 == 0) and (DetectedTextUpperVar1 == 1) and (DetectedTextNumberVar1 == 0) and (DetectedTextPuncVar1 == 1) and (DetectedTextMiscVar1 == 1)):
                char_whitelist = char_letter_A_to_Z + char_punctuation + char_special
            elif ((DetectedTextLetterVar1 == 0) and (DetectedTextLowerVar1 == 0) and (DetectedTextUpperVar1 == 1) and (DetectedTextNumberVar1 == 0) and (DetectedTextPuncVar1 == 1) and (DetectedTextMiscVar1 == 0)):
                char_whitelist = char_letter_A_to_Z + char_punctuation
            elif ((DetectedTextLetterVar1 == 0) and (DetectedTextLowerVar1 == 0) and (DetectedTextUpperVar1 == 1) and (DetectedTextNumberVar1 == 0) and (DetectedTextPuncVar1 == 0) and (DetectedTextMiscVar1 == 1)):
                char_whitelist = char_letter_A_to_Z +  char_special
            elif ((DetectedTextLetterVar1 == 0) and (DetectedTextLowerVar1 == 0) and (DetectedTextUpperVar1 == 1) and (DetectedTextNumberVar1 == 0) and (DetectedTextPuncVar1 == 0) and (DetectedTextMiscVar1 == 0)):
                char_whitelist = char_letter_A_to_Z

            elif ((DetectedTextLetterVar1 == 0) and (DetectedTextLowerVar1 == 0) and (DetectedTextUpperVar1 == 0) and (DetectedTextNumberVar1 == 1) and (DetectedTextPuncVar1 == 1) and (DetectedTextMiscVar1 == 1)):
                char_whitelist = char_digit + char_punctuation + char_special
            elif ((DetectedTextLetterVar1 == 0) and (DetectedTextLowerVar1 == 0) and (DetectedTextUpperVar1 == 0) and (DetectedTextNumberVar1 == 1) and (DetectedTextPuncVar1 == 1) and (DetectedTextMiscVar1 == 0)):
                char_whitelist = char_digit + char_punctuation
            elif ((DetectedTextLetterVar1 == 0) and (DetectedTextLowerVar1 == 0) and (DetectedTextUpperVar1 == 0) and (DetectedTextNumberVar1 == 1) and (DetectedTextPuncVar1 == 0) and (DetectedTextMiscVar1 == 1)):
                char_whitelist = char_digit + char_special
            elif ((DetectedTextLetterVar1 == 0) and (DetectedTextLowerVar1 == 0) and (DetectedTextUpperVar1 == 0) and (DetectedTextNumberVar1 == 1) and (DetectedTextPuncVar1 == 0) and (DetectedTextMiscVar1 == 0)):
                char_whitelist = char_digit
            elif ((DetectedTextLetterVar1 == 0) and (DetectedTextLowerVar1 == 0) and (DetectedTextUpperVar1 == 0) and (DetectedTextNumberVar1 == 0) and (DetectedTextPuncVar1 == 1) and (DetectedTextMiscVar1 == 1)):
                char_whitelist = char_punctuation + char_special
            elif ((DetectedTextLetterVar1 == 0) and (DetectedTextLowerVar1 == 0) and (DetectedTextUpperVar1 == 0) and (DetectedTextNumberVar1 == 0) and (DetectedTextPuncVar1 == 1) and (DetectedTextMiscVar1 == 0)):
                char_whitelist = char_punctuation
            elif ((DetectedTextLetterVar1 == 0) and (DetectedTextLowerVar1 == 0) and (DetectedTextUpperVar1 == 0) and (DetectedTextNumberVar1 == 0) and (DetectedTextPuncVar1 == 0) and (DetectedTextMiscVar1 == 1)):
                char_whitelist = char_special
            elif ((DetectedTextLetterVar1 == 0) and (DetectedTextLowerVar1 == 0) and (DetectedTextUpperVar1 == 0) and (DetectedTextNumberVar1 == 0) and (DetectedTextPuncVar1 == 0) and (DetectedTextMiscVar1 == 0)):
                char_whitelist = char_whitelist

            # //=======================================//
            if ((DetectedTextLetterVar1 == 1) and (DetectedTextLowerVar1 == 1) and (DetectedTextUpperVar1 == 1) and (DetectedTextNumberVar1 == 1) and (DetectedTextPuncVar1 == 1) and (DetectedTextMiscVar1 == 1)):
                char_blacklist = char_blacklist
            elif ((DetectedTextLetterVar1 == 1) and (DetectedTextLowerVar1 == 1) and (DetectedTextUpperVar1 == 1) and (DetectedTextNumberVar1 == 1) and (DetectedTextPuncVar1 == 1) and (DetectedTextMiscVar1 == 0)):
                char_blacklist = char_special
            elif ((DetectedTextLetterVar1 == 1) and (DetectedTextLowerVar1 == 1) and (DetectedTextUpperVar1 == 1) and (DetectedTextNumberVar1 == 1) and (DetectedTextPuncVar1 == 0) and (DetectedTextMiscVar1 == 1)):
                char_blacklist = char_punctuation
            elif ((DetectedTextLetterVar1 == 1) and (DetectedTextLowerVar1 == 1) and (DetectedTextUpperVar1 == 1) and (DetectedTextNumberVar1 == 1) and (DetectedTextPuncVar1 == 0) and (DetectedTextMiscVar1 == 0)):
                char_blacklist = char_punctuation + char_special
            elif ((DetectedTextLetterVar1 == 1) and (DetectedTextLowerVar1 == 1) and (DetectedTextUpperVar1 == 1) and (DetectedTextNumberVar1 == 0) and (DetectedTextPuncVar1 == 1) and (DetectedTextMiscVar1 == 1)):
                char_blacklist = char_digit
            elif ((DetectedTextLetterVar1 == 1) and (DetectedTextLowerVar1 == 1) and (DetectedTextUpperVar1 == 1) and (DetectedTextNumberVar1 == 0) and (DetectedTextPuncVar1 == 1) and (DetectedTextMiscVar1 == 0)):
                char_blacklist = char_digit + char_special
            elif ((DetectedTextLetterVar1 == 1) and (DetectedTextLowerVar1 == 1) and (DetectedTextUpperVar1 == 1) and (DetectedTextNumberVar1 == 0) and (DetectedTextPuncVar1 == 0) and (DetectedTextMiscVar1 == 1)):
                char_blacklist = char_digit + char_punctuation
            elif ((DetectedTextLetterVar1 == 1) and (DetectedTextLowerVar1 == 1) and (DetectedTextUpperVar1 == 1) and (DetectedTextNumberVar1 == 0) and (DetectedTextPuncVar1 == 0) and (DetectedTextMiscVar1 == 0)):
                char_blacklist = char_digit + char_punctuation + char_special

            elif ((DetectedTextLetterVar1 == 1) and (DetectedTextLowerVar1 == 1) and (DetectedTextUpperVar1 == 0) and (DetectedTextNumberVar1 == 1) and (DetectedTextPuncVar1 == 1) and (DetectedTextMiscVar1 == 1)):
                char_blacklist = char_letter_A_to_Z
            elif ((DetectedTextLetterVar1 == 1) and (DetectedTextLowerVar1 == 1) and (DetectedTextUpperVar1 == 0) and (DetectedTextNumberVar1 == 1) and (DetectedTextPuncVar1 == 1) and (DetectedTextMiscVar1 == 0)):
                char_blacklist = char_letter_A_to_Z + char_special
            elif ((DetectedTextLetterVar1 == 1) and (DetectedTextLowerVar1 == 1) and (DetectedTextUpperVar1 == 0) and (DetectedTextNumberVar1 == 1) and (DetectedTextPuncVar1 == 0) and (DetectedTextMiscVar1 == 1)):
                char_blacklist = char_letter_A_to_Z + char_punctuation
            elif ((DetectedTextLetterVar1 == 1) and (DetectedTextLowerVar1 == 1) and (DetectedTextUpperVar1 == 0) and (DetectedTextNumberVar1 == 1) and (DetectedTextPuncVar1 == 0) and (DetectedTextMiscVar1 == 0)):
                char_blacklist = char_letter_A_to_Z + char_punctuation + char_special
            elif ((DetectedTextLetterVar1 == 1) and (DetectedTextLowerVar1 == 1) and (DetectedTextUpperVar1 == 0) and (DetectedTextNumberVar1 == 0) and (DetectedTextPuncVar1 == 1) and (DetectedTextMiscVar1 == 1)):
                char_blacklist = char_letter_A_to_Z + char_digit
            elif ((DetectedTextLetterVar1 == 1) and (DetectedTextLowerVar1 == 1) and (DetectedTextUpperVar1 == 0) and (DetectedTextNumberVar1 == 0) and (DetectedTextPuncVar1 == 1) and (DetectedTextMiscVar1 == 0)):
                char_blacklist = char_letter_A_to_Z + char_digit + char_special
            elif ((DetectedTextLetterVar1 == 1) and (DetectedTextLowerVar1 == 1) and (DetectedTextUpperVar1 == 0) and (DetectedTextNumberVar1 == 0) and (DetectedTextPuncVar1 == 0) and (DetectedTextMiscVar1 == 1)):
                char_blacklist = char_letter_A_to_Z + char_digit + char_punctuation
            elif ((DetectedTextLetterVar1 == 1) and (DetectedTextLowerVar1 == 1) and (DetectedTextUpperVar1 == 0) and (DetectedTextNumberVar1 == 0) and (DetectedTextPuncVar1 == 0) and (DetectedTextMiscVar1 == 0)):
                char_blacklist = char_letter_A_to_Z + char_digit + char_punctuation + char_special

            if ((DetectedTextLetterVar1 == 1) and (DetectedTextLowerVar1 == 0) and (DetectedTextUpperVar1 == 1) and (DetectedTextNumberVar1 == 1) and (DetectedTextPuncVar1 == 1) and (DetectedTextMiscVar1 == 1)):
                char_blacklist = char_letter_a_to_z
            elif ((DetectedTextLetterVar1 == 1) and (DetectedTextLowerVar1 == 0) and (DetectedTextUpperVar1 == 1) and (DetectedTextNumberVar1 == 1) and (DetectedTextPuncVar1 == 1) and (DetectedTextMiscVar1 == 0)):
                char_blacklist = char_letter_a_to_z + char_special
            elif ((DetectedTextLetterVar1 == 1) and (DetectedTextLowerVar1 == 0) and (DetectedTextUpperVar1 == 1) and (DetectedTextNumberVar1 == 1) and (DetectedTextPuncVar1 == 0) and (DetectedTextMiscVar1 == 1)):
                char_blacklist = char_letter_a_to_z + char_punctuation
            elif ((DetectedTextLetterVar1 == 1) and (DetectedTextLowerVar1 == 0) and (DetectedTextUpperVar1 == 1) and (DetectedTextNumberVar1 == 1) and (DetectedTextPuncVar1 == 0) and (DetectedTextMiscVar1 == 0)):
                char_blacklist = char_letter_a_to_z + char_punctuation + char_special
            elif ((DetectedTextLetterVar1 == 1) and (DetectedTextLowerVar1 == 0) and (DetectedTextUpperVar1 == 1) and (DetectedTextNumberVar1 == 0) and (DetectedTextPuncVar1 == 1) and (DetectedTextMiscVar1 == 1)):
                char_blacklist = char_letter_a_to_z + char_digit
            elif ((DetectedTextLetterVar1 == 1) and (DetectedTextLowerVar1 == 0) and (DetectedTextUpperVar1 == 1) and (DetectedTextNumberVar1 == 0) and (DetectedTextPuncVar1 == 1) and (DetectedTextMiscVar1 == 0)):
                char_blacklist = char_letter_a_to_z + char_digit + char_special
            elif ((DetectedTextLetterVar1 == 1) and (DetectedTextLowerVar1 == 0) and (DetectedTextUpperVar1 == 1) and (DetectedTextNumberVar1 == 0) and (DetectedTextPuncVar1 == 0) and (DetectedTextMiscVar1 == 1)):
                char_blacklist = char_letter_a_to_z + char_digit + char_punctuation
            elif ((DetectedTextLetterVar1 == 1) and (DetectedTextLowerVar1 == 0) and (DetectedTextUpperVar1 == 1) and (DetectedTextNumberVar1 == 0) and (DetectedTextPuncVar1 == 0) and (DetectedTextMiscVar1 == 0)):
                char_blacklist = char_letter_a_to_z + char_digit + char_punctuation + char_special

            elif ((DetectedTextLetterVar1 == 1) and (DetectedTextLowerVar1 == 0) and (DetectedTextUpperVar1 == 0) and (DetectedTextNumberVar1 == 1) and (DetectedTextPuncVar1 == 1) and (DetectedTextMiscVar1 == 1)):
                char_blacklist = char_letter_a_to_z + char_letter_A_to_Z
            elif ((DetectedTextLetterVar1 == 1) and (DetectedTextLowerVar1 == 0) and (DetectedTextUpperVar1 == 0) and (DetectedTextNumberVar1 == 1) and (DetectedTextPuncVar1 == 1) and (DetectedTextMiscVar1 == 0)):
                char_blacklist = char_letter_a_to_z + char_letter_A_to_Z + char_special
            elif ((DetectedTextLetterVar1 == 1) and (DetectedTextLowerVar1 == 0) and (DetectedTextUpperVar1 == 0) and (DetectedTextNumberVar1 == 1) and (DetectedTextPuncVar1 == 0) and (DetectedTextMiscVar1 == 1)):
                char_blacklist = char_letter_a_to_z + char_letter_A_to_Z + char_punctuation
            elif ((DetectedTextLetterVar1 == 1) and (DetectedTextLowerVar1 == 0) and (DetectedTextUpperVar1 == 0) and (DetectedTextNumberVar1 == 1) and (DetectedTextPuncVar1 == 0) and (DetectedTextMiscVar1 == 0)):
                char_blacklist = char_letter_a_to_z + char_letter_A_to_Z + char_punctuation + char_special
            elif ((DetectedTextLetterVar1 == 1) and (DetectedTextLowerVar1 == 0) and (DetectedTextUpperVar1 == 0) and (DetectedTextNumberVar1 == 0) and (DetectedTextPuncVar1 == 1) and (DetectedTextMiscVar1 == 1)):
                char_blacklist = char_letter_a_to_z + char_letter_A_to_Z + char_digit
            elif ((DetectedTextLetterVar1 == 1) and (DetectedTextLowerVar1 == 0) and (DetectedTextUpperVar1 == 0) and (DetectedTextNumberVar1 == 0) and (DetectedTextPuncVar1 == 1) and (DetectedTextMiscVar1 == 0)):
                char_blacklist = char_letter_a_to_z + char_letter_A_to_Z + char_digit + char_special
            elif ((DetectedTextLetterVar1 == 1) and (DetectedTextLowerVar1 == 0) and (DetectedTextUpperVar1 == 0) and (DetectedTextNumberVar1 == 0) and (DetectedTextPuncVar1 == 0) and (DetectedTextMiscVar1 == 1)):
                char_blacklist = char_letter_a_to_z + char_letter_A_to_Z + char_digit + char_punctuation
            elif ((DetectedTextLetterVar1 == 1) and (DetectedTextLowerVar1 == 0) and (DetectedTextUpperVar1 == 0) and (DetectedTextNumberVar1 == 0) and (DetectedTextPuncVar1 == 0) and (DetectedTextMiscVar1 == 0)):
                char_blacklist = char_letter_a_to_z + char_letter_A_to_Z + char_digit + char_punctuation + char_special

        # //=====================================================//
        if (WhitelistVar1 == 0):
            print('=== No WhitelistCharVar1 ===')
        else:
            char_whitelist = MainGuiWindow.WhitelistCharVar1.replace("\n","")

        if (BlacklistVar1 == 0):
            print('=== No BlacklistCharVar1 ===')
        else:
            char_blacklist = MainGuiWindow.BlacklistCharVar1.replace("\n","")

        # //=====================================================//
        # Construct the OCR configuration flags for Tesseract
        # flag_config = flag_config+' '+'-c tessedit_char_whitelist=' + char_whitelist + char_space
        flag_config = flag_config+' '+'-c tessedit_char_whitelist=' + char_whitelist
        flag_config = flag_config+' '+'-c tessedit_char_blacklist=' + char_blacklist
        flag_config = '--oem 3'+' '+ flag_config  # Use LSTM OCR engine (default)
        flag_config = flag_config.replace("+", "", 1)
        flag_language = flag_language.replace("+", "", 1)

        # Print the final OCR configuration and language flags for debugging
        print('flag_config := ', flag_config)
        print('flag_language := ', flag_language)

    #//===================================================//
    def exitProgram(self):
        """
        Handles the program exit process:
        - Saves the current theme settings.
        - Closes any open OpenCV windows.
        - Checks for a specific file on the desktop and reads it if it exists.
        - Closes the main application window and quits the application.
        """

        from src.config.py_config import FILENAME2, DESKTOP_FOLDER

        print("=== exitProgram ===")
        # Save the current theme settings to a file
        MainGuiWindow.SaveThemeFileSetting(self)
        try:
            # Close all OpenCV windows
            cv2.destroyAllWindows()

            # Get the desktop path and construct the file path
            self.path_desktop = str(Path.home()/DESKTOP_FOLDER)
            self.path_desktop = self.path_desktop.replace('\\','/')
            self.path_filename = str(self.path_desktop) + '/' + str(FILENAME2)
            file2 = Path(self.path_filename)

            # If the file exists, read its content
            if (file2.exists()):
                self.read_document1()
        except:
            pass

        # Close the main window and quit the application
        self.close()
        qApp.quit()

    # //===========================================//
    def encode_ThemeSetting(self):
        """
        Encodes theme-related settings into binary or hexadecimal formats for saving.
        This includes settings like font family, font size, opacity, and toolbar flags.
        """
        global FontTextFamilyLightVarEnc, FontTextFamilyDarkVarEnc
        global FontTextColorLightVar, FontTextColorLightVarEnc, FontTextColorDarkVar, FontTextColorDarkVarEnc
        global ThemeVarEnc, FontTextSizeLightVarEnc, FontTextSizeDarkVarEnc, OpacityTextLightVarEnc, OpacityTextDarkVarEnc
        global DirectionTextVarEnc, ParagraphTextLightVarEnc, ParagraphTextDarkVarEnc
        global DockingVarEnc, FlagToolbarVarEnc, FlagFormatbarVarEnc, FlagStatusbarVarEnc
        global FontTextSizeLightVar, FontTextSizeDarkVar, DockingVar

        print('=== encode_ThemeSetting ===')

        # Encode theme type (light or dark)
        if (ThemeVar == 0):
            ThemeVarEnc = '1011'  # Light theme
        elif (ThemeVar == 1):
            ThemeVarEnc = '1110'  # Dark theme

        # Encode opacity settings for light theme
        if (OpacityTextLightVar == 0.005):
            OpacityTextLightVarEnc = '0011'
        elif (OpacityTextLightVar == 0.2):
            OpacityTextLightVarEnc = '1010'
        elif (OpacityTextLightVar == 0.4):
            OpacityTextLightVarEnc = '1011'
        elif (OpacityTextLightVar == 0.6):
            OpacityTextLightVarEnc = '0110'
        elif (OpacityTextLightVar == 0.8):
            OpacityTextLightVarEnc = '1001'
        elif (OpacityTextLightVar == 1.0):
            OpacityTextLightVarEnc = '0111'

        # Encode opacity settings for dark theme
        if (OpacityTextDarkVar == 0.005):
            OpacityTextDarkVarEnc = '0111'
        elif (OpacityTextDarkVar == 0.2):
            OpacityTextDarkVarEnc = '0100'
        elif (OpacityTextDarkVar == 0.4):
            OpacityTextDarkVarEnc = '1001'
        elif (OpacityTextDarkVar == 0.6):
            OpacityTextDarkVarEnc = '1100'
        elif (OpacityTextDarkVar == 0.8):
            OpacityTextDarkVarEnc = '1011'
        elif (OpacityTextDarkVar == 1.0):
            OpacityTextDarkVarEnc = '0010'

        # Encode text direction (left-to-right or right-to-left)
        if (DirectionTextVar == 0):
            DirectionTextVarEnc = '0101'
        elif (DirectionTextVar == 1):
            DirectionTextVarEnc = '1010'

        # Encode paragraph settings for light theme
        if (ParagraphTextLightVar == 0):
            ParagraphTextLightVarEnc = '1011'
        elif (ParagraphTextLightVar == 1):
            ParagraphTextLightVarEnc = '1010'

        # Encode paragraph settings for dark theme
        if (ParagraphTextDarkVar == 0):
            ParagraphTextDarkVarEnc = '0110'
        elif (ParagraphTextDarkVar == 1):
            ParagraphTextDarkVarEnc = '1010'

        # Encode docking settings
        DockingVar = str(DockingVar)
        DockingVarEnc = ''
        for i in DockingVar:
            DockingVarEnc = DockingVarEnc + format(int(i,16),"04b")

        # Encode toolbar flag
        if (FlagToolbarVar == 0):
            FlagToolbarVarEnc = '1101'
        elif (FlagToolbarVar == 1):
            FlagToolbarVarEnc = '1010'

        # Encode format bar flag
        if (FlagFormatbarVar == 0):
            FlagFormatbarVarEnc = '0101'
        elif (FlagFormatbarVar == 1):
            FlagFormatbarVarEnc = '1110'

        # Encode status bar flag
        if (FlagStatusbarVar == 0):
            FlagStatusbarVarEnc = '1011'
        elif (FlagStatusbarVar == 1):
            FlagStatusbarVarEnc = '1100'

        # Encode font size for light theme
        FontTextSizeLightVar = str(FontTextSizeLightVar)
        FontTextSizeLightVarEnc = ''
        for i in FontTextSizeLightVar:
            FontTextSizeLightVarEnc = FontTextSizeLightVarEnc + format(int(i,16),"04b")

        # Encode font size for dark theme
        FontTextSizeDarkVar = str(FontTextSizeDarkVar)
        FontTextSizeDarkVarEnc = ''
        for i in FontTextSizeDarkVar:
            FontTextSizeDarkVarEnc = FontTextSizeDarkVarEnc + format(int(i,16),"04b")

        # Encode font color for light theme
        FontTextColorLightVar = str(FontTextColorLightVar).replace('#','')
        FontTextColorLightVarEnc = ''
        for i in FontTextColorLightVar:
            FontTextColorLightVarEnc = FontTextColorLightVarEnc + format(int(i,16),"04b")

        # Encode font color for dark theme
        FontTextColorDarkVar = str(FontTextColorDarkVar).replace('#','')
        FontTextColorDarkVarEnc = ''
        for i in FontTextColorDarkVar:
            FontTextColorDarkVarEnc = FontTextColorDarkVarEnc + format(int(i,16),"04b")

        # Encode font family for light theme
        FontTextFamilyLightVarEnc = [ord(i) + 96 for i in FontTextFamilyLightVar]
        FontTextFamilyLightVarEnc = ''.join([str(format(int(i),"8b")) for i in FontTextFamilyLightVarEnc])

        # Encode font family for dark theme
        FontTextFamilyDarkVarEnc = [ord(i) + 96 for i in FontTextFamilyDarkVar]
        FontTextFamilyDarkVarEnc = ''.join([str(format(int(i),"8b")) for i in FontTextFamilyDarkVarEnc])

    # //===========================================//
    def SaveThemeFileSetting(self):
        """
        Saves the current theme settings to a configuration file.
        This includes settings like theme type, font size, font family, font color, opacity, and UI flags.
        """
        global  ThemeVar, FontTextSizeLightVar, FontTextSizeDarkVar, FontTextFamilyLightVar, FontTextFamilyDarkVar, \
                FontTextColorLightVar, FontTextColorDarkVar, OpacityTextLightVar, OpacityTextDarkVar, \
                DirectionTextVar, ParagraphTextLightVar, ParagraphTextDarkVar, DockingVar, \
                FlagToolbarVar, FlagFormatbarVar, FlagStatusbarVar

        # Determine the current theme (light or dark)
        if (MainGuiWindow.THEME == "light"):
            ThemeVar = 0  # Light theme
        elif (MainGuiWindow.THEME == "dark"):
            ThemeVar = 1  # Dark theme

        # Retrieve current settings from the MainGuiWindow class
        OpacityTextLightVar = MainGuiWindow.OPACITY_TEXT_LIGHT
        OpacityTextDarkVar = MainGuiWindow.OPACITY_TEXT_DARK
        DirectionTextVar = int(MainGuiWindow.DIRECTION_TEXT)
        ParagraphTextLightVar = int(MainGuiWindow.PARAGRAPH_TEXT_LIGHT)
        ParagraphTextDarkVar = int(MainGuiWindow.PARAGRAPH_TEXT_DARK)
        DockingVar = int(MainGuiWindow.DOCKING)
        FlagToolbarVar = int(MainGuiWindow.FLAG_TOOLBAR)
        FlagFormatbarVar = int(MainGuiWindow.FLAG_FORMATBAR)
        FlagStatusbarVar = int(MainGuiWindow.FLAG_STATUSBAR)
        FontTextSizeLightVar = MainGuiWindow.FONT_TEXT_SIZE_LIGHT
        FontTextSizeDarkVar = MainGuiWindow.FONT_TEXT_SIZE_DARK
        FontTextColorLightVar = MainGuiWindow.FONT_TEXT_COLOR_LIGHT
        FontTextColorDarkVar = MainGuiWindow.FONT_TEXT_COLOR_DARK
        FontTextFamilyLightVar = MainGuiWindow.FONT_TEXT_FAMILY_LIGHT
        FontTextFamilyDarkVar = MainGuiWindow.FONT_TEXT_FAMILY_DARK

        # Encode the settings into binary or hexadecimal formats
        self.encode_ThemeSetting()

        try:
            print('=== SaveThemeFileSetting ===')
            # Open the configuration file for writing
            with open(MainGuiWindow.file3, "w") as f_obj:
                # Write encoded settings to the file
                f_obj.write(f"{ThemeVarEnc}\n")                    # THEME
                f_obj.write(f"{OpacityTextLightVarEnc}\n")         # OPACITY_TEXT_LIGHT
                f_obj.write(f"{OpacityTextDarkVarEnc}\n")          # OPACITY_TEXT_DARK
                f_obj.write(f"{DirectionTextVarEnc}\n")            # DIRECTION_TEXT
                f_obj.write(f"{ParagraphTextLightVarEnc}\n")       # PARAGRAPH_TEXT_LIGHT
                f_obj.write(f"{ParagraphTextDarkVarEnc}\n")        # PARAGRAPH_TEXT_DARK
                f_obj.write(f"{DockingVarEnc}\n")                  # DOCKING
                f_obj.write(f"{FlagToolbarVarEnc}\n")              # FLAG_TOOLBAR
                f_obj.write(f"{FlagFormatbarVarEnc}\n")            # FLAG_FORMATBAR
                f_obj.write(f"{FlagStatusbarVarEnc}\n")            # FLAG_STATUSBAR
                f_obj.write(f"{FontTextSizeLightVarEnc}\n")        # FONT_TEXT_SIZE_LIGHT
                f_obj.write(f"{FontTextSizeDarkVarEnc}\n")         # FONT_TEXT_SIZE_DARK
                f_obj.write(f"{FontTextColorLightVarEnc}\n")       # FONT_TEXT_COLOR_LIGHT
                f_obj.write(f"{FontTextColorDarkVarEnc}\n")        # FONT_TEXT_COLOR_DARK
                f_obj.write(f"{FontTextFamilyLightVarEnc}\n")      # FONT_TEXT_FAMILY_LIGHT
                f_obj.write(f"{FontTextFamilyDarkVarEnc}")         # FONT_TEXT_FAMILY_DARK
        except:
            print('=== Error ===')

    #//===================================================//
    def createSystemTray(self):
        """
        Creates a system tray icon for the application.
        - Adds a combo box to switch between taskbar icon and main window.
        - Initializes actions and tray icon menu.
        - Connects tray icon events to appropriate handlers.
        """

        print('=== createSystemTray ===')
        # Create a combo box for status selection
        MainGuiWindow.statusComboBox = QComboBox(self)
        self.statusComboBox.setGeometry(650,15,175,25)
        self.statusComboBox.addItem(QIcon(':/resources/icon/app/ocr1.png'), "Taskbar Icon ")
        self.statusComboBox.addItem(QIcon(':/resources/icon/app/ocr2.png'), "MainWindow (working)")
        self.statusComboBox.setVisible(False)
        self.statusComboBox.setMouseTracking(True)

        # Create actions and tray icon
        self.statusComboBox.currentIndexChanged.connect(self.setIconFcn)
        self.createActions()
        self.createTrayIcon()
        self.trayIcon.activated.connect(self.iconActivated)
        self.statusComboBox.setCurrentIndex(1)
        self.trayIcon.show()

    #//===================================================//
    def setIconFcn(self,index):
        """
        Handles the behavior when the status combo box index changes.
        - Hides or shows the main window based on the selected index.
        - Updates the tray icon and tooltip.
        """
        from src.func.py_main_editor import TextGuiWindow
        from src.func.py_main_function import UIFunctions

        if self.statusComboBox.currentIndex() == 0:
            # Close the main window and hide the application
            print('=== Close ===')
            self.hide()
            TextGuiWindow.cancelText1(self)
            try:
                self.TextWindow.close()
            except:
                pass

        elif self.statusComboBox.currentIndex() == 1:
            # Show the main window and update the UI
            print('=== MainWindow ===')
            UIFunctions.printScreen(self)
            UIFunctions.setScreenImage(self)
            # self.createUI()
            self.showNormal()

        # Update the tray icon and tooltip
        icon = self.statusComboBox.itemIcon(index)
        self.trayIcon.setIcon(icon)
        self.setWindowIcon(icon)
        self.trayIcon.setToolTip(self.statusComboBox.itemText(index))

    #//===================================================//
    def iconActivated(self,reason):
        """
        Handles the activation of the system tray icon.
        - Toggles between taskbar icon and main window based on the current index.
        """
        print('=== iconActivated ===')
        # Check the reason for the activation
        if reason in (QSystemTrayIcon.ActivationReason.Trigger, QSystemTrayIcon.ActivationReason.DoubleClick):
            if self.statusComboBox.currentIndex() == 0:
                self.statusComboBox.setCurrentIndex(1)  # Switch to main window
            elif self.statusComboBox.currentIndex() == 1:
                self.statusComboBox.setCurrentIndex(0)  # Switch to taskbar icon

    #//===================================================//
    def createActions(self):
        """
        Creates actions for the system tray menu.
        - Includes actions for OCR screen, settings, help, and exit.
        """
        # Create actions for the tray icon menu
        self.mainAction = QAction("&OCR Screen", self)
        self.mainAction.triggered.connect(self.showNormal)                      # Show the main window
        MainGuiWindow.settingAction = QAction("&Setting", self)
        MainGuiWindow.settingAction.triggered.connect(self.showSettingWindow)   # Show the settings window
        MainGuiWindow.helpAction = QAction("&Help", self)
        MainGuiWindow.helpAction.triggered.connect(self.showHelpWindow)         # Show the help window
        MainGuiWindow.aboutAction = QAction("&About", self)
        MainGuiWindow.aboutAction.triggered.connect(self.showAboutWindow)       # Show the about window
        self.quitAction = QAction("&Exit", self)
        self.quitAction.triggered.connect(self.exitMenuPressed)                 # Exit the application

    #//===================================================//
    def createTrayIcon(self):
        """
        Creates the system tray icon and its context menu.
        - Adds actions to the tray icon menu.
        """
        self.trayIconMenu = QMenu(self)
        self.trayIconMenu.addAction(self.mainAction)
        self.trayIconMenu.addSeparator()
        self.trayIconMenu.addAction(self.settingAction)
        self.trayIconMenu.addAction(self.aboutAction)
        self.trayIconMenu.addAction(self.helpAction)
        self.trayIconMenu.addSeparator()
        self.trayIconMenu.addAction(self.quitAction)

    # Create the tray icon and set its context menu
        MainGuiWindow.trayIcon = QSystemTrayIcon(self)
        self.trayIcon.setContextMenu(self.trayIconMenu)

    #//===================================================//
    def exitMenuPressed(self):
        """
        Handles the exit action from the tray menu.
        - Delays the exit process slightly to ensure proper cleanup.
        """
        print('=== exitMenuPressed ===')
        QTimer.singleShot(150, self.exitProgram)

    #//===================================================//
    def showSettingWindow(self):
        """
        Opens the settings window for the application.
        - Initializes the settings window if it doesn't already exist.
        - Disables the settings action to prevent multiple instances.
        """
        from src.module.py_window_setting import SettingWindow

        print('=== showSettingWindow ===')
        if self.window2 is None:
            self.window2 = SettingWindow()
        self.window2.show()                     # Display the settings window
        self.settingAction.setEnabled(False)

        from src.func.py_main_editor import TextGuiWindow
        try:
            TextGuiWindow.setting_action.setEnabled(False)
            TextGuiWindow.updateEnabled_icon(self)
        except:
            pass

    #//===================================================//
    def showAboutWindow(self):
        """
        Opens the about window for the application.
        - Initializes the about window if it doesn't already exist.
        - Disables the about action to prevent multiple instances.
        """
        from src.module.py_window_about import AboutWindow

        print('=== showAboutWindow ===')
        if self.window7 is None:
            self.window7 = AboutWindow()
        self.window7.show()                     # Display the about window
        self.aboutAction.setEnabled(False)

        from src.module.py_window_setting import SettingWindow
        try:
            SettingWindow.btnAbout.setEnabled(False)
        except:
            pass

    #//===================================================//
    def showHelpWindow(self):
        """
        Opens the help window for the application.
        - Initializes the help window if it doesn't already exist.
        - Disables the help action to prevent multiple instances.
        """
        from src.module.py_window_help import HelpWindow

        print('=== showHelpWindow ===')
        if self.window6 is None:
            self.window6 = HelpWindow()
        self.window6.show()                     # Display the help window
        self.helpAction.setEnabled(False)

        from src.module.py_window_setting import SettingWindow
        try:
            SettingWindow.btnHelp.setEnabled(False)
        except:
            pass

    #//===================================================//
    def setCursorShape(self):
        """
        Sets the cursor shape based on the application's configuration.
        - Supports various cursor shapes such as cross, arrow, target, pointer, and hand.
        """
        print('=== setCursorShape ===')
        if (MainGuiWindow.CursorShapeVar1 == 0):
            self.setCursor(QCursor(Qt.CursorShape.CrossCursor))         # Cross cursor
        elif (MainGuiWindow.CursorShapeVar1 == 1):
            self.setCursor(QCursor(Qt.CursorShape.ArrowCursor))         # Arrow cursor
        elif (MainGuiWindow.CursorShapeVar1 == 2):
            pixmap = QPixmap(':resources/cursor/target.png')
            cursor_sized = pixmap.scaled(QSize(32,32), Qt.AspectRatioMode.KeepAspectRatio)
            cursor = QCursor(cursor_sized,-1,-1)
            self.setCursor(cursor)                          # Target cursor
        elif (MainGuiWindow.CursorShapeVar1 == 3):
            pixmap = QPixmap(':resources/cursor/pointer.png')
            cursor_sized = pixmap.scaled(QSize(32,32), Qt.AspectRatioMode.KeepAspectRatio)
            cursor = QCursor(cursor_sized,12,12)
            self.setCursor(cursor)                          # Pointer cursor
        elif (MainGuiWindow.CursorShapeVar1 == 4):
            self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))  # Hand cursor

    # //===================================================//
    def updateCursor(self):
        """
        Updates the cursor shape globally based on the application's configuration.
        - Overrides the default cursor with the selected shape.
        """
        print('=== updateCursor ===')
        if (MainGuiWindow.CursorShapeVar1 == 0):
            QApplication.setOverrideCursor(QCursor(Qt.CursorShape.CrossCursor))         # Cross cursor
        elif (MainGuiWindow.CursorShapeVar1 == 1):
            QApplication.setOverrideCursor(QCursor(Qt.CursorShape.ArrowCursor))         # Arrow cursor
        elif (MainGuiWindow.CursorShapeVar1 == 2):
            pixmap = QPixmap(':resources/cursor/target.png')
            cursor_sized = pixmap.scaled(QSize(32,32), Qt.AspectRatioMode.KeepAspectRatio)
            cursor = QCursor(cursor_sized,-1,-1)
            QApplication.setOverrideCursor(cursor)                          # Target cursor
        elif (MainGuiWindow.CursorShapeVar1 == 3):
            pixmap = QPixmap(':resources/cursor/pointer.png')
            cursor_sized = pixmap.scaled(QSize(32,32), Qt.AspectRatioMode.KeepAspectRatio)
            cursor = QCursor(cursor_sized,12,12)
            QApplication.setOverrideCursor(cursor)                          # Pointer cursor
        elif (MainGuiWindow.CursorShapeVar1 == 4):
            QApplication.setOverrideCursor(QCursor(Qt.CursorShape.PointingHandCursor))  # Hand cursor

    #//===================================================//
    def setRubberBand(self):
        """
        Initializes a rubber band selection tool for the application.
        - Creates a new rubber band object.
        - Enables mouse tracking for precise selection.
        - Sets the color of the rubber band.
        """
        from src.func.py_main_rubberband import RubberBandNew
        print('=== setRubberBand ===')
        MainGuiWindow.rubberband = RubberBandNew(QRubberBand.Rectangle,self)
        self.rubberband.setObjectName('rubberband')
        self.setMouseTracking(True) # Enable mouse tracking
        self.setRubberBandColor()   # Set the rubber band color

    #//===================================================//
    def setRubberBandColor(self):
        """
        Sets the color of the rubber band selection tool.
        - Applies a color effect to the rubber band based on the application's configuration.
        """
        global color_rubberband, COLOR_RBB

        print('=== setRubberBandColor ===')
        color_rubberband = QGraphicsColorizeEffect()
        color_rubberband.setColor(QColor(MainGuiWindow.RBBColorVar1))  # Set the color
        MainGuiWindow.rubberband.setGraphicsEffect(color_rubberband)   # Apply the color effect

    #//===================================================//
    def setRubberBandThicknessOpacity(self):
        """
        Sets the thickness and opacity of the rubber band selection tool.
        - Retrieves the values from the application's configuration.
        """
        print('=== setRubberBandThicknessOpacity ===')
        MainGuiWindow.THICKNESS_RBB = int(MainGuiWindow.RBBThicknessVar1) # Set the thickness
        MainGuiWindow.OPACITY_RBB_BG = int(MainGuiWindow.RBBOpacityVar1)  # Set the opacity

    #//==========================================================//
    def mousePressEvent(self, event):
        """
        Handles mouse press events.
        - Hides the rubber band selection tool initially.
        - Tracks the origin point of the mouse press.
        - Displays the rubber band for selection.
        - Detects which mouse button was pressed and performs corresponding actions.
        """
        # from src.func.py_main_function import UIFunctions

        print('=== mousePressEvent ===')
        self.rubberband.hide()
        self.origin = self.pic.mapFromParent(event .pos())
        self.rubberband.setGeometry(QtCore.QRect(self.origin, QtCore.QSize()))
        self.rubberband.show()  # Show the rubber band

        # Handle left mouse button click
        if event.buttons() == Qt.MouseButton.LeftButton:
            print('Mouse: Left Click')
            # print('p1: ( %d : %d )' % (event.x(), event.y()))
        # Handle right mouse button click
        if event.buttons() == Qt.MouseButton.RightButton:
            print('Mouse: Right Click')
            self.statusComboBox.setCurrentIndex(0)
        # Handle middle mouse button click
        if event.buttons() == Qt.MouseButton.MidButton:
            print('Mouse: Middle Click')

        # # Close various windows if they are open
        try:
            self.TextWindow.close()  # Close the TextEditor window
            cv2.destroyAllWindows()
        except:
            # print('Error: TextWindow not defined')
            pass

        # Close other windows if they are open
        try:
            self.TextWindow.window2.close()     # SettingWindow
        except:
            pass

        try:
            self.TextWindow.window3.close()     # ColorPicker
        except:
            pass

        try:
            self.TextWindow.window4.close()     # FindReplace
        except:
            pass

        try:
            self.TextWindow.window5.close()     # Tutorial
        except:
            pass

        try:
            self.TextWindow.window6.close()     # Help
        except:
            pass

        try:
            self.TextWindow.window7.close()     # About
        except:
            pass

    #//==========================================================//
    def mouseMoveEvent(self, event):
        """
        Handles mouse move events.
        - Restores the default cursor when no button is pressed.
        - Updates the rubber band geometry when the left mouse button is pressed.
        - Logs a message when dragging with the right mouse button.
        """
        QApplication.restoreOverrideCursor()

        if event.buttons() == QtCore.Qt.MouseButton.NoButton:
            pass
        elif event.buttons() == QtCore.Qt.MouseButton.LeftButton:
            rect = self.rubberband.geometry()
            if self.rubberband.isVisible():
                # Update the rubber band geometry based on the mouse position
                self.rubberband.setGeometry(QtCore.QRect(self.origin, event .pos()) & self.image.rect())
        elif event.buttons() == QtCore.Qt.MouseButton.RightButton:
            print("=== Drag: Right click ===")

    #//==========================================================//
    def mouseReleaseEvent(self, event):
        """
        Handles mouse release events.
        - Captures the selected region using the rubber band.
        - Processes the selected image with various image processing techniques.
        - Displays the processed images based on user settings.
        """

        from src.func.py_main_function import UIFunctions
        from src.func.py_main_image_processing import UIFunctionsImage

        print("=== mouseReleaseEvent (begin) ===")
        time_start = time.time()  # Start timing the event

        # print('p2: ( %d : %d )' % (event.x(), event.y()))
        rect = self.rubberband.geometry()
        self.dragPos = event.globalPos()  # Store the global position of the release

        if rect.width() > 10 and rect.height() > 10:
            self.setCursor(Qt.CursorShape.WaitCursor)
            self.selectedImage = UIFunctionsImage.cropImage(self, rect)                 # Crop the selected region (grayscale image)
            self.selectedImage_BGR = UIFunctionsImage.cropImage(self, rect)             # Crop the selected region (BGR image)
            self.image1 = UIFunctionsImage.convertCv2ToQimage(self, self.selectedImage_BGR)   # Convert to QImage
            self.selectedImage1 = UIFunctionsImage.convertQImageToMat(self, self.image1)      # Convert to RGB image

            print("=== IMAGE PROCESSING (begin) ===")
            from src.func.py_main_image_processing import UIFunctionsImage

            # Display the original images if enabled
            if MainGuiWindow.DisplayColorImageVar1 == 1:
                cv2.imshow('Original Color Image',self.selectedImage1)  # Display RGB image

            if MainGuiWindow.DisplayGrayImageVar1 == 1:
                cv2.imshow('Original Gray Image',self.selectedImage)  # Display grayscale image

            # Detect and correct image orientation
            global FLAG_IMAGE_ROTATE0, FLAG_IMAGE_ROTATE90, FLAG_IMAGE_ROTATE180
            global angle_detection
            angle_detection = UIFunctions.detect_orientation(self, self.selectedImage)

            if (angle_detection == 90):  # Rotate 90 degrees clockwise
                FLAG_IMAGE_ROTATE0 = False
                FLAG_IMAGE_ROTATE90 = True
                FLAG_IMAGE_ROTATE180 = False
                angle_correction = -90
                # angle = -45
            elif (angle_detection == 180):  # Rotate 180 degrees
                FLAG_IMAGE_ROTATE0 = False
                FLAG_IMAGE_ROTATE90 = False
                FLAG_IMAGE_ROTATE180 = True
                angle_correction = 180
            elif (angle_detection == 270):  # Rotate 90 degrees counterclockwise
                FLAG_IMAGE_ROTATE0 = False
                FLAG_IMAGE_ROTATE90 = True
                FLAG_IMAGE_ROTATE180 = False
                angle_correction = 90
            else:  # No rotation needed
                FLAG_IMAGE_ROTATE0 = True
                FLAG_IMAGE_ROTATE90 = False
                FLAG_IMAGE_ROTATE180 = False
                angle_correction = angle_detection

            # Check the optimization setting and apply the corresponding image processing
            if (OptimizationVar1 == 0):  # Standard optimization
                print('=== Optimization: Standard ===')

            elif (OptimizationVar1 == 1):  # Speed optimization
                print('=== Optimization: Speed ===')
                # Resize the image to 80% of its original size for faster processing
                self.selectedImage = UIFunctionsImage.resize_image(self, self.selectedImage,80)

            elif (OptimizationVar1 == 2):  # Accuracy optimization
                print('=== Optimization: Accuracy ===')
                # Enhance image contrast for better accuracy
                self.selectedImage = UIFunctionsImage.contrast_high1(self, self.selectedImage)
                # Sharpen the image to improve text clarity
                self.selectedImage = UIFunctionsImage.sharpen2(self, self.selectedImage,9)
                # Apply denoising to reduce background noise
                self.selectedImage = UIFunctionsImage.denoising_fast(self, self.selectedImage,FilteringBackgroundNoiseIntVar1,7,21)

            # Check if auto-rotate is enabled and apply rotation based on detected orientation
            if (PageLayoutAutoRotatePageVar1 == 1):
                print('=== rotatePage ===')

                if FLAG_IMAGE_ROTATE0:  # No rotation needed
                    if MainGuiWindow.DisplayProcessedAllImageVar1 == 1:
                        cv2.imshow('Auto-Rotate Page', self.selectedImage)
                if FLAG_IMAGE_ROTATE90:  # Rotate 90 degrees clockwise
                    self.selectedImage = UIFunctionsImage.rotate_image_deg1(self, self.selectedImage,angle_correction)
                    if MainGuiWindow.DisplayProcessedAllImageVar1 == 1:
                        cv2.imshow('Auto-Rotate Page', self.selectedImage)
                if FLAG_IMAGE_ROTATE180:  # Rotate 180 degrees
                    self.selectedImage = UIFunctionsImage.rotate_image180(self, self.selectedImage)
                    if MainGuiWindow.DisplayProcessedAllImageVar1 == 1:
                        cv2.imshow('Auto-Rotate Page', self.selectedImage)

            # Check if deskewing is enabled and apply deskewing to correct image alignment
            if (PageLayoutDeskewVar1 == 1):
                print('=== deskew ===')
                try:
                    # Detect the skew angle of the image
                    angle_deskew = UIFunctionsImage.deskew_angle(self, self.selectedImage)
                    if (abs(angle_deskew) <= 45):  # Apply deskewing for small angles
                        self.selectedImage = UIFunctionsImage.deskew(self, self.selectedImage,angle_deskew)
                    elif (abs(angle_deskew) > 45):  # Handle larger angles with additional processing
                        self.selectedImage = UIFunctionsImage.bordermake_image(self, self.selectedImage)
                        self.selectedImage = UIFunctionsImage.deskew(self, self.selectedImage,angle_deskew)
                        self.selectedImage = UIFunctionsImage.crop_image(self, self.selectedImage,8,6)
                    if MainGuiWindow.DisplayProcessedAllImageVar1 == 1:
                        cv2.imshow('Auto-Deskew',self.selectedImage)
                except:
                    pass

            # Check if color inversion is enabled and apply it
            if (LayoutInvertColorVar1 == 1):
                print('=== inverting ===')
                self.selectedImage = UIFunctionsImage.inverting(self, self.selectedImage)
                if MainGuiWindow.DisplayProcessedAllImageVar1 == 1:
                    cv2.imshow('Invert Color',self.selectedImage)

            # Apply Otsu's thresholding if enabled
            if (LayoutThresholdVar1 == 1):
                print('=== threshold_otsu ===')
                thres, self.selectedImage = UIFunctionsImage.threshold_otsu(self, self.selectedImage)
                if MainGuiWindow.DisplayProcessedAllImageVar1 == 1:
                    cv2.imshow('Threshold Binary',self.selectedImage)

            # Apply adaptive thresholding if enabled
            if (LayoutThresholdAdaptiveVar1 == 1):
                print('=== threshold_adaptive ===')
                self.selectedImage = UIFunctionsImage.threshold_adaptive(self, self.selectedImage,21,7)
                self.selectedImage = UIFunctionsImage.inverting(self, self.selectedImage)
                if MainGuiWindow.DisplayProcessedAllImageVar1 == 1:
                    cv2.imshow('Threshold Adaptive',self.selectedImage)

            # Apply custom thresholding if enabled
            if (FilteringThresholdVar1 == 1):
                print('=== threshold ===')
                thres, self.selectedImage = UIFunctionsImage.thresholdFcn(self, self.selectedImage,FilteringThresholdLowerIntVar1,FilteringThresholdUpperIntVar1)
                if MainGuiWindow.DisplayProcessedAllImageVar1 == 1:
                    cv2.imshow('Threshold',self.selectedImage)

            # Remove underlines if enabled
            if (PageLayoutRemoveUnderlineVar1 == 1):
                print('=== remove_lines1 ===')
                self.selectedImage = UIFunctionsImage.remove_lines1(self, self.selectedImage,15)
                if MainGuiWindow.DisplayProcessedAllImageVar1 == 1:
                    cv2.imshow('Remove UnderLines',self.selectedImage)

            # Remove tables if enabled
            if (PageLayoutRemoveTableVar1 == 1):
                print('=== remove_table1 ===')
                self.selectedImage = UIFunctionsImage.remove_table1(self, self.selectedImage,25)
                if MainGuiWindow.DisplayProcessedAllImageVar1 == 1:
                    cv2.imshow('Remove Tables',self.selectedImage)

            # Remove watermarks if enabled
            if (PageLayoutRemoveWatermarkVar1 == 1):
                print('=== remove_watermark ===')
                self.selectedImage = UIFunctionsImage.remove_watermark2(self, self.selectedImage)
                if MainGuiWindow.DisplayProcessedAllImageVar1 == 1:
                    cv2.imshow('Remove Watermark',self.selectedImage)

            # Enhance contrast if enabled
            if (LayoutContrastVar1 == 1):
                print('=== contrast_high ===')
                self.selectedImage = UIFunctionsImage.contrast_high1(self, self.selectedImage)
                if MainGuiWindow.DisplayProcessedAllImageVar1 == 1:
                    cv2.imshow('High Contrast',self.selectedImage)

            # Apply sharpening if enabled
            if (LayoutSharpenVar1 == 1):
                print('=== sharpen2 ===')
                self.selectedImage = UIFunctionsImage.sharpen2(self, self.selectedImage,9)
                if MainGuiWindow.DisplayProcessedAllImageVar1 == 1:
                    cv2.imshow('Sharpen',self.selectedImage)

            # Apply despeckling if enabled
            if (LayoutDespeckleVar1 == 1):
                print('=== denoising_fast ===')
                self.selectedImage = UIFunctionsImage.denoising_fast(self, self.selectedImage,15,7,21)
                if MainGuiWindow.DisplayProcessedAllImageVar1 == 1:
                    cv2.imshow('Despeckle',self.selectedImage)

            # Apply background noise filtering if enabled
            if (FilteringBackgroundNoiseVar1 == 1):
                print('=== denoise ===')
                self.selectedImage = UIFunctionsImage.denoising_fast(self, self.selectedImage,FilteringBackgroundNoiseIntVar1,7,21)
                if MainGuiWindow.DisplayProcessedAllImageVar1 == 1:
                    cv2.imshow('Background Noise',self.selectedImage)

            # Apply text noise filtering if enabled
            if (FilteringTextNoiseVar1 == 1):
                print('=== closing ===')
                self.selectedImage = UIFunctionsImage.closing(self, self.selectedImage, FilteringTextNoiseIntVar1)
                if MainGuiWindow.DisplayProcessedAllImageVar1 == 1:
                    cv2.imshow('Text Noise',self.selectedImage)

            # Apply text erosion if enabled
            if (FilteringTextErosionVar1 == 1):
                print('=== erode ===')
                self.selectedImage = UIFunctionsImage.inverting(self, self.selectedImage)
                self.selectedImage = UIFunctionsImage.erodeFcn(self, self.selectedImage, FilteringTextErosionIntVar1)
                self.selectedImage = UIFunctionsImage.inverting(self, self.selectedImage)
                if MainGuiWindow.DisplayProcessedAllImageVar1 == 1:
                    cv2.imshow('Text Erosion',self.selectedImage)

            # Apply text dilation if enabled
            if (FilteringTextDilationVar1 == 1):
                print('=== dilate ===')
                self.selectedImage = UIFunctionsImage.inverting(self, self.selectedImage)
                self.selectedImage = UIFunctionsImage.dilateFcn(self, self.selectedImage, FilteringTextDilationIntVar1)
                self.selectedImage = UIFunctionsImage.inverting(self, self.selectedImage)
                if MainGuiWindow.DisplayProcessedAllImageVar1 == 1:
                    cv2.imshow('Text Dilation',self.selectedImage)

            # Display the final processed image if enabled
            if MainGuiWindow.DisplayProcessedImageVar1 == 1:
                cv2.imshow('Final Processed Image',self.selectedImage)

            print("=== IMAGE PROCESSING (end) ===")

            # Perform OCR on the processed image
            UIFunctions.detect_text_ocr(self,self.selectedImage)
            UIFunctions.show_text_ocr(self)

        # Reset the cursor to its default shape and hide the rubber band
        self.setCursorShape()
        self.rubberband.hide()

        # Log the time taken for the mouse release event
        time_end = time.time()
        print("*** mouseReleaseEvent (end): %0.3f seconds ***" %(time_end - time_start))  # Print the elapsed time

    #//===================================================//
    def mouseDoubleClickEvent(self, event):
        """
        Handles mouse double-click events.
        """
        from src.module.py_window_setting import SettingWindow

        print("=== mouseDoubleClick ===")
        QApplication.restoreOverrideCursor()  # Restore the default cursor
        self.doubleClicked.emit()  # Emit the double-click signal
        self.showSettingWindow()  # Open the settings window

    #//===================================================//
    def paintEvent(self, event):
        """
        Handles paint events.
        """
        super().paintEvent(event)

    #//==========================================================//
    def keyPressEvent(self, event):
        """
        Handles key press events.
        - Detects specific key presses (e.g., Enter, Escape) and performs corresponding actions.
        """
        print('=== keyPressEvent ===')
        if (str(event.key()) == '16777220'):  # Key Enter
            print('=== Enter ===')
        elif (event.key() == Qt.Key.Key_Escape):  # Key Escape
            print('=== Esc ===')
            self.statusComboBox.setCurrentIndex(0)  # Reset the status combo box

    # //===================================================//
    def enterEvent(self, event):
        """
        Handles mouse enter events.
        """
        super().enterEvent(event)

    # //===================================================//
    def leaveEvent(self, event):
        """
        Handles mouse leave events.
        """
        QApplication.restoreOverrideCursor()  # Restore the default cursor

########################################################################
def setup_system():
    """
    Check and setup the system environment and verifies the installation of required components.
    This function ensures that Python, dependencies, and Tesseract OCR are properly installed
    and configured for the application to function correctly.
    """
    import src.config.py_config_tesseract as py_config_tesseract
    print("=== setup_system ===")
    check_os()  # Check if the operating system is compatible
    check_python_version()  # Check if the Python version is compatible
    check_dependencies()  # Check if all required dependencies are installed
    py_config_tesseract.check_tesseract()  # Check if the Tesseract OCR installation is valid

# //===================================================//
def check_os():
    """
    Checks the operating system to ensure compatibility with the application.
    This function verifies that the application is running on a supported operating system.
    """

    print("=== check_os ===")
    # Check if the operating system is Windows or Linux or MacOS
    os_name = platform.system()
    if os_name == "Windows":
        print("Operating System is compatible.")  # Windows operating system
    elif os_name == "Linux":
        print("This app is currently not supported on Linux.")  # Linux operating system
        sys.exit(1)
    elif os_name == "Darwin":
        print("This app is currently not supported on macOS.")  # macOS operating system
        sys.exit(1)
    else:
        print("This app is currently not supported on this operating system.")  # Unsupported operating system
        sys.exit(1)

# //===================================================//
def check_python_version():
    """
    Checks the Python version to ensure compatibility with the application.
    This function verifies that the installed Python version meets the minimum requirements
    for running the application.
    """

    print("=== check_python_version ===")
    # Get the current Python version
    python_version = sys.version_info
    # print("Python version:", python_version)

    if python_version < (3, 10):
        print("Python version is below the minimum required version (3.10).")
        sys.exit(1)
    else:
        print("Python version is compatible.")
        # print("Python version:", python_version[0], python_version[1], python_version[2])  # Print major, minor, and micro versions

# //===================================================//
def check_dependencies():
    """
    Checks for the installation of required dependencies.
    """

    print("=== check_dependencies ===")

    # Get current dependency list from current environment
    current_dependencies = sys.modules.keys()
    # print("Current dependencies:", current_dependencies)  # Debugging line to check all current dependencies

    # List of required dependencies
    required_dependencies = [
        "numpy", "opencv-python", "pynput", "pyautogui", "PyQt5",
        "pytesseract", "pywin32", "openpyxl", "pandas"
    ]

    # Check if each dependency is installed
    for current_dependencies in required_dependencies:
        # if all dependencies are installed, print a message
        if current_dependencies == required_dependencies[-1]:
            # Check if all dependencies are installed
            print("All required dependencies are installed.")
        else:
            # Check if the current dependency is in the list of current dependencies
            if current_dependencies in current_dependencies:
                # print(f"{current_dependencies} is already installed.")
                pass
            else:
                # Print a message if the current dependency is not installed
                print(f"{current_dependencies} is not installed. Please install it using pip.")

# //===================================================//
def initialize_app():
    """
    Initializes the application environment and sets up global variables.
    This function configures the application paths, creates necessary directories,
    and initializes the QApplication instance.
    """
    from src.config.py_config import FOLDERNAME1, DESKTOP_FOLDER, DOCUMENTS_FOLDER

    # Define paths for desktop and documents directories
    path_desktop = str(Path.home()/DESKTOP_FOLDER).replace('\\','/')
    path_documents = path_desktop.replace(DESKTOP_FOLDER,DOCUMENTS_FOLDER)
    path_foldernew1 = path_documents + '/' + FOLDERNAME1
    Path(path_foldernew1).mkdir(parents=True,exist_ok=True)
    # print('path_FOLDERNAME1 := ', path_foldernew1)
    return path_foldernew1, path_documents

# //===================================================//
def check_lock_file(lock_file_path):
    """
    Checks for the existence of a lock file to prevent multiple instances of the application.
    """
    # Check for lock file and handle multiple instances
    lock_file = QLockFile(lock_file_path)  # Create a lock file to prevent multiple instances
    return lock_file.tryLock()

######################################################################
def launch_gui():
    """
    Entry point for the application.
    - Initializes global variables and paths for the application.
    - Configures the application environment and system tray functionality.
    - Ensures only one instance of the application runs using a lock file mechanism.
    """
    from src.config.py_config import LOCK_FILE_NAME
    global app
    global Main1Window
    global path_documents
    print("=== launch_gui ===")
    time_start = time.time()  # Start timing the application initialization

    path_foldernew1, path_documents = initialize_app()  # Initialize the application environment and paths
    app = QApplication(sys.argv)  # Create a QApplication instance

    lock_file_path = path_foldernew1 + '/' + LOCK_FILE_NAME  # Define the lock file path
    lock_file = check_lock_file(lock_file_path)

    if lock_file:
        # Check if the system tray is available
        if not QSystemTrayIcon.isSystemTrayAvailable():
            QMessageBox.critical(None, "Systray", "Error: couldn't detect system tray on this system.")
            sys.exit(1)

        QApplication.setQuitOnLastWindowClosed(False)
        Main1Window = MainGuiWindow()  # Create the main GUI window
        Main1Window.hotkeyFcn()  # Set up global hotkeys
        time_end = time.time()  # End timing the application initialization
        print("*** launch_gui : %0.3f seconds ***" %(time_end - time_start))  # Log the initialization time
        sys.exit(app.exec_())
    else:
        # If another instance is already running, display an error message
        error_message = QMessageBox()
        # QApplication.setAttribute(Qt.AA_DontShowIconsInMenus)
        pixmap = QPixmap(32,32)  # Create a transparent pixmap for the window icon
        pixmap.fill(Qt.GlobalColor.transparent)
        error_message.setWindowIcon(QIcon(pixmap))  # Set the window icon
        error_message.setIcon(QMessageBox.Information)  # Set the icon to an information icon
        error_message.setWindowFlags(Qt.WindowFlags.Dialog | Qt.WindowFlags.WindowCloseButtonHint | Qt.WindowFlags.WindowStaysOnTopHint)  # Configure window flags
        error_message.setStandardButtons(QMessageBox.Ok)
        error_message.setWindowTitle("CubeOCR")
        error_message.setText('<p style="font-size: 12px;"> Press <b>Ctrl+Alt</b> to activate OCR screen<br> </p>')
        error_message.exec()  # Display the error message

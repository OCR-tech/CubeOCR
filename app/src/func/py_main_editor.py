# Import necessary modules
from pathlib import Path
import os
import pytesseract

# Import GUI-related modules and configurations
from src.module.py_window_main import *
from src.module.py_window_main import WIDTH, HEIGHT
from src.module.py_window_main import x0Pos, y0Pos
from src.config.py_config import FONT_TEXT_SIZE_MIN, FONT_TEXT_SIZE_MAX, FONT_TEXT_SIZE_INIT, FONT_TEXT_FAMILY_INIT, FONT_TEXT_INDEX_MAX, FONT_TEXT_INDEX_MIN
from src.config.py_config import OPACITY_TEXT_MIN, OPACITY_TEXT_MAX
from src.config.py_config import FLAG_SELECTALL, FLAG_MAXIMIZE, FLAG_FONT_INIT, FLAG_SAVEPATH_INIT
from src.config.py_config import FILENAME1, FILENAME2, FILENUM
from src.config.py_config_tesseract import path_tesseract_cmd
from src.resource.resources_rc import *

# Set the Tesseract OCR command path
pytesseract.pytesseract.tesseract_cmd = path_tesseract_cmd

# Define constants for UI element heights
HEIGHT_TT = 30      # Height_Titlebar
HEIGHT_TB = 30      # Height_Toolbar
HEIGHT_LB = 30      # Height_Layoutbar
HEIGHT_FB = 30      # Height_Formatbar
HEIGHT_SB = 10      # Height_Statusbar

# Define the main class for the text editor window
class TextGuiWindow(QMainWindow):
    """
    The TextGuiWindow class serves as the main window for the text editor application.
    It initializes the user interface, manages layouts, widgets, and shortcuts, and provides
    functionality for text editing, formatting, and theme management.
    """
    def __init__(self):
        # Initialize the QMainWindow
        QMainWindow.__init__(self)
        self.initUI()


    def initUI(self):
        from src.module.py_window_main import MainGuiWindow
        from src.module.py_window_main import WIDTH1

        global w1,h1
        global FILENAME1
        global font

        print('=== TextGuiWindow (initUI) (begin) ===')
        # Initialize variables for additional windows and file paths
        self.window2 = None                     # SettingWindow
        self.window3 = None                     # ColorPickerWindow
        self.window4 = None                     # FindReplace
        self.path = None                        # save file

        # Create the main window widget
        self.window = QWidget()                 # SettingWindow()

        # Set window flags and attributes for a frameless, translucent window
        self.setWindowFlags(Qt.Window | Qt.WindowType.FramelessWindowHint) # type: ignore
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setObjectName("TextWindow")

        # Adjust minimum width based on icon size
        if (MainGuiWindow.TextEditorIconSizeVar1 == 16):
            MainGuiWindow.WIDTH1_MIN = int(0.220*WIDTH1)
        elif (MainGuiWindow.TextEditorIconSizeVar1 == 18):
            MainGuiWindow.WIDTH1_MIN = int(0.235*WIDTH1)
        elif (MainGuiWindow.TextEditorIconSizeVar1 == 22):
            MainGuiWindow.WIDTH1_MIN = int(0.270*WIDTH1)

         # Set up keyboard shortcuts for various actions
        self.shortcut2 = QShortcut(QKeySequence("Ctrl+t"),self)
        self.shortcut3 = QShortcut(QKeySequence("Ctrl+r"),self)
        self.shortcut4 = QShortcut(QKeySequence("Ctrl+-"),self)
        self.shortcut5 = QShortcut(QKeySequence("Ctrl++"),self)
        self.shortcut6 = QShortcut(QKeySequence("Ctrl+["),self)
        self.shortcut7 = QShortcut(QKeySequence("Ctrl+]"),self)
        self.shortcut8 = QShortcut(QKeySequence("Ctrl+e"),self)
        self.shortcut10 = QShortcut(QKeySequence("Ctrl+g"),self)
        self.shortcut11 = QShortcut(QKeySequence("Ctrl+w"),self)
        self.shortcut12 = QShortcut(QKeySequence("Ctrl+n"),self)

        # Connect shortcuts to their respective functions
        self.shortcut2.activated.connect(self.toggleTheme)
        self.shortcut3.activated.connect(self.resetSetting)
        self.shortcut4.activated.connect(self.decreaseTextSize)
        self.shortcut5.activated.connect(self.increaseTextSize)
        self.shortcut6.activated.connect(self.decreaseOpacity)
        self.shortcut7.activated.connect(self.increaseOpacity)
        self.shortcut8.activated.connect(self.settingConfig)
        self.shortcut10.activated.connect(self.showColorPicker)
        self.shortcut11.activated.connect(self.toggleToolbar)
        self.shortcut12.activated.connect(self.setTextFont)

        # Initialize the horizontal layout for the title bar
        self.hboxWindow1 = QHBoxLayout()
        self.hboxWindow1.setContentsMargins(0,0,0,0)
        self.hboxWindow1.setSpacing(0)

        # Create a draggable window widget for the title bar
        TextGuiWindow.WidgetWindow = WindowDragger(self)
        self.WidgetWindow.setObjectName('WidgetWindow')
        self.WidgetWindow.setContentsMargins(0,0,0,0)
        self.WidgetWindow.setFixedHeight(HEIGHT_TT)

        # Create the main window container
        TextGuiWindow.windowMain = QMainWindow()
        self.windowMain.setObjectName('windowMain')
        self.windowMain.setContentsMargins(0,0,0,0)

        # Add a QLabel to act as the frame for the title bar
        TextGuiWindow.labelWindowFrame = QLabel(self)
        self.labelWindowFrame.setObjectName('labelw1')
        self.labelWindowFrame.setFixedHeight(HEIGHT_TT)
        self.labelWindowFrame.setContentsMargins(0,0,0,0)
        self.hboxWindow1.addWidget(self.labelWindowFrame)
        self.WidgetWindow.setLayout(self.hboxWindow1)

        # Create a QLabel for the main content area
        TextGuiWindow.windowContentMain = QLabel()
        self.windowContentMain.setObjectName('labelw2')
        self.windowContentMain.setContentsMargins(0,0,0,0)

        # Initialize a vertical layout for the main widget
        self.vboxWidgetWindow = QVBoxLayout()
        self.vboxWidgetWindow.setContentsMargins(0,0,0,0)

        # Initialize another vertical layout for additional content
        self.vbox1 = QVBoxLayout()
        self.vbox1.setContentsMargins(0,0,0,0)
        self.vbox1.setSpacing(0)
        self.vbox1.addWidget(self.windowContentMain)

        # Create a container widget for the main content
        TextGuiWindow.container1 = QWidget()
        self.container1.setObjectName('container1')
        self.container1.setLayout(self.vbox1)

        # Set the central widget for the main window
        self.windowMain.setCentralWidget(self.container1)

        # Add the title bar and main content to the vertical layout
        self.vboxWidgetWindow.addWidget(self.WidgetWindow)
        self.vboxWidgetWindow.setSpacing(0)
        self.vboxWidgetWindow.addWidget(self.windowMain)

        # Create a container widget for the entire window
        TextGuiWindow.containerMain = QWidget()
        self.containerMain.setObjectName('containerMain')
        self.containerMain.setLayout(self.vboxWidgetWindow)
        self.setCentralWidget(self.containerMain)

        # Initialize the status bar
        TextGuiWindow.statusBar = QStatusBar(self)
        self.statusBar.setObjectName('sb1')
        self.statusBar.setFixedHeight(20)
        self.setStatusBar(self.statusBar)
        self.statusBar.setSizeGripEnabled(True)

        # Initialize additional layouts for organizing UI elements
        self.layout1 = QVBoxLayout()
        self.layout1.setContentsMargins(0,0,0,0)
        self.layout1.setSpacing(0)

        self.layout2 = QHBoxLayout()
        self.layout3 = QHBoxLayout()
        self.layout7 = QHBoxLayout()
        self.layout8 = QHBoxLayout()
        self.layout9 = QHBoxLayout()

        self.layout1.addLayout(self.layout2,0)
        self.layout1.addLayout(self.layout3,0)
        self.layout1.addLayout(self.layout7,0)
        self.layout1.addLayout(self.layout8,0)
        self.layout1.addLayout(self.layout9,0)

        self.layout1.setContentsMargins(0,0,0,0)
        self.layout2.setContentsMargins(0,0,0,0)
        self.layout3.setContentsMargins(0,0,0,0)
        self.layout7.setContentsMargins(0,0,0,0)
        self.layout8.setContentsMargins(0,0,0,0)
        self.layout9.setContentsMargins(0,0,0,0)

        # Call functions to initialize the text box and other UI elements
        self.resizeTextbox()
        self.updateTextbox()
        self.ModernWindow()

        # Show toolbars, layout bars, format bars, and status bars
        self.showToolBars()
        self.showLayoutBars()
        self.showFormatBars()
        # self.showStatusBars()
        self.showTabSpaces()

        # Configure toolbar visibility based on settings
        if (MainGuiWindow.FLAG_TOOLBAR):
            self.toolbar.setVisible(True)

            if (MainGuiWindow.FLAG_FORMATBAR):
                self.layoutbar.setVisible(True)
                self.formatbar.setVisible(True)
            else:
                self.layoutbar.setVisible(False)
                self.formatbar.setVisible(False)

            self.label1.setFixedHeight(2)
            self.label2.setFixedHeight(5)
            self.label5.setFixedHeight(2)

            # Configure text size and opacity actions based on the theme
            if MainGuiWindow.THEME == "light":
                if (MainGuiWindow.FONT_TEXT_SIZE_LIGHT == FONT_TEXT_SIZE_MIN):
                    self.decrease_textsize_action.setEnabled(False)
                    self.increase_textsize_action.setEnabled(True)
                elif (MainGuiWindow.FONT_TEXT_SIZE_LIGHT == FONT_TEXT_SIZE_MAX):
                    self.decrease_textsize_action.setEnabled(True)
                    self.increase_textsize_action.setEnabled(False)
                else:
                    self.decrease_textsize_action.setEnabled(True)
                    self.increase_textsize_action.setEnabled(True)

                if MainGuiWindow.OPACITY_TEXT_LIGHT == 1:
                    self.increase_opacity_action.setEnabled(False)
                    self.decrease_opacity_action.setEnabled(True)
                elif MainGuiWindow.OPACITY_TEXT_LIGHT == 0.005:
                    self.decrease_opacity_action.setEnabled(False)
                    self.increase_opacity_action.setEnabled(True)
                else:
                    self.increase_opacity_action.setEnabled(True)
                    self.decrease_opacity_action.setEnabled(True)

            elif MainGuiWindow.THEME == "dark":
                if (MainGuiWindow.FONT_TEXT_SIZE_DARK == FONT_TEXT_SIZE_MIN):
                    self.decrease_textsize_action.setEnabled(False)
                    self.increase_textsize_action.setEnabled(True)
                elif (MainGuiWindow.FONT_TEXT_SIZE_DARK == FONT_TEXT_SIZE_MAX):
                    self.decrease_textsize_action.setEnabled(True)
                    self.increase_textsize_action.setEnabled(False)

                if MainGuiWindow.OPACITY_TEXT_DARK == 1:
                    self.increase_opacity_action.setEnabled(False)
                    self.decrease_opacity_action.setEnabled(True)
                elif MainGuiWindow.OPACITY_TEXT_DARK == 0.005:
                    self.decrease_opacity_action.setEnabled(False)
                    self.increase_opacity_action.setEnabled(True)
                else:
                    self.increase_opacity_action.setEnabled(True)
                    self.decrease_opacity_action.setEnabled(True)

            self.updateEnabled_icon()

        else:
            self.toolbar.setVisible(False)
            self.layoutbar.setVisible(False)
            self.formatbar.setVisible(False)
            self.label1.setFixedHeight(5)
            self.label2.setFixedHeight(2)
            self.label5.setFixedHeight(2)

        # Configure status bar visibility based on settings
        if (MainGuiWindow.FLAG_STATUSBAR):
            self.labelStatusbar1.setVisible(True)
            self.labelStatusbar2.setVisible(True)
            self.labelStatusbar3.setVisible(True)
        else:
            self.labelStatusbar1.setVisible(False)
            self.labelStatusbar2.setVisible(False)
            self.labelStatusbar3.setVisible(False)

        # Set the theme and connect text box signals
        self.setThemeFcn()
        self.textbox.selectionChanged.connect(self.textSelectionChanged)
        self.textbox.copyAvailable.connect(self.copyText)
        self.textbox.textChanged.connect(self.textChangedFcn)
        self.textbox.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        print('=== TextGuiWindow (initUI) (end) ===')



    #/===================================================//
    def ModernWindow(self):
        """
        Set up the ModernWindow functionality for the text editor window.
        This includes initializing the title bar, and configuring buttons for minimize, maximize, restore, and close actions.
        """

        print("=== ModernWindow ===")

        # Set size policy for buttons
        spButtons = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        # Initialize the toolbar toggle buttons
        TextGuiWindow.btnToggleToolbar1 = QToolButton()
        self.btnToggleToolbar1.setObjectName('btn3')
        self.btnToggleToolbar1.setSizePolicy(spButtons)
        self.btnToggleToolbar1.clicked.connect(self.toggleToolbar)

        TextGuiWindow.btnToggleToolbar2 = QToolButton()
        self.btnToggleToolbar2.setObjectName('btn4')
        self.btnToggleToolbar2.setSizePolicy(spButtons)
        self.btnToggleToolbar2.clicked.connect(self.toggleToolbar)

       # Initialize the theme toggle button
        TextGuiWindow.btnToggleTheme = QToolButton()
        self.btnToggleTheme.setObjectName('btn5')
        self.btnToggleTheme.setSizePolicy(spButtons)
        self.btnToggleTheme.clicked.connect(self.toggleTheme)

        # Initialize the minimize button
        TextGuiWindow.btnMinimize = QToolButton()
        self.btnMinimize.setObjectName('btnMinimize')
        self.btnMinimize.setSizePolicy(spButtons)

        # Initialize the restore button (hidden by default)
        TextGuiWindow.btnRestore = QToolButton()
        self.btnRestore.setObjectName('btnRestore')
        self.btnRestore.setSizePolicy(spButtons)
        self.btnRestore.setVisible(False)

        # Initialize the maximize button
        TextGuiWindow.btnMaximize = QToolButton()
        self.btnMaximize.setObjectName('btnMaximize')
        self.btnMaximize.setSizePolicy(spButtons)

        # Initialize the close button
        TextGuiWindow.btnClose = QToolButton()
        self.btnClose.setObjectName('btnClose')
        self.btnClose.setSizePolicy(spButtons)

        # Initialize the title label for buttons
        TextGuiWindow.labelTitleButton = QLabel(self)
        self.labelTitleButton.setObjectName('labelTitleButton')

        # Initialize the "OK" button
        TextGuiWindow.btnOK1 = QToolButton(self.labelTitleButton)
        self.btnOK1.setText('OK')
        self.btnOK1.setObjectName('btn1')
        self.btnOK1.setGeometry(8,5,65,17)
        self.btnOK1.setSizePolicy(spButtons)
        self.btnOK1.clicked.connect(self.acceptText1)
        self.btnOK1.clicked.connect(self.closeWindow)

        # Initialize the "Continue" button
        TextGuiWindow.btnContinue1 = QToolButton(self.labelTitleButton)
        self.btnContinue1.setText('Continue')
        self.btnContinue1.setObjectName('btn2')
        self.btnContinue1.setGeometry(83,5,65,17)
        self.btnContinue1.setSizePolicy(spButtons)
        self.btnContinue1.clicked.connect(self.saveText1)
        self.btnContinue1.clicked.connect(self.closeWindow)

        # Set up the layout for the title bar
        self.hboxTitle1 = QHBoxLayout(self.labelWindowFrame)
        self.hboxTitle1.setContentsMargins(0,0,0,0)
        self.hboxTitle1.setSpacing(0)
        self.hboxTitle1.addWidget(self.labelTitleButton)

        # Set up the layout for the title buttons
        self.hboxTitle2 = QHBoxLayout(self.labelTitleButton)
        self.hboxTitle2.setContentsMargins(0,0,0,0)
        self.hboxTitle2.setSpacing(6)

        # Add buttons to the title bar layout
        self.hboxTitle2.addWidget(self.btnToggleToolbar1)
        self.hboxTitle2.addWidget(self.btnToggleToolbar2)
        self.hboxTitle2.addWidget(self.btnToggleTheme)
        self.hboxTitle2.addWidget(self.btnMinimize)
        self.hboxTitle2.addWidget(self.btnRestore)
        self.hboxTitle2.addWidget(self.btnMaximize)
        self.hboxTitle2.addWidget(self.btnClose)
        self.hboxTitle2.addSpacing(8)
        self.hboxTitle2.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignRight)
        # self.labelStatusbar3.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignRight)

        # Adjust visibility of toolbar toggle buttons based on the toolbar state
        if (MainGuiWindow.FLAG_TOOLBAR):
            self.btnToggleToolbar2.setVisible(True)
            self.btnToggleToolbar1.setVisible(False)
        else:
            self.btnToggleToolbar1.setVisible(True)
            self.btnToggleToolbar2.setVisible(False)

        # Adjust visibility of maximize and restore buttons based on the window state
        if (self.isMaximized() == True):
            self.btnRestore.setVisible(True)
            self.btnMaximize.setVisible(False)
        else:
            self.btnRestore.setVisible(False)
            self.btnMaximize.setVisible(True)

        # Connect slots for button actions
        QMetaObject.connectSlotsByName(self)


    #/===================================================//
    @Slot()
    def on_btnMinimize_clicked(self):
        # Minimize the window when the minimize button is clicked
        print('=== on_btnMinimize_clicked ===')
        self.setWindowState(Qt.WindowState.WindowMinimized)

    @Slot()
    def on_btnRestore_clicked(self):
        # Restore the window to its normal state when the restore button is clicked
        global FLAG_MAXIMIZE

        print('=== on_btnRestore_clicked ===')
        FLAG_MAXIMIZE = False
        self.btnRestore.setVisible(False)
        self.btnMaximize.setVisible(True)
        self.setWindowState(Qt.WindowState.WindowNoState)

    @Slot()
    def on_btnMaximize_clicked(self):
        # Maximize the window when the maximize button is clicked
        global FLAG_MAXIMIZE
        print('=== on_btnMaximize_clicked ===')
        FLAG_MAXIMIZE = True
        self.btnRestore.setVisible(True)
        self.btnMaximize.setVisible(False)
        self.showMaximized()

    @Slot()
    def on_btnClose_clicked(self):
        # Close the window when the close button is clicked
        print('=== on_btnClose_clicked ===')
        self.closeWindow()

    @Slot()
    def on_WidgetWindow_doubleClicked(self):
        # Toggle between maximize and restore on double-click
        print('=== on_titleBar_doubleClicked ===')
        if self.btnMaximize.isVisible():
            self.on_btnMaximize_clicked()
        else:
            self.on_btnRestore_clicked()


    #/===================================================//
    def resizeTextbox(self):
        """
        Adjust the size of the text box based on the content and theme.
        """

        from src.func.py_main_function import UIFunctions
        from src.module.py_window_main import WIDTH1_MAX, HEIGHT1_MIN, HEIGHT1_MAX
        global w1, h1, w3, h3, font

        print("=== resizeTextbox (begin) ===")

        # Set font based on the current theme
        if MainGuiWindow.THEME == 'light':
            font = QFont(MainGuiWindow.FONT_TEXT_FAMILY_LIGHT,MainGuiWindow.FONT_TEXT_SIZE_LIGHT)
        if MainGuiWindow.THEME == 'dark':
            font = QFont(MainGuiWindow.FONT_TEXT_FAMILY_DARK,MainGuiWindow.FONT_TEXT_SIZE_DARK)

        # Initialize the text box
        TextGuiWindow.textbox = TextEdit(self)
        self.textbox.setObjectName('txtbox')
        self.textbox.setFrameShape(QFrame.NoFrame)

        # Apply theme-specific styles
        if (MainGuiWindow.THEME == 'light'):
            self.textbox.setStyleSheet('QTextEdit { color: %s }' %MainGuiWindow.FONT_TEXT_COLOR_LIGHT)
        elif (MainGuiWindow.THEME == 'dark'):
            self.textbox.setStyleSheet('QTextEdit { color: %s }' %MainGuiWindow.FONT_TEXT_COLOR_DARK)

        # Set cursor width and font
        self.textbox.setCursorWidth(2)
        self.textbox.setPlainText(UIFunctions.text)
        self.textbox.setFont(font)

        # Calculate text box dimensions
        cursor = self.textbox.textCursor()
        x = int(cursor.columnNumber() + 1)
        y = int(cursor.blockNumber() + 1)
        self.textbox.selectAll()

        # Set font based on the current theme
        if (MainGuiWindow.THEME == 'light'):
            self.textbox.setFontFamily(MainGuiWindow.FONT_TEXT_FAMILY_LIGHT)
            self.textbox.setFontPointSize(MainGuiWindow.FONT_TEXT_SIZE_LIGHT)
        elif (MainGuiWindow.THEME == 'dark'):
            self.textbox.setFontFamily(MainGuiWindow.FONT_TEXT_FAMILY_DARK)
            self.textbox.setFontPointSize(MainGuiWindow.FONT_TEXT_SIZE_DARK)

        # Calculate text box dimensions
        cursor.clearSelection()
        self.textbox.setTextCursor(cursor)
        cursor.movePosition(x,y)
        fontMetrics = QFontMetrics(font)
        textSize = fontMetrics.size(1,self.textbox.toPlainText())
        w1 = textSize.width() + 50
        h1 = textSize.height()

        # Ensure dimensions are within limits
        if (UIFunctions.text == ""):
            w1 = MainGuiWindow.WIDTH1_MIN
            h1 = HEIGHT1_MIN
        if (w1 > WIDTH1_MAX):
            w1 = WIDTH1_MAX
        if (h1 > HEIGHT1_MAX):
            h1 = HEIGHT1_MAX

        if (w1 < MainGuiWindow.WIDTH1_MIN):
            w1 = MainGuiWindow.WIDTH1_MIN
        if (h1 < HEIGHT1_MIN):
            h1 = HEIGHT1_MIN

        # Set initial position and size of the text box
        x1Pos = x0Pos                               # initial position
        y1Pos = y0Pos                               # initial position
        w3 = int(x1Pos-int(w1/2))
        h3 = int(y1Pos-int(h1/2)-150)
        TextGuiWindow.w2 = w1+30
        TextGuiWindow.h2 = h1+80+HEIGHT_TT
        print("=== resizeTextbox (end) ===")

    #/===================================================//
    def updateTextbox(self):
        """
        Update the layout and properties of the text box and related UI elements.
        """

        from src.module.py_window_main import WIDTH1, WIDTH1_MAX, HEIGHT1_MIN, HEIGHT1_MAX

        print("=== updateTextbox (begin) ===")

        # Initialize labels and toolbars
        self.label1 = QLabel()                          # top1
        self.label2 = QLabel()                          # top2
        self.label3 = QLabel()                          # left
        self.label4 = QLabel()                          # right
        self.label5 = QLabel()                          # bottom
        self.label1.setObjectName('lbl1')

        TextGuiWindow.labelStatusbarMain = QLabel()
        TextGuiWindow.labelStatusbarGrip = QLabel()
        TextGuiWindow.labelStatusbar1 = QLabel()
        TextGuiWindow.labelStatusbar2 = QLabel()
        TextGuiWindow.labelStatusbar3 = QLabel()
        TextGuiWindow.toolbar = QToolBar()
        self.toolbar.setObjectName('toolbar')

        TextGuiWindow.layoutbar = QToolBar()
        self.layoutbar.setObjectName('layoutbar')

        TextGuiWindow.formatbar = QToolBar()
        self.formatbar.setObjectName('formatbar')
        self.setDockingPosition()

        # Configure toolbar properties
        self.toolbar.setFloatable(False)
        self.layoutbar.setFloatable(False)
        self.formatbar.setFloatable(False)
        self.toolbar.setAllowedAreas(Qt.ToolBarArea.TopToolBarArea | Qt.ToolBarArea.BottomToolBarArea)
        self.layoutbar.setAllowedAreas(Qt.ToolBarArea.TopToolBarArea | Qt.ToolBarArea.BottomToolBarArea)
        self.formatbar.setAllowedAreas(Qt.ToolBarArea.TopToolBarArea | Qt.ToolBarArea.BottomToolBarArea)

        # Configure label dimensions
        self.label1.setFixedHeight(2)
        self.label2.setFixedHeight(2)
        self.label3.setFixedWidth(10)
        self.label4.setFixedWidth(10)
        self.label5.setFixedHeight(2)
        self.labelStatusbarMain.setMinimumWidth(300)
        self.labelStatusbarMain.setMinimumHeight(HEIGHT_SB+3)
        self.labelStatusbarGrip.setMaximumWidth(18)
        self.labelStatusbarGrip.setMinimumHeight(18)

        self.labelStatusbar1.setMinimumWidth(100)
        self.labelStatusbar1.setFixedHeight(HEIGHT_SB+3)
        self.labelStatusbar2.setMinimumWidth(100)
        self.labelStatusbar2.setFixedHeight(HEIGHT_SB+3)
        self.labelStatusbar3.setMinimumWidth(100)
        self.labelStatusbar3.setFixedHeight(HEIGHT_SB+3)
        self.labelStatusbar1.setStyleSheet('margin-left: 2px;')
        self.labelStatusbar1.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft)
        self.labelStatusbar2.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignCenter)
        self.labelStatusbar3.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignRight)

        # Add widgets to layouts
        self.layout3.addWidget(self.label1)
        self.layout7.addWidget(self.label2)
        self.layout8.addWidget(self.label3)
        self.layout8.addWidget(self.textbox)
        self.layout8.addWidget(self.label4)
        self.layout9.addWidget(self.label5)

        self.statusBar.addWidget(self.labelStatusbar1, Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft)
        self.statusBar.addWidget(self.labelStatusbar2, Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignCenter)
        self.statusBar.addWidget(self.labelStatusbar3, Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignRight)
        self.windowContentMain.setLayout(self.layout1)

        # Set text box geometry
        self.textbox.setGeometry(15,15,w1,h1)
        self.textbox.setMinimumSize(MainGuiWindow.WIDTH1_MIN,HEIGHT1_MIN)
        self.textbox.setMaximumSize(WIDTH1_MAX,HEIGHT1_MAX)
        self.textbox.resize(w1,h1)

        # Set window geometry
        self.setGeometry(w3,h3,w1+30,h1+80+HEIGHT_TT+HEIGHT_TB+HEIGHT_LB+HEIGHT_FB)
        self.setMinimumSize(MainGuiWindow.WIDTH1_MIN+30,HEIGHT1_MIN+80+HEIGHT_TT+HEIGHT_LB+HEIGHT_FB)
        self.setMaximumSize(WIDTH1_MAX+30,HEIGHT1_MAX+80+HEIGHT_TT+HEIGHT_LB+HEIGHT_FB)

        self.setWindowOpacity(1)
        print("=== updateTextbox (end) ===")

    #//===================================================//
    def setDockingPosition(self):
        """
        Set the docking position of toolbars based on the configuration.
        """

        print('=== setDockingPosition ===')

        # Top toolbar configurations
        if (MainGuiWindow.DOCKING == 0):
            self.windowMain.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolbar)
            self.windowMain.addToolBarBreak()
            self.windowMain.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.layoutbar)
            self.windowMain.addToolBarBreak()
            self.windowMain.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.formatbar)

        elif (MainGuiWindow.DOCKING == 1):
            self.windowMain.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolbar)
            self.windowMain.addToolBarBreak()
            self.windowMain.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.formatbar)
            self.windowMain.addToolBarBreak()
            self.windowMain.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.layoutbar)

        elif (MainGuiWindow.DOCKING == 2):
            self.windowMain.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.layoutbar)
            self.windowMain.addToolBarBreak()
            self.windowMain.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolbar)
            self.windowMain.addToolBarBreak()
            self.windowMain.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.formatbar)

        elif (MainGuiWindow.DOCKING == 3):
            self.windowMain.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.layoutbar)
            self.windowMain.addToolBarBreak()
            self.windowMain.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.formatbar)
            self.windowMain.addToolBarBreak()
            self.windowMain.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolbar)

        elif (MainGuiWindow.DOCKING == 4):
            self.windowMain.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.formatbar)
            self.windowMain.addToolBarBreak()
            self.windowMain.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolbar)
            self.windowMain.addToolBarBreak()
            self.windowMain.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.layoutbar)

        elif (MainGuiWindow.DOCKING == 5):
            self.windowMain.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.formatbar)
            self.windowMain.addToolBarBreak()
            self.windowMain.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.layoutbar)
            self.windowMain.addToolBarBreak()
            self.windowMain.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolbar)

        # Bottom toolbar configurations
        if (MainGuiWindow.DOCKING == 6):
            self.windowMain.addToolBar(Qt.ToolBarArea.BottomToolBarArea, self.formatbar)
            self.windowMain.addToolBarBreak(Qt.ToolBarArea.BottomToolBarArea)
            self.windowMain.addToolBar(Qt.ToolBarArea.BottomToolBarArea, self.layoutbar)
            self.windowMain.addToolBarBreak(Qt.ToolBarArea.BottomToolBarArea)
            self.windowMain.addToolBar(Qt.ToolBarArea.BottomToolBarArea, self.toolbar)

        elif (MainGuiWindow.DOCKING == 7):
            self.windowMain.addToolBar(Qt.ToolBarArea.BottomToolBarArea, self.layoutbar)
            self.windowMain.addToolBarBreak(Qt.ToolBarArea.BottomToolBarArea)
            self.windowMain.addToolBar(Qt.ToolBarArea.BottomToolBarArea, self.formatbar)
            self.windowMain.addToolBarBreak(Qt.ToolBarArea.BottomToolBarArea)
            self.windowMain.addToolBar(Qt.ToolBarArea.BottomToolBarArea, self.toolbar)

        elif (MainGuiWindow.DOCKING == 8):
            self.windowMain.addToolBar(Qt.ToolBarArea.BottomToolBarArea, self.formatbar)
            self.windowMain.addToolBarBreak(Qt.ToolBarArea.BottomToolBarArea)
            self.windowMain.addToolBar(Qt.ToolBarArea.BottomToolBarArea, self.toolbar)
            self.windowMain.addToolBarBreak(Qt.ToolBarArea.BottomToolBarArea)
            self.windowMain.addToolBar(Qt.ToolBarArea.BottomToolBarArea, self.layoutbar)

        elif (MainGuiWindow.DOCKING == 9):
            self.windowMain.addToolBar(Qt.ToolBarArea.BottomToolBarArea, self.toolbar)
            self.windowMain.addToolBarBreak(Qt.ToolBarArea.BottomToolBarArea)
            self.windowMain.addToolBar(Qt.ToolBarArea.BottomToolBarArea, self.formatbar)
            self.windowMain.addToolBarBreak(Qt.ToolBarArea.BottomToolBarArea)
            self.windowMain.addToolBar(Qt.ToolBarArea.BottomToolBarArea, self.layoutbar)

        elif (MainGuiWindow.DOCKING == 10):
            self.windowMain.addToolBar(Qt.ToolBarArea.BottomToolBarArea, self.layoutbar)
            self.windowMain.addToolBarBreak(Qt.ToolBarArea.BottomToolBarArea)
            self.windowMain.addToolBar(Qt.ToolBarArea.BottomToolBarArea, self.toolbar)
            self.windowMain.addToolBarBreak(Qt.ToolBarArea.BottomToolBarArea)
            self.windowMain.addToolBar(Qt.ToolBarArea.BottomToolBarArea, self.formatbar)

        elif (MainGuiWindow.DOCKING == 11):
            self.windowMain.addToolBar(Qt.ToolBarArea.BottomToolBarArea, self.toolbar)
            self.windowMain.addToolBarBreak(Qt.ToolBarArea.BottomToolBarArea)
            self.windowMain.addToolBar(Qt.ToolBarArea.BottomToolBarArea, self.layoutbar)
            self.windowMain.addToolBarBreak(Qt.ToolBarArea.BottomToolBarArea)
            self.windowMain.addToolBar(Qt.ToolBarArea.BottomToolBarArea, self.formatbar)

        # Mixed top and bottom toolbar configurations
        if (MainGuiWindow.DOCKING == 12):
            self.windowMain.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolbar)
            self.windowMain.addToolBarBreak(Qt.ToolBarArea.TopToolBarArea)
            self.windowMain.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.layoutbar)
            self.windowMain.addToolBarBreak(Qt.ToolBarArea.TopToolBarArea)
            self.windowMain.addToolBar(Qt.ToolBarArea.BottomToolBarArea, self.formatbar)

        elif (MainGuiWindow.DOCKING == 13):
            self.windowMain.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolbar)
            self.windowMain.addToolBarBreak(Qt.ToolBarArea.TopToolBarArea)
            self.windowMain.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.formatbar)
            self.windowMain.addToolBarBreak(Qt.ToolBarArea.TopToolBarArea)
            self.windowMain.addToolBar(Qt.ToolBarArea.BottomToolBarArea, self.layoutbar)

        elif (MainGuiWindow.DOCKING == 14):
            self.windowMain.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.layoutbar)
            self.windowMain.addToolBarBreak(Qt.ToolBarArea.TopToolBarArea)
            self.windowMain.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolbar)
            self.windowMain.addToolBarBreak(Qt.ToolBarArea.TopToolBarArea)
            self.windowMain.addToolBar(Qt.ToolBarArea.BottomToolBarArea, self.formatbar)

        elif (MainGuiWindow.DOCKING == 15):
            self.windowMain.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.layoutbar)
            self.windowMain.addToolBarBreak(Qt.ToolBarArea.TopToolBarArea)
            self.windowMain.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.formatbar)
            self.windowMain.addToolBarBreak(Qt.ToolBarArea.TopToolBarArea)
            self.windowMain.addToolBar(Qt.ToolBarArea.BottomToolBarArea, self.toolbar)

        elif (MainGuiWindow.DOCKING == 16):
            self.windowMain.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.formatbar)
            self.windowMain.addToolBarBreak(Qt.ToolBarArea.TopToolBarArea)
            self.windowMain.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolbar)
            self.windowMain.addToolBarBreak(Qt.ToolBarArea.TopToolBarArea)
            self.windowMain.addToolBar(Qt.ToolBarArea.BottomToolBarArea, self.layoutbar)

        elif (MainGuiWindow.DOCKING == 17):
            self.windowMain.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.formatbar)
            self.windowMain.addToolBarBreak(Qt.ToolBarArea.TopToolBarArea)
            self.windowMain.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.layoutbar)
            self.windowMain.addToolBarBreak(Qt.ToolBarArea.TopToolBarArea)
            self.windowMain.addToolBar(Qt.ToolBarArea.BottomToolBarArea, self.toolbar)

        if (MainGuiWindow.DOCKING == 18):
            self.windowMain.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolbar)
            self.windowMain.addToolBarBreak(Qt.ToolBarArea.TopToolBarArea)
            self.windowMain.addToolBar(Qt.ToolBarArea.BottomToolBarArea, self.formatbar)
            self.windowMain.addToolBarBreak(Qt.ToolBarArea.BottomToolBarArea)
            self.windowMain.addToolBar(Qt.ToolBarArea.BottomToolBarArea, self.layoutbar)

        elif (MainGuiWindow.DOCKING == 19):
            self.windowMain.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolbar)
            self.windowMain.addToolBarBreak(Qt.ToolBarArea.TopToolBarArea)
            self.windowMain.addToolBar(Qt.ToolBarArea.BottomToolBarArea, self.layoutbar)
            self.windowMain.addToolBarBreak(Qt.ToolBarArea.BottomToolBarArea)
            self.windowMain.addToolBar(Qt.ToolBarArea.BottomToolBarArea, self.formatbar)

        elif (MainGuiWindow.DOCKING == 20):
            self.windowMain.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.layoutbar)
            self.windowMain.addToolBarBreak(Qt.ToolBarArea.TopToolBarArea)
            self.windowMain.addToolBar(Qt.ToolBarArea.BottomToolBarArea, self.formatbar)
            self.windowMain.addToolBarBreak(Qt.ToolBarArea.BottomToolBarArea)
            self.windowMain.addToolBar(Qt.ToolBarArea.BottomToolBarArea, self.toolbar)

        elif (MainGuiWindow.DOCKING == 21):
            self.windowMain.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.layoutbar)
            self.windowMain.addToolBarBreak(Qt.ToolBarArea.TopToolBarArea)
            self.windowMain.addToolBar(Qt.ToolBarArea.BottomToolBarArea, self.toolbar)
            self.windowMain.addToolBarBreak(Qt.ToolBarArea.BottomToolBarArea)
            self.windowMain.addToolBar(Qt.ToolBarArea.BottomToolBarArea, self.formatbar)

        elif (MainGuiWindow.DOCKING == 22):
            self.windowMain.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.formatbar)
            self.windowMain.addToolBarBreak(Qt.ToolBarArea.TopToolBarArea)
            self.windowMain.addToolBar(Qt.ToolBarArea.BottomToolBarArea, self.layoutbar)
            self.windowMain.addToolBarBreak(Qt.ToolBarArea.BottomToolBarArea)
            self.windowMain.addToolBar(Qt.ToolBarArea.BottomToolBarArea, self.toolbar)

        elif (MainGuiWindow.DOCKING == 23):
            self.windowMain.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.formatbar)
            self.windowMain.addToolBarBreak(Qt.ToolBarArea.TopToolBarArea)
            self.windowMain.addToolBar(Qt.ToolBarArea.BottomToolBarArea, self.toolbar)
            self.windowMain.addToolBarBreak(Qt.ToolBarArea.BottomToolBarArea)
            self.windowMain.addToolBar(Qt.ToolBarArea.BottomToolBarArea, self.layoutbar)

    #//===================================================//
    def exitKeyPressed(self):
        """
        Handles the exit key press event by closing the current window
        and invoking the exit program functionality.
        """

        from src.module.py_window_main import MainGuiWindow

        print('=== exitKeyPressed ===')
        self.closeWindow()
        MainGuiWindow.exitProgram(self)

    #//===================================================//
    def setThemeFcn(self):
        """
        Sets the theme of the application based on the current theme configuration.
        Updates the stylesheet and text color accordingly.
        """

        print('=== setThemeFcn ===')

        if (MainGuiWindow.THEME == "light"):
            self.set_LightTheme()
        elif (MainGuiWindow.THEME == "dark"):
            self.set_DarkTheme()

        self.read_StyleSheet()

        # Update text color based on the theme
        if (MainGuiWindow.THEME == 'light'):
            self.textbox.setStyleSheet('QTextEdit { color: %s }' %MainGuiWindow.FONT_TEXT_COLOR_LIGHT)
        elif (MainGuiWindow.THEME == 'dark'):
            self.textbox.setStyleSheet('QTextEdit { color: %s }' %MainGuiWindow.FONT_TEXT_COLOR_DARK)

    #//===================================================//
    def set_LightTheme(self):
        """
        Configures the application to use the light theme.
        Sets global variables for colors, borders, and icon sizes based on the theme configuration.
        """

        global Border0, Border2, Border3, Border5, IconSize
        global Color_font, Color_TB, Color_FG, Color_BG, Color_BT, Color_BD
        global Color_btn_gradient2, Color_btn_gradient3, Color_btn_gradient4, Color_toolbar_hover

        print('=== set_LightTheme ===')

        # Configure border styles
        if (MainGuiWindow.BorderStyleVar1 == 0):
            Border0 = '0px'
            Border2 = '0px'
            Border3 = '0px'
            Border5 = '0px'
        elif (MainGuiWindow.BorderStyleVar1 == 1):
            Border0 = '0px'
            Border2 = '2px'
            Border3 = '3px'
            Border5 = '5px'

        # Configure icon sizes
        if (MainGuiWindow.TextEditorIconSizeVar1 == 16):
            IconSize = '16px'
        elif (MainGuiWindow.TextEditorIconSizeVar1 == 18):
            IconSize = '18px'
        elif (MainGuiWindow.TextEditorIconSizeVar1 == 22):
            IconSize = '22px'

        # Configure colors based on the selected light theme
        if (MainGuiWindow.THEME_LIGHT == "Default"):
            Color_font = 'black'
            Color_TB = 'rgb(215,215,215)'
            Color_FG = 'rgb(252,252,252)'
            Color_BG = 'white'
            Color_BT = 'rgb(135,135,135)'
            Color_BD = 'rgb(205,205,205)'

        elif (MainGuiWindow.THEME_LIGHT == "Yellow"):
            Color_font = 'rgb(150,150,25)'
            Color_TB = 'rgb(255,255,175)'
            Color_FG = 'rgb(255,255,254)'
            Color_BG = 'white'
            Color_BT = 'rgb(235,235,150)'
            Color_BD = 'rgb(225,225,175)'

        elif (MainGuiWindow.THEME_LIGHT == "Green"):
            Color_font = 'rgb(50,125,50)'
            Color_TB = 'rgb(195,255,195)'
            Color_FG = 'rgb(254,255,253)'
            Color_BG = 'white'
            Color_BT = 'rgb(125,255,125)'
            Color_BD = 'rgb(150,235,150)'

        elif (MainGuiWindow.THEME_LIGHT == "Blue"):
            Color_font = 'rgb(95,95,255)'
            Color_TB = 'rgb(150,215,255)'
            Color_FG = 'rgb(254,254,255)'
            Color_BG = 'white'
            Color_BT = 'rgb(150,200,255)'
            Color_BD = 'rgb(175,225,255)'

        elif (MainGuiWindow.THEME_LIGHT == "Pink"):
            Color_font = 'rgb(215,85,250)'
            Color_TB = 'rgb(255,225,255)'
            Color_FG = 'rgb(255,254,255)'
            Color_BG = 'white'
            Color_BT = 'rgb(255,200,255)'
            Color_BD = 'rgb(255,200,255)'

        elif (MainGuiWindow.THEME_LIGHT == "Orange"):
            Color_font = 'rgb(255,128,0)'
            Color_TB = 'rgb(250,225,200)'
            Color_FG = 'rgb(255,254,253)'
            Color_BG = 'white'
            Color_BT = 'rgb(250,215,175)'
            Color_BD = 'rgb(255,225,200)'

        elif (MainGuiWindow.THEME_LIGHT == "Custom"):
            Color_font = MainGuiWindow.FONT_COLOR_LIGHT_CUSTOM
            Color_TB = MainGuiWindow.TB_COLOR_LIGHT_CUSTOM
            Color_FG = MainGuiWindow.FG_COLOR_LIGHT_CUSTOM
            Color_BG = MainGuiWindow.BG_COLOR_LIGHT_CUSTOM
            Color_BT = MainGuiWindow.BT_COLOR_LIGHT_CUSTOM
            Color_BD = MainGuiWindow.BD_COLOR_LIGHT_CUSTOM

        # Configure additional colors
        Color_btn_gradient2 = 'rgb(185,185,185)'
        Color_btn_gradient3 = 'rgb(165,165,165)'
        Color_btn_gradient4 = 'rgb(135,135,135)'
        Color_toolbar_hover = 'rgb(220,235,245)'

    #//===================================================//
    def set_DarkTheme(self):
        """
        Configures the application to use the dark theme.
        Sets global variables for colors, borders, and icon sizes based on the theme configuration.
        """

        global Border0, Border2, Border3, Border5, IconSize
        global Color_font, Color_TB, Color_FG, Color_BG, Color_BT, Color_BD
        global Color_btn_gradient2, Color_btn_gradient3, Color_btn_gradient4, Color_toolbar_hover

        print('=== set_DarkTheme ===')

        # Configure border styles
        if (MainGuiWindow.BorderStyleVar1 == 0):
            Border0 = '0px'
            Border2 = '0px'
            Border3 = '0px'
            Border5 = '0px'
        elif (MainGuiWindow.BorderStyleVar1 == 1):
            Border0 = '0px'
            Border2 = '2px'
            Border3 = '3px'
            Border5 = '5px'

        # Configure icon sizes
        if (MainGuiWindow.TextEditorIconSizeVar1 == 16):
            IconSize = '16px'
        elif (MainGuiWindow.TextEditorIconSizeVar1 == 18):
            IconSize = '18px'
        elif (MainGuiWindow.TextEditorIconSizeVar1 == 22):
            IconSize = '22px'

        # Configure colors based on the selected dark theme
        if (MainGuiWindow.THEME_DARK == "Default"):
            Color_font = 'white'
            Color_TB = 'rgb(85,85,85)'
            Color_FG = 'rgb(60,60,60)'
            Color_BG = 'rgb(50,50,50)'
            Color_BT = 'rgb(175,175,175)'
            Color_BD = 'rgb(135,135,135)'

        elif (MainGuiWindow.THEME_DARK == "Yellow"):
            Color_font = 'rgb(225,225,125)'
            Color_TB = 'rgb(100,100,50)'
            Color_FG = 'rgb(60,60,60)'
            Color_BG = 'rgb(50,50,50)'
            Color_BT = 'rgb(235,235,150)'
            Color_BD = 'rgb(125,125,75)'

        elif (MainGuiWindow.THEME_DARK == "Green"):
            Color_font = 'rgb(115,235,115)'
            Color_TB = 'rgb(50,100,50)'
            Color_FG = 'rgb(60,60,60)'
            Color_BG = 'rgb(50,50,50)'
            Color_BT = 'rgb(125,255,125)'
            Color_BD = 'rgb(75,125,75)'

        elif (MainGuiWindow.THEME_DARK == "Blue"):
            Color_font = 'rgb(125,215,255)'
            Color_TB = 'rgb(25,65,125)'
            Color_FG = 'rgb(60,60,60)'
            Color_BG = 'rgb(50,50,50)'
            Color_BT = 'rgb(135,225,255)'
            Color_BD = 'rgb(25,100,150)'

        elif (MainGuiWindow.THEME_DARK == "Pink"):
            Color_font = 'rgb(225,175,225)'
            Color_TB = 'rgb(115,0,115)'
            Color_FG = 'rgb(60,60,60)'
            Color_BG = 'rgb(50,50,50)'
            Color_BT = 'rgb(235,185,255)'
            Color_BD = 'rgb(150,75,150)'

        elif (MainGuiWindow.THEME_DARK == "Orange"):
            Color_font = 'rgb(235,150,75)'
            Color_TB = 'rgb(175,65,0)'
            Color_FG = 'rgb(60,60,60)'
            Color_BG = 'rgb(50,50,50)'
            Color_BT = 'rgb(255,175,100)'
            Color_BD = 'rgb(175,75,5)'

        elif (MainGuiWindow.THEME_DARK == "Custom"):
            Color_font = MainGuiWindow.FONT_COLOR_DARK_CUSTOM
            Color_TB = MainGuiWindow.TB_COLOR_DARK_CUSTOM
            Color_FG = MainGuiWindow.FG_COLOR_DARK_CUSTOM
            Color_BG = MainGuiWindow.BG_COLOR_DARK_CUSTOM
            Color_BT = MainGuiWindow.BT_COLOR_DARK_CUSTOM
            Color_BD = MainGuiWindow.BD_COLOR_DARK_CUSTOM

        # Configure additional colors
        Color_btn_gradient2 = 'rgb(75,75,75)'
        Color_btn_gradient3 = 'rgb(65,65,65)'
        Color_btn_gradient4 = 'rgb(35,35,35)'
        Color_toolbar_hover = 'rgb(100,125,175)'

    #//===================================================//
    def read_StyleSheet(self):
        """
        Reads the stylesheet file and replaces placeholders with the current theme's colors and styles.
        Applies the updated stylesheet to the application.
        """

        global stylesheetNew

        print('=== read_StyleSheet ===')

        styleFile = QFile(":/resources/theme/styles_theme.qss")
        styleFile.open(QIODevice.ReadOnly)

        # Replace placeholders in the stylesheet with actual values
        stylesheetNew = QTextStream(styleFile).readAll()\
        .replace('$Color_btn_gradient2', Color_btn_gradient2)\
        .replace('$Color_btn_gradient3', Color_btn_gradient3)\
        .replace('$Color_btn_gradient4', Color_btn_gradient4)\
        .replace('$Color_toolbar_hover', Color_toolbar_hover)\
        .replace('$Color_font', Color_font)\
        .replace('$Color_TB', Color_TB)\
        .replace('$Color_FG', Color_FG)\
        .replace('$Color_BG', Color_BG)\
        .replace('$Color_BT', Color_BT)\
        .replace('$Color_BD', Color_BD)\
        .replace('$Border5', Border5)\
        .replace('$Border3', Border3)\
        .replace('$Border2', Border2)\
        .replace('$Border0', Border0)\
        .replace('$IconSize', IconSize)

        self.setStyleSheet(stylesheetNew)

    #//===================================================//
    def updateTheme(self):
        """
        Updates the application's theme by applying the appropriate styles and colors
        to all relevant UI components.
        """

        print('=== updateTheme ===')
        if (MainGuiWindow.THEME == 'light'):
            TextGuiWindow.set_LightTheme(self)
        elif (MainGuiWindow.THEME == 'dark'):
            TextGuiWindow.set_DarkTheme(self)

        from src.module.py_window_setting import SettingWindow
        from src.module.py_window_findreplace import FindReplace
        from src.module.py_window_colorpicker import ColorPicker
        from src.module.py_window_help import HelpWindow
        from src.module.py_window_tutorial import TutorialWindow
        from src.module.py_window_about import AboutWindow

        TextGuiWindow.read_StyleSheet(self)

        # Apply the updated stylesheet to various UI components
        try:
            TextGuiWindow.WidgetWindow.setStyleSheet(stylesheetNew)
            TextGuiWindow.labelWindowFrame.setStyleSheet(stylesheetNew)
            TextGuiWindow.windowContentMain.setStyleSheet(stylesheetNew)
            TextGuiWindow.containerMain.setStyleSheet(stylesheetNew)
            TextGuiWindow.statusBar.setStyleSheet(stylesheetNew)

            # Update text color based on the theme
            if (MainGuiWindow.THEME == 'light'):
                TextGuiWindow.textbox.setStyleSheet('QTextEdit { color: %s }' %MainGuiWindow.FONT_TEXT_COLOR_LIGHT)
            elif (MainGuiWindow.THEME == 'dark'):
                TextGuiWindow.textbox.setStyleSheet('QTextEdit { color: %s }' %MainGuiWindow.FONT_TEXT_COLOR_DARK)
        except:
            pass

        # Update styles for other windows if they exist
        try:
            SettingWindow.labelTitle2.setStyleSheet(stylesheetNew)
            SettingWindow.windowContent2.setStyleSheet(stylesheetNew)
            SettingWindow.labeltop.setStyleSheet(stylesheetNew)
            SettingWindow.btnOK2.setStyleSheet(stylesheetNew)
            SettingWindow.btnCancel2.setStyleSheet(stylesheetNew)
        except:
            pass

        try:
            ColorPicker.labelTitle3.setStyleSheet(stylesheetNew)
            ColorPicker.container3.setStyleSheet(stylesheetNew)
        except:
            pass

        try:
            FindReplace.labelTitle4.setStyleSheet(stylesheetNew)
            FindReplace.containerContent4.setStyleSheet(stylesheetNew)
        except:
            pass

        try:
            HelpWindow.labelTitle6.setStyleSheet(stylesheetNew)
            HelpWindow.container6.setStyleSheet(stylesheetNew)
        except:
            pass

        try:
            TutorialWindow.labelTitle8.setStyleSheet(stylesheetNew)
            TutorialWindow.container8.setStyleSheet(stylesheetNew)
        except:
            pass

        try:
            AboutWindow.labelTitle5.setStyleSheet(stylesheetNew)
            AboutWindow.container5.setStyleSheet(stylesheetNew)
            AboutWindow.labellink1b.setStyleSheet(stylesheetNew)
        except:
            pass

    #//===================================================//
    def setThemeLight(self):
        """
        Switches the application theme to light mode and updates the UI accordingly.
        """

        print('=== setThemeLight ===')
        MainGuiWindow.THEME = 'light'
        TextGuiWindow.updateTheme(self)

    #//===================================================//
    def setThemeDark(self):
        """
        Switches the application theme to dark mode and updates the UI accordingly.
        """

        print('=== setThemeDark ===')
        MainGuiWindow.THEME = 'dark'
        TextGuiWindow.updateTheme(self)

    #//===================================================//
    def toggleToolbar(self):
        """
        Toggles the visibility of the toolbar and updates related UI elements.
        """

        print('=== toggleToolbar ===')

        MainGuiWindow.FLAG_TOOLBAR = not(MainGuiWindow.FLAG_TOOLBAR)
        print('FLAG_TOOLBAR1 := ', MainGuiWindow.FLAG_TOOLBAR)

        if MainGuiWindow.FLAG_TOOLBAR:
            self.toolbar.setVisible(True)

            # Apply the current theme to the toolbar
            if MainGuiWindow.THEME == 'light':
                self.set_LightTheme()
            elif MainGuiWindow.THEME == 'dark':
                self.set_DarkTheme()

            # Show or hide format and layout bars based on settings
            if MainGuiWindow.FLAG_FORMATBAR:
                self.layoutbar.setVisible(True)
                self.formatbar.setVisible(True)
            else:
                self.layoutbar.setVisible(False)
                self.formatbar.setVisible(False)

            self.label1.setFixedHeight(2)
            self.label2.setFixedHeight(5)
            self.label5.setFixedHeight(2)
            self.btnToggleToolbar2.setVisible(True)
            self.btnToggleToolbar1.setVisible(False)

            # Disable opacity increase if already at maximum
            if ((MainGuiWindow.OPACITY_TEXT_LIGHT == 1) or (MainGuiWindow.OPACITY_TEXT_DARK == 1)):
                    self.increase_opacity_action.setEnabled(False)
            self.updateEnabled_icon()
        else:
            # Hide all toolbars and reset related UI elements
            self.label1.setStyleSheet('background-color: transparent;')
            self.toolbar.setVisible(False)
            self.layoutbar.setVisible(False)
            self.formatbar.setVisible(False)
            self.label1.setFixedHeight(5)
            self.label2.setFixedHeight(2)
            self.label5.setFixedHeight(2)
            self.btnToggleToolbar2.setVisible(False)
            self.btnToggleToolbar1.setVisible(True)

    #//===================================================//
    def toggleTheme(self):
        """
        Toggles the application's theme between light and dark modes.
        Updates font size, font family, opacity, and other settings based on the selected theme.
        """

        from src.module.py_window_setting import SettingWindow
        from src.module.py_window_colorpicker import ColorPicker
        from src.module.py_window_findreplace import FindReplace

        print('=== toggleTheme ===')

        # Toggle theme
        if (MainGuiWindow.THEME == "light"):
            MainGuiWindow.THEME = "dark"
        elif (MainGuiWindow.THEME == "dark"):
            MainGuiWindow.THEME = "light"

        # Update font and opacity settings based on the theme
        if MainGuiWindow.TextEditorModeVar1 == 0:
            if MainGuiWindow.THEME == "light":
                MainGuiWindow.FONT_TEXT_SIZE_LIGHT = MainGuiWindow.FONT_TEXT_SIZE_DARK
                MainGuiWindow.FONT_TEXT_FAMILY_LIGHT = MainGuiWindow.FONT_TEXT_FAMILY_DARK
                MainGuiWindow.OPACITY_TEXT_LIGHT = MainGuiWindow.OPACITY_TEXT_DARK
                MainGuiWindow.PARAGRAPH_TEXT_LIGHT = MainGuiWindow.PARAGRAPH_TEXT_DARK
            elif MainGuiWindow.THEME == "dark":
                MainGuiWindow.FONT_TEXT_SIZE_DARK = MainGuiWindow.FONT_TEXT_SIZE_LIGHT
                MainGuiWindow.FONT_TEXT_FAMILY_DARK = MainGuiWindow.FONT_TEXT_FAMILY_LIGHT
                MainGuiWindow.OPACITY_TEXT_DARK = MainGuiWindow.OPACITY_TEXT_LIGHT
                MainGuiWindow.PARAGRAPH_TEXT_DARK = MainGuiWindow.PARAGRAPH_TEXT_LIGHT

        elif MainGuiWindow.TextEditorModeVar1 == 1:
            if MainGuiWindow.THEME == "light":
                MainGuiWindow.FONT_TEXT_SIZE_LIGHT = MainGuiWindow.FONT_TEXT_SIZE_LIGHT
                MainGuiWindow.FONT_TEXT_FAMILY_LIGHT = MainGuiWindow.FONT_TEXT_FAMILY_LIGHT
                MainGuiWindow.OPACITY_TEXT_LIGHT = MainGuiWindow.OPACITY_TEXT_LIGHT
                MainGuiWindow.PARAGRAPH_TEXT_LIGHT = MainGuiWindow.PARAGRAPH_TEXT_LIGHT
            elif MainGuiWindow.THEME == "dark":
                MainGuiWindow.FONT_TEXT_SIZE_DARK = MainGuiWindow.FONT_TEXT_SIZE_DARK
                MainGuiWindow.FONT_TEXT_FAMILY_DARK = MainGuiWindow.FONT_TEXT_FAMILY_DARK
                MainGuiWindow.OPACITY_TEXT_DARK = MainGuiWindow.OPACITY_TEXT_DARK
                MainGuiWindow.PARAGRAPH_TEXT_DARK = MainGuiWindow.PARAGRAPH_TEXT_DARK

        # Update text box font size and cursor position based on the theme
        if MainGuiWindow.THEME == "light":
            cursor = self.textbox.textCursor()
            x = int(cursor.columnNumber() + 1)
            y = int(cursor.blockNumber() + 1)
            self.textbox.selectAll()
            self.textbox.setFontPointSize(MainGuiWindow.FONT_TEXT_SIZE_LIGHT)
            cursor.clearSelection()
            self.textbox.setTextCursor(cursor)
            cursor.movePosition(x,y)

            if (MainGuiWindow.FONT_TEXT_SIZE_LIGHT == FONT_TEXT_SIZE_MIN):
                self.decrease_textsize_action.setEnabled(False)
                self.increase_textsize_action.setEnabled(True)
            elif (MainGuiWindow.FONT_TEXT_SIZE_LIGHT == FONT_TEXT_SIZE_MAX):
                self.decrease_textsize_action.setEnabled(True)
                self.increase_textsize_action.setEnabled(False)
            else:
                self.decrease_textsize_action.setEnabled(True)
                self.increase_textsize_action.setEnabled(True)

            if MainGuiWindow.OPACITY_TEXT_LIGHT == 1:
                self.increase_opacity_action.setEnabled(False)
                self.decrease_opacity_action.setEnabled(True)
            elif MainGuiWindow.OPACITY_TEXT_LIGHT == 0.005:
                self.decrease_opacity_action.setEnabled(False)
                self.increase_opacity_action.setEnabled(True)
            else:
                self.increase_opacity_action.setEnabled(True)
                self.decrease_opacity_action.setEnabled(True)

            self.set_LightTheme()
            self.textbox.setStyleSheet('QTextEdit { color: %s }' %MainGuiWindow.FONT_TEXT_COLOR_LIGHT)

        elif MainGuiWindow.THEME == "dark":
            cursor = self.textbox.textCursor()
            x = int(cursor.columnNumber() + 1)
            y = int(cursor.blockNumber() + 1)
            self.textbox.selectAll()
            self.textbox.setFontPointSize(MainGuiWindow.FONT_TEXT_SIZE_DARK)
            cursor.clearSelection()
            self.textbox.setTextCursor(cursor)
            cursor.movePosition(x,y)

            if (MainGuiWindow.FONT_TEXT_SIZE_DARK == FONT_TEXT_SIZE_MIN):
                self.decrease_textsize_action.setEnabled(False)
                self.increase_textsize_action.setEnabled(True)
            elif (MainGuiWindow.FONT_TEXT_SIZE_DARK == FONT_TEXT_SIZE_MAX):
                self.decrease_textsize_action.setEnabled(True)
                self.increase_textsize_action.setEnabled(False)
            else:
                self.decrease_textsize_action.setEnabled(True)
                self.increase_textsize_action.setEnabled(True)

            if MainGuiWindow.OPACITY_TEXT_DARK == 1:
                self.increase_opacity_action.setEnabled(False)
                self.decrease_opacity_action.setEnabled(True)
            elif MainGuiWindow.OPACITY_TEXT_DARK == 0.005:
                self.decrease_opacity_action.setEnabled(False)
                self.increase_opacity_action.setEnabled(True)
            else:
                self.increase_opacity_action.setEnabled(True)
                self.decrease_opacity_action.setEnabled(True)

            self.set_DarkTheme()
            self.textbox.setStyleSheet('QTextEdit { color: %s }' %MainGuiWindow.FONT_TEXT_COLOR_DARK)

        # Update the stylesheet for the main window and other components
        self.read_StyleSheet()
        self.showTabSpaces()
        TextGuiWindow.WidgetWindow.setStyleSheet(stylesheetNew)
        TextGuiWindow.labelWindowFrame.setStyleSheet(stylesheetNew)
        TextGuiWindow.windowContentMain.setStyleSheet(stylesheetNew)
        TextGuiWindow.containerMain.setStyleSheet(stylesheetNew)
        TextGuiWindow.statusBar.setStyleSheet(stylesheetNew)

        # Update styles for other windows
        try:
            print('=== toggleTheme SettingWindow ===')
            SettingWindow.labelTitle2.setStyleSheet(stylesheetNew)
            SettingWindow.windowContent2.setStyleSheet(stylesheetNew)
            SettingWindow.labeltop.setStyleSheet(stylesheetNew)
            SettingWindow.btnOK2.setStyleSheet(stylesheetNew)
            SettingWindow.btnCancel2.setStyleSheet(stylesheetNew)
        except:
            pass

        try:
            print('=== toggleTheme ColorPicker ===')
            ColorPicker.labelTitle3.setStyleSheet(stylesheetNew)
            ColorPicker.container3.setStyleSheet(stylesheetNew)
        except:
            pass

        try:
            print('=== toggleTheme FindReplace ===')
            FindReplace.labelTitle4.setStyleSheet(stylesheetNew)
            FindReplace.containerContent4.setStyleSheet(stylesheetNew)
        except:
            pass

        from src.module.py_window_help import HelpWindow
        from src.module.py_window_tutorial import TutorialWindow
        from src.module.py_window_about import AboutWindow

        try:
            HelpWindow.labelTitle6.setStyleSheet(stylesheetNew)
            HelpWindow.container6.setStyleSheet(stylesheetNew)
        except:
            pass

        try:
            TutorialWindow.labelTitle8.setStyleSheet(stylesheetNew)
            TutorialWindow.container8.setStyleSheet(stylesheetNew)
        except:
            pass



        try:
            AboutWindow.labelTitle5.setStyleSheet(stylesheetNew)
            AboutWindow.container5.setStyleSheet(stylesheetNew)

            # if MainGuiWindow.THEME == 'light':
            #     print('=== light ===0000000000000000000000000000000000000000')
            #     AboutWindow.labellink1b.setStyleSheet('QLabel { color: rgb(200, 0, 255); }')
            # elif MainGuiWindow.THEME == 'dark':
            #     print('=== dark ===0000000000000000000000000000000000000000')
            #     AboutWindow.labellink1b.setStyleSheet('QLabel { color: rgb(50, 225, 225); }')

            # if (MainGuiWindow.THEME == 'light'):
            #     AboutWindow.labellink1a.setStyleSheet('QLabel {color: rgb(255, 0, 0)}')
            #     AboutWindow.labellink1b.setStyleSheet('QLabel {color: rgb(255, 0, 0)}')
            #     AboutWindow.labellink1c.setStyleSheet('QLabel {color: rgb(255, 0, 0)}')
            # elif (MainGuiWindow.THEME == 'dark'):
            #     AboutWindow.labellink1a.setStyleSheet('QLabel {color: rgb(50,225,225)}')
            #     AboutWindow.labellink1b.setStyleSheet('QLabel {color: rgb(50,225,225)}')
            #     AboutWindow.labellink1c.setStyleSheet('QLabel {color: rgb(50,225,225)}')
        except:
            pass

        self.repaint()
        self.updateEnabled_icon()

    #//===================================================//
    def increaseTextSize(self):
        """
        Increases the font size of the text box based on the current theme.
        """

        print('=== increaseTextSize ===')
        if MainGuiWindow.THEME == 'light':
            self.increaseTextSizeLight()
        elif MainGuiWindow.THEME == 'dark':
            self.increaseTextSizeDark()

    #//===================================================//
    def increaseTextSizeLight(self):
        """
        Increases the font size for the light theme.
        """

        global FONT_INDEX_LIGHT

        print('=== increaseTextSizeLight ===')

        FONT_SIZE_LIST = [6,7,8,10,12,14,18,24,28,36,48]
        if MainGuiWindow.FONT_TEXT_SIZE_LIGHT >= FONT_TEXT_SIZE_MAX:
            MainGuiWindow.FONT_TEXT_SIZE_LIGHT = FONT_TEXT_SIZE_MAX
        elif MainGuiWindow.FONT_TEXT_SIZE_LIGHT <= FONT_TEXT_SIZE_MIN:
            MainGuiWindow.FONT_TEXT_SIZE_LIGHT = FONT_TEXT_SIZE_MIN


        if FONT_TEXT_SIZE_MIN <= MainGuiWindow.FONT_TEXT_SIZE_LIGHT <= FONT_TEXT_SIZE_MAX:
            list = np.asarray(FONT_SIZE_LIST)
            FONT_INDEX_LIGHT = (np.abs(list - MainGuiWindow.FONT_TEXT_SIZE_LIGHT)).argmin()

            if FONT_INDEX_LIGHT < 10:
                FONT_INDEX_LIGHT = FONT_INDEX_LIGHT + 1
            else:
                FONT_INDEX_LIGHT = 10

            if (FONT_INDEX_LIGHT == 10):
                self.increase_textsize_action.setEnabled(False)

        MainGuiWindow.FONT_TEXT_SIZE_LIGHT = FONT_SIZE_LIST[FONT_INDEX_LIGHT]
        self.decrease_textsize_action.setEnabled(True)
        print('FONT_SIZE := ', MainGuiWindow.FONT_TEXT_SIZE_LIGHT)
        MainGuiWindow.FontTextSizeLightVar1 = MainGuiWindow.FONT_TEXT_SIZE_LIGHT

        # Update text box font size and cursor position
        cursor = self.textbox.textCursor()
        x = int(cursor.columnNumber()+1)
        y = int(cursor.blockNumber()+1)
        self.textbox.selectAll()
        self.textbox.setFontPointSize(MainGuiWindow.FONT_TEXT_SIZE_LIGHT)
        cursor.clearSelection()
        self.textbox.setTextCursor(cursor)
        cursor.movePosition(x,y)
        self.updateEnabled_icon()

    #//===================================================//
    def increaseTextSizeDark(self):
        """
        Increases the font size for the dark theme.
        """

        global FONT_INDEX_DARK

        print('=== increaseTextSizeDark ===')

        FONT_SIZE_LIST = [6,7,8,10,12,14,18,24,28,36,48]
        if MainGuiWindow.FONT_TEXT_SIZE_DARK >= FONT_TEXT_SIZE_MAX:
            MainGuiWindow.FONT_TEXT_SIZE_DARK = FONT_TEXT_SIZE_MAX
        elif MainGuiWindow.FONT_TEXT_SIZE_DARK <= FONT_TEXT_SIZE_MIN:
            MainGuiWindow.FONT_TEXT_SIZE_DARK = FONT_TEXT_SIZE_MIN

        if FONT_TEXT_SIZE_MIN <= MainGuiWindow.FONT_TEXT_SIZE_DARK <= FONT_TEXT_SIZE_MAX:
            list = np.asarray(FONT_SIZE_LIST)
            FONT_INDEX_DARK = (np.abs(list - MainGuiWindow.FONT_TEXT_SIZE_DARK)).argmin()

            if FONT_INDEX_DARK < FONT_TEXT_INDEX_MAX:
                FONT_INDEX_DARK = FONT_INDEX_DARK + 1
            else:
                FONT_INDEX_DARK = FONT_TEXT_INDEX_MAX

            if (FONT_INDEX_DARK == FONT_TEXT_INDEX_MAX):
                self.increase_textsize_action.setEnabled(False)

        MainGuiWindow.FONT_TEXT_SIZE_DARK = FONT_SIZE_LIST[FONT_INDEX_DARK]
        self.decrease_textsize_action.setEnabled(True)
        print('FONT_SIZE := ', MainGuiWindow.FONT_TEXT_SIZE_DARK)
        MainGuiWindow.FontTextSizeDarkVar1 = MainGuiWindow.FONT_TEXT_SIZE_DARK

        # Update text box font size and cursor position
        cursor = self.textbox.textCursor()
        x = int(cursor.columnNumber() + 1)
        y = int(cursor.blockNumber() + 1)
        self.textbox.selectAll()
        self.textbox.setFontPointSize(MainGuiWindow.FONT_TEXT_SIZE_DARK)
        cursor.clearSelection()
        self.textbox.setTextCursor(cursor)
        cursor.movePosition(x,y)
        self.updateEnabled_icon()

    #//===================================================//
    def decreaseTextSize(self):
        """
        Decreases the font size of the text box based on the current theme.
        """

        print('=== decreaseTextSize ===')
        if MainGuiWindow.THEME == 'light':
            self.decreaseTextSizeLight()
        elif MainGuiWindow.THEME == 'dark':
            self.decreaseTextSizeDark()

    #//===================================================//
    def decreaseTextSizeLight(self):
        """
        Decreases the font size for the light theme.
        """

        global FONT_INDEX_LIGHT

        print('=== decreaseTextSizeLight ===')
        FONT_SIZE_LIST = [6,7,8,10,12,14,18,24,28,36,48]

        if MainGuiWindow.FONT_TEXT_SIZE_LIGHT >= FONT_TEXT_SIZE_MAX:
            MainGuiWindow.FONT_TEXT_SIZE_LIGHT = FONT_TEXT_SIZE_MAX
        elif MainGuiWindow.FONT_TEXT_SIZE_LIGHT <= FONT_TEXT_SIZE_MIN:
            MainGuiWindow.FONT_TEXT_SIZE_LIGHT = FONT_TEXT_SIZE_MIN

        if FONT_TEXT_SIZE_MIN <= MainGuiWindow.FONT_TEXT_SIZE_LIGHT <= FONT_TEXT_SIZE_MAX:
            list = np.asarray(FONT_SIZE_LIST)
            FONT_INDEX_LIGHT = (np.abs(list - MainGuiWindow.FONT_TEXT_SIZE_LIGHT)).argmin()

            if FONT_INDEX_LIGHT >= 1:
                FONT_INDEX_LIGHT = FONT_INDEX_LIGHT - 1
            else:
                FONT_INDEX_LIGHT = FONT_TEXT_INDEX_MIN

            if (FONT_INDEX_LIGHT == FONT_TEXT_INDEX_MIN):
                self.decrease_textsize_action.setEnabled(False)

        MainGuiWindow.FONT_TEXT_SIZE_LIGHT = FONT_SIZE_LIST[FONT_INDEX_LIGHT]

        self.increase_textsize_action.setEnabled(True)
        print('FONT_SIZE := ', MainGuiWindow.FONT_TEXT_SIZE_LIGHT)
        MainGuiWindow.FontTextSizeLightVar1 = MainGuiWindow.FONT_TEXT_SIZE_LIGHT

        # Update text box font size and cursor position
        cursor = self.textbox.textCursor()
        x = int(cursor.columnNumber() + 1)
        y = int(cursor.blockNumber() + 1)
        self.textbox.selectAll()
        self.textbox.setFontPointSize(MainGuiWindow.FONT_TEXT_SIZE_LIGHT)
        cursor.clearSelection()
        self.textbox.setTextCursor(cursor)
        cursor.movePosition(x,y)
        self.updateEnabled_icon()

    #//===================================================//
    def decreaseTextSizeDark(self):
        """
        Decreases the font size for the dark theme.
        """

        global FONT_INDEX_DARK

        print('=== decreaseTextSizeDark ===')
        FONT_SIZE_LIST = [6,7,8,10,12,14,18,24,28,36,48]

        # Ensure font size stays within the defined range
        if MainGuiWindow.FONT_TEXT_SIZE_DARK >= FONT_TEXT_SIZE_MAX:
            MainGuiWindow.FONT_TEXT_SIZE_DARK = FONT_TEXT_SIZE_MAX
        elif MainGuiWindow.FONT_TEXT_SIZE_DARK <= FONT_TEXT_SIZE_MIN:
            MainGuiWindow.FONT_TEXT_SIZE_DARK = FONT_TEXT_SIZE_MIN

        # Adjust font size index based on the current size
        if FONT_TEXT_SIZE_MIN <= MainGuiWindow.FONT_TEXT_SIZE_DARK <= FONT_TEXT_SIZE_MAX:
            list = np.asarray(FONT_SIZE_LIST)
            FONT_INDEX_DARK = (np.abs(list - MainGuiWindow.FONT_TEXT_SIZE_DARK)).argmin()

            if FONT_INDEX_DARK >= 1:
                FONT_INDEX_DARK = FONT_INDEX_DARK - 1
            else:
                FONT_INDEX_DARK = 0

            if (FONT_INDEX_DARK == 0):
                self.decrease_textsize_action.setEnabled(False)

        MainGuiWindow.FONT_TEXT_SIZE_DARK = FONT_SIZE_LIST[FONT_INDEX_DARK]
        self.increase_textsize_action.setEnabled(True)
        print('FONT_SIZE := ', MainGuiWindow.FONT_TEXT_SIZE_DARK)
        MainGuiWindow.FontTextSizeLightVar1 = MainGuiWindow.FONT_TEXT_SIZE_DARK

        # Update text box font size and cursor position
        cursor = self.textbox.textCursor()
        x = int(cursor.columnNumber() + 1)
        y = int(cursor.blockNumber() + 1)
        self.textbox.selectAll()
        self.textbox.setFontPointSize(MainGuiWindow.FONT_TEXT_SIZE_DARK)
        cursor.clearSelection()
        self.textbox.setTextCursor(cursor)
        cursor.movePosition(x,y)
        self.updateEnabled_icon()

    #//===================================================//
    def setTextFont(self):
        """
        Opens a font dialog to allow the user to select a font and applies it to the text box.
        """

        global FONT_BOLD, FONT_ITALIC, FONT_UNDERLINE
        global FLAG_FONT_INIT, font_selected_pre, font_selected

        print('=== setTextFont ===')
        font_selected_pre = None
        # Open font dialog
        if (FLAG_FONT_INIT):
            FLAG_FONT_INIT = False
            font_selected, ok = QFontDialog.getFont(font)
        else:
            font_selected, ok = QFontDialog.getFont(font_selected_pre)

        # Ensure font size does not exceed the maximum limit
        if (int(font_selected.pointSizeF()) >= FONT_TEXT_SIZE_MAX):
            font_selected.setPointSize(FONT_TEXT_SIZE_MAX)

        if ok:
            # Apply selected font to the text box
            self.textbox.setFont(font_selected)
            cursor = self.textbox.textCursor()
            x = int(cursor.columnNumber() + 1)
            y = int(cursor.blockNumber() + 1)
            self.textbox.selectAll()
            self.textbox.setCurrentFont(font_selected)
            self.textbox.setFontPointSize(int(font_selected.pointSizeF()))
            cursor.clearSelection()
            self.textbox.setTextCursor(cursor)
            cursor.movePosition(x,y)

            # Update font properties
            font_selected_pre = font_selected
            FONT_BOLD = font_selected.bold()
            FONT_ITALIC = font_selected.italic()
            FONT_UNDERLINE = font_selected.underline()

            # Update theme-specific font settings
            if (MainGuiWindow.THEME == 'light'):
                MainGuiWindow.FONT_TEXT_SIZE_LIGHT = int(font_selected.pointSizeF())
                MainGuiWindow.FONT_TEXT_FAMILY_LIGHT = font_selected.family()
                print(MainGuiWindow.FONT_TEXT_SIZE_LIGHT, MainGuiWindow.FONT_TEXT_FAMILY_LIGHT, FONT_BOLD, FONT_ITALIC, FONT_UNDERLINE)

            elif (MainGuiWindow.THEME == 'dark'):
                MainGuiWindow.FONT_TEXT_SIZE_DARK = int(font_selected.pointSizeF())
                MainGuiWindow.FONT_TEXT_FAMILY_DARK = font_selected.family()
                print(MainGuiWindow.FONT_TEXT_SIZE_DARK, MainGuiWindow.FONT_TEXT_FAMILY_DARK, FONT_BOLD, FONT_ITALIC, FONT_UNDERLINE)

        else:
            font_selected_pre = font_selected
            print(font_selected.family())

    #//===================================================//
    def showColorPicker(self):
        """
        Opens the color picker dialog to allow the user to select a text color.
        """

        print('=== showColorPicker ===')
        from src.module.py_window_colorpicker import ColorPicker

        # Set preselected color based on the current theme
        if (MainGuiWindow.THEME == 'light'):
            TextGuiWindow.color_preselected = MainGuiWindow.FONT_TEXT_COLOR_LIGHT
        elif (MainGuiWindow.THEME == 'dark'):
            TextGuiWindow.color_preselected = MainGuiWindow.FONT_TEXT_COLOR_DARK
        print('color_preselected := ', TextGuiWindow.color_preselected)

        # Open the color picker window
        if self.window3 is None:
            self.window3 = ColorPicker()

        # Disable certain actions while the color picker is open
        self.window3.show()
        self.setting_action.setEnabled(False)
        self.set_textfont_action.setEnabled(False)
        self.set_textcolor_action.setEnabled(False)
        self.reset_action.setEnabled(False)
        self.preview_action.setEnabled(False)
        self.print_action.setEnabled(False)
        self.find_replace_action.setEnabled(False)
        self.font_color_action.setEnabled(False)
        self.font_color_highlight_action.setEnabled(False)
        self.updateEnabled_icon()

    #//===================================================//
    def setTextColor(self):
        """
        Applies the selected text color to the text box based on the current theme.
        """

        print('=== setTextColor ===')
        print('color_selected := ', TextGuiWindow.color_selected)

        # Update text color based on the theme
        if (MainGuiWindow.THEME == 'light'):
            MainGuiWindow.FONT_TEXT_COLOR_LIGHT = TextGuiWindow.color_selected
            MainGuiWindow.FontTextColorLightVar1 = MainGuiWindow.FONT_TEXT_COLOR_LIGHT
        elif (MainGuiWindow.THEME == 'dark'):
            MainGuiWindow.FONT_TEXT_COLOR_DARK = TextGuiWindow.color_selected
            MainGuiWindow.FontTextColorDarkVar1 = MainGuiWindow.FONT_TEXT_COLOR_DARK

        # Apply the selected color to the text box
        TextGuiWindow.textbox.setStyleSheet('QTextEdit { color: %s }' %TextGuiWindow.color_selected)

    ############################################################
    # LayoutBar
    ############################################################
    def previewText(self):
        """
        Opens a print preview dialog for the current text in the editor.
        """
        print('=== previewText ===')
        preview = QtPrintSupport.QPrintPreviewDialog()
        preview.paintRequested.connect(lambda p: self.textbox.print_(p))
        preview.exec_()

    #//===================================================//
    def printText(self):
        """
        Opens a print dialog to print the current text in the editor.
        """
        print('=== printText ===')
        dialog = QtPrintSupport.QPrintDialog()
        if dialog.exec_() == QDialog.Accepted:
            self.textbox.document().print_(dialog.printer())

    #//===================================================//
    def capitalizeCaseText(self):
        """
        Changes the selected text to capitalize case.
        """
        print('=== capitalizeCaseText ===')
        fmt = QTextCharFormat()
        fmt.setFontCapitalization(QFont.Capitalize)
        self.textbox.setCurrentCharFormat(fmt)

    #//===================================================//
    def lowerCaseText(self):
        """
        Changes the selected text to lowercase.
        """
        print('=== lowerCaseText ===')
        fmt = QTextCharFormat()
        fmt.setFontCapitalization(QFont.AllLowercase)
        self.textbox.setCurrentCharFormat(fmt)

    #//===================================================//
    def upperCaseText(self):
        """
        Changes the selected text to uppercase.
        """
        print('=== upperCaseText ===')
        fmt = QTextCharFormat()
        fmt.setFontCapitalization(QFont.AllUppercase)
        self.textbox.setCurrentCharFormat(fmt)

    #//===================================================//
    def alignLeftText(self):
        """
        Aligns the text to the left.
        """
        print('=== alignLeftText ===')
        self.textbox.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignAbsolute)

    #//===================================================//
    def alignRightText(self):
        """
        Aligns the text to the right.
        """
        print('=== alignRightText ===')
        self.textbox.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignAbsolute)

    #//===================================================//
    def alignCenterText(self):
        """
        Centers the text.
        """
        print('=== alignCenterText ===')
        self.textbox.setAlignment(Qt.AlignmentFlag.AlignCenter)

    #//===================================================//
    def alignJustifyText(self):
        """
        Justifies the text.
        """
        print('=== alignJustifyText ===')
        self.textbox.setAlignment(Qt.AlignmentFlag.AlignJustify)

    #//===================================================//
    def indentText(self):
        """
        Adds an indent (tab) to the selected text or current line.
        """
        print('=== indentText ===')
        cursor = self.textbox.textCursor()
        if cursor.hasSelection():
            cursor.clearSelection()
            cursor.insertText("\t")
            self.textbox.setTextCursor(cursor)
            cursor.clearSelection()
        else:
            cursor.insertText("\t")

    #//===================================================//
    def dedentText(self):
        """
        Removes an indent (tab) from the selected text or current line.
        """
        print('=== dedentText ===')
        cursor = self.textbox.textCursor()
        if cursor.hasSelection():
            cursor.clearSelection()
            self.handleDedent(cursor)
            self.textbox.setTextCursor(cursor)
            cursor.clearSelection()
        else:
            self.handleDedent(cursor)

    #//===================================================//
    def handleDedent(self,cursor):
        """
        Helper function to remove a single tab character from the current position.
        """
        print('=== handleDedent ===')
        cursor = self.textbox.textCursor()
        cursor.setPosition(cursor.position())
        cursor.movePosition(QTextCursor.Left, QTextCursor.KeepAnchor)
        character = str(cursor.selectedText())
        print('character := ', character)

        if character == "\t":
            self.textbox.textCursor().deletePreviousChar()

    #//===================================================//
    def bulletText(self):
        """
        Toggles bullet points for the selected text or current line.
        """
        print('=== bulletText ===')
        cursor = self.textbox.textCursor()
        blockFmt = cursor.blockFormat()
        listFmt = QTextListFormat()

        if cursor.currentList():
            print('=== removeList ===')
            listFmt = cursor.currentList().format()
            cursor = self.textbox.textCursor()
            cursor.movePosition(QTextCursor.StartOfLine,QTextCursor.MoveAnchor)
            self.textbox.setTextCursor(cursor)
            listFmt.setStyle(False)
            cursor.createList(listFmt)
            blockFmt.setObjectIndex(0)
            cursor.mergeBlockFormat(blockFmt)
        else:
            print('=== createList ===')
            listFmt.setIndent(blockFmt.indent() + 1)
            blockFmt.setIndent(0)
            cursor.setBlockFormat(blockFmt)
            listFmt.setStyle(QTextListFormat.ListDisc)
            cursor.createList(listFmt)

    #//===================================================//
    def numberText(self):
        """
        Toggles numbered lists for the selected text or current line.
        """
        print('=== numberText ===')
        cursor = self.textbox.textCursor()
        blockFmt = cursor.blockFormat()
        listFmt = QTextListFormat()

        if cursor.currentList():
            listFmt = cursor.currentList().format()
            cursor = self.textbox.textCursor()
            cursor.movePosition(QTextCursor.StartOfLine,QTextCursor.MoveAnchor)
            self.textbox.setTextCursor(cursor)
            listFmt.setStyle(False)
            cursor.createList(listFmt)
            blockFmt.setObjectIndex(0)
            cursor.mergeBlockFormat(blockFmt)
        else:
            listFmt.setIndent(blockFmt.indent() + 1)
            blockFmt.setIndent(0)
            cursor.setBlockFormat(blockFmt)
            listFmt.setStyle(QTextListFormat.ListDecimal)
            cursor.createList(listFmt)

    ############################################################
    # FormatBar
    ############################################################
    def fontColorText(self):
        """
        Opens a color picker to change the font color of the selected text.
        """
        print('=== fontColorChanged ===')
        color = QColorDialog.getColor()
        self.textbox.setTextColor(color)

    #//===================================================//
    def highlightColorText(self):
        """
        Opens a color picker to change the background color of the selected text.
        """
        print('=== highlightColorText ===')
        color = QColorDialog.getColor()
        self.textbox.setTextBackgroundColor(color)

    #//===================================================//
    def boldText(self):
        """
        Toggles bold formatting for the selected text.
        """
        print('=== boldText ===')
        if self.textbox.fontWeight() == QFont.Bold:
            self.textbox.setFontWeight(QFont.Normal)
        else:
            self.textbox.setFontWeight(QFont.Bold)

    #//===================================================//
    def italicText(self):
        """
        Toggles italic formatting for the selected text.
        """
        print('=== italicText ===')
        state = self.textbox.fontItalic()
        self.textbox.setFontItalic(not state)

    #//===================================================//
    def underlineText(self):
        """
        Toggles underline formatting for the selected text.
        """
        print('=== underlineText ===')
        state = self.textbox.fontUnderline()
        self.textbox.setFontUnderline(not state)

    #//===================================================//
    def strikeText(self):
        """
        Toggles strikethrough formatting for the selected text.
        """
        print('=== strikeText ===')
        fmt = self.textbox.currentCharFormat()
        fmt.setFontStrikeOut(not fmt.fontStrikeOut())
        self.textbox.setCurrentCharFormat(fmt)

    #//===================================================//
    def superscriptText(self):
        """
        Toggles superscript formatting for the selected text.
        """
        print('=== superscriptText ===')
        fmt = self.textbox.currentCharFormat()
        align = fmt.verticalAlignment()

        # Toggle between normal and superscript alignment
        if align == QTextCharFormat.AlignNormal:
            fmt.setVerticalAlignment(QTextCharFormat.AlignSuperScript)
        else:
            fmt.setVerticalAlignment(QTextCharFormat.AlignNormal)
        self.textbox.setCurrentCharFormat(fmt)

    #//===================================================//
    def subscriptText(self):
        """
        Toggles subscript formatting for the selected text.
        """
        print('=== subscriptText ===')
        fmt = self.textbox.currentCharFormat()
        align = fmt.verticalAlignment()

        # Toggle between normal and subscript alignment
        if align == QTextCharFormat.AlignNormal:
            fmt.setVerticalAlignment(QTextCharFormat.AlignSubScript)
        else:
            fmt.setVerticalAlignment(QTextCharFormat.AlignNormal)
        self.textbox.setCurrentCharFormat(fmt)

    #//===================================================//
    def toggleTabSpaces(self):
        """
        Toggles the visibility of tab and space markers in the text editor.
        """
        print('=== toggleTabSpaces ===')
        # Toggle paragraph text visibility based on the current theme
        if (MainGuiWindow.THEME == 'light'):
            MainGuiWindow.PARAGRAPH_TEXT_LIGHT = not(MainGuiWindow.PARAGRAPH_TEXT_LIGHT)
        elif (MainGuiWindow.THEME == 'dark'):
            MainGuiWindow.PARAGRAPH_TEXT_DARK = not(MainGuiWindow.PARAGRAPH_TEXT_DARK)

        print('PARAGRAPH_TEXT_LIGHT := ', MainGuiWindow.PARAGRAPH_TEXT_LIGHT)
        print('PARAGRAPH_TEXT_DARK := ', MainGuiWindow.PARAGRAPH_TEXT_DARK)
        self.showTabSpaces()

    #//===================================================//
    def showTabSpaces(self):
        """
        Updates the text editor to show or hide tab and space markers based on the current theme.
        """
        print('=== showTabSpaces ===')
        TextGuiWindow.option = QTextOption()
        TextGuiWindow.flag = QTextOption.ShowTabsAndSpaces | QTextOption.IncludeTrailingSpaces | QTextOption.ShowLineAndParagraphSeparators
        TextGuiWindow.wrapmode = QTextOption.WrapAtWordBoundaryOrAnywhere

        # Apply the appropriate flags based on the theme and visibility settings
        if (MainGuiWindow.THEME == 'light'):
            if MainGuiWindow.PARAGRAPH_TEXT_LIGHT:
                print('=== PARAGRAPH_TEXT_LIGHT ===')
                TextGuiWindow.option.setFlags(TextGuiWindow.flag)
                TextGuiWindow.option.setWrapMode(TextGuiWindow.wrapmode)
                TextGuiWindow.textbox.document().setDefaultTextOption(TextGuiWindow.option)
            else:
                TextGuiWindow.option.setFlags(TextGuiWindow.option.flags() & ~QTextOption.ShowTabsAndSpaces & ~QTextOption.IncludeTrailingSpaces & ~QTextOption.ShowLineAndParagraphSeparators)
                TextGuiWindow.option.setWrapMode(TextGuiWindow.wrapmode)
                TextGuiWindow.textbox.document().setDefaultTextOption(TextGuiWindow.option)
        elif (MainGuiWindow.THEME == 'dark'):
            if MainGuiWindow.PARAGRAPH_TEXT_DARK:
                TextGuiWindow.option.setFlags(TextGuiWindow.flag)
                TextGuiWindow.option.setWrapMode(TextGuiWindow.wrapmode)
                TextGuiWindow.textbox.document().setDefaultTextOption(self.option)
            else:
                TextGuiWindow.option.setFlags(TextGuiWindow.option.flags() & ~QTextOption.ShowTabsAndSpaces & ~QTextOption.ShowLineAndParagraphSeparators)
                TextGuiWindow.option.setWrapMode(TextGuiWindow.wrapmode)
                TextGuiWindow.textbox.document().setDefaultTextOption(TextGuiWindow.option)

    #//===================================================//
    def increaseOpacity(self):
        """
        Increases the text editor's opacity based on the current theme.
        """
        global flag_tabspaces, font_selected
        print('=== increaseOpacity ===')
        if MainGuiWindow.THEME == 'light':
            self.increaseOpacityLight()
        elif MainGuiWindow.THEME == 'dark':
            self.increaseOpacityDark()

    #//===================================================//
    def increaseOpacityLight(self):
        """
        Gradually increases the opacity for the light theme.
        """
        print('=== increaseOpacity ===')
        if OPACITY_TEXT_MIN <= MainGuiWindow.OPACITY_TEXT_LIGHT <= OPACITY_TEXT_MAX:
            # Increment opacity in predefined steps
            if MainGuiWindow.OPACITY_TEXT_LIGHT == 0.005:
                MainGuiWindow.OPACITY_TEXT_LIGHT = 0.2
            elif MainGuiWindow.OPACITY_TEXT_LIGHT == 0.2:
                MainGuiWindow.OPACITY_TEXT_LIGHT = 0.4
            elif MainGuiWindow.OPACITY_TEXT_LIGHT == 0.4:
                MainGuiWindow.OPACITY_TEXT_LIGHT = 0.6
            elif MainGuiWindow.OPACITY_TEXT_LIGHT == 0.6:
                MainGuiWindow.OPACITY_TEXT_LIGHT = 0.8
            elif MainGuiWindow.OPACITY_TEXT_LIGHT == 0.8:
                MainGuiWindow.OPACITY_TEXT_LIGHT = 1
                self.increase_opacity_action.setEnabled(False)

        self.decrease_opacity_action.setEnabled(True)
        print('OPACITY_TEXT_LIGHT := ', MainGuiWindow.OPACITY_TEXT_LIGHT)
        self.repaint()
        self.updateEnabled_icon()

    #//===================================================//
    def increaseOpacityDark(self):
        """
        Gradually increases the opacity for the dark theme.
        """
        print('=== increaseOpacityDark ===')
        if OPACITY_TEXT_MIN <= MainGuiWindow.OPACITY_TEXT_DARK <= OPACITY_TEXT_MAX:
            # Increment opacity in predefined steps
            if MainGuiWindow.OPACITY_TEXT_DARK == 0.005:
                MainGuiWindow.OPACITY_TEXT_DARK = 0.2
            elif MainGuiWindow.OPACITY_TEXT_DARK == 0.2:
                MainGuiWindow.OPACITY_TEXT_DARK = 0.4
            elif MainGuiWindow.OPACITY_TEXT_DARK == 0.4:
                MainGuiWindow.OPACITY_TEXT_DARK = 0.6
            elif MainGuiWindow.OPACITY_TEXT_DARK == 0.6:
                MainGuiWindow.OPACITY_TEXT_DARK = 0.8
            elif MainGuiWindow.OPACITY_TEXT_DARK == 0.8:
                MainGuiWindow.OPACITY_TEXT_DARK = 1
                self.increase_opacity_action.setEnabled(False)
        self.decrease_opacity_action.setEnabled(True)
        print('OPACITY_TEXT_DARK := ', MainGuiWindow.OPACITY_TEXT_DARK)
        self.repaint()
        self.updateEnabled_icon()

    #//===================================================//
    def decreaseOpacity(self):
        """
        Decreases the text editor's opacity based on the current theme.
        """
        global flag_tabspaces, font_selected
        print('=== decreaseOpacity ===')
        if MainGuiWindow.THEME == 'light':
            self.decreaseOpacityLight()
        elif MainGuiWindow.THEME == 'dark':
            self.decreaseOpacityDark()

    #//===================================================//
    def decreaseOpacityLight(self):
        """
        Gradually decreases the opacity for the light theme.
        """
        print('=== decreaseOpacityLight ===')
        if OPACITY_TEXT_MIN <= MainGuiWindow.OPACITY_TEXT_LIGHT <= OPACITY_TEXT_MAX:
            # Decrement opacity in predefined steps
            if MainGuiWindow.OPACITY_TEXT_LIGHT == 1.0:
                MainGuiWindow.OPACITY_TEXT_LIGHT = 0.8
            elif MainGuiWindow.OPACITY_TEXT_LIGHT == 0.8:
                MainGuiWindow.OPACITY_TEXT_LIGHT = 0.6
            elif MainGuiWindow.OPACITY_TEXT_LIGHT == 0.6:
                MainGuiWindow.OPACITY_TEXT_LIGHT = 0.4
            elif MainGuiWindow.OPACITY_TEXT_LIGHT == 0.4:
                MainGuiWindow.OPACITY_TEXT_LIGHT = 0.2
            elif MainGuiWindow.OPACITY_TEXT_LIGHT == 0.2:
                MainGuiWindow.OPACITY_TEXT_LIGHT = 0.005
                self.decrease_opacity_action.setEnabled(False)

        self.increase_opacity_action.setEnabled(True)
        print('OPACITY_TEXT_LIGHT := ', MainGuiWindow.OPACITY_TEXT_LIGHT)
        self.repaint()
        self.updateEnabled_icon()

    #//===================================================//
    def decreaseOpacityDark(self):
        """
        Gradually decreases the opacity for the dark theme.
        """
        print('=== decreaseOpacityDark ===')
        if OPACITY_TEXT_MIN <= MainGuiWindow.OPACITY_TEXT_DARK <= OPACITY_TEXT_MAX:
            # Decrement opacity in predefined steps
            if MainGuiWindow.OPACITY_TEXT_DARK == 1.0:
                MainGuiWindow.OPACITY_TEXT_DARK = 0.8
            elif MainGuiWindow.OPACITY_TEXT_DARK == 0.8:
                MainGuiWindow.OPACITY_TEXT_DARK = 0.6
            elif MainGuiWindow.OPACITY_TEXT_DARK == 0.6:
                MainGuiWindow.OPACITY_TEXT_DARK = 0.4
            elif MainGuiWindow.OPACITY_TEXT_DARK == 0.4:
                MainGuiWindow.OPACITY_TEXT_DARK = 0.2
            elif MainGuiWindow.OPACITY_TEXT_DARK == 0.2:
                MainGuiWindow.OPACITY_TEXT_DARK = 0.005
                self.decrease_opacity_action.setEnabled(False)

        self.increase_opacity_action.setEnabled(True)
        print('OPACITY_TEXT_DARK := ', MainGuiWindow.OPACITY_TEXT_DARK)
        self.repaint()
        self.updateEnabled_icon()

    #//===================================================//
    def highlight_text_ocr(self):
        """
        Highlights text in the editor based on OCR results.
        """
        from src.module.py_window_main import MainGuiWindow
        from src.func.py_main_function import UIFunctions

        print('=== highlight_text_ocr ===')
        UIFunctions.highlight_box_ocr(self,MainGuiWindow.selectedImage1Var)

    #//===================================================//
    def toggleFormatBar(self):
        """
        Toggles the visibility of the format bar.
        """
        print('=== toggleFormatBar ===')
        MainGuiWindow.FLAG_FORMATBAR = not MainGuiWindow.FLAG_FORMATBAR
        self.layoutbar.setVisible(MainGuiWindow.FLAG_FORMATBAR)
        self.formatbar.setVisible(MainGuiWindow.FLAG_FORMATBAR)

    #//===================================================//
    def toggleStatusBar(self):
        """
        Toggles the visibility of the status bar.
        """
        print('=== toggleStatusBar ===')
        MainGuiWindow.FLAG_STATUSBAR = not MainGuiWindow.FLAG_STATUSBAR
        self.labelStatusbar1.setVisible(MainGuiWindow.FLAG_STATUSBAR)
        self.labelStatusbar2.setVisible(MainGuiWindow.FLAG_STATUSBAR)
        self.labelStatusbar3.setVisible(MainGuiWindow.FLAG_STATUSBAR)

    #//===================================================//
    def resetSetting(self):
        """
        Resets the text editor settings to their default values.
        """
        print('=== resetSetting ===')
        # Reset theme to default
        if (MainGuiWindow.THEME == "light"):
            MainGuiWindow.ThemeLightColorVar1 = 0
            MainGuiWindow.THEME_LIGHT = "Default"
            self.set_LightTheme()
            self.read_StyleSheet()

        if (MainGuiWindow.THEME == "dark"):
            MainGuiWindow.ThemeDarkColorVar1 = 0
            MainGuiWindow.THEME_DARK = "Default"
            self.set_DarkTheme()
            self.read_StyleSheet()

        # Reset font size and family
        self.increase_textsize_action.setEnabled(True)
        self.decrease_textsize_action.setEnabled(True)


        cursor = self.textbox.textCursor()
        x = int(cursor.columnNumber() + 1)
        y = int(cursor.blockNumber() + 1)
        self.textbox.selectAll()
        self.textbox.setFontFamily(FONT_TEXT_FAMILY_INIT)
        self.textbox.setFontPointSize(FONT_TEXT_SIZE_INIT)
        cursor.clearSelection()
        self.textbox.setTextCursor(cursor)
        cursor.movePosition(x,y)

        if MainGuiWindow.THEME == 'light':
            MainGuiWindow.FONT_TEXT_SIZE_LIGHT = FONT_TEXT_SIZE_INIT
            MainGuiWindow.FONT_TEXT_FAMILY_LIGHT = FONT_TEXT_FAMILY_INIT
        elif MainGuiWindow.THEME == 'dark':
            MainGuiWindow.FONT_TEXT_SIZE_DARK = FONT_TEXT_SIZE_INIT
            MainGuiWindow.FONT_TEXT_FAMILY_DARK = FONT_TEXT_FAMILY_INIT

        # Reset font color
        if (MainGuiWindow.THEME == "light"):
            MainGuiWindow.FONT_TEXT_COLOR_LIGHT = '#000000'
            self.textbox.setStyleSheet('QTextEdit { color: %s }' %MainGuiWindow.FONT_TEXT_COLOR_LIGHT)
        elif (MainGuiWindow.THEME == "dark"):
            MainGuiWindow.FONT_TEXT_COLOR_DARK = '#FFFFFF'
            self.textbox.setStyleSheet('QTextEdit { color: %s }' %MainGuiWindow.FONT_TEXT_COLOR_DARK)

        # Reset opacity
        if MainGuiWindow.THEME == 'light':
            MainGuiWindow.OPACITY_TEXT_LIGHT = 1
        elif MainGuiWindow.THEME == 'dark':
            MainGuiWindow.OPACITY_TEXT_DARK = 1

        self.increase_opacity_action.setEnabled(False)
        self.decrease_opacity_action.setEnabled(True)
        self.repaint()
        self.updateEnabled_icon()

    #//===================================================//
    def settingConfig(self):
        """
        Opens the settings window and disables certain actions while it is active.
        """

        from src.module.py_window_setting import SettingWindow

        print('=== settingConfig ===')
        if self.window2 is None:
            self.window2 = SettingWindow()

        self.window2.show()
        self.window2.btnOK2.clicked.connect(self.close)

        # Disable actions while the settings window is open
        self.setting_action.setEnabled(False)
        self.set_textfont_action.setEnabled(False)
        self.set_textcolor_action.setEnabled(False)
        self.reset_action.setEnabled(False)
        self.preview_action.setEnabled(False)
        self.print_action.setEnabled(False)
        self.find_replace_action.setEnabled(False)
        self.font_color_action.setEnabled(False)
        self.font_color_highlight_action.setEnabled(False)
        self.updateEnabled_icon()

        from src.module.py_window_main import MainGuiWindow
        MainGuiWindow.settingAction.setEnabled(False)

    #//===================================================//
    def showToolBars(self):
        """
        Configures and displays the toolbar with actions based on the current theme.
        """

        print("=== showToolBars ===")
        self.toolbar.setIconSize(QSize(MainGuiWindow.TextEditorIconSizeVar1,MainGuiWindow.TextEditorIconSizeVar1))
        self.toolbar.setFixedHeight(HEIGHT_TB)

        # Configure toolbar actions based on the theme
        if MainGuiWindow.THEME == "light":
            TextGuiWindow.save_action = QAction(QIcon(":/resources/icon/toolbar/save1.png"),"Save",self)
            TextGuiWindow.undo_action = QAction(QIcon(":/resources/icon/toolbar/undo3.png"),"Undo",self)
            TextGuiWindow.redo_action = QAction(QIcon(":/resources/icon/toolbar/redo3.png"),"Redo",self)
            TextGuiWindow.cut_action = QAction(QIcon(":/resources/icon/toolbar/cut3.png"),"Cut",self)
            TextGuiWindow.copy_action = QAction(QIcon(":/resources/icon/toolbar/copy3.png"),"Copy",self)
            TextGuiWindow.paste_action = QAction(QIcon(":/resources/icon/toolbar/paste3.png"),"Paste",self)
            TextGuiWindow.delete_action = QAction(QIcon(":/resources/icon/toolbar/delete3.png"),"Delete",self)
            TextGuiWindow.selectall_action = QAction(QIcon(":/resources/icon/toolbar/selectall1.png"),"Select All",self)
            TextGuiWindow.decrease_textsize_action = QAction(QIcon(":/resources/icon/toolbar/font_decrease1.png"),"Decrease Font Size",self)
            TextGuiWindow.increase_textsize_action = QAction(QIcon(":/resources/icon/toolbar/font_increase1.png"),"Increase Font Size",self)
            TextGuiWindow.set_textfont_action = QAction(QIcon(":/resources/icon/toolbar/font_setting1.png"),"Set Font",self)
            TextGuiWindow.set_textcolor_action = QAction(QIcon(":/resources/icon/toolbar/font_color1.png"),"Set Font Color",self)
            TextGuiWindow.increase_opacity_action = QAction(QIcon(":/resources/icon/toolbar/opacity_increase3.png"),"Increase Opacity",self)
            TextGuiWindow.decrease_opacity_action = QAction(QIcon(":/resources/icon/toolbar/opacity_decrease1.png"),"Decrease Opacity",self)
            TextGuiWindow.reset_action = QAction(QIcon(":/resources/icon/toolbar/reset1.png"),"Reset Theme",self)
            TextGuiWindow.toggle_formatbar_action = QAction(QIcon(":/resources/icon/toolbar/toggle_fb3.png"),"Toggle Format Bar",self)
            TextGuiWindow.setting_action = QAction(QIcon(":/resources/icon/toolbar/setting1.png"),"Setting",self)

        elif MainGuiWindow.THEME == "dark":
            TextGuiWindow.save_action = QAction(QIcon(":/resources/icon/toolbar/save2.png"),"Save",self)
            TextGuiWindow.undo_action = QAction(QIcon(":/resources/icon/toolbar/undo1.png"),"Undo",self)
            TextGuiWindow.redo_action = QAction(QIcon(":/resources/icon/toolbar/redo1.png"),"Redo",self)
            TextGuiWindow.cut_action = QAction(QIcon(":/resources/icon/toolbar/cut1.png"),"Cut",self)
            TextGuiWindow.copy_action = QAction(QIcon(":/resources/icon/toolbar/copy1.png"),"Copy",self)
            TextGuiWindow.paste_action = QAction(QIcon(":/resources/icon/toolbar/paste1.png"),"Paste",self)
            TextGuiWindow.delete_action = QAction(QIcon(":/resources/icon/toolbar/delete1.png"),"Delete",self)
            TextGuiWindow.selectall_action = QAction(QIcon(":/resources/icon/toolbar/selectall2.png"),"Select All",self)
            TextGuiWindow.decrease_textsize_action = QAction(QIcon(":/resources/icon/toolbar/font2.png"),"Decrease Font Size",self)
            TextGuiWindow.increase_textsize_action = QAction(QIcon(":/resources/icon/toolbar/font5.png"),"Increase Font Size",self)
            TextGuiWindow.set_textfont_action = QAction(QIcon(":/resources/icon/toolbar/font_setting2.png"),"Set Font",self)
            TextGuiWindow.set_textcolor_action = QAction(QIcon(":/resources/icon/toolbar/font_color2.png"),"Font Color",self)
            TextGuiWindow.increase_opacity_action = QAction(QIcon(":/resources/icon/toolbar/opacity4.png"),"Increase Opacity",self)
            TextGuiWindow.decrease_opacity_action = QAction(QIcon(":/resources/icon/toolbar/opacity2.png"),"Decrease Opacity",self)
            TextGuiWindow.reset_action = QAction(QIcon(":/resources/icon/toolbar/reset2.png"),"Reset Theme",self)
            TextGuiWindow.toggle_formatbar_action = QAction(QIcon(":/resources/icon/toolbar/toggle_fb1.png"),"Toggle Format Bar",self)
            TextGuiWindow.setting_action = QAction(QIcon(":/resources/icon/toolbar/setting2.png"),"Setting",self)

        # Add tooltips and shortcuts for actions
        if (MainGuiWindow.TextEditorStatusBarVar1 == 1):
            self.save_action.setStatusTip('Save')
            self.undo_action.setStatusTip('Undo')
            self.redo_action.setStatusTip('Redo')
            self.cut_action.setStatusTip('Cut')
            self.copy_action.setStatusTip('Copy')
            self.paste_action.setStatusTip('Paste')
            self.delete_action.setStatusTip('Delete')
            self.selectall_action.setStatusTip('Select All')
            self.decrease_textsize_action.setStatusTip('Decrease Font Size')
            self.increase_textsize_action.setStatusTip('Increase Font Size')
            self.set_textfont_action.setStatusTip('Set Font')
            self.set_textcolor_action.setStatusTip('Set Font Color')
            self.decrease_opacity_action.setStatusTip('Decrease Opacity')
            self.increase_opacity_action.setStatusTip('Increase Opacity')
            self.reset_action.setStatusTip('Reset Theme')
            self.toggle_formatbar_action.setStatusTip('Toggle Format Bar')
            self.setting_action.setStatusTip('Setting')
        else:
            pass

        # Add actions to the toolbar
        self.save_action.setShortcut('Ctrl+S')
        self.save_action.setEnabled(True)
        self.save_action.triggered.connect(self.save_document)
        self.toolbar.addAction(self.save_action)

        self.spacer1 = QWidget(self)
        self.spacer1.setObjectName('spacer1')
        self.spacer1.setMinimumWidth(12)
        self.toolbar.addWidget(self.spacer1)

        self.undo_action.setShortcut('Ctrl+Z')
        self.undo_action.setEnabled(False)
        self.undo_action.triggered.connect(self.undoText)
        self.toolbar.addAction(self.undo_action)

        self.redo_action.setShortcut('Ctrl+Y')
        self.redo_action.setEnabled(False)
        self.redo_action.triggered.connect(self.redoText)
        self.toolbar.addAction(self.redo_action)

        self.cut_action.setShortcut('Ctrl+X')
        self.cut_action.setEnabled(False)
        self.cut_action.triggered.connect(self.cutText)
        self.toolbar.addAction(self.cut_action)

        self.copy_action.setShortcut('Ctrl+C')
        self.copy_action.setEnabled(False)
        self.copy_action.triggered.connect(self.copyText)
        self.toolbar.addAction(self.copy_action)

        self.paste_action.setShortcut('Ctrl+V')
        self.paste_action.setEnabled(False)
        self.paste_action.triggered.connect(self.pasteText)
        self.toolbar.addAction(self.paste_action)

        self.delete_action.setShortcut('Del')
        self.delete_action.setEnabled(False)
        self.delete_action.triggered.connect(self.deleteText)
        self.toolbar.addAction(self.delete_action)

        self.selectall_action.setShortcut('Ctrl+A')
        self.selectall_action.triggered.connect(self.selectAllText)
        self.toolbar.addAction(self.selectall_action)

        self.spacer2 = QWidget(self)
        self.spacer2.setObjectName('spacer2')
        self.spacer2.setMinimumWidth(12)
        self.toolbar.addWidget(self.spacer2)

        self.decrease_textsize_action.triggered.connect(self.decreaseTextSize)
        self.toolbar.addAction(self.decrease_textsize_action)
        self.increase_textsize_action.triggered.connect(self.increaseTextSize)
        self.toolbar.addAction(self.increase_textsize_action)

        self.set_textfont_action.triggered.connect(self.setTextFont)
        self.toolbar.addAction(self.set_textfont_action)
        self.set_textcolor_action.triggered.connect(self.showColorPicker)
        self.toolbar.addAction(self.set_textcolor_action)

        self.decrease_opacity_action.triggered.connect(self.decreaseOpacity)
        self.toolbar.addAction(self.decrease_opacity_action)
        self.increase_opacity_action.triggered.connect(self.increaseOpacity)
        self.toolbar.addAction(self.increase_opacity_action)

        self.spacer3 = QWidget(self)
        self.spacer3.setObjectName('spacer3')
        self.spacer3.setMinimumWidth(12)
        self.toolbar.addWidget(self.spacer3)

        self.reset_action.triggered.connect(self.resetSetting)
        self.toolbar.addAction(self.reset_action)
        self.toggle_formatbar_action.triggered.connect(self.toggleFormatBar)
        self.toolbar.addAction(self.toggle_formatbar_action)
        self.setting_action.triggered.connect(self.settingConfig)
        self.toolbar.addAction(self.setting_action)

        self.spacer1n = QWidget(self)
        self.spacer1n.setObjectName('spacer1n')
        self.spacer1n.setMinimumWidth(5)
        self.toolbar.addWidget(self.spacer1n)

    #//===================================================//
    def showLayoutBars(self):
        """
        Configures and displays the layout bar with actions based on the current theme.
        """

        print("=== showFormatBars ===")
        from src.module.py_window_main import MainGuiWindow

        # Set layout bar icon size and height
        self.layoutbar.setIconSize(QSize(MainGuiWindow.TextEditorIconSizeVar1,MainGuiWindow.TextEditorIconSizeVar1))
        self.layoutbar.setFixedHeight(HEIGHT_LB)

        # Configure layout bar actions based on the theme
        if MainGuiWindow.THEME == "light":
            TextGuiWindow.preview_action = QAction(QIcon(":/resources/icon/layoutbar/preview1.png"),"Preview",self)
            TextGuiWindow.print_action = QAction(QIcon(":/resources/icon/layoutbar/print1.png"),"Print",self)
            TextGuiWindow.lowercase_action = QAction(QIcon(":/resources/icon/layoutbar/lower1.png"),"Lower Case",self)
            TextGuiWindow.uppercase_action = QAction(QIcon(":/resources/icon/layoutbar/upper1.png"),"Upper Case",self)
            TextGuiWindow.capitalizecase_action = QAction(QIcon(":/resources/icon/layoutbar/capitalize1.png"),"Capitalize Case",self)
            TextGuiWindow.align_left_action = QAction(QIcon(":/resources/icon/layoutbar/align_left3.png"),"Align Left",self)
            TextGuiWindow.align_center_action = QAction(QIcon(":/resources/icon/layoutbar/align_center3.png"),"Align Center",self)
            TextGuiWindow.align_right_action = QAction(QIcon(":/resources/icon/layoutbar/align_right3.png"),"Align Right",self)
            TextGuiWindow.align_justify_action = QAction(QIcon(":/resources/icon/layoutbar/align_justify3.png"),"Align Justify",self)
            TextGuiWindow.indent_action = QAction(QIcon(":/resources/icon/layoutbar/indent3.png"),"Increase Indent",self)
            TextGuiWindow.dedent_action = QAction(QIcon(":/resources/icon/layoutbar/dedent3.png"),"Decrease Indent",self)
            TextGuiWindow.bullet_action = QAction(QIcon(":/resources/icon/layoutbar/bullet3.png"),"Bullets",self)
            TextGuiWindow.number_action = QAction(QIcon(":/resources/icon/layoutbar/number3.png"),"Numbering",self)
            TextGuiWindow.paragraph_action = QAction(QIcon(":/resources/icon/layoutbar/paragraph1.png"),"Paragraph Marks",self)
            TextGuiWindow.find_replace_action = QAction(QIcon(":/resources/icon/layoutbar/find1.png"),"Find && Replace",self)
            TextGuiWindow.toggle_statusbar_action = QAction(QIcon(":/resources/icon/layoutbar/toggle_sb3.png"),"Toggle Status Bar",self)

        elif MainGuiWindow.THEME == "dark":
            TextGuiWindow.preview_action = QAction(QIcon(":/resources/icon/layoutbar/preview2.png"),"Preview",self)
            TextGuiWindow.print_action = QAction(QIcon(":/resources/icon/layoutbar/print2.png"),"Print",self)
            TextGuiWindow.lowercase_action = QAction(QIcon(":/resources/icon/layoutbar/lower3.png"),"Lower Case",self)
            TextGuiWindow.uppercase_action = QAction(QIcon(":/resources/icon/layoutbar/upper3.png"),"Upper Case",self)
            TextGuiWindow.capitalizecase_action = QAction(QIcon(":/resources/icon/layoutbar/capitalize3.png"),"Capitalize Case",self)
            TextGuiWindow.align_left_action = QAction(QIcon(":/resources/icon/layoutbar/align_left3.png"),"Align Left",self)
            TextGuiWindow.align_center_action = QAction(QIcon(":/resources/icon/layoutbar/align_center3.png"),"Align Center",self)
            TextGuiWindow.align_right_action = QAction(QIcon(":/resources/icon/layoutbar/align_right3.png"),"Align Right",self)
            TextGuiWindow.align_justify_action = QAction(QIcon(":/resources/icon/layoutbar/align_justify3.png"),"Align Justify",self)
            TextGuiWindow.indent_action = QAction(QIcon(":/resources/icon/layoutbar/indent3.png"),"Increase Indent",self)
            TextGuiWindow.dedent_action = QAction(QIcon(":/resources/icon/layoutbar/dedent3.png"),"Decrease Indent",self)
            TextGuiWindow.bullet_action = QAction(QIcon(":/resources/icon/layoutbar/bullet3.png"),"Bullets",self)
            TextGuiWindow.number_action = QAction(QIcon(":/resources/icon/layoutbar/number3.png"),"Numbering",self)
            TextGuiWindow.paragraph_action = QAction(QIcon(":/resources/icon/layoutbar/paragraph1.png"),"Paragraph Marks",self)
            TextGuiWindow.find_replace_action = QAction(QIcon(":/resources/icon/layoutbar/find1.png"),"Find && Replace",self)
            TextGuiWindow.toggle_statusbar_action = QAction(QIcon(":/resources/icon/layoutbar/toggle_sb1.png"),"Toggle Status Bar",self)

        # Add tooltips for actions if the status bar is enabled
        if (MainGuiWindow.TextEditorStatusBarVar1 == 1):
            self.preview_action.setStatusTip('Preview')
            self.print_action.setStatusTip('Print')
            self.lowercase_action.setStatusTip('Lower Case')
            self.capitalizecase_action.setStatusTip('Capitalize Case')
            self.uppercase_action.setStatusTip('Upper Case')
            self.align_left_action.setStatusTip('Align Left')
            self.align_center_action.setStatusTip('Align Center')
            self.align_right_action.setStatusTip('Align Right')
            self.align_justify_action.setStatusTip('Align Justify')
            self.indent_action.setStatusTip('Increase Indent')
            self.dedent_action.setStatusTip('Decrease Indent')
            self.bullet_action.setStatusTip('Bullets')
            self.number_action.setStatusTip('Numbering')
            self.paragraph_action.setStatusTip('Paragraph Marks')
            self.find_replace_action.setStatusTip('Find & Replace')
            self.toggle_statusbar_action.setStatusTip('Toggle Status Bar')
        else:
            pass

        # Add actions to the layout bar
        self.preview_action.setShortcut('Ctrl+H')
        self.preview_action.triggered.connect(self.previewText)
        self.layoutbar.addAction(self.preview_action)

        self.print_action.setShortcut('Ctrl+P')
        self.print_action.triggered.connect(self.printText)
        self.layoutbar.addAction(self.print_action)

        # Add spacers for better layout organization
        self.spacer5 = QWidget(self)
        self.spacer5.setObjectName('spacer5')
        self.spacer5.setMinimumWidth(12)
        self.layoutbar.addWidget(self.spacer5)

        # Configure text transformation actions
        self.lowercase_action.setEnabled(False)
        self.lowercase_action.triggered.connect(self.lowerCaseText)
        self.layoutbar.addAction(self.lowercase_action)

        self.capitalizecase_action.setEnabled(False)
        self.capitalizecase_action.triggered.connect(self.capitalizeCaseText)
        self.layoutbar.addAction(self.capitalizecase_action)

        self.uppercase_action.setEnabled(False)
        self.uppercase_action.triggered.connect(self.upperCaseText)
        self.layoutbar.addAction(self.uppercase_action)

        self.spacer6 = QWidget(self)
        self.spacer6.setObjectName('spacer6')
        self.spacer6.setMinimumWidth(12)
        self.layoutbar.addWidget(self.spacer6)

        # Configure text alignment actions
        self.align_left_action.triggered.connect(self.alignLeftText)
        self.layoutbar.addAction(self.align_left_action)

        self.align_center_action.triggered.connect(self.alignCenterText)
        self.layoutbar.addAction(self.align_center_action)

        self.align_right_action.triggered.connect(self.alignRightText)
        self.layoutbar.addAction(self.align_right_action)

        self.align_justify_action.triggered.connect(self.alignJustifyText)
        self.layoutbar.addAction(self.align_justify_action)

        self.spacer7 = QWidget(self)
        self.spacer7.setObjectName('spacer7')
        self.spacer7.setMinimumWidth(12)
        self.layoutbar.addWidget(self.spacer7)

        # Configure indentation actions
        self.indent_action.triggered.connect(self.indentText)
        self.layoutbar.addAction(self.indent_action)

        self.dedent_action.triggered.connect(self.dedentText)
        self.layoutbar.addAction(self.dedent_action)

        # Configure list actions
        self.bullet_action.triggered.connect(self.bulletText)
        self.layoutbar.addAction(self.bullet_action)

        self.number_action.triggered.connect(self.numberText)
        self.layoutbar.addAction(self.number_action)

        # Configure paragraph and find/replace actions
        self.paragraph_action.setShortcut('Ctrl+*')
        self.paragraph_action.triggered.connect(self.toggleTabSpaces)
        self.layoutbar.addAction(self.paragraph_action)

        self.spacer8 = QWidget(self)
        self.spacer8.setObjectName('spacer8')
        self.spacer8.setMinimumWidth(12)
        self.layoutbar.addWidget(self.spacer8)

        self.find_replace_action.setShortcut('Ctrl+F')
        self.find_replace_action.triggered.connect(self.findreplaceText)
        self.layoutbar.addAction(self.find_replace_action)

        # Configure status bar toggle action
        self.toggle_statusbar_action.setShortcut('Ctrl+M')
        self.toggle_statusbar_action.triggered.connect(self.toggleStatusBar)
        self.layoutbar.addAction(self.toggle_statusbar_action)

        self.spacer2n = QWidget(self)
        self.spacer2n.setObjectName('spacer2n')
        self.spacer2n.setMinimumWidth(5)
        self.layoutbar.addWidget(self.spacer2n)

    #//===================================================//
    def showFormatBars(self):
        """
        Configures and displays the format bar with actions based on the current theme.
        """

        print("=== showFormatBars ===")
        from src.module.py_window_main import MainGuiWindow

        # Set format bar icon size and height
        self.formatbar.setIconSize(QSize(MainGuiWindow.TextEditorIconSizeVar1,MainGuiWindow.TextEditorIconSizeVar1))
        self.formatbar.setFixedHeight(HEIGHT_FB)

        # Configure format bar actions based on the theme
        if MainGuiWindow.THEME == "light":
            # Actions for light theme
            TextGuiWindow.bold_action = QAction(QIcon(":/resources/icon/formatbar/bold3.png"),"Bold",self)
            TextGuiWindow.italic_action = QAction(QIcon(":/resources/icon/formatbar/italic3.png"),"Italic",self)
            TextGuiWindow.under_action = QAction(QIcon(":/resources/icon/formatbar/underline3.png"),"Underline",self)
            TextGuiWindow.strike_action = QAction(QIcon(":/resources/icon/formatbar/strike3.png"),"Strikethrough",self)
            TextGuiWindow.sub_action = QAction(QIcon(":/resources/icon/formatbar/subscript3.png"),"Subscript",self)
            TextGuiWindow.super_action = QAction(QIcon(":/resources/icon/formatbar/superscript3.png"),"Superscript",self)
            TextGuiWindow.font_color_action = QAction(QIcon(":/resources/icon/formatbar/font_color3.png"),"Font Color",self)
            TextGuiWindow.font_color_highlight_action = QAction(QIcon(":/resources/icon/formatbar/highlight3.png"),"Text Highlight Color",self)

        elif MainGuiWindow.THEME == "dark":
            # Actions for dark theme
            TextGuiWindow.bold_action = QAction(QIcon(":/resources/icon/formatbar/bold1.png"),"Bold",self)
            TextGuiWindow.italic_action = QAction(QIcon(":/resources/icon/formatbar/italic1.png"),"Italic",self)
            TextGuiWindow.under_action = QAction(QIcon(":/resources/icon/formatbar/underline1.png"),"Underline",self)
            TextGuiWindow.strike_action = QAction(QIcon(":/resources/icon/formatbar/strike1.png"),"Strikethrough",self)
            TextGuiWindow.sub_action = QAction(QIcon(":/resources/icon/formatbar/subscript1.png"),"Subscript",self)
            TextGuiWindow.super_action = QAction(QIcon(":/resources/icon/formatbar/superscript1.png"),"Superscript",self)
            TextGuiWindow.font_color_action = QAction(QIcon(":/resources/icon/formatbar/font_color1.png"),"Font Color",self)
            TextGuiWindow.font_color_highlight_action = QAction(QIcon(":/resources/icon/formatbar/highlight1.png"),"Text Highlight Color",self)

        # Add tooltips for actions if the status bar is enabled
        if (MainGuiWindow.TextEditorStatusBarVar1 == 1):
            self.bold_action.setStatusTip('Bold')
            self.italic_action.setObjectName('Italic')
            self.under_action.setStatusTip('Underline')
            self.strike_action.setStatusTip('Strikethrough')
            self.sub_action.setStatusTip('Subscript')
            self.super_action.setStatusTip('Superscript')
            self.font_color_action.setStatusTip('Font Color')
            self.font_color_highlight_action.setStatusTip('Text Highlight Color')
        else:
            pass

        # Initialize font family dropdown
        self.fontBox = QFontComboBox(self.formatbar)
        self.fontBox.setMinimumHeight(20)
        self.fontBox.setMaximumWidth(185)
        self.fontBox.setMinimumWidth(185)
        self.fontBox.setMaxVisibleItems(15)

        # Set default font family based on theme
        if (MainGuiWindow.THEME == 'light'):
            self.fontBox.setCurrentText(MainGuiWindow.FONT_TEXT_FAMILY_LIGHT)
        elif (MainGuiWindow.THEME == 'dark'):
            self.fontBox.setCurrentText(MainGuiWindow.FONT_TEXT_FAMILY_LIGHT)

        self.fontBox.activated.connect(self.changedfontFamily)

        # Initialize font size dropdown
        font_size_list = ['6','7','8','10','12','14','18','24','28','36','48']
        self.fontSize = QComboBox(self.formatbar)
        self.fontSize.setMinimumHeight(20)
        self.fontSize.setMinimumWidth(38)
        self.fontSize.setObjectName("comboBox1")
        self.fontSize.setEditable(True)
        self.fontSize.addItems(font_size_list)
        self.fontSize.setMaxVisibleItems(11)

        # Set default font size based on theme
        if (MainGuiWindow.THEME == 'light'):
            self.fontSize.setCurrentText(str(MainGuiWindow.FONT_TEXT_SIZE_LIGHT))
        else:
            self.fontSize.setCurrentText(str(MainGuiWindow.FONT_TEXT_SIZE_DARK))

        self.fontSize.activated.connect(self.changedfontSize)

        # Add font family and size widgets to the format bar
        self.formatbar.addWidget(self.fontBox)
        self.formatbar.addSeparator()
        self.formatbar.addWidget(self.fontSize)
        self.formatbar.addSeparator()

        # Configure and add text formatting actions
        self.bold_action.setShortcut('Ctrl+B')
        self.bold_action.setEnabled(False)
        self.bold_action.triggered.connect(self.boldText)
        self.formatbar.addAction(self.bold_action)

        self.italic_action.setStatusTip('Italic')
        self.italic_action.setShortcut('Ctrl+I')
        self.italic_action.setEnabled(False)
        self.italic_action.triggered.connect(self.italicText)
        self.formatbar.addAction(self.italic_action)

        self.under_action.setShortcut('Ctrl+U')
        self.under_action.setEnabled(False)
        self.under_action.triggered.connect(self.underlineText)
        self.formatbar.addAction(self.under_action)

        self.strike_action.setEnabled(False)
        self.strike_action.triggered.connect(self.strikeText)
        self.formatbar.addAction(self.strike_action)

        self.sub_action.setShortcut('Ctrl+=')
        self.sub_action.setEnabled(False)
        self.sub_action.triggered.connect(self.subscriptText)
        self.formatbar.addAction(self.sub_action)

        self.super_action.setShortcut('Ctrl+Shift++')
        self.super_action.setEnabled(False)
        self.super_action.triggered.connect(self.superscriptText)
        self.formatbar.addAction(self.super_action)

        # Add spacers for better layout organization
        self.spacer9 = QWidget(self)
        self.spacer9.setObjectName('spacer9')
        self.spacer9.setMinimumWidth(12)
        self.formatbar.addWidget(self.spacer9)

        # Configure and add font color actions
        self.font_color_action.setEnabled(False)
        self.font_color_action.triggered.connect(self.fontColorText)
        self.formatbar.addAction(self.font_color_action)

        self.font_color_highlight_action.setEnabled(False)
        self.font_color_highlight_action.triggered.connect(self.highlightColorText)
        self.formatbar.addAction(self.font_color_highlight_action)

        self.spacer3n = QWidget(self)
        self.spacer3n.setObjectName('spacer3n')
        self.spacer3n.setMinimumWidth(5)
        self.formatbar.addWidget(self.spacer3n)

    # //===================================================//
    def updateEnabled_icon(self):
        """
        Updates the icons of toolbar, layout bar, and format bar actions
        based on their enabled/disabled state and the current theme.
        """

        print('=== updateEnabled_icon ===')
        if MainGuiWindow.THEME == "light":
            # Update toolbar icons for light theme
            if (TextGuiWindow.save_action.isEnabled()):
                TextGuiWindow.toolbar.widgetForAction(TextGuiWindow.save_action).setStyleSheet('qproperty-icon: url(:/resources/icon/toolbar/save1.png)')
            else:
                TextGuiWindow.toolbar.widgetForAction(TextGuiWindow.save_action).setStyleSheet('qproperty-icon: url(:/resources/icon/toolbar/save3.png)')

            if (TextGuiWindow.undo_action.isEnabled()):
                TextGuiWindow.toolbar.widgetForAction(TextGuiWindow.undo_action).setStyleSheet('qproperty-icon: url(:/resources/icon/toolbar/undo1.png)')
            else:
                TextGuiWindow.toolbar.widgetForAction(TextGuiWindow.undo_action).setStyleSheet('qproperty-icon: url(:/resources/icon/toolbar/undo3.png)')

            if (TextGuiWindow.redo_action.isEnabled()):
                TextGuiWindow.toolbar.widgetForAction(TextGuiWindow.redo_action).setStyleSheet('qproperty-icon: url(:/resources/icon/toolbar/redo1.png)')
            else:
                TextGuiWindow.toolbar.widgetForAction(TextGuiWindow.redo_action).setStyleSheet('qproperty-icon: url(:/resources/icon/toolbar/redo3.png)')

            if (TextGuiWindow.cut_action.isEnabled()):
                TextGuiWindow.toolbar.widgetForAction(TextGuiWindow.cut_action).setStyleSheet('qproperty-icon: url(:/resources/icon/toolbar/cut1.png)')
            else:
                TextGuiWindow.toolbar.widgetForAction(TextGuiWindow.cut_action).setStyleSheet('qproperty-icon: url(:/resources/icon/toolbar/cut3.png)')

            if (TextGuiWindow.copy_action.isEnabled()):
                TextGuiWindow.toolbar.widgetForAction(TextGuiWindow.copy_action).setStyleSheet('qproperty-icon: url(:/resources/icon/toolbar/copy1.png)')
            else:
                TextGuiWindow.toolbar.widgetForAction(TextGuiWindow.copy_action).setStyleSheet('qproperty-icon: url(:/resources/icon/toolbar/copy3.png)')

            if (TextGuiWindow.paste_action.isEnabled()):
                TextGuiWindow.toolbar.widgetForAction(TextGuiWindow.paste_action).setStyleSheet('qproperty-icon: url(:/resources/icon/toolbar/paste1.png)')
            else:
                TextGuiWindow.toolbar.widgetForAction(TextGuiWindow.paste_action).setStyleSheet('qproperty-icon: url(:/resources/icon/toolbar/paste3.png)')

            if (TextGuiWindow.delete_action.isEnabled()):
                TextGuiWindow.toolbar.widgetForAction(TextGuiWindow.delete_action).setStyleSheet('qproperty-icon: url(:/resources/icon/toolbar/delete1.png)')
            else:
                TextGuiWindow.toolbar.widgetForAction(TextGuiWindow.delete_action).setStyleSheet('qproperty-icon: url(:/resources/icon/toolbar/delete3.png)')

            if (TextGuiWindow.selectall_action.isEnabled()):
                TextGuiWindow.toolbar.widgetForAction(TextGuiWindow.selectall_action).setStyleSheet('qproperty-icon: url(:/resources/icon/toolbar/selectall1.png)')
            else:
                TextGuiWindow.toolbar.widgetForAction(TextGuiWindow.selectall_action).setStyleSheet('qproperty-icon: url(:/resources/icon/toolbar/selectall3.png)')

            if (TextGuiWindow.decrease_textsize_action.isEnabled()):
                TextGuiWindow.toolbar.widgetForAction(TextGuiWindow.decrease_textsize_action).setStyleSheet('qproperty-icon: url(:/resources/icon/toolbar/font_decrease1.png)')
            else:
                TextGuiWindow.toolbar.widgetForAction(TextGuiWindow.decrease_textsize_action).setStyleSheet('qproperty-icon: url(:/resources/icon/toolbar/font_decrease3.png)')

            if (TextGuiWindow.increase_textsize_action.isEnabled()):
                TextGuiWindow.toolbar.widgetForAction(TextGuiWindow.increase_textsize_action).setStyleSheet('qproperty-icon: url(:/resources/icon/toolbar/font_increase1.png)')
            else:
                TextGuiWindow.toolbar.widgetForAction(TextGuiWindow.increase_textsize_action).setStyleSheet('qproperty-icon: url(:/resources/icon/toolbar/font_increase3.png)')

            if (TextGuiWindow.set_textfont_action.isEnabled()):
                TextGuiWindow.toolbar.widgetForAction(TextGuiWindow.set_textfont_action).setStyleSheet('qproperty-icon: url(:/resources/icon/toolbar/font_setting1.png)')
            else:
                TextGuiWindow.toolbar.widgetForAction(TextGuiWindow.set_textfont_action).setStyleSheet('qproperty-icon: url(:/resources/icon/toolbar/font_setting3.png)')

            if (TextGuiWindow.set_textcolor_action.isEnabled()):
                TextGuiWindow.toolbar.widgetForAction(TextGuiWindow.set_textcolor_action).setStyleSheet('qproperty-icon: url(:/resources/icon/toolbar/font_color1.png)')
            else:
                TextGuiWindow.toolbar.widgetForAction(TextGuiWindow.set_textcolor_action).setStyleSheet('qproperty-icon: url(:/resources/icon/toolbar/font_color3.png)')

            if (TextGuiWindow.decrease_opacity_action.isEnabled()):
                TextGuiWindow.toolbar.widgetForAction(TextGuiWindow.decrease_opacity_action).setStyleSheet('qproperty-icon: url(:/resources/icon/toolbar/opacity_decrease1.png)')
            else:
                TextGuiWindow.toolbar.widgetForAction(TextGuiWindow.decrease_opacity_action).setStyleSheet('qproperty-icon: url(:/resources/icon/toolbar/opacity_decrease3.png)')

            if (TextGuiWindow.increase_opacity_action.isEnabled()):
                TextGuiWindow.toolbar.widgetForAction(TextGuiWindow.increase_opacity_action).setStyleSheet('qproperty-icon: url(:/resources/icon/toolbar/opacity_increase1.png)')
            else:
                TextGuiWindow.toolbar.widgetForAction(TextGuiWindow.increase_opacity_action).setStyleSheet('qproperty-icon: url(:/resources/icon/toolbar/opacity_increase3.png)')

            if (TextGuiWindow.toggle_formatbar_action.isEnabled()):
                TextGuiWindow.toolbar.widgetForAction(TextGuiWindow.toggle_formatbar_action).setStyleSheet('qproperty-icon: url(:/resources/icon/toolbar/toggle_fb1.png)')
            else:
                TextGuiWindow.toolbar.widgetForAction(TextGuiWindow.toggle_formatbar_action).setStyleSheet('qproperty-icon: url(:/resources/icon/toolbar/toggle_fb3.png)')

            if (TextGuiWindow.reset_action.isEnabled()):
                TextGuiWindow.toolbar.widgetForAction(TextGuiWindow.reset_action).setStyleSheet('qproperty-icon: url(:/resources/icon/toolbar/reset1.png)')
            else:
                TextGuiWindow.toolbar.widgetForAction(TextGuiWindow.reset_action).setStyleSheet('qproperty-icon: url(:/resources/icon/toolbar/reset3.png)')

            if (TextGuiWindow.setting_action.isEnabled()):
                TextGuiWindow.toolbar.widgetForAction(TextGuiWindow.setting_action).setStyleSheet('qproperty-icon: url(:/resources/icon/toolbar/setting1.png)')
            else:
                TextGuiWindow.toolbar.widgetForAction(TextGuiWindow.setting_action).setStyleSheet('qproperty-icon: url(:/resources/icon/toolbar/setting3.png)')


            # Update layout bar icons for light theme
            if (TextGuiWindow.print_action.isEnabled()):
                TextGuiWindow.layoutbar.widgetForAction(TextGuiWindow.print_action).setStyleSheet('qproperty-icon: url(:/resources/icon/layoutbar/print1.png)')
            else:
                TextGuiWindow.layoutbar.widgetForAction(TextGuiWindow.print_action).setStyleSheet('qproperty-icon: url(:/resources/icon/layoutbar/print3.png)')

            if (TextGuiWindow.preview_action.isEnabled()):
                TextGuiWindow.layoutbar.widgetForAction(TextGuiWindow.preview_action).setStyleSheet('qproperty-icon: url(:/resources/icon/layoutbar/preview1.png)')
            else:
                TextGuiWindow.layoutbar.widgetForAction(TextGuiWindow.preview_action).setStyleSheet('qproperty-icon: url(:/resources/icon/layoutbar/preview3.png)')

            if (TextGuiWindow.lowercase_action.isEnabled()):
                TextGuiWindow.layoutbar.widgetForAction(TextGuiWindow.lowercase_action).setStyleSheet('qproperty-icon: url(:/resources/icon/layoutbar/lower1.png)')
            else:
                TextGuiWindow.layoutbar.widgetForAction(TextGuiWindow.lowercase_action).setStyleSheet('qproperty-icon: url(:/resources/icon/layoutbar/lower3.png)')

            if (TextGuiWindow.capitalizecase_action.isEnabled()):
                TextGuiWindow.layoutbar.widgetForAction(TextGuiWindow.capitalizecase_action).setStyleSheet('qproperty-icon: url(:/resources/icon/layoutbar/capitalize1.png)')
            else:
                TextGuiWindow.layoutbar.widgetForAction(TextGuiWindow.capitalizecase_action).setStyleSheet('qproperty-icon: url(:/resources/icon/layoutbar/capitalize3.png)')

            if (TextGuiWindow.uppercase_action.isEnabled()):
                TextGuiWindow.layoutbar.widgetForAction(TextGuiWindow.uppercase_action).setStyleSheet('qproperty-icon: url(:/resources/icon/layoutbar/upper1.png)')
            else:
                TextGuiWindow.layoutbar.widgetForAction(TextGuiWindow.uppercase_action).setStyleSheet('qproperty-icon: url(:/resources/icon/layoutbar/upper3.png)')

            if (TextGuiWindow.align_left_action.isEnabled()):
                TextGuiWindow.layoutbar.widgetForAction(TextGuiWindow.align_left_action).setStyleSheet('qproperty-icon: url(:/resources/icon/layoutbar/align_left1.png)')
            else:
                TextGuiWindow.layoutbar.widgetForAction(TextGuiWindow.align_left_action).setStyleSheet('qproperty-icon: url(:/resources/icon/layoutbar/align_left3.png)')

            if (TextGuiWindow.align_right_action.isEnabled()):
                TextGuiWindow.layoutbar.widgetForAction(TextGuiWindow.align_right_action).setStyleSheet('qproperty-icon: url(:/resources/icon/layoutbar/align_right1.png)')
            else:
                TextGuiWindow.layoutbar.widgetForAction(TextGuiWindow.align_right_action).setStyleSheet('qproperty-icon: url(:/resources/icon/layoutbar/align_right3.png)')

            if (TextGuiWindow.align_justify_action.isEnabled()):
                TextGuiWindow.layoutbar.widgetForAction(TextGuiWindow.align_justify_action).setStyleSheet('qproperty-icon: url(:/resources/icon/layoutbar/align_justify1.png)')
            else:
                TextGuiWindow.layoutbar.widgetForAction(TextGuiWindow.align_justify_action).setStyleSheet('qproperty-icon: url(:/resources/icon/layoutbar/align_justify3.png)')

            if (TextGuiWindow.align_center_action.isEnabled()):
                TextGuiWindow.layoutbar.widgetForAction(TextGuiWindow.align_center_action).setStyleSheet('qproperty-icon: url(:/resources/icon/layoutbar/align_center1.png)')
            else:
                TextGuiWindow.layoutbar.widgetForAction(TextGuiWindow.align_center_action).setStyleSheet('qproperty-icon: url(:/resources/icon/layoutbar/align_center3.png)')

            if (TextGuiWindow.indent_action.isEnabled()):
                TextGuiWindow.layoutbar.widgetForAction(TextGuiWindow.indent_action).setStyleSheet('qproperty-icon: url(:/resources/icon/layoutbar/indent1.png)')
            else:
                TextGuiWindow.layoutbar.widgetForAction(TextGuiWindow.indent_action).setStyleSheet('qproperty-icon: url(:/resources/icon/layoutbar/indent3.png)')

            if (TextGuiWindow.dedent_action.isEnabled()):
                TextGuiWindow.layoutbar.widgetForAction(TextGuiWindow.dedent_action).setStyleSheet('qproperty-icon: url(:/resources/icon/layoutbar/dedent1.png)')
            else:
                TextGuiWindow.layoutbar.widgetForAction(TextGuiWindow.dedent_action).setStyleSheet('qproperty-icon: url(:/resources/icon/layoutbar/dedent3.png)')

            if (TextGuiWindow.bullet_action.isEnabled()):
                TextGuiWindow.layoutbar.widgetForAction(TextGuiWindow.bullet_action).setStyleSheet('qproperty-icon: url(:/resources/icon/layoutbar/bullet1.png)')
            else:
                TextGuiWindow.layoutbar.widgetForAction(TextGuiWindow.bullet_action).setStyleSheet('qproperty-icon: url(:/resources/icon/layoutbar/bullet3.png)')

            if (TextGuiWindow.number_action.isEnabled()):
                TextGuiWindow.layoutbar.widgetForAction(TextGuiWindow.number_action).setStyleSheet('qproperty-icon: url(:/resources/icon/layoutbar/number1.png)')
            else:
                TextGuiWindow.layoutbar.widgetForAction(TextGuiWindow.number_action).setStyleSheet('qproperty-icon: url(:/resources/icon/layoutbar/number3.png)')

            if (TextGuiWindow.paragraph_action.isEnabled()):
                TextGuiWindow.layoutbar.widgetForAction(TextGuiWindow.paragraph_action).setStyleSheet('qproperty-icon: url(:/resources/icon/layoutbar/paragraph1.png)')
            else:
                TextGuiWindow.layoutbar.widgetForAction(TextGuiWindow.paragraph_action).setStyleSheet('qproperty-icon: url(:/resources/icon/layoutbar/paragraph3.png)')

            if (TextGuiWindow.find_replace_action.isEnabled()):
                TextGuiWindow.layoutbar.widgetForAction(TextGuiWindow.find_replace_action).setStyleSheet('qproperty-icon: url(:/resources/icon/layoutbar/find1.png)')
            else:
                TextGuiWindow.layoutbar.widgetForAction(TextGuiWindow.find_replace_action).setStyleSheet('qproperty-icon: url(:/resources/icon/layoutbar/find3.png)')

            if (TextGuiWindow.toggle_statusbar_action.isEnabled()):
                TextGuiWindow.layoutbar.widgetForAction(TextGuiWindow.toggle_statusbar_action).setStyleSheet('qproperty-icon: url(:/resources/icon/layoutbar/toggle_sb1.png)')
            else:
                TextGuiWindow.layoutbar.widgetForAction(TextGuiWindow.toggle_statusbar_action).setStyleSheet('qproperty-icon: url(:/resources/icon/layoutbar/toggle_sb3.png)')


            # Update format bar icons for light theme
            if (TextGuiWindow.bold_action.isEnabled()):
                TextGuiWindow.formatbar.widgetForAction(TextGuiWindow.bold_action).setStyleSheet('qproperty-icon: url(:/resources/icon/formatbar/bold1.png)')
            else:
                TextGuiWindow.formatbar.widgetForAction(TextGuiWindow.bold_action).setStyleSheet('qproperty-icon: url(:/resources/icon/formatbar/bold3.png)')

            if (TextGuiWindow.italic_action.isEnabled()):
                TextGuiWindow.formatbar.widgetForAction(TextGuiWindow.italic_action).setStyleSheet('qproperty-icon: url(:/resources/icon/formatbar/italic1.png)')
            else:
                TextGuiWindow.formatbar.widgetForAction(TextGuiWindow.italic_action).setStyleSheet('qproperty-icon: url(:/resources/icon/formatbar/italic3.png)')

            if (TextGuiWindow.under_action.isEnabled()):
                TextGuiWindow.formatbar.widgetForAction(TextGuiWindow.under_action).setStyleSheet('qproperty-icon: url(:/resources/icon/formatbar/underline1.png)')
            else:
                TextGuiWindow.formatbar.widgetForAction(TextGuiWindow.under_action).setStyleSheet('qproperty-icon: url(:/resources/icon/formatbar/underline3.png)')

            if (TextGuiWindow.strike_action.isEnabled()):
                TextGuiWindow.formatbar.widgetForAction(TextGuiWindow.strike_action).setStyleSheet('qproperty-icon: url(:/resources/icon/formatbar/strike1.png)')
            else:
                TextGuiWindow.formatbar.widgetForAction(TextGuiWindow.strike_action).setStyleSheet('qproperty-icon: url(:/resources/icon/formatbar/strike3.png)')

            if (TextGuiWindow.sub_action.isEnabled()):
                TextGuiWindow.formatbar.widgetForAction(TextGuiWindow.sub_action).setStyleSheet('qproperty-icon: url(:/resources/icon/formatbar/subscript1.png)')
            else:
                TextGuiWindow.formatbar.widgetForAction(TextGuiWindow.sub_action).setStyleSheet('qproperty-icon: url(:/resources/icon/formatbar/subscript3.png)')

            if (TextGuiWindow.super_action.isEnabled()):
                TextGuiWindow.formatbar.widgetForAction(TextGuiWindow.super_action).setStyleSheet('qproperty-icon: url(:/resources/icon/formatbar/superscript1.png)')
            else:
                TextGuiWindow.formatbar.widgetForAction(TextGuiWindow.super_action).setStyleSheet('qproperty-icon: url(:/resources/icon/formatbar/superscript3.png)')

            if (TextGuiWindow.font_color_action.isEnabled()):
                TextGuiWindow.formatbar.widgetForAction(TextGuiWindow.font_color_action).setStyleSheet('qproperty-icon: url(:/resources/icon/formatbar/font_color1.png)')
            else:
                TextGuiWindow.formatbar.widgetForAction(TextGuiWindow.font_color_action).setStyleSheet('qproperty-icon: url(:/resources/icon/formatbar/font_color3.png)')

            if (TextGuiWindow.font_color_highlight_action.isEnabled()):
                TextGuiWindow.formatbar.widgetForAction(TextGuiWindow.font_color_highlight_action).setStyleSheet('qproperty-icon: url(:/resources/icon/formatbar/highlight1.png)')
            else:
                TextGuiWindow.formatbar.widgetForAction(TextGuiWindow.font_color_highlight_action).setStyleSheet('qproperty-icon: url(:/resources/icon/formatbar/highlight3.png)')


        elif MainGuiWindow.THEME == "dark":
            # Update toolbar icons for dark theme
            if (TextGuiWindow.save_action.isEnabled()):
                TextGuiWindow.toolbar.widgetForAction(TextGuiWindow.save_action).setStyleSheet('qproperty-icon: url(:/resources/icon/toolbar/save2.png)')
            else:
                TextGuiWindow.toolbar.widgetForAction(TextGuiWindow.save_action).setStyleSheet('qproperty-icon: url(:/resources/icon/toolbar/save1.png)')

            if (TextGuiWindow.undo_action.isEnabled()):
                TextGuiWindow.toolbar.widgetForAction(TextGuiWindow.undo_action).setStyleSheet('qproperty-icon: url(:/resources/icon/toolbar/undo2.png)')
            else:
                TextGuiWindow.toolbar.widgetForAction(TextGuiWindow.undo_action).setStyleSheet('qproperty-icon: url(:/resources/icon/toolbar/undo1.png)')

            if (TextGuiWindow.redo_action.isEnabled()):
                TextGuiWindow.toolbar.widgetForAction(TextGuiWindow.redo_action).setStyleSheet('qproperty-icon: url(:/resources/icon/toolbar/redo2.png)')
            else:
                TextGuiWindow.toolbar.widgetForAction(TextGuiWindow.redo_action).setStyleSheet('qproperty-icon: url(:/resources/icon/toolbar/redo1.png)')

            if (TextGuiWindow.cut_action.isEnabled()):
                TextGuiWindow.toolbar.widgetForAction(TextGuiWindow.cut_action).setStyleSheet('qproperty-icon: url(:/resources/icon/toolbar/cut2.png)')
            else:
                TextGuiWindow.toolbar.widgetForAction(TextGuiWindow.cut_action).setStyleSheet('qproperty-icon: url(:/resources/icon/toolbar/cut1.png)')

            if (TextGuiWindow.copy_action.isEnabled()):
                TextGuiWindow.toolbar.widgetForAction(TextGuiWindow.copy_action).setStyleSheet('qproperty-icon: url(:/resources/icon/toolbar/copy2.png)')
            else:
                TextGuiWindow.toolbar.widgetForAction(TextGuiWindow.copy_action).setStyleSheet('qproperty-icon: url(:/resources/icon/toolbar/copy1.png)')

            if (TextGuiWindow.paste_action.isEnabled()):
                TextGuiWindow.toolbar.widgetForAction(TextGuiWindow.paste_action).setStyleSheet('qproperty-icon: url(:/resources/icon/toolbar/paste2.png)')
            else:
                TextGuiWindow.toolbar.widgetForAction(TextGuiWindow.paste_action).setStyleSheet('qproperty-icon: url(:/resources/icon/toolbar/paste1.png)')

            if (TextGuiWindow.delete_action.isEnabled()):
                TextGuiWindow.toolbar.widgetForAction(TextGuiWindow.delete_action).setStyleSheet('qproperty-icon: url(:/resources/icon/toolbar/delete2.png)')
            else:
                TextGuiWindow.toolbar.widgetForAction(TextGuiWindow.delete_action).setStyleSheet('qproperty-icon: url(:/resources/icon/toolbar/delete1.png)')

            if (TextGuiWindow.selectall_action.isEnabled()):
                TextGuiWindow.toolbar.widgetForAction(TextGuiWindow.selectall_action).setStyleSheet('qproperty-icon: url(:/resources/icon/toolbar/selectall2.png)')
            else:
                TextGuiWindow.toolbar.widgetForAction(TextGuiWindow.selectall_action).setStyleSheet('qproperty-icon: url(:/resources/icon/toolbar/selectall1.png)')

            if (TextGuiWindow.decrease_textsize_action.isEnabled()):
                TextGuiWindow.toolbar.widgetForAction(TextGuiWindow.decrease_textsize_action).setStyleSheet('qproperty-icon: url(:/resources/icon/toolbar/font_decrease2.png)')
            else:
                TextGuiWindow.toolbar.widgetForAction(TextGuiWindow.decrease_textsize_action).setStyleSheet('qproperty-icon: url(:/resources/icon/toolbar/font_decrease1.png)')

            if (TextGuiWindow.increase_textsize_action.isEnabled()):
                TextGuiWindow.toolbar.widgetForAction(TextGuiWindow.increase_textsize_action).setStyleSheet('qproperty-icon: url(:/resources/icon/toolbar/font_increase2.png)')
            else:
                TextGuiWindow.toolbar.widgetForAction(TextGuiWindow.increase_textsize_action).setStyleSheet('qproperty-icon: url(:/resources/icon/toolbar/font_increase1.png)')

            if (TextGuiWindow.set_textfont_action.isEnabled()):
                TextGuiWindow.toolbar.widgetForAction(TextGuiWindow.set_textfont_action).setStyleSheet('qproperty-icon: url(:/resources/icon/toolbar/font_setting2.png)')
            else:
                TextGuiWindow.toolbar.widgetForAction(TextGuiWindow.set_textfont_action).setStyleSheet('qproperty-icon: url(:/resources/icon/toolbar/font_setting1.png)')

            if (TextGuiWindow.set_textcolor_action.isEnabled()):
                TextGuiWindow.toolbar.widgetForAction(TextGuiWindow.set_textcolor_action).setStyleSheet('qproperty-icon: url(:/resources/icon/toolbar/font_color2.png)')
            else:
                TextGuiWindow.toolbar.widgetForAction(TextGuiWindow.set_textcolor_action).setStyleSheet('qproperty-icon: url(:/resources/icon/toolbar/font_color1.png)')

            if (TextGuiWindow.decrease_opacity_action.isEnabled()):
                TextGuiWindow.toolbar.widgetForAction(TextGuiWindow.decrease_opacity_action).setStyleSheet('qproperty-icon: url(:/resources/icon/toolbar/opacity_decrease2.png)')
            else:
                TextGuiWindow.toolbar.widgetForAction(TextGuiWindow.decrease_opacity_action).setStyleSheet('qproperty-icon: url(:/resources/icon/toolbar/opacity_decrease1.png)')

            if (TextGuiWindow.increase_opacity_action.isEnabled()):
                TextGuiWindow.toolbar.widgetForAction(TextGuiWindow.increase_opacity_action).setStyleSheet('qproperty-icon: url(:/resources/icon/toolbar/opacity_increase2.png)')
            else:
                TextGuiWindow.toolbar.widgetForAction(TextGuiWindow.increase_opacity_action).setStyleSheet('qproperty-icon: url(:/resources/icon/toolbar/opacity_increase1.png)')

            if (TextGuiWindow.toggle_formatbar_action.isEnabled()):
                TextGuiWindow.toolbar.widgetForAction(TextGuiWindow.toggle_formatbar_action).setStyleSheet('qproperty-icon: url(:/resources/icon/toolbar/toggle_fb2.png)')
            else:
                TextGuiWindow.toolbar.widgetForAction(TextGuiWindow.toggle_formatbar_action).setStyleSheet('qproperty-icon: url(:/resources/icon/toolbar/toggle_fb1.png)')

            if (TextGuiWindow.reset_action.isEnabled()):
                TextGuiWindow.toolbar.widgetForAction(TextGuiWindow.reset_action).setStyleSheet('qproperty-icon: url(:/resources/icon/toolbar/reset2.png)')
            else:
                TextGuiWindow.toolbar.widgetForAction(TextGuiWindow.reset_action).setStyleSheet('qproperty-icon: url(:/resources/icon/toolbar/reset1.png)')


            if (TextGuiWindow.setting_action.isEnabled()):
                TextGuiWindow.toolbar.widgetForAction(TextGuiWindow.setting_action).setStyleSheet('qproperty-icon: url(:/resources/icon/toolbar/setting2.png)')
            else:
                TextGuiWindow.toolbar.widgetForAction(TextGuiWindow.setting_action).setStyleSheet('qproperty-icon: url(:/resources/icon/toolbar/setting1.png)')


            # Update layout bar icons for dark theme
            if (TextGuiWindow.print_action.isEnabled()):
                TextGuiWindow.layoutbar.widgetForAction(TextGuiWindow.print_action).setStyleSheet('qproperty-icon: url(:/resources/icon/layoutbar/print2.png)')
            else:
                TextGuiWindow.layoutbar.widgetForAction(TextGuiWindow.print_action).setStyleSheet('qproperty-icon: url(:/resources/icon/layoutbar/print1.png)')

            if (TextGuiWindow.preview_action.isEnabled()):
                TextGuiWindow.layoutbar.widgetForAction(TextGuiWindow.preview_action).setStyleSheet('qproperty-icon: url(:/resources/icon/layoutbar/preview2.png)')
            else:
                TextGuiWindow.layoutbar.widgetForAction(TextGuiWindow.preview_action).setStyleSheet('qproperty-icon: url(:/resources/icon/layoutbar/preview1.png)')

            if (TextGuiWindow.lowercase_action.isEnabled()):
                TextGuiWindow.layoutbar.widgetForAction(TextGuiWindow.lowercase_action).setStyleSheet('qproperty-icon: url(:/resources/icon/layoutbar/lower2.png)')
            else:
                TextGuiWindow.layoutbar.widgetForAction(TextGuiWindow.lowercase_action).setStyleSheet('qproperty-icon: url(:/resources/icon/layoutbar/lower1.png)')

            if (TextGuiWindow.capitalizecase_action.isEnabled()):
                TextGuiWindow.layoutbar.widgetForAction(TextGuiWindow.capitalizecase_action).setStyleSheet('qproperty-icon: url(:/resources/icon/layoutbar/capitalize2.png)')
            else:
                TextGuiWindow.layoutbar.widgetForAction(TextGuiWindow.capitalizecase_action).setStyleSheet('qproperty-icon: url(:/resources/icon/layoutbar/capitalize1.png)')

            if (TextGuiWindow.uppercase_action.isEnabled()):
                TextGuiWindow.layoutbar.widgetForAction(TextGuiWindow.uppercase_action).setStyleSheet('qproperty-icon: url(:/resources/icon/layoutbar/upper2.png)')
            else:
                TextGuiWindow.layoutbar.widgetForAction(TextGuiWindow.uppercase_action).setStyleSheet('qproperty-icon: url(:/resources/icon/layoutbar/upper1.png)')

            if (TextGuiWindow.align_left_action.isEnabled()):
                TextGuiWindow.layoutbar.widgetForAction(TextGuiWindow.align_left_action).setStyleSheet('qproperty-icon: url(:/resources/icon/layoutbar/align_left2.png)')
            else:
                TextGuiWindow.layoutbar.widgetForAction(TextGuiWindow.align_left_action).setStyleSheet('qproperty-icon: url(:/resources/icon/layoutbar/align_left1.png)')

            if (TextGuiWindow.align_right_action.isEnabled()):
                TextGuiWindow.layoutbar.widgetForAction(TextGuiWindow.align_right_action).setStyleSheet('qproperty-icon: url(:/resources/icon/layoutbar/align_right2.png)')
            else:
                TextGuiWindow.layoutbar.widgetForAction(TextGuiWindow.align_right_action).setStyleSheet('qproperty-icon: url(:/resources/icon/layoutbar/align_right1.png)')

            if (TextGuiWindow.align_justify_action.isEnabled()):
                TextGuiWindow.layoutbar.widgetForAction(TextGuiWindow.align_justify_action).setStyleSheet('qproperty-icon: url(:/resources/icon/layoutbar/align_justify2.png)')
            else:
                TextGuiWindow.layoutbar.widgetForAction(TextGuiWindow.align_justify_action).setStyleSheet('qproperty-icon: url(:/resources/icon/layoutbar/align_justify1.png)')

            if (TextGuiWindow.align_center_action.isEnabled()):
                TextGuiWindow.layoutbar.widgetForAction(TextGuiWindow.align_center_action).setStyleSheet('qproperty-icon: url(:/resources/icon/layoutbar/align_center2.png)')
            else:
                TextGuiWindow.layoutbar.widgetForAction(TextGuiWindow.align_center_action).setStyleSheet('qproperty-icon: url(:/resources/icon/layoutbar/align_center1.png)')

            if (TextGuiWindow.indent_action.isEnabled()):
                TextGuiWindow.layoutbar.widgetForAction(TextGuiWindow.indent_action).setStyleSheet('qproperty-icon: url(:/resources/icon/layoutbar/indent2.png)')
            else:
                TextGuiWindow.layoutbar.widgetForAction(TextGuiWindow.indent_action).setStyleSheet('qproperty-icon: url(:/resources/icon/layoutbar/indent1.png)')

            if (TextGuiWindow.dedent_action.isEnabled()):
                TextGuiWindow.layoutbar.widgetForAction(TextGuiWindow.dedent_action).setStyleSheet('qproperty-icon: url(:/resources/icon/layoutbar/dedent2.png)')
            else:
                TextGuiWindow.layoutbar.widgetForAction(TextGuiWindow.dedent_action).setStyleSheet('qproperty-icon: url(:/resources/icon/layoutbar/dedent1.png)')

            if (TextGuiWindow.bullet_action.isEnabled()):
                TextGuiWindow.layoutbar.widgetForAction(TextGuiWindow.bullet_action).setStyleSheet('qproperty-icon: url(:/resources/icon/layoutbar/bullet2.png)')
            else:
                TextGuiWindow.layoutbar.widgetForAction(TextGuiWindow.bullet_action).setStyleSheet('qproperty-icon: url(:/resources/icon/layoutbar/bullet1.png)')

            if (TextGuiWindow.number_action.isEnabled()):
                TextGuiWindow.layoutbar.widgetForAction(TextGuiWindow.number_action).setStyleSheet('qproperty-icon: url(:/resources/icon/layoutbar/number2.png)')
            else:
                TextGuiWindow.layoutbar.widgetForAction(TextGuiWindow.number_action).setStyleSheet('qproperty-icon: url(:/resources/icon/layoutbar/number1.png)')

            if (TextGuiWindow.paragraph_action.isEnabled()):
                TextGuiWindow.layoutbar.widgetForAction(TextGuiWindow.paragraph_action).setStyleSheet('qproperty-icon: url(:/resources/icon/layoutbar/paragraph2.png)')
            else:
                TextGuiWindow.layoutbar.widgetForAction(TextGuiWindow.paragraph_action).setStyleSheet('qproperty-icon: url(:/resources/icon/layoutbar/paragraph1.png)')

            if (TextGuiWindow.find_replace_action.isEnabled()):
                TextGuiWindow.layoutbar.widgetForAction(TextGuiWindow.find_replace_action).setStyleSheet('qproperty-icon: url(:/resources/icon/layoutbar/find2.png)')
            else:
                TextGuiWindow.layoutbar.widgetForAction(TextGuiWindow.find_replace_action).setStyleSheet('qproperty-icon: url(:/resources/icon/layoutbar/find1.png)')

            if (TextGuiWindow.toggle_statusbar_action.isEnabled()):
                TextGuiWindow.layoutbar.widgetForAction(TextGuiWindow.toggle_statusbar_action).setStyleSheet('qproperty-icon: url(:/resources/icon/layoutbar/toggle_sb2.png)')
            else:
                TextGuiWindow.layoutbar.widgetForAction(TextGuiWindow.toggle_statusbar_action).setStyleSheet('qproperty-icon: url(:/resources/icon/layoutbar/toggle_sb1.png)')


            # Update format bar icons for dark theme
            if (TextGuiWindow.bold_action.isEnabled()):
                TextGuiWindow.formatbar.widgetForAction(TextGuiWindow.bold_action).setStyleSheet('qproperty-icon: url(:/resources/icon/formatbar/bold2.png)')
            else:
                TextGuiWindow.formatbar.widgetForAction(TextGuiWindow.bold_action).setStyleSheet('qproperty-icon: url(:/resources/icon/formatbar/bold1.png)')

            if (TextGuiWindow.italic_action.isEnabled()):
                TextGuiWindow.formatbar.widgetForAction(TextGuiWindow.italic_action).setStyleSheet('qproperty-icon: url(:/resources/icon/formatbar/italic2.png)')
            else:
                TextGuiWindow.formatbar.widgetForAction(TextGuiWindow.italic_action).setStyleSheet('qproperty-icon: url(:/resources/icon/formatbar/italic1.png)')

            if (TextGuiWindow.under_action.isEnabled()):
                TextGuiWindow.formatbar.widgetForAction(TextGuiWindow.under_action).setStyleSheet('qproperty-icon: url(:/resources/icon/formatbar/underline2.png)')
            else:
                TextGuiWindow.formatbar.widgetForAction(TextGuiWindow.under_action).setStyleSheet('qproperty-icon: url(:/resources/icon/formatbar/underline1.png)')

            if (TextGuiWindow.strike_action.isEnabled()):
                TextGuiWindow.formatbar.widgetForAction(TextGuiWindow.strike_action).setStyleSheet('qproperty-icon: url(:/resources/icon/formatbar/strike2.png)')
            else:
                TextGuiWindow.formatbar.widgetForAction(TextGuiWindow.strike_action).setStyleSheet('qproperty-icon: url(:/resources/icon/formatbar/strike1.png)')

            if (TextGuiWindow.sub_action.isEnabled()):
                TextGuiWindow.formatbar.widgetForAction(TextGuiWindow.sub_action).setStyleSheet('qproperty-icon: url(:/resources/icon/formatbar/subscript2.png)')
            else:
                TextGuiWindow.formatbar.widgetForAction(TextGuiWindow.sub_action).setStyleSheet('qproperty-icon: url(:/resources/icon/formatbar/subscript1.png)')

            if (TextGuiWindow.super_action.isEnabled()):
                TextGuiWindow.formatbar.widgetForAction(TextGuiWindow.super_action).setStyleSheet('qproperty-icon: url(:/resources/icon/formatbar/superscript2.png)')
            else:
                TextGuiWindow.formatbar.widgetForAction(TextGuiWindow.super_action).setStyleSheet('qproperty-icon: url(:/resources/icon/formatbar/superscript1.png)')

            if (TextGuiWindow.font_color_action.isEnabled()):
                TextGuiWindow.formatbar.widgetForAction(TextGuiWindow.font_color_action).setStyleSheet('qproperty-icon: url(:/resources/icon/formatbar/font_color2.png)')
            else:
                TextGuiWindow.formatbar.widgetForAction(TextGuiWindow.font_color_action).setStyleSheet('qproperty-icon: url(:/resources/icon/formatbar/font_color1.png)')

            if (TextGuiWindow.font_color_highlight_action.isEnabled()):
                TextGuiWindow.formatbar.widgetForAction(TextGuiWindow.font_color_highlight_action).setStyleSheet('qproperty-icon: url(:/resources/icon/formatbar/highlight2.png)')
            else:
                TextGuiWindow.formatbar.widgetForAction(TextGuiWindow.font_color_highlight_action).setStyleSheet('qproperty-icon: url(:/resources/icon/formatbar/highlight1.png)')

    # //===================================================//
    def changedfontFamily(self,font):
        """
        Updates the font family of the text box based on the selected font.
        """
        print("=== changedfontFamily ===")
        font_family = self.fontBox.currentFont()
        print(font_family)
        self.textbox.setCurrentFont(font_family)

    # //===================================================//
    def changedfontSize(self):
        """
        Updates the font size of the text box based on user input.
        """
        print("=== changedfontSize ===")
        font_size_new = self.fontSize.currentText()
        print(font_size_new)
        index = self.fontSize.count()
        font_size_list = ['6','7','8','10','12','14','18','24','28','36','48']

        if font_size_new.isdigit():
            font_size_int = int(font_size_new)

            # Validate and apply the new font size
            if ((font_size_int >= 5) and (font_size_int <= 48) ):
                self.textbox.setFontPointSize(font_size_int)

                # Add the new size to the dropdown if not already present
                if (font_size_new in font_size_list):
                    pass
                else:
                    print('=== add input item ===')
                    self.fontSize.removeItem(index-1)
                    self.fontSize.setCurrentText(font_size_new)

        else:
            print('=== invalid input type ===')
            self.fontSize.removeItem(index-1)
            self.fontSize.setCurrentText(font_size)

    #//===================================================//
    def acceptText1(self):
        """
        Handles the "OK" or "Continue" button actions for saving or copying text.
        """
        from src.config.py_config import FOLDERNAME1
        from src.module.py_window_main import MainGuiWindow
        global path_FILENAME2, file2

        print('=== acceptText1 ===')
        path_FILENAME2 = MainGuiWindow.path_documents + '/' + FOLDERNAME1 + '/' + FILENAME2
        file2 = Path(path_FILENAME2)

        if (file2.exists()):
            print('=== Continue button ===')
            self.save_document1()
            self.read_document1()
        else:
            print('=== OK button ===')
            self.textbox.selectAll()
            self.textbox.copy()

        from src.module.py_window_main import MainGuiWindow
        MainGuiWindow.statusComboBox.setCurrentIndex(0)

        self.hide()

    #//===================================================//
    def cancelText1(self):
        """
        Handles the "Cancel" button action and hides the text window.
        """
        from src.config.py_config import FOLDERNAME1
        from src.module.py_window_main import MainGuiWindow
        global path_FILENAME2,file2

        print('=== cancelText1 ===')
        path_FILENAME2 = MainGuiWindow.path_documents + '/' + FOLDERNAME1 + '/' + FILENAME2
        file2 = Path(path_FILENAME2)

        try:
            self.TextWindow.hide()
        except:
            # print("Error: TextWindow is not defined.")
            pass

        if (file2.exists()):
            print('=== Close button ===')

    #//===================================================//
    def saveText1(self):
        """
        Saves the current document.
        """
        from src.func.py_main_editor import TextGuiWindow
        print('=== saveText1 ===')
        self.save_document1()

    #//===================================================//
    def textChangedFcn(self):
        """
        Updates toolbar actions and icons when the text changes.
        """
        print("=== textChangedFcn ===")

        if (MainGuiWindow.FLAG_TOOLBAR):
            try:
                self.save_action.setEnabled(True)
                self.undo_action.setEnabled(True)
                self.redo_action.setEnabled(True)

                # Enable/disable undo and redo actions based on availability
                self.undo_action.setEnabled(self.textbox.document().isUndoAvailable())
                self.redo_action.setEnabled(self.textbox.document().isRedoAvailable())

                self.updateEnabled_icon()
            except:
                pass

    # //===================================================//
    def textSelectionChanged(self):
        """
        Updates toolbar actions and font settings when text selection changes.
        """
        print("=== textSelectionChanged (begin) ===")

        global font_size
        self.cursor = self.textbox.textCursor()
        start = self.cursor.selectionStart()
        end = self.cursor.selectionEnd()
        num = int(abs(end-start))

        # Update font family and size in the dropdowns
        font_family = str(self.textbox.fontFamily())
        # print('font_family := ', font_family)
        self.fontBox.setCurrentText(font_family)

        font_size = str(int(self.textbox.fontPointSize()))
        # print('font_size := ', font_size)
        self.fontSize.setCurrentText(font_size)

        from src.module.py_window_main import MainGuiWindow

        if self.cursor.hasSelection():
            # Enable actions for selected text
            print("=== textSelectionChanged 1 ===")
            self.undo_action.setEnabled(True)
            self.redo_action.setEnabled(True)
            self.copy_action.setEnabled(True)
            self.paste_action.setEnabled(True)
            self.cut_action.setEnabled(True)
            self.delete_action.setEnabled(True)

            # Enable text formatting actions
            self.lowercase_action.setEnabled(True)
            self.capitalizecase_action.setEnabled(True)
            self.uppercase_action.setEnabled(True)
            self.bold_action.setEnabled(True)
            self.italic_action.setEnabled(True)
            self.under_action.setEnabled(True)
            self.strike_action.setEnabled(True)
            self.sub_action.setEnabled(True)
            self.super_action.setEnabled(True)
            self.font_color_action.setEnabled(True)
            self.font_color_highlight_action.setEnabled(True)
        else:
            # Disable actions when no text is selected
            print("=== textSelectionChanged 2 ===")
            self.copy_action.setEnabled(False)
            self.cut_action.setEnabled(False)
            self.delete_action.setEnabled(False)
            self.lowercase_action.setEnabled(False)
            self.capitalizecase_action.setEnabled(False)
            self.uppercase_action.setEnabled(False)
            self.bold_action.setEnabled(False)
            self.italic_action.setEnabled(False)
            self.under_action.setEnabled(False)
            self.strike_action.setEnabled(False)
            self.sub_action.setEnabled(False)
            self.super_action.setEnabled(False)
            self.font_color_action.setEnabled(False)
            self.font_color_highlight_action.setEnabled(False)

        try:
            # Enable/disable undo action based on availability
            print("=== textSelectionChanged 3 ===")
            self.undo_action.setEnabled(self.textbox.document().isUndoAvailable())
        except:
            pass

        try:
            # Enable/disable redo action based on availability
            print("=== textSelectionChanged 4 ===")
            self.redo_action.setEnabled(self.textbox.document().isRedoAvailable())
        except:
            pass

        try:
            # Enable "Select All" action and update icons
            print("=== textSelectionChanged 5 ===")
            self.selectall_action.setEnabled(True)
            self.updateEnabled_icon()
        except:
            pass

        print("=== textSelectionChanged (end) ===")

    #//===================================================//
    def undoText(self):
        """
        Undo the last action in the text editor and update the toolbar icons.
        """
        print('=== undoText ===')
        self.textbox.undo()
        self.selectall_action.setEnabled(True)

        # Enable/disable undo action based on availability
        if self.textbox.document().isUndoAvailable():
            self.undo_action.setEnabled(True)
        else:
            self.undo_action.setEnabled(False)
        self.updateEnabled_icon()


    def redoText(self):
        """
        Redo the last undone action in the text editor and update the toolbar icons.
        """
        print('=== redoText ===')
        self.textbox.redo()
        self.selectall_action.setEnabled(True)

        # Enable/disable redo action based on availability
        if self.textbox.document().isRedoAvailable():
            self.redo_action.setEnabled(True)
        else:
            self.redo_action.setEnabled(False)
        self.updateEnabled_icon()


    def cutText(self):
        """
        Cut the selected text and update the toolbar icons.
        """
        print('=== cutText ===')
        self.textbox.cut()
        self.cut_action.setEnabled(False)
        self.selectall_action.setEnabled(True)

        # Enable/disable redo action based on availability
        if self.textbox.document().isRedoAvailable():
            self.redo_action.setEnabled(True)
        else:
            self.redo_action.setEnabled(False)
        self.updateEnabled_icon()


    def copyText(self):
        """
        Copy the selected text and update the toolbar icons.
        """
        print('=== copyText ===')
        self.textbox.copy()
        self.copy_action.setEnabled(False)
        self.paste_action.setEnabled(True)
        self.selectall_action.setEnabled(True)

        # Enable/disable redo action based on availability
        if self.textbox.document().isRedoAvailable():
            self.redo_action.setEnabled(True)
        else:
            self.redo_action.setEnabled(False)
        self.updateEnabled_icon()


    def pasteText(self):
        """
        Paste the copied text and update the toolbar icons.
        """
        print('=== pasteText ===')
        self.textbox.paste()
        self.copy_action.setEnabled(False)
        self.cut_action.setEnabled(False)
        self.delete_action.setEnabled(False)
        self.selectall_action.setEnabled(True)

        # Enable/disable redo action based on availability
        if self.textbox.document().isRedoAvailable():
            self.redo_action.setEnabled(True)
        else:
            self.redo_action.setEnabled(False)
        self.updateEnabled_icon()


    def deleteText(self):
        """
        Delete the selected text and update the toolbar icons.
        """
        print('=== deleteText ===')
        self.textbox.cut()
        self.delete_action.setEnabled(False)
        self.selectall_action.setEnabled(True)

        # Enable/disable redo action based on availability
        if self.textbox.document().isRedoAvailable():
            self.redo_action.setEnabled(True)
        else:
            self.redo_action.setEnabled(False)
        self.updateEnabled_icon()


    def selectAllText(self):
        """
        Select all text in the editor and update the toolbar icons.
        """
        global FLAG_SELECTALL

        print('=== selectAllText ===')
        self.textbox.setFocus()
        self.textbox.selectAll()
        self.selectall_action.setEnabled(False)
        self.cut_action.setEnabled(True)
        self.copy_action.setEnabled(True)
        self.delete_action.setEnabled(True)
        self.updateEnabled_icon()


    def findreplaceText(self):
        """
        Open the Find and Replace window and disable certain actions while it is active.
        """
        from src.module.py_window_findreplace import FindReplace

        print('=== findreplaceText ===')

        if self.window4 is None:
            self.window4 = FindReplace()
        self.window4.show()
        self.window4.findFcn()

        # Disable actions while the Find and Replace window is open
        self.setting_action.setEnabled(False)
        self.set_textfont_action.setEnabled(False)
        self.set_textcolor_action.setEnabled(False)
        self.reset_action.setEnabled(False)
        self.preview_action.setEnabled(False)
        self.print_action.setEnabled(False)
        self.find_replace_action.setEnabled(False)
        self.font_color_action.setEnabled(False)
        self.font_color_highlight_action.setEnabled(False)
        self.updateEnabled_icon()

    #//===================================================//
    def confirm_save(self):
        """
        Display a confirmation dialog to save changes before closing.
        """
        print('=== confirm_save ===')
        self.msgBox = QMessageBox()
        self.msgBox.setWindowTitle("QMessageBox Example")
        self.msgBox.setText("Do you want to save changes to {self.path if self.path else 'Untitled'}")

        # Add OK and Cancel buttons to the dialog
        self.msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        self.msgBox.buttonClicked.connect(self.close)
        self.msgBox.exec()

    #//===================================================//
    def save_document(self):
        """
        Saves the current document in the selected format and location.
        """

        from src.module.py_window_main import MainGuiWindow
        global path_FILENAME1, FILENAME1
        global FLAG_SAVEPATH_INIT
        global filter1, FILENUM

        print('=== save_document ===')
        filter1 = None
        # Define file format filters based on the selected output format
        if (MainGuiWindow.OutputFormatVar1 == 0):
            filters = 'Text File (*.txt);;Word Document (*.docx);;Word 97-2003 Document (*.doc);;OpenDocument Text (*.odt);;Rich Text Format (*.rtf)'
        elif (MainGuiWindow.OutputFormatVar1 == 1):
            filters = 'Portable Document Format (*.pdf)'
        elif (MainGuiWindow.OutputFormatVar1 == 2):
            filters = 'Excel Workbook (*.xlsx);;Excel 97-2003 Workbook (*.xls);;Comma-separated Values (*.csv);;OpenDocument Spreadsheet (*.ods)'

        self.save_action.setEnabled(False)
        self.updateEnabled_icon()
        path_desktop = str(Path.home()/'Desktop')
        path_desktop = path_desktop.replace('\\','/')

        # Initialize save path if not already set
        if (FLAG_SAVEPATH_INIT):
            FLAG_SAVEPATH_INIT = False
            path_FILENAME1 = path_desktop + '/' + FILENAME1

        print('path_FILENAME1 := ', path_FILENAME1)

        file1 = Path(path_FILENAME1)
        if (file1.exists()):
            print('=== rewrite existing file ===')
            self.path = Path(path_FILENAME1)

            # Handle saving for text-based formats
            if (MainGuiWindow.OutputFormatVar1 == 0):
                import win32com.client as win32
                from win32com.client import constants

                if (filter1 == 'Text File (*.txt)'):
                    # Append new content to the existing text file
                    self.path.write_text(self.path.read_text(encoding="utf-8") + '\n\n'\
                    '----------------------- END -----------------------' \
                    '\n\n' \
                    + self.textbox.toPlainText() \
                    ,encoding="utf-8")

                elif (filter1 == 'Rich Text Format (*.rtf)'):
                    # Append new content to the existing RTF file
                    with open(self.path, "r", encoding="utf-8") as f:
                        temp_data1 = f.read()
                        print(temp_data1)

                    temp_data2 = self.textbox.toHtml()
                    self.textbox.insertHtml(temp_data1)
                    self.textbox.insertHtml('<br></br><p> ------------ END ------------ </p><br></br>')

                    with open(self.path, "w", encoding="utf-8") as f:
                        f.write(self.textbox.toHtml())

                    self.textbox.setHtml(temp_data2)

                elif (filter1 == 'OpenDocument Text (*.odt)'):
                    # Save as ODT format using Word automation
                    file2 = os.path.splitext(os.path.abspath(self.path))[0]
                    while (os.path.exists(os.path.abspath(file2+str(FILENUM)+".odt"))):
                        FILENUM += 1

                    self.path = file2 + str(FILENUM) + '.doc'
                    Path(self.path).write_text(self.textbox.toHtml(),encoding="utf-8")

                    word = win32.gencache.EnsureDispatch('Word.Application')
                    doc = word.Documents.Open(self.path)
                    doc.Activate()
                    file2 = os.path.splitext(os.path.abspath(self.path))[0] + ".odt"
                    word.ActiveDocument.SaveAs(file2, FileFormat=constants.wdFormatOpenDocumentText)
                    doc.Close(True)

                    if (Path(self.path).exists()):
                        Path.unlink(Path(self.path))

                elif (filter1 == 'Word 97-2003 Document (*.doc)'):
                    file2 = os.path.splitext(os.path.abspath(self.path))[0]
                    while (os.path.exists(os.path.abspath(file2+str(FILENUM)+".doc"))):
                        FILENUM += 1

                    self.path = file2 + str(FILENUM) + '.doc'
                    Path(self.path).write_text(self.textbox.toHtml(),encoding="utf-8")

                    word = win32.gencache.EnsureDispatch('Word.Application')
                    doc = word.Documents.Open(self.path)
                    doc.Activate()
                    file2 = os.path.splitext(os.path.abspath(self.path))[0] + ".doc"
                    word.ActiveDocument.SaveAs(file2, FileFormat=win32.constants.wdFormatOpenDocumentText)
                    doc.Close(True)

                elif (filter1 == 'Word Document (*.docx)'):
                    # Save as DOCX format using Word automation
                    file2 = os.path.splitext(os.path.abspath(self.path))[0]
                    while (os.path.exists(os.path.abspath(file2+str(FILENUM)+".docx"))):
                        FILENUM += 1

                    self.path = file2 + str(FILENUM) + '.doc'
                    Path(self.path).write_text(self.textbox.toHtml(),encoding="utf-8")

                    word = win32.gencache.EnsureDispatch('Word.Application')
                    doc = word.Documents.Open(self.path)
                    doc.Activate()
                    file2 = os.path.splitext(os.path.abspath(self.path))[0] + ".docx"
                    word.ActiveDocument.SaveAs(file2, FileFormat=win32.constants.wdFormatXMLDocument)
                    doc.Close(True)

                    if (Path(self.path).exists()):
                        Path.unlink(Path(self.path))

            elif (MainGuiWindow.OutputFormatVar1 == 1):
                # Save as PDF format
                file2 = os.path.splitext(os.path.abspath(self.path))[0]
                while (os.path.exists(os.path.abspath(file2+str(FILENUM)+".pdf"))):
                    FILENUM += 1
                self.path = file2 + str(FILENUM) + '.pdf'
                Path(self.path).write_text(self.textbox.toHtml(),encoding="utf-8")
                document = QTextDocument()
                document.setHtml(self.textbox.toHtml())
                printer = QtPrintSupport.QPrinter()
                printer.setPageSize(QtPrintSupport.QPrinter.A4)
                printer.setColorMode(QtPrintSupport.QPrinter.Color)
                printer.setOutputFormat(QtPrintSupport.QPrinter.PdfFormat)
                printer.setOutputFileName(self.path)
                document.print_(printer)

            elif (MainGuiWindow.OutputFormatVar1 == 2):
                # Save as spreadsheet formats
                import pandas as pd
                import win32com.client as win32
                # from win32com.client import constants

                if (filter1 == 'Excel Workbook (*.xlsx)'):
                    file2 = os.path.splitext(os.path.abspath(self.path))[0]
                    while (os.path.exists(os.path.abspath(file2+str(FILENUM)+".xlsx"))):
                        FILENUM += 1
                    self.path = file2 + str(FILENUM) + '.xlsx'
                    rows = self.textbox.toPlainText().split("\n")
                    table_data = [row.split("\t") for row in rows]
                    df = pd.DataFrame(table_data)
                    # df = df.applymap(lambda x: x if isinstance(x, str) and x.strip() != "" else pd.NA)
                    df = df.applymap(lambda x: x if x.strip() != "" else pd.NA)
                    output_excel_file = self.path
                    df.to_excel(output_excel_file, index=False, header=False)

                elif (filter1 == 'Excel 97-2003 Workbook (*.xls)'):
                    # Save as spreadsheet formats
                    file2 = os.path.splitext(os.path.abspath(self.path))[0]
                    while (os.path.exists(os.path.abspath(file2+str(FILENUM)+".xls"))):
                        FILENUM += 1
                    self.path = file2 + str(FILENUM) + '.xlsx'
                    rows = self.textbox.toPlainText().split("\n")
                    table_data = [row.split("\t") for row in rows]
                    df = pd.DataFrame(table_data)
                    df = df.applymap(lambda x: x if x.strip() != "" else pd.NA)
                    output_excel_file = self.path
                    df.to_excel(output_excel_file, index=False, header=False)

                    excel = win32.gencache.EnsureDispatch('Excel.Application')
                    doc = excel.Workbooks.Open(self.path)
                    doc.Activate()
                    file2 = os.path.splitext(os.path.abspath(self.path))[0] + ".xls"
                    excel.ActiveWorkbook.SaveAs(file2,FileFormat=56)
                    excel.Application.Quit()

                    if (Path(self.path).exists()):
                        Path.unlink(Path(self.path))

                elif (filter1 == 'Comma-separated Values (*.csv)'):
                    # Save as spreadsheet formats
                    file2 = os.path.splitext(os.path.abspath(self.path))[0]
                    while (os.path.exists(os.path.abspath(file2+str(FILENUM)+".csv"))):
                        FILENUM += 1
                    self.path = file2 + str(FILENUM) + '.csv'

                    rows = self.textbox.toPlainText().split("\n")
                    table_data = [row.split("\t") for row in rows]
                    df = pd.DataFrame(table_data)
                    df = df.applymap(lambda x: x if x.strip() != "" else pd.NA)
                    output_excel_file = self.path
                    df.to_csv(output_excel_file, index=False, header=False)

                elif (filter1 == 'OpenDocument Spreadsheet (*.ods)'):
                    # Save as spreadsheet formats
                    file2 = os.path.splitext(os.path.abspath(self.path))[0]
                    while (os.path.exists(os.path.abspath(file2+str(FILENUM)+".ods"))):
                        FILENUM += 1
                    self.path = file2 + str(FILENUM) + '.xlsx'

                    rows = self.textbox.toPlainText().split("\n")
                    table_data = [row.split("\t") for row in rows]
                    df = pd.DataFrame(table_data)
                    df = df.applymap(lambda x: x if x.strip() != "" else pd.NA)
                    output_excel_file = self.path
                    df.to_excel(output_excel_file, index=False, header=False)

                    excel = win32.gencache.EnsureDispatch('Excel.Application')
                    doc = excel.Workbooks.Open(self.path)
                    doc.Activate()
                    file2 = os.path.splitext(os.path.abspath(self.path))[0] + ".ods"
                    excel.ActiveWorkbook.SaveAs(file2, FileFormat=60)
                    excel.Application.Quit()

                    if (Path(self.path).exists()):
                        Path.unlink(Path(self.path))

            self.save_action.setEnabled(False)
            self.updateEnabled_icon()

        else:
            # Handle creating a new file
            print('=== create new file ===')
            self.filename, self.filter1 = QFileDialog.getSaveFileName(self,'Save File',path_desktop+'/'+FILENAME1,filter=filters)

            if not self.filename:
                print('=== cancel selection ===')
                self.save_action.setEnabled(True)
                self.updateEnabled_icon()
                return

            FILENAME1 = Path(self.filename).name
            self.path = Path(self.filename)
            print('filename := ', self.filename)
            print('filter1 := ', self.filter1)
            print('FILENAME1 := ', FILENAME1)
            print('path := ', self.path)
            path_FILENAME1 = self.path
            print('path_FILENAME1 := ', path_FILENAME1)
            filter1 = self.filter1

            # Save content based on the selected format
            if (MainGuiWindow.OutputFormatVar1 == 0):
                import win32com.client as win32
                from win32com.client import constants

                if (self.filter1 == 'Text File (*.txt)'):
                     # Save plain text content
                    self.path.write_text(self.textbox.toPlainText(),encoding="utf-8")

                elif (self.filter1 == 'Rich Text Format (*.rtf)'):
                    # Save content as RTF
                    self.path.write_text(self.textbox.toHtml(),encoding="utf-8")

                elif (self.filter1 == 'OpenDocument Text (*.odt)'):
                    # Convert and save as ODT using Word automation
                    self.path = str(self.path).replace('.odt','.doc')
                    Path(self.path).write_text(self.textbox.toHtml(),encoding="utf-8")

                    word = win32.gencache.EnsureDispatch('Word.Application')
                    doc = word.Documents.Open(self.path)
                    doc.Activate()
                    file2 = os.path.splitext(os.path.abspath(self.path))[0] + ".odt"
                    word.ActiveDocument.SaveAs(file2, FileFormat=constants.wdFormatOpenDocumentText)
                    doc.Close(True)

                    # Remove intermediate .doc file
                    if (Path(self.path).exists()):
                        Path.unlink(Path(self.path))

                elif (self.filter1 == 'Word 97-2003 Document (*.doc)'):
                    # Save as Word 97-2003 format
                    file2 = os.path.splitext(os.path.abspath(self.path))[0]
                    self.path = file2 + str(FILENUM) + '.doc'
                    Path(self.path).write_text(self.textbox.toHtml(),encoding="utf-8")

                    word = win32.gencache.EnsureDispatch('Word.Application')
                    doc = word.Documents.Open(self.path)
                    doc.Activate()
                    file2 = os.path.splitext(os.path.abspath(self.path))[0] + ".doc"
                    word.ActiveDocument.SaveAs(file2, FileFormat=constants.wdFormatOpenDocumentText)
                    doc.Close(True)

                elif (self.filter1 == 'Word Document (*.docx)'):
                    # Convert and save as DOCX using Word automation
                    self.path = str(self.path).replace('.docx','.doc')
                    Path(self.path).write_text(self.textbox.toHtml(),encoding="utf-8")

                    word = win32.gencache.EnsureDispatch('Word.Application')
                    doc = word.Documents.Open(self.path)
                    doc.Activate()
                    file2 = os.path.splitext(os.path.abspath(self.path))[0] + ".docx"
                    word.ActiveDocument.SaveAs(file2, FileFormat=constants.wdFormatXMLDocument)
                    doc.Close(True)

                    # Remove intermediate .doc file
                    if (Path(self.path).exists()):
                        Path.unlink(Path(self.path))

            elif (MainGuiWindow.OutputFormatVar1 == 1):
                # Save content as PDF
                document = QTextDocument()
                document.setHtml(self.textbox.toHtml())
                printer = QtPrintSupport.QPrinter()
                printer.setPageSize(QtPrintSupport.QPrinter.A4)
                printer.setColorMode(QtPrintSupport.QPrinter.Color)
                printer.setOutputFormat(QtPrintSupport.QPrinter.PdfFormat)
                printer.setOutputFileName(self.filename)
                document.print_(printer)

            elif (MainGuiWindow.OutputFormatVar1 == 2):
                import pandas as pd
                import win32com.client as win32
                # from win32com.client import constants

                if (self.filter1 == 'Excel Workbook (*.xlsx)'):
                    # Save as Excel Workbook
                    rows = self.textbox.toPlainText().split("\n")
                    table_data = [row.split("\t") for row in rows]
                    df = pd.DataFrame(table_data)
                    df = df.map(lambda x: x if x.strip() != "" else pd.NA)
                    output_excel_file = self.filename
                    df.to_excel(output_excel_file, index=False, header=False)
                elif (self.filter1 == 'Excel 97-2003 Workbook (*.xls)'):
                    # Convert and save as Excel 97-2003 format
                    self.filename = str(self.filename).replace('.xls','.xlsx')
                    rows = self.textbox.toPlainText().split("\n")
                    table_data = [row.split("\t") for row in rows]
                    df = pd.DataFrame(table_data)
                    df = df.applymap(lambda x: x if x.strip() != "" else pd.NA)
                    output_excel_file = self.filename
                    df.to_excel(output_excel_file, index=False, header=False)

                    excel = win32.gencache.EnsureDispatch('Excel.Application')
                    self.filename = str(self.filename).replace('/','\\')
                    print('filename := ', self.filename)
                    doc = excel.Workbooks.Open(self.filename)
                    doc.Activate()
                    file2 = os.path.splitext(os.path.abspath(self.filename))[0] + ".xls"
                    print('file2 := ', file2)
                    excel.ActiveWorkbook.SaveAs(file2,FileFormat=56)
                    excel.Application.Quit()
                    if (Path(self.filename).exists()):
                        Path.unlink(Path(self.filename))

                elif (self.filter1 == 'Comma-separated Values (*.csv)'):
                    # Convert and save as CSV format
                    rows = self.textbox.toPlainText().split("\n")
                    table_data = [row.split("\t") for row in rows]
                    df = pd.DataFrame(table_data)
                    df = df.applymap(lambda x: x if x.strip() != "" else pd.NA)
                    output_excel_file = self.filename
                    df.to_csv(output_excel_file, index=False, header=False)

                elif (self.filter1 == 'OpenDocument Spreadsheet (*.ods)'):
                    # Convert and save as ODS format
                    self.filename = str(self.filename).replace('.ods','.xlsx')
                    rows = self.textbox.toPlainText().split("\n")
                    table_data = [row.split("\t") for row in rows]
                    df = pd.DataFrame(table_data)
                    df = df.applymap(lambda x: x if x.strip() != "" else pd.NA)
                    output_excel_file = self.filename
                    df.to_excel(output_excel_file, index=False, header=False)

                    excel = win32.gencache.EnsureDispatch('Excel.Application')
                    self.filename = str(self.filename).replace('/','\\')
                    print('filename := ', self.filename)
                    doc = excel.Workbooks.Open(self.filename)
                    doc.Activate()
                    file2 = os.path.splitext(os.path.abspath(self.filename))[0] + ".ods"
                    print('file2 := ', file2)
                    excel.ActiveWorkbook.SaveAs(file2, FileFormat=60)
                    excel.Application.Quit()

                    # Remove intermediate .xlsx file
                    if (Path(self.filename).exists()):
                        Path.unlink(Path(self.filename))
        print('=== save_document ===')

    #//===================================================//
    def save_document1(self):
        """
        Saves the current document to the specified location.
        If the file already exists, appends the new content to the existing file.
        Otherwise, creates a new file and writes the content to it.
        """

        from src.module.py_window_main import MainGuiWindow
        from src.config.py_config import FOLDERNAME1
        global FILENAME2, file2, path

        print('=== save_document1 ===')

        # Construct the file path
        path_FILENAME2 = MainGuiWindow.path_documents + '/' + FOLDERNAME1 + '/' + FILENAME2
        file2 = Path(path_FILENAME2)
        if (file2.exists()):
            # Append new content to the existing file
            print('=== rewrite existing file ===')
            path = Path(path_FILENAME2)
            path.write_text(path.read_text(encoding="utf-8") + '\n\n'\
            + TextGuiWindow.textbox.toPlainText() + '\n\n'\
            '----------------------- END -----------------------',encoding="utf-8")
        else:
            # Create a new file and write content
            print('=== create new file ===')
            path = Path(path_FILENAME2)
            path.write_text(TextGuiWindow.textbox.toPlainText() + '\n\n'\
            '----------------------- END -----------------------',encoding="utf-8")

    #//===================================================//
    def read_document1(self):
        """
        Reads the content of the specified document.
        After reading, the file is deleted to ensure temporary files are not left behind.
        """

        global FILENAME2
        print('=== read_document1 ===')

        # Read content from the file
        textn1 = open(file2,encoding="utf-8").read()
        print('textn1 := ', textn1)

        # Load content into a QTextEdit
        self.textbox1 = QTextEdit(self)
        self.textbox1.setVisible(False)
        self.textbox1.setPlainText(textn1)
        self.textbox1.selectAll()
        self.textbox1.copy()

        # Delete the file after reading
        if (file2.exists()):
            Path.unlink(file2)

    #//===================================================//
    def closeWindow(self):
        """
        Closes the current window and performs cleanup operations.
        Ensures that any open auxiliary windows (e.g., ColorPicker, FindReplace) are closed.
        Also determines the docking position of toolbars and updates the main window's docking configuration.
        """

        print('=== closeWindow ===')
        # Determine the docking configuration based on toolbar positions
        if  ((self.windowMain.toolBarArea(self.toolbar) == 4) and (self.windowMain.toolBarArea(self.layoutbar) == 4) and (self.windowMain.toolBarArea(self.formatbar) == 4) and \
            (self.toolbar.geometry().top() < self.layoutbar.geometry().top() < self.formatbar.geometry().top())):
            MainGuiWindow.DOCKING = 0
        elif  ((self.windowMain.toolBarArea(self.toolbar) == 4) and (self.windowMain.toolBarArea(self.layoutbar) == 4) and (self.windowMain.toolBarArea(self.formatbar) == 4) and \
            (self.toolbar.geometry().top() < self.formatbar.geometry().top() < self.layoutbar.geometry().top())):
            MainGuiWindow.DOCKING = 1
        elif  ((self.windowMain.toolBarArea(self.toolbar) == 4) and (self.windowMain.toolBarArea(self.layoutbar) == 4) and (self.windowMain.toolBarArea(self.formatbar) == 4) and \
            (self.layoutbar.geometry().top() < self.toolbar.geometry().top() < self.formatbar.geometry().top())):
            MainGuiWindow.DOCKING = 2
        elif  ((self.windowMain.toolBarArea(self.toolbar) == 4) and (self.windowMain.toolBarArea(self.layoutbar) == 4) and (self.windowMain.toolBarArea(self.formatbar) == 4) and \
            (self.layoutbar.geometry().top() < self.formatbar.geometry().top() < self.toolbar.geometry().top())):
            MainGuiWindow.DOCKING = 3
        elif  ((self.windowMain.toolBarArea(self.toolbar) == 4) and (self.windowMain.toolBarArea(self.layoutbar) == 4) and (self.windowMain.toolBarArea(self.formatbar) == 4) and \
            (self.formatbar.geometry().top() < self.toolbar.geometry().top() < self.layoutbar.geometry().top())):
            MainGuiWindow.DOCKING = 4
        elif  ((self.windowMain.toolBarArea(self.toolbar) == 4) and (self.windowMain.toolBarArea(self.layoutbar) == 4) and (self.windowMain.toolBarArea(self.formatbar) == 4) and \
            (self.formatbar.geometry().top() < self.layoutbar.geometry().top() < self.toolbar.geometry().top())):
            MainGuiWindow.DOCKING = 5

        elif  ((self.windowMain.toolBarArea(self.toolbar) == 8) and (self.windowMain.toolBarArea(self.layoutbar) == 8) and (self.windowMain.toolBarArea(self.formatbar) == 8) and \
            (self.toolbar.geometry().top() < self.layoutbar.geometry().top() < self.formatbar.geometry().top())):
            MainGuiWindow.DOCKING = 6
        elif  ((self.windowMain.toolBarArea(self.toolbar) == 8) and (self.windowMain.toolBarArea(self.layoutbar) == 8) and (self.windowMain.toolBarArea(self.formatbar) == 8) and \
            (self.toolbar.geometry().top() < self.formatbar.geometry().top() < self.layoutbar.geometry().top())):
            MainGuiWindow.DOCKING = 7
        elif  ((self.windowMain.toolBarArea(self.toolbar) == 8) and (self.windowMain.toolBarArea(self.layoutbar) == 8) and (self.windowMain.toolBarArea(self.formatbar) == 8) and \
            (self.layoutbar.geometry().top() < self.toolbar.geometry().top() < self.formatbar.geometry().top())):
            MainGuiWindow.DOCKING = 8
        elif  ((self.windowMain.toolBarArea(self.toolbar) == 8) and (self.windowMain.toolBarArea(self.layoutbar) == 8) and (self.windowMain.toolBarArea(self.formatbar) == 8) and \
            (self.layoutbar.geometry().top() < self.formatbar.geometry().top() < self.toolbar.geometry().top())):
            MainGuiWindow.DOCKING = 9
        elif  ((self.windowMain.toolBarArea(self.toolbar) == 8) and (self.windowMain.toolBarArea(self.layoutbar) == 8) and (self.windowMain.toolBarArea(self.formatbar) == 8) and \
            (self.formatbar.geometry().top() < self.toolbar.geometry().top() < self.layoutbar.geometry().top())):
            MainGuiWindow.DOCKING = 10
        elif  ((self.windowMain.toolBarArea(self.toolbar) == 8) and (self.windowMain.toolBarArea(self.layoutbar) == 8) and (self.windowMain.toolBarArea(self.formatbar) == 8) and \
            (self.formatbar.geometry().top() < self.layoutbar.geometry().top() < self.toolbar.geometry().top())):
            MainGuiWindow.DOCKING = 11

        elif  ((self.windowMain.toolBarArea(self.toolbar) == 4) and (self.windowMain.toolBarArea(self.layoutbar) == 4) and (self.windowMain.toolBarArea(self.formatbar) == 8) and \
            (self.toolbar.geometry().top() < self.layoutbar.geometry().top() < self.formatbar.geometry().top())):
            MainGuiWindow.DOCKING = 12
        elif  ((self.windowMain.toolBarArea(self.toolbar) == 4) and (self.windowMain.toolBarArea(self.layoutbar) == 8) and (self.windowMain.toolBarArea(self.formatbar) == 4) and \
            (self.toolbar.geometry().top() < self.formatbar.geometry().top() < self.layoutbar.geometry().top())):
            MainGuiWindow.DOCKING = 13
        elif  ((self.windowMain.toolBarArea(self.toolbar) == 4) and (self.windowMain.toolBarArea(self.layoutbar) == 4) and (self.windowMain.toolBarArea(self.formatbar) == 8) and \
            (self.layoutbar.geometry().top() < self.toolbar.geometry().top() < self.formatbar.geometry().top())):
            MainGuiWindow.DOCKING = 14
        elif  ((self.windowMain.toolBarArea(self.toolbar) == 8) and (self.windowMain.toolBarArea(self.layoutbar) == 4) and (self.windowMain.toolBarArea(self.formatbar) == 4) and \
            (self.layoutbar.geometry().top() < self.formatbar.geometry().top() < self.toolbar.geometry().top())):
            MainGuiWindow.DOCKING = 15
        elif  ((self.windowMain.toolBarArea(self.toolbar) == 4) and (self.windowMain.toolBarArea(self.layoutbar) == 8) and (self.windowMain.toolBarArea(self.formatbar) == 4) and \
            (self.formatbar.geometry().top() < self.toolbar.geometry().top() < self.layoutbar.geometry().top())):
            MainGuiWindow.DOCKING = 16
        elif  ((self.windowMain.toolBarArea(self.toolbar) == 8) and (self.windowMain.toolBarArea(self.layoutbar) == 4) and (self.windowMain.toolBarArea(self.formatbar) == 4) and \
            (self.formatbar.geometry().top() < self.layoutbar.geometry().top() < self.toolbar.geometry().top())):
            MainGuiWindow.DOCKING = 17

        elif  ((self.windowMain.toolBarArea(self.toolbar) == 4) and (self.windowMain.toolBarArea(self.layoutbar) == 8) and (self.windowMain.toolBarArea(self.formatbar) == 8) and \
            (self.toolbar.geometry().top() < self.layoutbar.geometry().top() < self.formatbar.geometry().top())):
            MainGuiWindow.DOCKING = 18
        elif  ((self.windowMain.toolBarArea(self.toolbar) == 4) and (self.windowMain.toolBarArea(self.layoutbar) == 8) and (self.windowMain.toolBarArea(self.formatbar) == 8) and \
            (self.toolbar.geometry().top() < self.formatbar.geometry().top() < self.layoutbar.geometry().top())):
            MainGuiWindow.DOCKING = 19
        elif  ((self.windowMain.toolBarArea(self.toolbar) == 8) and (self.windowMain.toolBarArea(self.layoutbar) == 4) and (self.windowMain.toolBarArea(self.formatbar) == 8) and \
            (self.layoutbar.geometry().top() < self.toolbar.geometry().top() < self.formatbar.geometry().top())):
            MainGuiWindow.DOCKING = 20
        elif  ((self.windowMain.toolBarArea(self.toolbar) == 8) and (self.windowMain.toolBarArea(self.layoutbar) == 4) and (self.windowMain.toolBarArea(self.formatbar) == 8) and \
            (self.layoutbar.geometry().top() < self.formatbar.geometry().top() < self.toolbar.geometry().top())):
            MainGuiWindow.DOCKING = 21
        elif  ((self.windowMain.toolBarArea(self.toolbar) == 8) and (self.windowMain.toolBarArea(self.layoutbar) == 8) and (self.windowMain.toolBarArea(self.formatbar) == 4) and \
            (self.formatbar.geometry().top() < self.toolbar.geometry().top() < self.layoutbar.geometry().top())):
            MainGuiWindow.DOCKING = 22
        elif  ((self.windowMain.toolBarArea(self.toolbar) == 8) and (self.windowMain.toolBarArea(self.layoutbar) == 8) and (self.windowMain.toolBarArea(self.formatbar) == 4) and \
            (self.formatbar.geometry().top() < self.layoutbar.geometry().top() < self.toolbar.geometry().top())):
            MainGuiWindow.DOCKING = 23

        else:
            MainGuiWindow.DOCKING = 0

        # Close auxiliary windows if open
        try:
            if self.window3 is not None:
                self.window3.close()                # ColorPicker
            else:
                # print("Error: self.window3 is None.")
                pass
            # self.window3.close()
        except:
            pass

        try:
            if self.window4 is not None:
                self.window4.close()                # FindReplace
            else:
                # print("Error: self.window4 is None.")
                pass
            # self.window4.close()
        except:
            pass

        # Close OpenCV windows and the main window
        cv2.destroyAllWindows()
        self.close()

    #//===================================================//
    def mousePressEvent(self, event):
        """
        Handles mouse press events and logs the type of mouse button pressed.
        """
        print('=== mousePressEvent ===')
        if event.buttons() == Qt.MouseButton.NoButton:
            print("=== No mouse button is pressed ===")
        elif event.buttons() == Qt.MouseButton.LeftButton:
            print("=== Left click ===")
        elif event.buttons() == Qt.MouseButton.RightButton:
            print("=== Right click ===")
        elif event.buttons() == Qt.MouseButton.MidButton:
            print("=== Middle click ===")


    def mouseMoveEvent(self, event):
        """
        Handles mouse movement events and updates the window's dimensions.
        """
        print('=== mouseMoveEvent ===')
        TextGuiWindow.w2 = self.frameGeometry().width()
        TextGuiWindow.h2 = self.frameGeometry().height() - 90
        print('w2 := ', TextGuiWindow.w2)
        print('h2 := ', TextGuiWindow.h2)


    def resizeEvent(self,event=None):
        """
        Handles window resize events and adjusts the minimum width based on icon size.
        """
        print("=== resizeEvent ===")

        if MainGuiWindow.flag_resize_window:
            MainGuiWindow.flag_resize_window = False
            if (MainGuiWindow.TextEditorIconSizeVar1 == 16):
                MainGuiWindow.WIDTH1_MIN = int(0.220*WIDTH1)
                TextGuiWindow.setMinimumWidth(self,MainGuiWindow.WIDTH1_MIN+30)

                if (MainGuiWindow.WIDTH1_MIN > (self.size().width()-30)):
                    TextGuiWindow.resize(self,MainGuiWindow.WIDTH1_MIN+30,self.size().height())

            elif (MainGuiWindow.TextEditorIconSizeVar1 == 18):
                MainGuiWindow.WIDTH1_MIN = int(0.235*WIDTH1)
                TextGuiWindow.setMinimumWidth(self,MainGuiWindow.WIDTH1_MIN+30)

                if (MainGuiWindow.WIDTH1_MIN > (self.size().width()-30)):
                    TextGuiWindow.resize(self,MainGuiWindow.WIDTH1_MIN+30,self.size().height())

            elif (MainGuiWindow.TextEditorIconSizeVar1 == 22):
                MainGuiWindow.WIDTH1_MIN = int(0.270*WIDTH1)
                TextGuiWindow.setMinimumWidth(self,MainGuiWindow.WIDTH1_MIN+30)

                if (MainGuiWindow.WIDTH1_MIN > (self.size().width()-30)):
                    TextGuiWindow.resize(self,MainGuiWindow.WIDTH1_MIN+30,self.size().height())

    #//===================================================//
    def paintEvent(self,event=None):
        """
        Handles the paint event to set the background color and border style.
        """
        painter = QPainter(self)
        TextGuiWindow.setBackgroundColor(self,painter)
        TextGuiWindow.setBorderStyle(self)

        if MainGuiWindow.flag_resize_window:
            TextGuiWindow.resizeEvent(self)

    # #//===================================================//
    def setBackgroundColor(self,painter):
        """
        Sets the background color of the window based on the selected theme.
        """
        if MainGuiWindow.THEME == "light":
            if (MainGuiWindow.ThemeLightColorVar1 == 6):
                painter.setBrush(QColor(MainGuiWindow.BG_COLOR_LIGHT_CUSTOM))
                painter.setPen(QPen(QColor(MainGuiWindow.BG_COLOR_LIGHT_CUSTOM)))
            else:
                painter.setBrush(QColor(Qt.GlobalColor.white))
                painter.setPen(QPen(QColor(Qt.GlobalColor.white)))


        if MainGuiWindow.THEME == "dark":
            if (MainGuiWindow.ThemeDarkColorVar1 == 6):
                painter.setBrush(QColor(MainGuiWindow.BG_COLOR_DARK_CUSTOM))
                painter.setPen(QPen(QColor(MainGuiWindow.BG_COLOR_DARK_CUSTOM)))
            else:
                painter.setBrush(QColor(50,50,50))
                painter.setPen(QPen(QColor(50,50,50)))

        if MainGuiWindow.THEME == 'light':
            painter.setOpacity(MainGuiWindow.OPACITY_TEXT_LIGHT)
        elif MainGuiWindow.THEME == 'dark':
            painter.setOpacity(MainGuiWindow.OPACITY_TEXT_DARK)
        painter.drawRect(self.rect())

    # #//===================================================//
    def setBorderStyle(self):
        """
        Sets the border style of the window based on the configuration.
        """
        if (MainGuiWindow.BorderStyleVar1 == 0):
            radius = 0
        elif (MainGuiWindow.BorderStyleVar1 == 1):
            radius = 5

        path = QPainterPath()
        rect = QRectF(self.rect()).adjusted(0.5, 0.5, -0.5, -0.5)
        path.addRoundedRect(rect,radius,radius)
        region = QRegion(path.toFillPolygon(QTransform()).toPolygon())
        self.setMask(region)

    #//==========================================================//
    def keyPressEvent(self, event):
        """
        Handles key press events. Hides the window when the Escape key is pressed.
        """
        print('=== keyPressEvent ===')
        if (event.key() == Qt.Key.Key_Escape):      # Key Esc
            print('=== Esc ===')
            self.hide()






########################################################################
class TextEdit(QTextEdit):
    def __init__(self, parent=None):
        # Initialize the QTextEdit widget
        QTextEdit.__init__(self, parent)

    def paintEvent(self, event):
        # Handle the paint event and update word count and cursor position
        QTextEdit.paintEvent(self,event)

        if self.hasFocus():
            self.wordCount()
            cursor = TextGuiWindow.textbox.textCursor()
            x = int(cursor.columnNumber() + 1)
            y = int(cursor.blockNumber() + 1)

            # Update status bar with selection or cursor position
            if cursor.hasSelection():
                TextGuiWindow.labelStatusbar1.setText(f"Select: {symbols_selected}" + "  " + f"Word: {words_selected}")
            else:
                TextGuiWindow.labelStatusbar1.setText("")
            TextGuiWindow.labelStatusbar2.setText(f"Line: {y}" + "  " + f"Column: {x}")
            TextGuiWindow.labelStatusbar3.setText(f"Total: {symbols_total}" + "  " + f"Word: {words_total}")

    def wordCount(self):
        # Calculate word and symbol counts for selected and total text
        global symbols_selected, symbols_total, words_selected, words_total
        text_selected = TextGuiWindow.textbox.textCursor().selectedText()
        words_selected = str(len(text_selected.split()))
        symbols_selected = str(len(text_selected))
        text = TextGuiWindow.textbox.toPlainText()
        words_total = str(len(text.split()))
        symbols_total = str(len(text))







########################################################################
class WindowDragger(QWidget):
    doubleClicked = Signal()

    def __init__(self, window, parent=None):
        # Initialize the draggable window widget
        QWidget.__init__(self, parent)
        self._window = window
        self._mousePressed = False

    def mouseDoubleClickEvent(self, event):
        # Emit a signal on double-click
        print("=== mouseDoubleClickEvent ===")
        self.doubleClicked.emit()

    def mousePressEvent(self, event):
        # Capture the initial mouse and window positions on mouse press
        print('=== mousePressEvent ===')
        self._mousePressed = True
        self._mousePos = event.globalPos()
        self._windowPos = self._window.pos()

    def mouseMoveEvent(self, event):
        # Handle window dragging and enforce screen boundaries
        if (QCursor.pos().x() >= (WIDTH-50)):
            print("========== limited WIDTH ==========")
            QCursor.setPos(WIDTH-50,QCursor.pos().y())

        if (QCursor.pos().y() >= (HEIGHT-50)):
            print("========== limited HEIGHT ==========")
            QCursor().setPos(QCursor.pos().x(),HEIGHT-50)

        print('FLAG_TOOLBAR := ', MainGuiWindow.FLAG_TOOLBAR)
        print('FLAG_FORMATBAR := ', MainGuiWindow.FLAG_FORMATBAR)

        x0Pos = int(self._windowPos.x() + (event.globalPos() - self._mousePos).x())
        y0Pos = int(self._windowPos.y() + (event.globalPos() - self._mousePos).y())
        print('Pos2 := ', x0Pos, y0Pos)

        if self._mousePressed:
            # Enforce boundaries for window movement
            if (x0Pos < 0):
                print('=== limit 1 (Toolbar) ===')
                if (y0Pos < 0):
                    print('=== limit 1-1 ===')
                    self._window.move(0,0)
                elif ((y0Pos+TextGuiWindow.h2+HEIGHT_TT+HEIGHT_TB+30) > HEIGHT):
                    print('=== limit 1-2 ===')
                    self._window.move(0,HEIGHT-TextGuiWindow.h2-HEIGHT_TT-HEIGHT_TB-30)
                else:
                    print('=== limit 1-3 ===')
                    self._window.move(0,y0Pos)

            elif (y0Pos < 30):
                print('=== limit 2 (Toolbar) ===')
                if (x0Pos < 0):
                    print('=== limit 2-1 ===')
                    self._window.move(0,0)
                elif ((x0Pos+TextGuiWindow.w2) > WIDTH):
                    print('=== limit 2-2 ===')
                    self._window.move(WIDTH-TextGuiWindow.w2, 0)
                else:
                    print('=== limit 2-3 ===')
                    self._window.move(x0Pos,0)

            elif ((x0Pos+TextGuiWindow.w2) > WIDTH):
                print('=== limit 3 (Toolbar) ===')
                if (y0Pos < 30):
                    print('=== limit 3-1 ===')
                    self._window.move(WIDTH-TextGuiWindow.w2,0)
                elif ((y0Pos+TextGuiWindow.h2+HEIGHT_TT+HEIGHT_TB-0) > HEIGHT):
                    print('=== limit 3-2 ===')
                    self._window.move(WIDTH-TextGuiWindow.w2,HEIGHT-TextGuiWindow.h2-HEIGHT_TT-HEIGHT_TB-30)
                else:
                    print('=== limit 3-3 ===')
                    self._window.move(WIDTH-TextGuiWindow.w2,y0Pos-30)

            elif ((y0Pos+TextGuiWindow.h2+HEIGHT_TT+HEIGHT_TB-0) > HEIGHT):
                print('=== limit 4 (Toolbar) ===')
                if (x0Pos < 0):
                    print('=== limit 4-1 ===')
                    self._window.move(0, HEIGHT-TextGuiWindow.h2-HEIGHT_TT-HEIGHT_TB-30)
                elif ((x0Pos+TextGuiWindow.w2) > WIDTH):
                    print('=== limit 4-2 ===')
                    self._window.move(WIDTH-TextGuiWindow.w2, HEIGHT-TextGuiWindow.h2-HEIGHT_TT-HEIGHT_TB-30)
                else:
                    print('=== limit 4-3 ===')
                    self._window.move(x0Pos, HEIGHT-TextGuiWindow.h2-HEIGHT_TT-HEIGHT_TB-30)

            else:
                self._window.move(x0Pos,y0Pos-30)

    def mouseReleaseEvent(self, event):
        # Reset mouse press state and update window position
        global x0Pos, y0Pos
        self._mousePressed = False
        x0Pos = self._window.x() + int(TextGuiWindow.w2/2) - (0/2)
        y0Pos = self._window.y() + int(TextGuiWindow.h2/2) - (0/2)
        print('x0Pos, y0Pos := ', x0Pos, y0Pos)

    def enterEvent(self, event):
        # Update mouse and window positions on mouse enter
        self._mousePos = event.globalPos()
        self._windowPos = self._window.pos()

    def leaveEvent(self, event):
        # Handle mouse leave event (currently does nothing)
        pass

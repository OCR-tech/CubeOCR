# Import necessary modules and constants from py_main_gui
from src.module.py_window_main import *  # Import all components from py_main_gui


WIDTH = 1920  # Example screen width
HEIGHT = 1080  # Example screen height


# Define a dictionary of color palettes
PALETTES = {
    'rgb_color':    ['#330000', '#331900', '#333300', '#003300', '#003333', '#000033', '#190033', '#330033', '#330019', '#000000', \
                     '#660000', '#663300', '#666600', '#006600', '#006666', '#000066', '#330066', '#660066', '#660033', '#202020', \
                     '#990000', '#994C00', '#999900', '#009900', '#009999', '#000099', '#4C0099', '#990099', '#99004C', '#404040', \
                     '#CC0000', '#CC6600', '#CCCC00', '#00CC00', '#00CCCC', '#0000CC', '#6600CC', '#CC00CC', '#CC0066', '#606060', \
                     '#FF0000', '#FF8000', '#FFFF00', '#00FF00', '#00FFFF', '#0000FF', '#7F00FF', '#FF00FF', '#FF007F', '#808080', \
                     '#FF3333', '#FF9933', '#FFFF33', '#33FF33', '#33FFFF', '#3333FF', '#9933FF', '#FF33FF', '#FF3399', '#A0A0A0', \
                     '#FF6666', '#FFB266', '#FFFF66', '#66FF66', '#66FFFF', '#6666FF', '#B266FF', '#FF66FF', '#FF66B2', '#C0C0C0', \
                     '#FF9999', '#FFCC99', '#FFFF99', '#99FF99', '#99FFFF', '#9999FF', '#CC99FF', '#FF99FF', '#FF99CC', '#E0E0E0', \
                     '#FFCCCC', '#FFE5CC', '#FFFFCC', '#CCFFCC', '#CCFFFF', '#CCCCFF', '#E5CCFF', '#FFCCFF', '#FFCCE5', '#FFFFFF', \
                     ]
}


########################################################################
class _PaletteButton(QPushButton):
    """
    Custom button representing a single color in the palette.
    """
    def __init__(self, color):
        super().__init__()
        self.setFixedSize(QtCore.QSize(24,24))                  # Set fixed size for the button
        self.color = color                                      # Store the color value
        self.setStyleSheet("background-color: %s;" % color)     # Set the background color of the button



class _PaletteBase(QWidget):
    """
    Base class for color palettes, providing a signal for color selection.
    """
    selected = Signal(object)           # Signal emitted when a color is selected

    def _emit_color(self, color):
        # Emits the selected color through the signal.
        self.selected.emit(color)



class PaletteGrid(_PaletteBase):
    """
    Grid layout for displaying a palette of colors.
    """
    def __init__(self, colors, n_columns=10, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # If colors is a string, retrieve the corresponding palette from PALETTES
        if isinstance(colors, str):
            if colors in PALETTES:
                colors = PALETTES[colors]

        # Create a grid layout for the palette
        palette = QGridLayout()
        palette.setContentsMargins(0,0,0,0)
        palette.setSpacing(3)
        row, col = 0, 0

        # Add buttons for each color in the palette
        for c in colors:
            b = _PaletteButton(c)
            b.pressed.connect(
                lambda c=c: self._emit_color(c)
            )
            palette.addWidget(b,row,col)
            col += 1
            if col == n_columns:
                col = 0
                row += 1
        self.setLayout(palette)



########################################################################
class ColorPicker(QMainWindow):
    """
    Main window for the color picker dialog.
    """
    def __init__(self):
        super().__init__()
        # Set window properties: frameless, centered, fixed size
        self.setWindowFlags(Qt.Window | Qt.WindowType.FramelessWindowHint | Qt.WindowType.NoDropShadowWindowHint | Qt.WindowType.WindowStaysOnTopHint) # type: ignore
        self.setGeometry(int((WIDTH-300)/2),int((HEIGHT-300-150)/2),300,300)

        # Main vertical layout for the color picker
        self.vboxWindow = QVBoxLayout()
        self.vboxWindow.setContentsMargins(0,0,0,0)

        # Title bar setup
        ColorPicker.labelTitle3 = QLabel()
        self.labelTitle3.setText('Select Color')
        self.labelTitle3.setObjectName('lblTitle3')
        self.labelTitle3.setGeometry(0,0,300,28)
        self.labelTitle3.setFixedHeight(28)

        # Draggable title bar
        self.titleBar = WindowDragger(self,self.labelTitle3)
        self.titleBar.setGeometry(0,0,300,28)
        self.titleBar.setSizePolicy(QSizePolicy(QSizePolicy.Preferred,QSizePolicy.Fixed))

        # Create the color palette grid
        self.palette = PaletteGrid('rgb_color')
        self.palette.selected.connect(self.show_selected_color)

        # Bottom label for buttons
        self.labelbutton = QLabel()
        self.labelbutton.setObjectName('labelbutton')
        self.labelbutton.setGeometry(0,0,300,25)
        self.labelbutton.setFixedHeight(25)

        # Bottom separator
        self.labelbottom = QLabel()
        self.labelbottom.setObjectName('labelbottom')
        self.labelbottom.setGeometry(0,0,300,8)
        self.labelbottom.setFixedHeight(8)

        # Horizontal layout for the palette
        self.hboxWindow = QHBoxLayout()
        self.hboxWindow.setContentsMargins(0,0,0,0)
        self.hboxWindow.addSpacing(12)
        self.hboxWindow.addWidget(self.palette)
        self.hboxWindow.addSpacing(6)

        # Content container
        self.containerContent = QWidget()
        self.containerContent.setLayout(self.hboxWindow)

        # Add components to the main vertical layout
        self.vboxWindow.addWidget(self.labelTitle3)
        self.vboxWindow.addSpacing(10)
        self.vboxWindow.addWidget(self.containerContent)
        self.vboxWindow.addSpacing(8)
        self.vboxWindow.addWidget(self.labelbutton)
        self.vboxWindow.setSpacing(0)
        self.vboxWindow.addWidget(self.labelbottom)

        # Set the central widget
        ColorPicker.container3 = QWidget()
        self.container3.setObjectName('ctn3')
        self.container3.setLayout(self.vboxWindow)
        self.setCentralWidget(self.container3)

        # Add "OK" button
        self.btnOK3 = QPushButton(self.labelbutton)
        self.btnOK3.setGeometry(QRect(45,0,75,25))
        self.btnOK3.setObjectName("btnOK3")
        self.btnOK3.setText("OK")
        self.btnOK3.clicked.connect(self.OKSetting)

        # Add "Cancel" button
        self.btnCancel3 = QPushButton(self.labelbutton)
        self.btnCancel3.setGeometry(QRect(185,0,75,25))
        self.btnCancel3.setObjectName("btnCancel3")
        self.btnCancel3.setText("Cancel")
        self.btnCancel3.clicked.connect(self.CancelSetting)

        # Apply theme based on user settings
        from src.module.py_window_main import MainGuiWindow
        from src.func.py_main_editor import TextGuiWindow

        if MainGuiWindow.THEME == "light":
            TextGuiWindow.set_LightTheme(self)
        elif MainGuiWindow.THEME == "dark":
            TextGuiWindow.set_DarkTheme(self)
        TextGuiWindow.read_StyleSheet(self)

    #//===================================================//
    def exitKeyPressed(self):
        """
        Handles the "Escape" key press event. Closes the color picker window and exits the program.
        """
        from src.module.py_window_main import MainGuiWindow

        print('=== exitKeyPressed ===')
        self.close()
        MainGuiWindow.exitProgram(self)

    # //===========================================//
    def show_selected_color(self, c):
        """
        Displays the selected color and updates the text color in the editor.
        """
        from src.func.py_main_editor import TextGuiWindow

        print("Selected: {}".format(c))         # Log the selected color
        TextGuiWindow.color_selected = c        # Update the selected color in the editor
        print('color_selected := ', TextGuiWindow.color_selected)
        TextGuiWindow.setTextColor(self)        # Apply the selected color to the text

    # //===========================================//
    def OKSetting(self):
        """
        Handles the "OK" button click event. Saves the selected color and re-enables editor actions.
        """
        print('=== OKSetting ===')
        from src.module.py_window_main import MainGuiWindow
        from src.func.py_main_editor import TextGuiWindow

        try:
            # Re-enable editor actions after confirming the color selection
            TextGuiWindow.preview_action.setEnabled(True)
            TextGuiWindow.print_action.setEnabled(True)
            TextGuiWindow.find_replace_action.setEnabled(True)
            TextGuiWindow.font_color_action.setEnabled(True)
            TextGuiWindow.font_color_highlight_action.setEnabled(True)
            TextGuiWindow.updateEnabled_icon(self)
        except:
            pass

        try:
            TextGuiWindow.setting_action.setEnabled(True)
            TextGuiWindow.set_textfont_action.setEnabled(True)
            TextGuiWindow.set_textcolor_action.setEnabled(True)
            TextGuiWindow.reset_action.setEnabled(True)
            TextGuiWindow.updateEnabled_icon(self)
        except:
            pass

        self.close()
        print('---------------------')

    # //===========================================//
    def CancelSetting(self):
        """
        Handles the "Cancel" button click event. Restores the previously selected color and re-enables editor actions.
        """
        from src.func.py_main_editor import TextGuiWindow

        print('=== CancelSetting ===')
        TextGuiWindow.color_selected = TextGuiWindow.color_preselected
        TextGuiWindow.setTextColor(self)

        from src.module.py_window_main import MainGuiWindow
        from src.func.py_main_editor import TextGuiWindow

        try:
            # Re-enable editor actions after canceling the color selection
            TextGuiWindow.preview_action.setEnabled(True)
            TextGuiWindow.print_action.setEnabled(True)
            TextGuiWindow.find_replace_action.setEnabled(True)
            TextGuiWindow.font_color_action.setEnabled(True)
            TextGuiWindow.font_color_highlight_action.setEnabled(True)
            TextGuiWindow.updateEnabled_icon(self)
        except:
            pass

        try:
            TextGuiWindow.setting_action.setEnabled(True)
            TextGuiWindow.set_textfont_action.setEnabled(True)
            TextGuiWindow.set_textcolor_action.setEnabled(True)
            TextGuiWindow.reset_action.setEnabled(True)
            TextGuiWindow.updateEnabled_icon(self)
        except:
            pass

        self.close()
        print('---------------------')

    # //===================================================//
    def paintEvent(self, event=None):
        """
        Handles the paint event to set the background color and border style of the color picker window.
        """
        print('=== paintEvent SettingWindow (begin) ===')
        painter = QPainter(self)
        self.setBackgroundColor(painter)
        self.setBorderStyle()
        print('=== paintEvent SettingWindow (end) ===')

    # //===================================================//
    def setBackgroundColor(self,painter):
        """
        Sets the background color of the color picker window based on the selected theme.
        """
        from src.module.py_window_main import MainGuiWindow

        print('=== setBackgroundColor ===')
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

        painter.setOpacity(1)
        painter.drawRect(self.rect())

# //===========================================//
    def setBorderStyle(self):
        """
        Sets the border style of the color picker window based on the configuration.
        """
        from src.module.py_window_main import MainGuiWindow

        if (MainGuiWindow.BorderStyleVar1 == 0):
            radius = 0
        elif (MainGuiWindow.BorderStyleVar1 == 1):
            radius = 5

        path = QPainterPath()
        rect = QRectF(self.rect()).adjusted(0.5, 0.5, -0.5, -0.5)
        path.addRoundedRect(rect, radius, radius)
        region = QRegion(path.toFillPolygon(QTransform()).toPolygon())
        self.setMask(region)

    # //==========================================================//
    def keyPressEvent(self, event):
        """
        Handles key press events. Closes the color picker window when the Escape key is pressed.
        """
        print('=== keyPressEvent ===')
        if (event.key() == Qt.Key.Key_Escape):
            print('=== Esc ===')
            self.CancelSetting()



########################################################################
class WindowDragger(QWidget):
    """
    Custom widget to enable dragging of the window.
    """
    # doubleClicked = pyqtSignal()  # Add the doubleClicked signal
    def __init__(self, window, parent=None):
        """
        Initializes the WindowDragger with the parent window.
        """
        QWidget.__init__(self, parent)
        self._window = window           # Reference to the window being dragged
        self._mousePressed = False      # Tracks whether the mouse is pressed

    def mousePressEvent(self, event):
        """
        Captures the initial mouse and window positions on mouse press.
        """
        print('=== mousePressEvent ===')
        self._mousePressed = True               # Set mouse pressed state to True
        self._mousePos = event.globalPos()      # Store the global mouse position
        self._windowPos = self._window.pos()    # Store the current window position

    def mouseMoveEvent(self, event):
        """
        Handles window dragging and enforces screen boundaries.
        """
        global x0Pos, y0Pos
        w1 = 300        # Window width
        h1 = 300        # Window height

        # Enforce horizontal boundary
        if (QCursor.pos().x() >= (WIDTH-50)):
            print("=== limited ===")
            QCursor.setPos(WIDTH-50,QCursor.pos().y())

        # Enforce vertical boundary
        if (QCursor.pos().y() >= (HEIGHT-50)):
            print("=== limited ===")
            QCursor().setPos(QCursor.pos().x(),HEIGHT-50)

        # Calculate new window position based on mouse movement
        x0Pos = int(self._windowPos.x() + (event.globalPos() - self._mousePos).x())
        y0Pos = int(self._windowPos.y() + (event.globalPos() - self._mousePos).y())

        if self._mousePressed:
            # Enforce boundaries for window movement
            if (x0Pos < 0):
                print('=== limit 1 ===')
                if (y0Pos < 0):
                    self._window.move(0, 0)                     # Top-left corner boundary
                elif ((y0Pos+h1) > HEIGHT):
                    self._window.move(0, HEIGHT-h1-18)          # Bottom-left corner boundary
                else:
                    self._window.move(0, y0Pos)                 # Left boundary

            elif (y0Pos < 0):
                print('=== limit 2 ===')
                if (x0Pos < 0):
                    self._window.move(0, 0)                     # Top-left corner boundary
                elif ((x0Pos+w1) > WIDTH):
                    self._window.move(WIDTH-w1, 0)              # Top-right corner boundary
                else:
                    self._window.move(x0Pos, 0)                 # Top boundary

            elif ((x0Pos+w1) > WIDTH):
                print('=== limit 3 ===')
                if (y0Pos < 0):
                    self._window.move(WIDTH-w1, 0)              # Top-right corner boundary
                elif ((y0Pos+h1) > HEIGHT):
                    self._window.move(WIDTH-w1, HEIGHT-h1-18)   # Bottom-right corner boundary
                else:
                    self._window.move(WIDTH-w1, y0Pos)          # Right boundary

            elif ((y0Pos+h1+20) > HEIGHT):
                print('=== limit 4 ===')
                if (x0Pos < 0):
                    self._window.move(0, HEIGHT-h1-18)          # Bottom-left corner boundary
                elif ((x0Pos+w1) > WIDTH):
                    self._window.move(WIDTH-w1, HEIGHT-h1-18)   # Bottom-right corner boundary
                else:
                    self._window.move(x0Pos, HEIGHT-h1-18)      # Bottom boundary
            else:
                self._window.move(x0Pos, y0Pos)                 # Free movement within boundaries

    def mouseReleaseEvent(self, event):
        """
        Resets the mouse pressed state on mouse release.
        """
        print("=== mouseReleaseEvent ===")
        self._mousePressed = False  # Reset mouse pressed state

    def mouseDoubleClickEvent(self, event):
        """
        Placeholder for handling double-click events.
        """
        print("=== mouseDoubleClickEvent ===")
        # self.doubleClicked.emit()

    def enterEvent(self, event):
        """
        Updates the window position when the mouse enters the widget.
        """
        print("=== enterEvent ===")
        self._windowPos = self._window.pos()    # Update the stored window position

    def leaveEvent(self, event):
        """
        Placeholder for handling mouse leave events.
        """
        print("=== leaveEvent ===")

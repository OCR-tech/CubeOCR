# Import necessary modules and constants from py_main_gui
from src.module.py_window_main import *  # Import all components from py_main_gui
from src.module.py_window_main import WIDTH, HEIGHT  # Import screen width and height constants



########################################################################
class FindReplace(QDialog):
    def __init__(self, parent = None):
        """
        Initializes the Find & Replace dialog.
        """
        QDialog.__init__(self, parent)
        self._parent = parent
        self.lastStart = 0
        self.initUI()

    def initUI(self):
        """
        Sets up the UI components for the Find & Replace dialog.
        """
        # Set window properties: frameless, centered, fixed size
        # self.setWindowFlags(Qt.WindowFlags.Window | Qt.WindowFlags.FramelessWindowHint | Qt.WindowFlags.NoDropShadowWindowHint | Qt.WindowFlags.WindowStaysOnTopHint)
        self.setWindowFlags(Qt.Window | Qt.WindowType.FramelessWindowHint | Qt.WindowType.NoDropShadowWindowHint | Qt.WindowType.WindowStaysOnTopHint) # type: ignore
        self.setGeometry(int((WIDTH-360)/2),int((HEIGHT-183-150)/2),360,183)

        # Main vertical layout for the dialog
        self.vboxWindow = QVBoxLayout()
        self.vboxWindow.setContentsMargins(0,0,0,0)

        # Title bar setup
        FindReplace.labelTitle4 = QLabel()
        self.labelTitle4.setText('Find & Replace')
        self.labelTitle4.setObjectName('lblTitle4')
        self.labelTitle4.setGeometry(0,0,360,28)
        self.labelTitle4.setFixedHeight(28)

        # Draggable title bar
        self.titleBar = WindowDragger(self,self.labelTitle4)
        self.titleBar.setGeometry(0,0,360,28)
        self.titleBar.setSizePolicy(QSizePolicy(QSizePolicy.Preferred,QSizePolicy.Fixed))

        # Grid layout for the content
        layout = QGridLayout()

        # Content container
        FindReplace.containerContent4 = QWidget()
        self.containerContent4.setObjectName('ctnContent4')
        self.containerContent4.setLayout(layout)

        # Add title bar and content container to the main layout
        self.vboxWindow.addWidget(self.labelTitle4)
        self.vboxWindow.setSpacing(0)
        self.vboxWindow.addWidget(self.containerContent4)

        self.setLayout(self.vboxWindow)

        # Add "Find" label and text field
        self.label1 = QLabel(self.containerContent4)
        self.label1.setObjectName('label1')
        self.label1.setText('Find :')
        self.label1.setGeometry(QRect(15,10,150,25))

        self.findField = QTextEdit(self.containerContent4)
        self.findField.setObjectName('txtff')
        self.findField.setGeometry(QRect(75,12,185,24))

        # Add "Find" button
        findButton = QPushButton(self.containerContent4)
        findButton.setGeometry(QRect(272,12,75,25))
        findButton.setText('Find')
        findButton.clicked.connect(self.findFcn)

        # Add "Replace" label and text field
        self.label2 = QLabel(self.containerContent4)
        self.label2.setObjectName('label2')
        self.label2.setText('Replace :')
        self.label2.setGeometry(QRect(15,45,150,25))

        self.replaceField = QTextEdit(self.containerContent4)
        self.replaceField.setObjectName('txtrf')
        self.replaceField.setGeometry(QRect(75,47,185,24))

        # Add "Replace" button
        replaceButton = QPushButton(self.containerContent4)
        replaceButton.setGeometry(QRect(272,47,75,25))
        replaceButton.setText('Replace')
        replaceButton.clicked.connect(self.replaceFcn)

        # Add "Replace All" button
        allButton = QPushButton(self.containerContent4)
        allButton.setGeometry(QRect(272,82,75,25))
        allButton.setText('Replace all')
        allButton.clicked.connect(self.replaceAllFcn)

        # Add "Close" button
        self.btnClose4 = QPushButton(self.containerContent4)
        self.btnClose4.setGeometry(QRect(272,117,75,25))
        self.btnClose4.setObjectName("btnClose4")
        self.btnClose4.setText('Close')
        self.btnClose4.clicked.connect(self.closeFindReplace)

        self.setLayout(layout)

        # Apply theme based on user settings
        from src.module.py_window_main import MainGuiWindow
        from src.func.py_main_editor import TextGuiWindow

        if MainGuiWindow.THEME == "light":
            TextGuiWindow.set_LightTheme(self)
        elif MainGuiWindow.THEME == "dark":
            TextGuiWindow.set_DarkTheme(self)
        TextGuiWindow.read_StyleSheet(self)

    # //===================================================//
    def exitKeyPressed(self):
        """
        Handles the "Escape" key press event. Closes the Find & Replace dialog and exits the program.
        """
        from src.module.py_window_main import MainGuiWindow

        print('=== exitKeyPressed ===')
        self.close()
        MainGuiWindow.exitProgram(self)

    # //===================================================//
    def closeFindReplace(self):
        """
        Handles the "Close" button click event. Closes the Find & Replace dialog.
        """
        print('=== CloseFindReplace ===')
        from src.func.py_main_editor import TextGuiWindow
        try:
            # Re-enable editor actions after closing the dialog
            TextGuiWindow.setting_action.setEnabled(True)
            TextGuiWindow.set_textfont_action.setEnabled(True)
            TextGuiWindow.set_textcolor_action.setEnabled(True)
            TextGuiWindow.reset_action.setEnabled(True)
            TextGuiWindow.preview_action.setEnabled(True)
            TextGuiWindow.print_action.setEnabled(True)
            TextGuiWindow.find_replace_action.setEnabled(True)
            TextGuiWindow.font_color_action.setEnabled(True)
            TextGuiWindow.font_color_highlight_action.setEnabled(True)
            TextGuiWindow.updateEnabled_icon(self)
        except:
            pass
        self.close()

    # //===================================================//
    def findFcn(self):
        """
        Searches for the next occurrence of the query in the text editor.
        """
        from src.func.py_main_editor import TextGuiWindow

        text = TextGuiWindow.textbox.toPlainText()
        query = self.findField.toPlainText()
        self.lastStart = text.find(query,self.lastStart + 1)

        if self.lastStart >= 0:
            end = self.lastStart + len(query)
            self.moveCursor(self.lastStart,end)
        else:
            self.lastStart = 0
            TextGuiWindow.textbox.moveCursor(QtGui.QTextCursor.End)

    # //===================================================//
    def replaceFcn(self):
        """
        Replaces the currently selected text with the replacement text.
        """
        from src.func.py_main_editor import TextGuiWindow

        cursor = TextGuiWindow.textbox.textCursor()
        if cursor.hasSelection():
            cursor.insertText(self.replaceField.toPlainText())
            TextGuiWindow.textbox.setTextCursor(cursor)

    # //===================================================//
    def replaceAllFcn(self):
        """
        Replaces all occurrences of the search query with the replacement text.
        """
        self.lastStart = 0
        self.findFcn()
        while self.lastStart:
            self.replaceFcn()
            self.findFcn()

    # //===================================================//
    def moveCursor(self,start,end):
        """
        Moves the cursor to highlight the specified range in the text editor.
        """
        from src.func.py_main_editor import TextGuiWindow

        cursor = TextGuiWindow.textbox.textCursor()
        cursor.setPosition(start)
        cursor.movePosition(QtGui.QTextCursor.Right,QtGui.QTextCursor.KeepAnchor,end - start)
        TextGuiWindow.textbox.setTextCursor(cursor)

    # //===================================================//
    def paintEvent(self, event=None):
        """
        Handles the paint event to set the background color and border style.
        """
        print('=== paintEvent SettingWindow (begin) ===')
        painter = QPainter(self)
        self.setBackgroundColor(painter)
        self.setBorderStyle()
        print('=== paintEvent SettingWindow (end) ===')

    # //===================================================//
    def setBackgroundColor(self,painter):
        """
        Sets the background color of the dialog based on the selected theme.
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
        Sets the border style of the dialog based on the configuration.
        """
        from src.module.py_window_main import MainGuiWindow

        if (MainGuiWindow.BorderStyleVar1 == 0):
            radius = 0
            self.containerContent4.setStyleSheet('border-radius: 0px;')
        elif (MainGuiWindow.BorderStyleVar1 == 1):
            radius = 5

        path = QPainterPath()
        rect = QRectF(self.rect()).adjusted(0.5, 0.5, -0.5, -0.5)
        path.addRoundedRect(rect, radius, radius)

        # Apply the mask to enforce the border style
        region = QRegion(path.toFillPolygon(QTransform()).toPolygon())
        self.setMask(region)

    # //==========================================================//
    def keyPressEvent(self, event):
        """
        Handles key press events. Closes the dialog when the Escape key is pressed.
        """
        print('=== keyPressEvent ===')
        if (event.key() == Qt.Key.Key_Escape):
            print('=== Esc ===')
            self.closeFindReplace()




########################################################################
class WindowDragger(QWidget):
    """
    Custom widget to enable dragging of the window.
    """
    def __init__(self, window, parent=None):
        """
        Initializes the WindowDragger with the parent window.
        """
        QWidget.__init__(self, parent)
        self._window = window
        self._mousePressed = False

    def mousePressEvent(self, event):
        """
        Captures the initial mouse and window positions on mouse press.
        """
        print('=== mousePressEvent ===')
        self._mousePressed = True
        self._mousePos = event.globalPos()
        self._windowPos = self._window.pos()

    def mouseMoveEvent(self, event):
        """
        Handles window dragging and enforces screen boundaries.
        """
        global x0Pos, y0Pos
        w1 = 360        # Window width
        h1 = 183        # Window height

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
                    self._window.move(0, 0)                 # Top-left corner boundary
                elif ((y0Pos+h1) > HEIGHT):
                    self._window.move(0, HEIGHT-h1)         # Bottom-left corner boundary
                else:
                    self._window.move(0, y0Pos)             # Left boundary

            elif (y0Pos < 0):
                print('=== limit 2 ===')
                if (x0Pos < 0):
                    self._window.move(0, 0)                 # Top-left corner boundary
                elif ((x0Pos+w1) > WIDTH):
                    self._window.move(WIDTH-w1, 0)          # Top-right corner boundary
                else:
                    self._window.move(x0Pos, 0)             # Top boundary

            elif ((x0Pos+w1) > WIDTH):
                print('=== limit 3 ===')
                if (y0Pos < 0):
                    self._window.move(WIDTH-w1, 0)          # Top-right corner boundary
                elif ((y0Pos+h1) > HEIGHT):
                    self._window.move(WIDTH-w1, HEIGHT-h1)  # Bottom-right corner boundary
                else:
                    self._window.move(WIDTH-w1, y0Pos)      # Right boundary

            elif ((y0Pos+h1) > HEIGHT):
                print('=== limit 4 ===')
                if (x0Pos < 0):
                    self._window.move(0, HEIGHT-h1)         # Bottom-left corner boundary
                elif ((x0Pos+w1) > WIDTH):
                    self._window.move(WIDTH-w1, HEIGHT-h1)  # Bottom-right corner boundary
                else:
                    self._window.move(x0Pos, HEIGHT-h1)     # Bottom boundary
            else:
                self._window.move(x0Pos, y0Pos)             # Free movement within boundaries

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

    def enterEvent(self, event):
        """
        Updates the window position when the mouse enters the widget.
        """
        print("=== enterEvent ===")
        self._windowPos = self._window.pos()  # Update the stored window position

    def leaveEvent(self, event):
        """
        Placeholder for handling mouse leave events.
        """
        print("=== leaveEvent ===")

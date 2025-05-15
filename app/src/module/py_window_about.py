# Import necessary modules
from src.module.py_window_main import *
# from src.module.py_window_main import WIDTH, HEIGHT

# Import resources for the application
from src.resource.resources_rc import *



##########################################################################
class AboutWindow(QMainWindow):
    '''
    AboutWindow class to display the information about the software.
    This class inherits from QMainWindow and sets up the UI components
    '''

    def __init__(self):
        QMainWindow.__init__(self)

        # WIDTH = 1920
        # HEIGHT = 1080
        # Set window properties: frameless, centered, fixed size
        self.setWindowFlags(Qt.Window | Qt.WindowType.FramelessWindowHint | Qt.WindowType.NoDropShadowWindowHint | Qt.WindowType.WindowStaysOnTopHint) # type: ignore
        self.setGeometry(int((WIDTH-475)/2),int((HEIGHT-338-150)/2), 475, 338)
        self.setFixedSize(475, 338)

        # Main vertical layout for the about window
        self.vboxMain = QVBoxLayout()
        self.vboxMain.setContentsMargins(0, 0, 0, 0)

        # Main container for the about window
        AboutWindow.labelTitle5 = QLabel()
        self.labelTitle5.setText('CubeOCR : About')
        self.labelTitle5.setObjectName('lblTitle5')
        self.labelTitle5.setGeometry(0, 0, 475, 28)
        self.labelTitle5.setFixedHeight(28)

        # Title bar for the about window
        self.titleBar = WindowDragger(self,self.labelTitle5)
        self.titleBar.setGeometry(0, 0, 475, 28)
        self.titleBar.setSizePolicy(QSizePolicy(QSizePolicy.Preferred,QSizePolicy.Fixed))

        # About container
        AboutWindow.containerContent5 = QWidget()
        self.containerContent5.setObjectName('containerContent5')

        # Add title bar and content container to the main layout
        self.vboxMain.addWidget(self.labelTitle5)
        self.vboxMain.addSpacing(0)
        self.vboxMain.addWidget(self.containerContent5)
        self.vboxMain.setSpacing(0)

        # Set the main layout to the central widget
        AboutWindow.container5 = QWidget()
        self.container5.setObjectName('ctn5')
        self.container5.setLayout(self.vboxMain)
        self.setCentralWidget(self.container5)

        # Get system information
        self.getSystemInfo()

        # Add a logo to the about window
        self.pixmap = QPixmap(":/resources/image/logo1.png")
        self.labelpic = QLabel(self.containerContent5)
        self.labelpic.setPixmap(self.pixmap)
        self.labelpic.resize(self.pixmap.width(), self.pixmap.height())

        # Add a horizontal line as a separator
        self.line = QFrame(self.containerContent5)
        self.line.setGeometry(QRect(10, 88, 457, 5))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        # self.line.setFrameShadow(QFrame.Raised )
        self.line.setLineWidth(3)

        # Label for the software description
        self.label1a = QLabel(self.containerContent5)
        self.label1a.setGeometry(15, 100, 450, 30)
        self.label1a.setText("CubeOCR is a free OCR software tool developed by OCR-tech.")

        # Label for the license information
        self.label2 = QLabel(self.containerContent5)
        self.label2.setGeometry(15, 125, 450, 30)
        self.label2.setText("This software is licensed under the MIT License.")

        # Label for the email
        self.label1a = QLabel(self.containerContent5)
        self.label1a.setGeometry(15, 150, 450, 30)
        self.label1a.setText("Email : ")

        # Add a hyperlink label for the email
        self.labellink1a = QLabel(self.containerContent5)
        self.labellink1a.setObjectName('labellink1a')
        self.labellink1a.setOpenExternalLinks(True)
        self.labellink1a.setGeometry(120, 150, 400, 30)
        # self.labellink1a.setText('<a href="mailto:ocrtech.mail@gmail.com">ocrtech.mail@gmail.com</a>')
        self.labellink1a.setText('ocrtech.mail@gmail.com')

        # Label for the website
        self.label1b = QLabel(self.containerContent5)
        self.label1b.setGeometry(15, 200, 450, 30)
        self.label1b.setText("Website : ")

        # Add a hyperlink label for the website
        self.labellink1b = QLabel(self.containerContent5)
        self.labellink1b.setObjectName('labellink1b')
        self.labellink1b.setOpenExternalLinks(True)
        self.labellink1b.setGeometry(120, 200, 400, 30)
        self.labellink1b.setText('<a href="https://ocr-tech.github.io/CubeOCR/index.html">https://ocr-tech.github.io/CubeOCR/index.html</a>')

        # Label for the gitHub repository
        self.label1c = QLabel(self.containerContent5)
        self.label1c.setGeometry(15, 175, 450, 30)
        self.label1c.setText("GitHub : ")

        # Add a hyperlink label for the gitHub repository
        self.labellink1c = QLabel(self.containerContent5)
        self.labellink1c.setObjectName('labellink1c')
        self.labellink1c.setOpenExternalLinks(True)
        self.labellink1c.setGeometry(120, 175, 400, 30)
        self.labellink1c.setText('<a href="https://github.com/OCR-tech/CubeOCR">https://github.com/OCR-tech/CubeOCR</a>')

        # Lable for the sofware version
        self.label7 = QLabel(self.containerContent5)
        self.label7.setGeometry(15, 225, 400, 30)
        self.label7.setText("Software Version : ")

        self.label7a = QLabel(self.containerContent5)
        self.label7a.setGeometry(120, 225, 400, 30)
        self.label7a.setText(VERSION_SW)

        # Label for the license type
        self.label9 = QLabel(self.containerContent5)
        self.label9.setGeometry(15, 250, 400, 30)
        self.label9.setText("License Type : ")

        self.label9a = QLabel(self.containerContent5)
        self.label9a.setGeometry(120, 250, 400, 30)
        self.label9a.setText(TYPE_LC)

        # Add a footer label for copyright information
        self.label14 = QLabel(self.containerContent5)
        self.label14.setText("© 2025 OCR-tech")
        self.label14.setGeometry(15, 275, 400, 30)
        # self.label14.setAlignment(Qt.AlignLeft)
        self.label14.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Add an OK button to close the about window
        self.okButton = QPushButton(self.containerContent5)
        self.okButton.setText("OK")
        self.okButton.setGeometry(375, 265, 85, 30)
        self.okButton.clicked.connect(self.okAbout)

        # Set the stylesheet for the about window based on the theme
        from src.module.py_window_main import MainGuiWindow
        from src.func.py_main_editor import TextGuiWindow

        if MainGuiWindow.THEME == "light":
            TextGuiWindow.set_LightTheme(self)
        elif MainGuiWindow.THEME == "dark":
            TextGuiWindow.set_DarkTheme(self)
        TextGuiWindow.read_StyleSheet(self)

    # //===================================================//
    def okAbout(self):
        """
        Handles the 'OK' button click event to close the About window.
        """
        from src.module.py_window_main import MainGuiWindow
        from src.module.py_window_setting import SettingWindow
        print('=== okAbout ===')
        # Re-enable the 'About' action in the main window
        MainGuiWindow.aboutAction.setEnabled(True)
        # Re-enable the 'Settings' action in the main window
        try:
            SettingWindow.btnAbout.setEnabled(True)
        except:
            pass
        self.close()

    # //===================================================//
    def getSystemInfo(self):
        """
        Retrieves and sets system information.
        """
        global VERSION_SW, TYPE_LC
        print('=== getSystemInfo ===')
        # Set the software version and type of license
        VERSION_SW = '1.0'
        TYPE_LC = 'MIT License'

    # //===================================================//
    def paintEvent(self, event):
        """
        Handles the paint event to set the background color and border style.
        """
        painter = QPainter(self)
        self.setBackgroundColor(painter)
        self.setBorderStyle()

    # //===================================================//
    def setBackgroundColor(self,painter):
        """
        Sets the background color of the window based on the selected theme.
        """

        from src.module.py_window_main import MainGuiWindow
        print('=== setBackgroundColor ===')
        if MainGuiWindow.THEME == "light":
            if (MainGuiWindow.ThemeLightColorVar1 == 6):
                # Use custom light theme color
                painter.setBrush(QColor(MainGuiWindow.BG_COLOR_LIGHT_CUSTOM))
                painter.setPen(QPen(QColor(MainGuiWindow.BG_COLOR_LIGHT_CUSTOM)))
            else:
                # Default light theme color
                painter.setBrush(QColor(Qt.GlobalColor.white))
                painter.setPen(QPen(QColor(Qt.GlobalColor.white)))

        if MainGuiWindow.THEME == "dark":
            if (MainGuiWindow.ThemeDarkColorVar1 == 6):
                # Use custom dark theme color
                painter.setBrush(QColor(MainGuiWindow.BG_COLOR_DARK_CUSTOM))
                painter.setPen(QPen(QColor(MainGuiWindow.BG_COLOR_DARK_CUSTOM)))
            else:
                # Default dark theme color
                painter.setBrush(QColor(50, 50, 50))
                painter.setPen(QPen(QColor(50, 50, 50)))
        painter.setOpacity(1)
        painter.drawRect(self.rect())

    # //===========================================//
    def setBorderStyle(self):
        """
        Sets the border style of the window based on the configuration.
        """
        from src.module.py_window_main import MainGuiWindow

        print('=== setBorderStyle ===')
        if (MainGuiWindow.BorderStyleVar1 == 0):
            radius = 0
        elif (MainGuiWindow.BorderStyleVar1 == 1):
            radius = 5

        # Create a rounded rectangle path for the border
        path = QPainterPath()
        rect = QRectF(self.rect()).adjusted(0.5, 0.5, -0.5, -0.5)
        path.addRoundedRect(rect, radius, radius)

        # Apply the mask to the window to enforce the border style
        region = QRegion(path.toFillPolygon(QTransform()).toPolygon())
        self.setMask(region)

    #//==========================================================//
    def keyPressEvent(self, event):
        """
        Handles key press events. Closes the about window when the Escape key is pressed.
        """
        print('=== keyPressEvent ===')
        if (event.key() == Qt.Key.Key_Escape):  # Key Esc
            print('=== Esc ===')
            self.okAbout()



########################################################################
class WindowDragger(QWidget):
    '''
    WindowDragger class to handle the dragging of the window.
    '''
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
        w1 = 475            # Window width
        h1 = 338            # Window height

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
                    self._window.move(0, 0)
                elif ((y0Pos+h1) > HEIGHT):
                    self._window.move(0, HEIGHT-h1)
                else:
                    self._window.move(0, y0Pos)

            elif (y0Pos < 0):
                print('=== limit 2 ===')
                if (x0Pos < 0):
                    self._window.move(0, 0)
                elif ((x0Pos+w1) > WIDTH):
                    self._window.move(WIDTH-w1, 0)
                else:
                    self._window.move(x0Pos, 0)

            elif ((x0Pos+w1) > WIDTH):
                print('=== limit 3 ===')
                if (y0Pos < 0):
                    self._window.move(WIDTH-w1, 0)
                elif ((y0Pos+h1) > HEIGHT):
                    self._window.move(WIDTH-w1, HEIGHT-h1)
                else:
                    self._window.move(WIDTH-w1, y0Pos)

            elif ((y0Pos+h1) > HEIGHT):
                print('=== limit 4 ===')
                if (x0Pos < 0):
                    self._window.move(0, HEIGHT-h1)
                elif ((x0Pos+w1) > WIDTH):
                    self._window.move(WIDTH-w1, HEIGHT-h1)
                else:
                    self._window.move(x0Pos, HEIGHT-h1)
            else:
                self._window.move(x0Pos, y0Pos)

    def mouseReleaseEvent(self, event):
        """
        Resets the mouse press state on mouse release.
        """
        print("=== mouseReleaseEvent ===")

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
        self._windowPos = self._window.pos()

    def leaveEvent(self, event):
        """
        Placeholder for handling mouse leave events.
        """
        print("=== leaveEvent ===")

# Import necessary modules and constants from py_main_gui
from src.module.py_window_main import *
# from src.module.py_window_main import WIDTH, HEIGHT  # Import screen width and height constants

# Import resources for the application
from src.resource.resources_rc import *


##########################################################################
class HelpWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)

        # WIDTH = 1920
        # HEIGHT = 1080
        # Set window properties: frameless, centered, fixed size
        self.setWindowFlags(Qt.Window | Qt.WindowType.FramelessWindowHint | Qt.WindowType.NoDropShadowWindowHint | Qt.WindowType.WindowStaysOnTopHint) # type: ignore
        self.setGeometry(int((WIDTH-933)/2),int((HEIGHT-678-150)/2),933,678)
        self.setFixedSize(933,678)

        # Main vertical layout for the help window
        self.vboxMain = QVBoxLayout()
        self.vboxMain.setContentsMargins(0,0,0,0)

        # Title bar setup
        HelpWindow.labelTitle6 = QLabel()
        self.labelTitle6.setText('CubeOCR : Help')
        self.labelTitle6.setObjectName('lblTitle6')
        self.labelTitle6.setGeometry(0,0,933,28)
        self.labelTitle6.setFixedHeight(28)

        # Draggable title bar
        self.titleBar = WindowDragger(self,self.labelTitle6)
        self.titleBar.setGeometry(0,0,933,28)
        self.titleBar.setSizePolicy(QSizePolicy(QSizePolicy.Preferred,QSizePolicy.Fixed))

        # Content container
        HelpWindow.containerContent6 = QWidget()
        self.containerContent6.setObjectName('containerContent6')

        # Add title bar and content container to the main layout
        self.vboxMain.addWidget(self.labelTitle6)
        self.vboxMain.addSpacing(0)
        self.vboxMain.addWidget(self.containerContent6)
        self.vboxMain.setSpacing(0)

        # Form layout for the help content
        self.formLayout =QFormLayout()
        self.formLayout.setContentsMargins(0,0,0,0)
        self.formLayout.setSpacing(0)
        self.groupBox = QGroupBox()
        self.groupBox.setLayout(self.formLayout)

        # Top label for the help window
        self.labeltop = QLabel()
        self.labeltop.setObjectName('labeltop')
        self.labeltop.setFixedHeight(100)
        self.labeltop.setGeometry(0,0,933,28)

        # Scroll area for the help content
        self.scroll = QScrollArea()
        self.scroll.setWidget(self.groupBox)
        self.scroll.setWidgetResizable(True)

        # Bottom label for the help window
        self.labelbottom = QLabel()
        self.labelbottom.setObjectName('labelbottom')
        self.labelbottom.setFixedHeight(60)
        self.labelbottom.setGeometry(0,0,933,28)

        # Layout for the content container
        self.mainLayout = QVBoxLayout(self.containerContent6)
        self.mainLayout.setContentsMargins(0,0,0,0)
        self.mainLayout.addWidget(self.labeltop)
        self.mainLayout.setSpacing(0)
        self.mainLayout.addWidget(self.scroll)
        self.mainLayout.setSpacing(0)
        self.mainLayout.addWidget(self.labelbottom)

        # Add logo and separator line to the top label
        self.pixmap = QPixmap(":/resources/image/logo1.png")
        self.labelpic = QLabel(self.labeltop)
        self.labelpic.setPixmap(self.pixmap)
        self.labelpic.resize(self.pixmap.width(),self.pixmap.height())

        self.line = QFrame(self.labeltop)
        self.line.setGeometry(QRect(10,88,913,5))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setLineWidth(3)

        # Add help content labels
        self.label2 = QLabel()
        self.label2.setObjectName('lbl2h')
        self.label2.setGeometry(0,0,400,30)
        self.label2.setText("How to Use :")

        self.label3 = QLabel()
        self.label3.setGeometry(0,0,400,30)
        self.label3.setText('<p style="font-size: 13px; line-height: 25px; margin-left: 15px"> \
                            1. &nbsp;&nbsp; Launch the program. System tray icon will appear at the bottom-right of the screen.<br> \
                            2. &nbsp;&nbsp; Click on system tray icon or Use keyboard shortcut <b>"Ctrl+Alt"</b> or <b>"Ctrl+Windows"</b> to activate OCR screen.<br> \
                            3. &nbsp;&nbsp; Select text area on the computer screen (click at the top-left corner, drag to the bottom-right corner, and release the mouse).<br> \
                            4. &nbsp;&nbsp; Program will perform OCR conversion automatically. When finished, text editor will pop-up with fully editable text.<br> \
                            5. &nbsp;&nbsp; Verify the result, and edit text with built-in toolbar if neccessary.<br> \
                            6. &nbsp;&nbsp; Click <b>"OK"</b> button to finish or Click <b>"Continue"</b> button to proceed the next selection.<br> \
                            7. &nbsp;&nbsp; Program will automatically copy all the results to clipboard by defaults.<br> \
                            8. &nbsp;&nbsp; Paste to other text editors or appropriate applications for your requirements.<br> \
                            </p>')

        self.label4 = QLabel()
        self.label4.setObjectName('lbl4h')
        self.label4.setGeometry(0,0,400,30)
        self.label4.setText("Keyboard Shortcuts :")

        self.label5 = QLabel()
        self.label5.setGeometry(0,0,400,30)
        self.label5.setText('<p style="font-size: 13px; line-height: 25px; margin-left: 15px"> \
                            &#8226;&nbsp;&nbsp; <b>Ctrl+Alt</b> or <b>Ctrl+Windows</b> : Activate OCR screen<br> \
                            &#8226;&nbsp;&nbsp; <b>Right-click</b> : Deactivate OCR screen <br> \
                            &#8226;&nbsp;&nbsp; <b>Double-click</b> : Show Setting window <br> \
                            &#8226;&nbsp;&nbsp; <b>Ctrl+Q</b> : Exit program  <br> \
                            &#8226;&nbsp;&nbsp; <b>Esc</b> : Close window <br> \
                            </p>')

        self.label14 = QLabel()
        self.label14.setObjectName('lbl14h')
        self.label14.setGeometry(0,0,400,30)
        self.label14.setText("Shortcuts for Text Editor :")

        self.label15 = QLabel()
        self.label15.setGeometry(0,0,400,30)
        self.label15.setText('<p style="font-size: 13px; line-height: 25px; margin-left: 15px"> \
                            &#8226;&nbsp;&nbsp; <b>Ctrl+T</b> : Toggle theme \
                                <span style="white-space: pre"; padding-left:500px>                                       </span> \
                            &#8226;&nbsp;&nbsp; <b>Ctrl+S</b> : Save \
                                <span style="white-space: pre"; padding-left:500px>                                       </span> \
                            &#8226;&nbsp;&nbsp; <b>Ctrl+B</b> : Bold text <br> \
                            &#8226;&nbsp;&nbsp; <b>Ctrl+-</b> : Decrease text size \
                                <span style="white-space: pre">                                 </span> \
                            &#8226;&nbsp;&nbsp; <b>Ctrl+Z</b> : Undo \
                                <span style="white-space: pre"; padding-left:500px>                                       </span> \
                            &#8226;&nbsp;&nbsp; <b>Ctrl+I</b> : Italic text <br> \
                            &#8226;&nbsp;&nbsp; <b>Ctrl++</b> : Increase text size \
                                <span style="white-space: pre">                                 </span> \
                            &#8226;&nbsp;&nbsp; <b>Ctrl+Y</b> : Redo \
                                <span style="white-space: pre"; padding-left:500px>                                      </span> \
                            &#8226;&nbsp;&nbsp; <b>Ctrl+U</b> : Underline text <br> \
                            &#8226;&nbsp;&nbsp; <b>Ctrl+[</b> : Decrease opacity \
                                <span style="white-space: pre">                                   </span> \
                            &#8226;&nbsp;&nbsp; <b>Ctrl+X</b> : Cut \
                                <span style="white-space: pre"; padding-left:500px>                                        </span> \
                            &#8226;&nbsp;&nbsp; <b>Ctrl+=</b> : Subscript text <br> \
                            &#8226;&nbsp;&nbsp; <b>Ctrl+]</b> : Increase opacity \
                                <span style="white-space: pre">                                    </span> \
                            &#8226;&nbsp;&nbsp; <b>Ctrl+C</b> : Copy \
                                <span style="white-space: pre"; padding-left:500px>                                      </span> \
                            &#8226;&nbsp;&nbsp; <b>Ctrl+Shift++</b> : Superscript text <br> \
                            &#8226;&nbsp;&nbsp; <b>Ctrl+E</b> : Show Setting window \
                                <span style="white-space: pre">                            </span> \
                            &#8226;&nbsp;&nbsp; <b>Ctrl+V</b> : Paste \
                                <span style="white-space: pre">                                     </span> \
                            &#8226;&nbsp;&nbsp; <b>Ctrl+*</b> : Paragraph marks <br> \
                            &#8226;&nbsp;&nbsp; <b>Ctrl+G</b> : Show Color picker \
                                <span style="white-space: pre">                                 </span> \
                            &#8226;&nbsp;&nbsp; <b>Ctrl+A</b> : Select all <br> \
                            &#8226;&nbsp;&nbsp; <b>Ctrl+F</b> : Show Find & Replace \
                                <span style="white-space: pre">                             </span> \
                            &#8226;&nbsp;&nbsp; <b>Ctrl+P</b> : Print <br> \
                            &#8226;&nbsp;&nbsp; <b>Ctrl+W</b> : Toggle toolbar \
                                <span style="white-space: pre">                                     </span> \
                            &#8226;&nbsp;&nbsp; <b>Ctrl+H</b> : Preview <br> \
                            &#8226;&nbsp;&nbsp; <b>Ctrl+M</b> : Toggle statusbar \
                                <span style="white-space: pre">                                  </span> \
                            &#8226;&nbsp;&nbsp; <b>Del</b> : Delete <br> \
                            &#8226;&nbsp;&nbsp; <b>Ctrl+N</b> : Set text family <br> \
                            &#8226;&nbsp;&nbsp; <b>Ctrl+R</b> : Reset setting <br> \
                            </p>')

        self.label6 = QLabel()
        self.label6.setObjectName('lbl6h')
        self.label6.setGeometry(0,0,400,30)
        self.label6.setText("General Features :")

        self.label7 = QLabel()
        self.label7.setGeometry(0,0,400,30)
        self.label7.setText('<p style="font-size: 13px; line-height: 25px; margin-left: 15px"> \
                            &#8226;&nbsp;&nbsp; Extract any text on computer screen<br> \
                            &#8226;&nbsp;&nbsp; Fast and accurate text recognition<br> \
                            &#8226;&nbsp;&nbsp; Instant text editing with built-in toolbar<br> \
                            &#8226;&nbsp;&nbsp; Easily copy & paste  to other applications <br> \
                            &#8226;&nbsp;&nbsp; Activate OCR screen with hotkeys<br> \
                            </p>')

        # Add labels to the form layout
        self.formLayout.addRow(self.label2)
        self.formLayout.addRow(self.label3)
        self.formLayout.addRow(self.label4)
        self.formLayout.addRow(self.label5)
        self.formLayout.addRow(self.label14)
        self.formLayout.addRow(self.label15)
        self.formLayout.addRow(self.label6)
        self.formLayout.addRow(self.label7)

        # Add "OK" button to the bottom label
        self.okButton = QPushButton(self.labelbottom)
        self.okButton.setText("OK")
        self.okButton.setGeometry(835,15,85,30)
        self.okButton.clicked.connect(self.okHelp)

        # Set the central widget with the main layout
        HelpWindow.container6 = QWidget()
        self.container6.setObjectName('ctn6')
        self.container6.setLayout(self.vboxMain)
        self.setCentralWidget(self.container6)

        # Apply theme based on user settings
        from src.module.py_window_main import MainGuiWindow
        from src.func.py_main_editor import TextGuiWindow

        if MainGuiWindow.THEME == "light":
            TextGuiWindow.set_LightTheme(self)
        elif MainGuiWindow.THEME == "dark":
            TextGuiWindow.set_DarkTheme(self)
        TextGuiWindow.read_StyleSheet(self)

    #//=======================================================//
    def okHelp(self):
        """
        Handles the "OK" button click event. Closes the help window.
        """
        print('=== okHelp ===')
        from src.module.py_window_main import MainGuiWindow
        MainGuiWindow.helpAction.setEnabled(True)

        from src.module.py_window_setting import SettingWindow
        try:
            SettingWindow.btnHelp.setEnabled(True)
        except:
            pass

        self.close()

    # //===================================================//
    def paintEvent(self, event=None):
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
                painter.setBrush(QColor(50,50,50))
                painter.setPen(QPen(QColor(50,50,50)))

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
        Handles key press events. Closes the help window when the Escape key is pressed.
        """
        print('=== keyPressEvent ===')
        if (event.key() == Qt.Key.Key_Escape):      # Check if the pressed key is Escape
            print('=== Esc ===')
            self.okHelp()

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
        w1 = 933        # Window width
        h1 = 678        # Window height

        # Enforce horizontal boundary
        if (QCursor.pos().x() >= (WIDTH-50)):
            print("=== limited ===")
            QCursor.setPos(WIDTH-50,QCursor.pos().y())

        # Enforce vertical boundary
        if (QCursor.pos().y() >= (HEIGHT-50)):
            print("=== limited ===")
            QCursor().setPos(QCursor.pos().x(),HEIGHT-50)

        # Calculate new window position
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

            elif ((y0Pos+h1+20) > HEIGHT):
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

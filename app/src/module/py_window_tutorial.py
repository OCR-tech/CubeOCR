# Import necessary modules and constants from py_main_gui
from src.module.py_window_main import *

# Import resources for the application
from src.resource.resources_rc import *



##########################################################################
class TutorialWindow(QMainWindow):
    """
    Tutorial Window class for displaying the tutorial information.
    Inherits from QMainWindow and sets up the UI components and layout.
    """

    def __init__(self):
        QMainWindow.__init__(self)

        # Set window properties: frameless, centered, fixed size
        # self.setWindowFlags(Qt.WindowFlags.Window | Qt.WindowType.FramelessWindowHint | Qt.WindowType.NoDropShadowWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        self.setWindowFlags(Qt.Window | Qt.WindowType.FramelessWindowHint | Qt.WindowType.NoDropShadowWindowHint | Qt.WindowType.WindowStaysOnTopHint) # type: ignore
        self.setGeometry(int((WIDTH-753)/2),int((HEIGHT-878-50)/2),753,878)
        self.setFixedSize(753,878)

        # Main vertical layout for the tutorial window
        self.vboxMain = QVBoxLayout()
        self.vboxMain.setContentsMargins(0,0,0,0)

        # Title bar setup
        TutorialWindow.labelTitle8 = QLabel()
        self.labelTitle8.setText('CubeOCR : Tutorial')
        self.labelTitle8.setObjectName('lblTitle8')
        self.labelTitle8.setGeometry(0,0,753,28)
        self.labelTitle8.setFixedHeight(28)

        # Draggable title bar
        self.titleBar = WindowDragger(self,self.labelTitle8)
        self.titleBar.setGeometry(0,0,753,28)
        self.titleBar.setSizePolicy(QSizePolicy(QSizePolicy.Preferred,QSizePolicy.Fixed))

        # Content container
        TutorialWindow.containerContent8 = QWidget()
        self.containerContent8.setObjectName('containerContent8')

        # Add title bar and content container to the main layout
        self.vboxMain.addWidget(self.labelTitle8)
        self.vboxMain.addSpacing(0)
        self.vboxMain.addWidget(self.containerContent8)
        self.vboxMain.setSpacing(0)

        # Form layouts for different sections of the tutorial
        self.formLayout1 =QFormLayout()
        self.formLayout1.setContentsMargins(0,0,0,0)
        self.formLayout1.setSpacing(0)
        self.formLayout2 =QFormLayout()
        self.formLayout2.setContentsMargins(0,0,0,0)
        self.formLayout2.setSpacing(0)
        self.formLayout3 =QFormLayout()
        self.formLayout3.setContentsMargins(0,0,0,0)
        self.formLayout3.setSpacing(0)
        self.formLayout4 =QFormLayout()
        self.formLayout4.setContentsMargins(0,0,0,0)
        self.formLayout4.setSpacing(0)
        self.formLayout5 =QFormLayout()
        self.formLayout5.setContentsMargins(0,0,0,0)
        self.formLayout5.setSpacing(0)

        # Group boxes for each tutorial section
        self.groupBox1 = QGroupBox()
        self.groupBox1.setLayout(self.formLayout1)
        self.groupBox2 = QGroupBox()
        self.groupBox2.setLayout(self.formLayout2)
        self.groupBox3 = QGroupBox()
        self.groupBox3.setLayout(self.formLayout3)
        self.groupBox4 = QGroupBox()
        self.groupBox4.setLayout(self.formLayout4)
        self.groupBox5 = QGroupBox()
        self.groupBox5.setLayout(self.formLayout5)

        # Top label for the tutorial window
        self.labeltop = QLabel()
        self.labeltop.setObjectName('labeltop')
        self.labeltop.setFixedHeight(125)
        self.labeltop.setGeometry(0,0,753,28)

        # Scroll areas for each tutorial section
        self.scrollArea1 = QScrollArea()
        self.scrollArea1.setWidget(self.groupBox1)
        self.scrollArea1.setWidgetResizable(True)
        self.scrollArea1.setVisible(True)
        self.scrollArea2 = QScrollArea()
        self.scrollArea2.setWidget(self.groupBox2)
        self.scrollArea2.setWidgetResizable(True)
        self.scrollArea2.setVisible(False)
        self.scrollArea3 = QScrollArea()
        self.scrollArea3.setWidget(self.groupBox3)
        self.scrollArea3.setWidgetResizable(True)
        self.scrollArea3.setVisible(False)
        self.scrollArea4 = QScrollArea()
        self.scrollArea4.setWidget(self.groupBox4)
        self.scrollArea4.setWidgetResizable(True)
        self.scrollArea4.setVisible(False)
        self.scrollArea5 = QScrollArea()
        self.scrollArea5.setWidget(self.groupBox5)
        self.scrollArea5.setWidgetResizable(True)
        self.scrollArea5.setVisible(False)

        # Bottom label for the tutorial window
        self.labelbottom = QLabel()
        self.labelbottom.setObjectName('labelbottom')
        self.labelbottom.setFixedHeight(60)
        self.labelbottom.setGeometry(0,0,770,28)

        # Layout for the content container
        self.mainLayout = QVBoxLayout(self.containerContent8)
        self.mainLayout.setContentsMargins(0,0,0,0)

        # Add top label, scroll areas, and bottom label to the layout
        self.mainLayout.addWidget(self.labeltop)
        self.mainLayout.setSpacing(0)
        self.mainLayout.addWidget(self.scrollArea1)
        self.mainLayout.addWidget(self.scrollArea2)
        self.mainLayout.addWidget(self.scrollArea3)
        self.mainLayout.addWidget(self.scrollArea4)
        self.mainLayout.addWidget(self.scrollArea5)
        self.mainLayout.setSpacing(0)
        self.mainLayout.addWidget(self.labelbottom)

        # //================================================//
        # // labeltop
        # //================================================//
        # Add logo and separator line to the top label
        self.pixmap = QPixmap(":/resources/image/logo1.png")
        self.labelpic = QLabel(self.labeltop)
        self.labelpic.setPixmap(self.pixmap)
        self.labelpic.resize(self.pixmap.width(),self.pixmap.height())
        self.line = QFrame(self.labeltop)
        self.line.setGeometry(QRect(10,88,733,5))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setLineWidth(3)

        # Buttons for navigating tutorial sections
        self.generalButton = QPushButton(self.labeltop)
        self.generalButton.setObjectName("btn81")
        self.generalButton.setText("General")
        self.generalButton.setGeometry(10,98,135,25)
        self.generalButton.clicked.connect(self.generalButtonFcn)

        self.layoutButton = QPushButton(self.labeltop)
        self.layoutButton.setObjectName("btn82")
        self.layoutButton.setText("Page Layout")
        self.layoutButton.setGeometry(147,98,135,25)
        self.layoutButton.clicked.connect(self.layoutButtonFcn)

        self.image1Button = QPushButton(self.labeltop)
        self.image1Button.setObjectName("btn83")
        self.image1Button.setText("Image Enhancement")
        self.image1Button.setGeometry(284,98,135,25)
        self.image1Button.clicked.connect(self.image1ButtonFcn)

        self.image2Button = QPushButton(self.labeltop)
        self.image2Button.setObjectName("btn84")
        self.image2Button.setText("Image Filtering")
        self.image2Button.setGeometry(421,98,135,25)
        self.image2Button.clicked.connect(self.image2ButtonFcn)

        self.recognitionButton = QPushButton(self.labeltop)
        self.recognitionButton.setObjectName("btn85")
        self.recognitionButton.setText("Recognition")
        self.recognitionButton.setGeometry(558,98,135,25)
        self.recognitionButton.clicked.connect(self.recognitionButtonFcn)

        # //================================================//
        # // General //
        # //================================================//
        # Add a label for the general section
        self.label1 = QLabel()
        self.label1.setObjectName("lbl1t")
        self.label1.setGeometry(0,0,400,30)
        self.label1.setText("How to Use :")

        self.label1a = QLabel()
        self.label1a.setObjectName("lbl1at")
        self.label1a.setGeometry(0,0,400,30)
        self.label1a.setText("OCR Setting")

        self.label1b = QLabel()
        self.label1b.setGeometry(0,0,400,30)
        self.label1b.setText('<p style="font-size: 13px; line-height: 25px; margin-left: 15px"> \
                            &#8226;&nbsp;&nbsp; <b> Languages : </b> select for OCR languages <br> \
                            &#8226;&nbsp;&nbsp; <b> System Language : </b> select for system locale default language <br> \
                            &#8226;&nbsp;&nbsp; <b> Math & Equation : </b> select for math and equations for OCR detection \
                            </p>')

        self.label1c = QLabel()
        self.label1c.setObjectName("lbl1ct")
        self.label1c.setGeometry(0,0,400,30)
        self.label1c.setText("Text Layout")

        self.label1d = QLabel()
        self.label1d.setGeometry(0,0,400,30)
        self.label1d.setText('<p style="font-size: 13px; line-height: 25px; margin-left: 15px"> \
                            &#8226;&nbsp;&nbsp; <b> Auto : </b> select for detection text layout automatically <br> \
                            &#8226;&nbsp;&nbsp; <b> Single Character : </b> select for only single character <br> \
                            &#8226;&nbsp;&nbsp; <b> Single Word : </b> select for only single word character<br> \
                            &#8226;&nbsp;&nbsp; <b> Single Line : </b> select for only single line character<br> \
                            &#8226;&nbsp;&nbsp; <b> Sparse Text : </b> select for spread or distributed text layout<br> \
                            &#8226;&nbsp;&nbsp; <b> Vertical Text : </b> select for vertical text layout <br> \
                            &#8226;&nbsp;&nbsp; <b> Single Column : </b> select for single column layout <br> \
                            &#8226;&nbsp;&nbsp; <b> Multiple Column : </b> select for multiple columns layout \
                            </p>')

        self.label1e = QLabel()
        self.label1e.setObjectName("lbl1et")
        self.label1e.setGeometry(0,0,400,30)
        self.label1e.setText("Detected Text")

        self.label1f = QLabel()
        self.label1f.setGeometry(0,0,400,30)
        self.label1f.setText('<p style="font-size: 13px; line-height: 25px; margin-left: 15px"> \
                            &#8226;&nbsp;&nbsp; <b> Select All : </b> select for all detected text options <br> \
                            &#8226;&nbsp;&nbsp; <b> Custom : </b> select for customized detected text options <br> \
                            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&#8226;&nbsp;&nbsp; <b> Lower Cases : </b> select for lower cases letters (a to z) <br> \
                            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&#8226;&nbsp;&nbsp; <b> Upper Cases : </b> select for upper cases letters (A to Z) <br> \
                            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&#8226;&nbsp;&nbsp; <b> Letters : </b> select for alphabet letters of OCR languages <br> \
                            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&#8226;&nbsp;&nbsp; <b> Numbers : </b> select for digit numbers (0 to 9) <br> \
                            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&#8226;&nbsp;&nbsp; <b> Punctuation : </b> select for punctuation <br> \
                            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&#8226;&nbsp;&nbsp; <b> Special Characters : </b> select for special characters \
                            </p>')

        self.label1g = QLabel()
        self.label1g.setObjectName("lbl1gt")
        self.label1g.setGeometry(0,0,400,30)
        self.label1g.setText("Output Save as")

        self.label1h = QLabel()
        self.label1h.setGeometry(0,0,400,30)
        self.label1h.setText('<p style="font-size: 13px; line-height: 25px; margin-left: 15px"> \
                            &#8226;&nbsp;&nbsp; <b> Text : </b> select for plain text or rich text format (.txt, .rtf, .odt, .doc, .docx) <br> \
                            &#8226;&nbsp;&nbsp; <b> PDF : </b> select for PDF format (.pdf) <br> \
                            &#8226;&nbsp;&nbsp; <b> Spreadsheet : </b> select for spreadsheet format (.xlsx, .xls, .csv, .ods) \
                            </p>')

        self.label1i = QLabel()
        self.label1i.setObjectName("lbl1gt")
        self.label1i.setGeometry(0,0,400,30)
        self.label1i.setText("Optimization")

        self.label1j = QLabel()
        self.label1j.setGeometry(0,0,400,30)
        self.label1j.setText('<p style="font-size: 13px; line-height: 25px; margin-left: 15px"> \
                            &#8226;&nbsp;&nbsp; <b> Standard : </b> select for standard performance of OCR optimization  <br> \
                            &#8226;&nbsp;&nbsp; <b> Speed : </b> select for high speed performance with less accuracy <br> \
                            &#8226;&nbsp;&nbsp; <b> Accuracy : </b> select for high accuracy performance with slow speed \
                            </p>')

        self.label1k = QLabel()
        self.label1k.setObjectName("lbl1kt")
        self.label1k.setGeometry(0,0,400,30)
        self.label1k.setText("OCR Languagues supported")

        self.label1l = QLabel()
        self.label1l.setStyleSheet('margin-top: 5px; margin-bottom: 5px; margin-left: 15px')
        self.label1l.setFixedWidth(650)
        self.label1l.setFixedHeight(480)

        # List of supported languages for OCR
        data_language1 = ['Afrikaans','Albanian','Amharic','Arabic','Armenian','Assamese','Azerbaijani','Basque','Belarusian','Bengali','Bosnian', \
                          'Breton','Bulgarian','Burmese','Castilian','Catalan','Cebuano','Chinese','Chinese (vertical)','Cherokee','Croatian','Czech']
        data_language2 = ['Danish','Dhivehi','Dutch','Dzongkha','Esperanto','Estonian','Faroese','Filipino','Finnish','French','Frisian',
                          'Gaelic','Galician','Georgian','German','Greek','Gujarati','Haitian','Hebrew','Hindi','Hungarian','Icelandic']
        data_language3 = ['Indonesian','Inuktitut','Irish','Italian','Japanese','Japanese (vertical)','Javanese','Kannada','Kazakh','Khmer','Korean',
                          'Kurdish','Kyrgyz','Lao','Latin','Latvian','Lithuanian','Luxembourgish','Macedonian','Malay','Malayalam','Maltese']
        data_language4 = ['Maori','Marathi','Mongolian','Nepali','Norwegian','Occitan','Oriya','Panjabi','Pashto','Persian','Polish',
                          'Portuguese','Quechua','Romanian','Russian','Sanskrit','Serbian','Sindhi','Sinhala','Slovak','Slovenian','Spanish']
        data_language5 = ['Sundanese','Swahili','Swedish','Syriac','Tajik','Tamil','Tatar','Telugu','Thai','Tibetan','Tigrinya',
                          'Tonga','Turkish','Ukrainian','Urdu','Uyghur','Uzbek','Vietnamese','Welsh','Yiddish','Yoruba','-']

        from src.module.py_window_main import MainGuiWindow

        # Create a table widget to display supported languages
        self.table1 = QTableWidget(self.label1l)
        self.table1.setObjectName('tb1')
        self.table1.setFixedWidth(642)
        self.table1.setFixedHeight(474)
        self.table1.setColumnCount(5)
        self.table1.setColumnWidth(0,125)
        self.table1.setColumnWidth(1,125)
        self.table1.setColumnWidth(2,125)
        self.table1.setColumnWidth(3,125)
        self.table1.setColumnWidth(4,125)

        # self.table1.horizontalHeader().hide()
        # self.table1.verticalHeader().hide()
        header1 = self.table1.horizontalHeader()
        if header1 is not None:
            header1.hide()
        else:
            print("Error: horizontalHeader() returned None.")

        header2 = self.table1.verticalHeader()
        if header2 is not None:
            header2.hide()
        else:
            print("Error: verticalHeader() returned None.")

        self.table1.setRowCount(22)
        self.table1.setColumnCount(5)
        self.table1.setDisabled(True)
        row1 = 0
        row2 = 0
        row3 = 0
        row4 = 0
        row5 = 0

        # Set the table items for each language
        for i in data_language1:
            self.table1.setItem(row1, 0, QTableWidgetItem(str(i)))
            self.table1.setRowHeight(row1,21)
            row1 += 1

        for i in data_language2:
            self.table1.setItem(row2, 1, QTableWidgetItem(str(i)))
            row2 += 1

        for i in data_language3:
            self.table1.setItem(row3, 2, QTableWidgetItem(str(i)))
            self.table1.setRowHeight(row3,21)
            row3 += 1

        for i in data_language4:
            self.table1.setItem(row4, 3, QTableWidgetItem(str(i)))
            row4 += 1

        for i in data_language5:
            self.table1.setItem(row5, 4, QTableWidgetItem(str(i)))
            row5 += 1

        # //================================================//
        # // Page Layout //
        # //================================================//
        # Add a label for the page layout section
        self.label2 = QLabel()
        self.label2.setObjectName("lbl2t")
        self.label2.setGeometry(0,0,400,30)
        self.label2.setText("How to Use :")

        self.label2s = QLabel()
        self.label2s.setObjectName("lbl2st")
        self.label2s.setGeometry(0,0,400,30)
        self.label2s.setText("Page Layout")

        self.label2a = QLabel()
        self.label2a.setObjectName("lbl2at")
        self.label2a.setGeometry(0,0,400,30)
        self.label2a.setText("2.1) Auto-Rotate Page :")

        self.label2b = QLabel()
        self.label2b.setObjectName("lbl2bt")
        self.label2b.setGeometry(0,0,400,30)
        self.label2b.setText("2.2) Auto-Deskew :")

        self.label2c = QLabel()
        self.label2c.setObjectName("lbl2ct")
        self.label2c.setGeometry(0,0,400,30)
        self.label2c.setText("2.3) Decolumnize :")

        self.label2d = QLabel()
        self.label2d.setObjectName("lbl2dt")
        self.label2d.setGeometry(0,0,400,30)
        self.label2d.setText("2.4) Remove Tables :")

        self.label2e = QLabel()
        self.label2e.setObjectName("lbl2et")
        self.label2e.setGeometry(0,0,400,30)
        self.label2e.setText("2.5) Remove Watermarks :")

        self.label2f = QLabel()
        self.label2f.setObjectName("lbl2ft")
        self.label2f.setGeometry(0,0,400,30)
        self.label2f.setText("2.6) Remove Underlines :")

        self.label2g = QLabel()
        self.label2g.setObjectName("lbl2gt")
        self.label2g.setGeometry(0,0,400,30)
        self.label2g.setText("2.7) Remove Extra Spaces :")

        self.label2h = QLabel()
        self.label2h.setObjectName("lbl2ht")
        self.label2h.setGeometry(0,0,400,30)
        self.label2h.setText("2.8) Remove Empty Lines :")

        # //================================================//
        # // Image Enhancement //
        # //================================================//
        # Add a label for the image enhancement section
        self.label3 = QLabel()
        self.label3.setObjectName("lbl3t")
        self.label3.setGeometry(0,0,400,30)
        self.label3.setText("How to Use :")

        self.label3s = QLabel()
        self.label3s.setObjectName("lbl3st")
        self.label3s.setGeometry(0,0,400,30)
        self.label3s.setText("Image Enhancement")

        self.label3a = QLabel()
        self.label3a.setObjectName("lbl3at")
        self.label3a.setGeometry(0,0,400,30)
        self.label3a.setText("3.1) Despeckle :")

        self.label3b = QLabel()
        self.label3b.setObjectName("lbl3bt")
        self.label3b.setGeometry(0,0,400,30)
        self.label3b.setText("3.2) Invert Color :")

        self.label3c = QLabel()
        self.label3c.setObjectName("lbl3ct")
        self.label3c.setGeometry(0,0,400,30)
        self.label3c.setText("3.3) Threshold Binary :")

        self.label3d = QLabel()
        self.label3d.setObjectName("lbl3dt")
        self.label3d.setGeometry(0,0,400,30)
        self.label3d.setText("3.4) Threshold Adaptive :")

        self.label3e = QLabel()
        self.label3e.setObjectName("lbl3et")
        self.label3e.setGeometry(0,0,400,30)
        self.label3e.setText("3.5) Sharpen :")

        self.label3f = QLabel()
        self.label3f.setObjectName("lbl3ft")
        self.label3f.setGeometry(0,0,400,30)
        self.label3f.setText("3.6) Contrast :")

        # //================================================//
        # // Image Filtering //
        # //================================================//
        # Add a label for the image filtering section
        self.label4 = QLabel()
        self.label4.setObjectName("lbl4t")
        self.label4.setGeometry(0,0,400,30)
        self.label4.setText("How to Use :")

        self.label4s = QLabel()
        self.label4s.setObjectName("lbl4st")
        self.label4s.setGeometry(0,0,400,30)
        self.label4s.setText("Image Filtering")

        self.label4a = QLabel()
        self.label4a.setObjectName("lbl4at")
        self.label4a.setGeometry(0,0,400,30)
        self.label4a.setText("4.1) Background Noise :")

        self.label4b = QLabel()
        self.label4b.setObjectName("lbl4bt")
        self.label4b.setGeometry(0,0,400,30)
        self.label4b.setText("4.2) Text Noise :")

        self.label4c = QLabel()
        self.label4c.setObjectName("lbl4ct")
        self.label4c.setGeometry(0,0,400,30)
        self.label4c.setText("4.3) Text Erosion :")

        self.label4d = QLabel()
        self.label4d.setObjectName("lbl4dt")
        self.label4d.setGeometry(0,0,400,30)
        self.label4d.setText("4.4) Text Dilation :")

        self.label4e = QLabel()
        self.label4e.setObjectName("lbl4et")
        self.label4e.setGeometry(0,0,400,30)
        self.label4e.setText("4.5) Threshold [Low & High] :")

        # //================================================//
        # // Recognition //
        # //================================================//
        # Add a label for the recognition section
        self.label5 = QLabel()
        self.label5.setObjectName("lbl5t")
        self.label5.setGeometry(0,0,400,30)
        self.label5.setText("How to Use :")

        self.label5s = QLabel()
        self.label5s.setObjectName("lbl5st")
        self.label5s.setGeometry(0,0,400,30)
        self.label5s.setText("Recognition")

        self.label5a = QLabel()
        self.label5a.setObjectName("lbl5at")
        self.label5a.setGeometry(0,0,400,30)
        self.label5a.setText("5.1) Whitelist :")

        self.label5b = QLabel()
        self.label5b.setObjectName("lbl5bt")
        self.label5b.setGeometry(0,0,400,30)
        self.label5b.setText("5.2) Blacklist :")

        self.label6s = QLabel()
        self.label6s.setObjectName("lbl6st")
        self.label6s.setGeometry(0,0,400,30)
        self.label6s.setText("Example")

        self.label6a = QLabel()
        self.label6a.setObjectName("lbl6at")
        self.label6a.setGeometry(0,0,400,30)
        self.label6a.setText("6.1) Multiple Languages :")

        self.label6b = QLabel()
        self.label6b.setObjectName("lbl6bt")
        self.label6b.setGeometry(0,0,400,30)
        self.label6b.setText("6.2) Vertical Text :")

        # //=====================================================//
        # // Page Layout //
        # //=====================================================//
        # Add images for the page layout section
        self.pixmap2a = QPixmap(":/resources/image/tutorial2a.png")
        self.label2pa = QLabel()
        self.label2pa.setPixmap(self.pixmap2a)
        self.label2pa.setStyleSheet('margin-left: 15px')
        self.label2pa.resize(self.pixmap2a.width(),self.pixmap2a.height())

        self.pixmap2b = QPixmap(":/resources/image/tutorial2b.png")
        self.label2pb = QLabel()
        self.label2pb.setPixmap(self.pixmap2b)
        self.label2pb.setStyleSheet('margin-left: 15px')
        self.label2pb.resize(self.pixmap2b.width(),self.pixmap2b.height())

        self.pixmap2c = QPixmap(":/resources/image/tutorial2c.png")
        self.label2pc = QLabel()
        self.label2pc.setPixmap(self.pixmap2c)
        self.label2pc.setStyleSheet('margin-left: 15px')
        self.label2pc.resize(self.pixmap2c.width(),self.pixmap2c.height())

        self.pixmap2d = QPixmap(":/resources/image/tutorial2d.png")
        self.label2pd = QLabel()
        self.label2pd.setPixmap(self.pixmap2d)
        self.label2pd.setStyleSheet('margin-left: 15px')
        self.label2pd.resize(self.pixmap2d.width(),self.pixmap2d.height())

        self.pixmap2e = QPixmap(":/resources/image/tutorial2e.png")
        self.label2pe = QLabel()
        self.label2pe.setPixmap(self.pixmap2e)
        self.label2pe.setStyleSheet('margin-left: 15px')
        self.label2pe.resize(self.pixmap2e.width(),self.pixmap2e.height())

        self.pixmap2f = QPixmap(":/resources/image/tutorial2f.png")
        self.label2pf = QLabel()
        self.label2pf.setPixmap(self.pixmap2f)
        self.label2pf.setStyleSheet('margin-left: 15px')
        self.label2pf.resize(self.pixmap2f.width(),self.pixmap2f.height())

        self.pixmap2g = QPixmap(":/resources/image/tutorial2g.png")
        self.label2pg = QLabel()
        self.label2pg.setPixmap(self.pixmap2g)
        self.label2pg.setStyleSheet('margin-left: 15px')
        self.label2pg.resize(self.pixmap2g.width(),self.pixmap2g.height())

        self.pixmap2h = QPixmap(":/resources/image/tutorial2h.png")
        self.label2ph = QLabel()
        self.label2ph.setPixmap(self.pixmap2h)
        self.label2ph.setStyleSheet('margin-left: 15px; margin-bottom: 15px')
        self.label2ph.resize(self.pixmap2h.width(),self.pixmap2h.height())

        # //=====================================================//
        # // Image Enhancement //
        # //=====================================================//
        # Add images for the image enhancement section
        self.pixmap3a = QPixmap(":/resources/image/tutorial3a.png")
        self.label3pa = QLabel()
        self.label3pa.setPixmap(self.pixmap3a)
        self.label3pa.setStyleSheet('margin-left: 15px')
        self.label3pa.resize(self.pixmap3a.width(),self.pixmap3a.height())

        self.pixmap3b = QPixmap(":/resources/image/tutorial3b.png")
        self.label3pb = QLabel()
        self.label3pb.setPixmap(self.pixmap3b)
        self.label3pb.setStyleSheet('margin-left: 15px')
        self.label3pb.resize(self.pixmap3b.width(),self.pixmap3b.height())

        self.pixmap3c = QPixmap(":/resources/image/tutorial3c.png")
        self.label3pc = QLabel()
        self.label3pc.setPixmap(self.pixmap3c)
        self.label3pc.setStyleSheet('margin-left: 15px')
        self.label3pc.resize(self.pixmap3c.width(),self.pixmap3c.height())

        self.pixmap3d = QPixmap(":/resources/image/tutorial3d.png")
        self.label3pd = QLabel()
        self.label3pd.setPixmap(self.pixmap3d)
        self.label3pd.setStyleSheet('margin-left: 15px')
        self.label3pd.resize(self.pixmap3d.width(),self.pixmap3d.height())

        self.pixmap3e = QPixmap(":/resources/image/tutorial3e.png")
        self.label3pe = QLabel()
        self.label3pe.setPixmap(self.pixmap3e)
        self.label3pe.setStyleSheet('margin-left: 15px')
        self.label3pe.resize(self.pixmap3e.width(),self.pixmap3e.height())

        self.pixmap3f = QPixmap(":/resources/image/tutorial3f.png")
        self.label3pf = QLabel()
        self.label3pf.setPixmap(self.pixmap3f)
        self.label3pf.setStyleSheet('margin-left: 15px; margin-bottom: 15px')
        self.label3pf.resize(self.pixmap3f.width(),self.pixmap3f.height())

        # //=====================================================//
        # // Image Enhancement //
        # //=====================================================//
        # Add images for the image enhancement section
        self.pixmap4a = QPixmap(":/resources/image/tutorial4a.png")
        self.label4pa = QLabel()
        self.label4pa.setPixmap(self.pixmap4a)
        self.label4pa.setStyleSheet('margin-left: 15px')
        self.label4pa.resize(self.pixmap4a.width(),self.pixmap4a.height())

        self.pixmap4b = QPixmap(":/resources/image/tutorial4b.png")
        self.label4pb = QLabel()
        self.label4pb.setPixmap(self.pixmap4b)
        self.label4pb.setStyleSheet('margin-left: 15px')
        self.label4pb.resize(self.pixmap4b.width(),self.pixmap4b.height())

        self.pixmap4c = QPixmap(":/resources/image/tutorial4c.png")
        self.label4pc = QLabel()
        self.label4pc.setPixmap(self.pixmap4c)
        self.label4pc.setStyleSheet('margin-left: 15px')
        self.label4pc.resize(self.pixmap4c.width(),self.pixmap4c.height())

        self.pixmap4d = QPixmap(":/resources/image/tutorial4d.png")
        self.label4pd = QLabel()
        self.label4pd.setPixmap(self.pixmap4d)
        self.label4pd.setStyleSheet('margin-left: 15px')
        self.label4pd.resize(self.pixmap4d.width(),self.pixmap4d.height())

        self.pixmap4e = QPixmap(":/resources/image/tutorial4e.png")
        self.label4pe = QLabel()
        self.label4pe.setPixmap(self.pixmap4e)
        self.label4pe.setStyleSheet('margin-left: 15px; margin-bottom: 15px')
        self.label4pe.resize(self.pixmap4e.width(),self.pixmap4e.height())

        # //=====================================================//
        # // Recognition //
        # //=====================================================//
        # Add images for the recognition section
        self.pixmap5a = QPixmap(":/resources/image/tutorial5a.png")
        self.label5pa = QLabel()
        self.label5pa.setPixmap(self.pixmap5a)
        self.label5pa.setStyleSheet('margin-left: 15px')
        self.label5pa.resize(self.pixmap5a.width(),self.pixmap5a.height())

        self.pixmap5b = QPixmap(":/resources/image/tutorial5b.png")
        self.label5pb = QLabel()
        self.label5pb.setPixmap(self.pixmap5b)
        self.label5pb.setStyleSheet('margin-left: 15px')
        self.label5pb.resize(self.pixmap5b.width(),self.pixmap5b.height())

        self.pixmap6a = QPixmap(":/resources/image/tutorial6a.png")
        self.label6pa = QLabel()
        self.label6pa.setPixmap(self.pixmap6a)
        self.label6pa.setStyleSheet('margin-left: 15px')
        self.label6pa.resize(self.pixmap6a.width(),self.pixmap6a.height())

        self.pixmap6b = QPixmap(":/resources/image/tutorial6b.png")
        self.label6pb = QLabel()
        self.label6pb.setPixmap(self.pixmap6b)
        self.label6pb.setStyleSheet('margin-left: 15px; margin-bottom: 15px')
        self.label6pb.resize(self.pixmap6b.width(),self.pixmap6b.height())

        # //=====================================================//
        # // General //
        # //=====================================================//
        # Add rows for the general section
        self.formLayout1.addRow(self.label1)
        self.formLayout1.addRow(self.label1a)
        self.formLayout1.addRow(self.label1b)
        self.formLayout1.addRow(self.label1c)
        self.formLayout1.addRow(self.label1d)
        self.formLayout1.addRow(self.label1e)
        self.formLayout1.addRow(self.label1f)
        self.formLayout1.addRow(self.label1g)
        self.formLayout1.addRow(self.label1h)
        self.formLayout1.addRow(self.label1i)
        self.formLayout1.addRow(self.label1j)
        self.formLayout1.addRow(self.label1k)
        self.formLayout1.addRow(self.label1l)

        # //=====================================================//
        # // Page Layout //
        # //=====================================================//
        # Add rows for the page layout section
        self.formLayout2.addRow(self.label2)
        self.formLayout2.addRow(self.label2s)
        self.formLayout2.addRow(self.label2a)
        self.formLayout2.addRow(self.label2pa)
        self.formLayout2.addRow(self.label2b)
        self.formLayout2.addRow(self.label2pb)
        self.formLayout2.addRow(self.label2c)
        self.formLayout2.addRow(self.label2pc)
        self.formLayout2.addRow(self.label2d)
        self.formLayout2.addRow(self.label2pd)
        self.formLayout2.addRow(self.label2e)
        self.formLayout2.addRow(self.label2pe)
        self.formLayout2.addRow(self.label2f)
        self.formLayout2.addRow(self.label2pf)
        self.formLayout2.addRow(self.label2g)
        self.formLayout2.addRow(self.label2pg)
        self.formLayout2.addRow(self.label2h)
        self.formLayout2.addRow(self.label2ph)

        # //=====================================================//
        # // Image Enhancement //
        # //=====================================================//
        # Add rows for the image enhancement section
        self.formLayout3.addRow(self.label3)
        self.formLayout3.addRow(self.label3s)
        self.formLayout3.addRow(self.label3a)
        self.formLayout3.addRow(self.label3pa)
        self.formLayout3.addRow(self.label3b)
        self.formLayout3.addRow(self.label3pb)
        self.formLayout3.addRow(self.label3c)
        self.formLayout3.addRow(self.label3pc)
        self.formLayout3.addRow(self.label3d)
        self.formLayout3.addRow(self.label3pd)
        self.formLayout3.addRow(self.label3e)
        self.formLayout3.addRow(self.label3pe)
        self.formLayout3.addRow(self.label3f)
        self.formLayout3.addRow(self.label3pf)

        # //=====================================================//
        # // Image Filtering //
        # //=====================================================//
        # Add rows for the image filtering section
        self.formLayout4.addRow(self.label4)
        self.formLayout4.addRow(self.label4s)
        self.formLayout4.addRow(self.label4a)
        self.formLayout4.addRow(self.label4pa)
        self.formLayout4.addRow(self.label4b)
        self.formLayout4.addRow(self.label4pb)
        self.formLayout4.addRow(self.label4c)
        self.formLayout4.addRow(self.label4pc)
        self.formLayout4.addRow(self.label4d)
        self.formLayout4.addRow(self.label4pd)
        self.formLayout4.addRow(self.label4e)
        self.formLayout4.addRow(self.label4pe)

        # //=====================================================//
        # // Recognition //
        # //=====================================================//
        # Add rows for the recognition section
        self.formLayout5.addRow(self.label5)
        self.formLayout5.addRow(self.label5s)
        self.formLayout5.addRow(self.label5a)
        self.formLayout5.addRow(self.label5pa)
        self.formLayout5.addRow(self.label5b)
        self.formLayout5.addRow(self.label5pb)
        self.formLayout5.addRow(self.label6s)
        self.formLayout5.addRow(self.label6a)
        self.formLayout5.addRow(self.label6pa)
        self.formLayout5.addRow(self.label6b)
        self.formLayout5.addRow(self.label6pb)

        # //================================================//
        # // labelbottom
        # //================================================//
        # Add a label for the bottom section
        self.okButton = QPushButton(self.labelbottom)
        self.okButton.setText("OK")
        self.okButton.setGeometry(655,15,85,30)
        self.okButton.clicked.connect(self.okTutorial)

        # Set up the central widget with the main layout
        TutorialWindow.container8 = QWidget()
        self.container8.setObjectName('ctn8')
        self.container8.setLayout(self.vboxMain)
        self.setCentralWidget(self.container8)

        # //===================================================//
        # // set Theme
        # //===================================================//
        # Apply theme based on user settings
        from src.module.py_window_main import MainGuiWindow
        from src.func.py_main_editor import TextGuiWindow

        if MainGuiWindow.THEME == "light":
            TextGuiWindow.set_LightTheme(self)
        elif MainGuiWindow.THEME == "dark":
            TextGuiWindow.set_DarkTheme(self)

        TextGuiWindow.read_StyleSheet(self)


    # //=======================================================//
    def okTutorial(self):
        # Function to handle the "OK" button click
        print('=== okTutorial ===')
        from src.module.py_window_main import MainGuiWindow
        MainGuiWindow.helpAction.setEnabled(True)

        from src.module.py_window_setting import SettingWindow
        try:
            SettingWindow.btnTutorial.setEnabled(True)
        except:
            pass
        self.close()

    def generalButtonFcn(self):
        # Function to handle the general button click
        print('=== generalButtonFcn ===')
        self.scrollArea1.show()
        self.scrollArea2.hide()
        self.scrollArea3.hide()
        self.scrollArea4.hide()
        self.scrollArea5.hide()

    def layoutButtonFcn(self):
        # Function to handle the layout button click
        print('=== layoutButtonFcn ===')
        self.scrollArea1.hide()
        self.scrollArea2.show()
        self.scrollArea3.hide()
        self.scrollArea4.hide()
        self.scrollArea5.hide()

    def image1ButtonFcn(self):
        # Function to handle the image1 button click
        print('=== image1ButtonFcn ===')
        self.scrollArea1.hide()
        self.scrollArea2.hide()
        self.scrollArea3.show()
        self.scrollArea4.hide()
        self.scrollArea5.hide()

    def image2ButtonFcn(self):
        # Function to handle the image2 button click
        print('=== image2ButtonFcn ===')
        self.scrollArea1.hide()
        self.scrollArea2.hide()
        self.scrollArea3.hide()
        self.scrollArea4.show()
        self.scrollArea5.hide()

    def recognitionButtonFcn(self):
        # Function to handle the recognition button click
        print('=== recognitionButtonFcn ===')
        self.scrollArea1.hide()
        self.scrollArea2.hide()
        self.scrollArea3.hide()
        self.scrollArea4.hide()
        self.scrollArea5.show()

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

    # //==========================================================//
    def keyPressEvent(self, event):
        """
        Handles key press events. Closes the help window when the Escape key is pressed.
        """
        print('=== keyPressEvent ===')
        if (event.key() == Qt.Key.Key_Escape):  # Key Esc
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
        w1 = 753            # Window width
        h1 = 878            # Window height

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

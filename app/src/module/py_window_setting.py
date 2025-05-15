# Importing necessary libraries
from src.module.py_window_main import *
# from src.module.py_window_main import WIDTH, HEIGHT
# from src.module.py_window_main import x0Pos, y0Pos
from src.config.py_config import FLAG_SELECT_ALL_INIT
from src.config.py_config import FLAG_TBTHEMELIGHT, FLAG_FGTHEMELIGHT, FLAG_BGTHEMELIGHT, FLAG_FONTTHEMELIGHT, FLAG_BTTHEMELIGHT, FLAG_BDTHEMELIGHT
from src.config.py_config import FLAG_TBTHEMEDARK, FLAG_FGTHEMEDARK, FLAG_BGTHEMEDARK, FLAG_FONTTHEMEDARK, FLAG_BTTHEMEDARK, FLAG_BDTHEMEDARK




########################################################################
class SettingWindow(QWidget):
    """
    SettingWindow class is a QWidget that represents the settings window of the application.
    It contains various settings options for the user to configure the application.
    """
    def __init__(self):
        '''
        Constructor for SettingWindow class.
        Initializes the UI components and sets up the layout for the settings window.
        '''
        super().__init__()
        self.initUI()
        self.window5 = None                 # Tutorial window
        self.window6 = None                 # Help window
        self.window7 = None                 # About window

        #
        self.setWindowFlags(Qt.Window | Qt.WindowType.FramelessWindowHint | Qt.WindowType.NoDropShadowWindowHint)
        self.setObjectName("SettingWindow")
        self.setGeometry(int((WIDTH-370)/2),int((HEIGHT-675-150)/2),370,675)

    # //===================================================//
    def initUI(self):
        '''
        Initializes the UI components and sets up the layout for the settings window.
        '''
        self.vboxWindow = QVBoxLayout(self)
        self.vboxWindow.setContentsMargins(0,0,0,0)

        SettingWindow.labelTitle2 = QLabel(self)
        self.labelTitle2.setText('Setting')
        self.labelTitle2.setObjectName('lblTitle2')
        self.labelTitle2.setGeometry(0,0,370,28)

        self.windowFrame = QWidget(self)
        self.windowFrame.setObjectName('windowFrame')
        self.vboxFrame = QVBoxLayout(self.windowFrame)
        self.vboxFrame.setContentsMargins(0,0,0,0)

        self.titleBar = WindowDragger(self,self.windowFrame)
        self.titleBar.setObjectName('titleBar')
        self.titleBar.setSizePolicy(QSizePolicy(QSizePolicy.Preferred,QSizePolicy.Fixed))

        self.hboxTitle = QHBoxLayout(self.titleBar)
        self.hboxTitle.setContentsMargins(0,0,0,0)
        self.hboxTitle.setSpacing(0)

        self.labelTitle = QLabel()
        self.labelTitle.setObjectName('labelTitle')
        self.labelTitle.setGeometry(0,0,370,28)
        self.labelTitle.setFixedHeight(28)
        self.labelTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        from src.func.py_main_editor import TextGuiWindow

        SettingWindow.windowContent2 = QWidget(self.windowFrame)
        self.windowContent2.setObjectName('wdContent2')

        SettingWindow.labeltop = QWidget(self.windowFrame)
        self.labeltop.setObjectName('lbltop')
        self.labeltop.setFixedHeight(5)

        self.hboxTitle.addWidget(self.labelTitle)
        self.vboxFrame.addWidget(self.titleBar)
        self.vboxFrame.setSpacing(0)
        self.vboxFrame.addWidget(self.labeltop)
        self.vboxFrame.setSpacing(0)
        self.vboxFrame.addWidget(self.windowContent2)
        self.vboxWindow.addWidget(self.windowFrame)

        self.tabwidget = QTabWidget(self.windowContent2)
        self.tabwidget.setObjectName('tabwidget')
        self.tabwidget.setGeometry(15,3,341,590)

        self.page_general = QWidget(self)
        self.page_layout = QWidget(self)
        self.page_recognition = QWidget(self)
        self.page_theme = QWidget(self)
        self.page_misc = QWidget(self)

        self.page_general.setObjectName('page_general')
        self.page_layout.setObjectName('page_layout')
        self.page_recognition.setObjectName('page_recognition')
        self.page_theme.setObjectName('page_theme')
        self.page_misc.setObjectName('page_misc')

        self.tabwidget.addTab(self.page_general, 'General')
        self.tabwidget.addTab(self.page_layout, 'Layout')
        self.tabwidget.addTab(self.page_recognition, 'Recognition')
        self.tabwidget.addTab(self.page_theme, 'Theme')
        self.tabwidget.addTab(self.page_misc, 'Misc')


    # groupBox11
    # //==========================================================//
        self.groupBox11 = QGroupBox(self.page_general)
        self.groupBox11.setObjectName("groupBox11")
        self.groupBox11.setGeometry(QRect(12,18,315,80))

        self.label11 = QLabel(self.page_general)
        self.label11.setGeometry(QRect(22,10,80,15))
        self.label11.setObjectName("lbl11")
        self.label11.setText(" OCR Setting :")

    # //===================================================//
        self.label13 = QLabel(self.groupBox11)
        self.label13.setGeometry(QRect(20,15,67,25))
        self.label13.setText("Languages :")

    # //===================================================//
        self.comboBox1 = CheckableComboBox(self.groupBox11)
        self.comboBox1.setGeometry(QRect(125,18,175,20))
        self.comboBox1.setObjectName("comboBox1")
        self.comboBox1.setMaxVisibleItems(43)

        # //==============================================//
        list_language = ['English', \
        'Afrikaans', 'Albanian', 'Amharic', 'Arabic', 'Armenian', 'Assamese', 'Azerbaijani', \
        'Basque', 'Belarusian', 'Bengali', 'Bosnian', 'Breton', 'Bulgarian', 'Burmese', \
        'Castilian', 'Catalan', 'Cebuano', 'Chinese', 'Chinese (vertical)', 'Cherokee', 'Corsican', \
        'Croatian', 'Czech', 'Danish', 'Dhivehi', 'Dutch', 'Dzongkha', 'Esperanto', \
        'Estonian' , 'Faroese', 'Filipino', 'Finnish', 'French', 'Frisian', 'Gaelic', \
        'Galician', 'Georgian', 'German', 'Greek', 'Gujarati', 'Haitian', 'Hebrew', \
        'Hindi', 'Hungarian', 'Icelandic', 'Indonesian', 'Inuktitut', 'Irish', 'Italian', \
        'Japanese', 'Japanese (vertical)', 'Javanese', 'Kannada', 'Kazakh', 'Khmer', 'Korean', \
        'Kurdish', 'Kyrgyz', 'Lao', 'Latin', 'Latvian', 'Lithuanian', 'Luxembourgish', \
        'Macedonian', 'Malay', 'Malayalam', 'Maltese', 'Maori', 'Marathi', 'Mongolian', \
        'Nepali', 'Norwegian', 'Occitan', 'Oriya', 'Panjabi', 'Pashto', 'Persian', \
        'Polish', 'Portuguese', 'Quechua', 'Romanian', 'Russian', 'Sanskrit', 'Serbian', \
        'Sindhi', 'Sinhala', 'Slovak', 'Slovenian', 'Spanish', 'Sundanese', 'Swahili', \
        'Swedish', 'Syriac', 'Tajik', 'Tamil', 'Tatar', 'Telugu', 'Thai', \
        'Tibetan', 'Tigrinya',  'Tonga', 'Turkish', 'Ukrainian', 'Urdu', 'Uyghur', \
        'Uzbek', 'Vietnamese', 'Welsh', 'Yiddish', 'Yoruba', \
        'Select All' \
        ]

        self.comboBox1.addItems(list_language)
        self.comboBox1.insertSeparator(1)
        self.comboBox1.insertSeparator(112)
        self.comboBox1.insertSeparator(114)

        for i in range(len(list_language)+3):
            item = self.comboBox1.model().item(i, 0)
            item.setCheckState(Qt.CheckState.Unchecked)
        self.comboBox1.activated.connect(self.onChanged_combobox1)

        self.checkbox2 = QCheckBox("System Language",self.groupBox11)
        self.checkbox2.setGeometry(QRect(25,48,135,20))
        self.checkbox2.setChecked(False)

        self.checkbox3 = QCheckBox("Math && Equation",self.groupBox11)
        self.checkbox3.setGeometry(QRect(165,48,135,20))
        self.checkbox3.setChecked(False)


    # groupBox13
    # //===================================================//
        self.groupBox13 = QGroupBox(self.page_general)
        self.groupBox13.setObjectName("groupBox13")
        self.groupBox13.setGeometry(QRect(12,115,315,118))

        self.label131 = QLabel(self.page_general)
        self.label131.setGeometry(QRect(22,107,85,15))
        self.label131.setObjectName("lbl131")
        self.label131.setText(" Text Layout :")

        self.radioButton13a = QRadioButton(self.groupBox13)
        self.radioButton13a.setGeometry(QRect(25,15,100,15))
        self.radioButton13a.setChecked(True)
        self.radioButton13a.setText("Auto")

        self.radioButton13b = QRadioButton(self.groupBox13)
        self.radioButton13b.setGeometry(QRect(25,40,115,15))
        self.radioButton13b.setText("Single Character")

        self.radioButton13c = QRadioButton(self.groupBox13)
        self.radioButton13c.setGeometry(QRect(25,65,100,15))
        self.radioButton13c.setText("Single Word")

        self.radioButton13d = QRadioButton(self.groupBox13)
        self.radioButton13d.setGeometry(QRect(25,90,100,15))
        self.radioButton13d.setText("Single Line")

        self.radioButton13e = QRadioButton(self.groupBox13)
        self.radioButton13e.setGeometry(QRect(165,15,100,15))
        self.radioButton13e.setText("Sparse Text")

        self.radioButton13f = QRadioButton(self.groupBox13)
        self.radioButton13f.setGeometry(QRect(165,40,100,15))
        self.radioButton13f.setText("Veritcal Text")

        self.radioButton13g = QRadioButton(self.groupBox13)
        self.radioButton13g.setGeometry(QRect(165,65,100,15))
        self.radioButton13g.setText("Single Column")

        self.radioButton13h = QRadioButton(self.groupBox13)
        self.radioButton13h.setGeometry(QRect(165,90,115,15))
        self.radioButton13h.setText("Multiple Columns")


    # groupBox12
    # //===================================================//
        self.groupBox12 = QGroupBox(self.page_general)
        self.groupBox12.setObjectName("groupBox12")
        self.groupBox12.setGeometry(QRect(12,248,315,150))

        self.label121 = QLabel(self.page_general)
        self.label121.setGeometry(QRect(22,240,85,15))
        self.label121.setObjectName("lbl121")
        self.label121.setText(" Detected Text :")

        self.groupBox12a = QGroupBox(self.groupBox12)
        self.groupBox12a.setObjectName("groupBox12a")
        self.groupBox12a.setGeometry(QRect(13,13,289,30))

        self.radioButton12a = QRadioButton(self.groupBox12a)
        self.radioButton12a.setGeometry(QRect(15,8,100,15))
        self.radioButton12a.setChecked(True)
        self.radioButton12a.setText("Select All")
        self.radioButton12a.toggled.connect(self.onClicked_radioButton12a)

        self.radioButton12b = QRadioButton(self.groupBox12a)
        self.radioButton12b.setGeometry(QRect(155,8,115,15))
        self.radioButton12b.setText("Custom")
        self.radioButton12b.toggled.connect(self.onClicked_radioButton12b)

        self.groupBox12b = QGroupBox(self.groupBox12)
        self.groupBox12b.setObjectName("groupBox12b")
        self.groupBox12b.setGeometry(QRect(13,53,289,85))

        self.checkbox122 = QCheckBox("Lower Case (a-z)",self.groupBox12b)
        self.checkbox122.setGeometry(QRect(15,8,180,20))
        self.checkbox122.toggled.connect(self.onClicked_checkbox122)

        self.checkbox123 = QCheckBox("Upper Case (A-Z)",self.groupBox12b)
        self.checkbox123.setGeometry(QRect(15,33,180,20))
        self.checkbox123.toggled.connect(self.onClicked_checkbox123)

        self.checkbox124 = QCheckBox("Numbers (0-9)",self.groupBox12b)
        self.checkbox124.setGeometry(QRect(15,58,180,20))
        self.checkbox124.toggled.connect(self.onClicked_checkbox124)

        self.checkbox121 = QCheckBox("Letters",self.groupBox12b)
        self.checkbox121.setGeometry(QRect(155,8,180,20))
        self.checkbox121.toggled.connect(self.onClicked_checkbox121)

        self.checkbox125 = QCheckBox("Punctuation",self.groupBox12b)
        self.checkbox125.setGeometry(QRect(155,33,180,20))
        self.checkbox125.toggled.connect(self.onClicked_checkbox125)

        self.checkbox126 = QCheckBox("Special Characters",self.groupBox12b)
        self.checkbox126.setGeometry(QRect(155,58,180,20))
        self.checkbox126.toggled.connect(self.onClicked_checkbox126)

    # groupBox14
    # //===================================================//
        self.groupBox14 = QGroupBox(self.page_general)
        self.groupBox14.setObjectName("groupBox14")
        self.groupBox14.setGeometry(QRect(12,413,315,45))

        self.label141 = QLabel(self.page_general)
        self.label141.setGeometry(QRect(22,405,92,15))
        self.label141.setObjectName("lbl141")
        self.label141.setText(" Output Save as :")

        self.radioButton14a = QRadioButton(self.groupBox14)
        self.radioButton14a.setGeometry(QRect(25,15,80,15))
        self.radioButton14a.setChecked(True)
        self.radioButton14a.setText("Text")
        self.radioButton14a.setEnabled(True)

        self.radioButton14b = QRadioButton(self.groupBox14)
        self.radioButton14b.setGeometry(QRect(125,15,80,15))
        self.radioButton14b.setChecked(True)
        self.radioButton14b.setText("PDF")
        self.radioButton14b.setEnabled(True)

        self.radioButton14c = QRadioButton(self.groupBox14)
        self.radioButton14c.setGeometry(QRect(215,15,90,15))
        self.radioButton14c.setChecked(True)
        self.radioButton14c.setText("Spreadsheet")
        self.radioButton14c.setEnabled(True)


    # groupBox15
    # //===================================================//
        self.groupBox15 = QGroupBox(self.page_general)
        self.groupBox15.setObjectName("groupBox15")
        self.groupBox15.setGeometry(QRect(12,473,315,45))

        self.label151 = QLabel(self.page_general)
        self.label151.setGeometry(QRect(22,465,80,15))
        self.label151.setObjectName("lbl151")
        self.label151.setText(" Optimization :")

        self.radioButton15a = QRadioButton(self.groupBox15)
        self.radioButton15a.setGeometry(QRect(25,15,80,15))
        self.radioButton15a.setChecked(True)
        self.radioButton15a.setText("Standard")

        self.radioButton15b = QRadioButton(self.groupBox15)
        self.radioButton15b.setGeometry(QRect(125,15,80,15))
        self.radioButton15b.setText("Speed")

        self.radioButton15c = QRadioButton(self.groupBox15)
        self.radioButton15c.setGeometry(QRect(215,15,80,15))
        self.radioButton15c.setText("Accuracy")

        self.btnReset1 = QPushButton(self.page_general)
        self.btnReset1.setGeometry(QRect(252,530,75,25))
        self.btnReset1.setObjectName("btnReset1")
        self.btnReset1.setText("Reset")
        self.btnReset1.clicked.connect(self.ResetSetting1)
    # //===================================================//



    # //===================================================//
    # page_layout
    # //===================================================//
    # Pre-Process
    # Despeckle
    # Deskew
    # Fax Correction
    # image Inversion
    # Enhanced Image Resolution
    # Rotation

        self.groupBox16 = QGroupBox(self.page_layout)
        self.groupBox16.setObjectName("groupBox16")
        self.groupBox16.setGeometry(QRect(12,18,315,123))

        self.label161 = QLabel(self.page_layout)
        self.label161.setGeometry(QRect(22,10,82,15))
        self.label161.setObjectName("lbl31")
        self.label161.setText(" Page Layout :")

        self.checkbox161 = QCheckBox("Auto-Rotate Page",self.groupBox16)
        self.checkbox161.setGeometry(QRect(20,15,150,20))
        self.checkbox161.setChecked(False)
        self.checkbox161.toggled.connect(self.onClicked_checkbox161)

        self.checkbox162 = QCheckBox("Auto-Deskew",self.groupBox16)
        self.checkbox162.setGeometry(QRect(160,15,150,20))
        self.checkbox162.setChecked(False)
        self.checkbox162.toggled.connect(self.onClicked_checkbox162)

        self.checkbox163 = QCheckBox("Decolumnize",self.groupBox16)
        self.checkbox163.setGeometry(QRect(20,40,150,20))
        self.checkbox163.setChecked(False)

        self.checkbox164 = QCheckBox("Remove Tables",self.groupBox16)
        self.checkbox164.setGeometry(QRect(160,40,155,20))
        self.checkbox164.setChecked(False)
        self.checkbox164.toggled.connect(self.onClicked_checkbox164)

        self.checkbox165 = QCheckBox("Remove Watermarks",self.groupBox16)
        self.checkbox165.setGeometry(QRect(20,65,150,20))
        self.checkbox165.setChecked(False)
        self.checkbox165.toggled.connect(self.onClicked_checkbox165)

        self.checkbox166 = QCheckBox("Remove Underlines",self.groupBox16)
        self.checkbox166.setGeometry(QRect(160,65,150,20))
        self.checkbox166.setChecked(False)
        self.checkbox166.toggled.connect(self.onClicked_checkbox166)

        self.checkbox167 = QCheckBox("Remove Extra Spaces",self.groupBox16)
        self.checkbox167.setGeometry(QRect(20,90,150,20))
        self.checkbox167.setChecked(False)

        self.checkbox168 = QCheckBox("Remove Empty Lines",self.groupBox16)
        self.checkbox168.setGeometry(QRect(160,90,150,20))
        self.checkbox168.setChecked(False)
    # //===================================================//



    # //===================================================//
        self.groupBox43 = QGroupBox(self.page_layout)
        self.groupBox43.setObjectName("groupBox43")
        self.groupBox43.setGeometry(QRect(12,158,315,98))

        self.label221 = QLabel(self.page_layout)
        self.label221.setGeometry(QRect(22,150,115,15))
        self.label221.setObjectName("lbl221")
        self.label221.setText(" Image Enhancement :")

        self.checkbox35 = QCheckBox("Despeckle",self.groupBox43)
        self.checkbox35.setGeometry(QRect(20,15,150,20))
        self.checkbox35.setChecked(False)
        self.checkbox35.toggled.connect(self.onClicked_checkbox35)

        self.checkbox36 = QCheckBox("Threshold Binary",self.groupBox43)
        self.checkbox36.setGeometry(QRect(160,15,150,20))
        self.checkbox36.setChecked(False)
        self.checkbox36.toggled.connect(self.onClicked_checkbox36)

        self.checkbox37 = QCheckBox("Invert Color",self.groupBox43)
        self.checkbox37.setGeometry(QRect(20,40,150,20))
        self.checkbox37.setChecked(False)
        self.checkbox37.toggled.connect(self.onClicked_checkbox37)

        self.checkbox38 = QCheckBox("Threshold Adaptive",self.groupBox43)
        self.checkbox38.setGeometry(QRect(160,40,150,20))
        self.checkbox38.setChecked(False)
        self.checkbox38.toggled.connect(self.onClicked_checkbox38)

        self.checkbox39 = QCheckBox("Sharpen",self.groupBox43)
        self.checkbox39.setGeometry(QRect(20,65,150,20))
        self.checkbox39.setChecked(False)
        self.checkbox39.toggled.connect(self.onClicked_checkbox39)

        self.checkbox310 = QCheckBox("Contrast",self.groupBox43)
        self.checkbox310.setGeometry(QRect(160,65,150,20))
        self.checkbox310.setChecked(False)
        self.checkbox310.toggled.connect(self.onClicked_checkbox310)



        # Background filter
        # Text noise filter
        # Text erode filter
        # Text Dilate filter
    # //===================================================//
        self.groupBox44 = QGroupBox(self.page_layout)
        self.groupBox44.setObjectName("groupBox44")
        self.groupBox44.setGeometry(QRect(12,273,315,147))

        self.label311 = QLabel(self.page_layout)
        self.label311.setGeometry(QRect(22,265,92,15))
        self.label311.setObjectName("lbl311")
        self.label311.setText(" Image Filtering :")

        self.checkbox311 = QCheckBox("Background Noise",self.groupBox44)
        self.checkbox311.setGeometry(QRect(20,15,150,20))
        self.checkbox311.setChecked(False)
        self.checkbox311.toggled.connect(self.onClicked_checkbox311)

        self.slider311 = QSlider(Qt.Orientation.Horizontal,self.groupBox44)
        self.slider311.setGeometry(QRect(160,15,135,20))
        self.slider311.setObjectName("slider311")
        self.slider311.setRange(0,4)
        self.slider311.setMinimum(0)
        self.slider311.setMaximum(4)
        self.slider311.setSingleStep(1)
        self.slider311.setValue(2)
        self.slider311.setTickInterval(1)
        self.slider311.setTickPosition(QSlider.TicksBelow)
        self.slider311.setEnabled(False)
        self.slider311.valueChanged.connect(self.update_slider311)

        self.checkbox312 = QCheckBox("Text Noise",self.groupBox44)
        self.checkbox312.setGeometry(QRect(20,40,150,20))
        self.checkbox312.setChecked(False)
        self.checkbox312.toggled.connect(self.onClicked_checkbox312)

        self.slider312 = QSlider(Qt.Orientation.Horizontal,self.groupBox44)
        self.slider312.setGeometry(QRect(160,40,135,20))
        self.slider312.setObjectName("slider312")
        self.slider312.setRange(0,4)
        self.slider312.setMinimum(0)
        self.slider312.setMaximum(4)
        self.slider312.setSingleStep(1)
        self.slider312.setValue(2)
        self.slider312.setTickPosition(QSlider.TicksBelow)
        self.slider312.setTickInterval(1)
        self.slider312.setEnabled(False)
        self.slider312.valueChanged.connect(self.update_slider312)

        self.checkbox313 = QCheckBox("Text Erosion",self.groupBox44)
        self.checkbox313.setGeometry(QRect(20,65,150,20))
        self.checkbox313.setChecked(False)
        self.checkbox313.toggled.connect(self.onClicked_checkbox313)

        self.slider313 = QSlider(Qt.Orientation.Horizontal,self.groupBox44)
        self.slider313.setGeometry(QRect(160,65,135,20))
        self.slider313.setObjectName("slider313")
        self.slider313.setRange(0,4)
        self.slider313.setMinimum(0)
        self.slider313.setMaximum(4)
        self.slider313.setSingleStep(1)
        self.slider313.setValue(2)
        self.slider313.setTickPosition(QSlider.TicksBelow)
        self.slider313.setTickInterval(1)
        self.slider313.setEnabled(False)
        self.slider313.valueChanged.connect(self.update_slider313)

        self.checkbox314 = QCheckBox("Text Dilation",self.groupBox44)
        self.checkbox314.setGeometry(QRect(20,90,150,20))
        self.checkbox314.setChecked(False)
        self.checkbox314.toggled.connect(self.onClicked_checkbox314)

        self.slider314 = QSlider(Qt.Orientation.Horizontal,self.groupBox44)
        self.slider314.setGeometry(QRect(160,90,135,20))
        self.slider314.setObjectName("slider314")
        self.slider314.setRange(0,4)
        self.slider314.setMinimum(0)
        self.slider314.setMaximum(4)
        self.slider314.setSingleStep(1)
        self.slider314.setValue(2)
        self.slider314.setTickPosition(QSlider.TicksBelow)
        self.slider314.setTickInterval(1)
        self.slider314.setEnabled(False)
        self.slider314.valueChanged.connect(self.update_slider314)

        self.checkbox315 = QCheckBox("Threshold [L&&H]",self.groupBox44)
        self.checkbox315.setGeometry(QRect(20,115,150,20))
        self.checkbox315.setChecked(False)
        self.checkbox315.toggled.connect(self.onClicked_checkbox315)

        self.slider315a = QSlider(Qt.Orientation.Horizontal,self.groupBox44)
        self.slider315a.setGeometry(QRect(160,115,65,20))
        self.slider315a.setObjectName("slider315a")
        self.slider315a.setRange(0,255)
        self.slider315a.setMinimum(0)
        self.slider315a.setMaximum(255)
        self.slider315a.setSingleStep(1)
        self.slider315a.setValue(0)
        self.slider315a.setTickPosition(QSlider.TicksBelow)
        self.slider315a.setTickInterval(1)
        self.slider315a.setEnabled(False)
        self.slider315a.valueChanged.connect(self.update_slider315a)

        self.slider315b = QSlider(Qt.Orientation.Horizontal,self.groupBox44)
        self.slider315b.setGeometry(QRect(230,115,65,20))
        self.slider315b.setObjectName("slider315b")
        self.slider315b.setRange(0,255)
        self.slider315b.setMinimum(0)
        self.slider315b.setMaximum(255)
        self.slider315b.setSingleStep(1)
        self.slider315b.setValue(0)
        self.slider315b.setTickPosition(QSlider.TicksBelow)
        self.slider315b.setTickInterval(1)
        self.slider315b.setEnabled(False)
        self.slider315b.valueChanged.connect(self.update_slider315b)

    # //===================================================//
        self.groupBox45 = QGroupBox(self.page_layout)
        self.groupBox45.setObjectName("groupBox45")
        self.groupBox45.setGeometry(QRect(12,438,315,73))

        self.label312 = QLabel(self.page_layout)
        self.label312.setGeometry(QRect(22,430,92,15))
        self.label312.setObjectName("lbl312")
        self.label312.setText(" Output Display:")

        self.checkbox321 = QCheckBox("Original Color Image",self.groupBox45)
        self.checkbox321.setGeometry(QRect(20,15,135,20))
        self.checkbox321.setChecked(False)

        self.checkbox322 = QCheckBox("Original Gray Image",self.groupBox45)
        self.checkbox322.setGeometry(QRect(20,40,135,20))
        self.checkbox322.setChecked(False)

        self.checkbox323 = QCheckBox("Final Processed Image",self.groupBox45)
        self.checkbox323.setGeometry(QRect(160,15,150,20))
        self.checkbox323.setChecked(False)
        self.checkbox323.setEnabled(False)

        self.checkbox324 = QCheckBox("All Processed Images",self.groupBox45)
        self.checkbox324.setGeometry(QRect(160,40,150,20))
        self.checkbox324.setChecked(False)
        self.checkbox324.setEnabled(False)

        self.btnReset2 = QPushButton(self.page_layout)
        self.btnReset2.setGeometry(QRect(252,530,75,25))
        self.btnReset2.setObjectName("btnReset2")
        self.btnReset2.setText("Reset")
        self.btnReset2.clicked.connect(self.ResetSetting2)



    # //===================================================//
    # page_recognition
    # //===================================================//
        self.checkbox41 = QCheckBox("Whitelist",self.page_recognition)
        self.checkbox41.setGeometry(QRect(15,7,150,20))
        self.checkbox41.setChecked(False)
        self.checkbox41.toggled.connect(self.onClicked_checkbox41)

        self.groupBox31 = QGroupBox(self.page_recognition)
        self.groupBox31.setObjectName("groupBox31")
        self.groupBox31.setGeometry(QRect(12,38,315,190))

        self.label41 = QLabel(self.page_recognition)
        self.label41.setGeometry(QRect(22,30,117,15))
        self.label41.setObjectName("lbl41")
        self.label41.setText(" Character Included :")

        self.checkbox41a = QCheckBox("a-z",self.groupBox31)
        self.checkbox41a.setGeometry(QRect(15,12,50,20))
        self.checkbox41a.setChecked(False)
        self.checkbox41a.setEnabled(False)
        self.checkbox41a.toggled.connect(self.onClicked_checkbox41a)

        self.checkbox41b = QCheckBox("A-Z",self.groupBox31)
        self.checkbox41b.setGeometry(QRect(65,12,50,20))
        self.checkbox41b.setChecked(False)
        self.checkbox41b.setEnabled(False)
        self.checkbox41b.toggled.connect(self.onClicked_checkbox41b)

        self.checkbox41c = QCheckBox("0-9",self.groupBox31)
        self.checkbox41c.setGeometry(QRect(115,12,50,20))
        self.checkbox41c.setChecked(False)
        self.checkbox41c.setEnabled(False)
        self.checkbox41c.toggled.connect(self.onClicked_checkbox41c)

        self.checkbox41d = QCheckBox("Punct",self.groupBox31)
        self.checkbox41d.setGeometry(QRect(163,12,125,20))
        self.checkbox41d.setChecked(False)
        self.checkbox41d.setEnabled(False)
        self.checkbox41d.toggled.connect(self.onClicked_checkbox41d)

        self.checkbox41e = QCheckBox("Special Char",self.groupBox31)
        self.checkbox41e.setGeometry(QRect(220,12,125,20))
        self.checkbox41e.setChecked(False)
        self.checkbox41e.setEnabled(False)
        self.checkbox41e.toggled.connect(self.onClicked_checkbox41e)

        self.textbox_whitelist = QTextEdit(self.groupBox31)
        self.textbox_whitelist.setGeometry(QRect(13,40,288,135))
        self.textbox_whitelist.setObjectName("tbwl")
        self.textbox_whitelist.setEnabled(False)

        self.checkbox42 = QCheckBox("Blacklist",self.page_recognition)
        self.checkbox42.setGeometry(QRect(15,257,150,20))
        self.checkbox42.setChecked(False)
        self.checkbox42.toggled.connect(self.onClicked_checkbox42)

        self.groupBox32 = QGroupBox(self.page_recognition)
        self.groupBox32.setObjectName("groupBox32")
        self.groupBox32.setGeometry(QRect(12,288,315,190))

        self.label42 = QLabel(self.page_recognition)
        self.label42.setGeometry(QRect(22,280,117,15))
        self.label42.setObjectName("lbl42")
        self.label42.setText(" Character Excluded :")

        self.checkbox42a = QCheckBox("a-z",self.groupBox32)
        self.checkbox42a.setGeometry(QRect(15,12,50,20))
        self.checkbox42a.setChecked(False)
        self.checkbox42a.setEnabled(False)
        self.checkbox42a.toggled.connect(self.onClicked_checkbox42a)

        self.checkbox42b = QCheckBox("A-Z",self.groupBox32)
        self.checkbox42b.setGeometry(QRect(65,12,50,20))
        self.checkbox42b.setChecked(False)
        self.checkbox42b.setEnabled(False)
        self.checkbox42b.toggled.connect(self.onClicked_checkbox42b)

        self.checkbox42c = QCheckBox("0-9",self.groupBox32)
        self.checkbox42c.setGeometry(QRect(115,12,50,20))
        self.checkbox42c.setChecked(False)
        self.checkbox42c.setEnabled(False)
        self.checkbox42c.toggled.connect(self.onClicked_checkbox42c)

        self.checkbox42d = QCheckBox("Punct",self.groupBox32)
        self.checkbox42d.setGeometry(QRect(163,12,125,20))
        self.checkbox42d.setChecked(False)
        self.checkbox42d.setEnabled(False)
        self.checkbox42d.toggled.connect(self.onClicked_checkbox42d)

        self.checkbox42e = QCheckBox("Special Char",self.groupBox32)
        self.checkbox42e.setGeometry(QRect(220,12,125,20))
        self.checkbox42e.setChecked(False)
        self.checkbox42e.setEnabled(False)
        self.checkbox42e.toggled.connect(self.onClicked_checkbox42e)

        self.textbox_blacklist = QTextEdit(self.groupBox32)
        self.textbox_blacklist.setGeometry(QRect(13,40,288,135))
        self.textbox_blacklist.setObjectName("tbbl")
        self.textbox_blacklist.setEnabled(False)

        self.btnReset3 = QPushButton(self.page_recognition)
        self.btnReset3.setGeometry(QRect(252,530,75,25))
        self.btnReset3.setObjectName("btnReset3")
        self.btnReset3.setText("Reset")
        self.btnReset3.clicked.connect(self.ResetSetting3)

    # //===================================================//
    # page_theme
    # //===================================================//
        self.groupBox51 = QGroupBox(self.page_theme)
        self.groupBox51.setObjectName("groupBox51")
        self.groupBox51.setGeometry(QRect(12,18,315,110))

        self.label511 = QLabel(self.page_theme)
        self.label511.setGeometry(QRect(22,10,85,15))
        self.label511.setObjectName("lbl511")
        self.label511.setText(" Theme Color :")

        self.label512 = QLabel(self.groupBox51)
        self.label512.setGeometry(QRect(20,15,95,25))
        self.label512.setObjectName("label512")
        self.label512.setText("Light Theme :")

        self.comboBox5 = QComboBox(self.groupBox51)
        self.comboBox5.setGeometry(QRect(125,18,175,20))
        self.comboBox5.addItem("")
        self.comboBox5.setItemText(0,"Default")
        self.comboBox5.addItem("")
        self.comboBox5.setItemText(1,"Yellow")
        self.comboBox5.addItem("")
        self.comboBox5.setItemText(2,"Green")
        self.comboBox5.addItem("")
        self.comboBox5.setItemText(3,"Blue")
        self.comboBox5.addItem("")
        self.comboBox5.setItemText(4,"Pink")
        self.comboBox5.addItem("")
        self.comboBox5.setItemText(5,"Orange")
        self.comboBox5.addItem("")
        self.comboBox5.setItemText(6,"Custom")
        self.comboBox5.activated.connect(self.update_combobox5)

        self.label513 = QLabel(self.groupBox51)
        self.label513.setGeometry(QRect(20,45,95,25))
        self.label513.setObjectName("label513")
        self.label513.setText("Dark Theme :")

        self.comboBox6 = QComboBox(self.groupBox51)
        self.comboBox6.setGeometry(QRect(125,48,175,20))
        self.comboBox6.addItem("")
        self.comboBox6.setItemText(0,"Default")
        self.comboBox6.addItem("")
        self.comboBox6.setItemText(1,"Yellow")
        self.comboBox6.addItem("")
        self.comboBox6.setItemText(2,"Green")
        self.comboBox6.addItem("")
        self.comboBox6.setItemText(3,"Blue")
        self.comboBox6.addItem("")
        self.comboBox6.setItemText(4,"Pink")
        self.comboBox6.addItem("")
        self.comboBox6.setItemText(5,"Orange")
        self.comboBox6.addItem("")
        self.comboBox6.setItemText(6,"Custom")
        self.comboBox6.activated.connect(self.update_combobox6)

        from src.module.py_window_main import MainGuiWindow
        global Temp_ThemeLightColorVar, Temp_ThemeDarkColorVar
        Temp_ThemeLightColorVar = MainGuiWindow.ThemeLightColorVar1
        Temp_ThemeDarkColorVar = MainGuiWindow.ThemeDarkColorVar1

        self.label64 = QLabel(self.groupBox51)
        self.label64.setGeometry(QRect(20,75,85,25))
        self.label64.setObjectName("label64")
        self.label64.setText("Cursor Shape :")

        self.comboBox7 = QComboBox(self.groupBox51)
        self.comboBox7.setGeometry(QRect(125,78,175,20))
        self.comboBox7.addItem("")
        self.comboBox7.setItemText(0,"Default")
        self.comboBox7.addItem("")
        self.comboBox7.setItemText(1,"Arrow")
        self.comboBox7.addItem("")
        self.comboBox7.setItemText(2,"Target")
        self.comboBox7.addItem("")
        self.comboBox7.setItemText(3,"Pointer")
        self.comboBox7.addItem("")
        self.comboBox7.setItemText(4,"Pointing Hand")

        self.groupBox52 = QGroupBox(self.page_theme)
        self.groupBox52.setObjectName("groupBox52")
        self.groupBox52.setGeometry(QRect(12,143,315,185))

        self.label521 = QLabel(self.page_theme)
        self.label521.setGeometry(QRect(22,135,85,15))
        self.label521.setObjectName("lbl521")
        self.label521.setText(" Custom Color:")

        self.groupBox52a = QGroupBox(self.groupBox52)
        self.groupBox52a.setObjectName("groupBox52a")
        self.groupBox52a.setGeometry(QRect(12,18,290,70))

        self.label523 = QLabel(self.groupBox52)
        self.label523.setGeometry(QRect(25,10,120,15))
        self.label523.setObjectName("lbl523")
        self.label523.setText("Light Theme :")

        self.btn521 = QPushButton(self.groupBox52a)
        self.btn521.setGeometry(QRect(13,14,84,20))
        self.btn521.setObjectName("btn521")
        self.btn521.setText("TitleBar")
        self.btn521.setEnabled(False)
        self.btn521.clicked.connect(self.SetColorTBThemeLight)

        self.btn522 = QPushButton(self.groupBox52a)
        self.btn522.setGeometry(QRect(103,14,84,20))
        self.btn522.setObjectName("btn522")
        self.btn522.setText("Foreground")
        self.btn522.setEnabled(False)
        self.btn522.clicked.connect(self.SetColorFGThemeLight)

        self.btn523 = QPushButton(self.groupBox52a)
        self.btn523.setGeometry(QRect(193,14,84,20))
        self.btn523.setObjectName("btn523")
        self.btn523.setText("Background")
        self.btn523.setEnabled(False)
        self.btn523.clicked.connect(self.SetColorBGThemeLight)

        self.btn524 = QPushButton(self.groupBox52a)
        self.btn524.setGeometry(QRect(13,39,84,20))
        self.btn524.setObjectName("btn524")
        self.btn524.setText("Font")
        self.btn524.setEnabled(False)
        self.btn524.clicked.connect(self.SetColorFontThemeLight)

        self.btn525 = QPushButton(self.groupBox52a)
        self.btn525.setGeometry(QRect(103,39,84,20))
        self.btn525.setObjectName("btn525")
        self.btn525.setText("Button")
        self.btn525.setEnabled(False)
        self.btn525.clicked.connect(self.SetColorBTThemeLight)

        self.btn526 = QPushButton(self.groupBox52a)
        self.btn526.setGeometry(QRect(193,39,84,20))
        self.btn526.setObjectName("btn526")
        self.btn526.setText("Border")
        self.btn526.setEnabled(False)
        self.btn526.clicked.connect(self.SetColorBDThemeLight)

        self.groupBox52b = QGroupBox(self.groupBox52)
        self.groupBox52b.setObjectName("groupBox52b")
        self.groupBox52b.setGeometry(QRect(12,100,290,70))

        self.label524 = QLabel(self.groupBox52)
        self.label524.setGeometry(QRect(25,92,120,15))
        self.label524.setObjectName("lbl524")
        self.label524.setText("Dark Theme :")

        self.btn527 = QPushButton(self.groupBox52b)
        self.btn527.setGeometry(QRect(13,14,84,20))
        self.btn527.setObjectName("btn527")
        self.btn527.setText("TitleBar")
        self.btn527.setEnabled(False)
        self.btn527.clicked.connect(self.SetColorTBThemeDark)

        self.btn528 = QPushButton(self.groupBox52b)
        self.btn528.setGeometry(QRect(103,14,84,20))
        self.btn528.setObjectName("btn528")
        self.btn528.setText("Foreground")
        self.btn528.setEnabled(False)
        self.btn528.clicked.connect(self.SetColorFGThemeDark)

        self.btn529 = QPushButton(self.groupBox52b)
        self.btn529.setGeometry(QRect(193,14,84,20))
        self.btn529.setObjectName("btn529")
        self.btn529.setText("Background")
        self.btn529.setEnabled(False)
        self.btn529.clicked.connect(self.SetColorBGThemeDark)

        self.btn5210 = QPushButton(self.groupBox52b)
        self.btn5210.setGeometry(QRect(13,39,84,20))
        self.btn5210.setObjectName("btn5210")
        self.btn5210.setText("Font")
        self.btn5210.setEnabled(False)
        self.btn5210.clicked.connect(self.SetColorFontThemeDark)

        self.btn5211 = QPushButton(self.groupBox52b)
        self.btn5211.setGeometry(QRect(103,39,84,20))
        self.btn5211.setObjectName("btn5211")
        self.btn5211.setText("Button")
        self.btn5211.setEnabled(False)
        self.btn5211.clicked.connect(self.SetColorBTThemeDark)

        self.btn5212 = QPushButton(self.groupBox52b)
        self.btn5212.setGeometry(QRect(193,39,84,20))
        self.btn5212.setObjectName("btn5212")
        self.btn5212.setText("Border")
        self.btn5212.setEnabled(False)
        self.btn5212.clicked.connect(self.SetColorBDThemeDark)

        self.groupBox53 = QGroupBox(self.page_theme)
        self.groupBox53.setObjectName("groupBox53")
        self.groupBox53.setGeometry(QRect(12,345,315,100))

        self.label531 = QLabel(self.page_theme)
        self.label531.setGeometry(QRect(22,337,75,15))
        self.label531.setObjectName("lbl531")
        self.label531.setText(" Rubber Band :")

        self.label533 = QLabel(self.groupBox53)
        self.label533.setGeometry(QRect(15,15,120,15))
        self.label533.setObjectName("label533")
        self.label533.setText("Thickness :")

        self.slider531 = QSlider(Qt.Orientation.Horizontal,self.groupBox53)
        self.slider531.setGeometry(QRect(110,13,185,20))
        self.slider531.setObjectName("slider531")
        self.slider531.setMinimum(0)
        self.slider531.setMaximum(4)
        self.slider531.setValue(1)
        self.slider531.setTickPosition(QSlider.TicksBelow)
        self.slider531.setTickInterval(1)

        self.label534 = QLabel(self.groupBox53)
        self.label534.setGeometry(QRect(15,40,120,15))
        self.label534.setObjectName("label534")
        self.label534.setText("Opacity :")

        self.slider532 = QSlider(Qt.Orientation.Horizontal,self.groupBox53)
        self.slider532.setGeometry(QRect(110,38,185,20))
        self.slider532.setObjectName("slider532")
        self.slider532.setMinimum(0)
        self.slider532.setMaximum(4)
        self.slider532.setValue(2)
        self.slider532.setTickPosition(QSlider.TicksBelow)
        self.slider532.setTickInterval(1)

        self.label532 = QLabel(self.groupBox53)
        self.label532.setGeometry(QRect(15,65,120,15))
        self.label532.setObjectName("label532")
        self.label532.setText("Color :")

        self.btnRubberbandColor = QPushButton(self.groupBox53)
        self.btnRubberbandColor.setGeometry(QRect(110,63,185,23))
        self.btnRubberbandColor.setObjectName("btnRubberbandColor")
        self.btnRubberbandColor.setText("Select Color")
        self.btnRubberbandColor.clicked.connect(self.SetRubberbandBDColor)

        self.btnReset5 = QPushButton(self.page_theme)
        self.btnReset5.setGeometry(QRect(252,530,75,25))
        self.btnReset5.setObjectName("btnReset5")
        self.btnReset5.setText("Reset")
        self.btnReset5.clicked.connect(self.ResetSetting5)
     # //===================================================//











    # //===================================================//
    # page_misc
    # //===================================================//
        self.groupBox61 = QGroupBox(self.page_misc)
        self.groupBox61.setObjectName("groupBox61")
        self.groupBox61.setGeometry(QRect(12,18,315,80))

        self.label61 = QLabel(self.page_misc)
        self.label61.setGeometry(QRect(22,10,103,15))
        self.label61.setObjectName("lbl61")
        self.label61.setText(" System Setting :")

        self.label62 = QLabel(self.groupBox61)
        self.label62.setGeometry(QRect(20,15,95,25))
        self.label62.setObjectName("label62")
        self.label62.setText("Font Size :")

        self.comboBox8 = QComboBox(self.groupBox61)
        self.comboBox8.setGeometry(QRect(125,18,175,20))
        self.comboBox8.addItem("")
        self.comboBox8.setItemText(0,"Small")
        self.comboBox8.addItem("")
        self.comboBox8.setItemText(1,"Default")
        self.comboBox8.addItem("")
        self.comboBox8.setItemText(2,"Large")
        self.comboBox8.activated.connect(self.update_combobox8)

        self.label63 = QLabel(self.groupBox61)
        self.label63.setGeometry(QRect(20,45,95,25))
        self.label63.setObjectName("label63")
        self.label63.setText("Border Style :")

        self.comboBox9 = QComboBox(self.groupBox61)
        self.comboBox9.setGeometry(QRect(125,48,175,20))
        self.comboBox9.addItem("")
        self.comboBox9.setItemText(0,"Classic")
        self.comboBox9.addItem("")
        self.comboBox9.setItemText(1,"Default")
        self.comboBox9.activated.connect(self.update_combobox9)

        self.groupBox62 = QGroupBox(self.page_misc)
        self.groupBox62.setObjectName("groupBox62")
        self.groupBox62.setGeometry(QRect(12,113,315,110))

        self.label64 = QLabel(self.page_misc)
        self.label64.setGeometry(QRect(22,105,85,15))
        self.label64.setObjectName("lbl64")
        self.label64.setText(" Text Editor :")

        self.label66 = QLabel(self.groupBox62)
        self.label66.setGeometry(QRect(20,15,85,25))
        self.label66.setObjectName("lbl66")
        self.label66.setText("Icon Size :")

        self.comboBox11 = QComboBox(self.groupBox62)
        self.comboBox11.setGeometry(QRect(125,18,175,20))
        self.comboBox11.addItem("")
        self.comboBox11.setItemText(0,"Small")
        self.comboBox11.addItem("")
        self.comboBox11.setItemText(1,"Default")
        self.comboBox11.addItem("")
        self.comboBox11.setItemText(2,"Large")
        self.comboBox11.activated.connect(self.update_combobox11)

        self.label67 = QLabel(self.groupBox62)
        self.label67.setGeometry(QRect(20,45,85,25))
        self.label67.setObjectName("label67")
        self.label67.setText("Status Bar :")

        self.comboBox12 = QComboBox(self.groupBox62)
        self.comboBox12.setGeometry(QRect(125,48,175,20))
        self.comboBox12.addItem("")
        self.comboBox12.setItemText(0,"Default")
        self.comboBox12.addItem("")
        self.comboBox12.setItemText(1,"Show Message")
        self.comboBox12.activated.connect(self.update_combobox12)

        self.label68 = QLabel(self.groupBox62)
        self.label68.setGeometry(QRect(20,75,85,25))
        self.label68.setObjectName("label68")
        self.label68.setText("Toggle Mode :")

        self.comboBox13 = QComboBox(self.groupBox62)
        self.comboBox13.setGeometry(QRect(125,78,175,20))
        self.comboBox13.addItem("")
        self.comboBox13.setItemText(0,"Default")
        self.comboBox13.addItem("")
        self.comboBox13.setItemText(1,"Separated")
        self.comboBox13.activated.connect(self.update_combobox13)

        self.checkbox62 = QCheckBox("Hide Icon at System Tray",self.page_misc)
        self.checkbox62.setGeometry(QRect(25,235,185,20))
        self.checkbox62.setChecked(False)
        self.checkbox62.toggled.connect(self.onClicked_checkbox62)

        SettingWindow.btnAbout = QPushButton(self.page_misc)
        self.btnAbout.setGeometry(QRect(252,235,75,25))
        self.btnAbout.setObjectName("btnAbout")
        self.btnAbout.setText("About")
        self.btnAbout.clicked.connect(self.showAboutWindow)

        SettingWindow.btnHelp = QPushButton(self.page_misc)
        self.btnHelp.setGeometry(QRect(252,270,75,25))
        self.btnHelp.setObjectName("btnHelp")
        self.btnHelp.setText("Help")
        self.btnHelp.clicked.connect(self.showHelpWindow)

        SettingWindow.btnTutorial = QPushButton(self.page_misc)
        self.btnTutorial.setGeometry(QRect(252,305,75,25))
        self.btnTutorial.setObjectName("btnTutorial")
        self.btnTutorial.setText("Tutorial")
        self.btnTutorial.clicked.connect(self.showTutorialWindow)

        self.btnResetDefault = QPushButton(self.page_misc)
        self.btnResetDefault.setGeometry(QRect(143,530,98,25))
        self.btnResetDefault.setObjectName("btnResetDefault")
        self.btnResetDefault.setText("Restore Defaults")
        self.btnResetDefault.clicked.connect(self.ResetDefaultSetting)


        self.btnReset6 = QPushButton(self.page_misc)
        self.btnReset6.setGeometry(QRect(252,530,75,25))
        self.btnReset6.setObjectName("btnReset5")
        self.btnReset6.setText("Reset")
        self.btnReset6.clicked.connect(self.ResetSetting6)

    # button
    # //===================================================//
        SettingWindow.btnOK2 = QPushButton(self)
        self.btnOK2.setGeometry(QRect(75,638,75,25))
        self.btnOK2.setObjectName("btnOK2")
        self.btnOK2.setText("OK")
        self.btnOK2.clicked.connect(self.OKSetting)

        SettingWindow.btnCancel2 = QPushButton(self)
        self.btnCancel2.setGeometry(QRect(220,638,75,25))
        self.btnCancel2.setObjectName("btnCancel2")
        self.btnCancel2.setText("Cancel")
        self.btnCancel2.clicked.connect(self.CancelSetting)


    # set Theme
    # //===================================================//
        from src.module.py_window_main import MainGuiWindow
        from src.func.py_main_editor import TextGuiWindow

        if MainGuiWindow.THEME == "light":
            TextGuiWindow.set_LightTheme(self)
        elif MainGuiWindow.THEME == "dark":
            TextGuiWindow.set_DarkTheme(self)
        TextGuiWindow.read_StyleSheet(self)
        self.LoadConfig()

        global Theme_light_temp, ThemeLightColorVar1_temp, Theme_dark_temp, ThemeDarkColorVar1_temp
        global FontSystemSizeVar1_temp, BorderStyleVar1_temp, TextEditorIconSizeVar1_temp, TextEditorStatusBarVar1_temp

        FontSystemSizeVar1_temp = MainGuiWindow.FontSystemSizeVar1
        BorderStyleVar1_temp = MainGuiWindow.BorderStyleVar1
        TextEditorIconSizeVar1_temp = MainGuiWindow.TextEditorIconSizeVar1
        TextEditorStatusBarVar1_temp = MainGuiWindow.TextEditorStatusBarVar1

        Theme_light_temp = MainGuiWindow.THEME_LIGHT
        ThemeLightColorVar1_temp = MainGuiWindow.ThemeLightColorVar1
        Theme_dark_temp = MainGuiWindow.THEME_DARK
        ThemeDarkColorVar1_temp = MainGuiWindow.ThemeDarkColorVar1

        global Color_font_light_temp, Color_TB_light_temp, Color_FG_light_temp, Color_BG_light_temp, Color_BT_light_temp, Color_BD_light_temp
        global Color_font_dark_temp, Color_TB_dark_temp, Color_FG_dark_temp, Color_BG_dark_temp, Color_BT_dark_temp, Color_BD_dark_temp
        Color_font_light_temp = MainGuiWindow.FONT_COLOR_LIGHT_CUSTOM
        Color_TB_light_temp = MainGuiWindow.TB_COLOR_LIGHT_CUSTOM
        Color_FG_light_temp = MainGuiWindow.FG_COLOR_LIGHT_CUSTOM
        Color_BG_light_temp = MainGuiWindow.BG_COLOR_LIGHT_CUSTOM
        Color_BT_light_temp = MainGuiWindow.BT_COLOR_LIGHT_CUSTOM
        Color_BD_light_temp = MainGuiWindow.BD_COLOR_LIGHT_CUSTOM
        Color_font_dark_temp = MainGuiWindow.FONT_COLOR_DARK_CUSTOM
        Color_TB_dark_temp = MainGuiWindow.TB_COLOR_DARK_CUSTOM
        Color_FG_dark_temp = MainGuiWindow.FG_COLOR_DARK_CUSTOM
        Color_BG_dark_temp = MainGuiWindow.BG_COLOR_DARK_CUSTOM
        Color_BT_dark_temp = MainGuiWindow.BT_COLOR_DARK_CUSTOM
        Color_BD_dark_temp = MainGuiWindow.BD_COLOR_DARK_CUSTOM

        global RBBColorVar1_temp
        RBBColorVar1_temp = MainGuiWindow.RBBColorVar1

    # //===================================================//
        self.update_combobox8()
    # //===================================================//


    # //===================================================//
        from src.module.py_window_main import MainGuiWindow
        if MainGuiWindow.THEME == "light":
            self.update_combobox5()
        elif MainGuiWindow.THEME == "dark":
            self.update_combobox6()
        QMetaObject.connectSlotsByName(self)
#########################################################################



#########################################################################
# //===========================================//
    def LoadConfig(self):
        from src.module.py_window_main import MainGuiWindow
        global RBBColorVar
        global FLAG_SELECT_ALL_INIT, FLAG_COMBOBOX_SELECT_ALL

        print('=== LoadConfig ===')
        LanguageVarList = MainGuiWindow.LanguageVarList1
        LanguageSystemVar  = MainGuiWindow.LanguageSystemVar1
        MathEquationVar = MainGuiWindow.MathEquationVar1
        TextLayoutVar = MainGuiWindow.TextLayoutVar1
        DetectedTextVar = MainGuiWindow.DetectedTextVar1
        DetectedTextLetterVar = MainGuiWindow.DetectedTextLetterVar1
        DetectedTextLowerVar = MainGuiWindow.DetectedTextLowerVar1
        DetectedTextUpperVar = MainGuiWindow.DetectedTextUpperVar1
        DetectedTextNumberVar = MainGuiWindow.DetectedTextNumberVar1
        DetectedTextPuncVar = MainGuiWindow.DetectedTextPuncVar1
        DetectedTextMiscVar = MainGuiWindow.DetectedTextMiscVar1
        PageLayoutAutoRotatePageVar = MainGuiWindow.PageLayoutAutoRotatePageVar1
        PageLayoutDeskewVar = MainGuiWindow.PageLayoutDeskewVar1
        PageLayoutDecolumnizeVar = MainGuiWindow.PageLayoutDecolumnizeVar1
        PageLayoutRemoveTableVar = MainGuiWindow.PageLayoutRemoveTableVar1
        PageLayoutRemoveWatermarkVar = MainGuiWindow.PageLayoutRemoveWatermarkVar1
        PageLayoutRemoveUnderlineVar = MainGuiWindow.PageLayoutRemoveUnderlineVar1
        PageLayoutRemoveSpaceVar = MainGuiWindow.PageLayoutRemoveSpaceVar1
        PageLayoutRemoveLineVar = MainGuiWindow.PageLayoutRemoveLineVar1
        OutputFormatVar = MainGuiWindow.OutputFormatVar1
        OptimizationVar = MainGuiWindow.OptimizationVar1
        LayoutDespeckleVar = MainGuiWindow.LayoutDespeckleVar1
        LayoutThresholdVar = MainGuiWindow.LayoutThresholdVar1
        LayoutInvertColorVar  = MainGuiWindow.LayoutInvertColorVar1
        LayoutThresholdAdaptiveVar = MainGuiWindow.LayoutThresholdAdaptiveVar1
        LayoutSharpenVar = MainGuiWindow.LayoutSharpenVar1
        LayoutContrastVar = MainGuiWindow.LayoutContrastVar1
        FilteringBackgroundNoiseVar = MainGuiWindow.FilteringBackgroundNoiseVar1
        FilteringBackgroundNoiseIntVar = MainGuiWindow.FilteringBackgroundNoiseIntVar1
        FilteringTextNoiseVar = MainGuiWindow.FilteringTextNoiseVar1
        FilteringTextNoiseIntVar = MainGuiWindow.FilteringTextNoiseIntVar1
        FilteringTextErosionVar = MainGuiWindow.FilteringTextErosionVar1
        FilteringTextErosionIntVar = MainGuiWindow.FilteringTextErosionIntVar1
        FilteringTextDilationVar = MainGuiWindow.FilteringTextDilationVar1
        FilteringTextDilationIntVar = MainGuiWindow.FilteringTextDilationIntVar1
        FilteringThresholdVar = MainGuiWindow.FilteringThresholdVar1
        FilteringThresholdLowerIntVar = MainGuiWindow.FilteringThresholdLowerIntVar1
        FilteringThresholdUpperIntVar = MainGuiWindow.FilteringThresholdUpperIntVar1
        DisplayColorImageVar = MainGuiWindow.DisplayColorImageVar1
        DisplayGrayImageVar = MainGuiWindow.DisplayGrayImageVar1
        DisplayProcessedImageVar = MainGuiWindow.DisplayProcessedImageVar1
        DisplayProcessedAllImageVar = MainGuiWindow.DisplayProcessedAllImageVar1
        WhitelistVar = MainGuiWindow.WhitelistVar1
        Whitelist1Var = MainGuiWindow.Whitelist1Var1
        Whitelist2Var = MainGuiWindow.Whitelist2Var1
        Whitelist3Var = MainGuiWindow.Whitelist3Var1
        Whitelist4Var = MainGuiWindow.Whitelist4Var1
        Whitelist5Var = MainGuiWindow.Whitelist5Var1
        WhitelistCharVar = MainGuiWindow.WhitelistCharVar1
        BlacklistVar = MainGuiWindow.BlacklistVar1
        Blacklist1Var = MainGuiWindow.Blacklist1Var1
        Blacklist2Var = MainGuiWindow.Blacklist2Var1
        Blacklist3Var = MainGuiWindow.Blacklist3Var1
        Blacklist4Var = MainGuiWindow.Blacklist4Var1
        Blacklist5Var = MainGuiWindow.Blacklist5Var1
        BlacklistCharVar = MainGuiWindow.BlacklistCharVar1
        ThemeLightColorVar = MainGuiWindow.ThemeLightColorVar1
        ThemeDarkColorVar = MainGuiWindow.ThemeDarkColorVar1
        CursorShapeVar = MainGuiWindow.CursorShapeVar1
        RBBThicknessVar = MainGuiWindow.RBBThicknessVar1
        RBBOpacityVar = MainGuiWindow.RBBOpacityVar1
        RBBColorVar = MainGuiWindow.RBBColorVar1
        FontSystemSizeVar = MainGuiWindow.FontSystemSizeVar1
        BorderStyleVar = MainGuiWindow.BorderStyleVar1
        TextEditorIconSizeVar = MainGuiWindow.TextEditorIconSizeVar1
        TextEditorStatusBarVar = MainGuiWindow.TextEditorStatusBarVar1
        TextEditorModeVar = MainGuiWindow.TextEditorModeVar1
        SystemTrayIconVar = MainGuiWindow.SystemTrayIconVar1

    # page1
    # //===========================================//
        LanguageVar = ' '.join([str(element) for i,element in enumerate(LanguageVarList)])
        LanguageVarFirst = int(int(LanguageVar.find('1'))/2)
        FLAG_SELECT_ALL_INIT = True
        FLAG_COMBOBOX_SELECT_ALL = bool(LanguageVarList[56])

        for i in range(len(LanguageVarList)):
            if (LanguageVarList[i] == 1):
                item = self.comboBox1.model().item(i, 0)
                item.setCheckState(Qt.CheckState.Checked)

        self.comboBox1.setCurrentIndex(int(LanguageVarFirst))

        if LanguageSystemVar  == 0:
            self.checkbox2.setChecked(False)
        else:
            self.checkbox2.setChecked(True)

        if MathEquationVar == 0:
            self.checkbox3.setChecked(False)
        else:
            self.checkbox3.setChecked(True)

        if TextLayoutVar == 0:
            self.radioButton13a.setChecked(True)
        if TextLayoutVar == 1:
            self.radioButton13b.setChecked(True)
        if TextLayoutVar == 2:
            self.radioButton13c.setChecked(True)
        if TextLayoutVar == 3:
            self.radioButton13d.setChecked(True)
        if TextLayoutVar == 4:
            self.radioButton13e.setChecked(True)
        if TextLayoutVar == 5:
            self.radioButton13f.setChecked(True)
        if TextLayoutVar == 6:
            self.radioButton13g.setChecked(True)
        if TextLayoutVar == 7:
            self.radioButton13h.setChecked(True)

        if DetectedTextVar == 0:
            self.radioButton12a.setChecked(True)
            self.checkbox121.setEnabled(False)
            self.checkbox122.setEnabled(False)
            self.checkbox123.setEnabled(False)
            self.checkbox124.setEnabled(False)
            self.checkbox125.setEnabled(False)
            self.checkbox126.setEnabled(False)
        if DetectedTextVar == 1:
            self.radioButton12b.setChecked(True)
            self.checkbox121.setEnabled(True)
            self.checkbox122.setEnabled(True)
            self.checkbox123.setEnabled(True)
            self.checkbox124.setEnabled(True)
            self.checkbox125.setEnabled(True)
            self.checkbox126.setEnabled(True)

        if DetectedTextLetterVar == 0:
            self.checkbox121.setChecked(False)
        else:
            self.checkbox121.setChecked(True)

        if DetectedTextLowerVar == 0:
            self.checkbox122.setChecked(False)
        else:
            self.checkbox122.setChecked(True)

        if DetectedTextUpperVar == 0:
            self.checkbox123.setChecked(False)
        else:
            self.checkbox123.setChecked(True)

        if DetectedTextNumberVar == 0:
            self.checkbox124.setChecked(False)
        else:
            self.checkbox124.setChecked(True)

        if DetectedTextPuncVar == 0:
            self.checkbox125.setChecked(False)
        else:
            self.checkbox125.setChecked(True)

        if DetectedTextMiscVar == 0:
            self.checkbox126.setChecked(False)
        else:
            self.checkbox126.setChecked(True)

        if OutputFormatVar == 0:
            self.radioButton14a.setChecked(True)
        if OutputFormatVar == 1:
            self.radioButton14b.setChecked(True)
        if OutputFormatVar == 2:
            self.radioButton14c.setChecked(True)

        if OptimizationVar == 0:
            self.radioButton15a.setChecked(True)
        if OptimizationVar == 1:
            self.radioButton15b.setChecked(True)
        if OptimizationVar == 2:
            self.radioButton15c.setChecked(True)

    # page2-1
    # //===========================================//
        if PageLayoutAutoRotatePageVar == 0:
            self.checkbox161.setChecked(False)
        else:
            self.checkbox161.setChecked(True)

        if PageLayoutDeskewVar == 0:
            self.checkbox162.setChecked(False)
        else:
            self.checkbox162.setChecked(True)

        if PageLayoutDecolumnizeVar == 0:
            self.checkbox163.setChecked(False)
        else:
            self.checkbox163.setChecked(True)

        if PageLayoutRemoveTableVar == 0:
            self.checkbox164.setChecked(False)
        else:
            self.checkbox164.setChecked(True)

        if PageLayoutRemoveWatermarkVar == 0:
            self.checkbox165.setChecked(False)
        else:
            self.checkbox165.setChecked(True)

        if PageLayoutRemoveUnderlineVar == 0:
            self.checkbox166.setChecked(False)
        else:
            self.checkbox166.setChecked(True)

        if PageLayoutRemoveSpaceVar == 0:
            self.checkbox167.setChecked(False)
        else:
            self.checkbox167.setChecked(True)

        if PageLayoutRemoveLineVar == 0:
            self.checkbox168.setChecked(False)
        else:
            self.checkbox168.setChecked(True)

        if LayoutDespeckleVar == 0:
            self.checkbox35.setChecked(False)
        else:
            self.checkbox35.setChecked(True)

        if LayoutThresholdVar == 0:
            self.checkbox36.setChecked(False)
        else:
            self.checkbox36.setChecked(True)

        if LayoutInvertColorVar == 0:
            self.checkbox37.setChecked(False)
        else:
            self.checkbox37.setChecked(True)

        if LayoutThresholdAdaptiveVar == 0:
            self.checkbox38.setChecked(False)
        else:
            self.checkbox38.setChecked(True)

        if LayoutSharpenVar == 0:
            self.checkbox39.setChecked(False)
        else:
            self.checkbox39.setChecked(True)

        if LayoutContrastVar == 0:
            self.checkbox310.setChecked(False)
        else:
            self.checkbox310.setChecked(True)

    # page2-2
    # //===========================================//

        if FilteringBackgroundNoiseVar == 0:
            self.checkbox311.setChecked(False)
        else:
            self.checkbox311.setChecked(True)
        self.slider311.setValue(int((FilteringBackgroundNoiseIntVar-3)/4))      # [3,7,11,15,19]

        if FilteringTextNoiseVar == 0:
            self.checkbox312.setChecked(False)
        else:
            self.checkbox312.setChecked(True)
        self.slider312.setValue(int(FilteringTextNoiseIntVar-2))                # [2,3,4,5,6]

        if FilteringTextErosionVar == 0:
            self.checkbox313.setChecked(False)
        else:
            self.checkbox313.setChecked(True)
        self.slider313.setValue(int(FilteringTextErosionIntVar-2))

        if FilteringTextDilationVar == 0:
            self.checkbox314.setChecked(False)
        else:
            self.checkbox314.setChecked(True)
        self.slider314.setValue(int(FilteringTextDilationIntVar-2))

        if FilteringThresholdVar == 0:
            self.checkbox315.setChecked(False)
        else:
            self.checkbox315.setChecked(True)
        self.slider315a.setValue(int(FilteringThresholdLowerIntVar))        # [0-255]
        self.slider315b.setValue(int(FilteringThresholdUpperIntVar))        # [0-255]

        if DisplayColorImageVar == 0:
            self.checkbox321.setChecked(False)
        else:
            self.checkbox321.setChecked(True)

        if DisplayGrayImageVar == 0:
            self.checkbox322.setChecked(False)
        else:
            self.checkbox322.setChecked(True)

        if DisplayProcessedImageVar == 0:
            self.checkbox323.setChecked(False)
        else:
            self.checkbox323.setChecked(True)

        if DisplayProcessedAllImageVar == 0:
            self.checkbox324.setChecked(False)
        else:
            self.checkbox324.setChecked(True)

    # page3
    # //===========================================//
        if WhitelistVar == 0:
            self.checkbox41.setChecked(False)
        else:
            self.checkbox41.setChecked(True)

        if Whitelist1Var == 0:
            self.checkbox41a.setChecked(False)
        else:
            self.checkbox41a.setChecked(True)

        if Whitelist2Var == 0:
            self.checkbox41b.setChecked(False)
        else:
            self.checkbox41b.setChecked(True)

        if Whitelist3Var == 0:
            self.checkbox41c.setChecked(False)
        else:
            self.checkbox41c.setChecked(True)

        if Whitelist4Var == 0:
            self.checkbox41d.setChecked(False)
        else:
            self.checkbox41d.setChecked(True)

        if Whitelist5Var == 0:
            self.checkbox41e.setChecked(False)
        else:
            self.checkbox41e.setChecked(True)
        self.textbox_whitelist.setPlainText(str(WhitelistCharVar))

        if BlacklistVar == 0:
            self.checkbox42.setChecked(False)
        else:
            self.checkbox42.setChecked(True)

        if Blacklist1Var == 0:
            self.checkbox42a.setChecked(False)
        else:
            self.checkbox42a.setChecked(True)

        if Blacklist2Var == 0:
            self.checkbox42b.setChecked(False)
        else:
            self.checkbox42b.setChecked(True)

        if Blacklist3Var == 0:
            self.checkbox42c.setChecked(False)
        else:
            self.checkbox42c.setChecked(True)

        if Blacklist4Var == 0:
            self.checkbox42d.setChecked(False)
        else:
            self.checkbox42d.setChecked(True)

        if Blacklist5Var == 0:
            self.checkbox42e.setChecked(False)
        else:
            self.checkbox42e.setChecked(True)

        self.textbox_blacklist.setPlainText(str(BlacklistCharVar))


    # page5
    # //===========================================//
        self.comboBox5.setCurrentIndex(int(ThemeLightColorVar))

        if (ThemeLightColorVar == 6):
            self.btn521.setEnabled(True)
            self.btn522.setEnabled(True)
            self.btn523.setEnabled(True)
            self.btn524.setEnabled(True)
            self.btn525.setEnabled(True)
            self.btn526.setEnabled(True)
        else:
            self.btn521.setEnabled(False)
            self.btn522.setEnabled(False)
            self.btn523.setEnabled(False)
            self.btn524.setEnabled(False)
            self.btn525.setEnabled(False)
            self.btn526.setEnabled(False)
        self.comboBox6.setCurrentIndex(int(ThemeDarkColorVar))

        if (ThemeDarkColorVar == 6):
            self.btn527.setEnabled(True)
            self.btn528.setEnabled(True)
            self.btn529.setEnabled(True)
            self.btn5210.setEnabled(True)
            self.btn5211.setEnabled(True)
            self.btn5212.setEnabled(True)
        else:
            self.btn527.setEnabled(False)
            self.btn528.setEnabled(False)
            self.btn529.setEnabled(False)
            self.btn5210.setEnabled(False)
            self.btn5211.setEnabled(False)
            self.btn5212.setEnabled(False)
        self.comboBox7.setCurrentIndex(int(CursorShapeVar))

        if (RBBThicknessVar == 0):
            self.slider531.setValue(0)
        elif (RBBThicknessVar == 2):
            self.slider531.setValue(1)
        elif (RBBThicknessVar == 6):
            self.slider531.setValue(2)
        elif (RBBThicknessVar == 8):
            self.slider531.setValue(3)
        elif (RBBThicknessVar == 12):
            self.slider531.setValue(4)
        self.slider532.setValue(int(int(RBBOpacityVar)/50))
        MainGuiWindow.RBBColorVar1 = RBBColorVar

    # page6
    # //===========================================//

        if (FontSystemSizeVar == 7):
            self.comboBox8.setCurrentIndex(0)
        elif (FontSystemSizeVar == 8):
            self.comboBox8.setCurrentIndex(1)
        elif (FontSystemSizeVar == 9):
            self.comboBox8.setCurrentIndex(2)
        self.comboBox9.setCurrentIndex(int(BorderStyleVar))

        if (TextEditorIconSizeVar == 16):
            self.comboBox11.setCurrentIndex(0)
        elif (TextEditorIconSizeVar == 18):
            self.comboBox11.setCurrentIndex(1)
        elif (TextEditorIconSizeVar == 22):
            self.comboBox11.setCurrentIndex(2)
        self.comboBox12.setCurrentIndex(int(TextEditorStatusBarVar))
        self.comboBox13.setCurrentIndex(int(TextEditorModeVar))

        if SystemTrayIconVar == 0:
            self.checkbox62.setChecked(False)
        else:
            self.checkbox62.setChecked(True)

# //===========================================//
    def ResetSetting1(self):
        print('=== ResetSetting1 ===')
        LanguageVarList =  [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        LanguageSystemVar = 0
        MathEquationVar = 0
        TextLayoutVar = 0
        DetectedTextVar = 0
        DetectedTextLetterVar = 0
        DetectedTextLowerVar = 0
        DetectedTextUpperVar = 0
        DetectedTextNumberVar = 0
        DetectedTextPuncVar = 0
        DetectedTextMiscVar = 0
        OutputFormatVar = 0
        OptimizationVar = 0

    # page1
    # //===========================================//
        LanguageVar = ' '.join([str(element) for i,element in enumerate(LanguageVarList)])
        LanguageVarFirst = int(int(LanguageVar.find('1'))/2)

        global FLAG_COMBOBOX_SELECT_ALL
        FLAG_COMBOBOX_SELECT_ALL = bool(LanguageVarList[56])

        for i in range(len(LanguageVarList)):
            item = self.comboBox1.model().item(i, 0)
            item.setCheckState(Qt.CheckState.Unchecked)

        for i in range(len(LanguageVarList)):
            if (LanguageVarList[i] == 1):
                item = self.comboBox1.model().item(i, 0)
                item.setCheckState(Qt.CheckState.Checked)

        self.comboBox1.setCurrentIndex(int(LanguageVarFirst))

        if LanguageSystemVar == 0:
            self.checkbox2.setChecked(False)
        else:
            self.checkbox2.setChecked(True)

        if MathEquationVar == 0:
            self.checkbox3.setChecked(False)
        else:
            self.checkbox3.setChecked(True)

        if TextLayoutVar == 0:
            self.radioButton13a.setChecked(True)
        if TextLayoutVar == 1:
            self.radioButton13b.setChecked(True)
        if TextLayoutVar == 2:
            self.radioButton13c.setChecked(True)
        if TextLayoutVar == 3:
            self.radioButton13d.setChecked(True)
        if TextLayoutVar == 4:
            self.radioButton13e.setChecked(True)
        if TextLayoutVar == 5:
            self.radioButton13f.setChecked(True)
        if TextLayoutVar == 6:
            self.radioButton13g.setChecked(True)
        if TextLayoutVar == 7:
            self.radioButton13h.setChecked(True)

        if DetectedTextVar == 0:
            self.radioButton12a.setChecked(True)
        if DetectedTextVar == 1:
            self.radioButton12b.setChecked(True)

        if DetectedTextLetterVar == 0:
            self.checkbox121.setChecked(False)
        else:
            self.checkbox121.setChecked(True)

        if DetectedTextLowerVar == 0:
            self.checkbox122.setChecked(False)
        else:
            self.checkbox122.setChecked(True)

        if DetectedTextUpperVar == 0:
            self.checkbox123.setChecked(False)
        else:
            self.checkbox123.setChecked(True)

        if DetectedTextNumberVar == 0:
            self.checkbox124.setChecked(False)
        else:
            self.checkbox124.setChecked(True)

        if DetectedTextPuncVar == 0:
            self.checkbox125.setChecked(False)
        else:
            self.checkbox125.setChecked(True)

        if DetectedTextMiscVar == 0:
            self.checkbox126.setChecked(False)
        else:
            self.checkbox126.setChecked(True)

        if OutputFormatVar == 0:
            self.radioButton14a.setChecked(True)
        if OutputFormatVar == 1:
            self.radioButton14b.setChecked(True)
        if OutputFormatVar == 2:
            self.radioButton14c.setChecked(True)
        if OptimizationVar == 0:
            self.radioButton15a.setChecked(True)
        if OptimizationVar == 1:
            self.radioButton15b.setChecked(True)
        if OptimizationVar == 2:
            self.radioButton15c.setChecked(True)

# //===========================================//
    def ResetSetting2(self):

        print('=== ResetSetting2 ===')
        PageLayoutAutoRotatePageVar = 0
        PageLayoutDeskewVar = 0
        PageLayoutDecolumnizeVar = 0
        PageLayoutRemoveTableVar = 0
        PageLayoutRemoveWatermarkVar = 0
        PageLayoutRemoveUnderlineVar = 0
        PageLayoutRemoveSpaceVar = 0
        PageLayoutRemoveLineVar = 0
        LayoutDespeckleVar = 0
        LayoutThresholdVar = 0
        LayoutInvertColorVar = 0
        LayoutThresholdAdaptiveVar = 0
        LayoutSharpenVar = 0
        LayoutContrastVar = 0
        FilteringBackgroundNoiseVar = 0
        FilteringBackgroundNoiseIntVar = 0
        FilteringTextNoiseVar = 0
        FilteringTextNoiseIntVar = 0
        FilteringTextErosionVar = 0
        FilteringTextErosionIntVar = 0
        FilteringTextDilationVar = 0
        FilteringTextDilationIntVar = 0
        FilteringThresholdVar = 0
        FilteringThresholdLowerIntVar = 0
        FilteringThresholdUpperIntVar = 0
        DisplayColorImageVar = 0
        DisplayGrayImageVar = 0
        DisplayProcessedImageVar = 0
        DisplayProcessedAllImageVar = 0

    # page2-1
    # //===========================================//
        if PageLayoutAutoRotatePageVar == 0:
            self.checkbox161.setChecked(False)
        else:
            self.checkbox161.setChecked(True)

        if PageLayoutDeskewVar == 0:
            self.checkbox162.setChecked(False)
        else:
            self.checkbox162.setChecked(True)

        if PageLayoutDecolumnizeVar == 0:
            self.checkbox163.setChecked(False)
        else:
            self.checkbox163.setChecked(True)

        if PageLayoutRemoveTableVar == 0:
            self.checkbox164.setChecked(False)
        else:
            self.checkbox164.setChecked(True)

        if PageLayoutRemoveWatermarkVar == 0:
            self.checkbox165.setChecked(False)
        else:
            self.checkbox165.setChecked(True)

        if PageLayoutRemoveUnderlineVar == 0:
            self.checkbox166.setChecked(False)
        else:
            self.checkbox166.setChecked(True)

        if PageLayoutRemoveSpaceVar == 0:
            self.checkbox167.setChecked(False)
        else:
            self.checkbox167.setChecked(True)

        if PageLayoutRemoveLineVar == 0:
            self.checkbox168.setChecked(False)
        else:
            self.checkbox168.setChecked(True)

        if LayoutDespeckleVar == 0:
            self.checkbox35.setChecked(False)
        else:
            self.checkbox35.setChecked(True)

        if LayoutThresholdVar == 0:
            self.checkbox36.setChecked(False)
        else:
            self.checkbox36.setChecked(True)

        if LayoutInvertColorVar == 0:
            self.checkbox37.setChecked(False)
        else:
            self.checkbox37.setChecked(True)

        if LayoutThresholdAdaptiveVar == 0:
            self.checkbox38.setChecked(False)
        else:
            self.checkbox38.setChecked(True)

        if LayoutSharpenVar == 0:
            self.checkbox39.setChecked(False)
        else:
            self.checkbox39.setChecked(True)

        if LayoutContrastVar == 0:
            self.checkbox310.setChecked(False)
        else:
            self.checkbox310.setChecked(True)

    # page2-2
    # //===========================================//
        if FilteringBackgroundNoiseVar == 0:
            self.checkbox311.setChecked(False)
        else:
            self.checkbox311.setChecked(True)
        self.slider311.setValue(int((FilteringBackgroundNoiseIntVar-3)/4))

        if FilteringTextNoiseVar == 0:
            self.checkbox312.setChecked(False)
        else:
            self.checkbox312.setChecked(True)
        self.slider312.setValue(int(FilteringTextNoiseIntVar-2))

        if FilteringTextErosionVar == 0:
            self.checkbox313.setChecked(False)
        else:
            self.checkbox313.setChecked(True)
        self.slider313.setValue(int(FilteringTextErosionIntVar-2))

        if FilteringTextDilationVar == 0:
            self.checkbox314.setChecked(False)
        else:
            self.checkbox314.setChecked(True)
        self.slider314.setValue(int(FilteringTextDilationIntVar-2))

        if FilteringThresholdVar == 0:
            self.checkbox315.setChecked(False)
        else:
            self.checkbox315.setChecked(True)
        self.slider315a.setValue(int(FilteringThresholdLowerIntVar))
        self.slider315b.setValue(int(FilteringThresholdUpperIntVar))

        if DisplayColorImageVar == 0:
            self.checkbox321.setChecked(False)
        else:
            self.checkbox321.setChecked(True)

        if DisplayGrayImageVar == 0:
            self.checkbox322.setChecked(False)
        else:
            self.checkbox322.setChecked(True)

        if DisplayProcessedImageVar == 0:
            self.checkbox323.setChecked(False)
        else:
            self.checkbox323.setChecked(True)

        if DisplayProcessedAllImageVar == 0:
            self.checkbox324.setChecked(False)
        else:
            self.checkbox324.setChecked(True)

# //===========================================//
    def ResetSetting3(self):
        print('=== ResetSetting3 ===')
        WhitelistVar = 0
        Whitelist1Var = 0
        Whitelist2Var = 0
        Whitelist3Var = 0
        Whitelist4Var = 0
        Whitelist5Var = 0
        WhitelistCharVar = ''
        BlacklistVar = 0
        Blacklist1Var = 0
        Blacklist2Var = 0
        Blacklist3Var = 0
        Blacklist4Var = 0
        Blacklist5Var = 0
        BlacklistCharVar = ''

    # page3
    # //===========================================//
        if WhitelistVar == 0:
            self.checkbox41.setChecked(False)
        else:
            self.checkbox41.setChecked(True)

        if Whitelist1Var == 0:
            self.checkbox41a.setChecked(False)
        else:
            self.checkbox41a.setChecked(True)

        if Whitelist2Var == 0:
            self.checkbox41b.setChecked(False)
        else:
            self.checkbox41b.setChecked(True)

        if Whitelist3Var == 0:
            self.checkbox41c.setChecked(False)
        else:
            self.checkbox41c.setChecked(True)

        if Whitelist4Var == 0:
            self.checkbox41d.setChecked(False)
        else:
            self.checkbox41d.setChecked(True)

        if Whitelist5Var == 0:
            self.checkbox41e.setChecked(False)
        else:
            self.checkbox41e.setChecked(True)

        self.textbox_whitelist.setPlainText(str(WhitelistCharVar))

        if BlacklistVar == 0:
            self.checkbox42.setChecked(False)
        else:
            self.checkbox42.setChecked(True)

        if Blacklist1Var == 0:
            self.checkbox42a.setChecked(False)
        else:
            self.checkbox42a.setChecked(True)

        if Blacklist2Var == 0:
            self.checkbox42b.setChecked(False)
        else:
            self.checkbox42b.setChecked(True)

        if Blacklist3Var == 0:
            self.checkbox42c.setChecked(False)
        else:
            self.checkbox42c.setChecked(True)

        if Blacklist4Var == 0:
            self.checkbox42d.setChecked(False)
        else:
            self.checkbox42d.setChecked(True)

        if Blacklist5Var == 0:
            self.checkbox42e.setChecked(False)
        else:
            self.checkbox42e.setChecked(True)
        self.textbox_blacklist.setPlainText(str(BlacklistCharVar))


# //===========================================//
    def ResetSetting5(self):

        print('=== ResetSetting5 ===')
        from src.module.py_window_main import MainGuiWindow

        ThemeLightColorVar = 0
        MainGuiWindow.TB_COLOR_LIGHT_CUSTOM = '#AA5500'
        MainGuiWindow.FG_COLOR_LIGHT_CUSTOM = '#FFFBAA'
        MainGuiWindow.BG_COLOR_LIGHT_CUSTOM = '#FFFFAA'
        MainGuiWindow.FONT_COLOR_LIGHT_CUSTOM = '#550000'
        MainGuiWindow.BT_COLOR_LIGHT_CUSTOM = '#553333'
        MainGuiWindow.BD_COLOR_LIGHT_CUSTOM = '#AA5500'
        ThemeDarkColorVar = 0
        MainGuiWindow.TB_COLOR_DARK_CUSTOM = '#3A3A95'
        MainGuiWindow.FG_COLOR_DARK_CUSTOM = '#3A3A5A'
        MainGuiWindow.BG_COLOR_DARK_CUSTOM = '#33334F'
        MainGuiWindow.FONT_COLOR_DARK_CUSTOM = '#FFFFFF'
        MainGuiWindow.BT_COLOR_DARK_CUSTOM = '#11AAFF'
        MainGuiWindow.BD_COLOR_DARK_CUSTOM = '#3F3FCC'
        CursorShapeVar = 0
        RBBThicknessVar = 6
        RBBOpacityVar = 100
        MainGuiWindow.RBBColorVar1 = '#00CC00'
        MainGuiWindow.setRubberBandColor(self)

    # page5
    # //===========================================//
        self.btn521.setEnabled(False)
        self.btn522.setEnabled(False)
        self.btn523.setEnabled(False)
        self.btn524.setEnabled(False)
        self.btn525.setEnabled(False)
        self.btn526.setEnabled(False)
        self.btn527.setEnabled(False)
        self.btn528.setEnabled(False)
        self.btn529.setEnabled(False)
        self.btn5210.setEnabled(False)
        self.btn5211.setEnabled(False)
        self.btn5212.setEnabled(False)

    # page5
    # //===========================================//
        self.comboBox5.setCurrentIndex(int(ThemeLightColorVar))
        self.comboBox6.setCurrentIndex(int(ThemeDarkColorVar))
        self.comboBox7.setCurrentIndex(int(CursorShapeVar))
        self.update_combobox5()

        if (RBBThicknessVar == 0):
            self.slider531.setValue(0)
        elif (RBBThicknessVar == 2):
            self.slider531.setValue(1)
        elif (RBBThicknessVar == 6):
            self.slider531.setValue(2)
        elif (RBBThicknessVar == 8):
            self.slider531.setValue(3)
        elif (RBBThicknessVar == 12):
            self.slider531.setValue(4)

        self.slider532.setValue(int(int(RBBOpacityVar)/50))


# //===========================================//
    def ResetSetting6(self):
        print('=== ResetSetting6 ===')
        FontSystemSizeVar = 8
        BorderStyleVar = 1
        TextEditorIconSizeVar = 18
        TextEditorStatusBarVar = 0
        TextEditorModeVar = 0
        SystemTrayIconVar = 0

    # page6
    # //===========================================//
        if (FontSystemSizeVar == 7):
            self.comboBox8.setCurrentIndex(0)
        elif (FontSystemSizeVar == 8):
            self.comboBox8.setCurrentIndex(1)
        elif (FontSystemSizeVar == 9):
            self.comboBox8.setCurrentIndex(2)
        self.comboBox9.setCurrentIndex(int(BorderStyleVar))

        if (TextEditorIconSizeVar == 16):
            self.comboBox11.setCurrentIndex(0)
        elif (TextEditorIconSizeVar == 18):
            self.comboBox11.setCurrentIndex(1)
        elif (TextEditorIconSizeVar == 22):
            self.comboBox11.setCurrentIndex(2)

        self.comboBox12.setCurrentIndex(int(TextEditorStatusBarVar))
        self.comboBox13.setCurrentIndex(int(TextEditorModeVar))
        self.update_combobox8()
        self.update_combobox9()
        self.update_combobox11()

        if SystemTrayIconVar == 0:
            self.checkbox62.setChecked(False)
        else:
            self.checkbox62.setChecked(True)

        self.update_combobox8()
        self.update_combobox9()


# //===========================================//
    def ResetDefaultSetting(self):

        print('=== ResetDefaultSetting ===')
        self.ResetSetting1()
        self.ResetSetting2()
        self.ResetSetting3()
        self.ResetSetting5()
        self.ResetSetting6()

        from src.module.py_window_main import MainGuiWindow
        from src.func.py_main_editor import TextGuiWindow
        from src.config.py_config import FONT_TEXT_SIZE_INIT, FONT_TEXT_FAMILY_INIT

        MainGuiWindow.THEME = "light"
        MainGuiWindow.THEME_LIGHT = "Default"
        MainGuiWindow.THEME_DARK = "Default"
        MainGuiWindow.ThemeLightColorVar1 = 0
        MainGuiWindow.ThemeDarkColorVar1 = 0
        MainGuiWindow.FONT_TEXT_SIZE_LIGHT = FONT_TEXT_SIZE_INIT
        MainGuiWindow.FONT_TEXT_SIZE_DARK = FONT_TEXT_SIZE_INIT
        MainGuiWindow.FONT_TEXT_FAMILY_LIGHT = FONT_TEXT_FAMILY_INIT
        MainGuiWindow.FONT_TEXT_FAMILY_DARK = FONT_TEXT_FAMILY_INIT
        MainGuiWindow.FONT_TEXT_COLOR_LIGHT = '#000000'
        MainGuiWindow.FONT_TEXT_COLOR_DARK = '#FFFFFF'
        MainGuiWindow.OPACITY_TEXT_LIGHT = 1
        MainGuiWindow.OPACITY_TEXT_DARK = 1
        MainGuiWindow.PARAGRAPH_TEXT_LIGHT = False
        MainGuiWindow.PARAGRAPH_TEXT_DARK = False
        MainGuiWindow.DOCKING = 0
        MainGuiWindow.FLAG_TOOLBAR = False
        MainGuiWindow.FLAG_FORMATBAR = False
        MainGuiWindow.FLAG_STATUSBAR = False

        try:
            TextGuiWindow.textbox.setStyleSheet('QTextEdit { color: %s }' %MainGuiWindow.FONT_TEXT_COLOR_LIGHT)
            TextGuiWindow.updateEnabled_icon(self)
            TextGuiWindow.showTabSpaces(self)
        except:
            pass

    # //===================================================//
    def showAboutWindow(self):
        from src.module.py_window_about import AboutWindow

        print('=== showAboutWindow ===')
        if self.window7 is None:
            self.window7 = AboutWindow()
        self.window7.show()
        self.btnAbout.setEnabled(False)

        from src.module.py_window_main import MainGuiWindow
        MainGuiWindow.aboutAction.setEnabled(False)

    # //===================================================//
    def showHelpWindow(self):
        from src.module.py_window_help import HelpWindow

        print('=== showHelpWindow ===')
        if self.window6 is None:
            self.window6 = HelpWindow()
        self.window6.show()
        self.btnHelp.setEnabled(False)

        from src.module.py_window_main import MainGuiWindow
        MainGuiWindow.helpAction.setEnabled(False)

    # //===================================================//
    def showTutorialWindow(self):
        from src.module.py_window_tutorial import TutorialWindow

        print('=== showTutorialWindow ===')
        if self.window5 is None:
            self.window5 = TutorialWindow()
        self.window5.show()
        self.btnTutorial.setEnabled(False)

# //===========================================//
    def OKSetting(self):
        from src.module.py_window_main import MainGuiWindow
        print('=== OKSetting ===')

    #page1
# //===========================================//
        language_selected = self.comboBox1.currentData()
        MainGuiWindow.LanguageVarList1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

        for i in language_selected:
            if (i == 'English'):
                MainGuiWindow.LanguageVarList1[0] = 1
            elif (i == 'Afrikaans'):
                MainGuiWindow.LanguageVarList1[2] = 1
            elif (i == 'Albanian'):
                MainGuiWindow.LanguageVarList1[3] = 1
            elif (i == 'Amharic'):
                MainGuiWindow.LanguageVarList1[4] = 1
            elif (i == 'Arabic'):
                MainGuiWindow.LanguageVarList1[5] = 1
            elif (i == 'Armenian'):
                MainGuiWindow.LanguageVarList1[6] = 1
            elif (i == 'Assamese'):
                MainGuiWindow.LanguageVarList1[7] = 1
            elif (i == 'Azerbaijani'):
                MainGuiWindow.LanguageVarList1[8] = 1
            elif (i == 'Basque'):
                MainGuiWindow.LanguageVarList1[9] = 1
            elif (i == 'Belarusian'):
                MainGuiWindow.LanguageVarList1[10] = 1
            elif (i == 'Bengali'):
                MainGuiWindow.LanguageVarList1[11] = 1
            elif (i == 'Bosnian'):
                MainGuiWindow.LanguageVarList1[12] = 1
            elif (i == 'Breton'):
                MainGuiWindow.LanguageVarList1[13] = 1
            elif (i == 'Bulgarian'):
                MainGuiWindow.LanguageVarList1[14] = 1
            elif (i == 'Burmese'):
                MainGuiWindow.LanguageVarList1[15] = 1
            elif (i == 'Castilian'):
                MainGuiWindow.LanguageVarList1[16] = 1
            elif (i == 'Catalan'):
                MainGuiWindow.LanguageVarList1[17] = 1
            elif (i == 'Cebuano'):
                MainGuiWindow.LanguageVarList1[18] = 1
            elif (i == 'Chinese'):
                MainGuiWindow.LanguageVarList1[19] = 1
            elif (i == 'Chinese (vertical)'):
                MainGuiWindow.LanguageVarList1[20] = 1
            elif (i == 'Cherokee'):
                MainGuiWindow.LanguageVarList1[21]= 1
            elif (i == 'Corsican'):
                MainGuiWindow.LanguageVarList1[22]= 1
            elif (i == 'Croatian'):
                MainGuiWindow.LanguageVarList1[23]= 1
            elif (i == 'Czech'):
                MainGuiWindow.LanguageVarList1[24] = 1
            elif (i == 'Danish'):
                MainGuiWindow.LanguageVarList1[25] = 1
            elif (i == 'Dhivehi'):
                MainGuiWindow.LanguageVarList1[26] = 1
            elif (i == 'Dutch'):
                MainGuiWindow.LanguageVarList1[27] = 1
            elif (i == 'Dzongkha'):
                MainGuiWindow.LanguageVarList1[28] = 1
            elif (i == 'Esperanto'):
                MainGuiWindow.LanguageVarList1[29] = 1
            elif (i == 'Estonian'):
                MainGuiWindow.LanguageVarList1[30] = 1
            elif (i == 'Faroese'):
                MainGuiWindow.LanguageVarList1[31] = 1
            elif (i == 'Filipino'):
                MainGuiWindow.LanguageVarList1[32] = 1
            elif (i == 'Finnish'):
                MainGuiWindow.LanguageVarList1[33] = 1
            elif (i == 'French'):
                MainGuiWindow.LanguageVarList1[34] = 1
            elif (i == 'Frisian'):
                MainGuiWindow.LanguageVarList1[35] = 1
            elif (i == 'Gaelic'):
                MainGuiWindow.LanguageVarList1[36] = 1
            elif (i == 'Galician'):
                MainGuiWindow.LanguageVarList1[37] = 1
            elif (i == 'Georgian'):
                MainGuiWindow.LanguageVarList1[38] = 1
            elif (i == 'German'):
                MainGuiWindow.LanguageVarList1[39] = 1
            elif (i == 'Greek'):
                MainGuiWindow.LanguageVarList1[40] = 1
            elif (i == 'Gujarati'):
                MainGuiWindow.LanguageVarList1[41] = 1
            elif (i == 'Haitian'):
                MainGuiWindow.LanguageVarList1[42] = 1
            elif (i == 'Hebrew'):
                MainGuiWindow.LanguageVarList1[43] = 1
            elif (i == 'Hindi'):
                MainGuiWindow.LanguageVarList1[44] = 1
            elif (i == 'Hungarian'):
                MainGuiWindow.LanguageVarList1[45] = 1
            elif (i == 'Icelandic'):
                MainGuiWindow.LanguageVarList1[46] = 1
            elif (i == 'Indonesian'):
                MainGuiWindow.LanguageVarList1[47] = 1
            elif (i == 'Inuktitut'):
                MainGuiWindow.LanguageVarList1[48] = 1
            elif (i == 'Irish'):
                MainGuiWindow.LanguageVarList1[49] = 1
            elif (i == 'Italian'):
                MainGuiWindow.LanguageVarList1[50] = 1
            elif (i == 'Japanese'):
                MainGuiWindow.LanguageVarList1[51] = 1
            elif (i == 'Japanese (vertical)'):
                MainGuiWindow.LanguageVarList1[52] = 1
            elif (i == 'Javanese'):
                MainGuiWindow.LanguageVarList1[53] = 1
            elif (i == 'Kannada'):
                MainGuiWindow.LanguageVarList1[54] = 1
            elif (i == 'Kazakh'):
                MainGuiWindow.LanguageVarList1[55] = 1
            elif (i == 'Khmer'):
                MainGuiWindow.LanguageVarList1[56] = 1
            elif (i == 'Korean'):
                MainGuiWindow.LanguageVarList1[57] = 1
            elif (i == 'Kurdish'):
                MainGuiWindow.LanguageVarList1[58] = 1
            elif (i == 'Kyrgyz'):
                MainGuiWindow.LanguageVarList1[59] = 1
            elif (i == 'Lao'):
                MainGuiWindow.LanguageVarList1[60] = 1
            elif (i == 'Latin'):
                MainGuiWindow.LanguageVarList1[61] = 1
            elif (i == 'Latvian'):
                MainGuiWindow.LanguageVarList1[62] = 1
            elif (i == 'Lithuanian'):
                MainGuiWindow.LanguageVarList1[63] = 1
            elif (i == 'Luxembourgish'):
                MainGuiWindow.LanguageVarList1[64] = 1
            elif (i == 'Macedonian'):
                MainGuiWindow.LanguageVarList1[65] = 1
            elif (i == 'Malay'):
                MainGuiWindow.LanguageVarList1[66] = 1
            elif (i == 'Malayalam'):
                MainGuiWindow.LanguageVarList1[67] = 1
            elif (i == 'Maltese'):
                MainGuiWindow.LanguageVarList1[68] = 1
            elif (i == 'Maori'):
                MainGuiWindow.LanguageVarList1[69] = 1
            elif (i == 'Marathi'):
                MainGuiWindow.LanguageVarList1[70] = 1
            elif (i == 'Mongolian'):
                MainGuiWindow.LanguageVarList1[71] = 1
            elif (i == 'Nepali'):
                MainGuiWindow.LanguageVarList1[72] = 1
            elif (i == 'Norwegian'):
                MainGuiWindow.LanguageVarList1[73] = 1
            elif (i == 'Occitan'):
                MainGuiWindow.LanguageVarList1[74] = 1
            elif (i == 'Oriya'):
                MainGuiWindow.LanguageVarList1[75] = 1
            elif (i == 'Panjabi'):
                MainGuiWindow.LanguageVarList1[76] = 1
            elif (i == 'Pashto'):
                MainGuiWindow.LanguageVarList1[77] = 1
            elif (i == 'Persian'):
                MainGuiWindow.LanguageVarList1[78] = 1
            elif (i == 'Polish'):
                MainGuiWindow.LanguageVarList1[79] = 1
            elif (i == 'Portuguese'):
                MainGuiWindow.LanguageVarList1[80] = 1
            elif (i == 'Quechua'):
                MainGuiWindow.LanguageVarList1[81] = 1
            elif (i == 'Romanian'):
                MainGuiWindow.LanguageVarList1[82] = 1
            elif (i == 'Russian'):
                MainGuiWindow.LanguageVarList1[83] = 1
            elif (i == 'Sanskrit'):
                MainGuiWindow.LanguageVarList1[84] = 1
            elif (i == 'Serbian'):
                MainGuiWindow.LanguageVarList1[85] = 1
            elif (i == 'Sindhi'):
                MainGuiWindow.LanguageVarList1[86] = 1
            elif (i == 'Sinhala'):
                MainGuiWindow.LanguageVarList1[87] = 1
            elif (i == 'Slovak'):
                MainGuiWindow.LanguageVarList1[88] = 1
            elif (i == 'Slovenian'):
                MainGuiWindow.LanguageVarList1[89] = 1
            elif (i == 'Spanish'):
                MainGuiWindow.LanguageVarList1[90] = 1
            elif (i == 'Sundanese'):
                MainGuiWindow.LanguageVarList1[91] = 1
            elif (i == 'Swahili'):
                MainGuiWindow.LanguageVarList1[92] = 1
            elif (i == 'Swedish'):
                MainGuiWindow.LanguageVarList1[93] = 1
            elif (i == 'Syriac'):
                MainGuiWindow.LanguageVarList1[94] = 1
            elif (i == 'Tajik'):
                MainGuiWindow.LanguageVarList1[95] = 1
            elif (i == 'Tamil'):
                MainGuiWindow.LanguageVarList1[96] = 1
            elif (i == 'Tatar'):
                MainGuiWindow.LanguageVarList1[97] = 1
            elif (i == 'Telugu'):
                MainGuiWindow.LanguageVarList1[98] = 1
            elif (i == 'Thai'):
                MainGuiWindow.LanguageVarList1[99] = 1
            elif (i == 'Tibetan'):
                MainGuiWindow.LanguageVarList1[100] = 1
            elif (i == 'Tigrinya'):
                MainGuiWindow.LanguageVarList1[101] = 1
            elif (i == 'Tonga'):
                MainGuiWindow.LanguageVarList1[102] = 1
            elif (i == 'Turkish'):
                MainGuiWindow.LanguageVarList1[103] = 1
            elif (i == 'Ukrainian'):
                MainGuiWindow.LanguageVarList1[104] = 1
            elif (i == 'Urdu'):
                MainGuiWindow.LanguageVarList1[105] = 1
            elif (i == 'Uyghur'):
                MainGuiWindow.LanguageVarList1[106] = 1
            elif (i == 'Uzbek'):
                MainGuiWindow.LanguageVarList1[107] = 1
            elif (i == 'Vietnamese'):
                MainGuiWindow.LanguageVarList1[108] = 1
            elif (i == 'Welsh'):
                MainGuiWindow.LanguageVarList1[109] = 1
            elif (i == 'Yiddish'):
                MainGuiWindow.LanguageVarList1[110] = 1
            elif (i == 'Yoruba'):
                MainGuiWindow.LanguageVarList1[111] = 1
            elif (i == 'Select All'):
                MainGuiWindow.LanguageVarList1[113] = 1

        if (language_selected == []):
            MainGuiWindow.LanguageVarList1 = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

        if self.checkbox2.isChecked():
            MainGuiWindow.LanguageSystemVar1 = 1
        else:
            MainGuiWindow.LanguageSystemVar1 = 0

        if self.checkbox3.isChecked():
            MainGuiWindow.MathEquationVar1 = 1
        else:
            MainGuiWindow.MathEquationVar1 = 0

        if self.radioButton13a.isChecked() == True:
            MainGuiWindow.TextLayoutVar1 = 0
        if self.radioButton13b.isChecked() == True:
            MainGuiWindow.TextLayoutVar1 = 1
        if self.radioButton13c.isChecked() == True:
            MainGuiWindow.TextLayoutVar1 = 2
        if self.radioButton13d.isChecked() == True:
            MainGuiWindow.TextLayoutVar1 = 3
        if self.radioButton13e.isChecked() == True:
            MainGuiWindow.TextLayoutVar1 = 4
        if self.radioButton13f.isChecked() == True:
            MainGuiWindow.TextLayoutVar1 = 5
        if self.radioButton13g.isChecked() == True:
            MainGuiWindow.TextLayoutVar1 = 6
        if self.radioButton13h.isChecked() == True:
            MainGuiWindow.TextLayoutVar1 = 7


        if self.radioButton12a.isChecked() == True:
            MainGuiWindow.DetectedTextVar1 = 0
        if self.radioButton12b.isChecked() == True:
            MainGuiWindow.DetectedTextVar1 = 1


        if self.checkbox121.isChecked():
            MainGuiWindow.DetectedTextLetterVar1 = 1
        else:
            MainGuiWindow.DetectedTextLetterVar1 = 0

        if self.checkbox122.isChecked():
            MainGuiWindow.DetectedTextLowerVar1 = 1
        else:
            MainGuiWindow.DetectedTextLowerVar1 = 0

        if self.checkbox123.isChecked():
            MainGuiWindow.DetectedTextUpperVar1 = 1
        else:
            MainGuiWindow.DetectedTextUpperVar1 = 0

        if self.checkbox124.isChecked():
            MainGuiWindow.DetectedTextNumberVar1 = 1
        else:
            MainGuiWindow.DetectedTextNumberVar1 = 0

        if self.checkbox125.isChecked():
            MainGuiWindow.DetectedTextPuncVar1 = 1
        else:
            MainGuiWindow.DetectedTextPuncVar1 = 0

        if self.checkbox126.isChecked():
            MainGuiWindow.DetectedTextMiscVar1 = 1
        else:
            MainGuiWindow.DetectedTextMiscVar1 = 0


        if self.checkbox161.isChecked():
            MainGuiWindow.PageLayoutAutoRotatePageVar1 = 1
        else:
            MainGuiWindow.PageLayoutAutoRotatePageVar1 = 0

        if self.checkbox162.isChecked():
            MainGuiWindow.PageLayoutDeskewVar1 = 1
        else:
            MainGuiWindow.PageLayoutDeskewVar1 = 0

        if self.checkbox163.isChecked():
            MainGuiWindow.PageLayoutDecolumnizeVar1 = 1
        else:
            MainGuiWindow.PageLayoutDecolumnizeVar1 = 0

        if self.checkbox164.isChecked():
            MainGuiWindow.PageLayoutRemoveTableVar1 = 1
        else:
            MainGuiWindow.PageLayoutRemoveTableVar1 = 0

        if self.checkbox165.isChecked():
            MainGuiWindow.PageLayoutRemoveWatermarkVar1 = 1
        else:
            MainGuiWindow.PageLayoutRemoveWatermarkVar1 = 0

        if self.checkbox166.isChecked():
            MainGuiWindow.PageLayoutRemoveUnderlineVar1 = 1
        else:
            MainGuiWindow.PageLayoutRemoveUnderlineVar1 = 0

        if self.checkbox167.isChecked():
            MainGuiWindow.PageLayoutRemoveSpaceVar1 = 1
        else:
            MainGuiWindow.PageLayoutRemoveSpaceVar1 = 0

        if self.checkbox168.isChecked():
            MainGuiWindow.PageLayoutRemoveLineVar1 = 1
        else:
            MainGuiWindow.PageLayoutRemoveLineVar1 = 0

        if self.radioButton14a.isChecked() == True:
            MainGuiWindow.OutputFormatVar1 = 0             # Text
        if self.radioButton14b.isChecked() == True:
            MainGuiWindow.OutputFormatVar1 = 1             # PDF
        if self.radioButton14c.isChecked() == True:
            MainGuiWindow.OutputFormatVar1 = 2             # Spreadsheet

        if self.radioButton15a.isChecked() == True:
            MainGuiWindow.OptimizationVar1 = 0             # Standard
        if self.radioButton15b.isChecked() == True:
            MainGuiWindow.OptimizationVar1 = 1             # Speed
        if self.radioButton15c.isChecked() == True:
            MainGuiWindow.OptimizationVar1 = 2             # Accuracy

        if self.checkbox35.isChecked():
            MainGuiWindow.LayoutDespeckleVar1 = 1
        else:
            MainGuiWindow.LayoutDespeckleVar1 = 0

        if self.checkbox36.isChecked():
            MainGuiWindow.LayoutThresholdVar1 = 1
        else:
            MainGuiWindow.LayoutThresholdVar1 = 0

        if self.checkbox37.isChecked():
            MainGuiWindow.LayoutInvertColorVar1 = 1
        else:
            MainGuiWindow.LayoutInvertColorVar1 = 0

        if self.checkbox38.isChecked():
            MainGuiWindow.LayoutThresholdAdaptiveVar1 = 1
        else:
            MainGuiWindow.LayoutThresholdAdaptiveVar1 = 0

        if self.checkbox39.isChecked():
            MainGuiWindow.LayoutSharpenVar1 = 1
        else:
            MainGuiWindow.LayoutSharpenVar1 = 0

        if self.checkbox310.isChecked():
            MainGuiWindow.LayoutContrastVar1 = 1
        else:
            MainGuiWindow.LayoutContrastVar1 = 0


    # page2-2
# //===========================================//
        if self.checkbox311.isChecked():
            MainGuiWindow.FilteringBackgroundNoiseVar1 = 1
        else:
            MainGuiWindow.FilteringBackgroundNoiseVar1 = 0
        MainGuiWindow.FilteringBackgroundNoiseIntVar1 = (4*self.slider311.value())+3       # [3,7,11,15,19]

        if self.checkbox312.isChecked():
            MainGuiWindow.FilteringTextNoiseVar1 = 1
        else:
            MainGuiWindow.FilteringTextNoiseVar1 = 0
        MainGuiWindow.FilteringTextNoiseIntVar1 = (self.slider312.value())+2               # [2,3,4,5,6]

        if self.checkbox313.isChecked():
            MainGuiWindow.FilteringTextErosionVar1 = 1
        else:
            MainGuiWindow.FilteringTextErosionVar1 = 0
        MainGuiWindow.FilteringTextErosionIntVar1 = (self.slider313.value())+2             # [2,3,4,5,6]

        if self.checkbox314.isChecked():
            MainGuiWindow.FilteringTextDilationVar1 = 1
        else:
            MainGuiWindow.FilteringTextDilationVar1 = 0
        MainGuiWindow.FilteringTextDilationIntVar1 = (self.slider314.value())+2            # [2,3,4,5,6]

        if self.checkbox315.isChecked():
            MainGuiWindow.FilteringThresholdVar1 = 1
        else:
            MainGuiWindow.FilteringThresholdVar1 = 0
        MainGuiWindow.FilteringThresholdLowerIntVar1 = (self.slider315a.value())           # [0-255]
        MainGuiWindow.FilteringThresholdUpperIntVar1 = (self.slider315b.value())           # [0-255]


        if self.checkbox321.isChecked():
            MainGuiWindow.DisplayColorImageVar1 = 1
        else:
            MainGuiWindow.DisplayColorImageVar1 = 0

        if self.checkbox322.isChecked():
            MainGuiWindow.DisplayGrayImageVar1 = 1
        else:
            MainGuiWindow.DisplayGrayImageVar1 = 0

        if self.checkbox323.isChecked():
            MainGuiWindow.DisplayProcessedImageVar1 = 1
        else:
            MainGuiWindow.DisplayProcessedImageVar1 = 0

        if self.checkbox324.isChecked():
            MainGuiWindow.DisplayProcessedAllImageVar1 = 1
        else:
            MainGuiWindow.DisplayProcessedAllImageVar1 = 0


    # page3
# //===========================================//
        if self.checkbox41.isChecked():
            MainGuiWindow.WhitelistVar1 = 1
        else:
            MainGuiWindow.WhitelistVar1 = 0

        if self.checkbox41a.isChecked():
            MainGuiWindow.Whitelist1Var1 = 1
        else:
            MainGuiWindow.Whitelist1Var1 = 0

        if self.checkbox41b.isChecked():
            MainGuiWindow.Whitelist2Var1 = 1
        else:
            MainGuiWindow.Whitelist2Var1 = 0

        if self.checkbox41c.isChecked():
            MainGuiWindow.Whitelist3Var1 = 1
        else:
            MainGuiWindow.Whitelist3Var1 = 0

        if self.checkbox41d.isChecked():
            MainGuiWindow.Whitelist4Var1 = 1
        else:
            MainGuiWindow.Whitelist4Var1 = 0

        if self.checkbox41e.isChecked():
            MainGuiWindow.Whitelist5Var1 = 1
        else:
            MainGuiWindow.Whitelist5Var1 = 0
        MainGuiWindow.WhitelistCharVar1 = self.textbox_whitelist.toPlainText()

        if self.checkbox42.isChecked():
            MainGuiWindow.BlacklistVar1 = 1
        else:
            MainGuiWindow.BlacklistVar1 = 0

        if self.checkbox42a.isChecked():
            MainGuiWindow.Blacklist1Var1 = 1
        else:
            MainGuiWindow.Blacklist1Var1 = 0

        if self.checkbox42b.isChecked():
            MainGuiWindow.Blacklist2Var1 = 1
        else:
            MainGuiWindow.Blacklist2Var1 = 0

        if self.checkbox42c.isChecked():
            MainGuiWindow.Blacklist3Var1 = 1
        else:
            MainGuiWindow.Blacklist3Var1 = 0

        if self.checkbox42d.isChecked():
            MainGuiWindow.Blacklist4Var1 = 1
        else:
            MainGuiWindow.Blacklist4Var1 = 0

        if self.checkbox42e.isChecked():
            MainGuiWindow.Blacklist5Var1 = 1
        else:
            MainGuiWindow.Blacklist5Var1 = 0
        MainGuiWindow.BlacklistCharVar1 = self.textbox_blacklist.toPlainText()


    #page5
# //===========================================//
        if (self.comboBox5.currentIndex() == 0):
            MainGuiWindow.ThemeLightColorVar1 = 0
        elif (self.comboBox5.currentIndex() == 1):
            MainGuiWindow.ThemeLightColorVar1 = 1
        elif (self.comboBox5.currentIndex() == 2):
            MainGuiWindow.ThemeLightColorVar1 = 2
        elif (self.comboBox5.currentIndex() == 3):
            MainGuiWindow.ThemeLightColorVar1 = 3
        elif (self.comboBox5.currentIndex() == 4):
            MainGuiWindow.ThemeLightColorVar1 = 4
        elif (self.comboBox5.currentIndex() == 5):
            MainGuiWindow.ThemeLightColorVar1 = 5
        elif (self.comboBox5.currentIndex() == 6):
            MainGuiWindow.ThemeLightColorVar1 = 6

        if (self.comboBox6.currentIndex() == 0):
            MainGuiWindow.ThemeDarkColorVar1 = 0
        elif (self.comboBox6.currentIndex() == 1):
            MainGuiWindow.ThemeDarkColorVar1 = 1
        elif (self.comboBox6.currentIndex() == 2):
            MainGuiWindow.ThemeDarkColorVar1 = 2
        elif (self.comboBox6.currentIndex() == 3):
            MainGuiWindow.ThemeDarkColorVar1 = 3
        elif (self.comboBox6.currentIndex() == 4):
            MainGuiWindow.ThemeDarkColorVar1 = 4
        elif (self.comboBox6.currentIndex() == 5):
            MainGuiWindow.ThemeDarkColorVar1 = 5
        elif (self.comboBox6.currentIndex() == 6):
            MainGuiWindow.ThemeDarkColorVar1 = 6

        if (self.comboBox7.currentIndex() == 0):            # Default (Cross)
            MainGuiWindow.CursorShapeVar1 = 0
        elif (self.comboBox7.currentIndex() == 1):          # Arrow
            MainGuiWindow.CursorShapeVar1 = 1
        elif (self.comboBox7.currentIndex() == 2):          # Target
            MainGuiWindow.CursorShapeVar1 = 2
        elif (self.comboBox7.currentIndex() == 3):          # Pointer
            MainGuiWindow.CursorShapeVar1 = 3
        elif (self.comboBox7.currentIndex() == 4):          # Pointing Hand
            MainGuiWindow.CursorShapeVar1 = 4

        if (self.slider531.value() == 0):
            MainGuiWindow.RBBThicknessVar1 = 0
        elif (self.slider531.value() == 1):
            MainGuiWindow.RBBThicknessVar1 = 2
        elif (self.slider531.value() == 2):
            MainGuiWindow.RBBThicknessVar1 = 6
        elif (self.slider531.value() == 3):
            MainGuiWindow.RBBThicknessVar1 = 8
        elif (self.slider531.value() == 4):
            MainGuiWindow.RBBThicknessVar1 = 12
        MainGuiWindow.RBBOpacityVar1 = int(50*self.slider532.value())


    # page6
    # //===========================================//
        if (self.comboBox8.currentIndex() == 0):            # Small
            MainGuiWindow.FontSystemSizeVar1 = 7
        elif (self.comboBox8.currentIndex() == 1):          # Default
            MainGuiWindow.FontSystemSizeVar1 = 8
        elif (self.comboBox8.currentIndex() == 2):          # Large
            MainGuiWindow.FontSystemSizeVar1 = 9

        if (self.comboBox9.currentIndex() == 0):            # Classic
            MainGuiWindow.BorderStyleVar1 = 0
        elif (self.comboBox9.currentIndex() == 1):          # Default
            MainGuiWindow.BorderStyleVar1 = 1

        if (self.comboBox11.currentIndex() == 0):            # Small
            MainGuiWindow.TextEditorIconSizeVar1 = 16
        elif (self.comboBox11.currentIndex() == 1):          # Default
            MainGuiWindow.TextEditorIconSizeVar1 = 18
        elif (self.comboBox11.currentIndex() == 2):          # Large
            MainGuiWindow.TextEditorIconSizeVar1 = 22

        if (self.comboBox12.currentIndex() == 0):            # Default
            MainGuiWindow.TextEditorStatusBarVar1 = 0
        elif (self.comboBox12.currentIndex() == 1):          # No Message
            MainGuiWindow.TextEditorStatusBarVar1 = 1

        if (self.comboBox13.currentIndex() == 0):            # Default
            MainGuiWindow.TextEditorModeVar1 = 0
        elif (self.comboBox13.currentIndex() == 1):          # Separated
            MainGuiWindow.TextEditorModeVar1 = 1

        if self.checkbox62.isChecked():
            MainGuiWindow.SystemTrayIconVar1 = 1
        else:
            MainGuiWindow.SystemTrayIconVar1 = 0

        from src.module.py_window_main import MainGuiWindow

        MainGuiWindow.setFlagOCR(self)
        MainGuiWindow.setRubberBandThicknessOpacity(self)
        MainGuiWindow.setCursorShape(self)
        MainGuiWindow.settingAction.setEnabled(True)

        from src.func.py_main_editor import TextGuiWindow
        try:
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

        self.SaveConfigFile_Setting()
        self.close()
        print('---------------------')











# //===========================================//
    def CancelSetting(self):
        from src.func.py_main_editor import TextGuiWindow
        # global flag_config_init

        print('=== CancelSetting ===')
        from src.module.py_window_main import MainGuiWindow
        from src.func.py_main_editor import TextGuiWindow

        try:
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

        self.LoadConfig()

        from src.module.py_window_main import MainGuiWindow
        self.comboBox5.setCurrentIndex(int(Temp_ThemeLightColorVar))
        self.comboBox6.setCurrentIndex(int(Temp_ThemeDarkColorVar))
        MainGuiWindow.ThemeLightColorVar1 = Temp_ThemeLightColorVar
        MainGuiWindow.ThemeLightColorVar1 = Temp_ThemeDarkColorVar
        MainGuiWindow.settingAction.setEnabled(True)

        try:
            if (MainGuiWindow.THEME == 'light'):
                MainGuiWindow.THEME_LIGHT = Theme_light_temp
                MainGuiWindow.ThemeLightColorVar1 = ThemeLightColorVar1_temp
                MainGuiWindow.FONT_COLOR_LIGHT_CUSTOM = Color_font_light_temp
                MainGuiWindow.TB_COLOR_LIGHT_CUSTOM = Color_TB_light_temp
                MainGuiWindow.FG_COLOR_LIGHT_CUSTOM = Color_FG_light_temp
                MainGuiWindow.BG_COLOR_LIGHT_CUSTOM = Color_BG_light_temp
                MainGuiWindow.BT_COLOR_LIGHT_CUSTOM = Color_BT_light_temp
                MainGuiWindow.BD_COLOR_LIGHT_CUSTOM = Color_BD_light_temp
                self.update_combobox5()

            elif (MainGuiWindow.THEME == 'dark'):
                MainGuiWindow.THEME_DARK = Theme_dark_temp
                MainGuiWindow.ThemeDarkColorVar1 = ThemeDarkColorVar1_temp
                MainGuiWindow.FONT_COLOR_DARK_CUSTOM = Color_font_dark_temp
                MainGuiWindow.TB_COLOR_DARK_CUSTOM = Color_TB_dark_temp
                MainGuiWindow.FG_COLOR_DARK_CUSTOM = Color_FG_dark_temp
                MainGuiWindow.BG_COLOR_DARK_CUSTOM = Color_BG_dark_temp
                MainGuiWindow.BT_COLOR_DARK_CUSTOM = Color_BT_dark_temp
                MainGuiWindow.BD_COLOR_DARK_CUSTOM = Color_BD_dark_temp
                self.update_combobox6()

            MainGuiWindow.FontSystemSizeVar1 = FontSystemSizeVar1_temp
            if (FontSystemSizeVar1_temp == 7):
                self.comboBox8.setCurrentIndex(0)
            elif (FontSystemSizeVar1_temp == 8):
                self.comboBox8.setCurrentIndex(1)
            elif (FontSystemSizeVar1_temp == 9):
                self.comboBox8.setCurrentIndex(2)
            self.update_combobox8()

            MainGuiWindow.BorderStyleVar1 = BorderStyleVar1_temp
            self.comboBox9.setCurrentIndex(int(BorderStyleVar1_temp))
            self.update_combobox9()

            MainGuiWindow.TextEditorIconSizeVar1 = TextEditorIconSizeVar1_temp
            if (TextEditorIconSizeVar1_temp == 16):
                self.comboBox11.setCurrentIndex(0)
            elif (TextEditorIconSizeVar1_temp == 18):
                self.comboBox11.setCurrentIndex(1)
            elif (TextEditorIconSizeVar1_temp == 22):
                self.comboBox11.setCurrentIndex(2)
            self.update_combobox11()

            MainGuiWindow.TextEditorStatusBarVar1 = TextEditorStatusBarVar1_temp
            self.comboBox12.setCurrentIndex(int(TextEditorStatusBarVar1_temp))
            self.update_combobox12()
            MainGuiWindow.RBBColorVar1 = RBBColorVar1_temp
            MainGuiWindow.setRubberBandColor(self)
        except:
            pass

        self.SaveConfigFile_Setting()
        self.close()
        print('---------------------')





# //===========================================//
    def encode_Setting(self):
        global LanguageVar
        global LanguageVarEnc, LanguageSystemVarEnc, MathEquationVarEnc, TextLayoutVarEnc
        global ThemeLightColorTBVar, ThemeLightColorFGVar, ThemeLightColorBGVar, ThemeLightColorFontVar, ThemeLightColorBTVar, ThemeLightColorBDVar
        global ThemeLightColorTBVarEnc, ThemeLightColorFGVarEnc, ThemeLightColorBGVarEnc, ThemeLightColorFontVarEnc, ThemeLightColorBTVarEnc, ThemeLightColorBDVarEnc
        global ThemeDarkColorTBVar, ThemeDarkColorFGVar, ThemeDarkColorBGVar, ThemeDarkColorFontVar, ThemeDarkColorBTVar, ThemeDarkColorBDVar
        global ThemeDarkColorTBVarEnc, ThemeDarkColorFGVarEnc, ThemeDarkColorBGVarEnc, ThemeDarkColorFontVarEnc, ThemeDarkColorBTVarEnc, ThemeDarkColorBDVarEnc
        global RBBColorVar, RBBColorVarEnc
        global DetectedTextVarEnc, DetectedTextLetterVarEnc, DetectedTextLowerVarEnc, DetectedTextUpperVarEnc, DetectedTextNumberVarEnc, DetectedTextPuncVarEnc, DetectedTextMiscVarEnc
        global OutputFormatVarEnc, OptimizationVarEnc
        global PageLayoutAutoRotatePageVarEnc, PageLayoutDeskewVarEnc, PageLayoutDecolumnizeVarEnc, PageLayoutRemoveTableVarEnc
        global PageLayoutRemoveWatermarkVarEnc, PageLayoutRemoveUnderlineVarEnc, PageLayoutRemoveSpaceVarEnc, PageLayoutRemoveLineVarEnc
        global LayoutDespeckleVarEnc, LayoutThresholdVarEnc, LayoutInvertColorVarEnc, LayoutThresholdAdaptiveVarEnc, LayoutSharpenVarEnc, LayoutContrastVarEnc
        global FilteringBackgroundNoiseVarEnc, FilteringBackgroundNoiseIntVarEnc, FilteringTextNoiseVarEnc, FilteringTextNoiseIntVarEnc
        global FilteringTextErosionVarEnc, FilteringTextErosionIntVarEnc, FilteringTextDilationVarEnc, FilteringTextDilationIntVarEnc
        global FilteringThresholdVarEnc, FilteringThresholdLowerIntVarEnc, FilteringThresholdLowerIntVar, FilteringThresholdUpperIntVarEnc, FilteringThresholdUpperIntVar
        global DisplayColorImageVarEnc, DisplayGrayImageVarEnc, DisplayProcessedImageVarEnc, DisplayProcessedAllImageVarEnc
        global WhitelistVarEnc, Whitelist1VarEnc, Whitelist2VarEnc, Whitelist3VarEnc, Whitelist4VarEnc, Whitelist5VarEnc, WhitelistCharVar
        global BlacklistVarEnc, Blacklist1VarEnc, Blacklist2VarEnc, Blacklist3VarEnc, Blacklist4VarEnc, Blacklist5VarEnc, BlacklistCharVar
        global ThemeLightColorVarEnc, ThemeDarkColorVarEnc
        global CursorShapeVarEnc, RBBThicknessVarEnc, RBBOpacityVarEnc
        global FontSystemSizeVarEnc, BorderStyleVarEnc, TextEditorIconSizeVarEnc, TextEditorStatusBarVarEnc, TextEditorModeVarEnc, SystemTrayIconVarEnc

        print('=== encode_Setting ===')
        if (LanguageSystemVar == 0):
            LanguageSystemVarEnc = '10010'
        elif (LanguageSystemVar == 1):
            LanguageSystemVarEnc = '10110'

        if (MathEquationVar == 0):
            MathEquationVarEnc = '01011'
        elif (MathEquationVar == 1):
            MathEquationVarEnc = '11100'

        if (TextLayoutVar == 0):
            TextLayoutVarEnc = '01001'
        elif (TextLayoutVar == 1):
            TextLayoutVarEnc = '01101'
        elif (TextLayoutVar == 2):
            TextLayoutVarEnc = '00110'
        elif (TextLayoutVar == 3):
            TextLayoutVarEnc = '10101'
        elif (TextLayoutVar == 4):
            TextLayoutVarEnc = '11000'
        elif (TextLayoutVar == 5):
            TextLayoutVarEnc = '11001'
        elif (TextLayoutVar == 6):
            TextLayoutVarEnc = '10010'
        elif (TextLayoutVar == 7):
            TextLayoutVarEnc = '00011'

        if (DetectedTextVar == 0):
            DetectedTextVarEnc = '11011'
        elif (DetectedTextVar == 1):
            DetectedTextVarEnc = '00101'

        if (DetectedTextLetterVar == 0):
            DetectedTextLetterVarEnc = '00110'
        elif (DetectedTextLetterVar == 1):
            DetectedTextLetterVarEnc = '00101'

        if (DetectedTextLowerVar == 0):
            DetectedTextLowerVarEnc = '10100'
        elif (DetectedTextLowerVar == 1):
            DetectedTextLowerVarEnc = '11001'

        if (DetectedTextUpperVar == 0):
            DetectedTextUpperVarEnc = '11101'
        elif (DetectedTextUpperVar == 1):
            DetectedTextUpperVarEnc = '01001'

        if (DetectedTextNumberVar == 0):
            DetectedTextNumberVarEnc = '01100'
        elif (DetectedTextNumberVar == 1):
            DetectedTextNumberVarEnc = '10110'

        if (DetectedTextPuncVar == 0):
            DetectedTextPuncVarEnc = '11011'
        elif (DetectedTextPuncVar == 1):
            DetectedTextPuncVarEnc = '10110'

        if (DetectedTextMiscVar == 0):
            DetectedTextMiscVarEnc = '01100'
        elif (DetectedTextMiscVar == 1):
            DetectedTextMiscVarEnc = '01001'

        if (OutputFormatVar == 0):
            OutputFormatVarEnc = '11101'
        elif (OutputFormatVar == 1):
            OutputFormatVarEnc = '11010'
        elif (OutputFormatVar == 2):
            OutputFormatVarEnc = '10111'

        if (OptimizationVar == 0):
            OptimizationVarEnc = '01001'
        elif (OptimizationVar == 1):
            OptimizationVarEnc = '01110'
        elif (OptimizationVar == 2):
            OptimizationVarEnc = '01010'

        if (PageLayoutAutoRotatePageVar == 0):
            PageLayoutAutoRotatePageVarEnc = '01011'
        elif (PageLayoutAutoRotatePageVar == 1):
            PageLayoutAutoRotatePageVarEnc = '10110'

        if (PageLayoutDeskewVar == 0):
            PageLayoutDeskewVarEnc = '10010'
        elif (PageLayoutDeskewVar == 1):
            PageLayoutDeskewVarEnc = '11011'

        if (PageLayoutDecolumnizeVar == 0):
            PageLayoutDecolumnizeVarEnc = '11001'
        elif (PageLayoutDecolumnizeVar == 1):
            PageLayoutDecolumnizeVarEnc = '01011'

        if (PageLayoutRemoveTableVar == 0):
            PageLayoutRemoveTableVarEnc = '01100'
        elif (PageLayoutRemoveTableVar == 1):
            PageLayoutRemoveTableVarEnc = '01010'

        if (PageLayoutRemoveWatermarkVar == 0):
            PageLayoutRemoveWatermarkVarEnc = '11011'
        elif (PageLayoutRemoveWatermarkVar == 1):
            PageLayoutRemoveWatermarkVarEnc = '10110'

        if (PageLayoutRemoveUnderlineVar == 0):
            PageLayoutRemoveUnderlineVarEnc = '01011'
        elif (PageLayoutRemoveUnderlineVar == 1):
            PageLayoutRemoveUnderlineVarEnc = '10011'

        if (PageLayoutRemoveSpaceVar == 0):
            PageLayoutRemoveSpaceVarEnc = '11011'
        elif (PageLayoutRemoveSpaceVar == 1):
            PageLayoutRemoveSpaceVarEnc = '11010'

        if (PageLayoutRemoveLineVar == 0):
            PageLayoutRemoveLineVarEnc = '11001'
        elif (PageLayoutRemoveLineVar == 1):
            PageLayoutRemoveLineVarEnc = '01110'

        if (LayoutDespeckleVar == 0):
            LayoutDespeckleVarEnc = '00100'
        elif (LayoutDespeckleVar == 1):
            LayoutDespeckleVarEnc = '11010'

        if (LayoutThresholdVar == 0):
            LayoutThresholdVarEnc = '01010'
        elif (LayoutThresholdVar == 1):
            LayoutThresholdVarEnc = '01110'

        if (LayoutInvertColorVar == 0):
            LayoutInvertColorVarEnc = '10100'
        elif (LayoutInvertColorVar == 1):
            LayoutInvertColorVarEnc = '11101'

        if (LayoutThresholdAdaptiveVar == 0):
            LayoutThresholdAdaptiveVarEnc = '11001'
        elif (LayoutThresholdAdaptiveVar == 1):
            LayoutThresholdAdaptiveVarEnc = '01101'

        if (LayoutSharpenVar == 0):
            LayoutSharpenVarEnc = '01010'
        elif (LayoutSharpenVar == 1):
            LayoutSharpenVarEnc = '11001'

        if (LayoutContrastVar == 0):
            LayoutContrastVarEnc = '00110'
        elif (LayoutContrastVar == 1):
            LayoutContrastVarEnc = '11101'

        if (FilteringBackgroundNoiseVar == 0):
            FilteringBackgroundNoiseVarEnc = '11011'
        elif (FilteringBackgroundNoiseVar == 1):
            FilteringBackgroundNoiseVarEnc = '10110'

        if (FilteringBackgroundNoiseIntVar == 3):
            FilteringBackgroundNoiseIntVarEnc = '01101'
        elif (FilteringBackgroundNoiseIntVar == 7):
            FilteringBackgroundNoiseIntVarEnc = '01110'
        elif (FilteringBackgroundNoiseIntVar == 11):
            FilteringBackgroundNoiseIntVarEnc = '11100'
        elif (FilteringBackgroundNoiseIntVar == 15):
            FilteringBackgroundNoiseIntVarEnc = '11001'
        elif (FilteringBackgroundNoiseIntVar == 19):
            FilteringBackgroundNoiseIntVarEnc = '01100'

        if (FilteringTextNoiseVar == 0):
            FilteringTextNoiseVarEnc = '11100'
        elif (FilteringTextNoiseVar == 1):
            FilteringTextNoiseVarEnc = '01101'

        if (FilteringTextNoiseIntVar == 2):
            FilteringTextNoiseIntVarEnc = '11001'
        elif (FilteringTextNoiseIntVar == 3):
            FilteringTextNoiseIntVarEnc = '01101'
        elif (FilteringTextNoiseIntVar == 4):
            FilteringTextNoiseIntVarEnc = '11100'
        elif (FilteringTextNoiseIntVar == 5):
            FilteringTextNoiseIntVarEnc = '01110'
        elif (FilteringTextNoiseIntVar == 6):
            FilteringTextNoiseIntVarEnc = '10111'

        if (FilteringTextErosionVar == 0):
            FilteringTextErosionVarEnc = '01101'
        elif (FilteringTextErosionVar == 1):
            FilteringTextErosionVarEnc = '10110'

        if (FilteringTextErosionIntVar == 2):
            FilteringTextErosionIntVarEnc = '10100'
        elif (FilteringTextErosionIntVar == 3):
            FilteringTextErosionIntVarEnc = '11011'
        elif (FilteringTextErosionIntVar == 4):
            FilteringTextErosionIntVarEnc = '01110'
        elif (FilteringTextErosionIntVar == 5):
            FilteringTextErosionIntVarEnc = '01101'
        elif (FilteringTextErosionIntVar == 6):
            FilteringTextErosionIntVarEnc = '10111'

        if (FilteringTextDilationVar == 0):
            FilteringTextDilationVarEnc = '10110'
        elif (FilteringTextDilationVar == 1):
            FilteringTextDilationVarEnc = '10011'

        if (FilteringTextDilationIntVar == 2):
            FilteringTextDilationIntVarEnc = '10010'
        elif (FilteringTextDilationIntVar == 3):
            FilteringTextDilationIntVarEnc = '00100'
        elif (FilteringTextDilationIntVar == 4):
            FilteringTextDilationIntVarEnc = '10111'
        elif (FilteringTextDilationIntVar == 5):
            FilteringTextDilationIntVarEnc = '01100'
        elif (FilteringTextDilationIntVar == 6):
            FilteringTextDilationIntVarEnc = '01110'

        if (FilteringThresholdVar == 0):
            FilteringThresholdVarEnc = '01010'
        elif (FilteringThresholdVar == 1):
            FilteringThresholdVarEnc = '10100'

        if (DisplayColorImageVar == 0):
            DisplayColorImageVarEnc = '11001'
        elif (DisplayColorImageVar == 1):
            DisplayColorImageVarEnc = '10100'

        if (DisplayGrayImageVar == 0):
            DisplayGrayImageVarEnc = '10110'
        elif (DisplayGrayImageVar == 1):
            DisplayGrayImageVarEnc = '11100'

        if (DisplayProcessedImageVar == 0):
            DisplayProcessedImageVarEnc = '01010'
        elif (DisplayProcessedImageVar == 1):
            DisplayProcessedImageVarEnc = '00111'

        if (DisplayProcessedAllImageVar == 0):
            DisplayProcessedAllImageVarEnc = '10100'
        elif (DisplayProcessedAllImageVar == 1):
            DisplayProcessedAllImageVarEnc = '01011'

        if (WhitelistVar == 0):
            WhitelistVarEnc = '11100'
        elif (WhitelistVar == 1):
            WhitelistVarEnc = '10100'

        if (Whitelist1Var == 0):
            Whitelist1VarEnc = '01110'
        elif (Whitelist1Var == 1):
            Whitelist1VarEnc = '01101'

        if (Whitelist2Var == 0):
            Whitelist2VarEnc = '01101'
        elif (Whitelist2Var == 1):
            Whitelist2VarEnc = '01110'

        if (Whitelist3Var == 0):
            Whitelist3VarEnc = '11010'
        elif (Whitelist3Var == 1):
            Whitelist3VarEnc = '10111'

        if (Whitelist4Var == 0):
            Whitelist4VarEnc = '10100'
        elif (Whitelist4Var == 1):
            Whitelist4VarEnc = '01110'

        if (Whitelist5Var == 0):
            Whitelist5VarEnc = '10110'
        elif (Whitelist5Var == 1):
            Whitelist5VarEnc = '01011'

        if (BlacklistVar == 0):
            BlacklistVarEnc = '11001'
        elif (BlacklistVar == 1):
            BlacklistVarEnc = '01001'

        if (Blacklist1Var == 0):
            Blacklist1VarEnc = '01110'
        elif (Blacklist1Var == 1):
            Blacklist1VarEnc = '11011'

        if (Blacklist2Var == 0):
            Blacklist2VarEnc = '11011'
        elif (Blacklist2Var == 1):
            Blacklist2VarEnc = '11011'

        if (Blacklist3Var == 0):
            Blacklist3VarEnc = '01101'
        elif (Blacklist3Var == 1):
            Blacklist3VarEnc = '10110'

        if (Blacklist4Var == 0):
            Blacklist4VarEnc = '10100'
        elif (Blacklist4Var == 1):
            Blacklist4VarEnc = '11101'

        if (Blacklist5Var == 0):
            Blacklist5VarEnc = '10100'
        elif (Blacklist5Var == 1):
            Blacklist5VarEnc = '10101'

        if (ThemeLightColorVar == 0):
            ThemeLightColorVarEnc = '10100'
        elif (ThemeLightColorVar == 1):
            ThemeLightColorVarEnc = '01011'
        elif (ThemeLightColorVar == 2):
            ThemeLightColorVarEnc = '01101'
        elif (ThemeLightColorVar == 3):
            ThemeLightColorVarEnc = '11010'
        elif (ThemeLightColorVar == 4):
            ThemeLightColorVarEnc = '11001'
        elif (ThemeLightColorVar == 5):
            ThemeLightColorVarEnc = '10011'
        elif (ThemeLightColorVar == 6):
            ThemeLightColorVarEnc = '01101'

        if (ThemeDarkColorVar == 0):
            ThemeDarkColorVarEnc = '10011'
        elif (ThemeDarkColorVar == 1):
            ThemeDarkColorVarEnc = '11001'
        elif (ThemeDarkColorVar == 2):
            ThemeDarkColorVarEnc = '11100'
        elif (ThemeDarkColorVar == 3):
            ThemeDarkColorVarEnc = '01011'
        elif (ThemeDarkColorVar == 4):
            ThemeDarkColorVarEnc = '00110'
        elif (ThemeDarkColorVar == 5):
            ThemeDarkColorVarEnc = '11011'
        elif (ThemeDarkColorVar == 6):
            ThemeDarkColorVarEnc = '01001'

        if (CursorShapeVar == 0):
            CursorShapeVarEnc = '11001'
        elif (CursorShapeVar == 1):
            CursorShapeVarEnc = '10110'
        elif (CursorShapeVar == 2):
            CursorShapeVarEnc = '01101'
        elif (CursorShapeVar == 3):
            CursorShapeVarEnc = '01110'
        elif (CursorShapeVar == 4):
            CursorShapeVarEnc = '10011'

        if (RBBThicknessVar == 0):
            RBBThicknessVarEnc = '11100'
        elif (RBBThicknessVar == 2):
            RBBThicknessVarEnc = '10100'
        elif (RBBThicknessVar == 6):
            RBBThicknessVarEnc = '10101'
        elif (RBBThicknessVar == 8):
            RBBThicknessVarEnc = '01111'
        elif (RBBThicknessVar == 12):
            RBBThicknessVarEnc = '10111'

        if (RBBOpacityVar == 0):
            RBBOpacityVarEnc = '01110'
        elif (RBBOpacityVar == 50):
            RBBOpacityVarEnc = '11100'
        elif (RBBOpacityVar == 100):
            RBBOpacityVarEnc = '01111'
        elif (RBBOpacityVar == 150):
            RBBOpacityVarEnc = '11001'
        elif (RBBOpacityVar == 200):
            RBBOpacityVarEnc = '11101'

        if (FontSystemSizeVar == 7):
            FontSystemSizeVarEnc = '00111'
        elif (FontSystemSizeVar == 8):
            FontSystemSizeVarEnc = '11001'
        elif (FontSystemSizeVar == 9):
            FontSystemSizeVarEnc = '01101'

        if (BorderStyleVar == 0):
            BorderStyleVarEnc = '11011'
        elif (BorderStyleVar == 1):
            BorderStyleVarEnc = '01100'

        if (TextEditorIconSizeVar == 16):
            TextEditorIconSizeVarEnc = '10110'
        elif (TextEditorIconSizeVar == 18):
            TextEditorIconSizeVarEnc = '11000'
        elif (TextEditorIconSizeVar == 22):
            TextEditorIconSizeVarEnc = '11111'

        if (TextEditorStatusBarVar == 0):
            TextEditorStatusBarVarEnc = '01110'
        elif (TextEditorStatusBarVar == 1):
            TextEditorStatusBarVarEnc = '00011'

        if (TextEditorModeVar == 0):
            TextEditorModeVarEnc = '10110'
        elif (TextEditorModeVar == 1):
            TextEditorModeVarEnc = '11101'

        if (SystemTrayIconVar == 0):
            SystemTrayIconVarEnc = '01101'
        elif (SystemTrayIconVar == 1):
            SystemTrayIconVarEnc = '11101'

        FilteringThresholdLowerIntVar = str(FilteringThresholdLowerIntVar)
        FilteringThresholdLowerIntVarEnc = ''
        for i in FilteringThresholdLowerIntVar:
            FilteringThresholdLowerIntVarEnc = FilteringThresholdLowerIntVarEnc + format(int(i,16),"04b")

        FilteringThresholdUpperIntVar = str(FilteringThresholdUpperIntVar)
        FilteringThresholdUpperIntVarEnc = ''
        for i in FilteringThresholdUpperIntVar:
            FilteringThresholdUpperIntVarEnc = FilteringThresholdUpperIntVarEnc + format(int(i,16),"04b")

        ThemeLightColorTBVar = str(ThemeLightColorTBVar).replace('#','')
        ThemeLightColorTBVarEnc = ''
        for i in ThemeLightColorTBVar:
            ThemeLightColorTBVarEnc = ThemeLightColorTBVarEnc + format(int(i,16),"04b")

        ThemeLightColorFGVar = str(ThemeLightColorFGVar).replace('#','')
        ThemeLightColorFGVarEnc = ''
        for i in ThemeLightColorFGVar:
            ThemeLightColorFGVarEnc = ThemeLightColorFGVarEnc + format(int(i,16),"04b")

        ThemeLightColorBGVar = str(ThemeLightColorBGVar).replace('#','')
        ThemeLightColorBGVarEnc = ''
        for i in ThemeLightColorBGVar:
            ThemeLightColorBGVarEnc = ThemeLightColorBGVarEnc + format(int(i,16),"04b")

        ThemeLightColorFontVar = str(ThemeLightColorFontVar).replace('#','')
        ThemeLightColorFontVarEnc = ''
        for i in ThemeLightColorFontVar:
            ThemeLightColorFontVarEnc = ThemeLightColorFontVarEnc + format(int(i,16),"04b")

        ThemeLightColorBTVar = str(ThemeLightColorBTVar).replace('#','')
        ThemeLightColorBTVarEnc = ''
        for i in ThemeLightColorBTVar:
            ThemeLightColorBTVarEnc = ThemeLightColorBTVarEnc + format(int(i,16),"04b")

        ThemeLightColorBDVar = str(ThemeLightColorBDVar).replace('#','')
        ThemeLightColorBDVarEnc = ''
        for i in ThemeLightColorBDVar:
            ThemeLightColorBDVarEnc = ThemeLightColorBDVarEnc + format(int(i,16),"04b")

        ThemeDarkColorTBVar = str(ThemeDarkColorTBVar).replace('#','')
        ThemeDarkColorTBVarEnc = ''
        for i in ThemeDarkColorTBVar:
            ThemeDarkColorTBVarEnc = ThemeDarkColorTBVarEnc + format(int(i,16),"04b")

        ThemeDarkColorFGVar = str(ThemeDarkColorFGVar).replace('#','')
        ThemeDarkColorFGVarEnc = ''
        for i in ThemeDarkColorFGVar:
            ThemeDarkColorFGVarEnc = ThemeDarkColorFGVarEnc + format(int(i,16),"04b")

        ThemeDarkColorBGVar = str(ThemeDarkColorBGVar).replace('#','')
        ThemeDarkColorBGVarEnc = ''
        for i in ThemeDarkColorBGVar:
            ThemeDarkColorBGVarEnc = ThemeDarkColorBGVarEnc + format(int(i,16),"04b")

        ThemeDarkColorFontVar = str(ThemeDarkColorFontVar).replace('#','')
        ThemeDarkColorFontVarEnc = ''
        for i in ThemeDarkColorFontVar:
            ThemeDarkColorFontVarEnc = ThemeDarkColorFontVarEnc + format(int(i,16),"04b")

        ThemeDarkColorBTVar = str(ThemeDarkColorBTVar).replace('#','')
        ThemeDarkColorBTVarEnc = ''
        for i in ThemeDarkColorBTVar:
            ThemeDarkColorBTVarEnc = ThemeDarkColorBTVarEnc + format(int(i,16),"04b")

        ThemeDarkColorBDVar = str(ThemeDarkColorBDVar).replace('#','')
        ThemeDarkColorBDVarEnc = ''
        for i in ThemeDarkColorBDVar:
            ThemeDarkColorBDVarEnc = ThemeDarkColorBDVarEnc + format(int(i,16),"04b")

        RBBColorVar = str(RBBColorVar).replace('#','')
        RBBColorVarEnc = ''
        for i in RBBColorVar:
            RBBColorVarEnc = RBBColorVarEnc + format(int(i,16),"04b")




        LanguageVarEnc = ''
        for i in LanguageVar:
            if (i == '1'):
                LanguageVarEnc = LanguageVarEnc + '111'
            elif (i == '0'):
                LanguageVarEnc = LanguageVarEnc + '110'


# //===========================================//
    def SaveConfigFile_Setting(self):
        # global OCREngineVar, LanguageVar, PageLayoutVar, PageLayoutRemoveWatermarkVar
        global LanguageVar, LanguageSystemVar, MathEquationVar, TextLayoutVar
        global DetectedTextVar, DetectedTextLetterVar, DetectedTextLowerVar, DetectedTextUpperVar, DetectedTextNumberVar, DetectedTextPuncVar, DetectedTextMiscVar
        global PageLayoutAutoRotatePageVar, PageLayoutDeskewVar, PageLayoutDecolumnizeVar, PageLayoutRemoveTableVar
        global PageLayoutRemoveWatermarkVar, PageLayoutRemoveUnderlineVar, PageLayoutRemoveSpaceVar, PageLayoutRemoveLineVar
        global OutputFormatVar, OptimizationVar
        global LayoutDespeckleVar, LayoutThresholdVar, LayoutInvertColorVar, LayoutThresholdAdaptiveVar, LayoutSharpenVar, LayoutContrastVar
        global FilteringBackgroundNoiseVar, FilteringBackgroundNoiseIntVar, FilteringTextNoiseVar, FilteringTextNoiseIntVar
        global FilteringTextErosionVar, FilteringTextErosionIntVar, FilteringTextDilationVar, FilteringTextDilationIntVar
        global FilteringThresholdVar, FilteringThresholdLowerIntVar, FilteringThresholdUpperIntVar
        global DisplayColorImageVar, DisplayGrayImageVar, DisplayProcessedImageVar, DisplayProcessedAllImageVar
        global WhitelistVar, Whitelist1Var, Whitelist2Var, Whitelist3Var, Whitelist4Var, Whitelist5Var, WhitelistCharVar
        global BlacklistVar, Blacklist1Var, Blacklist2Var, Blacklist3Var, Blacklist4Var, Blacklist5Var, BlacklistCharVar
        global ThemeLightColorVar, ThemeLightColorTBVar, ThemeLightColorFGVar, ThemeLightColorBGVar, ThemeLightColorFontVar, ThemeLightColorBTVar, ThemeLightColorBDVar
        global ThemeDarkColorVar, ThemeDarkColorTBVar, ThemeDarkColorFGVar, ThemeDarkColorBGVar, ThemeDarkColorFontVar, ThemeDarkColorBTVar, ThemeDarkColorBDVar
        global CursorShapeVar, RBBThicknessVar, RBBOpacityVar, RBBColorVar
        global FontSystemSizeVar, BorderStyleVar, TextEditorIconSizeVar, TextEditorStatusBarVar, TextEditorModeVar, SystemTrayIconVar

        print('=== SaveConfigFile_Setting ===')





    # page1
# //===========================================//
        LanguageVar = ''
        for i in range(self.comboBox1.count()):
            if (self.comboBox1.model().item(i,0).checkState() == Qt.CheckState.Checked):
                LanguageFlag = '1'
            else:
                LanguageFlag = '0'
            LanguageVar = LanguageVar + ',' + LanguageFlag

        LanguageVar = LanguageVar.replace(',','',1)

        if self.checkbox2.isChecked():
            LanguageSystemVar = 1
        else:
            LanguageSystemVar = 0

        if self.checkbox3.isChecked():
            MathEquationVar = 1
        else:
            MathEquationVar = 0



        if self.radioButton13a.isChecked() == True:
            TextLayoutVar = 0
        if self.radioButton13b.isChecked() == True:
            TextLayoutVar = 1
        if self.radioButton13c.isChecked() == True:
            TextLayoutVar = 2
        if self.radioButton13d.isChecked() == True:
            TextLayoutVar = 3
        if self.radioButton13e.isChecked() == True:
            TextLayoutVar = 4
        if self.radioButton13f.isChecked() == True:
            TextLayoutVar = 5
        if self.radioButton13g.isChecked() == True:
            TextLayoutVar = 6
        if self.radioButton13h.isChecked() == True:
            TextLayoutVar = 7

        if self.radioButton12a.isChecked() == True:
            DetectedTextVar = 0
        if self.radioButton12b.isChecked() == True:
            DetectedTextVar = 1

        if self.checkbox121.isChecked():
            DetectedTextLetterVar = 1
        else:
            DetectedTextLetterVar = 0

        if self.checkbox122.isChecked():
            DetectedTextLowerVar = 1
        else:
            DetectedTextLowerVar = 0

        if self.checkbox123.isChecked():
            DetectedTextUpperVar = 1
        else:
            DetectedTextUpperVar = 0

        if self.checkbox124.isChecked():
            DetectedTextNumberVar = 1
        else:
            DetectedTextNumberVar = 0

        if self.checkbox125.isChecked():
            DetectedTextPuncVar = 1
        else:
            DetectedTextPuncVar = 0

        if self.checkbox126.isChecked():
            DetectedTextMiscVar = 1
        else:
            DetectedTextMiscVar = 0




        if self.checkbox161.isChecked():
            PageLayoutAutoRotatePageVar = 1
        else:
            PageLayoutAutoRotatePageVar = 0

        if self.checkbox162.isChecked():
            PageLayoutDeskewVar = 1
        else:
            PageLayoutDeskewVar = 0

        if self.checkbox163.isChecked():
            PageLayoutDecolumnizeVar = 1
        else:
            PageLayoutDecolumnizeVar = 0

        if self.checkbox164.isChecked():
            PageLayoutRemoveTableVar = 1
        else:
            PageLayoutRemoveTableVar = 0

        if self.checkbox165.isChecked():
            PageLayoutRemoveWatermarkVar = 1
        else:
            PageLayoutRemoveWatermarkVar = 0

        if self.checkbox166.isChecked():
            PageLayoutRemoveUnderlineVar = 1
        else:
            PageLayoutRemoveUnderlineVar = 0

        if self.checkbox167.isChecked():
            PageLayoutRemoveSpaceVar = 1
        else:
            PageLayoutRemoveSpaceVar = 0

        if self.checkbox168.isChecked():
            PageLayoutRemoveLineVar = 1
        else:
            PageLayoutRemoveLineVar = 0



        if self.radioButton14a.isChecked():
            OutputFormatVar = 0
        elif self.radioButton14b.isChecked():
            OutputFormatVar = 1
        elif self.radioButton14c.isChecked():
            OutputFormatVar = 2

        if self.radioButton15a.isChecked():
            OptimizationVar = 0
        elif self.radioButton15b.isChecked():
            OptimizationVar = 1
        elif self.radioButton15c.isChecked():
            OptimizationVar = 2



    # page2-1
# //===========================================//
        if self.checkbox35.isChecked():
            LayoutDespeckleVar = 1
        else:
            LayoutDespeckleVar = 0

        if self.checkbox36.isChecked():
            LayoutThresholdVar = 1
        else:
            LayoutThresholdVar = 0

        if self.checkbox37.isChecked():
            LayoutInvertColorVar = 1
        else:
            LayoutInvertColorVar = 0

        if self.checkbox38.isChecked():
            LayoutThresholdAdaptiveVar = 1
        else:
            LayoutThresholdAdaptiveVar = 0

        if self.checkbox39.isChecked():
            LayoutSharpenVar = 1
        else:
            LayoutSharpenVar = 0

        if self.checkbox310.isChecked():
            LayoutContrastVar = 1
        else:
            LayoutContrastVar = 0


    # page2-2
# //===========================================//
        if self.checkbox311.isChecked():
            FilteringBackgroundNoiseVar = 1
        else:
            FilteringBackgroundNoiseVar = 0
        FilteringBackgroundNoiseIntVar = (4*self.slider311.value())+3       # [3,7,11,15,19]

        if self.checkbox312.isChecked():
            FilteringTextNoiseVar = 1
        else:
            FilteringTextNoiseVar = 0
        FilteringTextNoiseIntVar = (self.slider312.value())+2               # [2,3,4,5,6]

        if self.checkbox313.isChecked():
            FilteringTextErosionVar = 1
        else:
            FilteringTextErosionVar = 0
        FilteringTextErosionIntVar = (self.slider313.value())+2             # [2,3,4,5,6]

        if self.checkbox314.isChecked():
            FilteringTextDilationVar = 1
        else:
            FilteringTextDilationVar = 0
        FilteringTextDilationIntVar = (self.slider314.value())+2            # [2,3,4,5,6]

        if self.checkbox315.isChecked():
            FilteringThresholdVar = 1
        else:
            FilteringThresholdVar = 0
        FilteringThresholdLowerIntVar = (self.slider315a.value())           # [0-255]
        FilteringThresholdUpperIntVar = (self.slider315b.value())           # [0-255]

        if self.checkbox321.isChecked():
            DisplayColorImageVar = 1
        else:
            DisplayColorImageVar = 0

        if self.checkbox322.isChecked():
            DisplayGrayImageVar = 1
        else:
            DisplayGrayImageVar = 0

        if self.checkbox323.isChecked():
            DisplayProcessedImageVar = 1
        else:
            DisplayProcessedImageVar = 0

        if self.checkbox324.isChecked():
            DisplayProcessedAllImageVar = 1
        else:
            DisplayProcessedAllImageVar = 0


    # page3
# //===========================================//
        if self.checkbox41.isChecked():
            WhitelistVar = 1
        else:
            WhitelistVar = 0

        if self.checkbox41a.isChecked():
            Whitelist1Var = 1
        else:
            Whitelist1Var = 0

        if self.checkbox41b.isChecked():
            Whitelist2Var = 1
        else:
            Whitelist2Var = 0

        if self.checkbox41c.isChecked():
            Whitelist3Var = 1
        else:
            Whitelist3Var = 0

        if self.checkbox41d.isChecked():
            Whitelist4Var = 1
        else:
            Whitelist4Var = 0

        if self.checkbox41e.isChecked():
            Whitelist5Var = 1
        else:
            Whitelist5Var = 0


        WhitelistCharVar = self.textbox_whitelist.toPlainText()

        if self.checkbox42.isChecked():
            BlacklistVar = 1
        else:
            BlacklistVar = 0

        if self.checkbox42a.isChecked():
            Blacklist1Var = 1
        else:
            Blacklist1Var = 0

        if self.checkbox42b.isChecked():
            Blacklist2Var = 1
        else:
            Blacklist2Var = 0

        if self.checkbox42c.isChecked():
            Blacklist3Var = 1
        else:
            Blacklist3Var = 0

        if self.checkbox42d.isChecked():
            Blacklist4Var = 1
        else:
            Blacklist4Var = 0

        if self.checkbox42e.isChecked():
            Blacklist5Var = 1
        else:
            Blacklist5Var = 0

        BlacklistCharVar = self.textbox_blacklist.toPlainText()


    # page5
    # //===========================================//
        ThemeLightColorVar = self.comboBox5.currentIndex()
        ThemeDarkColorVar = self.comboBox6.currentIndex()

        from src.func.py_main_editor import MainGuiWindow

        if FLAG_TBTHEMELIGHT:
            ThemeLightColorTBVar = MainGuiWindow.TB_COLOR_LIGHT_CUSTOM
        else:
            ThemeLightColorTBVar = MainGuiWindow.ThemeLightColorTBVar1

        if FLAG_FGTHEMELIGHT:
            ThemeLightColorFGVar = MainGuiWindow.FG_COLOR_LIGHT_CUSTOM
        else:
            ThemeLightColorFGVar = MainGuiWindow.ThemeLightColorFGVar1

        if FLAG_BGTHEMELIGHT:
            ThemeLightColorBGVar = MainGuiWindow.BG_COLOR_LIGHT_CUSTOM
        else:
            ThemeLightColorBGVar = MainGuiWindow.ThemeLightColorBGVar1

        if FLAG_FONTTHEMELIGHT:
            ThemeLightColorFontVar = MainGuiWindow.FONT_COLOR_LIGHT_CUSTOM
        else:
            ThemeLightColorFontVar = MainGuiWindow.ThemeLightColorFontVar1

        if FLAG_BTTHEMELIGHT:
            ThemeLightColorBTVar = MainGuiWindow.BT_COLOR_LIGHT_CUSTOM
        else:
            ThemeLightColorBTVar = MainGuiWindow.ThemeLightColorBTVar1

        if FLAG_BDTHEMELIGHT:
            ThemeLightColorBDVar = MainGuiWindow.BD_COLOR_LIGHT_CUSTOM
        else:
            ThemeLightColorBDVar = MainGuiWindow.ThemeLightColorBDVar1



        if FLAG_TBTHEMEDARK:
            ThemeDarkColorTBVar = MainGuiWindow.TB_COLOR_DARK_CUSTOM
        else:
            ThemeDarkColorTBVar = MainGuiWindow.ThemeDarkColorTBVar1

        if FLAG_FGTHEMEDARK:
            ThemeDarkColorFGVar = MainGuiWindow.FG_COLOR_DARK_CUSTOM
        else:
            ThemeDarkColorFGVar = MainGuiWindow.ThemeDarkColorFGVar1

        if FLAG_BGTHEMEDARK:
            ThemeDarkColorBGVar = MainGuiWindow.BG_COLOR_DARK_CUSTOM
        else:
            ThemeDarkColorBGVar = MainGuiWindow.ThemeDarkColorBGVar1

        if FLAG_FONTTHEMEDARK:
            ThemeDarkColorFontVar = MainGuiWindow.FONT_COLOR_DARK_CUSTOM
        else:
            ThemeDarkColorFontVar = MainGuiWindow.ThemeDarkColorFontVar1

        if FLAG_BTTHEMEDARK:
            ThemeDarkColorBTVar = MainGuiWindow.BT_COLOR_DARK_CUSTOM
        else:
            ThemeDarkColorBTVar = MainGuiWindow.ThemeDarkColorBTVar1

        if FLAG_BDTHEMEDARK:
            ThemeDarkColorBDVar = MainGuiWindow.BD_COLOR_DARK_CUSTOM
        else:
            ThemeDarkColorBDVar = MainGuiWindow.ThemeDarkColorBDVar1


        CursorShapeVar = self.comboBox7.currentIndex()

        if (self.slider531.value() == 0):
            RBBThicknessVar = 0
        elif (self.slider531.value() == 1):
            RBBThicknessVar = 2
        elif (self.slider531.value() == 2):
            RBBThicknessVar = 6
        elif (self.slider531.value() == 3):
            RBBThicknessVar = 8
        elif (self.slider531.value() == 4):
            RBBThicknessVar = 12

        RBBOpacityVar = int(50*self.slider532.value())
        RBBColorVar = str(MainGuiWindow.RBBColorVar1)


    # page6
    # //===========================================//
        if (self.comboBox8.currentIndex() == 0):
            FontSystemSizeVar = 7
        elif (self.comboBox8.currentIndex() == 1):
            FontSystemSizeVar = 8
        elif (self.comboBox8.currentIndex() == 2):
            FontSystemSizeVar = 9

        BorderStyleVar = self.comboBox9.currentIndex()

        if (self.comboBox11.currentIndex() == 0):
            TextEditorIconSizeVar = 16
        elif (self.comboBox11.currentIndex() == 1):
            TextEditorIconSizeVar = 18
        elif (self.comboBox11.currentIndex() == 2):
            TextEditorIconSizeVar = 22

        TextEditorStatusBarVar = self.comboBox12.currentIndex()
        TextEditorModeVar = self.comboBox13.currentIndex()

        if self.checkbox62.isChecked():
            SystemTrayIconVar = 1
        else:
            SystemTrayIconVar = 0

        # //=========================//
        self.encode_Setting()
        # //=========================//

        from src.module.py_window_main import MainGuiWindow
        with open(MainGuiWindow.file4, "w") as f_obj:
            f_obj.write(f"{LanguageSystemVarEnc}\n")
            f_obj.write(f"{MathEquationVarEnc}\n")
            f_obj.write(f"{TextLayoutVarEnc}\n")
            f_obj.write(f"{DetectedTextVarEnc}\n")
            f_obj.write(f"{DetectedTextLetterVarEnc}\n")
            f_obj.write(f"{DetectedTextLowerVarEnc}\n")
            f_obj.write(f"{DetectedTextUpperVarEnc}\n")
            f_obj.write(f"{DetectedTextNumberVarEnc}\n")
            f_obj.write(f"{DetectedTextPuncVarEnc}\n")
            f_obj.write(f"{DetectedTextMiscVarEnc}\n")
            f_obj.write(f"{OutputFormatVarEnc}\n")
            f_obj.write(f"{OptimizationVarEnc}\n")
            f_obj.write(f"{PageLayoutAutoRotatePageVarEnc}\n")
            f_obj.write(f"{PageLayoutDeskewVarEnc}\n")
            f_obj.write(f"{PageLayoutDecolumnizeVarEnc}\n")
            f_obj.write(f"{PageLayoutRemoveTableVarEnc}\n")
            f_obj.write(f"{PageLayoutRemoveWatermarkVarEnc}\n")
            f_obj.write(f"{PageLayoutRemoveUnderlineVarEnc}\n")
            f_obj.write(f"{PageLayoutRemoveSpaceVarEnc}\n")
            f_obj.write(f"{PageLayoutRemoveLineVarEnc}\n")
            f_obj.write(f"{LayoutDespeckleVarEnc}\n")
            f_obj.write(f"{LayoutThresholdVarEnc}\n")
            f_obj.write(f"{LayoutInvertColorVarEnc}\n")
            f_obj.write(f"{LayoutThresholdAdaptiveVarEnc}\n")
            f_obj.write(f"{LayoutSharpenVarEnc}\n")
            f_obj.write(f"{LayoutContrastVarEnc}\n")
            f_obj.write(f"{FilteringBackgroundNoiseVarEnc}\n")
            f_obj.write(f"{FilteringBackgroundNoiseIntVarEnc}\n")
            f_obj.write(f"{FilteringTextNoiseVarEnc}\n")
            f_obj.write(f"{FilteringTextNoiseIntVarEnc}\n")
            f_obj.write(f"{FilteringTextErosionVarEnc}\n")
            f_obj.write(f"{FilteringTextErosionIntVarEnc}\n")
            f_obj.write(f"{FilteringTextDilationVarEnc}\n")
            f_obj.write(f"{FilteringTextDilationIntVarEnc}\n")
            f_obj.write(f"{FilteringThresholdVarEnc}\n")
            f_obj.write(f"{DisplayColorImageVarEnc}\n")
            f_obj.write(f"{DisplayGrayImageVarEnc}\n")
            f_obj.write(f"{DisplayProcessedImageVarEnc}\n")
            f_obj.write(f"{DisplayProcessedAllImageVarEnc}\n")
            f_obj.write(f"{WhitelistVarEnc}\n")
            f_obj.write(f"{Whitelist1VarEnc}\n")
            f_obj.write(f"{Whitelist2VarEnc}\n")
            f_obj.write(f"{Whitelist3VarEnc}\n")
            f_obj.write(f"{Whitelist4VarEnc}\n")
            f_obj.write(f"{Whitelist5VarEnc}\n")
            f_obj.write(f"{BlacklistVarEnc}\n")
            f_obj.write(f"{Blacklist1VarEnc}\n")
            f_obj.write(f"{Blacklist2VarEnc}\n")
            f_obj.write(f"{Blacklist3VarEnc}\n")
            f_obj.write(f"{Blacklist4VarEnc}\n")
            f_obj.write(f"{Blacklist5VarEnc}\n")
            f_obj.write(f"{ThemeLightColorVarEnc}\n")
            f_obj.write(f"{ThemeDarkColorVarEnc}\n")
            f_obj.write(f"{CursorShapeVarEnc}\n")
            f_obj.write(f"{RBBThicknessVarEnc}\n")
            f_obj.write(f"{RBBOpacityVarEnc}\n")
            f_obj.write(f"{FontSystemSizeVarEnc}\n")
            f_obj.write(f"{BorderStyleVarEnc}\n")
            f_obj.write(f"{TextEditorIconSizeVarEnc}\n")
            f_obj.write(f"{TextEditorStatusBarVarEnc}\n")
            f_obj.write(f"{TextEditorModeVarEnc}\n")
            f_obj.write(f"{SystemTrayIconVarEnc}\n")
            f_obj.write(f"{FilteringThresholdLowerIntVarEnc}\n")
            f_obj.write(f"{FilteringThresholdUpperIntVarEnc}\n")
            f_obj.write(f"{ThemeLightColorTBVarEnc}\n")
            f_obj.write(f"{ThemeLightColorFGVarEnc}\n")
            f_obj.write(f"{ThemeLightColorBGVarEnc}\n")
            f_obj.write(f"{ThemeLightColorFontVarEnc}\n")
            f_obj.write(f"{ThemeLightColorBTVarEnc}\n")
            f_obj.write(f"{ThemeLightColorBDVarEnc}\n")
            f_obj.write(f"{ThemeDarkColorTBVarEnc}\n")
            f_obj.write(f"{ThemeDarkColorFGVarEnc}\n")
            f_obj.write(f"{ThemeDarkColorBGVarEnc}\n")
            f_obj.write(f"{ThemeDarkColorFontVarEnc}\n")
            f_obj.write(f"{ThemeDarkColorBTVarEnc}\n")
            f_obj.write(f"{ThemeDarkColorBDVarEnc}\n")
            f_obj.write(f"{RBBColorVarEnc}\n")
            f_obj.write(f"{LanguageVarEnc}")

        with open(MainGuiWindow.file5, "w") as f_obj:
            f_obj.write(f"{WhitelistCharVar}")

        with open(MainGuiWindow.file6, "w") as f_obj:
            f_obj.write(f"{BlacklistCharVar}")


#########################################################################


    #//===================================================//
    def exitKeyPressed(self):
        from src.module.py_window_main import MainGuiWindow

        print('=== exitKeyPressed ===')
        self.close()
        MainGuiWindow.exitProgram(self)


    # page1
    # //===========================================//
    def onChanged_combobox1(self):
        # from src.module.py_window_main import MainGuiWindow
        global FLAG_SELECT_ALL_INIT, FLAG_COMBOBOX_SELECT_ALL

        print('=== onChanged_combobox1 ===')
        if not(FLAG_COMBOBOX_SELECT_ALL) and (self.comboBox1.model().item(113,0).checkState() == Qt.CheckState.Checked):

            print('=== Select all ===')
            FLAG_COMBOBOX_SELECT_ALL = True
            for i in range(self.comboBox1.count()):
                item = self.comboBox1.model().item(i, 0)
                item.setCheckState(Qt.CheckState.Checked)
                self.comboBox1.model().item(1,0).setCheckState(Qt.CheckState.Unchecked)
                self.comboBox1.model().item(112,0).setCheckState(Qt.CheckState.Unchecked)
                self.comboBox1.model().item(114,0).setCheckState(Qt.CheckState.Unchecked)

        if (FLAG_COMBOBOX_SELECT_ALL) and (self.comboBox1.model().item(113,0).checkState() == Qt.CheckState.Unchecked):
            print('=== Deselect all ===')
            FLAG_COMBOBOX_SELECT_ALL = False
            for i in range(self.comboBox1.count()-1):
                item = self.comboBox1.model().item(i, 0)
                item.setCheckState(Qt.CheckState.Unchecked)

        print('FLAG_COMBOBOX_SELECT_ALL := ', FLAG_COMBOBOX_SELECT_ALL)

    # page1
# //===========================================//
    def onClicked_checkbox121(self):
        print('=== onClicked_checkbox121 ===')


# //===========================================//
    def onClicked_checkbox122(self):
        print('=== onClicked_checkbox122 ===')

# //===========================================//
    def onClicked_checkbox123(self):
        print('=== onClicked_checkbox123 ===')

# //===========================================//
    def onClicked_checkbox124(self):
        print('=== onClicked_checkbox124 ===')

# //===========================================//
    def onClicked_checkbox125(self):
        print('=== onClicked_checkbox125 ===')

# //===========================================//
    def onClicked_checkbox126(self):
        print('=== onClicked_checkbox126 ===')



# //===========================================//
# // page2-1
# //===========================================//
    def onClicked_checkbox32(self):
        print('=== onClicked_checkbox32 ===')

# //===========================================//
    # page2-2
# //===========================================//
    def onClicked_checkbox21(self):
        print('=== onClicked_checkbox21 ===')

# //===========================================//
    # page3
# //===========================================//
    def onClicked_checkbox41(self):
        print('=== onClicked_checkbox41 ===')
        if (self.checkbox41.isChecked()):
            self.checkbox41a.setEnabled(True)
            self.checkbox41b.setEnabled(True)
            self.checkbox41c.setEnabled(True)
            self.checkbox41d.setEnabled(True)
            self.checkbox41e.setEnabled(True)
            self.textbox_whitelist.setEnabled(True)
        else:
            self.checkbox41a.setEnabled(False)
            self.checkbox41b.setEnabled(False)
            self.checkbox41c.setEnabled(False)
            self.checkbox41d.setEnabled(False)
            self.checkbox41e.setEnabled(False)
            self.textbox_whitelist.setEnabled(False)

# //===========================================//
    def onClicked_checkbox41a(self):
        print('=== onClicked_checkbox41a ===')
        if (self.checkbox41a.isChecked()):
            text_whitelist = self.textbox_whitelist.toPlainText()
            text_whitelist = text_whitelist.replace('\n\n','\n').strip()
            a_to_z_char = 'abcdefghijklmnopqrstuvwxyz'
            if text_whitelist == '':
                self.textbox_whitelist.setPlainText(text_whitelist+a_to_z_char)
            else:
                self.textbox_whitelist.setPlainText(text_whitelist+'\n'+a_to_z_char)
        else:
            text_whitelist = self.textbox_whitelist.toPlainText()
            text_whitelist = text_whitelist.strip()
            text_whitelist = text_whitelist.replace('a','').replace('b','').replace('c','').replace('d','').replace('e','').replace('f','')     \
            .replace('g','').replace('h','').replace('i','').replace('j','').replace('k','').replace('l','').replace('m','').replace('n','')    \
            .replace('o','').replace('p','').replace('q','').replace('r','').replace('s','').replace('t','').replace('u','').replace('v','')    \
            .replace('w','').replace('x','').replace('y','').replace('z','')
            text_whitelist = text_whitelist.replace('\n\n','\n').lstrip()
            self.textbox_whitelist.setPlainText(text_whitelist)

# //===========================================//
    def onClicked_checkbox41b(self):
        print('=== onClicked_checkbox41b ===')
        if (self.checkbox41b.isChecked()):
            text_whitelist = self.textbox_whitelist.toPlainText()
            text_whitelist = text_whitelist.replace('\n\n','\n').strip()
            A_to_Z_char = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            if text_whitelist == '':
                self.textbox_whitelist.setPlainText(text_whitelist+A_to_Z_char)
            else:
                self.textbox_whitelist.setPlainText(text_whitelist+'\n'+A_to_Z_char)
        else:
            text_whitelist = self.textbox_whitelist.toPlainText()
            text_whitelist = text_whitelist.replace('A','').replace('B','').replace('C','').replace('D','').replace('E','').replace('F','')     \
            .replace('G','').replace('H','').replace('I','').replace('J','').replace('K','').replace('L','').replace('M','').replace('N','')    \
            .replace('O','').replace('P','').replace('Q','').replace('R','').replace('S','').replace('T','').replace('U','').replace('V','')    \
            .replace('W','').replace('X','').replace('Y','').replace('Z','')
            text_whitelist = text_whitelist.replace('\n\n','\n').lstrip()
            self.textbox_whitelist.setPlainText(text_whitelist)

# //===========================================//
    def onClicked_checkbox41c(self):
        print('=== onClicked_checkbox41c ===')
        if (self.checkbox41c.isChecked()):
            text_whitelist = self.textbox_whitelist.toPlainText()
            text_whitelist = text_whitelist.replace('\n\n','\n').strip()
            number_char = '0123456789'
            if text_whitelist == '':
                self.textbox_whitelist.setPlainText(text_whitelist+number_char)
            else:
                self.textbox_whitelist.setPlainText(text_whitelist+'\n'+number_char)
        else:
            text_whitelist = self.textbox_whitelist.toPlainText()
            text_whitelist = text_whitelist.strip()
            text_whitelist = text_whitelist.replace('0','').replace('1','').replace('2','').replace('3','').replace('4','').replace('5','')     \
            .replace('6','').replace('7','').replace('8','').replace('9','')
            text_whitelist = text_whitelist.replace('\n\n','\n').lstrip()
            self.textbox_whitelist.setPlainText(text_whitelist)

# //===========================================//
    def onClicked_checkbox41d(self):
        print('=== onClicked_checkbox41d ===')
        if (self.checkbox41d.isChecked()):
            text_whitelist = self.textbox_whitelist.toPlainText()
            text_whitelist = text_whitelist.replace('\n\n','\n').strip()
            punct_char = "'.,:;_=+-*/\\|^%?!()[]{}<>—‘’“”'" + "\'\"\'" + '\"\'\"'

            if text_whitelist == '':
                self.textbox_whitelist.setPlainText(text_whitelist+punct_char)
            else:
                self.textbox_whitelist.setPlainText(text_whitelist+'\n'+punct_char)
        else:
            text_whitelist = self.textbox_whitelist.toPlainText()
            text_whitelist = text_whitelist.strip()
            text_whitelist = text_whitelist.replace('.','').replace(',','').replace(':','').replace(';','').replace('_','').replace('=','')     \
            .replace('+','').replace('-','').replace('*','').replace('/','').replace('\\','').replace('|','').replace('^','').replace('%','')   \
            .replace('?','').replace('!','').replace('(','').replace(')','').replace('[','').replace(']','').replace('{','').replace('}','')    \
            .replace('<','').replace('>','').replace('—','').replace('‘','').replace('’','').replace('“','').replace('”','')  \
            .replace("'",'').replace('"','')
            text_whitelist = text_whitelist.replace('\n\n','\n').lstrip()
            self.textbox_whitelist.setPlainText(text_whitelist)

# //===========================================//
    def onClicked_checkbox41e(self):
        print('=== onClicked_checkbox41e ===')
        if (self.checkbox41e.isChecked()):
            text_whitelist = self.textbox_whitelist.toPlainText()
            text_whitelist = text_whitelist.replace('\n\n','\n').strip()

            special_char = "&#$~§@©®°™¥£¢«»€"
            if text_whitelist == '':
                self.textbox_whitelist.setPlainText(text_whitelist+special_char)
            else:
                self.textbox_whitelist.setPlainText(text_whitelist+'\n'+special_char)
        else:
            text_whitelist = self.textbox_whitelist.toPlainText()
            text_whitelist = text_whitelist.strip()
            text_whitelist = text_whitelist.replace('&','').replace('#','').replace('$','').replace('~','').replace('§','').replace('@','')     \
            .replace('©','').replace('®','').replace('°','').replace('™','').replace('¥','').replace('£','').replace('¢','').replace('«','')   \
            .replace('»','').replace('€','')
            text_whitelist = text_whitelist.replace('\n\n','\n').lstrip()
            self.textbox_whitelist.setPlainText(text_whitelist)

# //===========================================//
    def onClicked_checkbox42(self):
        print('=== onClicked_checkbox42 ===')
        if (self.checkbox42.isChecked()):
            self.checkbox42a.setEnabled(True)
            self.checkbox42b.setEnabled(True)
            self.checkbox42c.setEnabled(True)
            self.checkbox42d.setEnabled(True)
            self.checkbox42e.setEnabled(True)
            self.textbox_blacklist.setEnabled(True)
        else:
            self.checkbox42a.setEnabled(False)
            self.checkbox42b.setEnabled(False)
            self.checkbox42c.setEnabled(False)
            self.checkbox42d.setEnabled(False)
            self.checkbox42e.setEnabled(False)
            self.textbox_blacklist.setEnabled(False)

# //===========================================//
    def onClicked_checkbox42a(self):
        print('=== onClicked_checkbox42a ===')
        if (self.checkbox42a.isChecked()):
            text_blacklist = self.textbox_blacklist.toPlainText()
            text_blacklist = text_blacklist.replace('\n\n','\n').strip()
            a_to_z_char = 'abcdefghijklmnopqrstuvwxyz'
            if text_blacklist == '':
                self.textbox_blacklist.setPlainText(text_blacklist+a_to_z_char)
            else:
                self.textbox_blacklist.setPlainText(text_blacklist+'\n'+a_to_z_char)
        else:
            text_blacklist = self.textbox_blacklist.toPlainText()
            text_blacklist = text_blacklist.strip()
            text_blacklist = text_blacklist.replace('a','').replace('b','').replace('c','').replace('d','').replace('e','').replace('f','')     \
            .replace('g','').replace('h','').replace('i','').replace('j','').replace('k','').replace('l','').replace('m','').replace('n','')    \
            .replace('o','').replace('p','').replace('q','').replace('r','').replace('s','').replace('t','').replace('u','').replace('v','')    \
            .replace('w','').replace('x','').replace('y','').replace('z','').lstrip()
            text_blacklist = text_blacklist.replace('\n\n','\n').lstrip()
            self.textbox_blacklist.setPlainText(text_blacklist)

# //===========================================//
    def onClicked_checkbox42b(self):
        print('=== onClicked_checkbox42b ===')
        if (self.checkbox42b.isChecked()):
            text_blacklist = self.textbox_blacklist.toPlainText()
            text_blacklist = text_blacklist.replace('\n\n','\n').strip()
            A_to_Z_char = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            if text_blacklist == '':
                self.textbox_blacklist.setPlainText(text_blacklist+A_to_Z_char)
            else:
                self.textbox_blacklist.setPlainText(text_blacklist+'\n'+A_to_Z_char)
        else:
            text_blacklist = self.textbox_blacklist.toPlainText()
            text_blacklist = text_blacklist.strip()
            text_blacklist = text_blacklist.replace('A','').replace('B','').replace('C','').replace('D','').replace('E','').replace('F','')     \
            .replace('G','').replace('H','').replace('I','').replace('J','').replace('K','').replace('L','').replace('M','').replace('N','')    \
            .replace('O','').replace('P','').replace('Q','').replace('R','').replace('S','').replace('T','').replace('U','').replace('V','')    \
            .replace('W','').replace('X','').replace('Y','').replace('Z','').lstrip()
            text_blacklist = text_blacklist.replace('\n\n','\n').lstrip()
            self.textbox_blacklist.setPlainText(text_blacklist)

# //===========================================//
    def onClicked_checkbox42c(self):
        print('=== onClicked_checkbox42c ===')
        if (self.checkbox42c.isChecked()):
            text_blacklist = self.textbox_blacklist.toPlainText()
            text_blacklist = text_blacklist.replace('\n\n','\n').strip()
            number_char = '0123456789'
            if text_blacklist == '':
                self.textbox_blacklist.setPlainText(text_blacklist+number_char)
            else:
                self.textbox_blacklist.setPlainText(text_blacklist+'\n'+number_char)
        else:
            text_blacklist = self.textbox_blacklist.toPlainText()
            text_blacklist = text_blacklist.strip()
            text_blacklist = text_blacklist.replace('0','').replace('1','').replace('2','').replace('3','').replace('4','').replace('5','')     \
            .replace('6','').replace('7','').replace('8','').replace('9','').lstrip()
            text_blacklist = text_blacklist.replace('\n\n','\n').lstrip()
            self.textbox_blacklist.setPlainText(text_blacklist)

# //===========================================//
    def onClicked_checkbox42d(self):
        print('=== onClicked_checkbox42d ===')
        if (self.checkbox42d.isChecked()):
            text_blacklist = self.textbox_blacklist.toPlainText()
            text_blacklist = text_blacklist.replace('\n\n','\n').strip()
            punct_char = "'.,:;_=+-*/\\|^%?!()[]{}<>—‘’“”'" + "\'\"\'" + '\"\'\"'

            if text_blacklist == '':
                self.textbox_blacklist.setPlainText(text_blacklist+punct_char)
            else:
                self.textbox_blacklist.setPlainText(text_blacklist+'\n'+punct_char)
        else:
            text_blacklist = self.textbox_blacklist.toPlainText()
            text_blacklist = text_blacklist.strip()
            text_blacklist = text_blacklist.replace('.','').replace(',','').replace(':','').replace(';','').replace('_','').replace('=','')     \
            .replace('+','').replace('-','').replace('*','').replace('/','').replace('\\','').replace('|','').replace('^','').replace('%','')   \
            .replace('?','').replace('!','').replace('(','').replace(')','').replace('[','').replace(']','').replace('{','').replace('}','')    \
            .replace('<','').replace('>','').replace('—','').replace('‘','').replace('’','').replace('“','').replace('”','')  \
            .replace("'",'').replace('"','')
            text_blacklist = text_blacklist.replace('\n\n','\n').lstrip()
            self.textbox_blacklist.setPlainText(text_blacklist)

# //===========================================//
    def onClicked_checkbox42e(self):
        print('=== onClicked_checkbox42e ===')
        if (self.checkbox42e.isChecked()):
            text_blacklist = self.textbox_blacklist.toPlainText()
            text_blacklist = text_blacklist.replace('\n\n','\n').strip()
            special_char = "&#$~§@©®°™¥£¢«»€"
            if text_blacklist == '':
                self.textbox_blacklist.setPlainText(text_blacklist+special_char)
            else:
                self.textbox_blacklist.setPlainText(text_blacklist+'\n'+special_char)
        else:
            text_blacklist = self.textbox_blacklist.toPlainText()
            text_blacklist = text_blacklist.strip()
            text_blacklist = text_blacklist.replace('&','').replace('#','').replace('$','').replace('~','').replace('§','').replace('@','')     \
            .replace('©','').replace('®','').replace('°','').replace('™','').replace('¥','').replace('£','').replace('¢','').replace('«','')   \
            .replace('»','').replace('€','')
            text_blacklist = text_blacklist.replace('\n\n','\n').lstrip()
            self.textbox_blacklist.setPlainText(text_blacklist)


# //===========================================//
    # page4
# //===========================================//
    def onClicked_radioButton12a(self):
        print('=== onClicked_radioButton12a ===')
        self.checkbox121.setEnabled(False)
        self.checkbox122.setEnabled(False)
        self.checkbox123.setEnabled(False)
        self.checkbox124.setEnabled(False)
        self.checkbox125.setEnabled(False)
        self.checkbox126.setEnabled(False)

# //===========================================//
    def onClicked_radioButton12b(self):
        print('=== onClicked_radioButton12b ===')
        self.checkbox121.setEnabled(True)
        self.checkbox122.setEnabled(True)
        self.checkbox123.setEnabled(True)
        self.checkbox124.setEnabled(True)
        self.checkbox125.setEnabled(True)
        self.checkbox126.setEnabled(True)

# //===========================================//
    def onClicked_radioButton13a(self):
        print('=== onClicked_radioButton13a ===')
        self.checkbox37.setEnabled(True)
        self.checkbox38.setEnabled(True)
        self.checkbox39.setEnabled(True)
        self.checkbox310.setEnabled(True)
        self.checkbox311.setEnabled(True)
        self.checkbox312.setEnabled(True)
        self.checkbox313.setEnabled(True)
        self.checkbox314.setEnabled(True)
        self.slider311.setEnabled(True)
        self.slider312.setEnabled(True)
        self.slider313.setEnabled(True)
        self.slider314.setEnabled(True)

# //===========================================//
    def onClicked_radioButton13b(self):
        print('=== onClicked_radioButton13b ===')
        self.checkbox37.setEnabled(False)
        self.checkbox38.setEnabled(False)
        self.checkbox39.setEnabled(False)
        self.checkbox310.setEnabled(False)
        self.checkbox311.setEnabled(False)
        self.checkbox312.setEnabled(False)
        self.checkbox313.setEnabled(False)
        self.checkbox314.setEnabled(False)
        self.slider311.setEnabled(False)
        self.slider312.setEnabled(False)
        self.slider313.setEnabled(False)
        self.slider314.setEnabled(False)

# //===========================================//
    def onClicked_checkbox62(self):
        print('=== onClicked_checkbox62 ===')

        from src.module.py_window_main import MainGuiWindow
        if self.checkbox62.isChecked():
            MainGuiWindow.trayIcon.setVisible(False)
        else:
            MainGuiWindow.trayIcon.setVisible(True)

# //===========================================//
    def onClicked_checkbox161(self):
        print('=== onClicked_checkbox161 ===')
        if (self.checkbox161.isChecked() or self.checkbox162.isChecked() or self.checkbox164.isChecked() or \
            self.checkbox165.isChecked() or self.checkbox166.isChecked() or self.checkbox35.isChecked() or \
            self.checkbox36.isChecked() or self.checkbox37.isChecked() or self.checkbox38.isChecked() or \
            self.checkbox39.isChecked() or self.checkbox310.isChecked() or self.checkbox311.isChecked() or \
            self.checkbox312.isChecked() or self.checkbox313.isChecked() or self.checkbox314.isChecked() or \
            self.checkbox315.isChecked()):
            self.checkbox323.setEnabled(True)
            self.checkbox324.setEnabled(True)
        else:
            self.checkbox323.setEnabled(False)
            self.checkbox324.setEnabled(False)

# //===========================================//
    def onClicked_checkbox162(self):
        print('=== onClicked_checkbox162 ===')
        if (self.checkbox161.isChecked() or self.checkbox162.isChecked() or self.checkbox164.isChecked() or \
            self.checkbox165.isChecked() or self.checkbox166.isChecked() or self.checkbox35.isChecked() or \
            self.checkbox36.isChecked() or self.checkbox37.isChecked() or self.checkbox38.isChecked() or \
            self.checkbox39.isChecked() or self.checkbox310.isChecked() or self.checkbox311.isChecked() or \
            self.checkbox312.isChecked() or self.checkbox313.isChecked() or self.checkbox314.isChecked() or \
            self.checkbox315.isChecked()):
            self.checkbox323.setEnabled(True)
            self.checkbox324.setEnabled(True)
        else:
            self.checkbox323.setEnabled(False)
            self.checkbox324.setEnabled(False)

# //===========================================//
    def onClicked_checkbox164(self):
        print('=== onClicked_checkbox164 ===')
        if (self.checkbox161.isChecked() or self.checkbox162.isChecked() or self.checkbox164.isChecked() or \
            self.checkbox165.isChecked() or self.checkbox166.isChecked() or self.checkbox35.isChecked() or \
            self.checkbox36.isChecked() or self.checkbox37.isChecked() or self.checkbox38.isChecked() or \
            self.checkbox39.isChecked() or self.checkbox310.isChecked() or self.checkbox311.isChecked() or \
            self.checkbox312.isChecked() or self.checkbox313.isChecked() or self.checkbox314.isChecked() or \
            self.checkbox315.isChecked()):
            self.checkbox323.setEnabled(True)
            self.checkbox324.setEnabled(True)
        else:
            self.checkbox323.setEnabled(False)
            self.checkbox324.setEnabled(False)

# //===========================================//
    def onClicked_checkbox165(self):
        print('=== onClicked_checkbox165 ===')
        if (self.checkbox161.isChecked() or self.checkbox162.isChecked() or self.checkbox164.isChecked() or \
            self.checkbox165.isChecked() or self.checkbox166.isChecked() or self.checkbox35.isChecked() or \
            self.checkbox36.isChecked() or self.checkbox37.isChecked() or self.checkbox38.isChecked() or \
            self.checkbox39.isChecked() or self.checkbox310.isChecked() or self.checkbox311.isChecked() or \
            self.checkbox312.isChecked() or self.checkbox313.isChecked() or self.checkbox314.isChecked() or \
            self.checkbox315.isChecked()):
            self.checkbox323.setEnabled(True)
            self.checkbox324.setEnabled(True)
        else:
            self.checkbox323.setEnabled(False)
            self.checkbox324.setEnabled(False)

# //===========================================//
    def onClicked_checkbox166(self):
        print('=== onClicked_checkbox166 ===')
        if (self.checkbox161.isChecked() or self.checkbox162.isChecked() or self.checkbox164.isChecked() or \
            self.checkbox165.isChecked() or self.checkbox166.isChecked() or self.checkbox35.isChecked() or \
            self.checkbox36.isChecked() or self.checkbox37.isChecked() or self.checkbox38.isChecked() or \
            self.checkbox39.isChecked() or self.checkbox310.isChecked() or self.checkbox311.isChecked() or \
            self.checkbox312.isChecked() or self.checkbox313.isChecked() or self.checkbox314.isChecked() or \
            self.checkbox315.isChecked()):
            self.checkbox323.setEnabled(True)
            self.checkbox324.setEnabled(True)
        else:
            self.checkbox323.setEnabled(False)
            self.checkbox324.setEnabled(False)

# //===========================================//
    def onClicked_checkbox35(self):
        print('=== onClicked_checkbox35 ===')
        if (self.checkbox161.isChecked() or self.checkbox162.isChecked() or self.checkbox164.isChecked() or \
            self.checkbox165.isChecked() or self.checkbox166.isChecked() or self.checkbox35.isChecked() or \
            self.checkbox36.isChecked() or self.checkbox37.isChecked() or self.checkbox38.isChecked() or \
            self.checkbox39.isChecked() or self.checkbox310.isChecked() or self.checkbox311.isChecked() or \
            self.checkbox312.isChecked() or self.checkbox313.isChecked() or self.checkbox314.isChecked() or \
            self.checkbox315.isChecked()):
            self.checkbox323.setEnabled(True)
            self.checkbox324.setEnabled(True)
        else:
            self.checkbox323.setEnabled(False)
            self.checkbox324.setEnabled(False)

# //===========================================//
    def onClicked_checkbox36(self):
        print('=== onClicked_checkbox36 ===')
        if (self.checkbox161.isChecked() or self.checkbox162.isChecked() or self.checkbox164.isChecked() or \
            self.checkbox165.isChecked() or self.checkbox166.isChecked() or self.checkbox35.isChecked() or \
            self.checkbox36.isChecked() or self.checkbox37.isChecked() or self.checkbox38.isChecked() or \
            self.checkbox39.isChecked() or self.checkbox310.isChecked() or self.checkbox311.isChecked() or \
            self.checkbox312.isChecked() or self.checkbox313.isChecked() or self.checkbox314.isChecked() or \
            self.checkbox315.isChecked()):
            self.checkbox323.setEnabled(True)
            self.checkbox324.setEnabled(True)
        else:
            self.checkbox323.setEnabled(False)
            self.checkbox324.setEnabled(False)

# //===========================================//
    def onClicked_checkbox37(self):
        print('=== onClicked_checkbox37 ===')
        if (self.checkbox161.isChecked() or self.checkbox162.isChecked() or self.checkbox164.isChecked() or \
            self.checkbox165.isChecked() or self.checkbox166.isChecked() or self.checkbox35.isChecked() or \
            self.checkbox36.isChecked() or self.checkbox37.isChecked() or self.checkbox38.isChecked() or \
            self.checkbox39.isChecked() or self.checkbox310.isChecked() or self.checkbox311.isChecked() or \
            self.checkbox312.isChecked() or self.checkbox313.isChecked() or self.checkbox314.isChecked() or \
            self.checkbox315.isChecked()):
            self.checkbox323.setEnabled(True)
            self.checkbox324.setEnabled(True)
        else:
            self.checkbox323.setEnabled(False)
            self.checkbox324.setEnabled(False)

# //===========================================//
    def onClicked_checkbox38(self):
        print('=== onClicked_checkbox38 ===')
        if (self.checkbox161.isChecked() or self.checkbox162.isChecked() or self.checkbox164.isChecked() or \
            self.checkbox165.isChecked() or self.checkbox166.isChecked() or self.checkbox35.isChecked() or \
            self.checkbox36.isChecked() or self.checkbox37.isChecked() or self.checkbox38.isChecked() or \
            self.checkbox39.isChecked() or self.checkbox310.isChecked() or self.checkbox311.isChecked() or \
            self.checkbox312.isChecked() or self.checkbox313.isChecked() or self.checkbox314.isChecked() or \
            self.checkbox315.isChecked()):
            self.checkbox323.setEnabled(True)
            self.checkbox324.setEnabled(True)
        else:
            self.checkbox323.setEnabled(False)
            self.checkbox324.setEnabled(False)

# //===========================================//
    def onClicked_checkbox39(self):
        print('=== onClicked_checkbox39 ===')
        if (self.checkbox161.isChecked() or self.checkbox162.isChecked() or self.checkbox164.isChecked() or \
            self.checkbox165.isChecked() or self.checkbox166.isChecked() or self.checkbox35.isChecked() or \
            self.checkbox36.isChecked() or self.checkbox37.isChecked() or self.checkbox38.isChecked() or \
            self.checkbox39.isChecked() or self.checkbox310.isChecked() or self.checkbox311.isChecked() or \
            self.checkbox312.isChecked() or self.checkbox313.isChecked() or self.checkbox314.isChecked() or \
            self.checkbox315.isChecked()):
            self.checkbox323.setEnabled(True)
            self.checkbox324.setEnabled(True)
        else:
            self.checkbox323.setEnabled(False)
            self.checkbox324.setEnabled(False)

# //===========================================//
    def onClicked_checkbox310(self):
        print('=== onClicked_checkbox310 ===')
        if (self.checkbox161.isChecked() or self.checkbox162.isChecked() or self.checkbox164.isChecked() or \
            self.checkbox165.isChecked() or self.checkbox166.isChecked() or self.checkbox35.isChecked() or \
            self.checkbox36.isChecked() or self.checkbox37.isChecked() or self.checkbox38.isChecked() or \
            self.checkbox39.isChecked() or self.checkbox310.isChecked() or self.checkbox311.isChecked() or \
            self.checkbox312.isChecked() or self.checkbox313.isChecked() or self.checkbox314.isChecked() or \
            self.checkbox315.isChecked()):
            self.checkbox323.setEnabled(True)
            self.checkbox324.setEnabled(True)
        else:
            self.checkbox323.setEnabled(False)
            self.checkbox324.setEnabled(False)

# //===========================================//
    def onClicked_checkbox311(self):
        print('=== onClicked_checkbox311 ===')
        if (self.checkbox311.isChecked()):
            self.slider311.setEnabled(True)
        else:
            self.slider311.setEnabled(False)

        if (self.checkbox161.isChecked() or self.checkbox162.isChecked() or self.checkbox164.isChecked() or \
            self.checkbox165.isChecked() or self.checkbox166.isChecked() or self.checkbox35.isChecked() or \
            self.checkbox36.isChecked() or self.checkbox37.isChecked() or self.checkbox38.isChecked() or \
            self.checkbox39.isChecked() or self.checkbox310.isChecked() or self.checkbox311.isChecked() or \
            self.checkbox312.isChecked() or self.checkbox313.isChecked() or self.checkbox314.isChecked() or \
            self.checkbox315.isChecked()):
            self.checkbox323.setEnabled(True)
            self.checkbox324.setEnabled(True)
        else:
            self.checkbox323.setEnabled(False)
            self.checkbox324.setEnabled(False)

# //===========================================//
    def onClicked_checkbox312(self):
        print('=== onClicked_checkbox312 ===')
        if (self.checkbox312.isChecked()):
            self.slider312.setEnabled(True)
        else:
            self.slider312.setEnabled(False)

        if (self.checkbox161.isChecked() or self.checkbox162.isChecked() or self.checkbox164.isChecked() or \
            self.checkbox165.isChecked() or self.checkbox166.isChecked() or self.checkbox35.isChecked() or \
            self.checkbox36.isChecked() or self.checkbox37.isChecked() or self.checkbox38.isChecked() or \
            self.checkbox39.isChecked() or self.checkbox310.isChecked() or self.checkbox311.isChecked() or \
            self.checkbox312.isChecked() or self.checkbox313.isChecked() or self.checkbox314.isChecked() or \
            self.checkbox315.isChecked()):
            self.checkbox323.setEnabled(True)
            self.checkbox324.setEnabled(True)
        else:
            self.checkbox323.setEnabled(False)
            self.checkbox324.setEnabled(False)

# //===========================================//
    def onClicked_checkbox313(self):
        print('=== onClicked_checkbox313 ===')
        if (self.checkbox313.isChecked()):
            self.slider313.setEnabled(True)
        else:
            self.slider313.setEnabled(False)

        if (self.checkbox161.isChecked() or self.checkbox162.isChecked() or self.checkbox164.isChecked() or \
            self.checkbox165.isChecked() or self.checkbox166.isChecked() or self.checkbox35.isChecked() or \
            self.checkbox36.isChecked() or self.checkbox37.isChecked() or self.checkbox38.isChecked() or \
            self.checkbox39.isChecked() or self.checkbox310.isChecked() or self.checkbox311.isChecked() or \
            self.checkbox312.isChecked() or self.checkbox313.isChecked() or self.checkbox314.isChecked() or \
            self.checkbox315.isChecked()):
            self.checkbox323.setEnabled(True)
            self.checkbox324.setEnabled(True)
        else:
            self.checkbox323.setEnabled(False)
            self.checkbox324.setEnabled(False)

# //===========================================//
    def onClicked_checkbox314(self):
        print('=== onClicked_checkbox314 ===')
        if (self.checkbox314.isChecked()):
            self.slider314.setEnabled(True)
        else:
            self.slider314.setEnabled(False)

        if (self.checkbox161.isChecked() or self.checkbox162.isChecked() or self.checkbox164.isChecked() or \
            self.checkbox165.isChecked() or self.checkbox166.isChecked() or self.checkbox35.isChecked() or \
            self.checkbox36.isChecked() or self.checkbox37.isChecked() or self.checkbox38.isChecked() or \
            self.checkbox39.isChecked() or self.checkbox310.isChecked() or self.checkbox311.isChecked() or \
            self.checkbox312.isChecked() or self.checkbox313.isChecked() or self.checkbox314.isChecked() or \
            self.checkbox315.isChecked()):
            self.checkbox323.setEnabled(True)
            self.checkbox324.setEnabled(True)
        else:
            self.checkbox323.setEnabled(False)
            self.checkbox324.setEnabled(False)

# //===========================================//
    def onClicked_checkbox315(self):
        print('=== onClicked_checkbox315 ===')
        if (self.checkbox315.isChecked()):
            self.slider315a.setEnabled(True)
            self.slider315b.setEnabled(True)
        else:
            self.slider315a.setEnabled(False)
            self.slider315b.setEnabled(False)

        if (self.checkbox161.isChecked() or self.checkbox162.isChecked() or self.checkbox164.isChecked() or \
            self.checkbox165.isChecked() or self.checkbox166.isChecked() or self.checkbox35.isChecked() or \
            self.checkbox36.isChecked() or self.checkbox37.isChecked() or self.checkbox38.isChecked() or \
            self.checkbox39.isChecked() or self.checkbox310.isChecked() or self.checkbox311.isChecked() or \
            self.checkbox312.isChecked() or self.checkbox313.isChecked() or self.checkbox314.isChecked() or \
            self.checkbox315.isChecked()):
            self.checkbox323.setEnabled(True)
            self.checkbox324.setEnabled(True)
        else:
            self.checkbox323.setEnabled(False)
            self.checkbox324.setEnabled(False)

# //===========================================//
    def update_slider311(self):
        print('=== update_slider311 ===')

# //===========================================//
    def update_slider312(self):
        print('=== update_slider312 ===')

# //===========================================//
    def update_slider313(self):
        print('=== update_slider313 ===')

# //===========================================//
    def update_slider314(self):
        print('=== update_slider314 ===')

# //===========================================//
    def update_slider315a(self):
        print('=== update_slider315a ===')

# //===========================================//
    def update_slider315b(self):
        print('=== update_slider315b ===')
        print('slider315b :=', self.slider315b.value())         # [0-255]

# //===========================================//
    def update_spinbox53(self):
        print('=== update_spinbox53 ===')

    def update_spinbox54(self):
        print('=== update_spinbox54 ===')

    def update_spinbox55(self):
        print('=== update_spinbox55 ===')

    def update_spinbox56(self):
        print('=== update_spinbox56 ===')

    def update_spinbox57(self):
        print('=== update_spinbox57 ===')

    def update_spinbox58a(self):
        print('=== update_spinbox58a ===')

    def update_spinbox58b(self):
        print('=== update_spinbox58b ===')


# //===========================================//
    def update_combobox5(self):
        from src.module.py_window_main import MainGuiWindow
        from src.func.py_main_editor import TextGuiWindow

        print('=== update_combobox5 ===')
        self.btn521.setEnabled(False)
        self.btn522.setEnabled(False)
        self.btn523.setEnabled(False)
        self.btn524.setEnabled(False)
        self.btn525.setEnabled(False)
        self.btn526.setEnabled(False)

        if (self.comboBox5.currentIndex() == 0):
            MainGuiWindow.THEME_LIGHT = "Default"
            MainGuiWindow.ThemeLightColorVar1 = 0
        elif (self.comboBox5.currentIndex() == 1):
            MainGuiWindow.THEME_LIGHT = "Yellow"
            MainGuiWindow.ThemeLightColorVar1 = 1
        elif (self.comboBox5.currentIndex() == 2):
            MainGuiWindow.THEME_LIGHT = "Green"
            MainGuiWindow.ThemeLightColorVar1 = 2
        elif (self.comboBox5.currentIndex() == 3):
            MainGuiWindow.THEME_LIGHT = "Blue"
            MainGuiWindow.ThemeLightColorVar1 = 3
        elif (self.comboBox5.currentIndex() == 4):
            MainGuiWindow.THEME_LIGHT = "Pink"
            MainGuiWindow.ThemeLightColorVar1 = 4
        elif (self.comboBox5.currentIndex() == 5):
            MainGuiWindow.THEME_LIGHT = "Orange"
            MainGuiWindow.ThemeLightColorVar1 = 5
        elif (self.comboBox5.currentIndex() == 6):
            MainGuiWindow.THEME_LIGHT = "Custom"
            MainGuiWindow.ThemeLightColorVar1 = 6
            self.btn521.setEnabled(True)
            self.btn522.setEnabled(True)
            self.btn523.setEnabled(True)
            self.btn524.setEnabled(True)
            self.btn525.setEnabled(True)
            self.btn526.setEnabled(True)
        TextGuiWindow.setThemeLight(self)
        try:
            TextGuiWindow.updateEnabled_icon(self)
        except:
            pass
        self.update_combobox9()

# //===========================================//
    def update_combobox6(self):
        from src.module.py_window_main import MainGuiWindow
        from src.func.py_main_editor import TextGuiWindow

        print('=== update_combobox6 ===')
        self.btn527.setEnabled(False)
        self.btn528.setEnabled(False)
        self.btn529.setEnabled(False)
        self.btn5210.setEnabled(False)
        self.btn5211.setEnabled(False)
        self.btn5212.setEnabled(False)

        if (self.comboBox6.currentIndex() == 0):
            MainGuiWindow.THEME_DARK = "Default"
            MainGuiWindow.ThemeDarkColorVar1 = 0
        elif (self.comboBox6.currentIndex() == 1):
            MainGuiWindow.THEME_DARK = "Yellow"
            MainGuiWindow.ThemeDarkColorVar1 = 1
        elif (self.comboBox6.currentIndex() == 2):
            MainGuiWindow.THEME_DARK = "Green"
            MainGuiWindow.ThemeDarkColorVar1 = 2
        elif (self.comboBox6.currentIndex() == 3):
            MainGuiWindow.THEME_DARK = "Blue"
            MainGuiWindow.ThemeDarkColorVar1 = 3
        elif (self.comboBox6.currentIndex() == 4):
            MainGuiWindow.THEME_DARK = "Pink"
            MainGuiWindow.ThemeDarkColorVar1 = 4
        elif (self.comboBox6.currentIndex() == 5):
            MainGuiWindow.THEME_DARK = "Orange"
            MainGuiWindow.ThemeDarkColorVar1 = 5
        elif (self.comboBox6.currentIndex() == 6):
            MainGuiWindow.THEME_DARK = "Custom"
            MainGuiWindow.ThemeDarkColorVar1 = 6
            self.btn527.setEnabled(True)
            self.btn528.setEnabled(True)
            self.btn529.setEnabled(True)
            self.btn5210.setEnabled(True)
            self.btn5211.setEnabled(True)
            self.btn5212.setEnabled(True)
        TextGuiWindow.setThemeDark(self)
        try:
            TextGuiWindow.updateEnabled_icon(self)
        except:
            pass
        self.update_combobox9()


# //===========================================//
    def SetColorTBThemeLight(self):
        from src.module.py_window_main import MainGuiWindow
        from src.func.py_main_editor import TextGuiWindow

        global FLAG_TBTHEMELIGHT

        print('=== SetColorTBThemeLight ===')
        TextGuiWindow.setThemeLight(self)
        color_selected_LightTB = QColorDialog.getColor()

        if color_selected_LightTB.isValid():
            print('color_selected_LightTB := ', str(color_selected_LightTB.name()))
            FLAG_TBTHEMELIGHT = True
            MainGuiWindow.TB_COLOR_LIGHT_CUSTOM = str(color_selected_LightTB.name())

        TextGuiWindow.setThemeLight(self)


# //===========================================//
    def SetColorFGThemeLight(self):
        from src.module.py_window_main import MainGuiWindow
        from src.func.py_main_editor import TextGuiWindow

        global FLAG_FGTHEMELIGHT

        print('=== SetColorFGThemeLight ===')
        TextGuiWindow.setThemeLight(self)
        color_selected_LightFG = QColorDialog.getColor()

        if color_selected_LightFG.isValid():
            print('color_selected_LightFG := ', str(color_selected_LightFG.name()))
            FLAG_FGTHEMELIGHT = True
            MainGuiWindow.FG_COLOR_LIGHT_CUSTOM = str(color_selected_LightFG.name())

        TextGuiWindow.setThemeLight(self)



# //===========================================//
    def SetColorBGThemeLight(self):
        from src.module.py_window_main import MainGuiWindow
        from src.func.py_main_editor import TextGuiWindow

        global FLAG_BGTHEMELIGHT

        print('=== SetColorBGThemeLight ===')
        TextGuiWindow.setThemeLight(self)
        color_selected_LightBG = QColorDialog.getColor()

        if color_selected_LightBG.isValid():
            print('color_selected_LightBG := ', str(color_selected_LightBG.name()))
            FLAG_BGTHEMELIGHT = True
            MainGuiWindow.BG_COLOR_LIGHT_CUSTOM = str(color_selected_LightBG.name())
        self.close()
        TextGuiWindow.repaint(self)
        self.show()


# //===========================================//
    def SetColorFontThemeLight(self):
        from src.module.py_window_main import MainGuiWindow
        from src.func.py_main_editor import TextGuiWindow

        global FLAG_FONTTHEMELIGHT

        print('=== SetColorFontThemeLight ===')
        TextGuiWindow.setThemeLight(self)
        color_selected_LightFont = QColorDialog.getColor()

        if color_selected_LightFont.isValid():
            print('color_selected_LightFont := ', str(color_selected_LightFont.name()))
            FLAG_FONTTHEMELIGHT = True
            MainGuiWindow.FONT_COLOR_LIGHT_CUSTOM = str(color_selected_LightFont.name())

        TextGuiWindow.setThemeLight(self)


# //===========================================//
    def SetColorBTThemeLight(self):
        from src.module.py_window_main import MainGuiWindow
        from src.func.py_main_editor import TextGuiWindow

        global FLAG_BTTHEMELIGHT

        print('=== SetColorBTThemeLight ===')
        TextGuiWindow.setThemeLight(self)
        color_selected_LightBT = QColorDialog.getColor()

        if color_selected_LightBT.isValid():
            print('color_selected_LightBT := ', str(color_selected_LightBT.name()))
            FLAG_BTTHEMELIGHT = True
            MainGuiWindow.BT_COLOR_LIGHT_CUSTOM = str(color_selected_LightBT.name())

        TextGuiWindow.setThemeLight(self)


# //===========================================//
    def SetColorBDThemeLight(self):
        from src.module.py_window_main import MainGuiWindow
        from src.func.py_main_editor import TextGuiWindow

        global FLAG_BDTHEMELIGHT

        print('=== SetColorBDThemeLight ===')
        TextGuiWindow.setThemeLight(self)
        color_selected_LightBD = QColorDialog.getColor()

        if color_selected_LightBD.isValid():
            print('color_selected_LightBD := ', str(color_selected_LightBD.name()))
            FLAG_BDTHEMELIGHT = True
            MainGuiWindow.BD_COLOR_LIGHT_CUSTOM = str(color_selected_LightBD.name())

        TextGuiWindow.setThemeLight(self)


# //===========================================//
    def SetColorTBThemeDark(self):
        from src.module.py_window_main import MainGuiWindow
        from src.func.py_main_editor import TextGuiWindow
        global FLAG_FGTHEMEDARK

        print('=== SetColorTBThemeDark ===')
        TextGuiWindow.setThemeDark(self)
        color_selected_DarkTB = QColorDialog.getColor()

        if color_selected_DarkTB.isValid():
            print('color_selected_DarkTB := ', str(color_selected_DarkTB.name()))
            FLAG_TBTHEMEDARK = True
            MainGuiWindow.TB_COLOR_DARK_CUSTOM = str(color_selected_DarkTB.name())

        TextGuiWindow.setThemeDark(self)


# //===========================================//
    def SetColorFGThemeDark(self):
        from src.module.py_window_main import MainGuiWindow
        from src.func.py_main_editor import TextGuiWindow
        global FLAG_FGTHEMEDARK

        print('=== SetColorFGThemeDark ===')
        TextGuiWindow.setThemeDark(self)
        color_selected_DarkFG = QColorDialog.getColor()

        if color_selected_DarkFG.isValid():
            print('color_selected_DarkFG := ', str(color_selected_DarkFG.name()))
            FLAG_FGTHEMEDARK = True
            MainGuiWindow.FG_COLOR_DARK_CUSTOM = str(color_selected_DarkFG.name())

        TextGuiWindow.setThemeDark(self)


# //===========================================//
    def SetColorBGThemeDark(self):
        from src.module.py_window_main import MainGuiWindow
        from src.func.py_main_editor import TextGuiWindow
        global FLAG_BGTHEMEDARK

        print('=== SetColorBGThemeDark ===')
        TextGuiWindow.setThemeDark(self)
        color_selected_DarkBG = QColorDialog.getColor()

        if color_selected_DarkBG.isValid():
            print('color_selected_DarkBG := ', str(color_selected_DarkBG.name()))
            FLAG_BGTHEMEDARK = True
            MainGuiWindow.BG_COLOR_DARK_CUSTOM = str(color_selected_DarkBG.name())

        self.close()
        TextGuiWindow.repaint(self)
        self.show()


# //===========================================//
    def SetColorFontThemeDark(self):
        from src.module.py_window_main import MainGuiWindow
        from src.func.py_main_editor import TextGuiWindow
        global FLAG_FONTTHEMEDARK

        print('=== SetColorFontThemeDark ===')
        TextGuiWindow.setThemeDark(self)
        color_selected_DarkFont = QColorDialog.getColor()
        if color_selected_DarkFont.isValid():
            print('color_selected_DarkFont := ', str(color_selected_DarkFont.name()))
            FLAG_FONTTHEMEDARK = True
            MainGuiWindow.FONT_COLOR_DARK_CUSTOM = str(color_selected_DarkFont.name())
        TextGuiWindow.setThemeDark(self)


# //===========================================//
    def SetColorBTThemeDark(self):
        from src.module.py_window_main import MainGuiWindow
        from src.func.py_main_editor import TextGuiWindow
        global FLAG_BTTHEMEDARK

        print('=== SetColorBTThemeDark ===')
        TextGuiWindow.setThemeDark(self)
        color_selected_DarkBT = QColorDialog.getColor()

        if color_selected_DarkBT.isValid():
            print('color_selected_DarkBT := ', str(color_selected_DarkBT.name()))
            FLAG_BTTHEMEDARK = True
            MainGuiWindow.BT_COLOR_DARK_CUSTOM = str(color_selected_DarkBT.name())
        TextGuiWindow.setThemeDark(self)


# //===========================================//
    def SetColorBDThemeDark(self):
        from src.module.py_window_main import MainGuiWindow
        from src.func.py_main_editor import TextGuiWindow
        global FLAG_BDTHEMEDARK

        print('=== SetColorBDThemeDark ===')
        TextGuiWindow.setThemeDark(self)
        color_selected_DarkBD = QColorDialog.getColor()

        if color_selected_DarkBD.isValid():
            print('color_selected_DarkBD := ', str(color_selected_DarkBD.name()))
            FLAG_BDTHEMEDARK = True
            MainGuiWindow.BD_COLOR_DARK_CUSTOM = str(color_selected_DarkBD.name())
        TextGuiWindow.setThemeDark(self)


# //===========================================//
    def SetRubberbandBDColor(self):
        from src.module.py_window_main import MainGuiWindow

        print('=== SetRubberbandBDColor ===')
        color_selected_BD = QColorDialog.getColor()
        if color_selected_BD.isValid():
            print('color_selected_BD := ', str(color_selected_BD.name()))
            MainGuiWindow.flag_rubberband_init = False
            MainGuiWindow.color_rubberband = color_selected_BD
            MainGuiWindow.RBBColorVar1 = str(MainGuiWindow.color_rubberband.name())
            MainGuiWindow.setRubberBandColor(self)


# //===========================================//
    def update_combobox8(self):
        from src.module.py_window_main import MainGuiWindow
        from src.func.py_main_editor import TextGuiWindow

        print('=== update_combobox8 ===')
        if (self.comboBox8.currentIndex() == 0):
            MainGuiWindow.FontSystemSizeVar1 = 7
        elif (self.comboBox8.currentIndex() == 1):
            MainGuiWindow.FontSystemSizeVar1 = 8
        elif (self.comboBox8.currentIndex() == 2):
            MainGuiWindow.FontSystemSizeVar1 = 9

        font_system = QFont()
        font_system.setPointSize(MainGuiWindow.FontSystemSizeVar1)
        QApplication.setFont(font_system)

        if MainGuiWindow.THEME == 'light':
            TextGuiWindow.setThemeLight(self)

        if MainGuiWindow.THEME == 'dark':
            TextGuiWindow.setThemeDark(self)

        self.label11.adjustSize()
        self.label121.adjustSize()
        self.label131.adjustSize()
        self.label141.adjustSize()
        self.label151.adjustSize()
        self.label221.adjustSize()
        self.label311.adjustSize()
        self.label312.adjustSize()
        self.label41.adjustSize()
        self.label42.adjustSize()
        self.label511.adjustSize()
        self.label521.adjustSize()
        self.label523.adjustSize()
        self.label524.adjustSize()
        self.label531.adjustSize()
        self.label61.adjustSize()
        self.label64.adjustSize()

        self.label11.setFixedHeight(15)
        self.label121.setFixedHeight(15)
        self.label131.setFixedHeight(15)
        self.label141.setFixedHeight(15)
        self.label151.setFixedHeight(15)
        self.label221.setFixedHeight(15)
        self.label311.setFixedHeight(15)
        self.label312.setFixedHeight(15)
        self.label41.setFixedHeight(15)
        self.label42.setFixedHeight(15)
        self.label511.setFixedHeight(15)
        self.label521.setFixedHeight(15)
        self.label523.setFixedHeight(15)
        self.label524.setFixedHeight(15)
        self.label531.setFixedHeight(15)
        self.label61.setFixedHeight(15)
        self.label64.setFixedHeight(15)

        try:
            TextGuiWindow.labelStatusbar1.setFont(QFont('Arial', MainGuiWindow.FontSystemSizeVar1))
            TextGuiWindow.labelStatusbar2.setFont(QFont('Arial', MainGuiWindow.FontSystemSizeVar1))
            TextGuiWindow.labelStatusbar3.setFont(QFont('Arial', MainGuiWindow.FontSystemSizeVar1))
        except:
            pass


# //===========================================//
    def update_combobox9(self):
        from src.module.py_window_main import MainGuiWindow
        from src.func.py_main_editor import TextGuiWindow

        print('=== update_combobox9 ===')
        if (self.comboBox9.currentIndex() == 0):
            MainGuiWindow.BorderStyleVar1 = 0
        elif (self.comboBox9.currentIndex() == 1):
            MainGuiWindow.BorderStyleVar1 = 1

        if MainGuiWindow.THEME == 'light':
            TextGuiWindow.setThemeLight(self)
        if MainGuiWindow.THEME == 'dark':
            TextGuiWindow.setThemeDark(self)


# //===========================================//
    def update_combobox11(self):
        from src.module.py_window_main import MainGuiWindow
        from src.func.py_main_editor import TextGuiWindow

        print('=== update_combobox11 ===')
        if (self.comboBox11.currentIndex() == 0):
            MainGuiWindow.TextEditorIconSizeVar1 = 16
        elif (self.comboBox11.currentIndex() == 1):
            MainGuiWindow.TextEditorIconSizeVar1 = 18
        elif (self.comboBox11.currentIndex() == 2):
            MainGuiWindow.TextEditorIconSizeVar1 = 22

        if MainGuiWindow.THEME == 'light':
            TextGuiWindow.setThemeLight(self)
        if MainGuiWindow.THEME == 'dark':
            TextGuiWindow.setThemeDark(self)

        MainGuiWindow.flag_resize_window = True


# //===========================================//
    def update_combobox12(self):
        from src.module.py_window_main import MainGuiWindow

        print('=== update_combobox12 ===')
        if (self.comboBox12.currentIndex() == 0):
            MainGuiWindow.TextEditorStatusBarVar1 = 0
        elif (self.comboBox12.currentIndex() == 1):
            MainGuiWindow.TextEditorStatusBarVar1 = 1


# //===========================================//
    def update_combobox13(self):
        from src.module.py_window_main import MainGuiWindow

        print('=== update_combobox13 ===')
        if (self.comboBox13.currentIndex() == 0):
            MainGuiWindow.TextEditorModeVar1 = 0
        elif (self.comboBox13.currentIndex() == 1):
            MainGuiWindow.TextEditorModeVar1 = 1
        print('TextEditorModeVar1 : = ', MainGuiWindow.TextEditorModeVar1)


#########################################################################
    def mousePressEvent(self, event):
        print('=== mousePressEvent ===')

    def mouseMoveEvent(self, event):
        global w2, h2
        print('=== mouseMoveEvent ===')
        SettingWindow.w2 = self.frameGeometry().width()
        SettingWindow.h2 = self.frameGeometry().height()
        print('w2 := ', SettingWindow.w2)
        print('h2 := ', SettingWindow.h2)

    def mouseReleaseEvent(self, event):
        print('=== mouseReleaseEvent ===')

    def mouseDoubleClickEvent(self, event):
        pass

    #//===================================================//
    def paintEvent(self, event=None):
        painter = QPainter(self)
        self.setBackgroundColor(painter)
        self.setBorderStyle()

    #//===================================================//
    def setBackgroundColor(self,painter):
        from src.module.py_window_main import MainGuiWindow

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


    def enterEvent(self, event):
        print("=== enterEvent (SettingWindow) ===")
        self.setCursor(Qt.CursorShape.ArrowCursor)

    def closeEvent(self, event: QCloseEvent) -> None:
        print('=== closeEvent ===')

    #//==========================================================//
    def setBorderStyle(self):
        from src.module.py_window_main import MainGuiWindow

        global radius
        if (MainGuiWindow.BorderStyleVar1 == 0):
            radius = 0
        elif (MainGuiWindow.BorderStyleVar1 == 1):
            radius = 5
        path = QPainterPath()
        rect = QRectF(self.rect()).adjusted(0.5,0.5,-0.5,-0.5)
        path.addRoundedRect(rect, radius, radius)
        region = QRegion(path.toFillPolygon(QTransform()).toPolygon())
        self.setMask(region)

    #//==========================================================//
    def keyPressEvent(self, event):
        print('=== keyPressEvent ===')
        if (event.key() == Qt.Key.Key_Escape):
            print('=== Esc ===')
            self.CancelSetting()

########################################################################




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
        w1 = 370        # Window width
        h1 = 675        # Window height

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
########################################################################



# ########################################################################
class CheckableComboBox(QComboBox):
    def __init__(self, parent=None):
        super(CheckableComboBox, self).__init__(parent)

        self.text1 = []
        self.view().pressed.connect(self.handleItemPressed)
        self.view().pressed.connect(self.currentData)
        self.setModel(QStandardItemModel(self))

    def handleItemPressed(self, index):
        global itemVar

        # print('index := ', index)
        item = self.model().itemFromIndex(index)
        if item.checkState() == Qt.Checked:
            item.setCheckState(Qt.CheckState.Unchecked)
        else:
            item.setCheckState(Qt.CheckState.Checked)

    def currentData(self):
        result = []
        texts = []
        for i in range(self.model().rowCount()):
            if self.model().item(i).checkState() == Qt.CheckState.Checked:
                texts.append(self.model().item(i).text())
        text = texts
        self.text1 = ", ".join(text)
        result = list(text)
        return result

########################################################################

# Import necessary libraries and modules
import time                                     # For measuring execution time
import pytesseract                              # For OCR (Optical Character Recognition)
import pyautogui                                # For taking screenshots
import numpy as np                              # For numerical operations
import cv2                                      # For OpenCV operations
from PIL import ImageFont, ImageDraw, Image     # For image manipulation and drawing text
from pytesseract import Output                  # For structured OCR output
from src.module.py_window_main import *             # Import GUI-related configurations and variables
from src.resource.resources_rc import *             # Import resources (e.g., fonts, images)

# Constants for UI layout
HEIGHT_TT = 30      # Height of the title bar
HEIGHT_TB = 30      # Height of the toolbar



########################################################################
class UIFunctions(MainGuiWindow):
    """
    This class contains various functions for image processing, OCR detection,
    and UI updates in a PyQt5 application.
    It includes methods for taking screenshots, detecting text orientation,
    highlighting text in images, and displaying detected text in a separate window.
    """

    #//===================================================//
    def printScreen(self):
        """
        Captures a screenshot of the current screen and converts it to a CV2 image.
        """
        global image
        print('=== printScreen ===')
        image = pyautogui.screenshot()
        image = cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR)

    #//=========================================================//
    def setScreenImage(self):
        """
        Sets the captured screenshot as the background image in the UI.
        """
        from src.func.py_main_image_processing import UIFunctionsImage

        print('=== setScreenImage ===')
        self.bg = QFrame(self)
        self.bg.setGeometry(0,0,WIDTH,HEIGHT)
        self.pic = QLabel(self.bg)
        self.pic.setBackgroundRole(QPalette.Base)
        self.pic.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.pic.setScaledContents(True)
        self.image = QtGui.QImage()
        self.cv2Image = image
        self.selectedImage = None
        self.image = UIFunctionsImage.convertCv2ToQimage(self, self.cv2Image)
        self.pic.setPixmap(QtGui.QPixmap.fromImage(self.image))
        self.pic.setMouseTracking(True)

    #//===================================================//
    def showImageArea(self):
        """
        Displays the selected image in a separate CV2 window.
        """
        print('=== showImageArea ===')
        if self.selectedImage is None:
            print("Error: No image selected to display.")
            return
        cv2.imshow('Selected Image', self.selectedImage)
        cv2.waitKey(0)

    #//===================================================//
    def detect_osd_ocr(self):
        """
        Detects the orientation and script direction of the selected image using Tesseract OSD.
        """
        from src.module.py_window_main import flag_config, flag_language
        global text
        global img1

        print('=== detect_osd_ocr ===')
        img1 = self.selectedImage
        osd = pytesseract.image_to_osd(img1, config='--psm 0 --dpi 300 -c min_characters_to_try=2')
        osd_list = [int(i) for i in osd.split() if i.isdigit()]
        angle_orientation = int(abs(osd_list[2]-180))
        return angle_orientation

    #//===================================================//
    def detect_orientation(self, image):
        """
        Detects the orientation of the image based on pixel distribution.
        """
        global img1

        print('=== detect_orientation ===')
        img1 = image
        mask = np.zeros(img1.shape, dtype=np.uint8)
        blur = cv2.GaussianBlur(img1, (3,3), 0)
        adaptive = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,15,4)
        cnts = cv2.findContours(adaptive, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if len(cnts) == 2 else cnts[1]

        for c in cnts:
            area = cv2.contourArea(c)
            if area < 45000 and area > 20:      # Filter contours by area
                cv2.drawContours(mask, [c], -1, (255,255,255), -1)

        h, w = mask.shape
        if w > h:                       # Landscape orientation
            left = mask[0:h, 0:0+w//2]
            right = mask[0:h, w//2:]
            left_pixels = cv2.countNonZero(left)
            right_pixels = cv2.countNonZero(right)
            return 0 if left_pixels >= right_pixels else 180
        else:                           # Portrait orientation
            top = mask[0:h//2, 0:w]
            bottom = mask[h//2:, 0:w]
            top_pixels = cv2.countNonZero(top)
            bottom_pixels = cv2.countNonZero(bottom)
            return 90 if bottom_pixels >= top_pixels else 270

    #//===================================================//
    def detect_text_ocr(self,img1):
        """
        Detects text in the given image using Tesseract OCR.
        Applies optional post-processing to remove extra spaces or line breaks.
        """
        from src.module.py_window_main import flag_config, flag_language
        from src.module.py_window_main import PageLayoutRemoveSpaceVar1, PageLayoutRemoveLineVar1

        # print("=====================================================================")
        print('=== detect_text_ocr (begin) ===')
        time_start = time.time()

        print('- flag_config := ', flag_config)
        print('- flag_language := ', flag_language)

        # Perform OCR on the image
        UIFunctions.text = pytesseract.image_to_string(img1, lang = flag_language, config = flag_config)
        UIFunctions.text = UIFunctions.text.strip()

        # Remove extra line breaks if enabled
        if (PageLayoutRemoveLineVar1  == 1):
            UIFunctions.remove_ExtraCRLF(self)

        if (PageLayoutRemoveSpaceVar1 == 1):
            UIFunctions.remove_ExtraSpace(self)

        if UIFunctions.text is not None:
            print('***************************************')
            print('text := ', UIFunctions.text)
            print('***************************************')
        else:
            print("Error: OCR cannot detect Text!")

        time_end = time.time()
        print("*** detect_text_ocr (end): %0.3f seconds ***" %(time_end - time_start))
        # print("====================================================================")

    #//===================================================//
    def remove_ExtraCRLF(self):
        """
        Removes extra line breaks from the detected text.
        """
        print('=== remove_ExtraCRLF ===')
        if ('\n\n' in UIFunctions.text):
            while ('\n\n' in UIFunctions.text):
                UIFunctions.text = UIFunctions.text.replace('\n\n','\n')

    #//===================================================//
    def remove_ExtraSpace(self):
        """
        Removes extra spaces from the detected text.
        """
        print('=== remove_ExtraSpace ===')
        if ('  ' in UIFunctions.text):
            while ('  ' in UIFunctions.text):
                UIFunctions.text = UIFunctions.text.replace('  ',' ')

    #//=========================================================//
    # Color Image
    #//=========================================================//
    def highlight_text_ocr(self,img1):
        """
        Highlights detected text in a color image by drawing bounding boxes around text regions.
        """
        global img1n, img1m
        global h1, w1, c1, b1, boxes1

        print('=== highlight_text_ocr ===')
        cv2.imshow('Original Image', img1)
        img1n = img1.copy()
        h1, w1, c1 = img1n.shape
        img1n = cv2.cvtColor(img1n,cv2.COLOR_BGR2RGB)
        boxes1 = pytesseract.image_to_boxes(img1n)
        for b1 in boxes1.splitlines():
            b1 = b1.split(' ')
            img1m = cv2.rectangle(img1n, (int(b1[1]), h1 - int(b1[2])), (int(b1[3]), h1 - int(b1[4])), (0,255,0),1)
        cv2.imshow('Highlighted Image', img1m)

    #//=========================================================//
    # Grey Image
    #//=========================================================//
    def highlight_text_ocr1(self,img3):
        """
        Highlights detected text in a grey image by drawing bounding boxes around text regions.
        """
        global img3m, img3n
        global h3, w3, b3, boxes3

        print('=== highlight_text_ocr1 ===')
        cv2.imshow('Original Image', img3)
        img3n = img3.copy()
        h3, w3 = img3n.shape
        img3n = cv2.cvtColor(img3n,cv2.COLOR_GRAY2RGB)
        boxes3 = pytesseract.image_to_boxes(img3n)
        for b3 in boxes3.splitlines():
            b3 = b3.split(' ')
            img3m = cv2.rectangle(img3n, (int(b3[1]), h3 - int(b3[2])), (int(b3[3]), h3 - int(b3[4])), (0,255,0),1)

        cv2.imshow('Highlighted Image', img3m)

    #//=========================================================//
    def highlight_box_ocr(self,img2):
        """
        Highlights detected text in a color image using OCR data with confidence scores.
        """
        global img2m, img2n
        global h2, w2, c2, boxes2, data2

        print('=== highlight_box_ocr ===')
        cv2.imshow('Original Image', img2)
        img2n = img2.copy()
        h2, w2, c2 = img2n.shape
        img2n = cv2.cvtColor(img2n,cv2.COLOR_BGR2RGB)
        data2 = pytesseract.image_to_data(img2n,output_type=Output.DICT)
        print(data2.keys())
        print(data2['conf'])

        boxes2 = len(data2['text'])
        for i in range(boxes2):
            if int(data2['conf'][i]) >= 0:  # Only highlight text with valid confidence
                (x, y, w2, h2) = (data2['left'][i], data2['top'][i], data2['width'][i], data2['height'][i])
                img2m = cv2.rectangle(img2n, (x, y), (x + w2, y + h2), (0, 255, 0), 1)

        cv2.imshow('Highlighted Image', img2m)

    #//=========================================================//
    def highlight_box_ocr1(self,img4):
        """
        Highlights detected text in a grey image using OCR data with confidence scores.
        """
        global img4m, img4n
        global h4, w4, c4, boxes4, data4

        print('=== highlight_box_ocr ===')
        cv2.imshow('Original Image', img4)
        img4n = img4.copy()
        h4, w4 = img4n.shape
        img4n = cv2.cvtColor(img4n,cv2.COLOR_GRAY2RGB)
        data4 = pytesseract.image_to_data(img4n,output_type=Output.DICT)
        print(data4.keys())
        print(data4['conf'])

        boxes4 = len(data4['text'])
        for i in range(boxes4):
            if int(data4['conf'][i]) >= 0:
                (x, y, w4, h4) = (data4['left'][i], data4['top'][i], data4['width'][i], data4['height'][i])
                img4m = cv2.rectangle(img4n, (x, y), (x + w4, y + h4), (0, 255, 0), 1)

        cv2.imshow('Highlighted Image', img4m)

    # #//===================================================//
    # def display_text_ocr(self):
    #     """
    #     Displays the detected text on the image using PIL for rendering.
    #     """
    #     from py_main_gui import xPos, yPos

    #     print('=== display_text_ocr ===')
    #     img2n = self.cv2Image
    #     imgHeight, imgWidth, c = img2n.shape

    #     # Draw text on the image
    #     fill_ink = (5, 255, 5, 5)      # Text color (r, g, b)
    #     img_cv2_rgb = cv2.cvtColor(img2n, cv2.COLOR_BGR2RGB)
    #     img_pil = Image.fromarray(img_cv2_rgb)
    #     img_draw = ImageDraw.Draw(img_pil)
    #     font1 = ImageFont.truetype(":/resources/font/boon.ttf", 13)
    #     img_draw.multiline_text((xPos, yPos), text, font=font1, fill=fill_ink,spacing=8,anchor='mm')

    #     # Convert PIL image back to OpenCV BGR format
    #     img2n = cv2.cvtColor(np.array(img_pil),cv2.COLOR_RGB2BGR)
    #     self.cv2Imagen = img2n

    #//=========================================================//
    def show_text_ocr(self):
        """
        Opens a new text editor window to display the detected text.
        """
        from src.func.py_main_editor import TextGuiWindow
        print('=== show_text_ocr ===')
        self.TextWindow = TextGuiWindow()
        self.TextWindow.show()

    #//=========================================================//
    def updateScreen(self):
        """
        Updates the displayed image with the modified version.
        """
        print('=== updateScreen ===')
        self.image = self.convertCv2ToQimage(self.cv2Imagen)
        self.pic.setPixmap(QtGui.QPixmap.fromImage(self.image))

    #//=========================================================//
    def updateScreenOriginal(self):
        """
        Restores the original image on the screen.
        """
        self.image = self.convertCv2ToQimage(self.cv2Image)
        self.pic.setPixmap(QtGui.QPixmap.fromImage(self.image))

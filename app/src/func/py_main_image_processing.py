# Importing necessary libraries
import math                 # For mathematical operations
import numpy as np          # For numerical computations
import cv2                  # For image processing
from src.module.py_window_main import *   # Import all components from py_main_gui



##################################################################
# Basic Image Processing Functions
##################################################################
class UIFunctionsImage(MainGuiWindow):
    """
    A class containing basic image processing functions.
    """

    def __init__(self):
        """
        Initializes the main GUI window.
        """
        super().__init__()

    #//=======================================================//
    def convertQImageToMat(self, img):
        """
        Converts a QImage into an OpenCV MAT format.
        - Converts the QImage to a 4-channel format (ARGB).
        - Returns the matrix in grayscale format.
        Args:
            incomingImage: QImage to be converted.
        Returns:
            OpenCV grayscale image (MAT format).
        """
        print('=== convertQImageToMat ===')
        img = img.convertToFormat(4)  # Convert to ARGB format
        width = img.width()
        height = img.height()
        ptr = img.bits()  # Access raw image data
        ptr.setsize(img.byteCount())  # Set the size of the data buffer
        arr = np.array(ptr).reshape(height, width, 4)  # Reshape to a 4-channel image
        return cv2.cvtColor(arr, cv2.COLOR_BGR2GRAY)  # Convert to grayscale and return

    #//=======================================================//
    def convertCv2ToQimage(self, img):
        """
        Converts an OpenCV image (MAT format) to a QImage for use in PyQt5.
        - Supports grayscale, BGR, and ARGB formats.
        - Handles images with 8-bit depth (uint8).
        Args:
            im: OpenCV image to be converted.
        Returns:
            QImage representation of the input image.
        """
        print('=== convertCv2ToQimage ===')
        qimg = QImage()  # Initialize an empty QImage
        if img is None:
            return qimg  # Return an empty QImage if the input image is None
        if img.dtype == np.uint8:  # Check if the image has 8-bit depth
            if len(img.shape) == 2:  # Grayscale image
                qimg = QImage(img.data, img.shape[1], img.shape[0], img.strides[0], QImage.Format_Indexed8)
                qimg.setColorTable([qRgb(i, i, i) for i in range(256)])  # Set grayscale color table
            elif len(img.shape) == 3:  # Color image
                if img.shape[2] == 3:  # BGR format
                    qimg = QImage(img.data, img.shape[1], img.shape[0], img.strides[0], QImage.Format_BGR888)
                elif img.shape[2] == 4:  # ARGB format
                    qimg = QImage(img.data, img.shape[1], img.shape[0], img.strides[0], QImage.Format_ARGB32)
        return qimg  # Return the converted QImage

    #//===================================================//
    def cropImage(self, rect):
        """
        Crops a portion of the image based on the given rectangle.
        - Converts the cropped image to a format suitable for further processing.
        """
        print('=== cropImage ===')
        croppedImage = self.image.copy(rect)
        return UIFunctionsImage.convertQImageToMat(self, croppedImage)

    #//===================================================//
    def inverting(self, image):
        """
        Inverts the colors of the input image.
        """
        print('=== inverting ===')
        image_inverted = cv2.bitwise_not(image)
        return image_inverted

    #//===================================================//
    def resize_image(self, image, scale_percent):
        """
        Resizes the input image by a given scale percentage.
        """
        print('=== resize_image ===')
        height, width = image.shape[:2]
        width1 = int(image.shape[1] * scale_percent/100)
        height1 = int(image.shape[0] * scale_percent/100)
        dimension1 = (width1, height1)
        image_resized = cv2.resize(image, dimension1, interpolation=cv2.INTER_AREA)
        return image_resized

    #//===================================================//
    def crop_image(self, image, WidthRatio, HeigthRatio):
        """
        Crops the input image based on width and height ratios.
        """
        print('=== crop_image ===')
        width, height = image.shape[1], image.shape[0]
        dim = int(WidthRatio*width/10), int(HeigthRatio*height/10)
        crop_width = dim[0] if dim[0] < image.shape[1] else image.shape[1]
        crop_height = dim[1] if dim[1] < image.shape[0] else image.shape[0]
        mid_x, mid_y = int(width/2), int(height/2)
        cw2, ch2 = int(crop_width/2), int(crop_height/2)
        image_crop = image[mid_y-ch2:mid_y+ch2, mid_x-cw2:mid_x+cw2]
        return image_crop

    #//===================================================//
    def contrast_high1(self, image):
        """
        Enhances the contrast of a grayscale image.
        """
        print('=== contrast_high1 ===')
        min = image.min()
        max= image.max()
        Range = max - min
        for i in range(int(image.shape[0])):
            for j in range(int(image.shape[1])):
                image[i][j] = (image[i][j] - min) * (255/Range)
        image_contrast_high1 = image
        return image_contrast_high1

    #//===================================================//
    def sharpen2(self, image, ksize):
        """
        Sharpens the input image using a kernel.
        """
        print('=== sharpen2 ===')
        kernel = np.array([[-1,-1,-1], [-1,ksize,-1], [-1,-1,-1]])
        image_sharpen2 = cv2.filter2D(image, -1, kernel)
        return (image_sharpen2)

    ##############################################
    # Making Borders for Images (Padding)
    ##############################################

    #//===================================================//
    def bordermake_image(self, image):
        """
        Adds a border around the input image.
        """
        print('=== bordermake_image ===')
        color = [255,255,255]
        height, width = image.shape[:2]
        print('h,w := ',height,width)
        dimension = (width, height)
        image_bordermake = cv2.copyMakeBorder(image, int(height/3), int(height/3), int(width/3), int(width/3), cv2.BORDER_REPLICATE)
        return image_bordermake

    ##############################################
    # Image Roation
    ##############################################

    #//===================================================//
    def deskew_angle(self, image):
        """
        Calculates the skew angle of the input image.
        """
        print('=== deskew_angle ===')
        height, width = image.shape[:2]
        if len(image.shape) == 3:
            height, width, _ = image.shape
        elif len(image.shape) == 2:
            height, width = image.shape
        else:
            print('Error: Unsupported image type')

        img = cv2.medianBlur(image, 3)
        edges = cv2.Canny(img, threshold1=30, threshold2=100, apertureSize=3, L2gradient=True)
        lines = cv2.HoughLinesP(edges, 1, math.pi/180, 30, minLineLength=width / 4.0, maxLineGap=height /4.0)
        angle = 0.0
        cnt = 0
        for x1, y1, x2, y2 in lines[0]:
            ang = np.arctan2(y2-y1, x2-x1)
            if math.fabs(ang) <= 30:
                angle += ang
                cnt += 1

        if cnt == 0:
            return 0.0
        angle_deskew = (angle / cnt)*180/math.pi
        return angle_deskew

    #//===================================================//
    def deskew(self, image, angle_deskew):
        """
        Corrects the skew of the input image based on the given angle.
        """
        print('=== deskew ===')
        (h, w) = image.shape[:2]
        center = (w // 2, h // 2)
        M = cv2.getRotationMatrix2D(center, angle_deskew, 1.0)
        rotated_image = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
        return rotated_image

    #//===================================================//
    def rotate_image_deg1(self, image, angle):
        """
        Rotates the input image by a specified angle.
        """
        print('=== rotate_image_deg1 ===')
        color = [255,255,255]
        height, width = image.shape[:2]
        image_center = (width/2,height/2)
        rotation_mat = cv2.getRotationMatrix2D(image_center, angle, 1)
        radians = math.radians(angle)
        sin = math.sin(radians)
        cos = math.cos(radians)

        # calculate the new bounding dimensions of the image
        bound_w = int((height * abs(sin)) + (width * abs(cos)))
        bound_h = int((height * abs(cos)) + (width * abs(sin)))

        # adjust the rotation matrix to account for translation
        rotation_mat[0,2] += ((bound_w / 2) - image_center[0])
        rotation_mat[1,2] += ((bound_h / 2) - image_center[1])

        # perform the rotation and return the image
        image_rotated = cv2.warpAffine(image, rotation_mat, (bound_w, bound_h), borderMode=cv2.BORDER_CONSTANT, borderValue=color)
        return image_rotated

    #//===================================================//
    def rotate_image180(self, image):
        """
        Rotates the input image by 180 degrees.
        """
        print('=== rotate_image180 ===')
        image_rotated = cv2.rotate(image, cv2.ROTATE_180)
        return image_rotated

    ##################################################################
    # denoise
    ##################################################################

    #//===================================================//
    def denoising_fast(self, image, h, templatewindowsize, searchwindowsize):
        """
        Removes noise from the input image using fast non-local means denoising.
        Args:
            image: Input image to be denoised.
            h: Filter strength for noise removal.
            templatewindowsize: Size of the template patch used for denoising.
            searchwindowsize: Size of the search window used for denoising.
        Returns:
            image_denoising_fast: The denoised image.
        """
        print('=== denoising_fast ===')
        image_denoising_fast = cv2.fastNlMeansDenoising(image, None, h, templatewindowsize, searchwindowsize)
        return (image_denoising_fast)

    ##############################################
    # Image Thresholding
    ##############################################

    #//===================================================//
    def thresholdFcn(self, image, thres_lower, thres_upper):
        """
        Applies binary thresholding to the input image.
        """
        print('=== thresholdFcn ===')
        thres, image_threshod = cv2.threshold(image, thres_lower, thres_upper, cv2.THRESH_BINARY)
        return thres, image_threshod

    #//===================================================//
    def threshold_otsu(self, image):
        """
        Applies Otsu's thresholding to the input image.
        """
        print('=== threshold_otsu ===')
        thres_otsu, image_threshod_otsu = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        return thres_otsu, image_threshod_otsu

    #//===================================================//
    def threshold_adaptive(self, image, blocksize, C):
        """
        Applies adaptive thresholding to the input image.
        Args:
            image: Input image to be thresholded.
            blocksize: Size of the neighborhood used for thresholding.
            C: Constant subtracted from the mean.
        Returns:
            image_thres_adaptive: The adaptively thresholded image.
        """
        print('=== threshold_adaptive ===')
        image_thres_adaptive = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, blocksize, C)
        return image_thres_adaptive

    ##############################################
    # Morphological Transformations
    ##############################################

    #//===================================================//
    def dilateFcn(self, image, ksize):
        """
        Applies dilation to the input image.
        """
        print('=== dilateFcn ===')
        kernel = np.ones((ksize, ksize), np.uint8)
        image_dilate = cv2.dilate(image, kernel, iterations=1)
        return image_dilate

    #//===================================================//
    def erodeFcn(self, image, ksize):
        """
        Applies erosion to the input image.
        """
        print('=== erodeFcn ===')
        kernel = np.ones((ksize, ksize), np.uint8)
        image_erode = cv2.erode(image, kernel, iterations=1)
        return image_erode

    #//===================================================//
    def closing(self, image, ksize):
        """
        Applies morphological closing to the input image.
        """
        print('=== closing ===')
        kernel = np.ones((ksize, ksize), np.uint8)
        image_closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
        return image_closing

    ##############################################
    # Image Masking
    ##############################################

    #//===================================================//
    def remove_lines1(self, image, ksize):
        """
        Removes horizontal lines from the input image.
        """
        print('=== remove_lines1 ===')
        kernel = np.ones((1, ksize), np.uint8)
        line = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
        clean = cv2.subtract(line, image)
        image_remove_line1 = cv2.bitwise_not(clean)
        return image_remove_line1

    #//===================================================//
    def remove_table1(self, image, ksize):
        """
        Removes table structures (horizontal and vertical lines) from the input image.
        """
        print('=== remove_table1 ===')
        kernel_h = cv2.getStructuringElement(cv2.MORPH_RECT, (ksize, 1))
        line_h = cv2.morphologyEx(image,cv2.MORPH_CLOSE,kernel_h,iterations=1)
        kernel_v = cv2.getStructuringElement(cv2.MORPH_RECT ,(1, ksize))
        line_v = cv2.morphologyEx(image,cv2.MORPH_CLOSE, kernel_v, iterations=1)
        table_mask = cv2.bitwise_and(line_h, line_v)
        clean = cv2.subtract(table_mask, image)
        clean = cv2.bitwise_not(clean)
        image_remove_table1 = clean
        return image_remove_table1

    #//===================================================//
    def remove_watermark2(self, image):
        """
        Removes watermarks from the input image.
        """
        print('=== remove_watermark2 ===')
        bg = image.copy()
        for i in range(5):
            kernel2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2*i+1, 2*i+1))
            bg = cv2.morphologyEx(bg, cv2.MORPH_CLOSE, kernel2)
            bg = cv2.morphologyEx(bg, cv2.MORPH_OPEN, kernel2)

        dif = cv2.subtract(bg, image)
        bw = cv2.threshold(dif, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
        dark = cv2.threshold(bg, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
        darkpix = image[np.where(dark > 0)]
        darkpix = cv2.threshold(darkpix, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

        try:
            bw[np.where(dark > 0)] = darkpix.T
            image_remove_watermark2 = bw
        except:
            image_remove_watermark2 = bg
        return image_remove_watermark2

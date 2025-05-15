# Import necessary modules and constants from py_main_gui
from src.module.py_window_main import *       # Import all components from py_main_gui


########################################################################
class RubberBandNew(QRubberBand):
    """
    Custom implementation of QRubberBand with additional styling and behavior.
    """

    def __init__(self, QRubberBand_Shape, QWidget_parent=None):
        """
        Initializes the custom rubber band with the specified shape and parent widget.
        """
        super(RubberBandNew, self).__init__(QRubberBand_Shape, QWidget_parent)

        # Import the main GUI window to access global settings
        from src.module.py_window_main import MainGuiWindow

        # Set the thickness of the rubber band border based on the global configuration
        MainGuiWindow.THICKNESS_RBB = int(MainGuiWindow.RBBThicknessVar1)

    def paintEvent(self, QPaintEvent):
        """
        Handles the paint event to customize the appearance of the rubber band.
        """
        from src.module.py_window_main import MainGuiWindow

        painter = QPainter(self)

        # Determine the opacity of the rubber band border
        if (MainGuiWindow.THICKNESS_RBB == 0):
            OPACITY_RBB_BD = 0
        else:
            OPACITY_RBB_BD = 250

        # Set the pen for the border with the specified color and thickness
        pen_color = QColor(0,0,0,OPACITY_RBB_BD)
        painter.setPen(QPen(pen_color,MainGuiWindow.THICKNESS_RBB))    # Border thickness: 0/2/4/8/12

        # Set the brush for the background with the specified color and opacity
        brush_color = QColor(0,0,0,MainGuiWindow.OPACITY_RBB_BG)
        painter.setBrush(QBrush(brush_color))

        # Draw the rectangular rubber band
        painter.drawRect(QPaintEvent.rect())


    def resizeEvent(self, event):
        """
        Handles the resize event to apply rounded corners to the rubber band if needed.
        """
        from src.module.py_window_main import MainGuiWindow

        # Apply rounded corners if the border thickness is greater than 2
        if (MainGuiWindow.THICKNESS_RBB > 2):
            radius = 5
            path = QPainterPath()
            rect = QRectF(self.rect()).adjusted(0.5, 0.5, -0.5, -0.5)
            path.addRoundedRect(rect, radius, radius)

            # Create a region from the rounded rectangle and apply it as a mask
            region = QRegion(path.toFillPolygon(QTransform()).toPolygon())
            self.setMask(region)
        else:
            pass

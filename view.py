# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize, QRectF, Qt
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QAbstractButton
import functools


class PicButton(QAbstractButton):
    """Custom buttons"""
    def __init__(self, text, parent=None):
        super().__init__(parent)
        self.text = text
        self.pixmap = QtGui.QPixmap("Graphic/button.png")
        self.pixmap_hover = QtGui.QPixmap("Graphic/button_hover.png")
        self.pixmap_pressed = QtGui.QPixmap("Graphic/button_pressed.png")

        self.pressed.connect(self.update)
        self.released.connect(self.update)
        self.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

    def paintEvent(self, event):
        pix = self.pixmap_hover if self.underMouse() else self.pixmap
        if self.isDown():
            pix = self.pixmap_pressed

        painter = QPainter(self)
        painter.drawPixmap(event.rect(), pix)
        painter.drawText(QRectF(0.0,0.0,self.width(),self.height()), Qt.AlignCenter, self.text)

    def set_default_graphic(self, btn: QtGui.QPixmap, btn_hover: QtGui.QPixmap, btn_pressed: QtGui.QPixmap):
        self.pixmap = btn
        self.pixmap_hover = btn_hover
        self.pixmap_pressed = btn_pressed


class View(object):
    def __init__(self):
        self.mw = None
        self.central_widget = None
        self.src_arrow = "Graphic/arrow.png"
        self.src_logo = "Graphic/logo.png"
        self.src_null = "Graphic/NULL.png"

        self.reverse_button = None
        self.duplicates_button = None
        self.sort_desc_button = None
        self.sort_asc_button = None
        self.reset_button = None
        self.delete_button = None

        """Input"""
        self.input_field = None
        self.enter_button = None

        """Linked list"""
        self.result = []
        self.list = None

        """Presenter instance"""
        self.presenter = None

    def setup(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(680, 450)
        MainWindow.setWindowTitle("Linked-list")

        self.central_widget = QtWidgets.QWidget(self.mw)
        self.central_widget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.central_widget.setStyleSheet("PicButton{ color: white; font-size:18px;}")
        #self.central_widget.setStyleSheet("QPushButton{background: #22291F; border-radius: 10px; color: white; font-size:18px;} QPushButton:hover{background: #363D33;} QPushButton:pressed{background: #4C5249;}")
        self.central_widget.setObjectName("centralwidget")

        self.back_ground = QtWidgets.QFrame(self.central_widget)
        self.back_ground.setGeometry(QtCore.QRect(0, 0, 680, 450))
        self.back_ground.setStyleSheet("#back_ground{background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(113, 222, 137, 255), stop:1 rgba(69, 223, 168, 255))}")
        self.back_ground.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.back_ground.setFrameShadow(QtWidgets.QFrame.Raised)
        self.back_ground.setObjectName("back_ground")

        """Input field and button"""

        self.enter_button = PicButton("Add", self.back_ground)
        self.enter_button.setGeometry(QtCore.QRect(205, 330, 102, 62))
        self.enter_button.set_default_graphic(QtGui.QPixmap("Graphic/add_button.png"), QtGui.QPixmap("Graphic/add_btn_hover.png"), QtGui.QPixmap("Graphic/add_btn_pressed.png"))
        self.enter_button.setStyleSheet("#enter_button{color: white; font-size: 18px;}")
        self.enter_button.clicked.connect(lambda: self.presenter.insert(self.input_field.toPlainText()))

        self.input_field = QtWidgets.QTextEdit(self.back_ground)
        self.input_field.setGeometry(QtCore.QRect(30, 338, 181, 46))
        self.input_field.setStyleSheet("#input_field{ background: white; border-top-left-radius: 10px; border-bottom-left-radius: 10px; font-size: 20px; text-align: center;}")
        self.input_field.setObjectName("input_field")


        """Linked List"""
        self.list = List(self.back_ground)
        self.list.setContentsMargins(0,0,0,0)
        self.list.setGeometry(QtCore.QRect(20, 40, 500, 60))
        self.list.setup(self.back_ground, self.src_null, self.src_arrow)

        """Buttons"""

        self.delete_button = PicButton("Delete", self.back_ground)
        self.delete_button.setGeometry(QtCore.QRect(390, 170, 112, 62))
        self.delete_button.setObjectName("enter_button_2")
        self.delete_button.clicked.connect(lambda: self.presenter.remove_node(self.list.active_node))

        self.reset_button = PicButton("Reset", self.back_ground)
        self.reset_button.setGeometry(QtCore.QRect(520, 170, 112, 62))
        self.reset_button.setObjectName("enter_button_3")
        self.reset_button.clicked.connect(lambda: self.presenter.reset())

        self.sort_asc_button = PicButton("Sort ↑", self.back_ground)
        self.sort_asc_button.setGeometry(QtCore.QRect(390, 250, 112, 62))
        self.sort_asc_button.setObjectName("enter_button_4")
        self.sort_asc_button.clicked.connect(lambda: self.presenter.sort_asc())

        self.sort_desc_button = PicButton("Sort ↓", self.back_ground)
        self.sort_desc_button.setGeometry(QtCore.QRect(520, 250, 112, 62))
        self.sort_desc_button.setObjectName("enter_button_5")
        self.sort_desc_button.clicked.connect(lambda: self.presenter.sort_desc())

        self.duplicates_button = PicButton("Duplicates", self.back_ground)
        self.duplicates_button.setGeometry(QtCore.QRect(390, 330, 112, 62))
        self.duplicates_button.setObjectName("enter_button_6")
        self.duplicates_button.clicked.connect(lambda: self.presenter.duplicates())

        self.reverse_button = PicButton("Reverse", self.back_ground)
        self.reverse_button.setGeometry(QtCore.QRect(520, 330, 112, 62))
        self.reverse_button.setObjectName("enter_button_7")
        self.reverse_button.clicked.connect(lambda: self.presenter.reverse())

        """Others"""

        self.line = QtWidgets.QFrame(self.back_ground)
        self.line.setGeometry(QtCore.QRect(340, 150, 20, 255))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.logo = QtWidgets.QLabel(self.back_ground)
        self.logo.setGeometry(QtCore.QRect(40, 160, 241, 151))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap(self.src_logo))
        self.logo.setObjectName("label_3")

        MainWindow.setCentralWidget(self.central_widget)
        QtCore.QMetaObject.connectSlotsByName(self.mw)
        # self.menubar = QtWidgets.QMenuBar(MainWindow)
        # self.menubar.setGeometry(QtCore.QRect(0, 0, 680, 26))
        # self.menubar.setObjectName("menubar")
        # MainWindow.setMenuBar(self.menubar)
        # self.statusbar = QtWidgets.QStatusBar(MainWindow)
        # self.statusbar.setObjectName("statusbar")
        # MainWindow.setStatusBar(self.statusbar)


    def set_presenter(self, presenter):
        self.presenter = presenter


class List(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedHeight(60)
        self.nodes = []
        self.nulls = []
        self.arrows = []
        self.active_node = None

    def setup(self, frame, src_null, src_arrow):
        x = 140
        for i in range(5):
            """create nulls"""
            label_null = QtWidgets.QLabel(frame)
            label_null.setGeometry(QtCore.QRect(20 + x * i, 62, 80, 15))
            label_null.setText("")
            label_null.setPixmap(QtGui.QPixmap(src_null))
            label_null.setObjectName("label_null")
            label_null.hide()
            self.nulls.append(label_null)

            """Create shadow effect"""
            shadow = QtWidgets.QGraphicsDropShadowEffect()
            shadow.setBlurRadius(8)
            shadow.setXOffset(0)
            shadow.setYOffset(0)

            """create nodes"""
            res = QtWidgets.QLabel(frame)
            res.setGeometry(QtCore.QRect(20 + x * i, 40, 80, 52))
            res.setGraphicsEffect(shadow)
            res.setStyleSheet("QLabel { background: white; border-radius: 10px; font-size: 18px;}")
            res.setText("")
            res.setAlignment(QtCore.Qt.AlignCenter)
            res.setObjectName("res_"+str(i))
            res.mousePressEvent = functools.partial(self.pressed, source_object=res)
            res.hide()
            self.nodes.append(res)

        """Create arrows"""
        for i in range(4):
            arrow = QtWidgets.QLabel(frame)
            arrow.setGeometry(QtCore.QRect(110 + x * i, 60, 40, 16))
            arrow.setText("")
            arrow.setPixmap(QtGui.QPixmap(src_arrow))
            arrow.setScaledContents(False)
            arrow.setObjectName("arrow")
            arrow.hide()
            self.arrows.append(arrow)

        self.nulls[0].show()

    # def set_active(self, p):
    #     """this method is called from reverse method to reverse also node that is currently active"""
    #     if p == self.active_node:  # when you want to active node that is already active (has red border) then don't do anything
    #         return
    #     self.pressed(event=None, source_object=self.nodes[p])

    def deactivate_node(self):
        if self.active_node is not None:
            self.nodes[self.active_node].setStyleSheet("QLabel { background: white; border-radius: 10px; font-size: 18px; }")
            self.active_node = None

    def pressed(self, event, source_object):
        index = int(source_object.objectName()[4:])  # get the index from node name (res_1)
        if self.active_node is not None:
            self.nodes[self.active_node].setStyleSheet("QLabel { background: white; border-radius: 10px; font-size: 18px; }")
            if self.active_node == index:  # if was clicked active node then deactivate it and end method here
                self.active_node = None
                return
            self.active_node = None

        self.active_node = index
        source_object.setStyleSheet("QLabel { background: white; border-radius: 10px; font-size: 18px; border: 2px solid #F15454;}")

    def show_nodes(self, p):
        self.hide_all()
        if p == 0:
            self.nulls[0].show()
        else:
            if p < 5:
                self.nulls[p].show()
            for i in range(p):
                self.nodes[i].show()
                if i < 4:
                    self.arrows[i].show()

    def hide_all(self):
        for a in self.nulls:
            a.hide()
        for a in self.nodes:
            a.hide()
        for a in self.arrows:
            a.hide()


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = View()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())

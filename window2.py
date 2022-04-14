from PyQt5 import QtCore, QtGui, QtWidgets, QtGui, QtSvg


class Ui_window(object):
    def setupUi(self, window, filename):
        window.setObjectName("window")
        window.showFullScreen()
        self.centralwidget = QtWidgets.QWidget(window)
        self.centralwidget.setObjectName("centralwidget")

        self.image = QtSvg.QSvgWidget(filename, self.centralwidget)
        self.image.setObjectName("image")
        self.image.renderer().setAspectRatioMode(QtCore.Qt.KeepAspectRatio)
        self.image.setGeometry(50, 0, 1000, 800)
        self.image.show()

        self.edges_scroll = QtWidgets.QScrollArea(self.centralwidget)
        self.edges_scroll.setGeometry(QtCore.QRect(1100, 100, 170, 600))
        self.edges_scroll.setWidgetResizable(True)
        self.edges_scroll.setObjectName("edges_scroll")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 168, 798))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.edges_scroll.setWidget(self.scrollAreaWidgetContents)
        self.add_edge_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_edge_button.setGeometry(QtCore.QRect(1190, 40, 80, 40))
        self.add_edge_button.setObjectName("add_edge_button")
        self.node1_label = QtWidgets.QLabel(self.centralwidget)
        self.node1_label.setGeometry(QtCore.QRect(1030, 30, 50, 20))
        self.node1_label.setObjectName("node1_label")
        self.node2_label = QtWidgets.QLabel(self.centralwidget)
        self.node2_label.setGeometry(QtCore.QRect(1030, 60, 50, 20))
        self.node2_label.setObjectName("node2_label")
        self.node1_insert = QtWidgets.QLineEdit(self.centralwidget)
        self.node1_insert.setGeometry(QtCore.QRect(1080, 30, 110, 20))
        self.node1_insert.setObjectName("node1_insert")
        self.node2_insert = QtWidgets.QLineEdit(self.centralwidget)
        self.node2_insert.setGeometry(QtCore.QRect(1080, 60, 110, 20))
        self.node2_insert.setObjectName("node2_insert")

        window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(window)
        self.menubar.setNativeMenuBar(False)
        self.menubar.setGeometry(QtCore.QRect(0, 10, 1200, 22))
        self.menubar.setObjectName("menubar")
        self.menuAdd_Node = QtWidgets.QMenu(self.menubar)
        self.menuAdd_Node.setObjectName("menuAdd_Node")
        self.menuRemove_Node = QtWidgets.QMenu(self.menubar)
        self.menuRemove_Node.setObjectName("menuRemove_Node")
        window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(window)
        self.statusbar.setObjectName("statusbar")
        window.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuAdd_Node.menuAction())
        self.menubar.addAction(self.menuRemove_Node.menuAction())

        self.retranslateUi(window)
        QtCore.QMetaObject.connectSlotsByName(window)

    def retranslateUi(self, window):
        _translate = QtCore.QCoreApplication.translate
        window.setWindowTitle(_translate("window", "SAD3E"))
        self.add_edge_button.setText(_translate("window", "Add Edge"))
        self.node1_label.setText(_translate("window", "Node1:"))
        self.node2_label.setText(_translate("window", "Node2:"))
        self.menuAdd_Node.setTitle(_translate("window", "Add Node"))
        self.menuRemove_Node.setTitle(_translate("window", "Remove Node"))


    def mousePressEvent(self, event):
        a = 0

    def insertNode(self):
        a = 0


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = Ui_window()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())

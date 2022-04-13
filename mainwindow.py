from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SAD3E(object):
    def setupUi(self, SAD3E):
        SAD3E.setObjectName("SAD3E")
        SAD3E.resize(500, 335)
        SAD3E.setMinimumSize(QtCore.QSize(500, 335))
        SAD3E.setMaximumSize(QtCore.QSize(500, 335))
        self.centralwidget = QtWidgets.QWidget(SAD3E)
        self.centralwidget.setObjectName("centralwidget")
        self.sade3_label = QtWidgets.QLabel(self.centralwidget)
        self.sade3_label.setGeometry(QtCore.QRect(170, 40, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(36)
        font.setBold(True)
        self.sade3_label.setFont(font)
        self.sade3_label.setObjectName("sade3_label")
        self.sistema_label = QtWidgets.QLabel(self.centralwidget)
        self.sistema_label.setGeometry(QtCore.QRect(40, 80, 421, 16))
        self.sistema_label.setObjectName("sistema_label")
        self.new_buttom = QtWidgets.QPushButton(self.centralwidget)
        self.new_buttom.setGeometry(QtCore.QRect(190, 100, 100, 32))
        self.new_buttom.setObjectName("new_buttom")
        self.open_button = QtWidgets.QPushButton(self.centralwidget)
        self.open_button.setGeometry(QtCore.QRect(190, 130, 100, 32))
        self.open_button.setObjectName("open_button")
        self.about_button = QtWidgets.QPushButton(self.centralwidget)
        self.about_button.setGeometry(QtCore.QRect(190, 160, 100, 32))
        self.about_button.setObjectName("about_button")
        self.feup_logo_label = QtWidgets.QLabel(self.centralwidget)
        self.feup_logo_label.setGeometry(QtCore.QRect(170, 200, 147, 51))
        self.feup_logo_label.setText("")
        self.feup_logo_label.setPixmap(QtGui.QPixmap("images/feup_logo.png"))
        self.feup_logo_label.setScaledContents(True)
        self.feup_logo_label.setObjectName("feup_logo_label")
        self.nibble_logo_label = QtWidgets.QLabel(self.centralwidget)
        self.nibble_logo_label.setGeometry(QtCore.QRect(190, 270, 106, 19))
        self.nibble_logo_label.setText("")
        self.nibble_logo_label.setPixmap(QtGui.QPixmap("images/nibble.png"))
        self.nibble_logo_label.setScaledContents(True)
        self.nibble_logo_label.setObjectName("nibble_logo_label")
        SAD3E.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(SAD3E)
        self.statusbar.setObjectName("statusbar")
        SAD3E.setStatusBar(self.statusbar)

        self.retranslateUi(SAD3E)
        QtCore.QMetaObject.connectSlotsByName(SAD3E)

    def retranslateUi(self, SAD3E):
        _translate = QtCore.QCoreApplication.translate
        SAD3E.setWindowTitle(_translate("SAD3E", "SAD3E"))
        self.sade3_label.setText(_translate("SAD3E", "SAD3E"))
        self.sistema_label.setText(_translate("SAD3E", "Sistema de Apoio à Decisão na Evacuação de Emergência de Edifícios"))
        self.new_buttom.setText(_translate("SAD3E", "New"))
        self.open_button.setText(_translate("SAD3E", "Open"))
        self.about_button.setText(_translate("SAD3E", "About"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SAD3E = QtWidgets.QMainWindow()
    ui = Ui_SAD3E()
    ui.setupUi(SAD3E)
    SAD3E.show()
    sys.exit(app.exec_())

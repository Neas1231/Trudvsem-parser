# Form implementation generated from reading ui file '../design_test.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(441, 155)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 441, 91))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.main_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setObjectName("main_layout")
        self.label_main = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_main.setFont(font)
        self.label_main.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_main.setObjectName("label_main")
        self.main_layout.addWidget(self.label_main)
        self.url = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.url.setToolTipDuration(-1)
        self.url.setInputMask("")
        self.url.setObjectName("url")
        self.main_layout.addWidget(self.url)
        self.parsing_button = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.parsing_button.setEnabled(True)
        self.parsing_button.setObjectName("parsing_button")
        self.main_layout.addWidget(self.parsing_button)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 90, 441, 51))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.loading_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.loading_layout.setContentsMargins(0, 0, 0, 0)
        self.loading_layout.setObjectName("loading_layout")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TrudVsem parser"))
        self.label_main.setText(_translate("MainWindow", "Введите url с сайта trudvsem.ru"))
        self.url.setText(_translate("MainWindow", "https://trudvsem.ru/vacancy/search"))
        self.parsing_button.setText(_translate("MainWindow", "Спарсить"))

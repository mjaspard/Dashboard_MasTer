# Form implementation generated from reading ui file '/Users/maxime/Project/QT/eric/Dashboard_Master/main_window.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1099, 946)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMaximumSize)
        self.horizontalLayout.setContentsMargins(10, 0, 10, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_RAW = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_RAW.sizePolicy().hasHeightForWidth())
        self.pushButton_RAW.setSizePolicy(sizePolicy)
        self.pushButton_RAW.setMinimumSize(QtCore.QSize(199, 30))
        self.pushButton_RAW.setObjectName("pushButton_RAW")
        self.horizontalLayout.addWidget(self.pushButton_RAW)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_CSL = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_CSL.sizePolicy().hasHeightForWidth())
        self.pushButton_CSL.setSizePolicy(sizePolicy)
        self.pushButton_CSL.setMinimumSize(QtCore.QSize(199, 30))
        self.pushButton_CSL.setObjectName("pushButton_CSL")
        self.horizontalLayout.addWidget(self.pushButton_CSL)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton_SET = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_SET.sizePolicy().hasHeightForWidth())
        self.pushButton_SET.setSizePolicy(sizePolicy)
        self.pushButton_SET.setMinimumSize(QtCore.QSize(199, 30))
        self.pushButton_SET.setObjectName("pushButton_SET")
        self.horizontalLayout.addWidget(self.pushButton_SET)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pushButton_RESAMPLED = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_RESAMPLED.sizePolicy().hasHeightForWidth())
        self.pushButton_RESAMPLED.setSizePolicy(sizePolicy)
        self.pushButton_RESAMPLED.setMinimumSize(QtCore.QSize(60, 30))
        self.pushButton_RESAMPLED.setObjectName("pushButton_RESAMPLED")
        self.horizontalLayout.addWidget(self.pushButton_RESAMPLED)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.pushButton_MSBAS = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_MSBAS.sizePolicy().hasHeightForWidth())
        self.pushButton_MSBAS.setSizePolicy(sizePolicy)
        self.pushButton_MSBAS.setMinimumSize(QtCore.QSize(60, 30))
        self.pushButton_MSBAS.setObjectName("pushButton_MSBAS")
        self.horizontalLayout.addWidget(self.pushButton_MSBAS)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.pushButton_SAR_MP = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_SAR_MP.sizePolicy().hasHeightForWidth())
        self.pushButton_SAR_MP.setSizePolicy(sizePolicy)
        self.pushButton_SAR_MP.setMinimumSize(QtCore.QSize(60, 30))
        self.pushButton_SAR_MP.setObjectName("pushButton_SAR_MP")
        self.horizontalLayout.addWidget(self.pushButton_SAR_MP)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.pushButton_SAR_SM = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_SAR_SM.sizePolicy().hasHeightForWidth())
        self.pushButton_SAR_SM.setSizePolicy(sizePolicy)
        self.pushButton_SAR_SM.setMinimumSize(QtCore.QSize(60, 30))
        self.pushButton_SAR_SM.setObjectName("pushButton_SAR_SM")
        self.horizontalLayout.addWidget(self.pushButton_SAR_SM)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.line = QtWidgets.QFrame(self.centralWidget)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(10, 1, 10, 1)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.pushButton_SCRIPT_OK = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_SCRIPT_OK.sizePolicy().hasHeightForWidth())
        self.pushButton_SCRIPT_OK.setSizePolicy(sizePolicy)
        self.pushButton_SCRIPT_OK.setMinimumSize(QtCore.QSize(60, 30))
        self.pushButton_SCRIPT_OK.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_SCRIPT_OK.setAutoDefault(False)
        self.pushButton_SCRIPT_OK.setFlat(False)
        self.pushButton_SCRIPT_OK.setObjectName("pushButton_SCRIPT_OK")
        self.horizontalLayout_8.addWidget(self.pushButton_SCRIPT_OK)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem6)
        self.pushButton_CRON = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_CRON.sizePolicy().hasHeightForWidth())
        self.pushButton_CRON.setSizePolicy(sizePolicy)
        self.pushButton_CRON.setMinimumSize(QtCore.QSize(60, 30))
        self.pushButton_CRON.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_CRON.setAutoDefault(False)
        self.pushButton_CRON.setFlat(False)
        self.pushButton_CRON.setObjectName("pushButton_CRON")
        self.horizontalLayout_8.addWidget(self.pushButton_CRON)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem7)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem8)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.line_2 = QtWidgets.QFrame(self.centralWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setContentsMargins(10, 1, -1, 1)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.pushButton_RUN1 = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_RUN1.sizePolicy().hasHeightForWidth())
        self.pushButton_RUN1.setSizePolicy(sizePolicy)
        self.pushButton_RUN1.setMinimumSize(QtCore.QSize(60, 30))
        self.pushButton_RUN1.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_RUN1.setObjectName("pushButton_RUN1")
        self.horizontalLayout_9.addWidget(self.pushButton_RUN1)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem9)
        self.pushButton_RUN2 = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_RUN2.sizePolicy().hasHeightForWidth())
        self.pushButton_RUN2.setSizePolicy(sizePolicy)
        self.pushButton_RUN2.setMinimumSize(QtCore.QSize(60, 30))
        self.pushButton_RUN2.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_RUN2.setObjectName("pushButton_RUN2")
        self.horizontalLayout_9.addWidget(self.pushButton_RUN2)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem10)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem11)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralWidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.tab_RAW = QtWidgets.QWidget()
        self.tab_RAW.setObjectName("tab_RAW")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.tab_RAW)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.columnView_RAW = QtWidgets.QColumnView(self.tab_RAW)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.columnView_RAW.sizePolicy().hasHeightForWidth())
        self.columnView_RAW.setSizePolicy(sizePolicy)
        self.columnView_RAW.setMinimumSize(QtCore.QSize(0, 0))
        self.columnView_RAW.setObjectName("columnView_RAW")
        self.horizontalLayout_5.addWidget(self.columnView_RAW)
        self.stackedWidget.addWidget(self.tab_RAW)
        self.tab_CSL = QtWidgets.QWidget()
        self.tab_CSL.setObjectName("tab_CSL")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.tab_CSL)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.columnView_CSL = QtWidgets.QColumnView(self.tab_CSL)
        self.columnView_CSL.setObjectName("columnView_CSL")
        self.horizontalLayout_6.addWidget(self.columnView_CSL)
        self.stackedWidget.addWidget(self.tab_CSL)
        self.tab_SET = QtWidgets.QWidget()
        self.tab_SET.setObjectName("tab_SET")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.tab_SET)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.columnView_SET = QtWidgets.QColumnView(self.tab_SET)
        self.columnView_SET.setObjectName("columnView_SET")
        self.horizontalLayout_7.addWidget(self.columnView_SET)
        self.stackedWidget.addWidget(self.tab_SET)
        self.verticalLayout_2.addWidget(self.stackedWidget)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(10, 5, 10, 5)
        self.horizontalLayout_3.setSpacing(30)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.checkBox_ADD = QtWidgets.QCheckBox(self.centralWidget)
        self.checkBox_ADD.setText("")
        self.checkBox_ADD.setChecked(True)
        self.checkBox_ADD.setObjectName("checkBox_ADD")
        self.horizontalLayout_3.addWidget(self.checkBox_ADD)
        self.lineEdit_INPUT = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_INPUT.setObjectName("lineEdit_INPUT")
        self.horizontalLayout_3.addWidget(self.lineEdit_INPUT)
        self.pushButton_ADD = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_ADD.sizePolicy().hasHeightForWidth())
        self.pushButton_ADD.setSizePolicy(sizePolicy)
        self.pushButton_ADD.setMinimumSize(QtCore.QSize(60, 30))
        self.pushButton_ADD.setObjectName("pushButton_ADD")
        self.horizontalLayout_3.addWidget(self.pushButton_ADD)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(10, 5, 10, 5)
        self.horizontalLayout_4.setSpacing(30)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.checkBox_FROM = QtWidgets.QCheckBox(self.centralWidget)
        self.checkBox_FROM.setText("")
        self.checkBox_FROM.setObjectName("checkBox_FROM")
        self.horizontalLayout_4.addWidget(self.checkBox_FROM)
        self.label_FROM = QtWidgets.QLabel(self.centralWidget)
        self.label_FROM.setObjectName("label_FROM")
        self.horizontalLayout_4.addWidget(self.label_FROM)
        self.lineEdit_FROM = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_FROM.setClearButtonEnabled(False)
        self.lineEdit_FROM.setObjectName("lineEdit_FROM")
        self.horizontalLayout_4.addWidget(self.lineEdit_FROM)
        self.pushButton_HOME = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_HOME.sizePolicy().hasHeightForWidth())
        self.pushButton_HOME.setSizePolicy(sizePolicy)
        self.pushButton_HOME.setMinimumSize(QtCore.QSize(60, 30))
        self.pushButton_HOME.setObjectName("pushButton_HOME")
        self.horizontalLayout_4.addWidget(self.pushButton_HOME)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(10, 5, 10, 5)
        self.horizontalLayout_2.setSpacing(30)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_CMD = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_CMD.setMinimumSize(QtCore.QSize(0, 80))
        self.lineEdit_CMD.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit_CMD.setObjectName("lineEdit_CMD")
        self.horizontalLayout_2.addWidget(self.lineEdit_CMD)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_EXEC = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_EXEC.sizePolicy().hasHeightForWidth())
        self.pushButton_EXEC.setSizePolicy(sizePolicy)
        self.pushButton_EXEC.setMinimumSize(QtCore.QSize(60, 30))
        self.pushButton_EXEC.setObjectName("pushButton_EXEC")
        self.verticalLayout.addWidget(self.pushButton_EXEC)
        spacerItem12 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        self.verticalLayout.addItem(spacerItem12)
        self.pushButton_CLEAR = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_CLEAR.sizePolicy().hasHeightForWidth())
        self.pushButton_CLEAR.setSizePolicy(sizePolicy)
        self.pushButton_CLEAR.setMinimumSize(QtCore.QSize(60, 30))
        self.pushButton_CLEAR.setObjectName("pushButton_CLEAR")
        self.verticalLayout.addWidget(self.pushButton_CLEAR)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1099, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuConfiguration = QtWidgets.QMenu(self.menuBar)
        self.menuConfiguration.setObjectName("menuConfiguration")
        MainWindow.setMenuBar(self.menuBar)
        self.actionOpen_file = QtGui.QAction(MainWindow)
        self.actionOpen_file.setObjectName("actionOpen_file")
        self.menuConfiguration.addAction(self.actionOpen_file)
        self.menuBar.addAction(self.menuConfiguration.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_RAW.setText(_translate("MainWindow", "RAW"))
        self.pushButton_CSL.setText(_translate("MainWindow", "CSL"))
        self.pushButton_SET.setText(_translate("MainWindow", "SET"))
        self.pushButton_RESAMPLED.setText(_translate("MainWindow", "RESAMPLED"))
        self.pushButton_MSBAS.setText(_translate("MainWindow", "MSBAS"))
        self.pushButton_SAR_MP.setText(_translate("MainWindow", "SAR_MP"))
        self.pushButton_SAR_SM.setText(_translate("MainWindow", "SAR_SM"))
        self.pushButton_SCRIPT_OK.setText(_translate("MainWindow", "SCRIPT_OK"))
        self.pushButton_CRON.setText(_translate("MainWindow", "CRON"))
        self.pushButton_RUN1.setText(_translate("MainWindow", "RUN1"))
        self.pushButton_RUN2.setText(_translate("MainWindow", "RUN2"))
        self.pushButton_ADD.setText(_translate("MainWindow", "Add"))
        self.label_FROM.setText(_translate("MainWindow", "Exec scripts below from location: "))
        self.lineEdit_FROM.setText(_translate("MainWindow", "${HOME}"))
        self.pushButton_HOME.setText(_translate("MainWindow", "HOME"))
        self.pushButton_EXEC.setText(_translate("MainWindow", "EXEC"))
        self.pushButton_CLEAR.setText(_translate("MainWindow", "CLEAR"))
        self.menuConfiguration.setTitle(_translate("MainWindow", "Configuration"))
        self.actionOpen_file.setText(_translate("MainWindow", "Open file"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())

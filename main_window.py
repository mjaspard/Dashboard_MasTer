
import os
import re
import subprocess,  shlex
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QFileSystemModel
from PyQt6.QtCore import pyqtSlot,  QModelIndex
from Ui_main_window import Ui_MainWindow

config_file = "config.txt"

def getPath(target):
    with open(config_file,  'r') as f:
        lines = f.readlines()
        for line in lines:
            if re.search(r"^"+str(target)+"\s*#{1}", line):
                path_target = re.split(r"#", line)[1]
                path_target = path_target.strip() # remove spaces
                return path_target
        return '/'
        
                
                
            
    

dir_path = '/Users/maxime/Project/QT'
RAW_Path = getPath("RAW")
CSL_Path = getPath("CSL")
SET_Path = getPath("SET")
SCRIPTS_Path = getPath("SCRIPTS")
MSBAS_Path = getPath("MSBAS")
SAR_MP_Path = getPath("SAR_MP")
SAR_SM_Path = getPath("SAR_SM")



class MainWindow(QMainWindow,  Ui_MainWindow):
    

    def __init__(self, parent=None):
        super(MainWindow,  self).__init__(parent)
        self.setupUi(self)
        self.model = QFileSystemModel()
        self.model.setRootPath(dir_path)
        self.checkBox_ADD.stateChanged.connect(self.disable_cb_FROM)
        self.checkBox_FROM.stateChanged.connect(self.disable_cb_ADD)
        self.lineEdit_FROM.setText("${HOME}")
        self.pushButton_EXEC.setStyleSheet("background-color : LightSalmon")
  

        self.columnView_RAW.setModel(self.model)
        self.columnView_RAW.setRootIndex(self.model.index(RAW_Path))  

    
        self.columnView_CSL.setModel(self.model)
        self.columnView_CSL.setRootIndex(self.model.index(CSL_Path))  

        self.columnView_SET.setModel(self.model)
        self.columnView_SET.setRootIndex(self.model.index(SET_Path)) 

    
    @pyqtSlot()
    def on_pushButton_RAW_clicked(self):
        self.stackedWidget.setCurrentWidget(self.tab_RAW)
    @pyqtSlot()
    def on_pushButton_CSL_clicked(self):
        self.stackedWidget.setCurrentWidget(self.tab_CSL)  
    @pyqtSlot()
    def on_pushButton_SET_clicked(self):
        self.stackedWidget.setCurrentWidget(self.tab_SET)


  
    def on_columnView_RAW_clicked(self,  index):
        indexItem = self.model.index(index.row(), 0, index.parent())
        filePath = self.model.filePath(indexItem)
        if self.checkBox_ADD.isChecked():
            self.lineEdit_INPUT.setText(filePath)
        elif self.checkBox_FROM.isChecked():
            self.lineEdit_FROM.setText(filePath)

    def on_columnView_CSL_clicked(self,  index):
        indexItem = self.model.index(index.row(), 0, index.parent())
        filePath = self.model.filePath(indexItem)
        if self.checkBox_ADD.isChecked():
            self.lineEdit_INPUT.setText(filePath)
        elif self.checkBox_FROM.isChecked():
            self.lineEdit_FROM.setText(filePath)

    def on_columnView_SET_clicked(self,  index):
        indexItem = self.model.index(index.row(), 0, index.parent())
        filePath = self.model.filePath(indexItem)
        if self.checkBox_ADD.isChecked():
            self.lineEdit_INPUT.setText(filePath)
        elif self.checkBox_FROM.isChecked():
            self.lineEdit_FROM.setText(filePath)        
        
    @pyqtSlot()
    def on_pushButton_ADD_clicked(self):
        current_text = self.lineEdit_CMD
        new_text = "{} {}".format(current_text.displayText(), self.lineEdit_INPUT.displayText())
        self.lineEdit_CMD.setText(new_text)
        
    @pyqtSlot()
    def on_pushButton_CLEAR_clicked(self):
        self.lineEdit_CMD.clear()
    
    def disable_cb_FROM(self):
        if self.checkBox_ADD.isChecked():
            self.checkBox_FROM.setChecked(False)

    def disable_cb_ADD(self):
        if self.checkBox_FROM.isChecked():
            self.checkBox_ADD.setChecked(False)
            
 
    @pyqtSlot()
    def on_pushButton_HOME_clicked(self):
        self.lineEdit_FROM.setText("${HOME}")
        
    @pyqtSlot()
    def on_pushButton_EXEC_clicked(self):
        current_cmd = self.lineEdit_CMD
        source = self.lineEdit_FROM
        cmd = "xterm -e \'cd {}; {};read\'".format(source.displayText(), current_cmd.displayText())
#        os.system(cmd)        
        subprocess.Popen(shlex.split(cmd))
        
        

      


import re, subprocess
import subprocess,  shlex
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QFileSystemModel
from PyQt6.QtCore import pyqtSlot,  QModelIndex, QSize
from Ui_main_window_man import Ui_MainWindow, button_l1, button_l2, button_l3

dir_path = subprocess.Popen("pwd", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
dir_path = dir_path[0].decode('ascii')


class MainWindow(QMainWindow,  Ui_MainWindow):


	def __init__(self, parent=None):
		super(MainWindow,  self).__init__(parent)
		self.setupUi(self)
		self.model = QFileSystemModel()
		self.model.setRootPath(dir_path)

		self.lineEdit_FROM.setText("${HOME}")
		self.pushButton_EXEC.setStyleSheet("background-color : LightSalmon")
	
		k = 0 # Initialise a counter used to manage position of horizontal layout in the main vertical layout of the window 
		for i in range(1,4,1):	# Loop through 3 dictionary (i = index for each line and the number of dictionary)
		
			nb_button = len(globals()["button_l" + str(i)])
			max_button = 8
			cu_hl = 0
			cu_hl_mem = 0
			print("incermentation {}".format(i))
			
			# Create another counter for columnView
			j = 40 + 1
			


			# Manage horizontal layouts for this set of buttons
			nb_horizLayout = 1 + int(nb_button/max_button) # max 10 button on same line
			print("Need to create {} horizontal layout".format(nb_horizLayout))
			for i_hl in range(0, nb_horizLayout, 1):
				print("create Layout: self.horizontalLayout_{}{}".format(str(i_hl), str(i)))
				globals()["self.horizontalLayout_" + str(i_hl)+ str(i)] = QHBoxLayout()
				globals()["self.horizontalLayout_" + str(i_hl) + str(i)].setContentsMargins(10, 1, 10, 1)
				globals()["self.horizontalLayout_" + str(i_hl) + str(i)].setSpacing(0)
				globals()["self.horizontalLayout_" + str(i_hl) + str(i)].setObjectName("horizontalLayout_{}{}".format(str(i_hl), str(i)))
	

			# Loop through each button
			nb_button_add = 0
			nb_button_add_line = 0
			for key, value in globals()["button_l" + str(i)].items():
				nb_button_add += 1
				nb_button_add_line += 1
				cu_hl = int((nb_button_add - 1)/max_button)
				if (cu_hl != cu_hl_mem):
					nb_button_add_line = 0
					spacerItem = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
					globals()["self.horizontalLayout_" + str(cu_hl) + str(i)].addItem(spacerItem)
				cu_hl_mem = cu_hl
				globals()["self.pushButton_"+str(key)] = QPushButton(self.centralWidget)
				# sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
				# sizePolicy.setHorizontalStretch(0)
				# sizePolicy.setVerticalStretch(0)       	
				# sizePolicy.setHeightForWidth(globals()["self.pushButton_"+str(key)].sizePolicy().hasHeightForWidth())
				
				# globals()["self.pushButton_"+str(key)].setSizePolicy(sizePolicy)
				globals()["self.pushButton_"+str(key)].setMinimumSize(QSize(100, 35))
				globals()["self.pushButton_"+str(key)].setObjectName("pushButton_{}".format(key))
				globals()["self.pushButton_"+str(key)].setText(str(key))
				globals()["self.pushButton_"+str(key)].resize(600, 50)
				globals()["self.horizontalLayout_" + str(cu_hl) + str(i)].addWidget(globals()["self.pushButton_"+str(key)])
				spacerItem = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
				globals()["self.horizontalLayout_" + str(cu_hl) + str(i)].addItem(spacerItem)
# 				self.verticalLayout_2.insertLayout(k, globals()["self.horizontalLayout_" + str(i)])
# 				print("insert self.horizontalLayout_{} at position {}".format(i, k))			
				
				
				globals()["self.tab_"+str(key)] = QWidget()
				globals()["self.tab_"+str(key)].setObjectName("tab_{}".format(key))
				globals()["self.horizontalLayout_" + str(j)] = QHBoxLayout(globals()["self.tab_"+str(key)])
				globals()["self.horizontalLayout_" + str(j)].setObjectName("horizontalLayout_{}".format(str(j)))	
				globals()["self.columnView_"+str(key)] = QColumnView(globals()["self.tab_"+str(key)])
				# sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
				# sizePolicy.setHorizontalStretch(0)
				# sizePolicy.setVerticalStretch(0)
				# sizePolicy.setHeightForWidth(globals()["self.columnView_"+str(key)].sizePolicy().hasHeightForWidth())
				# globals()["self.columnView_"+str(key)].setSizePolicy(sizePolicy)
				globals()["self.columnView_"+str(key)].setMinimumSize(QSize(0, 0))
				globals()["self.columnView_"+str(key)].setObjectName("columnView_{}".format(str(key)))
				globals()["self.horizontalLayout_" + str(j)].addWidget(globals()["self.columnView_"+str(key)])
				self.stackedWidget.addWidget(globals()["self.tab_"+str(key)])

				globals()["self.pushButton_"+str(key)].pressed.connect(lambda val=key: self.displayColumn(val))
				globals()["self.columnView_"+str(key)].setModel(self.model)
				globals()["self.columnView_"+str(key)].setRootIndex(self.model.index(value))
			
			# Manage button position by adding spaces if number of button < 10
			for i_space in range(nb_button_add_line, (max_button+1), 1):
				spacerItem = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
				globals()["self.horizontalLayout_" + str(cu_hl) + str(i)].addItem(spacerItem)
				
			globals()["self.horizontalLayout_" + str(j)].setStretch(31, 10)
			for i_hl in range(0, nb_horizLayout, 1):
				self.verticalLayout_2.insertLayout(k, globals()["self.horizontalLayout_" + str(i_hl) + str(i)])
				k += 1
				print("insert self.horizontalLayout_{}{} at position {}".format(i_hl, i, k))
			
			
			print("k = {}".format(k))
			self.line = QFrame(self.centralWidget)
			# self.line.setLineWidth(3)
			self.line.setFrameShape(QFrame.Shape.HLine)
			self.line.setFrameShadow(QFrame.Shadow.Sunken)
			self.line.setObjectName("line")
			self.verticalLayout_2.insertWidget(k, self.line)
			print("insert line at position {}".format(k))
			k += 1
			

		self.verticalLayout_2.insertWidget(k, self.stackedWidget)
		print("insert Widget stacked to verticalLayout position 7")			
# 		self.verticalLayout_2.addWidget(self.stackedWidget)
# 		print("add Widget stacked to verticalLayout")
# 		self.verticalLayout_2.addLayout(self.horizontalLayout_5)
# 		print("add horizontalLayout_5 to verticalLayout")
# 		self.verticalLayout_2.addLayout(self.horizontalLayout_6)
# 		print("add horizontalLayout_6 to verticalLayout")
# 		self.verticalLayout_2.addLayout(self.horizontalLayout_7)
# 		print("add horizontalLayout_7 to verticalLayout")
		




	@pyqtSlot(str)
	def displayColumn(self, button):
		print("display column : {}".format(button))
		self.stackedWidget.setCurrentWidget(globals()["self.tab_"+ str(button)])
	# 	for key, value in button_l1.items():
	# 		@pyqtSlot()
	# 		def globals()["self.show_"+str(key)]():
	# 			self.stackedWidget.setCurrentWidget(locals()["self.tab_"+str(key)]


	# #    @pyqtSlot()
	#     def on_pushButton_RAW_clicked(self):
	#         self.stackedWidget.setCurrentWidget(self.tab_RAW)
	# #    @pyqtSlot()
	#     def on_pushButton_CSL_clicked(self):
	#         self.stackedWidget.setCurrentWidget(self.tab_CSL)  
	# #    @pyqtSlot()
	#     def on_pushButton_SET_clicked(self):
	#         self.stackedWidget.setCurrentWidget(self.tab_SET)
	# 
	# 
	#   
	#     def on_columnView_RAW_clicked(self,  index):
	#         indexItem = self.model.index(index.row(), 0, index.parent())
	#         filePath = self.model.filePath(indexItem)
	#         if self.checkBox_ADD.isChecked():
	#             self.lineEdit_INPUT.setText(filePath)
	#         elif self.checkBox_FROM.isChecked():
	#             self.lineEdit_FROM.setText(filePath)
	# 
		def on_columnView_CSL_clicked(self,  index):
		    indexItem = self.model.index(index.row(), 0, index.parent())
		    filePath = self.model.filePath(indexItem)
		    self.lineEdit_CMD.setText(filePath)

	# 
	#     def on_columnView_SET_clicked(self,  index):
	#         indexItem = self.model.index(index.row(), 0, index.parent())
	#         filePath = self.model.filePath(indexItem)
	#         if self.checkBox_ADD.isChecked():
	#             self.lineEdit_INPUT.setText(filePath)
	#         elif self.checkBox_FROM.isChecked():
	#             self.lineEdit_FROM.setText(filePath)        

	#    @pyqtSlot()
	def on_pushButton_ADD_clicked(self):
		current_text = self.lineEdit_CMD
		new_text = "{} {}".format(current_text.displayText(), self.lineEdit_INPUT.displayText())
		self.lineEdit_TERM.setText(new_text)

	#    @pyqtSlot()
	def on_pushButton_CLEAR_clicked(self):
		self.lineEdit_CMD.clear()


	

	#    @pyqtSlot()
	def on_pushButton_HOME_clicked(self):
		self.lineEdit_FROM.setText("${HOME}")

	#    @pyqtSlot()
	def on_pushButton_EXEC_clicked(self):
		current_cmd = self.lineEdit_CMD
		source = self.lineEdit_FROM
		cmd = "xterm -e \'cd {}; {};read\'".format(source.displayText(), current_cmd.displayText())
	#        os.system(cmd)        
		subprocess.Popen(shlex.split(cmd))

	print("end mainWindow class")

        

      

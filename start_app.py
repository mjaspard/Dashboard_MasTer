import sys
from PyQt6.QtWidgets import QApplication
from main_window import MainWindow
app = QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
rc = app.exec()
sys.exit(rc)

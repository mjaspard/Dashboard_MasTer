import sys
from PyQt6.QtWidgets import QApplication
from main_window import MainWindow
app = QApplication(sys.argv)
mainWindow = MainWindow()

# print(mainWindow.__dict__)

mainWindow.show()

rc = app.exec()

sys.exit(rc)

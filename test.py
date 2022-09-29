from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QPushButton,
    QWidget, QLabel, QVBoxLayout, QHBoxLayout
)

import sys


class Window(QWidget):

	def __init__(self):
		super().__init__()

		v = QVBoxLayout()
		h = QHBoxLayout()

		for a in range(10):
			if a == 5:
				var = "cinq"
			else:
				var = a
		
			button = QPushButton(str(a))
			button.pressed.connect(
				lambda val=var: self.button_pressed(val)
			)
			h.addWidget(button)

		v.addLayout(h)
		self.label = QLabel("")
		v.addWidget(self.label)
		self.setLayout(v)

	def button_pressed(self, n):
		self.label.setText(str(n))


app = QApplication(sys.argv)
w = Window()
w.show()
app.exec()
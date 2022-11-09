from PyQt6.QtWidgets import QApplication, QMainWindow

import sys

from package.gui.MainWindow import MainWindow

app = QApplication(sys.argv)

window = MainWindow()

window.show()

app.exec()

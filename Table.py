from PyQt6.QtWidgets import QTableWidget


class Table(QTableWidget):
    def __init__(self):
        super().__init__()
        self.columnCount = 2
        self.rowCount = 10

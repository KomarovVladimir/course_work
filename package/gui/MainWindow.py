from PyQt6.QtWidgets import QMainWindow
from package.gui.ListWidget import ListWidget
from package.gui.ListWidgetItem import ListWidgetItem


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        schedule_list = ListWidget()
        item1 = ListWidgetItem("234234")
        item2 = ListWidgetItem("444")
        schedule_list.addItem(item1)
        schedule_list.addItem(item2)

        self.setCentralWidget(schedule_list)

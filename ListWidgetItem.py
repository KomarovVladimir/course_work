from PyQt6.QtWidgets import QListWidgetItem


class ListWidgetItem(QListWidgetItem):
    def __init__(self, label):
        super(ListWidgetItem, self).__init__()
        self.setText(label)

from PyQt5.QtWidgets import QComboBox, QStyledItemDelegate, QStyle
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel


class CheckableComboBox(QComboBox):
    def __init__(self, parent=None):
        super(CheckableComboBox, self).__init__(parent)
        self.setModel(QStandardItemModel(self))
        self.view().pressed.connect(self.handleItemPressed)
        self.setItemDelegate(CheckableComboBoxDelegate(self))


    def handleItemPressed(self, index):
        item = self.model().itemFromIndex(index)
        if item.checkState() == Qt.Checked:
            item.setCheckState(Qt.Unchecked)
        else:
            item.setCheckState(Qt.Checked)

    def checkedItems(self):
        checked_items = []
        for index in range(self.count()):
            item = self.model().item(index)
            if item.checkState() == Qt.Checked:
                checked_items.append(item.text())
        return checked_items

    def hidePopup(self):
            pass



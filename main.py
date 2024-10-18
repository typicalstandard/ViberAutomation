from PyQt5.Qt import QStandardItem,QFileDialog,QMessageBox
from PyQt5 import  QtWidgets
from ui import Ui_Input_Window
from Custom_widget import CheckableComboBox
from clicker_viber import ViberAutomation
import sys
import py_win_keyboard_layout


def reverse_transliterate(text):
    reverse_mapping = {
        'ф': 'a', 'и': 'b', 'с': 'c', 'в': 'd', 'у': 'e', 'а': 'f', 'п': 'g', 'р': 'h', 'ш': 'i', 'о': 'j',
        'л': 'k', 'д': 'l', 'ь': 'm', 'т': 'n', 'щ': 'o', 'з': 'p', 'й': 'q', 'к': 'r', 'ы': 's', 'е': 't',
        'г': 'u', 'м': 'v', 'ц': 'w', 'ч': 'x', 'н': 'y', 'я': 'z', 'х': '[', 'ъ': ']', 'ж': ';', 'э': "'",
        'б': ',', 'ю': '.', '.': '/'
    }
    return ''.join(reverse_mapping.get(char, char) for char in text)
class MainWindow(QtWidgets.QWidget, Ui_Input_Window):
        def __init__(self):
            MAXIMUM_INPUT_LIMIT = 8
            super(MainWindow, self).__init__()

            self.setupUi(self)
            self.initUI()

            self.pushButton.clicked.connect(self.input_path)
            self.combo_box.currentIndexChanged.connect(self.select_group)

        def initUI(self):
            self.combo_box = CheckableComboBox(self)
            groups = ['Первая', 'Вторая']

            for item in groups:
                item = QStandardItem(item)
                item.setCheckable(True)
                self.combo_box.model().appendRow(item)

            self.verticalLayout_2.addWidget(self.combo_box)
            self.combo_box.setToolTip('Закрывать на esc')
        def select_group(self):
            return self.combo_box.checkedItems()


        def input_path(self):
            file, _ = QFileDialog.getOpenFileName(self, "Выберите файл", "", "Executable Files (*.exe)")
            self.lineEdit.setText(file)

        def ok_callback(self):
            if not self.lineEdit.text():
                QMessageBox.warning(self, "Ошибка", "Поле ввода пустое")
                self.lineEdit.setStyleSheet('border: 2px solid red;')


            elif not self.select_group():
                QMessageBox.warning(self, "Ошибка", "Поле группы не должен быть пустыми")
                self.combo_box.setStyleSheet('border: 2px solid red;')









import traceback


def log_uncaught_exceptions(ex_cls, ex, tb):
    text = '{}: {}:\n'.format(ex_cls.__name__, ex)

    text += ''.join(traceback.format_tb(tb))

    print(text)
    QtWidgets.QMessageBox.critical(None, 'Error', text)

    sys.exit()


sys.excepthook = log_uncaught_exceptions

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Frame = MainWindow()
    Frame.show()
    sys.exit(app.exec_())
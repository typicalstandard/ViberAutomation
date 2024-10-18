from PyQt5.Qt import QStandardItem,QFileDialog,QMessageBox
from PyQt5 import  QtWidgets
from ui import Ui_Input_Window
from Custom_widget import CheckableComboBox
from clicker_viber import ViberAutomation
import sys
import py_win_keyboard_layout



class MainWindow(QtWidgets.QWidget, Ui_Input_Window):
        def __init__(self):
            super(MainWindow, self).__init__()

            self.setupUi(self)

            self.pushButton.clicked.connect(self.input_path)
            self.combo_box.currentIndexChanged.connect(self.select_group)



        def select_group(self):
            return self.combo_box.checkedItems()


        def input_path(self):
            file, _ = QFileDialog.getOpenFileName(self, "Выберите файл", "", "Executable Files (*.exe)")
            self.lineEdit.setText(file)





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
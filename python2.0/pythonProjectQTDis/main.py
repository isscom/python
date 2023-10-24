from PyQt5 import QtWidgets
from guiFunction import Ui_MainWindow
from addFunction import Ui_Form
import sys

# easygui -> tkinter -> PyQt5
class addRow(QtWidgets.QDialog):
    def __init__(self, root):
        super(addRow, self).__init__(root)
        self.main = root
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.readData)
        self.ui.pushButton_2.clicked.connect(self.reset)

    def readData(self):
        name = self.ui.lineEdit.text() if not None else ""
        surname = self.ui.lineEdit_2.text() if not None else ""
        phone = self.ui.lineEdit_3.text() if not None else ""
        address = self.ui.lineEdit_4.text() if not None else ""
        file = self.ui.comboBox.currentText()
        if file == 'First':
            self.main.ui.listWidget.addItem(f'{name} {surname} {phone} {address}')
        else:
            self.main.ui.listWidget_2.addItem(f'{name} {surname} {phone} {address}')
        self.close()

    def reset(self):
        self.close()


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()  # добавляем функции/методы в свой класс из родительского класса
        self.ui = Ui_MainWindow()
        self.dialog = addRow(self)  # !!!
        self.ui.setupUi(self)
        self.ui.putButton.clicked.connect(self.putclicked)
        self.ui.addButton.clicked.connect(self.addclicked)
        self.ui.deleteButton.clicked.connect(self.deleteclicked)

    def putclicked(self):
        print(1)

    def deleteclicked(self):
        data = [i.row() for i in self.ui.listWidget.selectedIndexes()]
        for row in data:
            self.ui.listWidget.takeItem(row)

        data = [i.row() for i in self.ui.listWidget_2.selectedIndexes()]
        for row in data:
            self.ui.listWidget_2.takeItem(row)

    def addclicked(self):
        self.dialog.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    application = mywindow()
    application.show()

    sys.exit(app.exec())

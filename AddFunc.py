import input
import sys
import os
from PySide2 import QtUiTools, QtGui
from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox


class Additional(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()


    def setupUI(self):
        global UI_set

        UI_set = QtUiTools.QUiLoader().load(resource_path("AddWindow.ui"))

        UI_set.Enter.clicked.connect(self.button)
        UI_set.Rate.returnPressed.connect(self.button)
        UI_set.Line.currentIndexChanged.connect(self.info)

        self.setCentralWidget(UI_set)
        self.setWindowTitle("ADD DATA")
        self.resize(530, 300)
        self.show()

    def info(self):
        if UI_set.Line.currentText() == 'BOT':
            UI_set.Label.setText("챔프 1 = 원딜, 챔프 2 = 서폿\n듀오 승률")
        elif UI_set.Line.currentText() == '':
            UI_set.Label.setText("승률")
        else:
            UI_set.Label.setText("챔프 2에 대한 챔프 1의 승률")

    def button(self):
        global champ1
        global champ2
        global mode

        line = UI_set.Line.currentText()
        champ1 = UI_set.Champ1.text()
        champ2 = UI_set.Champ2.text()
        champ1, champ2 = champ1.replace(' ', ''), champ2.replace(' ', '')
        rate = round(float(UI_set.Rate.text()), 2)
        mode = 0
        if UI_set.Line.currentIndex() == 0 or champ1 == '' or champ2 == '':
            self.message()
        elif 0 > float(UI_set.Rate.text()) or 100.00 <float(UI_set.Rate.text()):
            mode = -3
            self.message()
        else:
            mode = input.in_data(line, champ1, champ2, rate)
            if mode != 0:
                result = self.message()
                if result == QMessageBox.Yes:
                    input.add_data(line, champ1, champ2, rate, mode)
                    mode = -2
                    self.message()
            else:
                input.add_data(line, champ1, champ2, rate, mode)
                mode = -2
                self.message()

    def message(self):
        msg = QMessageBox()
        msg.setWindowTitle("Check!")
        msg.setIcon(QMessageBox.NoIcon)

        if UI_set.Line.currentIndex() == 0:
            msg.setText("라인을 입력하세요.")
            msg.setStandardButtons(QMessageBox.Ok)
            return msg.exec_()
        elif champ1.replace(' ', '') == '' or champ2.replace(' ', '') == '':
            msg.setText("챔피언을 입력하세요.")
            msg.setStandardButtons(QMessageBox.Ok)
            return msg.exec_()
        elif mode == -3:
            msg.setText("승률은 0.00 ~ 100.00 사이의 값만 입력할 수 있습니다.")
            return msg.exec_()
        elif mode == -1:
            msg.setText("해당 상성값이 존재합니다.")
            msg.setStandardButtons(QMessageBox.Ok)
            return msg.exec_()
        elif mode > 0:
            msg.setText("해당 상성값이 존재합니다.\n값을 바꾸시겠습니까?")
            msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msg.setDefaultButton(QMessageBox.No)
            return msg.exec_()
        else:
            msg.setText("추가되었습니다.")
            msg.setStandardButtons(QMessageBox.Ok)
            return msg.exec_()


def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)

    return os.path.join(os.path.abspath("."), relative_path)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Additional()
    sys.exit(app.exec_())
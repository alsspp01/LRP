import sys
import os
from PySide2 import QtUiTools, QtGui
from PySide2.QtWidgets import QApplication, QMainWindow


class MainView(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setupUI()

    def setupUI(self):
        global UI_set
        UI_set = QtUiTools.QUiLoader().load(resource_path("Print.ui"))
        self.setCentralWidget(UI_set)
        self.setWindowTitle("UI TEST")
        self.resize(1000,600)
        self.show()


    def Print_buff(buff):
        if(buff==0):
            UI_set.Result.setText("정버프를 추천드립니다.\n")
        else :
            UI_set.Result.setText("역버프를 추천드립니다.\n")
    def Print_gank(gank):
        if(gank[0]==0):
            if(gank[1]==0):
                UI_set.Result.append("탑갱을 추천드립니다\n")
            elif(gank[1]==1):
                UI_set.Result.append("미드갱을 추천드립니다\n")
            else :
                UI_set.Result.append("바텀갱을 추천드립니다\n")
        elif(gank[0]==1):
            if (gank[1] == 0):
                UI_set.Result.append("탑 역갱을 추천드립니다\n")
            elif (gank[1] == 1):
                UI_set.Result.append("미드 역갱을 추천드립니다\n")
            else:
                UI_set.Result.append("바텀 역갱을 추천드립니다\n")
        else :
            if (gank[1] == 0):
                UI_set.Result.append("탑갱을 가지 않는것을 추천드립니다\n")
            elif (gank[1] == 1):
                UI_set.Result.append("미드갱을 가지 않는것을 추천드립니다\n")
            else:
                UI_set.Result.append("바텀갱을 가지 않는것을 추천드립니다\n")
    def Print_obj(obj):
        if (obj==[1, 1, 1, 1]):
            UI_set.Result.append("모든 오브젝트 싸움에서 이길 확률이 높습니다. 최대한 챙기세요.\n")
        elif(obj==[1, 0, 0, 1]):
            UI_set.Result.append("위쪽 오브젝트 싸움에서 이길 확률이 높습니다. 최대한 챙기세요.\n")
        elif(obj==[1, 1, 1, 0]):
            UI_set.Result.append("윗바위게와 아래쪽 오브젝트 싸움에서 이길 확률이 높습니다. 최대한 챙기세요.\n")
        elif(obj==[1, 0, 0, 0]):
            UI_set.Result.append("윗바위게 싸움에서만 주도권이 있습니다. 가능한 한 조심하세요.\n")
        elif(obj==[0, 1, 1, 0]):
            UI_set.Result.append("아래쪽 오브젝트 싸움에서 이길 확률이 높습니다. 최대한 챙기세요.\n")
        elif(obj==[0, 0, 0, 0]):
            UI_set.Result.append("모든 오브젝트에서 주도권이 없습니다. 최대한 조심하게 플레이하세요.\n")
        elif(obj==[0, 1, 0, 0]):
            UI_set.Result.append("아랫바위게 싸움에서만 주도권이 있습니다. 가능한 한 조심하세요.\n")


def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)

    return os.path.join(os.path.abspath("."), relative_path)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = MainView()

    # main.show()

    sys.exit(app.exec_())
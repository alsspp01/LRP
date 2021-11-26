import AddFunc
import StdFunc
import sys
import os
from PySide2 import QtUiTools, QtGui
from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox, QLabel
from PySide2.QtGui import QPixmap, QImage

path = os.getcwd()
def img(obj):
    return path + '\\image\\' + obj + '.png'

from AddFunc import resource_path

Botrate=[0,0]
buff = 0
thief = 0
gank = [0,0]
object = [0,0,0,0]

class MainView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        global temp
        global UI_set
        global top_rate
        global jg_rate
        global mid_rate
        global bot_rate
        global my_team
        global your_team

        UI_set = QtUiTools.QUiLoader().load(resource_path("main.ui"))
        UI_set.Add_Data.clicked.connect(self.AddData)
        UI_set.Top_rec.addItem('추천 챔프')
        UI_set.Jg_rec.addItem('추천 챔프')
        UI_set.Mid_rec.addItem('추천 챔프')
        UI_set.Bot_rec.addItem('추천 챔프')
        UI_set.Enter.clicked.connect(self.button)
        UI_set.Top_2.textChanged.connect(self.RcmdTop)
        UI_set.Jg_2.textChanged.connect(self.RcmdJg)
        UI_set.Mid_2.textChanged.connect(self.RcmdMid)
        UI_set.Bot_2_1.textChanged.connect(self.RcmdBot)
        UI_set.Bot_2_2.textChanged.connect(self.RcmdBot)
        UI_set.Top_rec.currentIndexChanged.connect(self.setTop)
        UI_set.Jg_rec.currentIndexChanged.connect(self.setJg)
        UI_set.Mid_rec.currentIndexChanged.connect(self.setMid)
        UI_set.Bot_rec.currentIndexChanged.connect(self.setBot)
        UI_set.Top_1.textChanged.connect(self.writeTop)
        UI_set.Jg_1.textChanged.connect(self.writeJg)
        UI_set.Mid_1.textChanged.connect(self.writeMid)
        UI_set.Bot_1_1.textChanged.connect(self.writeBot)
        UI_set.Bot_1_2.textChanged.connect(self.writeBot)
        UI_set.label.setPixmap(QtGui.QPixmap(img("Map")))
        my_team = ['top', 'jg', 'mid', 'ad', 'sp']
        your_team = ['top', 'jg', 'mid', 'ad', 'sp']
        my_team[0], my_team[1], my_team[2], my_team[3], my_team[
            4] = UI_set.Top_1.text(), UI_set.Jg_1.text(), UI_set.Mid_1.text(), UI_set.Bot_1_1.text(), UI_set.Bot_1_2.text()
        your_team[0], your_team[1], your_team[2], your_team[3], your_team[
            4] = UI_set.Top_2.text(), UI_set.Jg_2.text(), UI_set.Mid_2.text(), UI_set.Bot_2_1.text(), UI_set.Bot_2_2.text()
        self.setCentralWidget(UI_set)
        self.setWindowTitle("Jungle Route Recommend")
        self.resize(1000, 1000)
        self.show()

    def AddData(self):
        w = AddFunc.Additional()
        self.w.show()

    def RcmdTop(self): #탑 추천챔프를 알려준다. 적팀 라인 챔피언을 먼저 입력하면 라인에딧 아래 콤보박스를 통해 승률이 높은 챔피언을 고를 수 있게 만듦.
        global Top_Rcmd
        their_top = UI_set.Top_2.text().replace(' ', '')
        if their_top != '':
            topdata = StdFunc.input.upload('top')
            rt = 1
            for i in range(len(topdata)):
                if their_top == topdata[i][1] or their_top == topdata[i][2]:
                    rt = 0
                    break
            if rt == 0:
                Top_Rcmd = StdFunc.RcmdChamp('top', their_top)
                UI_set.Top_rec.clear()
                UI_set.Top_rec.addItem('직접 입력')
                for i in range(len(Top_Rcmd)):
                    UI_set.Top_rec.addItem(Top_Rcmd[i])
            else: #만약 이기는 매치업의 챔피언이 없을 경우 Out of Data 출력
                UI_set.Top_rec.clear()
                UI_set.Top_rec.addItem('Out of Data')

        else:
            UI_set.Top_rec.clear()
            UI_set.Top_rec.addItem('추천 챔프')

    def RcmdJg(self): #정글 추천챔프를 알려준다.
        global Jg_Rcmd
        their_jg = UI_set.Jg_2.text().replace(' ', '')
        if their_jg != '':
            jgdata = StdFunc.input.upload('jg')
            rt = 1
            for i in range(len(jgdata)):
                if their_jg == jgdata[i][1] or their_jg == jgdata[i][2]:
                    rt = 0
                    break
            if rt == 0:
                Jg_Rcmd = StdFunc.RcmdChamp('jg', their_jg)
                UI_set.Jg_rec.clear()
                UI_set.Jg_rec.addItem('직접 입력')
                for i in range(len(Jg_Rcmd)):
                    UI_set.Jg_rec.addItem(Jg_Rcmd[i])
            else:
                UI_set.Jg_rec.clear()
                UI_set.Jg_rec.addItem('Out of Data')
        else:
            UI_set.Jg_rec.clear()
            UI_set.Jg_rec.addItem('추천 챔프')

    def RcmdMid(self): #미드 추천챔프를 알려준다.
        global Mid_Rcmd
        their_mid = UI_set.Mid_2.text().replace(' ', '')
        if their_mid != '':
            middata = StdFunc.input.upload('mid')
            rt = 1
            for i in range(len(middata)):
                if their_mid == middata[i][1] or their_mid == middata[i][2]:
                    rt = 0
                    break
            if rt == 0:
                Mid_Rcmd = StdFunc.RcmdChamp('mid', their_mid)
                UI_set.Mid_rec.clear()
                UI_set.Mid_rec.addItem('직접 입력')
                for i in range(len(Mid_Rcmd)):
                    UI_set.Mid_rec.addItem(Mid_Rcmd[i])
            else:
                UI_set.Mid_rec.clear()
                UI_set.Mid_rec.addItem('Out of Data')
        else:
            UI_set.Mid_rec.clear()
            UI_set.Mid_rec.addItem('추천 챔프')

    def RcmdBot(self): #봇 추천챔프를 알려준다.
        global Bot_Rcmd
        botdata = StdFunc.input.upload('bot')
        my_ad, my_sp = UI_set.Bot_1_1.text(), UI_set.Bot_1_2.text()
        their_ad, their_sp = UI_set.Bot_2_1.text(), UI_set.Bot_2_2.text()
        if their_ad != '' and their_sp != '':
            rt = 1
            for i in range(len(botdata)):
                if botdata[i][1] == their_ad and botdata[i][2] == their_sp:
                    rt = 0
                    break
                elif botdata[i][2] == their_ad and botdata[i][1] == their_sp:
                    rt = 0
                    break
            if rt == 0:
                Bot_Rcmd = StdFunc.RcmdChamp_bot(my_ad, my_sp, their_ad, their_sp)
                UI_set.Bot_rec.clear()
                UI_set.Bot_rec.addItem('직접 입력')
                for i in range(len(Bot_Rcmd)):
                    UI_set.Bot_rec.addItem(Bot_Rcmd[i])
            else:
                UI_set.Bot_rec.clear()
                UI_set.Bot_rec.addItem('Out of Data')
        else:
            UI_set.Bot_rec.clear()
            UI_set.Bot_rec.addItem('추천 챔프')

    def setTop(self):
        if UI_set.Top_rec.currentIndex() > 0:
            UI_set.Top_1.setText(UI_set.Top_rec.currentText())

    def setJg(self):
        if UI_set.Jg_rec.currentIndex() > 0:
            UI_set.Jg_1.setText(UI_set.Jg_rec.currentText())

    def setMid(self):
        if UI_set.Mid_rec.currentIndex() > 0:
            UI_set.Mid_1.setText(UI_set.Mid_rec.currentText())

    def setBot(self):
        if UI_set.Bot_rec.currentIndex() > 0:
            bot = UI_set.Bot_rec.currentText().split(' ')
            UI_set.Bot_1_1.setText(bot[0])
            UI_set.Bot_1_2.setText(bot[1])

    def writeTop(self):
        if UI_set.Top_2.text() not in StdFunc.all_champ('top'):
            UI_set.Top_rec.setCurrentIndex(0)
        else:
            if UI_set.Top_1.text() in Top_Rcmd:
                UI_set.Top_rec.setCurrentText(UI_set.Top_1.text())
            else:
                UI_set.Top_rec.setCurrentIndex(0)

    def writeJg(self):
        if UI_set.Jg_2.text() not in StdFunc.all_champ('jg'):
            UI_set.Jg_rec.setCurrentIndex(0)
        else:
            if UI_set.Jg_1.text() in Jg_Rcmd:
                UI_set.Jg_rec.setCurrentText(UI_set.Jg_1.text())
            else:
                UI_set.Jg_rec.setCurrentIndex(0)

    def writeMid(self):
        if UI_set.Mid_2.text() not in StdFunc.all_champ('mid'):
            UI_set.Mid_rec.setCurrentIndex(0)
        else:
            if UI_set.Mid_1.text() in Mid_Rcmd:
                UI_set.Mid_rec.setCurrentText(UI_set.Mid_1.text())
            else:
                UI_set.Mid_rec.setCurrentIndex(0)

    def writeBot(self):
        duo = UI_set.Bot_1_1.text() + ' ' + UI_set.Bot_1_2.text()
        if duo not in StdFunc.RcmdChamp_bot('', '', '', ''):
            UI_set.Bot_rec.setCurrentIndex(0)
        else:
            if duo in Bot_Rcmd:
                UI_set.Bot_rec.setCurrentText(duo)
            else:
                UI_set.Bot_rec.setCurrentIndex(0)

    def button(self):
            global Top_A
            global Top_B
            global Jg_A
            global Jg_B
            global Mid_A
            global Mid_B
            global Bot_A_A
            global Bot_A_B
            global Bot_B_A
            global Bot_B_B
            global Toprate
            global Midrate
            global Jgrate
            global Botrate
            Top_A = UI_set.Top_1.text()
            Top_B = UI_set.Top_2.text()
            Jg_A = UI_set.Jg_1.text()
            Jg_B = UI_set.Jg_2.text()
            Mid_A = UI_set.Mid_1.text()
            Mid_B = UI_set.Mid_2.text()
            Bot_A_A = UI_set.Bot_1_1.text()
            Bot_A_B = UI_set.Bot_1_2.text()
            Bot_B_A = UI_set.Bot_2_1.text()
            Bot_B_B = UI_set.Bot_2_2.text()
            Toprate = StdFunc.top(Top_A, Top_B) #탑 승률
            Jgrate = StdFunc.jg(Jg_A, Jg_B) #정글 승률
            Midrate = StdFunc.mid(Mid_A, Mid_B) #미드 승률
            Botrate = StdFunc.bot(Bot_A_A, Bot_A_B, Bot_B_A, Bot_B_B) #봇 승률
            thief=self.messageBox() #카정 여부 변수, yes=16384  no=65536
            if Jgrate >= 50.00:
                buff = 0 #정버프인지 역버프인지를 정하는 변수, 0일때 정버프, 1일때 역버프를 가리킨다.
                if Midrate >= 50.00:
                    if thief == 16384:
                        UI_set.label_7.setPixmap(QtGui.QPixmap("red_Red.png"))
                        UI_set.label_8.setPixmap(QtGui.QPixmap("red_Blue.png"))
                        if Toprate >= 50.00:
                            if Botrate[0] >= Botrate[1]:
                                gank = [0, 0] #승률 계산 후 어느 쪽 갱킹을 갈 지 정하는 변수, gank[0]은 갱, 역갱, 배제, gank[1]은 라인을 가리킨다.
                                object = [1, 1, 1, 1] #승률 계산 후 어떤 오브젝트를 챙기는 것이 유리한지 정하는 변수, 0은 탑바위게, 1은 봇바위게, 2는 용, 3은 전령을 가리킨다.
                                Print_buff(buff) #main 536번째 줄 참고
                                Print_gank(gank) #main 544번째 줄 참고
                                Print_obj(object) #main 567번째 줄 참고
                            else:
                                gank = [0, 0]
                                object = [1, 0, 0, 1]
                                Print_buff(buff)
                                Print_gank(gank)
                                Print_obj(object)
                        else:
                            if Botrate[0] >= Botrate[1]:
                                gank = [2][0]
                                object = [1, 1, 1, 0]
                                Print_buff(buff)
                                Print_gank(gank)
                                Print_obj(object)
                            else:
                                gank = [2][0]
                                object = [1, 0, 0, 0]
                                Print_buff(buff)
                                Print_gank(gank)
                                Print_obj(object)
                    if thief == 65536:
                        if Toprate >= 50.00:
                            if Botrate[0] >= Botrate[1]:
                                if Toprate >= Midrate:
                                    gank = [0, 0]
                                    Print_buff(buff)
                                    Print_gank(gank)
                                else:
                                    gank = [0, 1]
                                    Print_buff(buff)
                                    Print_gank(gank)
                                object = [1, 1, 1, 1]
                                Print_obj(object)
                            else:
                                if Toprate >= Midrate:
                                    gank = [0, 0]
                                    Print_buff(buff)
                                    Print_gank(gank)
                                else:
                                    gank = [0, 1]
                                    Print_buff(buff)
                                    Print_gank(gank)
                                object = [1, 0, 0, 1]
                                Print_obj(object)
                        else:
                            if Botrate[0] >= 50.00:
                                gank = [0, 1]
                                object = [0, 1, 1, 0]
                                Print_buff(buff)
                                Print_gank(gank)
                                Print_obj(object)
                            else:
                                gank = [0, 1]
                                object = [0, 0, 0, 0]
                                Print_buff(buff)
                                Print_gank(gank)
                                Print_obj(object)
                else:
                    if Toprate >= 50.00:
                        if Botrate[0] >= 50.00:
                            if Toprate >= Botrate[0]:
                                gank = [0, 0]
                                object = [1, 0, 0, 1]
                                Print_buff(buff)
                                Print_gank(gank)
                                Print_obj(object)
                            else:
                                gank = [0, 2]
                                object = [0, 1, 1, 0]
                                Print_buff(buff)
                                Print_gank(gank)
                                Print_obj(object)
                        else:
                            gank = [0, 0]
                            object = [1, 0, 0, 1]
                            Print_buff(buff)
                            Print_gank(gank)
                            Print_obj(object)
                    else:
                        if Botrate[0] >= 50.00:
                            gank = [0, 2]
                            object = [0, 1, 1, 0]
                            Print_buff(buff)
                            Print_gank(gank)
                            Print_obj(object)
                        else:
                            if Toprate >= Midrate:
                                gank = [1, 0]
                                object = [0, 0, 0, 0]
                                Print_buff(buff)
                                Print_gank(gank)
                                Print_obj(object)
                            else:
                                gank = [1, 1]
                                object = [0, 0, 0, 0]
                                Print_buff(buff)
                                Print_gank(gank)
                                Print_obj(object)
                if Jgrate < 50.00:
                    buff = 1
                    if Midrate >= 50.00:
                        if Toprate >= 50.00:
                            if Botrate[0] >= 50.00:
                                gank = [0, 2]
                                object = [0, 1, 1, 0]
                                Print_buff(buff)
                                Print_gank(gank)
                                Print_obj(object)
                            else:
                                gank = [1, 0]
                                object = [1, 0, 0, 1]
                                Print_buff(buff)
                                Print_gank(gank)
                                Print_obj(object)
                        else:
                            if Botrate[0] >= 50.00:
                                gank = [0, 2]
                                object = [0, 1, 1, 0]
                                Print_buff(buff)
                                Print_gank(gank)
                                Print_obj(object)
                            else:
                                if Toprate >= 50.00:
                                    gank = [1, 1]
                                    object = [1, 0, 0, 1]
                                    Print_buff(buff)
                                    Print_gank(gank)
                                    Print_obj(object)
                    else:
                        if Toprate >= 50.00:
                            if Botrate[0] >= 50.00:
                                gank = [1, 1]
                                object = [0, 0, 0, 0]
                                Print_buff(buff)
                                Print_gank(gank)
                                Print_obj(object)
                            else:
                                if Midrate >= Botrate:
                                    gank = [1, 2]
                                    object = [0, 1, 0, 0]
                                    Print_buff(buff)
                                    Print_gank(gank)
                                    Print_obj(object)
                                else:
                                    gank = [1, 1]
                                    object = [0, 1, 0, 0]
                                    Print_buff(buff)
                                    Print_gank(gank)
                                    Print_obj(object)
                        else:
                            if Botrate[0] >= 50.00:
                                if Toprate >= Midrate:
                                    gank = [1, 1]
                                    object = [1, 0, 0, 0]
                                    Print_buff(buff)
                                    Print_gank(gank)
                                    Print_obj(object)
                                else:
                                    gank = [1, 0]
                                    object = [1, 0, 0, 0]
                                    Print_buff(buff)
                                    Print_gank(gank)
                                    Print_obj(object)
                            else:
                                gank = [2][0]
                                object = [0, 0, 0, 0]
                                Print_buff(buff)
                                Print_gank(gank)
                                Print_obj(object)
            if Jgrate < 50.00:
                buff = 1
                if Midrate >= 50.00:
                    if Toprate >= 50.00:
                        if Botrate[0] >= 50.00:
                            gank = [0, 2]
                            object = [0, 1, 1, 0]
                            Print_buff(buff)
                            Print_gank(gank)
                            Print_obj(object)
                        else:
                            gank = [1, 0]
                            object = [1, 0, 0, 1]
                            Print_buff(buff)
                            Print_gank(gank)
                            Print_obj(object)
                    else:
                        if Botrate[0] >= 50.00:
                            gank = [0, 2]
                            object = [0, 1, 1, 0]
                            Print_buff(buff)
                            Print_gank(gank)
                            Print_obj(object)
                        else:
                            if Toprate >= 50.00:
                                gank = [1, 1]
                                object = [1, 0, 0, 1]
                                Print_buff(buff)
                                Print_gank(gank)
                                Print_obj(object)
                else:
                    if Toprate >= 50.00:
                        if Botrate[0] >= 50.00:
                            gank = [1, 1]
                            object = [0, 0, 0, 0]
                            Print_buff(buff)
                            Print_gank(gank)
                            Print_obj(object)
                        else:
                            if Midrate >= Botrate:
                                gank = [1, 2]
                                object = [0, 1, 0, 0]
                                Print_buff(buff)
                                Print_gank(gank)
                                Print_obj(object)
                            else:
                                gank = [1, 1]
                                object = [0, 1, 0, 0]
                                Print_buff(buff)
                                Print_gank(gank)
                                Print_obj(object)
                    else:
                        if Botrate[0] >= 50.00:
                            if Toprate >= Midrate:
                                gank = [1, 1]
                                object = [1, 0, 0, 0]
                                Print_buff(buff)
                                Print_gank(gank)
                                Print_obj(object)
                            else:
                                gank = [1, 0]
                                object = [1, 0, 0, 0]
                                Print_buff(buff)
                                Print_gank(gank)
                                Print_obj(object)
                        else:
                            gank = [2][0]
                            object = [0, 0, 0, 0]
                            Print_buff(buff)
                            Print_gank(gank)
                            Print_obj(object)

    def messageBox(self): #챔피언 데이터가 없거나 특정상황에서 카정을 물을 때 나오는 팝업창
        msgBox = QMessageBox()
        global Toprate
        global Midrate
        global Jgrate
        global Botrate
        exist = ['', '', '', '']
        if Toprate == 0 or Jgrate == 0 or Midrate == 0 or Botrate[0] == 0: #챔피언 데이터가 없는 상황
            if Toprate == 0:
                exist[0] = '탑 승률'
            if Jgrate == 0:
                exist[1] == '정글 승률'
            if Midrate == 0:
                exist[2] == '미드 승률'
            if Botrate[0] == 0:
                exist[3] == '바텀 승률'
            ment = ''
            for i in range(4):
                ment+=exist[i]
                if exist[i] != '':
                    ment+=', '
            msgBox.setWindowTitle('Out of Data')
            msgBox.setText(ment + '존재하지 않습니다.\n승률 데이터를 추가하거나 다른 챔피언을 입력하세요.')
            msgBox.setStandardButtons(QMessageBox.Ok)
            return msgBox.exec()
        elif(Midrate>=50 and Jgrate>=50): #카정 여부를 묻는 상황, 카정은 정글 승률과 미드 승률 둘다 우위에 있을 때에만 확인한다.
            msgBox.setText("카정")
            msgBox.setInformativeText("카정을 가시겠습니까?")
            msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msgBox.setDefaultButton(QMessageBox.Yes)
            return msgBox.exec_()

def Print_buff(Buff): #계산 결과를 통해 어느쪽 정글을 먼저 먹는 것이 유리한지 알려준다.
    if(Buff==0):
        UI_set.Result.setText("정버프를 추천드립니다.\n")
        UI_set.label_2.setPixmap(QtGui.QPixmap("blue_Red.png"))
    else :
        UI_set.Result.setText("역버프를 추천드립니다.\n")
        UI_set.label_2.setPixmap(QtGui.QPixmap("blue_Blue.png"))

def Print_gank(Gank): #계산 결과를 통해 어느 라인에 갱킹, 혹은 역갱킹을 가는 것이 유리한지 알려준다.
    if(Gank[0]==0):
        if(Gank[1]==0):
            UI_set.Result.append("탑갱을 추천드립니다\n")
        elif(Gank[1]==1):
            UI_set.Result.append("미드갱을 추천드립니다\n")
        else :
            UI_set.Result.append("바텀갱을 추천드립니다\n")
    elif(Gank[0]==1):
        if (Gank[1] == 0):
            UI_set.Result.append("탑 역갱을 추천드립니다\n")
        elif (Gank[1] == 1):
            UI_set.Result.append("미드 역갱을 추천드립니다\n")
        else:
            UI_set.Result.append("바텀 역갱을 추천드립니다\n")
    else :
        if (Gank[1] == 0):
            UI_set.Result.append("탑갱을 가지 않는것을 추천드립니다\n")
        elif (Gank[1] == 1):
            UI_set.Result.append("미드갱을 가지 않는것을 추천드립니다\n")
        else:
            UI_set.Result.append("바텀갱을 가지 않는것을 추천드립니다\n")

def Print_obj(Obj): #계산 결과를 통해 어떤 오브젝트를 챙길 가능성이 높은지를 알려준다.
    if (Obj==[1, 1, 1, 1]):
        UI_set.Result.append("모든 오브젝트 싸움에서 이길 확률이 높습니다. 최대한 챙기세요.\n")
        UI_set.label_3.setPixmap(QtGui.QPixmap(img("top_RS")))
        UI_set.label_4.setPixmap(QtGui.QPixmap(img("bot_RS")))
        UI_set.label_5.setPixmap(QtGui.QPixmap(img("Dragon")))
        UI_set.label_6.setPixmap(QtGui.QPixmap(img("Herald")))
    elif(Obj==[1, 0, 0, 1]):
        UI_set.Result.append("위쪽 오브젝트 싸움에서 이길 확률이 높습니다. 최대한 챙기세요.\n")
        UI_set.label_3.setPixmap(QtGui.QPixmap(img("top_RS")))
        UI_set.label_6.setPixmap(QtGui.QPixmap(img("Herald")))
    elif(Obj==[1, 1, 1, 0]):
        UI_set.Result.append("윗바위게와 아래쪽 오브젝트 싸움에서 이길 확률이 높습니다. 최대한 챙기세요.\n")
        UI_set.label_3.setPixmap(QtGui.QPixmap(img("top_RS")))
        UI_set.label_4.setPixmap(QtGui.QPixmap(img("bot_RS")))
        UI_set.label_5.setPixmap(QtGui.QPixmap(img("Dragon")))
    elif(Obj==[1, 0, 0, 0]):
        UI_set.Result.append("윗바위게 싸움에서만 주도권이 있습니다. 가능한 한 조심하세요.\n")
        UI_set.label_3.setPixmap(QtGui.QPixmap(img("top_RS")))
    elif(Obj==[0, 1, 1, 0]):
        UI_set.Result.append("아래쪽 오브젝트 싸움에서 이길 확률이 높습니다. 최대한 챙기세요.\n")
        UI_set.label_4.setPixmap(QtGui.QPixmap(img("bot_RS")))
        UI_set.label_5.setPixmap(QtGui.QPixmap(img("Dragon")))
    elif(Obj==[0, 0, 0, 0]):
        UI_set.Result.append("모든 오브젝트에서 주도권이 없습니다. 최대한 조심하게 플레이하세요.\n")
    elif(Obj==[0, 1, 0, 0]):
        UI_set.Result.append("아랫바위게 싸움에서만 주도권이 있습니다. 가능한 한 조심하세요.\n")
        UI_set.label_4.setPixmap(QtGui.QPixmap(img("bot_RS")))

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainView()
    sys.exit(app.exec_())
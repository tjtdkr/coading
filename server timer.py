import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from threading import Timer
import time, urllib3

QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)


class CWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.year = QLCDNumber(self)
        self.month = QLCDNumber(self)
        self.day = QLCDNumber(self)
        self.hour = QLCDNumber(self)
        self.min = QLCDNumber(self)
        self.sec = QLCDNumber(self)
        self.initUI()

    def initUI(self):
        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.year)
        hbox1.addWidget(self.month)
        hbox1.addWidget(self.day)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.hour)
        hbox2.addWidget(self.min)
        hbox2.addWidget(self.sec)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)

        self.setLayout(vbox)

        self.setWindowTitle('시계')
        self.setGeometry(200, 200, 400, 200)

        self.showtime()

        self.lbl = QLabel(self)
        self.lbl.move(60, 40)

        qle = QLineEdit(self)
        qle.move(60, 100)
        qle.textChanged[str].connect(self.onChanged)

        self.setWindowTitle('server timer')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def showtime(self):
        # 1970년 1월 1일 0시 0분 0초 부터 현재까지 경과시간 (초단위)
        t = time.time()
        # 한국 시간 얻기
        date = urllib.request('qle').headers['Date']
        self.year.display(date.tm_year)
        self.month.display(date.tm_mon)
        self.day.display(date.tm_mday)
        self.hour.display(date.tm_hour)
        self.min.display(date.tm_min)
        self.sec.display(date.tm_sec)

        # 타이머 설정  (1초마다, 콜백함수)
        timer = Timer(1, self.showtime)
        timer.start()

    def onChanged(self, text):
            self.lbl.setText(text)
            self.lbl.adjustSize()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = CWidget()
    w.show()
    sys.exit(app.exec_())

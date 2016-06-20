#!/usr/bin/python3
# -*- conding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.Qt import *
import sys
import subprocess


class MainWindow(QMainWindow):

    ADDR = ""

    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()

    def initUI(self):

        self.resize(640, 480)

        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignCenter)
        self.btn = QPushButton()
        self.btn.setText('Ping')
        self.btn.setMaximumWidth(40)

        self.textEditAddr = QTextEdit()
        self.textEditAddr.setMaximumHeight(20)
        self.textEditAddr.setText = '127.0.0.1'
        self.textEditOutput = QTextEdit()

        self.layout.addWidget(self.textEditAddr)
        self.layout.addWidget(self.textEditOutput)
        self.layout.addWidget(self.btn)

        self.btn.clicked.connect(self.ping)

        self.setCentralWidget(QWidget())
        self.centralWidget().setLayout(self.layout)
        self.show()

    def ping(self):

        self.textEditOutput.clear()
        for count in range(5):
            ping_response = subprocess.Popen(['/bin/ping', '-c1',
                                              '-w100',
                                              self.textEditAddr.toPlainText()],
                                             stdout=subprocess.PIPE)\
                .stdout.read()

            self.textEditOutput.append(ping_response.decode("utf-8"))

if __name__ == '__main__':

    app = QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec_())

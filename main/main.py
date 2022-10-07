import sys
import os
import datetime
import pyscreenrec
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic
from qt_material import *

rec =  pyscreenrec.ScreenRecorder()

app = QApplication(sys.argv)

class ScreenRec(QMainWindow):
    def __init__(self):
        super(ScreenRec, self).__init__()
        uic.loadUi("mainui.ui", self)

        extra = {

            # Button colors
            'danger': '#dc3545',
            'warning': '#ffc107',
            'success': '#17a2b8',

            # Font
            'font_family': 'Roboto',
        }

        apply_stylesheet(app, theme='dark_teal.xml', extra=extra)

        self.recording = False
        self.paused = False

        self.rec.setProperty('class', 'danger')
        self.play.setProperty('class', 'success')

        self.rec.setIcon(QIcon(os.path.join(os.path.curdir, 'FEATHER ICONS', 'screenrec', 'disc.svg')))
        self.play.setIcon(QIcon(os.path.join(os.path.curdir, 'FEATHER ICONS', 'screenrec', 'play-circle.svg')))

        self.rec.setIconSize(QSize(40, 40))
        self.play.setIconSize(QSize(40, 40))

        self.rec.clicked.connect(self.startRec)
        self.play.clicked.connect(self.playRec)

        self.actionStart.triggered.connect(self.startRec)
        self.actionStop.triggered.connect(self.startRec)
        self.actionPlay.triggered.connect(self.playRec)
        self.actionPause.triggered.connect(self.playRec)

        self.name.setPlaceholderText('File name')

    def startRec(self):
        if self.recording:
            self.stopRec()

        else:
            fn = self.name.text()
            if fn:
                self.play.setIcon(QIcon(os.path.join(os.path.curdir, 'FEATHER ICONS', 'screenrec', 'pause-circle.svg')))
                self.rec.setIcon(QIcon(os.path.join(os.path.curdir, 'FEATHER ICONS', 'screenrec', 'stop-circle.svg')))
                rec.start_recording(str(fn + '.mp4'), 15)
                self.recording = True
            

    def stopRec(self):
        rec.stop_recording()
        self.rec.setIcon(QIcon(os.path.join(os.path.curdir, 'FEATHER ICONS', 'screenrec', 'disc.svg')))
        
        self.recording = False

        self.FN.setText('')
    
    def pauseRec(self):
        rec.pause_recording()
        self.play.setIcon(QIcon(os.path.join(os.path.curdir, 'FEATHER ICONS', 'screenrec', 'play-circle.svg')))

        self.paused = True

    def playRec(self):
        if self.paused:
            rec.resume_recording()
            self.play.setIcon(QIcon(os.path.join(os.path.curdir, 'FEATHER ICONS', 'screenrec', 'pause-circle.svg')))
            self.paused = False

        else:
            self.pauseRec()

def main():
    window = ScreenRec()
    window.show()
    
    app.exec_()

if __name__ == "__main__":
    main()

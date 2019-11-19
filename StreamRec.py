from PyQt5 import QtCore, QtGui, QtWidgets
import os
import subprocess as sp
import PyQt5,sys
from PyQt5.QtCore import pyqtSlot
class MainWindow(PyQt5.QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.setObjectName("Streamer")
        self.resize(503, 378)
        self.Resolution=''
        self.record_command =['ffmpeg',
                 '-f','mjpeg',
                 '-re',
                 '-i','http://127.0.0.1:8081/?action=stream',
                '-q:v','10',
                 '/home/pi/Videos/recording_(date).mpeg' ]
        self.record_proc = sp.Popen(self.record_command, stdin=sp.PIPE, stderr=sp.PIPE)
        self.recordButton = QtWidgets.QPushButton(self)
        self.recordButton.setGeometry(QtCore.QRect(80, 80, 121, 23))
        self.recordButton.setObjectName("recordButton")
        self.streamButton = QtWidgets.QPushButton(self)
        self.streamButton.setGeometry(QtCore.QRect(260, 80, 131, 23))
        self.streamButton.setObjectName("pushButton_2")
        self.toolButton_3 = QtWidgets.QToolButton(self)
        self.toolButton_3.setGeometry(QtCore.QRect(80, 130, 121, 23))
        self.toolButton_3.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.toolButton_3.setPopupMode(QtWidgets.QToolButton.MenuButtonPopup)
        self.toolButton_3.setObjectName("toolButton_3")
        self.pushButton_3 = QtWidgets.QPushButton(self)
        self.pushButton_3.setGeometry(QtCore.QRect(340, 320, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.startrec=0
        self.startstr=0
        menu = PyQt5.QtWidgets.QMenu()
        menu.addAction('1024x786', self.Action1)
        menu.addAction('640x480', self.Action2)
        self.toolButton_3.setMenu(menu)
        self.recordButton.clicked.connect(self._Recording)
        self.streamButton.clicked.connect(self._Streaming)
        self.rec_gr= QtWidgets.QButtonGroup()
        self.rec_gr.addButton(self.recordButton)
        self.rec_gr.addButton(self.streamButton)
        self.rec_gr.setExclusive(False)
        self.show()
    @pyqtSlot()
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.recordButton.setText(_translate("Dialog", "Start Recording"))
        self.streamButton.setText(_translate("Dialog", "Start Streaming"))
        self.toolButton_3.setText(_translate("Dialog", "Set Resolution"))
        self.pushButton_3.setText(_translate("Dialog", "Exit"))
    def Action1(self):    
        print ('Resolution is 1024x786')
        self.toolButton_3.setText("1024x786")
        self.Resolution='1024x786'    
    def Action2(self):
        print ('Resolution is 640x480')
        self.toolButton_3.setText("640x480")
        self.Resolution='640x480'
    def _Recording(self):
        
        recordButton=self.sender()
        self.startrec=self.startrec+1
        if (self.startrec==1):
            print("Recording")
            self.recordButton.setText("Stop Recording")
            stdout, stderr = self.record_proc.communicate()
        elif(self.startrec==2):
            print("Recording Stopped")
            self.recordButton.setText("Start Recording")
            self.record_proc.terminate() 
            self.startrec=0
    def _Streaming(self):
        streamButton=self.sender()
        self.startstr=self.startstr+1
        
        if (self.startstr==1):
            self.stream_command =['./mjpeg.sh','start','-r',self.Resolution ]
            self.stream_proc = sp.Popen(record_command, stdin=sp.PIPE, stderr=sp.PIPE)
            stdout, stderr = self.stream_proc.communicate()
            print("Streaming")
            print(stderr)
            self.streamButton.setText("Stop Streaming")
            
        elif(self.startstr==2):
            os.system('./mjpeg.sh stop')
            self.stream_proc.terminate()
            print("Recording Stopped")
            self.streamButton.setText("Start Streaming")
            self.startstr=0


    

if __name__ == "__main__":
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    
    sys.exit(app.exec_())

#uncomment for a good joke
#import antigravity

from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import QThread, pyqtSignal
import paho.mqtt.client as mqtt
import threading
import sys
import time

host = "192.168.0.20"
topic = "DATA"

class MyThread(QThread):
    dataSignal = pyqtSignal('PyQt_PyObject')

    def __init__(self):
        QThread.__init__(self)
        self.MQTT_init()
    
    def MQTT_init(self):
        print("\nDAQC Server Ready")
        print("Waiting to Establish Connection")

        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_disconnect = self.on_disconnect        
        self.client.connect(host, 1883, 60)
        self.client.loop_start()

        print("Connection Established")

    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code: " + str(rc))
        time.sleep(1)
        self.client.on_message = self.on_message
        self.client.subscribe(topic)
        error  = rc
        return error

    def on_disconnect(self, client, userdata , rc = 0):
        print("disconnected")
        self.client.loop_stop()
        
    def on_message(self, client, userdata, msg):
        raw = str(msg.payload)[2:-1] 
        data = raw.split(',')
    
        for i in range(0, len(data)):
            data[i] = (data[i].lstrip(" "))
    
        data[-1] = data[-1].rstrip("\\n")

        self.dataSignal.emit(data)

class MyGUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyGUI, self).__init__()

        uic.loadUi('IcarusGUI.ui', self)
        
        #self.thread = MyThread()
        
        self.batteryProgressBar.setMaximum(11)
        #self.batteryProgressBar.setValue(750)
        self.batteryLCD.setSegmentStyle(2)
        #self.batteryLCD.display(str(1500.12))

        self.chamberPProgressBar.setMaximum(1500)
        self.chamberPProgressBar.setValue(750)
        self.chamberPLCD.setSegmentStyle(2)
        self.chamberPLCD.display(str(1500.12))

        self.chamberTProgressBar.setMaximum(1500)
        self.chamberTProgressBar.setValue(750)
        self.chamberTLCD.setSegmentStyle(2)
        self.chamberTLCD.display(str(1500.12))

        self.thrustProgressBar.setMaximum(1500)
        self.thrustProgressBar.setValue(750)
        self.thrustLCD.setSegmentStyle(2)
        self.thrustLCD.display(str(1500.12))

        self.launchPushButton.clicked.connect(self.launch)

        #self.thread.dataSignal.connect(self.displayData)

    def launch(self, data):
        if(self.ignitorSafetyCheckBox.isChecked() != True):
            print("Launch")

    def displayData(self, data):
        #data[1] = float(data[1]) * 40
        #self.timeBox.setText(data[0])
        print(data)
        #self.batteryProgressBar.setValue(data[1])
        #self.batteryLCD.display((data[1]))

def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    window= MyGUI()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()



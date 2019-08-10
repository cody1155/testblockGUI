from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys
import time


class MyGUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi('IcarusGUI.ui', self)

        self.batteryProgressBar.setMaximum(1500)
        self.batteryProgressBar.setValue(750)
        self.batteryLCD.setSegmentStyle(2)
        self.batteryLCD.display(str(1500.12))

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
            

    def launch(self):
        if(self.ignitorSafetyCheckBox.isChecked() != True):
            print("Launch")
        
        

def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    window= MyGUI()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

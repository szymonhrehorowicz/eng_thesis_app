import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QTimer
from PySide6.QtWebEngineWidgets import QWebEngineView
from ui_form import Ui_MainWindow
###
from check_connection import is_connected
from MathEquation import MathEquation
from MainMenuHandler import MainMenuHandler
from FanControlsHandler import FanControlsHandler
from HeaterControlsHandler import HeaterControlsHandler
from BB import BB
from PID import PID
from Serial import Serial
from COM import COM

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.fanPIDequationwebView = QWebEngineView()
        self.heaterPIDequationwebView = QWebEngineView()
        self.fanPIDequation = MathEquation(self.fanPIDequationwebView)
        self.heaterPIDequation = MathEquation(self.heaterPIDequationwebView)
        self.mainMenuHandler = MainMenuHandler(self)
        # Controllers
        self.fanBBcontroller = BB()
        self.fanPIDcontroller = PID()
        self.fanControlsHandler = FanControlsHandler(self, self.fanPIDcontroller, self.fanBBcontroller)
        self.heaterBBcontroller = BB()
        self.heaterPIDcontroller = PID()
        self.heaterControlsHandler = HeaterControlsHandler(self, self.heaterPIDcontroller, self.heaterBBcontroller)
        # Serial
        self.serial = Serial(self)
        self.COM = COM(self)

        # DEFAULT LOCATION
        self.mainMenuHandler.open_heater()
        self.mainMenuHandler.set_heater_bb()

        # Connect button
        self.ui.btnConnect.clicked.connect(self.serial.slot_btnConnect)

        # Main menu buttons
        self.ui.btnHeaterControls.clicked.connect(self.mainMenuHandler.open_heater)
        self.ui.btnFanControls.clicked.connect(self.mainMenuHandler.open_fan)
        self.ui.btnDataExport.clicked.connect(self.mainMenuHandler.open_export)
        self.ui.btnHelp.clicked.connect(self.mainMenuHandler.open_help)
        # Heater controller select buttons
        self.ui.btnHeaterControllerSetBB.clicked.connect(self.mainMenuHandler.set_heater_bb)
        self.ui.btnHeaterControllerSetPID.clicked.connect(self.mainMenuHandler.set_heater_pid)
        self.ui.btnHeaterControllerSetHighPower.clicked.connect(self.mainMenuHandler.set_heater_high_power)
        self.ui.btnHeaterControllerSetLowPower.clicked.connect(self.mainMenuHandler.set_heater_low_power)
        self.ui.btnHeaterControllerSetRightCoil.clicked.connect(self.mainMenuHandler.set_heater_right_coil)
        self.ui.btnHeaterControllerSetLeftCoil.clicked.connect(self.mainMenuHandler.set_heater_left_coil)
        # Fan controller select buttons
        self.ui.btnFanControllerSetBB.clicked.connect(self.mainMenuHandler.set_fan_bb)
        self.ui.btnFanControllerSetPID.clicked.connect(self.mainMenuHandler.set_fan_pid)
        #Heater BB inputs
        self.ui.inHeaterBBSetValue.editingFinished.connect(self.heaterControlsHandler.bb_setValue)
        self.ui.inHeaterBBHysteresis.editingFinished.connect(self.heaterControlsHandler.bb_setHysteresis)
        self.ui.inHeaterBBPower.valueChanged.connect(self.heaterControlsHandler.bb_setPower)
        # Heater PID inputs
        self.ui.inHeaterPIDSetValue.editingFinished.connect(self.heaterControlsHandler.pid_setValue)
        self.ui.inHeaterPID_Kp.editingFinished.connect(self.heaterControlsHandler.pid_setKp)
        self.ui.inHeaterPID_Ki.editingFinished.connect(self.heaterControlsHandler.pid_setKi)
        self.ui.inHeaterPID_Kd.editingFinished.connect(self.heaterControlsHandler.pid_setKd)
        self.ui.inHeaterPID_Kaw.editingFinished.connect(self.heaterControlsHandler.pid_setKaw)
        self.ui.inHeaterPID_Ti.editingFinished.connect(self.heaterControlsHandler.pid_setTi)
        self.ui.inHeaterPID_Td.editingFinished.connect(self.heaterControlsHandler.pid_setTd)
        # Fan BB inputs
        self.ui.inFanBBSetValue.editingFinished.connect(self.fanControlsHandler.bb_setValue)
        self.ui.inFanBBHysteresis.editingFinished.connect(self.fanControlsHandler.bb_setHysteresis)
        # Fan PID inputs
        self.ui.inFanPIDSetValue.editingFinished.connect(self.fanControlsHandler.pid_setValue)
        self.ui.inFanPID_Kp.editingFinished.connect(self.fanControlsHandler.pid_setKp)
        self.ui.inFanPID_Ki.editingFinished.connect(self.fanControlsHandler.pid_setKi)
        self.ui.inFanPID_Kd.editingFinished.connect(self.fanControlsHandler.pid_setKd)
        self.ui.inFanPID_Kaw.editingFinished.connect(self.fanControlsHandler.pid_setKaw)
        self.ui.inFanPID_Ti.editingFinished.connect(self.fanControlsHandler.pid_setTi)
        self.ui.inFanPID_Td.editingFinished.connect(self.fanControlsHandler.pid_setTd)


        if is_connected():
            self.ui.fanEquation.addWidget(self.fanPIDequationwebView)
            self.ui.heaterEquation.addWidget(self.heaterPIDequationwebView)


        #self.timer = QTimer()
        #self.timer.setInterval(1000)
        #self.timer.timeout.connect(self.tim_1000ms_IRS)
        #self.timer.start()

    def tim_1000ms_IRS(self):
        pass



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())

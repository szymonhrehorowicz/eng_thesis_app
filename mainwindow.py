import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtWebEngineWidgets import QWebEngineView
from ui_form import Ui_MainWindow
from PySide6.QtCore import QTimer
###
from check_connection import is_connected
from MathEquation import MathEquation
from MainMenuHandler import MainMenuHandler, INDICES
from FanControlsHandler import FanControlsHandler
from HeaterControlsHandler import HeaterControlsHandler
from BB import BB
from PID import PID
from Serial import Serial
from COM import COM
from HeaterController import HeaterController
from FanController import FanController
from FanBBGraph import FanBBGraph
from FanPIDGraph import FanPIDGraph
from HeaterBBGraph import HeaterBBGraph
from HeaterPIDGraph import HeaterPIDGraph

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
        self.fanController = FanController()
        self.heaterController = HeaterController()
        # Serial
        self.serial = Serial(self)
        self.COM = COM(self)
        # Graphs
        self.fanBBgraph = FanBBGraph(self, self.ui.layFanBBGraph, 'RPM')
        self.fanPIDgraph = FanPIDGraph(self, self.ui.layFanPIDGraph, 'RPM')
        self.heaterBBgraph = HeaterBBGraph(self, self.ui.layHeaterBBGraph, 'degC')
        self.heaterPIDgraph = HeaterPIDGraph(self, self.ui.layHeaterPIDGraph, 'degC')

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

        # Fan BB Graph buttons
        self.ui.btnFanBB_graph_x.clicked.connect(self.fanBBgraph.set_value)
        self.ui.btnFanBB_graph_x_max.clicked.connect(self.fanBBgraph.set_threshold_top)
        self.ui.btnFanBB_graph_x_min.clicked.connect(self.fanBBgraph.set_threshold_bottom)
        self.ui.btnFanBB_graph_u_max.clicked.connect(self.fanBBgraph.set_u_max)
        self.ui.btnFanBB_graph_u_min.clicked.connect(self.fanBBgraph.set_u_min)
        self.ui.btnFanBB_graph_y.clicked.connect(self.fanBBgraph.set_y)
        self.ui.btnFanBB_graph_mode.clicked.connect(self.fanBBgraph.set_mode)
        # Fan PID Graph buttons
        self.ui.btnFanPID_graph_x.clicked.connect(self.fanPIDgraph.set_value)
        self.ui.btnFanPID_graph_e.clicked.connect(self.fanPIDgraph.set_e)
        self.ui.btnFanPID_graph_int_e.clicked.connect(self.fanPIDgraph.set_int_e)
        self.ui.btnFanPID_graph_aw_int_e.clicked.connect(self.fanPIDgraph.set_aw_int_e)
        self.ui.btnFanPID_graph_k_p.clicked.connect(self.fanPIDgraph.set_k_p)
        self.ui.btnFanPID_graph_k_i.clicked.connect(self.fanPIDgraph.set_k_i)
        self.ui.btnFanPID_graph_k_d.clicked.connect(self.fanPIDgraph.set_k_d)
        self.ui.btnFanPID_graph_k_aw.clicked.connect(self.fanPIDgraph.set_k_aw)
        self.ui.btnFanPID_graph_u.clicked.connect(self.fanPIDgraph.set_u)
        self.ui.btnFanPID_graph_u_sat.clicked.connect(self.fanPIDgraph.set_u_sat)
        self.ui.btnFanPID_graph_u_p.clicked.connect(self.fanPIDgraph.set_u_p)
        self.ui.btnFanPID_graph_u_i.clicked.connect(self.fanPIDgraph.set_u_i)
        self.ui.btnFanPID_graph_u_d.clicked.connect(self.fanPIDgraph.set_u_d)
        self.ui.btnFanPID_graph_u_max.clicked.connect(self.fanPIDgraph.set_u_max)
        self.ui.btnFanPID_graph_u_max.clicked.connect(self.fanPIDgraph.set_u_min)
        self.ui.btnFanPID_graph_y.clicked.connect(self.fanPIDgraph.set_y)
        self.ui.btnFanPID_graph_mode.clicked.connect(self.fanPIDgraph.set_mode)
        # Heater BB Graph buttons
        self.ui.btnHeaterBB_graph_x.clicked.connect(self.heaterBBgraph.set_value)
        self.ui.btnHeaterBB_graph_x_max.clicked.connect(self.heaterBBgraph.set_threshold_top)
        self.ui.btnHeaterBB_graph_x_min.clicked.connect(self.heaterBBgraph.set_threshold_bottom)
        self.ui.btnHeaterBB_graph_u_max.clicked.connect(self.heaterBBgraph.set_u_max)
        self.ui.btnHeaterBB_graph_u_min.clicked.connect(self.heaterBBgraph.set_u_min)
        self.ui.btnHeaterBB_graph_y_1.clicked.connect(self.heaterBBgraph.set_y_1)
        self.ui.btnHeaterBB_graph_y_2.clicked.connect(self.heaterBBgraph.set_y_2)
        self.ui.btnHeaterBB_graph_mode.clicked.connect(self.heaterBBgraph.set_mode)
        # Heater PID Graph buttons
        self.ui.btnHeaterPID_graph_x.clicked.connect(self.heaterPIDgraph.set_value)
        self.ui.btnHeaterPID_graph_e.clicked.connect(self.heaterPIDgraph.set_e)
        self.ui.btnHeaterPID_graph_int_e.clicked.connect(self.heaterPIDgraph.set_int_e)
        self.ui.btnHeaterPID_graph_aw_int_e.clicked.connect(self.heaterPIDgraph.set_aw_int_e)
        self.ui.btnHeaterPID_graph_k_p.clicked.connect(self.heaterPIDgraph.set_k_p)
        self.ui.btnHeaterPID_graph_k_i.clicked.connect(self.heaterPIDgraph.set_k_i)
        self.ui.btnHeaterPID_graph_k_d.clicked.connect(self.heaterPIDgraph.set_k_d)
        self.ui.btnHeaterPID_graph_k_aw.clicked.connect(self.heaterPIDgraph.set_k_aw)
        self.ui.btnHeaterPID_graph_u.clicked.connect(self.heaterPIDgraph.set_u)
        self.ui.btnHeaterPID_graph_u_sat.clicked.connect(self.heaterPIDgraph.set_u_sat)
        self.ui.btnHeaterPID_graph_u_p.clicked.connect(self.heaterPIDgraph.set_u_p)
        self.ui.btnHeaterPID_graph_u_i.clicked.connect(self.heaterPIDgraph.set_u_i)
        self.ui.btnHeaterPID_graph_u_d.clicked.connect(self.heaterPIDgraph.set_u_d)
        self.ui.btnHeaterPID_graph_u_max.clicked.connect(self.heaterPIDgraph.set_u_max)
        self.ui.btnHeaterPID_graph_u_max.clicked.connect(self.heaterPIDgraph.set_u_min)
        self.ui.btnHeaterPID_graph_y_1.clicked.connect(self.heaterPIDgraph.set_y_1)
        self.ui.btnHeaterPID_graph_y_2.clicked.connect(self.heaterPIDgraph.set_y_2)
        self.ui.btnHeaterPID_graph_mode.clicked.connect(self.heaterPIDgraph.set_mode)

        if is_connected():
            self.ui.fanEquation.addWidget(self.fanPIDequationwebView)
            self.ui.heaterEquation.addWidget(self.heaterPIDequationwebView)


        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.tim_1000ms_IRS)
        self.timer.start()

    def tim_1000ms_IRS(self):
        current_window = self.ui.stackGraphs.currentIndex()
        if current_window == INDICES["heater_bb"]:
            self.heaterBBgraph.update_graph()
        elif current_window == INDICES["heater_pid"]:
            self.heaterPIDgraph.update_graph()
        elif current_window == INDICES["fan_bb"]:
            self.fanBBgraph.update_graph()
        elif current_window == INDICES["fan_pid"]:
            self.fanPIDgraph.update_graph()
        
        



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())

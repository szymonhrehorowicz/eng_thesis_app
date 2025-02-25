from email.mime import application
import sys
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QAbstractSpinBox
from PySide6.QtWebEngineWidgets import QWebEngineView
from ui_form import QSize, Ui_MainWindow
from PySide6.QtCore import QTimer, QTranslator
from PySide6 import QtWidgets
###
from check_connection import is_connected
from MathEquation import MathEquation
from MainMenuHandler import MainMenuHandler, INDICES
from controls.FanControlsHandler import FanControlsHandler
from controls.HeaterControlsHandler import HeaterControlsHandler
from controls.BB import BB
from controls.PID import PID
from Serial import Serial
from COM import COM
from controls.HeaterController import HeaterController
from controls.FanController import FanController
from graphs.FanBBGraph import FanBBGraph
from graphs.FanPIDGraph import FanPIDGraph
from graphs.HeaterBBGraph import HeaterBBGraph
from graphs.HeaterPIDGraph import HeaterPIDGraph
from Export import Export
from Import import Import
from graphs.GraphsPage import GraphsPage

import rc_resources

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.app_translator = QTranslator(self)
        self.current_language = "pl"
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.fanPIDequationwebView = QWebEngineView()
        self.heaterPIDequationwebView = QWebEngineView()
        self.fanPIDequation = MathEquation(self.fanPIDequationwebView)
        self.heaterPIDequation = MathEquation(self.heaterPIDequationwebView)
        self.ui.frHeaterTi.hide()
        self.ui.frHeaterTd.hide()
        self.ui.frHeaterKi.show()
        self.ui.frHeaterKd.show()
        self.ui.frFanTi.hide()
        self.ui.frFanTd.hide()
        self.ui.frFanKi.show()
        self.ui.frFanKd.show()
        self.mainMenuHandler = MainMenuHandler(self)
        self.ui.btnLanguage.clicked.connect(self.change_language)

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
        self.isSerialConnected = False
        # Graphs
        self.graphsPage = GraphsPage(self)
        self.fanBBgraph = FanBBGraph(self, self.ui.layFanBBGraph)
        self.fanPIDgraph = FanPIDGraph(self, self.ui.layFanPIDGraph)
        self.heaterBBgraph = HeaterBBGraph(self, self.ui.layHeaterBBGraph)
        self.heaterPIDgraph = HeaterPIDGraph(self, self.ui.layHeaterPIDGraph)
        self.areGraphsRunning = False
        # Export
        self.export = Export(self)
        self.importer = Import(self)

        # DEFAULT LOCATION
        self.ui.btnHeaterControls.setEnabled(False)
        self.ui.btnFanControls.setEnabled(False)
        self.mainMenuHandler.open_help()

        # Connect button
        self.ui.btnConnect.clicked.connect(self.serial.slot_btnConnect)

        # Equation buttons
        self.ui.btnEquationTypeFan.clicked.connect(self.fanControlsHandler.change_equation_type)
        self.ui.btnEquationTypeHeater.clicked.connect(self.heaterControlsHandler.change_equation_type)
        
        # Main menu buttons
        self.ui.btnHeaterControls.clicked.connect(self.mainMenuHandler.open_heater)
        self.ui.btnFanControls.clicked.connect(self.mainMenuHandler.open_fan)
        self.ui.btnDataExport.clicked.connect(self.mainMenuHandler.open_export)
        self.ui.btnHelp.clicked.connect(self.mainMenuHandler.open_help)
        self.ui.btnImport.clicked.connect(self.mainMenuHandler.open_import)
        self.ui.btnGraphs.clicked.connect(self.mainMenuHandler.open_graphs)
        self.ui.btnGraphs.setEnabled(False)
        # Heater controller select buttons
        self.ui.btnHeaterControllerSetBB.clicked.connect(self.mainMenuHandler.set_heater_bb)
        self.ui.btnHeaterControllerSetPID.clicked.connect(self.mainMenuHandler.set_heater_pid)
        self.ui.btnHeaterControllerSetNone.clicked.connect(self.mainMenuHandler.set_heater_none)
        self.ui.btnHeaterControllerSetHighPower.clicked.connect(self.mainMenuHandler.set_heater_high_power)
        self.ui.btnHeaterControllerSetLowPower.clicked.connect(self.mainMenuHandler.set_heater_low_power)
        self.ui.btnHeaterControllerSetRightCoil.clicked.connect(self.mainMenuHandler.set_heater_right_coil)
        self.ui.btnHeaterControllerSetLeftCoil.clicked.connect(self.mainMenuHandler.set_heater_left_coil)
        # Fan controller select buttons
        self.ui.btnFanControllerSetBB.clicked.connect(self.mainMenuHandler.set_fan_bb)
        self.ui.btnFanControllerSetPID.clicked.connect(self.mainMenuHandler.set_fan_pid)
        self.ui.btnFanControllerSetNone.clicked.connect(self.mainMenuHandler.set_fan_none)

        self.ui.inHeaterSetValue.editingFinished.connect(self.heaterControlsHandler.set_value)
        self.ui.inHeaterSetValue.setButtonSymbols(QAbstractSpinBox.NoButtons)
        #Heater BB inputs
        self.ui.inHeaterBBHysteresis.editingFinished.connect(self.heaterControlsHandler.bb_setHysteresis)
        self.ui.inHeaterBBPower.valueChanged.connect(self.heaterControlsHandler.bb_setPower)
        self.ui.inHeaterBBHysteresis.setButtonSymbols(QAbstractSpinBox.NoButtons)
        # Heater PID inputs
        self.ui.inHeaterPID_Kp.editingFinished.connect(self.heaterControlsHandler.pid_setKp)
        self.ui.inHeaterPID_Ki.editingFinished.connect(self.heaterControlsHandler.pid_setKi)
        self.ui.inHeaterPID_Kd.editingFinished.connect(self.heaterControlsHandler.pid_setKd)
        self.ui.inHeaterPID_Kaw.editingFinished.connect(self.heaterControlsHandler.pid_setKaw)
        self.ui.inHeaterPID_Ti.editingFinished.connect(self.heaterControlsHandler.pid_setTi)
        self.ui.inHeaterPID_Td.editingFinished.connect(self.heaterControlsHandler.pid_setTd)
        self.ui.inHeaterPID_Kp.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.ui.inHeaterPID_Ki.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.ui.inHeaterPID_Kd.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.ui.inHeaterPID_Kaw.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.ui.inHeaterPID_Ti.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.ui.inHeaterPID_Td.setButtonSymbols(QAbstractSpinBox.NoButtons)
        # Heater PID ref inputs
        self.ui.btnHeaterRefStep.clicked.connect(self.heaterControlsHandler.setRefStep)
        self.ui.btnHeaterRefRamp.clicked.connect(self.heaterControlsHandler.setRefRamp)
        self.ui.btnHeaterRefSinewave.clicked.connect(self.heaterControlsHandler.setRefSinewave)
        self.ui.frHeaterRefSlope.setVisible(False)
        self.ui.frHeaterRefAmplitude.setVisible(False)
        self.ui.frHeaterRefOmega.setVisible(False)

        self.ui.inFanSetValue.editingFinished.connect(self.fanControlsHandler.set_value)
        self.ui.inFanSetValue.setButtonSymbols(QAbstractSpinBox.NoButtons)
        # Fan BB inputs
        self.ui.inFanBBHysteresis.editingFinished.connect(self.fanControlsHandler.bb_setHysteresis)
        self.ui.inFanBBHysteresis.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.ui.inFanPWM.valueChanged.connect(self.fanControlsHandler.pwm)
        self.ui.frFanPWM.setVisible(False)
        # Fan PID inputs
        self.ui.inFanPID_Kp.editingFinished.connect(self.fanControlsHandler.pid_setKp)
        self.ui.inFanPID_Ki.editingFinished.connect(self.fanControlsHandler.pid_setKi)
        self.ui.inFanPID_Kd.editingFinished.connect(self.fanControlsHandler.pid_setKd)
        self.ui.inFanPID_Kaw.editingFinished.connect(self.fanControlsHandler.pid_setKaw)
        self.ui.inFanPID_Ti.editingFinished.connect(self.fanControlsHandler.pid_setTi)
        self.ui.inFanPID_Td.editingFinished.connect(self.fanControlsHandler.pid_setTd)
        self.ui.inFanPID_Kp.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.ui.inFanPID_Ki.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.ui.inFanPID_Kd.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.ui.inFanPID_Kaw.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.ui.inFanPID_Ti.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.ui.inFanPID_Td.setButtonSymbols(QAbstractSpinBox.NoButtons)
        # Fan PID ref inputs
        self.ui.btnFanRefStep.clicked.connect(self.fanControlsHandler.setRefStep)
        self.ui.btnFanRefRamp.clicked.connect(self.fanControlsHandler.setRefRamp)
        self.ui.btnFanRefSinewave.clicked.connect(self.fanControlsHandler.setRefSinewave)
        self.ui.frFanRefSlope.setVisible(False)
        self.ui.frFanRefAmplitude.setVisible(False)
        self.ui.frFanRefOmega.setVisible(False)

        # Fan BB Graph buttons
        self.ui.btnFanBB_graph_x.clicked.connect(self.fanBBgraph.set_value)
        self.ui.btnFanBB_graph_x_max.clicked.connect(self.fanBBgraph.set_threshold_top)
        self.ui.btnFanBB_graph_x_min.clicked.connect(self.fanBBgraph.set_threshold_bottom)
        self.ui.btnFanBB_graph_u_max.clicked.connect(self.fanBBgraph.set_u_max)
        self.ui.btnFanBB_graph_u_min.clicked.connect(self.fanBBgraph.set_u_min)
        self.ui.btnFanBB_graph_y.clicked.connect(self.fanBBgraph.set_y)
        self.ui.btnFanBB_graph_mode.clicked.connect(self.fanBBgraph.set_mode)
        self.ui.btnFanBB_graph_e.clicked.connect(self.fanBBgraph.set_e)
        self.ui.btnFanBB_graph_u.clicked.connect(self.fanBBgraph.set_u)
        # Fan PID Graph buttons
        self.ui.btnFanPID_graph_x.clicked.connect(self.fanPIDgraph.set_value)
        self.ui.btnFanPID_graph_e.clicked.connect(self.fanPIDgraph.set_e)
        self.ui.btnFanPID_graph_int_e.clicked.connect(self.fanPIDgraph.set_int_e)
        self.ui.btnFanPID_graph_aw_int_e.clicked.connect(self.fanPIDgraph.set_aw_int_e)
        self.ui.btnFanPID_graph_u.clicked.connect(self.fanPIDgraph.set_u)
        self.ui.btnFanPID_graph_u_sat.clicked.connect(self.fanPIDgraph.set_u_sat)
        self.ui.btnFanPID_graph_u_p.clicked.connect(self.fanPIDgraph.set_u_p)
        self.ui.btnFanPID_graph_u_i.clicked.connect(self.fanPIDgraph.set_u_i)
        self.ui.btnFanPID_graph_u_d.clicked.connect(self.fanPIDgraph.set_u_d)
        self.ui.btnFanPID_graph_u_max.clicked.connect(self.fanPIDgraph.set_u_max)
        self.ui.btnFanPID_graph_u_min.clicked.connect(self.fanPIDgraph.set_u_min)
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
        self.ui.btnHeaterBB_graph_e.clicked.connect(self.heaterBBgraph.set_e)
        self.ui.btnHeaterBB_graph_u.clicked.connect(self.heaterBBgraph.set_u)
        # Heater PID Graph buttons
        self.ui.btnHeaterPID_graph_x.clicked.connect(self.heaterPIDgraph.set_value)
        self.ui.btnHeaterPID_graph_e.clicked.connect(self.heaterPIDgraph.set_e)
        self.ui.btnHeaterPID_graph_int_e.clicked.connect(self.heaterPIDgraph.set_int_e)
        self.ui.btnHeaterPID_graph_aw_int_e.clicked.connect(self.heaterPIDgraph.set_aw_int_e)
        self.ui.btnHeaterPID_graph_u.clicked.connect(self.heaterPIDgraph.set_u)
        self.ui.btnHeaterPID_graph_u_sat.clicked.connect(self.heaterPIDgraph.set_u_sat)
        self.ui.btnHeaterPID_graph_u_p.clicked.connect(self.heaterPIDgraph.set_u_p)
        self.ui.btnHeaterPID_graph_u_i.clicked.connect(self.heaterPIDgraph.set_u_i)
        self.ui.btnHeaterPID_graph_u_d.clicked.connect(self.heaterPIDgraph.set_u_d)
        self.ui.btnHeaterPID_graph_u_max.clicked.connect(self.heaterPIDgraph.set_u_max)
        self.ui.btnHeaterPID_graph_u_min.clicked.connect(self.heaterPIDgraph.set_u_min)
        self.ui.btnHeaterPID_graph_y_1.clicked.connect(self.heaterPIDgraph.set_y_1)
        self.ui.btnHeaterPID_graph_y_2.clicked.connect(self.heaterPIDgraph.set_y_2)
        self.ui.btnHeaterPID_graph_mode.clicked.connect(self.heaterPIDgraph.set_mode)

        # Help buttons
        self.ui.btnBBFanHelp.clicked.connect(self.mainMenuHandler.bb_help)
        self.ui.btnBBHeaterHelp.clicked.connect(self.mainMenuHandler.bb_help)

        # Start/Stop buttons
        self.ui.btnHeaterStart.clicked.connect(self.COM.set_heater_config)
        self.ui.btnFanStart.clicked.connect(self.COM.set_fan_config)

        # Graph controls
        self.ui.btn_graph_Stop.clicked.connect(self.mainMenuHandler.stop_graphs)
        self.ui.btn_graph_Clear.clicked.connect(self.mainMenuHandler.clear_graphs)
        self.ui.btn_graph_Stop.setEnabled(False)
        self.ui.btn_graph_Stop.setIcon(self.mainMenuHandler.playIcon)
        self.ui.btn_graph_Clear.setEnabled(False)

        # Export controls
            # Export button
        self.ui.btnExportAction.clicked.connect(self.export.export)
            # Main controls
        self.ui.chxExHeaterNone.clicked.connect(self.export.set_heater_none)
        self.ui.chxExHeaterBB.clicked.connect(self.export.set_heater_bb)
        self.ui.chxExHeaterPID.clicked.connect(self.export.set_heater_pid)
        self.ui.chxExFanNone.clicked.connect(self.export.set_fan_none)
        self.ui.chxExFanBB.clicked.connect(self.export.set_fan_bb)
        self.ui.chxExFanPID.clicked.connect(self.export.set_fan_pid)
            # Heater None
        self.ui.chxExHeaterNone_y_1.clicked.connect(self.export.set_heater_none_y_1)
        self.ui.chxExHeaterNone_y_2.clicked.connect(self.export.set_heater_none_y_2)
        self.ui.chxExHeaterNone_u_max.clicked.connect(self.export.set_heater_none_u_max)
        self.ui.chxExHeaterNone_u_min.clicked.connect(self.export.set_heater_none_u_min)
            # Heater BB
        self.ui.chxExHeaterBB_x.clicked.connect(self.export.set_heater_bb_x)
        self.ui.chxExHeaterBB_x_max.clicked.connect(self.export.set_heater_bb_x_max)
        self.ui.chxExHeaterBB_x_min.clicked.connect(self.export.set_heater_bb_x_min)
        self.ui.chxExHeaterBB_u_max.clicked.connect(self.export.set_heater_bb_u_max)
        self.ui.chxExHeaterBB_u_min.clicked.connect(self.export.set_heater_bb_u_min)
        self.ui.chxExHeaterBB_y_1.clicked.connect(self.export.set_heater_bb_y_1)
        self.ui.chxExHeaterBB_y_2.clicked.connect(self.export.set_heater_bb_y_2)
        self.ui.chxExHeaterBB_mode.clicked.connect(self.export.set_heater_bb_mode)
            # Heater PID
        self.ui.chxExHeaterPID_x.clicked.connect(self.export.set_heater_pid_x)
        self.ui.chxExHeaterPID_e.clicked.connect(self.export.set_heater_pid_e)
        self.ui.chxExHeaterPID_int_e.clicked.connect(self.export.set_heater_pid_int_e)
        self.ui.chxExHeaterPID_aw_int_e.clicked.connect(self.export.set_heater_pid_aw_int_e)
        self.ui.chxExHeaterPID_k_p.clicked.connect(self.export.set_heater_pid_k_p)
        self.ui.chxExHeaterPID_k_i.clicked.connect(self.export.set_heater_pid_k_i)
        self.ui.chxExHeaterPID_k_d.clicked.connect(self.export.set_heater_pid_k_d)
        self.ui.chxExHeaterPID_k_aw.clicked.connect(self.export.set_heater_pid_k_aw)
        self.ui.chxExHeaterPID_u.clicked.connect(self.export.set_heater_pid_u)
        self.ui.chxExHeaterPID_u_sat.clicked.connect(self.export.set_heater_pid_u_sat)
        self.ui.chxExHeaterPID_u_p.clicked.connect(self.export.set_heater_pid_u_p)
        self.ui.chxExHeaterPID_u_i.clicked.connect(self.export.set_heater_pid_u_i)
        self.ui.chxExHeaterPID_u_d.clicked.connect(self.export.set_heater_pid_u_d)
        self.ui.chxExHeaterPID_u_max.clicked.connect(self.export.set_heater_pid_u_max)
        self.ui.chxExHeaterPID_u_min.clicked.connect(self.export.set_heater_pid_u_min)
        self.ui.chxExHeaterPID_y_1.clicked.connect(self.export.set_heater_pid_y_1)
        self.ui.chxExHeaterPID_y_2.clicked.connect(self.export.set_heater_pid_y_2)
        self.ui.chxExHeaterPID_mode.clicked.connect(self.export.set_heater_pid_mode)
            # Fan None
        self.ui.chxExFanNone_y.clicked.connect(self.export.set_fan_none_y)
        self.ui.chxExFanNone_u_max.clicked.connect(self.export.set_fan_none_u_max)
        self.ui.chxExFanNone_u_min.clicked.connect(self.export.set_fan_none_u_min)
            # Fan BB
        self.ui.chxExFanBB_x.clicked.connect(self.export.set_fan_bb_x)
        self.ui.chxExFanBB_x_max.clicked.connect(self.export.set_fan_bb_x_max)
        self.ui.chxExFanBB_x_min.clicked.connect(self.export.set_fan_bb_x_min)
        self.ui.chxExFanBB_u_max.clicked.connect(self.export.set_fan_bb_u_max)
        self.ui.chxExFanBB_u_min.clicked.connect(self.export.set_fan_bb_u_min)
        self.ui.chxExFanBB_y.clicked.connect(self.export.set_fan_bb_y)
        self.ui.chxExFanBB_mode.clicked.connect(self.export.set_fan_bb_mode)
            # Fan PID
        self.ui.chxExFanPID_x.clicked.connect(self.export.set_fan_pid_x)
        self.ui.chxExFanPID_e.clicked.connect(self.export.set_fan_pid_e)
        self.ui.chxExFanPID_int_e.clicked.connect(self.export.set_fan_pid_int_e)
        self.ui.chxExFanPID_aw_int_e.clicked.connect(self.export.set_fan_pid_aw_int_e)
        self.ui.chxExFanPID_k_p.clicked.connect(self.export.set_fan_pid_k_p)
        self.ui.chxExFanPID_k_i.clicked.connect(self.export.set_fan_pid_k_i)
        self.ui.chxExFanPID_k_d.clicked.connect(self.export.set_fan_pid_k_d)
        self.ui.chxExFanPID_k_aw.clicked.connect(self.export.set_fan_pid_k_aw)
        self.ui.chxExFanPID_u.clicked.connect(self.export.set_fan_pid_u)
        self.ui.chxExFanPID_u_sat.clicked.connect(self.export.set_fan_pid_u_sat)
        self.ui.chxExFanPID_u_p.clicked.connect(self.export.set_fan_pid_u_p)
        self.ui.chxExFanPID_u_i.clicked.connect(self.export.set_fan_pid_u_i)
        self.ui.chxExFanPID_u_d.clicked.connect(self.export.set_fan_pid_u_d)
        self.ui.chxExFanPID_u_max.clicked.connect(self.export.set_fan_pid_u_max)
        self.ui.chxExFanPID_u_min.clicked.connect(self.export.set_fan_pid_u_min)
        self.ui.chxExFanPID_y.clicked.connect(self.export.set_fan_pid_y)
        self.ui.chxExFanPID_mode.clicked.connect(self.export.set_fan_pid_mode)

        # Graphs page
        self.ui.btnGraphsPageHeater.clicked.connect(self.graphsPage.open_heater)
        self.ui.btnGraphsPageFan.clicked.connect(self.graphsPage.open_fan)

        self.ui.btnGraphsPage_y.setVisible(False)
        self.ui.btnGraphsPage_x.clicked.connect(self.graphsPage.set_x)
        self.ui.btnGraphPage_e.clicked.connect(self.graphsPage.set_e)
        self.ui.btnGraphsPage_y.clicked.connect(self.graphsPage.set_y)
        self.ui.btnGraphsPage_y_1.clicked.connect(self.graphsPage.set_y_1)
        self.ui.btnGraphsPage_y_2.clicked.connect(self.graphsPage.set_y_2)
        self.ui.btnGraphsPage_u_sat.clicked.connect(self.graphsPage.set_u_sat)
        self.ui.btnGraphsPage_u.clicked.connect(self.graphsPage.set_u)
        self.ui.btnGraphsPage_u_p.clicked.connect(self.graphsPage.set_u_p)
        self.ui.btnGraphsPage_u_i.clicked.connect(self.graphsPage.set_u_i)
        self.ui.btnGraphsPage_u_d.clicked.connect(self.graphsPage.set_u_d)

        # Import
        self.ui.btnImportLoad.clicked.connect(self.importer.load_file)
        self.ui.btnImportAction.clicked.connect(self.importer.import_data)

        if is_connected():
            self.ui.fanEquation.addWidget(self.fanPIDequationwebView)
            self.ui.heaterEquation.addWidget(self.heaterPIDequationwebView)

        # Timers
        self.timer100ms = QTimer()
        self.timer100ms.setInterval(100)
        self.timer100ms.timeout.connect(self.tim_100ms_IRS)
        self.timer100ms.start()

        self.timer1s = QTimer()
        self.timer1s.setInterval(1000)
        self.timer1s.timeout.connect(self.tim_1s_IRS)
        self.timer1s.start()

        self.fanBBgraph.update_graph()
        self.fanPIDgraph.update_graph()
        self.heaterBBgraph.update_graph()
        self.heaterPIDgraph.update_graph()
        self.graphsPage.update()

    def tim_100ms_IRS(self):
        current_main_window = self.ui.container.currentIndex()
        if current_main_window == INDICES["controls"]:
            current_window = self.ui.stackGraphs.currentIndex()
            if (current_window == INDICES["heater_bb"]) and self.areGraphsRunning:
                self.heaterBBgraph.update_graph()
            elif (current_window == INDICES["heater_pid"]) and self.areGraphsRunning:
                self.heaterPIDgraph.update_graph()
            elif (current_window == INDICES["fan_bb"]) and self.areGraphsRunning:
                self.fanBBgraph.update_graph()
            elif (current_window == INDICES["fan_pid"]) and self.areGraphsRunning:
                self.fanPIDgraph.update_graph()

    def tim_1s_IRS(self):
        if self.isSerialConnected:
            self.serial.send_ack()
    
    def change_language(self):
        lang = "en" if self.current_language == "pl" else "pl"
        
        QApplication.instance().removeTranslator(self.app_translator)
        if self.app_translator.load(f"{lang}.qm", ":/translations"):
            QApplication.instance().installTranslator(self.app_translator)

        self.ui.retranslateUi(self)

        langIcon = QIcon()
        langIcon.addFile(f":/assets/assets/{lang}.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ui.btnLanguage.setIcon(langIcon)

        self.current_language = lang


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())

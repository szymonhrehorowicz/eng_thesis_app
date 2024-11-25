# This Python file uses the following encoding: utf-8
from PySide6.QtCore import Slot, QSize
from PySide6.QtGui import QIcon
import rc_resources

INDICES = {
    "controls": 0,
    "heater": 0,
    "fan": 1,
    "export": 1,
    "help": 2,
    "heater_bb": 0,
    "heater_pid": 1,
    "fan_bb": 2,
    "fan_pid": 3,
}

class MainMenuHandler:
    def __init__(self, handler):
        self.handler = handler
        self.playIcon = QIcon()
        self.pauseIcon = QIcon()
        self.playIcon.addFile(u":/assets/assets/play.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pauseIcon.addFile(u":/assets/assets/pause.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

    # MAIN MENU
    @Slot()
    def open_heater(self):
        self.handler.ui.btnHeaterControls.setChecked(True)
        self.handler.ui.btnFanControls.setChecked(False)
        self.handler.ui.btnDataExport.setChecked(False)
        self.handler.ui.btnHelp.setChecked(False)

        self.handler.ui.container.setCurrentIndex(INDICES["controls"])
        self.handler.ui.stackControllerDesc.setCurrentIndex(INDICES["heater"])
        self.handler.ui.stackControllerSelect.setCurrentIndex(INDICES["heater"])
        self.handler.ui.stackGraphs.setCurrentIndex(INDICES["heater"])
        if self.handler.ui.btnHeaterControllerSetBB.isChecked():
            self.handler.ui.stackController.setCurrentIndex(INDICES["heater_bb"])
            self.handler.ui.stackGraphs.setCurrentIndex(INDICES["heater_bb"])
        else:
            self.handler.ui.stackController.setCurrentIndex(INDICES["heater_pid"])
            self.handler.ui.stackGraphs.setCurrentIndex(INDICES["heater_pid"])

    @Slot()
    def open_fan(self):
        self.handler.ui.btnHeaterControls.setChecked(False)
        self.handler.ui.btnFanControls.setChecked(True)
        self.handler.ui.btnDataExport.setChecked(False)
        self.handler.ui.btnHelp.setChecked(False)

        self.handler.ui.container.setCurrentIndex(INDICES["controls"])
        self.handler.ui.stackControllerDesc.setCurrentIndex(INDICES["fan"])
        self.handler.ui.stackControllerSelect.setCurrentIndex(INDICES["fan"])
        self.handler.ui.stackGraphs.setCurrentIndex(INDICES["fan"])
        if self.handler.ui.btnFanControllerSetBB.isChecked():
            self.handler.ui.stackController.setCurrentIndex(INDICES["fan_bb"])
            self.handler.ui.stackGraphs.setCurrentIndex(INDICES["fan_bb"])
        else:
            self.handler.ui.stackController.setCurrentIndex(INDICES["fan_pid"])
            self.handler.ui.stackGraphs.setCurrentIndex(INDICES["fan_pid"])

    @Slot()
    def open_export(self):
        self.handler.ui.btnHeaterControls.setChecked(False)
        self.handler.ui.btnFanControls.setChecked(False)
        self.handler.ui.btnDataExport.setChecked(True)
        self.handler.ui.btnHelp.setChecked(False)

        self.handler.ui.container.setCurrentIndex(INDICES["export"])

    @Slot()
    def open_help(self):
        self.handler.ui.btnHeaterControls.setChecked(False)
        self.handler.ui.btnFanControls.setChecked(False)
        self.handler.ui.btnDataExport.setChecked(False)
        self.handler.ui.btnHelp.setChecked(True)
        self.handler.ui.container.setCurrentIndex(INDICES["help"])

    # HEATER
    @Slot()
    def set_heater_bb(self):
        self.handler.ui.btnHeaterControllerSetBB.setChecked(True)
        self.handler.ui.btnHeaterControllerSetPID.setChecked(False)
        self.handler.ui.stackController.setCurrentIndex(INDICES["heater_bb"])
        self.handler.ui.stackGraphs.setCurrentIndex(INDICES["heater_bb"])

    @Slot()
    def set_heater_pid(self):
        self.handler.ui.btnHeaterControllerSetPID.setChecked(True)
        self.handler.ui.btnHeaterControllerSetBB.setChecked(False)
        self.handler.ui.stackController.setCurrentIndex(INDICES["heater_pid"])
        self.handler.ui.stackGraphs.setCurrentIndex(INDICES["heater_pid"])
    
    @Slot()
    def set_heater_high_power(self):
        R17POWER = 9
        self.handler.ui.btnHeaterControllerSetHighPower.setChecked(True)
        self.handler.ui.btnHeaterControllerSetLowPower.setChecked(False)
        power = str(self.handler.ui.inHeaterBBPower.value() / 100 * R17POWER)
        self.handler.ui.lblPower.setText(power[:power.index('.') + 2])

    @Slot()
    def set_heater_low_power(self):
        R33POWER = 4.5
        self.handler.ui.btnHeaterControllerSetHighPower.setChecked(False)
        self.handler.ui.btnHeaterControllerSetLowPower.setChecked(True)
        power = str(self.handler.ui.inHeaterBBPower.value() / 100 * R33POWER)
        self.handler.ui.lblPower.setText(power[:power.index('.') + 2])

    @Slot()
    def set_heater_right_coil(self):
        self.handler.ui.btnHeaterControllerSetRightCoil.setChecked(True)
        self.handler.ui.btnHeaterControllerSetLeftCoil.setChecked(False)

    @Slot()
    def set_heater_left_coil(self):
        self.handler.ui.btnHeaterControllerSetRightCoil.setChecked(False)
        self.handler.ui.btnHeaterControllerSetLeftCoil.setChecked(True)

    # FAN
    @Slot()
    def set_fan_bb(self):
        self.handler.ui.btnFanControllerSetBB.setChecked(True)
        self.handler.ui.btnFanControllerSetPID.setChecked(False)
        self.handler.ui.stackController.setCurrentIndex(INDICES["fan_bb"])
        self.handler.ui.stackGraphs.setCurrentIndex(INDICES["fan_bb"])

    @Slot()
    def set_fan_pid(self):
        self.handler.ui.btnFanControllerSetPID.setChecked(True)
        self.handler.ui.btnFanControllerSetBB.setChecked(False)
        self.handler.ui.stackController.setCurrentIndex(INDICES["fan_pid"])
        self.handler.ui.stackGraphs.setCurrentIndex(INDICES["fan_pid"])

    @Slot(bool)
    def stop_fan_bb_graph(self, state):
        self.handler.ui.btnFanBB_graph_Stop.setIcon(self.playIcon if state else self.pauseIcon)
        self.handler.isFanBB_graph_running = not state

    @Slot(bool)
    def stop_fan_pid_graph(self, state):
        self.handler.ui.btnFanPID_graph_Stop.setIcon(self.playIcon if state else self.pauseIcon)
        self.handler.isFanPID_graph_running = not state

    @Slot(bool)
    def stop_heater_bb_graph(self, state):
        self.handler.ui.btnHeaterBB_graph_Stop.setIcon(self.playIcon if state else self.pauseIcon)
        self.handler.isHeaterBB_graph_running = not state

    @Slot(bool)
    def stop_heater_pid_graph(self, state):
        self.handler.ui.btnHeaterPID_graph_Stop.setIcon(self.playIcon if state else self.pauseIcon)
        self.handler.isHeaterPID_graph_running = not state

    @Slot()
    def clear_fan_bb_graph(self):
        self.handler.fanController.clear_bb()
        self.handler.fanBBgraph.update_graph()

    @Slot()
    def clear_fan_pid_graph(self):
        self.handler.fanController.clear_pid()
        self.handler.fanPIDgraph.update_graph()

    @Slot()
    def clear_heater_bb_graph(self):
        self.handler.heaterController.clear_bb()
        self.handler.heaterBBgraph.update_graph()

    @Slot()
    def clear_heater_pid_graph(self):
        self.handler.heaterController.clear_pid()
        self.handler.heaterPIDgraph.update_graph()

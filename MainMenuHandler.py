# This Python file uses the following encoding: utf-8
from PySide6.QtCore import Slot, QSize
from PySide6.QtGui import QIcon
from utilities import info_dialog

import rc_resources

INDICES = {
    "controls": 0,
    "heater": 0,
    "fan": 1,
    "export": 1,
    "import": 3,
    "graphs": 4,
    "help": 2,
    "heater_bb": 0,
    "heater_pid": 1,
    "fan_bb": 2,
    "fan_pid": 3,
    "graphs_heater": 0,
    "graphs_fan": 1,
}

class MainMenuHandler:
    def __init__(self, handler):
        self.handler = handler
        self.playIcon = QIcon()
        self.pauseIcon = QIcon()
        self.playIcon.addFile(u":/assets/assets/play.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pauseIcon.addFile(u":/assets/assets/pause.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.previous_page = INDICES["help"]

    # MAIN MENU
    @Slot()
    def open_heater(self):
        self.handler.ui.btnHeaterControls.setChecked(True)
        self.handler.ui.btnFanControls.setChecked(False)
        self.handler.ui.btnDataExport.setChecked(False)
        self.handler.ui.btnHelp.setChecked(False)
        self.handler.ui.btnImport.setChecked(False)
        self.handler.ui.btnGraphs.setChecked(False)

        if self.handler.ui.btnHeaterControllerSetNone.isChecked():
            self.handler.ui.stackController.setVisible(False)
            self.handler.ui.frHeaterConfig.setVisible(False)
        else:
            self.handler.ui.stackController.setVisible(True)
            self.handler.ui.frHeaterConfig.setVisible(True)

        self.handler.ui.container.setCurrentIndex(INDICES["controls"])
        self.handler.ui.stackControllerDesc.setCurrentIndex(INDICES["heater"])
        self.handler.ui.stackControllerSelect.setCurrentIndex(INDICES["heater"])
        self.handler.ui.stackGraphs.setCurrentIndex(INDICES["heater"])
        if self.handler.ui.btnHeaterControllerSetBB.isChecked() or self.handler.ui.btnHeaterControllerSetNone.isChecked():
            self.handler.ui.stackController.setCurrentIndex(INDICES["heater_bb"])
            self.handler.ui.stackGraphs.setCurrentIndex(INDICES["heater_bb"])
            self.handler.heaterBBgraph.update_graph()
        else:
            self.handler.ui.stackController.setCurrentIndex(INDICES["heater_pid"])
            self.handler.ui.stackGraphs.setCurrentIndex(INDICES["heater_pid"])
            self.handler.heaterPIDgraph.update_graph()

    @Slot()
    def open_fan(self):
        self.handler.ui.btnHeaterControls.setChecked(False)
        self.handler.ui.btnFanControls.setChecked(True)
        self.handler.ui.btnDataExport.setChecked(False)
        self.handler.ui.btnHelp.setChecked(False)
        self.handler.ui.btnImport.setChecked(False)
        self.handler.ui.btnGraphs.setChecked(False)

        if self.handler.ui.btnFanControllerSetNone.isChecked():
            self.handler.ui.stackController.setVisible(False)
            self.handler.ui.frFanConfig.setVisible(False)
        else:
            self.handler.ui.stackController.setVisible(True)
            self.handler.ui.frFanConfig.setVisible(True)

        self.handler.ui.container.setCurrentIndex(INDICES["controls"])
        self.handler.ui.stackControllerDesc.setCurrentIndex(INDICES["fan"])
        self.handler.ui.stackControllerSelect.setCurrentIndex(INDICES["fan"])
        self.handler.ui.stackGraphs.setCurrentIndex(INDICES["fan"])
        if self.handler.ui.btnFanControllerSetBB.isChecked() or self.handler.ui.btnFanControllerSetNone.isChecked():
            self.handler.ui.stackController.setCurrentIndex(INDICES["fan_bb"])
            self.handler.ui.stackGraphs.setCurrentIndex(INDICES["fan_bb"])
            self.handler.fanBBgraph.update_graph()
        else:
            self.handler.ui.stackController.setCurrentIndex(INDICES["fan_pid"])
            self.handler.ui.stackGraphs.setCurrentIndex(INDICES["fan_pid"])
            self.handler.fanPIDgraph.update_graph()

    @Slot()
    def open_export(self):
        self.handler.ui.btnHeaterControls.setChecked(False)
        self.handler.ui.btnFanControls.setChecked(False)
        self.handler.ui.btnDataExport.setChecked(True)
        self.handler.ui.btnHelp.setChecked(False)
        self.handler.ui.btnImport.setChecked(False)
        self.handler.ui.btnGraphs.setChecked(False)
        self.handler.ui.container.setCurrentIndex(INDICES["export"])

    @Slot()
    def open_help(self):
        self.handler.ui.btnHeaterControls.setChecked(False)
        self.handler.ui.btnFanControls.setChecked(False)
        self.handler.ui.btnDataExport.setChecked(False)
        self.handler.ui.btnHelp.setChecked(True)
        self.handler.ui.btnImport.setChecked(False)
        self.handler.ui.btnGraphs.setChecked(False)
        self.handler.ui.container.setCurrentIndex(INDICES["help"])

    @Slot()
    def open_import(self):
        self.handler.ui.btnHeaterControls.setChecked(False)
        self.handler.ui.btnFanControls.setChecked(False)
        self.handler.ui.btnDataExport.setChecked(False)
        self.handler.ui.btnHelp.setChecked(False)
        self.handler.ui.btnImport.setChecked(True)
        self.handler.ui.btnGraphs.setChecked(False)
        self.handler.ui.container.setCurrentIndex(INDICES["import"])
    
    @Slot()
    def open_graphs(self):
        current_idx = self.handler.ui.container.currentIndex()
        if current_idx != INDICES["graphs"]:
            self.previous_page = current_idx
        self.handler.ui.btnHeaterControls.setChecked(False)
        self.handler.ui.btnFanControls.setChecked(False)
        self.handler.ui.btnDataExport.setChecked(False)
        self.handler.ui.btnHelp.setChecked(False)
        self.handler.ui.btnImport.setChecked(False)
        self.handler.ui.btnGraphs.setChecked(True)
        self.handler.ui.container.setCurrentIndex(INDICES["graphs"])
        self.handler.graphsPage.update()
        self.handler.graphsPage.home()

    # HEATER
    @Slot()
    def set_heater_bb(self):
        self.handler.ui.btnHeaterControllerSetBB.setChecked(True)
        self.handler.ui.btnHeaterControllerSetPID.setChecked(False)
        self.handler.ui.btnHeaterControllerSetNone.setChecked(False)
        self.handler.ui.stackController.setVisible(True)
        self.handler.ui.frHeaterConfig.setVisible(True)
        self.handler.ui.stackController.setCurrentIndex(INDICES["heater_bb"])
        self.handler.ui.stackGraphs.setCurrentIndex(INDICES["heater_bb"])

    @Slot()
    def set_heater_pid(self):
        self.handler.ui.btnHeaterControllerSetPID.setChecked(True)
        self.handler.ui.btnHeaterControllerSetBB.setChecked(False)
        self.handler.ui.btnHeaterControllerSetNone.setChecked(False)
        self.handler.ui.stackController.setVisible(True)
        self.handler.ui.frHeaterConfig.setVisible(True)
        self.handler.ui.stackController.setCurrentIndex(INDICES["heater_pid"])
        self.handler.ui.stackGraphs.setCurrentIndex(INDICES["heater_pid"])
    
    @Slot()
    def set_heater_none(self):
        self.handler.ui.btnHeaterControllerSetBB.setChecked(False)
        self.handler.ui.btnHeaterControllerSetPID.setChecked(False)
        self.handler.ui.btnHeaterControllerSetNone.setChecked(True)
        self.handler.ui.stackController.setVisible(False)
        self.handler.ui.frHeaterConfig.setVisible(False)
        self.handler.ui.stackGraphs.setCurrentIndex(INDICES["heater_bb"])
    
    @Slot()
    def set_heater_high_power(self):
        self.handler.ui.btnHeaterControllerSetHighPower.setChecked(True)
        self.handler.ui.btnHeaterControllerSetLowPower.setChecked(False)

    @Slot()
    def set_heater_low_power(self):
        self.handler.ui.btnHeaterControllerSetHighPower.setChecked(False)
        self.handler.ui.btnHeaterControllerSetLowPower.setChecked(True)

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
        self.handler.ui.btnFanControllerSetNone.setChecked(False)
        self.handler.ui.stackController.setVisible(True)
        self.handler.ui.frFanConfig.setVisible(True)
        self.handler.ui.stackController.setCurrentIndex(INDICES["fan_bb"])
        self.handler.ui.stackGraphs.setCurrentIndex(INDICES["fan_bb"])
        self.handler.ui.frFanPWM.setVisible(False)

    @Slot()
    def set_fan_pid(self):
        self.handler.ui.btnFanControllerSetPID.setChecked(True)
        self.handler.ui.btnFanControllerSetBB.setChecked(False)
        self.handler.ui.btnFanControllerSetNone.setChecked(False)
        self.handler.ui.stackController.setVisible(True)
        self.handler.ui.frFanConfig.setVisible(True)
        self.handler.ui.stackController.setCurrentIndex(INDICES["fan_pid"])
        self.handler.ui.stackGraphs.setCurrentIndex(INDICES["fan_pid"])
        self.handler.ui.frFanPWM.setVisible(False)

    @Slot()
    def set_fan_none(self):
        self.handler.ui.btnFanControllerSetBB.setChecked(False)
        self.handler.ui.btnFanControllerSetPID.setChecked(False)
        self.handler.ui.btnFanControllerSetNone.setChecked(True)
        self.handler.ui.stackController.setVisible(False)
        self.handler.ui.frFanConfig.setVisible(False)
        self.handler.ui.stackController.setCurrentIndex(INDICES["fan_bb"])
        self.handler.ui.stackGraphs.setCurrentIndex(INDICES["fan_bb"])
        self.handler.ui.frFanPWM.setVisible(True)

    @Slot(bool)
    def stop_graphs(self, state):
        self.handler.graphsPage.zoom_pending = 0

        self.handler.ui.btn_graph_Stop.setIcon(self.playIcon if state else self.pauseIcon)
        self.handler.areGraphsRunning = not state
        if not state:
            self.handler.fanController.was_stopped = True
            self.handler.heaterController.was_stopped = True

        if state:
            # unlock graphs page
            self.handler.ui.btnGraphs.setEnabled(True)
        else:
            # lock graphs page
            self.handler.ui.btnGraphs.setEnabled(False)
            # move user to previouos page
            if self.handler.ui.container.currentIndex() == INDICES["graphs"]:
                if self.previous_page == INDICES["controls"]:
                    if self.handler.ui.stackControllerDesc.currentIndex() == INDICES["heater"]:
                        self.open_heater()
                    else:
                        self.open_fan()
                elif self.previous_page == INDICES["export"]:
                    self.open_export()
                elif self.previous_page == INDICES["import"]:
                    self.open_import()
                elif self.previous_page == INDICES["help"]:
                    self.open_help()
            # reset graphs size
            self.handler.fanBBgraph.home()
            self.handler.fanPIDgraph.home()
            self.handler.heaterBBgraph.home()
            self.handler.heaterPIDgraph.home()

    @Slot()
    def clear_graphs(self):
        self.handler.fanController.clear()
        self.handler.heaterController.clear()

        self.handler.fanBBgraph.update_graph()
        self.handler.fanPIDgraph.update_graph()

        self.handler.heaterBBgraph.update_graph()
        self.handler.heaterPIDgraph.update_graph()

        self.handler.graphsPage.update()

    @Slot()
    def bb_help(self):
        info_dialog(self.handler, "Opis sygnałów regulatora dwupołożeniowego", u":/assets/assets/bb.png")

# This Python file uses the following encoding: utf-8
from PySide6.QtCore import Slot, QSize
from PySide6.QtGui import QIcon
from MainMenuHandler import INDICES
from utilities import DEGREE_SIGN
from graphs.Graph import Graph
import rc_resources

class HeaterGraphY(Graph):
    def __init__(self, handler, layout, label):
        super(HeaterGraphY, self).__init__(handler, layout, label, use_toolbar=True)
        self.init_controls()
        self.keys = list(self.controls.keys())

    def init_controls(self):
        self.controller = self.handler.heaterController
        self.controls = {
            "x(t)": {
                "state": self.handler.ui.btnGraphsPageHeater_x.isChecked(),
                "color": 'indianred',
            },
            "y_1(t)": {
                "state": self.handler.ui.btnGraphsPageHeater_y_1.isChecked(),
                "color": 'hotpink',
            },
            "y_2(t)": {
                "state": self.handler.ui.btnGraphsPageHeater_y_2.isChecked(),
                "color": 'crimson',
            },
        }

    @Slot()
    def update_graph(self):
        self.plot([
            self.controller.pid_set_value,
            self.controller.pid_temp_left,
            self.controller.pid_temp_right,
        ], self.controller.pid_time)
class HeaterGraphE(Graph):
    def __init__(self, handler, layout, label):
        super(HeaterGraphE, self).__init__(handler, layout, label, use_toolbar=True)
        self.init_controls()
        self.keys = list(self.controls.keys())

    def init_controls(self):
        self.controller = self.handler.heaterController
        self.controls = {
            "e(t)": {
                "state": True,
                "color": "tomato",
            },
        }

    @Slot()
    def update_graph(self):
        self.plot([
            self.controller.pid_error,
        ], self.controller.pid_time)
class HeaterGraphU(Graph):
    def __init__(self, handler, layout, label):
        super(HeaterGraphU, self).__init__(handler, layout, label, use_toolbar=True)
        self.init_controls()
        self.keys = list(self.controls.keys())

    def init_controls(self):
        self.controller = self.handler.heaterController
        self.controls = {
            "u_sat(t)": {
                "state": self.handler.ui.btnGraphsPageHeater_u_sat.isChecked(),
                "color": "aquamarine",
            },
            "u(t)": {
                "state": self.handler.ui.btnGraphsPageHeater_u.isChecked(),
                "color": "lime",
            },
            "u_p(t)": {
                "state": self.handler.ui.btnGraphsPageHeater_u_p.isChecked(),
                "color": "darkcyan",
            },
            "u_i(t)": {
                "state": self.handler.ui.btnGraphsPageHeater_u_i.isChecked(),
                "color": "royalblue",
            },
            "u_d(t)": {
                "state": self.handler.ui.btnGraphsPageHeater_u_d.isChecked(),
                "color": "navy",
            },
        }

    @Slot()
    def update_graph(self):
        self.plot([
            self.controller.pid_u_saturated,
            self.controller.pid_u,
            self.controller.pid_u_p,
            self.controller.pid_u_i,
            self.controller.pid_u_d,
        ], self.controller.pid_time)

class FanGraphY(Graph):
    def __init__(self, handler, layout, label):
        super(FanGraphY, self).__init__(handler, layout, label, use_toolbar=True)
        self.init_controls()
        self.keys = list(self.controls.keys())

    def init_controls(self):
        self.controller = self.handler.fanController
        self.controls = {
            "x(t)": {
                "state": self.handler.ui.btnGraphsPageFan_x.isChecked(),
                "color": 'indianred',
            },
            "y(t)": {
                "state": self.handler.ui.btnGraphsPageFan_y.isChecked(),
                "color": 'hotpink',
            },
        }

    @Slot()
    def update_graph(self):
        self.plot([
            self.controller.pid_set_value,
            self.controller.pid_speed,
        ], self.controller.pid_time)
class FanGraphE(Graph):
    def __init__(self, handler, layout, label):
        super(FanGraphE, self).__init__(handler, layout, label, use_toolbar=True)
        self.init_controls()
        self.keys = list(self.controls.keys())

    def init_controls(self):
        self.controller = self.handler.fanController
        self.controls = {
            "e(t)": {
                "state": True,
                "color": "tomato",
            },
        }

    @Slot()
    def update_graph(self):
        self.plot([
            self.controller.pid_error,
        ], self.controller.pid_time)
class FanGraphU(Graph):
    def __init__(self, handler, layout, label):
        super(FanGraphU, self).__init__(handler, layout, label, use_toolbar=True)
        self.init_controls()
        self.keys = list(self.controls.keys())

    def init_controls(self):
        self.controller = self.handler.fanController
        self.controls = {
            "u_sat(t)": {
                "state": self.handler.ui.btnGraphsPageFan_u_sat.isChecked(),
                "color": "aquamarine",
            },
            "u(t)": {
                "state": self.handler.ui.btnGraphsPageFan_u.isChecked(),
                "color": "lime",
            },
            "u_p(t)": {
                "state": self.handler.ui.btnGraphsPageFan_u_p.isChecked(),
                "color": "darkcyan",
            },
            "u_i(t)": {
                "state": self.handler.ui.btnGraphsPageFan_u_i.isChecked(),
                "color": "royalblue",
            },
            "u_d(t)": {
                "state": self.handler.ui.btnGraphsPageFan_u_d.isChecked(),
                "color": "navy",
            },
        }

    @Slot()
    def update_graph(self):
        self.plot([
            self.controller.pid_u_saturated,
            self.controller.pid_u,
            self.controller.pid_u_p,
            self.controller.pid_u_i,
            self.controller.pid_u_d,
        ], self.controller.pid_time)

class GraphsPage:
    def __init__(self, handler):
        self.handler = handler
        self.heater_graph_y = HeaterGraphY(self.handler, self.handler.ui.layGraphsPageHeater_y, f"{DEGREE_SIGN}C")
        self.heater_graph_e = HeaterGraphE(self.handler, self.handler.ui.layGraphsPageHeater_e, f"{DEGREE_SIGN}C")
        self.heater_graph_u = HeaterGraphU(self.handler, self.handler.ui.layGraphsPageHeater_u, "")
        self.fan_graph_y = FanGraphY(self.handler, self.handler.ui.layGraphsPageFan_y, "RPM")
        self.fan_graph_e = FanGraphE(self.handler, self.handler.ui.layGraphsPageFan_e, "RPM")
        self.fan_graph_u = FanGraphU(self.handler, self.handler.ui.layGraphsPageFan_u, "")
        self.areGraphsRunning = True
        self.playIcon = QIcon()
        self.pauseIcon = QIcon()
        self.playIcon.addFile(u":/assets/assets/play.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pauseIcon.addFile(u":/assets/assets/pause.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

    def update(self):
        if self.areGraphsRunning:
            if self.handler.ui.btnGraphsPageHeater.isChecked():
                self.heater_graph_y.update_graph()
                self.heater_graph_e.update_graph()
                self.heater_graph_u.update_graph()
            else:
                self.fan_graph_y.update_graph()
                self.fan_graph_e.update_graph()
                self.fan_graph_u.update_graph()
    
    @Slot()
    def stop(self, state):
        self.handler.ui.btnGraphsPageStop.setIcon(self.playIcon if state else self.pauseIcon)
        self.areGraphsRunning = not state

    @Slot()
    def open_heater(self):
        self.handler.ui.btnGraphsPageHeater.setChecked(True)
        self.handler.ui.btnGraphsPageFan.setChecked(False)
        self.handler.isHeaterGraphsGraph = True
        self.handler.isFanGraphsGraph_running = False
        self.handler.ui.stackGraphsPage.setCurrentIndex(INDICES["graphs_heater"])

    @Slot()
    def open_fan(self):
        self.handler.ui.btnGraphsPageHeater.setChecked(False)
        self.handler.ui.btnGraphsPageFan.setChecked(True)
        self.handler.isHeaterGraphsGraph = False
        self.handler.isFanGraphsGraph_running = True
        self.handler.ui.stackGraphsPage.setCurrentIndex(INDICES["graphs_fan"])

    # Heater
    @Slot(bool)
    def set_heater_x(self, state):
        self.heater_graph_y.controls['x(t)']["state"] = state

    @Slot(bool)
    def set_heater_y_1(self, state):
        self.heater_graph_y.controls['y_1(t)']["state"] = state
        
    @Slot(bool)
    def set_heater_y_2(self, state):
        self.heater_graph_y.controls['y_2(t)']["state"] = state
        
    @Slot(bool)
    def set_heater_u_sat(self, state):
        self.heater_graph_u.controls['u_sat(t)']["state"] = state

    @Slot(bool)
    def set_heater_u(self, state):
        self.heater_graph_u.controls['u(t)']["state"] = state

    @Slot(bool)
    def set_heater_u_p(self, state):
        self.heater_graph_u.controls['u_p(t)']["state"] = state

    @Slot(bool)
    def set_heater_u_i(self, state):
        self.heater_graph_u.controls['u_i(t)']["state"] = state

    @Slot(bool)
    def set_heater_u_d(self, state):
        self.heater_graph_u.controls['u_d(t)']["state"] = state

    # Fan
    @Slot(bool)
    def set_fan_x(self, state):
        self.fan_graph_y.controls['x(t)']["state"] = state

    @Slot(bool)
    def set_fan_y(self, state):
        self.fan_graph_y.controls['y(t)']["state"] = state
        
    @Slot(bool)
    def set_fan_u_sat(self, state):
        self.fan_graph_u.controls['u_sat(t)']["state"] = state

    @Slot(bool)
    def set_fan_u(self, state):
        self.fan_graph_u.controls['u(t)']["state"] = state

    @Slot(bool)
    def set_fan_u_p(self, state):
        self.fan_graph_u.controls['u_p(t)']["state"] = state

    @Slot(bool)
    def set_fan_u_i(self, state):
        self.fan_graph_u.controls['u_i(t)']["state"] = state

    @Slot(bool)
    def set_fan_u_d(self, state):
        self.fan_graph_u.controls['u_d(t)']["state"] = state

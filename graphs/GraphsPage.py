# This Python file uses the following encoding: utf-8
from PySide6.QtCore import Slot, QSize
from PySide6.QtGui import QIcon
from MainMenuHandler import INDICES
from utilities import DEGREE_SIGN
from graphs.Graph import Graph
import rc_resources

class HeaterGraphY(Graph):
    def __init__(self, handler, layout, label, shared_x = None):
        super(HeaterGraphY, self).__init__(handler, layout, label, use_toolbar=True, shared_x=shared_x, show_coords=True)
        self.init_controls()
        self.keys = list(self.controls.keys())
        self.init_plot(False, True)

    def init_controls(self):
        self.controls = {
            "r(t)": {
                "state": True,
                "color": 'indianred',
            },
            "y_1(t)": {
                "state": True,
                "color": 'hotpink',
            },
            "y_2(t)": {
                "state": True,
                "color": 'crimson',
            },
        }

    @Slot()
    def update_graph(self):
        self.plot([
            self.handler.heaterController.pid_set_value,
            self.handler.heaterController.pid_temp_left,
            self.handler.heaterController.pid_temp_right,
        ], self.handler.heaterController.time)

class HeaterGraphE(Graph):
    def __init__(self, handler, layout, label, shared_x = None):
        super(HeaterGraphE, self).__init__(handler, layout, label, use_toolbar=True, shared_x=shared_x, show_coords=True)
        self.init_controls()
        self.keys = list(self.controls.keys())
        self.init_plot(False, True)

    def init_controls(self):
        self.controls = {
            "e(t)": {
                "state": True,
                "color": "tomato",
            },
        }

    @Slot()
    def update_graph(self):
        self.plot([
            self.handler.heaterController.pid_error,
        ], self.handler.heaterController.time)
    
class HeaterGraphU(Graph):
    def __init__(self, handler, layout, label, shared_x = None):
        super(HeaterGraphU, self).__init__(handler, layout, label, use_toolbar=True, shared_x=shared_x, show_coords=True)
        self.init_controls()
        self.keys = list(self.controls.keys())
        self.init_plot()

    def init_controls(self):
        self.controls = {
            "u_sat(t)": {
                "state": True,
                "color": "aquamarine",
            },
            "u(t)": {
                "state": True,
                "color": "lime",
            },
            "u_p(t)": {
                "state": True,
                "color": "darkcyan",
            },
            "u_i(t)": {
                "state": True,
                "color": "royalblue",
            },
            "u_d(t)": {
                "state": True,
                "color": "navy",
            },
        }

    @Slot()
    def update_graph(self):
        self.plot([
            self.handler.heaterController.pid_u_saturated,
            self.handler.heaterController.pid_u,
            self.handler.heaterController.pid_u_p,
            self.handler.heaterController.pid_u_i,
            self.handler.heaterController.pid_u_d,
        ], self.handler.heaterController.time)

class FanGraphY(Graph):
    def __init__(self, handler, layout, label, shared_x = None):
        super(FanGraphY, self).__init__(handler, layout, label, use_toolbar=True, shared_x=shared_x, show_coords=True)
        self.init_controls()
        self.keys = list(self.controls.keys())
        self.init_plot(False, True)

    def init_controls(self):
        self.controls = {
            "r(t)": {
                "state": True,
                "color": 'indianred',
            },
            "y(t)": {
                "state": True,
                "color": 'hotpink',
            },
        }

    @Slot()
    def update_graph(self):
        self.plot([
            self.handler.fanController.pid_set_value,
            self.handler.fanController.pid_speed,
        ], self.handler.fanController.time)

class FanGraphE(Graph):
    def __init__(self, handler, layout, label, shared_x = None):
        super(FanGraphE, self).__init__(handler, layout, label, use_toolbar=True, shared_x=shared_x, show_coords=True)
        self.init_controls()
        self.keys = list(self.controls.keys())
        self.init_plot(False, True)

    def init_controls(self):
        self.controls = {
            "e(t)": {
                "state": True,
                "color": "tomato",
            },
        }

    @Slot()
    def update_graph(self):
        self.plot([
            self.handler.fanController.pid_error,
        ], self.handler.fanController.time)

class FanGraphU(Graph):
    def __init__(self, handler, layout, label, shared_x = None):
        super(FanGraphU, self).__init__(handler, layout, label, use_toolbar=True, shared_x=shared_x, show_coords=True)
        self.init_controls()
        self.keys = list(self.controls.keys())
        self.init_plot()

    def init_controls(self):
        self.controls = {
            "u_sat(t)": {
                "state": True,
                "color": "aquamarine",
            },
            "u(t)": {
                "state": True,
                "color": "lime",
            },
            "u_p(t)": {
                "state": True,
                "color": "darkcyan",
            },
            "u_i(t)": {
                "state": True,
                "color": "royalblue",
            },
            "u_d(t)": {
                "state": True,
                "color": "navy",
            },
        }

    @Slot()
    def update_graph(self):
        self.plot([
            self.handler.fanController.pid_u_saturated,
            self.handler.fanController.pid_u,
            self.handler.fanController.pid_u_p,
            self.handler.fanController.pid_u_i,
            self.handler.fanController.pid_u_d,
        ], self.handler.fanController.time)

class GraphsPage:
    def __init__(self, handler):
        self.handler = handler
        self.heater_graph_y = HeaterGraphY(self.handler, self.handler.ui.layGraphsPageHeater_y, f"{DEGREE_SIGN}C")
        self.heater_graph_e = HeaterGraphE(self.handler, self.handler.ui.layGraphsPageHeater_e, f"{DEGREE_SIGN}C")
        self.heater_graph_u = HeaterGraphU(self.handler, self.handler.ui.layGraphsPageHeater_u, "V")
        self.heater_graph_e.ax.sharex(self.heater_graph_y.ax)
        self.heater_graph_u.ax.sharex(self.heater_graph_y.ax)
        self.fan_graph_y = FanGraphY(self.handler, self.handler.ui.layGraphsPageFan_y, "RPM")
        self.fan_graph_e = FanGraphE(self.handler, self.handler.ui.layGraphsPageFan_e, "RPM")
        self.fan_graph_u = FanGraphU(self.handler, self.handler.ui.layGraphsPageFan_u, "V")
        self.fan_graph_e.ax.sharex(self.fan_graph_y.ax)
        self.fan_graph_u.ax.sharex(self.fan_graph_y.ax)
        self.playIcon = QIcon()
        self.pauseIcon = QIcon()
        self.playIcon.addFile(u":/assets/assets/play.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pauseIcon.addFile(u":/assets/assets/pause.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.zoom_pending = 0

    def update(self):
        self.heater_graph_y.update_graph()
        self.heater_graph_e.update_graph()
        self.heater_graph_u.update_graph()
        self.fan_graph_y.update_graph()
        self.fan_graph_e.update_graph()
        self.fan_graph_u.update_graph()
    
    def home(self):
        self.heater_graph_y.home()
        self.heater_graph_e.home()
        self.heater_graph_u.home()
        self.fan_graph_y.home()
        self.fan_graph_e.home()
        self.fan_graph_u.home()

    @Slot()
    def open_heater(self):
        self.handler.ui.btnGraphsPageHeater.setChecked(True)
        self.handler.ui.btnGraphsPageFan.setChecked(False)
        self.handler.isHeaterGraphsGraph = True
        self.handler.isFanGraphsGraph_running = False
        self.handler.ui.stackGraphsPage.setCurrentIndex(INDICES["graphs_heater"])
        self.handler.ui.btnGraphsPage_y_1.setVisible(True)
        self.handler.ui.btnGraphsPage_y_2.setVisible(True)
        self.handler.ui.btnGraphsPage_y.setVisible(False)

        self.handler.ui.btnGraphsPage_x.setChecked(self.heater_graph_y.controls['r(t)']["state"])
        self.handler.ui.btnGraphsPage_y_1.setChecked(self.heater_graph_y.controls['y_1(t)']["state"])
        self.handler.ui.btnGraphsPage_y_2.setChecked(self.heater_graph_y.controls['y_2(t)']["state"])
        self.handler.ui.btnGraphsPage_u_sat.setChecked(self.heater_graph_u.controls['u_sat(t)']["state"])
        self.handler.ui.btnGraphsPage_u.setChecked(self.heater_graph_u.controls['u(t)']["state"])
        self.handler.ui.btnGraphsPage_u_p.setChecked(self.heater_graph_u.controls['u_p(t)']["state"])
        self.handler.ui.btnGraphsPage_u_i.setChecked(self.heater_graph_u.controls['u_i(t)']["state"])
        self.handler.ui.btnGraphsPage_u_d.setChecked(self.heater_graph_u.controls['u_d(t)']["state"])

    @Slot()
    def open_fan(self):
        self.handler.ui.btnGraphsPageHeater.setChecked(False)
        self.handler.ui.btnGraphsPageFan.setChecked(True)
        self.handler.isHeaterGraphsGraph = False
        self.handler.isFanGraphsGraph_running = True
        self.handler.ui.stackGraphsPage.setCurrentIndex(INDICES["graphs_fan"])
        self.handler.ui.btnGraphsPage_y_1.setVisible(False)
        self.handler.ui.btnGraphsPage_y_2.setVisible(False)
        self.handler.ui.btnGraphsPage_y.setVisible(True)

        self.handler.ui.btnGraphsPage_x.setChecked(self.fan_graph_y.controls['r(t)']["state"])
        self.handler.ui.btnGraphsPage_y.setChecked(self.fan_graph_y.controls['y(t)']["state"])
        self.handler.ui.btnGraphsPage_u_sat.setChecked(self.fan_graph_u.controls['u_sat(t)']["state"])
        self.handler.ui.btnGraphsPage_u.setChecked(self.fan_graph_u.controls['u(t)']["state"])
        self.handler.ui.btnGraphsPage_u_p.setChecked(self.fan_graph_u.controls['u_p(t)']["state"])
        self.handler.ui.btnGraphsPage_u_i.setChecked(self.fan_graph_u.controls['u_i(t)']["state"])
        self.handler.ui.btnGraphsPage_u_d.setChecked(self.fan_graph_u.controls['u_d(t)']["state"])

    # Heater
    @Slot(bool)
    def set_x(self, state):
        if self.handler.ui.btnGraphsPageHeater.isChecked():
            self.heater_graph_y.controls['r(t)']["state"] = state
            self.heater_graph_y.set_line_visibility('r(t)', state)
        else:
            self.fan_graph_y.controls['r(t)']["state"] = state
            self.fan_graph_y.set_line_visibility('r(t)', state)
    
    @Slot(bool)
    def set_y(self, state):
        self.fan_graph_y.controls['y(t)']["state"] = state
        self.fan_graph_y.set_line_visibility('y(t)', state)

    @Slot(bool)
    def set_y_1(self, state):
        self.heater_graph_y.controls['y_1(t)']["state"] = state
        self.heater_graph_y.set_line_visibility('y_1(t)', state)
        
    @Slot(bool)
    def set_y_2(self, state):
        self.heater_graph_y.controls['y_2(t)']["state"] = state
        self.heater_graph_y.set_line_visibility('y_2(t)', state)
        
    @Slot(bool)
    def set_u_sat(self, state):
        if self.handler.ui.btnGraphsPageHeater.isChecked():
            self.heater_graph_u.controls['u_sat(t)']["state"] = state
            self.heater_graph_u.set_line_visibility('u_sat(t)', state)
        else:
            self.fan_graph_u.controls['u_sat(t)']["state"] = state
            self.fan_graph_u.set_line_visibility('u_sat(t)', state)

    @Slot(bool)
    def set_u(self, state):
        if self.handler.ui.btnGraphsPageHeater.isChecked():
            self.heater_graph_u.controls['u(t)']["state"] = state
            self.heater_graph_u.set_line_visibility('u(t)', state)
        else:
            self.fan_graph_u.controls['u(t)']["state"] = state
            self.fan_graph_u.set_line_visibility('u(t)', state)

    @Slot(bool)
    def set_u_p(self, state):
        if self.handler.ui.btnGraphsPageHeater.isChecked():
            self.heater_graph_u.controls['u_p(t)']["state"] = state
            self.heater_graph_u.set_line_visibility('u_p(t)', state)
        else:
            self.fan_graph_u.controls['u_p(t)']["state"] = state
            self.fan_graph_u.set_line_visibility('u_p(t)', state)

    @Slot(bool)
    def set_u_i(self, state):
        if self.handler.ui.btnGraphsPageHeater.isChecked():
            self.heater_graph_u.controls['u_i(t)']["state"] = state
            self.heater_graph_u.set_line_visibility('u_i(t)', state)
        else:
            self.fan_graph_u.controls['u_i(t)']["state"] = state
            self.fan_graph_u.set_line_visibility('u_i(t)', state)

    @Slot(bool)
    def set_u_d(self, state):
        if self.handler.ui.btnGraphsPageHeater.isChecked():
            self.heater_graph_u.controls['u_d(t)']["state"] = state
            self.heater_graph_u.set_line_visibility('u_d(t)', state)
        else:
            self.fan_graph_u.controls['u_d(t)']["state"] = state
            self.fan_graph_u.set_line_visibility('u_d(t)', state)


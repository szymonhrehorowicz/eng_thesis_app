# This Python file uses the following encoding: utf-8
from graphs.Graph import Graph
from PySide6.QtCore import Slot

class FanPIDGraph(Graph):
    def __init__(self, handler, layout, label):
        super(FanPIDGraph, self).__init__(handler, layout, label, use_toolbar=True)
        self.init_controls()
        self.keys = list(self.controls.keys())
        self.init_plot()
    
    def init_controls(self):
        self.controller = self.handler.fanController
        self.controls = {
            "x(t)": {
                "state": self.handler.ui.btnFanPID_graph_x.isChecked(),
                "color": "indianred",
            },
            "e(t)": {
                "state": self.handler.ui.btnFanPID_graph_e.isChecked(),
                "color": "tomato",
            },
            "int_e(t)": {
                "state": self.handler.ui.btnFanPID_graph_int_e.isChecked(),
                "color": "peachpuff",
            },
            "aw_int_e(t)": {
                "state": self.handler.ui.btnFanPID_graph_aw_int_e.isChecked(),
                "color": "darkorange",
            },
            "k_p": {
                "state": self.handler.ui.btnFanPID_graph_k_p.isChecked(),
                "color": "gold",
            },
            "k_i": {
                "state": self.handler.ui.btnFanPID_graph_k_i.isChecked(),
                "color": "olive",
            },
            "k_d": {
                "state": self.handler.ui.btnFanPID_graph_k_d.isChecked(),
                "color": "yellow",
            },
            "k_aw": {
                "state": self.handler.ui.btnFanPID_graph_k_aw.isChecked(),
                "color": "greenyellow",
            },
            "u(t)": {
                "state": self.handler.ui.btnFanPID_graph_u.isChecked(),
                "color": "lime",
            },
            "u_sat(t)": {
                "state": self.handler.ui.btnFanPID_graph_u_sat.isChecked(),
                "color": "aquamarine",
            },
            "u_p(t)": {
                "state": self.handler.ui.btnFanPID_graph_u_p.isChecked(),
                "color": "darkcyan",
            },
            "u_i(t)": {
                "state": self.handler.ui.btnFanPID_graph_u_i.isChecked(),
                "color": "royalblue",
            },
            "u_d(t)": {
                "state": self.handler.ui.btnFanPID_graph_u_d.isChecked(),
                "color": "navy",
            },
            "u_max": {
                "state": self.handler.ui.btnFanPID_graph_u_max.isChecked(),
                "color": "blueviolet",
            },
            "u_min": {
                "state": self.handler.ui.btnFanPID_graph_u_min.isChecked(),
                "color": "violet",
            },
            "y(t)": {
                "state": self.handler.ui.btnFanPID_graph_y.isChecked(),
                "color": "hotpink",
            },
            "stan": {
                "state": self.handler.ui.btnFanPID_graph_mode.isChecked(),
                "color": "crimson",
            }
        }

    @Slot()
    def update_graph(self):
        self.plot([
            self.controller.pid_set_value,
            self.controller.pid_error,
            self.controller.pid_int_error,
            self.controller.pid_aw_int_error,
            self.controller.pid_kp,
            self.controller.pid_ki,
            self.controller.pid_kd,
            self.controller.pid_kaw,
            self.controller.pid_u,
            self.controller.pid_u_saturated,
            self.controller.pid_u_p,
            self.controller.pid_u_i,
            self.controller.pid_u_d,
            self.controller.pid_u_max,
            self.controller.pid_u_min,
            self.controller.pid_speed,
            self.controller.pid_mode,
        ], self.controller.pid_time)

    @Slot(bool)
    def set_value(self, state):
        self.controls['x(t)']["state"] = state
        self.set_line_visibility('x(t)', state)

    @Slot(bool)
    def set_e(self, state):
        self.controls['e(t)']["state"] = state
        self.set_line_visibility('e(t)', state)
    
    @Slot(bool)
    def set_int_e(self, state):
        self.controls['int_e(t)']["state"] = state
        self.set_line_visibility('int_e(t)', state)
    
    @Slot(bool)
    def set_aw_int_e(self, state):
        self.controls['aw_int_e(t)']["state"] = state
        self.set_line_visibility('aw_int_e(t)', state)

    @Slot(bool)
    def set_k_p(self, state):
        self.controls['k_p']["state"] = state
        self.set_line_visibility('k_p', state)

    @Slot(bool)
    def set_k_i(self, state):
        self.controls['k_i']["state"] = state
        self.set_line_visibility('k_i', state)
    
    @Slot(bool)
    def set_k_d(self, state):
        self.controls['k_d']["state"] = state
        self.set_line_visibility('k_d', state)
    
    @Slot(bool)
    def set_k_aw(self, state):
        self.controls['k_aw']["state"] = state
        self.set_line_visibility('k_aw', state)
    
    @Slot(bool)
    def set_u(self, state):
        self.controls['u(t)']["state"] = state
        self.set_line_visibility('u(t)', state)

    @Slot(bool)
    def set_u_sat(self, state):
        self.controls['u_sat(t)']["state"] = state
        self.set_line_visibility('u_sat(t)', state)
    
    @Slot(bool)
    def set_u_p(self, state):
        self.controls['u_p(t)']["state"] = state
        self.set_line_visibility('u_p(t)', state)
    
    @Slot(bool)
    def set_u_i(self, state):
        self.controls['u_i(t)']["state"] = state
        self.set_line_visibility('u_i(t)', state)
    
    @Slot(bool)
    def set_u_d(self, state):
        self.controls['u_d(t)']["state"] = state
        self.set_line_visibility('u_d(t)', state)

    @Slot(bool)
    def set_u_max(self, state):
        self.controls['u_max']["state"] = state
        self.set_line_visibility('u_max', state)
    
    @Slot(bool)
    def set_u_min(self, state):
        self.controls['u_min']["state"] = state
        self.set_line_visibility('u_min', state)
    
    @Slot(bool)
    def set_y(self, state):
        self.controls['y(t)']["state"] = state
        self.set_line_visibility('y(t)', state)
    
    @Slot(bool)
    def set_mode(self, state):
        self.controls['stan']["state"] = state
        self.set_line_visibility('stan', state)
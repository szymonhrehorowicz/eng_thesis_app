# This Python file uses the following encoding: utf-8
from Graph import Graph
from PySide6.QtCore import Slot

class HeaterPIDGraph(Graph):
    def __init__(self, handler, layout, label):
        super(HeaterPIDGraph, self).__init__(handler, layout, label, use_toolbar=True)
        self.init_controls()
        self.keys = list(self.controls.keys())
    
    def init_controls(self):
        self.controller = self.handler.heaterController
        self.controls = {
            "x(t)": {
                "state": True,
                "handler": self.handler.ui.btnHeaterPID_graph_x,
            },
            "e(t)": {
                "state": True,
                "handler": self.handler.ui.btnHeaterPID_graph_e,
            },
            "int_e(t)": {
                "state": True,
                "handler": self.handler.ui.btnHeaterPID_graph_int_e,
            },
            "aw_int_e(t)": {
                "state": True,
                "handler": self.handler.ui.btnHeaterPID_graph_aw_int_e,
            },
            "k_p(t)": {
                "state": True,
                "handler": self.handler.ui.btnHeaterPID_graph_k_p,
            },
            "k_i(t)": {
                "state": True,
                "handler": self.handler.ui.btnHeaterPID_graph_k_i,
            },
            "k_d(t)": {
                "state": True,
                "handler": self.handler.ui.btnHeaterPID_graph_k_d,
            },
            "k_aw(t)": {
                "state": True,
                "handler": self.handler.ui.btnHeaterPID_graph_k_aw,
            },
            "u(t)": {
                "state": True,
                "handler": self.handler.ui.btnHeaterPID_graph_u,
            },
            "u_sat(t)": {
                "state": True,
                "handler": self.handler.ui.btnHeaterPID_graph_u_sat,
            },
            "u_p(t)": {
                "state": True,
                "handler": self.handler.ui.btnHeaterPID_graph_u_p,
            },
            "u_i(t)": {
                "state": True,
                "handler": self.handler.ui.btnHeaterPID_graph_u_i,
            },
            "u_d(t)": {
                "state": True,
                "handler": self.handler.ui.btnHeaterPID_graph_u_d,
            },
            "u_max(t)": {
                "state": True,
                "handler": self.handler.ui.btnHeaterPID_graph_u_max,
            },
            "u_min(t)": {
                "state": True,
                "handler": self.handler.ui.btnHeaterPID_graph_u_min,
            },
            "y_1(t)": {
                "state": True,
                "handler": self.handler.ui.btnHeaterPID_graph_y_1,
            },
            "y_2(t)": {
                "state": True,
                "handler": self.handler.ui.btnHeaterPID_graph_y_2,
            },
            "stan": {
                "state": True,
                "handelr": self.handler.ui.btnHeaterPID_graph_mode,
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
            self.controller.pid_temp_left,
            self.controller.pid_temp_right,
            self.controller.pid_mode,
        ], self.controller.time)

    @Slot(bool)
    def set_value(self, state):
        self.controls['x(t)']["state"] = state

    @Slot(bool)
    def set_e(self, state):
        self.controls['e(t)']["state"] = state
    
    @Slot(bool)
    def set_int_e(self, state):
        self.controls['int_e(t)']["state"] = state
    
    @Slot(bool)
    def set_aw_int_e(self, state):
        self.controls['aw_int_e(t)']["state"] = state

    @Slot(bool)
    def set_k_p(self, state):
        self.controls['k_p(t)']["state"] = state

    @Slot(bool)
    def set_k_i(self, state):
        self.controls['k_i(t)']["state"] = state
    
    @Slot(bool)
    def set_k_d(self, state):
        self.controls['k_d(t)']["state"] = state
    
    @Slot(bool)
    def set_k_aw(self, state):
        self.controls['k_aw(t)']["state"] = state
    
    @Slot(bool)
    def set_u(self, state):
        self.controls['u(t)']["state"] = state

    @Slot(bool)
    def set_u_sat(self, state):
        self.controls['u_sat(t)']["state"] = state
    
    @Slot(bool)
    def set_u_p(self, state):
        self.controls['u_p(t)']["state"] = state
    
    @Slot(bool)
    def set_u_i(self, state):
        self.controls['u_i(t)']["state"] = state
    
    @Slot(bool)
    def set_u_d(self, state):
        self.controls['u_d(t)']["state"] = state

    @Slot(bool)
    def set_u_max(self, state):
        self.controls['u_max(t)']["state"] = state
    
    @Slot(bool)
    def set_u_min(self, state):
        self.controls['u_min(t)']["state"] = state
    
    @Slot(bool)
    def set_y_1(self, state):
        self.controls['y_1(t)']["state"] = state

    @Slot(bool)
    def set_y_2(self, state):
        self.controls['y_2(t)']["state"] = state
    
    @Slot(bool)
    def set_mode(self, state):
        self.controls['stan']["state"] = state

# This Python file uses the following encoding: utf-8
from Graph import Graph
from PySide6.QtCore import Slot

class FanBBGraph(Graph):
    def __init__(self, handler, layout, label):
        super(FanBBGraph, self).__init__(handler, layout, label, use_toolbar=True)
        self.init_controls()
        self.keys = list(self.controls.keys())

    def init_controls(self):
        self.controller = self.handler.fanController
        self.controls = {
            "x(t)": {
                "state": True,
                "handler": self.handler.ui.btnFanBB_graph_x,
            },
            "x_max(t)": {
                "state": True,
                "handler": self.handler.ui.btnFanBB_graph_x_max,
            },
            "x_min(t)": {
                "state": True,
                "handler": self.handler.ui.btnFanBB_graph_x_min,
            },
            "u_max(t)": {
                "state": True,
                "handler": self.handler.ui.btnFanBB_graph_u_max,
            },
            "u_min(t)": {
                "state": True,
                "handler": self.handler.ui.btnFanBB_graph_u_min,
            },
            "y(t)": {
                "state": True,
                "handler": self.handler.ui.btnFanBB_graph_y,
            },
            "stan": {
                "state": True,
                "handler": self.handler.ui.btnFanBB_graph_mode,
            }
        }

    @Slot()
    def update_graph(self):
        self.plot([
            self.controller.bb_set_value,
            self.controller.bb_threshold_top,
            self.controller.bb_threshold_bottom,
            self.controller.bb_u_max,
            self.controller.bb_u_min,
            self.controller.pid_speed,
            self.controller.bb_mode
        ], self.controller.time)

    @Slot(bool)
    def set_value(self, state):
        self.controls['x(t)']["state"] = state

    @Slot(bool)
    def set_threshold_top(self, state):
        self.controls['x_max(t)']["state"] = state

    @Slot(bool)
    def set_threshold_bottom(self, state):
        self.controls['x_min(t)']["state"] = state

    @Slot(bool)
    def set_u_max(self, state):
        self.controls['u_max(t)']["state"] = state

    @Slot(bool)
    def set_u_min(self, state):
        self.controls['u_min(t)']["state"] = state

    @Slot(bool)
    def set_y(self, state):
        self.controls['y(t)']["state"] = state

    @Slot(bool)
    def set_mode(self, state):
        self.controls['stan']["state"] = state
    

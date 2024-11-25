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
                "state": self.handler.ui.btnFanBB_graph_x.isChecked(),
            },
            "x_max(t)": {
                "state": self.handler.ui.btnFanBB_graph_x_max.isChecked(),
            },
            "x_min(t)": {
                "state": self.handler.ui.btnFanBB_graph_x_min.isChecked(),
            },
            "u_max(t)": {
                "state": self.handler.ui.btnFanBB_graph_u_max.isChecked(),
            },
            "u_min(t)": {
                "state": self.handler.ui.btnFanBB_graph_u_min.isChecked(),
            },
            "y(t)": {
                "state": self.handler.ui.btnFanBB_graph_y.isChecked(),
            },
            "stan": {
                "state": self.handler.ui.btnFanBB_graph_mode.isChecked(),
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
    

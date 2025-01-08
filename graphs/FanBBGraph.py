# This Python file uses the following encoding: utf-8
from graphs.Graph import Graph
from PySide6.QtCore import Slot

class FanBBGraph(Graph):
    def __init__(self, handler, layout, label):
        super(FanBBGraph, self).__init__(handler, layout, label, use_toolbar=True)
        self.init_controls()
        self.keys = list(self.controls.keys())
        self.init_plot()

    def init_controls(self):
        self.controller = self.handler.fanController
        self.controls = {
            "x(t)": {
                "state": self.handler.ui.btnFanBB_graph_x.isChecked(),
                "color": 'indianred',
            },
            "x_max": {
                "state": self.handler.ui.btnFanBB_graph_x_max.isChecked(),
                "color": 'tomato',
            },
            "x_min": {
                "state": self.handler.ui.btnFanBB_graph_x_min.isChecked(),
                "color": 'peachpuff',
            },
            "u_max": {
                "state": self.handler.ui.btnFanBB_graph_u_max.isChecked(),
                "color": 'darkorange',
            },
            "u_min": {
                "state": self.handler.ui.btnFanBB_graph_u_min.isChecked(),
                "color": 'gold',
            },
            "y(t)": {
                "state": self.handler.ui.btnFanBB_graph_y.isChecked(),
                "color": 'olive',
            },
            "stan": {
                "state": self.handler.ui.btnFanBB_graph_mode.isChecked(),
                "color": 'yellow',
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
            self.controller.bb_speed,
            self.controller.bb_mode
        ], self.controller.bb_time)

    @Slot(bool)
    def set_value(self, state):
        self.controls['x(t)']["state"] = state
        self.set_line_visibility('x(t)', state)

    @Slot(bool)
    def set_threshold_top(self, state):
        self.controls['x_max']["state"] = state
        self.set_line_visibility('x_max', state)

    @Slot(bool)
    def set_threshold_bottom(self, state):
        self.controls['x_min']["state"] = state
        self.set_line_visibility('x_min', state)

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
    

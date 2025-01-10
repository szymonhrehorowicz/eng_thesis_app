# This Python file uses the following encoding: utf-8
from graphs.Graph import Graph
from PySide6.QtCore import Slot

class HeaterBBGraph(Graph):
    def __init__(self, handler, layout, label):
        super(HeaterBBGraph, self).__init__(handler, layout, label, use_toolbar=True)
        self.init_controls()
        self.keys = list(self.controls.keys())
        self.init_plot()

    def init_controls(self):
        self.controller = self.handler.heaterController
        self.controls = {
            "r(t)": {
                "state": self.handler.ui.btnHeaterBB_graph_x.isChecked(),
                "color": "indianred",
            },
            "r_max": {
                "state": self.handler.ui.btnHeaterBB_graph_x_max.isChecked(),
                "color": "tomato",
            },
            "r_min": {
                "state": self.handler.ui.btnHeaterBB_graph_x_min.isChecked(),
                "color": "peachpuff",
            },
            "u_max": {
                "state": self.handler.ui.btnHeaterBB_graph_u_max.isChecked(),
                "color": "darkorange",
            },
            "u_min": {
                "state": self.handler.ui.btnHeaterBB_graph_u_min.isChecked(),
                "color": "gold",
            },
            "y_1(t)": {
                "state": self.handler.ui.btnHeaterBB_graph_y_1.isChecked(),
                "color": "olive",
            },
            "y_2(t)": {
                "state": self.handler.ui.btnHeaterBB_graph_y_2.isChecked(),
                "color": "yellow",
            },
            "stan": {
                "state": self.handler.ui.btnHeaterBB_graph_mode.isChecked(),
                "color": "greenyellow",
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
            self.controller.bb_temp_left,
            self.controller.bb_temp_right,
            self.controller.bb_mode
        ], self.controller.time)

    @Slot(bool)
    def set_value(self, state):
        self.controls['r(t)']["state"] = state
        self.set_line_visibility('r(t)', state)

    @Slot(bool)
    def set_threshold_top(self, state):
        self.controls['r_max']["state"] = state
        self.set_line_visibility('r_max', state)

    @Slot(bool)
    def set_threshold_bottom(self, state):
        self.controls['r_min']["state"] = state
        self.set_line_visibility('r_min', state)

    @Slot(bool)
    def set_u_max(self, state):
        self.controls['u_max']["state"] = state
        self.set_line_visibility('u_max', state)

    @Slot(bool)
    def set_u_min(self, state):
        self.controls['u_min']["state"] = state
        self.set_line_visibility('u_min', state)

    @Slot(bool)
    def set_y_1(self, state):
        self.controls['y_1(t)']["state"] = state
        self.set_line_visibility('y_1(t)', state)

    @Slot(bool)
    def set_y_2(self, state):
        self.controls['y_2(t)']["state"] = state
        self.set_line_visibility('y_2(t)', state)

    @Slot(bool)
    def set_mode(self, state):
        self.controls['stan']["state"] = state
        self.set_line_visibility('stan', state)

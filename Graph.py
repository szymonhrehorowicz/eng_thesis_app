# This Python file uses the following encoding: utf-8
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QSizePolicy
from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.figure import Figure
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar

class Graph:
    def __init__(self, handler, layout, label, use_toolbar=True):
        # Handlers
        self.handler = handler
        self.layout = layout
        # Insert Graph into the application
        self.figure = Figure(figsize=(5, 3))
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.layout.addWidget(self.canvas)
        # Add toolbar
        if use_toolbar:
            self.layout.addWidget(NavigationToolbar(self.canvas, self.handler))
        # Get plot handler
        self.ax = self.canvas.figure.add_subplot(111)
        # Label
        self.label = label
        # Controls
        self.controls = {
            # BB
            'x1'  : True,
            'u_max': True,
            'u_min': True,
            'x1_threshold_top': True,
            'x1_threshold_bottom': True,
            'mode': True,
            # PID
            'x2': True,
            'error': True,
            'int_error': True,
            'aw_int_error': True,
            'Kp': True,
            'Ki': True,
            'Kd': True,
            'Kaw': True,
            'u': True,
            'u_saturated': True,
            'u_p': True,
            'u_i': True,
            'u_d': True,
            'u_max': True,
            'mode': True,
            # Common
            'y1' : True,
            'y2' : True,
        }
        self.figure.tight_layout()

    def plot(self, signals: list, t: list):
        # Clear the previous plot
        self.ax.cla()
        # Plot lines
        for signal in signals:
            if self.controls[signal["name"]]:
                self.ax.plot(signal["values"], t, label=f'{signal["name"]}(t)', marker='.')
        if any([self.controls[key] for key in self.controls]):
            self.ax.legend(loc='lower left')  # Add legend to differentiate the lines
        self.ax.set_xlabel('t, s')  # Label x-axis
        self.ax.set_ylabel(self.label)  # Label y-axis
        self.ax.grid()
        self.canvas.draw()  # Redraw the canvas to reflect the updates

    @Slot()
    def update_graph(self, type):
        data = self.handler.coil_controller.get_data() if type == 'coil' else self.handler.fan_controller.get_data()
        self.plot([
            {
                "name": "P",
                "values": data[1],
            },
            {
                "name": "I",
                "values": data[2],
            },
            {
                "name": "D",
                "values": data[3],
            },
            {
                "name": "x",
                "values": data[4],
            },
            {
                "name": "e_a",
                "values": data[5][0],
            },
            {
                "name": "e_b",
                "values": data[5][1],
            },
            {
                "name": "y_a",
                "values": data[6][0],
            },
            {
                "name": "y_b",
                "values": data[6][1],
            }
        ], t=data[0])

    @Slot(bool)
    def set_ctrl_set(self, state):
        self.controls['x'] = state

    @Slot(bool)
    def set_ctrl_errorA(self, state):
        self.controls['e_a'] = state

    @Slot(bool)
    def set_ctrl_errorB(self, state):
        self.controls['e_b'] = state

    @Slot(bool)
    def set_ctrl_valueA(self, state):
        self.controls['y_a'] = state

    @Slot(bool)
    def set_ctrl_valueB(self, state):
        self.controls['y_b'] = state

    @Slot(bool)
    def set_ctrl_P(self, state):
        self.controls['P'] = state

    @Slot(bool)
    def set_ctrl_I(self, state):
        self.controls['I'] = state

    @Slot(bool)
    def set_ctrl_D(self, state):
        self.controls['D'] = state


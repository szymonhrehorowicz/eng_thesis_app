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
        self.figure.tight_layout()

    def init_controls(self):
        pass

    def plot(self, signals: list, t: list):
        # Clear the previous plot
        self.ax.cla()
        # Plot lines
        for idx, signal in enumerate(signals):
            if self.controls[self.keys[idx]]["state"]:
                self.ax.plot(t, signal, label=self.keys[idx], marker='')
        if any([self.controls[key]["state"] for key in self.keys]):
            self.ax.legend(loc="lower left")
        self.ax.set_xlabel('t, s')  # Label x-axis
        self.ax.set_ylabel(self.label)  # Label y-axis
        self.ax.grid()
        self.canvas.draw()  # Redraw the canvas to reflect the updates

    @Slot()
    def update_graph(self, type):
        pass


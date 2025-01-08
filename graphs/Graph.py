# This Python file uses the following encoding: utf-8
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QSizePolicy
from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.figure import Figure
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.colors import CSS4_COLORS

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
            self.toolbar = NavigationToolbar(self.canvas, self.handler)
            self.layout.addWidget(self.toolbar)
        # Get plot handler
        self.ax = self.canvas.figure.add_subplot(111)
        # Label
        self.label = label
        # Controls
        self.figure.tight_layout()

    def init_controls(self):
        pass

    def init_plot(self):
        for idx, control in enumerate(self.controls):
            self.ax.plot([], [], color=CSS4_COLORS[self.controls[self.keys[idx]]["color"]], label=self.keys[idx], marker='')
            if not self.controls[self.keys[idx]]["state"]:
                self.ax.get_lines()[-1].set_visible(False)
        self.ax.set_xlabel('t, s')  # Label x-axis
        self.ax.legend(loc="lower left")
        self.ax.set_ylabel(self.label)  # Label y-axis
        self.ax.grid()
        self.canvas.draw()  # Redraw the canvas to reflect the updates

    def plot(self, signals: list, t:list):
        lines = self.ax.get_lines()
        for idx, signal in enumerate(signals):
            lines[idx].set_xdata(t)
            lines[idx].set_ydata(signal)
        self.refresh()
    
    def refresh(self):
        handles, labels = self.ax.get_legend_handles_labels()
        helper = 0
        for idx, key in enumerate(self.controls):
            if not self.controls[key]["state"]:
                del handles[idx - helper]
                del labels[idx - helper]
                helper += 1
        self.ax.legend(handles, labels, loc="lower left")
        self.ax.relim(visible_only=True)
        self.ax.autoscale_view()
        self.canvas.draw()

    @Slot()
    def update_graph(self, type):
        pass

    def set_line_visibility(self, key, state):
        self.ax.get_lines()[list(self.controls.keys()).index(key)].set_visible(state)
        self.refresh()


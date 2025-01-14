# This Python file uses the following encoding: utf-8
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QSizePolicy, QWidget, QVBoxLayout
from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.figure import Figure
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.colors import CSS4_COLORS

from PySide6.QtCore import Qt

class VerticalToolbar(NavigationToolbar):
    def __init__(self, canvas, parent=None):
        super().__init__(canvas, parent)

        # Get the default actions
        actions = self.actions()

        # Remove the existing widgets (actions)
        for action in actions:
            self.removeAction(action)

        # Create a new vertical layout
        self.setOrientation(Qt.Vertical)

        # Add the actions back to the vertical layout
        for action in actions:
            self.addAction(action)

        self.setMaximumWidth(50)
        self.setMinimumWidth(50)

class Graph:
    def __init__(self, handler, layout, label, use_toolbar=True):
        # Handlers
        self.handler = handler
        self.layout = layout
        # Insert Graph into the application
        self.figure = Figure(constrained_layout=True, figsize=(5, 3))
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # Add toolbar
        if use_toolbar:
            self.toolbar = VerticalToolbar(self.canvas, self.handler)
            self.layout.addWidget(self.toolbar)
        self.layout.addWidget(self.canvas)
        # Get plot handler
        self.ax = self.canvas.figure.add_subplot(111)
        # Label
        label = ' ' if label == '' else label
        self.label = label

    def init_controls(self):
        pass

    def init_plot(self, set_x_label = True, hide_tickmarks = False):
        for idx, control in enumerate(self.controls):
            self.ax.plot([], [], color=CSS4_COLORS[self.controls[self.keys[idx]]["color"]], label=self.keys[idx], marker='')
            if not self.controls[self.keys[idx]]["state"]:
                self.ax.get_lines()[-1].set_visible(False)
        if set_x_label:
            self.ax.set_xlabel('t, s')  # Label x-axis
        self.ax.legend(loc="lower left")
        self.ax.set_ylabel(self.label)  # Label y-axis
        self.ax.grid()
        self.canvas.draw()  # Redraw the canvas to reflect the updates
        if hide_tickmarks:
            self.ax.tick_params(axis='x', labelbottom=False)
        

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

    def home(self):
        self.toolbar.home()

    @Slot()
    def update_graph(self, type):
        pass

    def set_line_visibility(self, key, state):
        self.ax.get_lines()[list(self.controls.keys()).index(key)].set_visible(state)
        self.refresh()


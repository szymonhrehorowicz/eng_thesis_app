# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QDialogButtonBox

class VariableWithBoundires:
    def __init__(self, value: int, min: int, max: int):
        self.value = value
        self.min = min
        self.max = max

def trim_to_boundries(value: int, var: VariableWithBoundires):
    value = value if value < var.max else var.max
    value = value if value > var.min else var.min
    return value

DEGREE_SIGN = u'\N{DEGREE SIGN}'

if __name__ == "__main__":
    pass

def error_dialog(handler, text):
    dialog = QDialog(handler)
    dialog.setWindowTitle("Błąd")
    buttonBox = QDialogButtonBox(QDialogButtonBox.Ok)
    buttonBox.accepted.connect(dialog.close)
    message = QLabel(text)
    layout = QVBoxLayout()
    layout.addWidget(message)
    layout.addWidget(buttonBox)
    dialog.setLayout(layout)
    dialog.exec()

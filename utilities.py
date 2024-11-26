# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QDialogButtonBox
from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon
import rc_resources

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

def dialog(handler, window_text, text, icon):
    dialog = QDialog(handler)
    alertIcon = QIcon()
    alertIcon.addFile(icon, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
    dialog.setWindowIcon(alertIcon)
    dialog.setWindowTitle(window_text)
    buttonBox = QDialogButtonBox(QDialogButtonBox.Ok)
    buttonBox.accepted.connect(dialog.close)
    message = QLabel(text)
    layout = QVBoxLayout()
    layout.addWidget(message)
    layout.addWidget(buttonBox)
    dialog.setLayout(layout)
    dialog.exec()

def error_dialog(handler, text):
    dialog(handler, "Błąd", text, u":/assets/assets/alert.ico")

def success_dialog(handler, text):
    dialog(handler, "Sukces", text, u":/assets/assets/success.ico")
# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QDialogButtonBox
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QIcon, QPixmap
import struct
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

def dialog(handler, window_text, text, icon, picture=None):
    dialog = QDialog(handler)
    alertIcon = QIcon()
    alertIcon.addFile(icon, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
    dialog.setWindowIcon(alertIcon)
    dialog.setWindowTitle(window_text)
    buttonBox = QDialogButtonBox(QDialogButtonBox.Ok)
    buttonBox.accepted.connect(dialog.close)
    message = QLabel()
    layout = QVBoxLayout()
    if picture:
        pixmap = QPixmap(picture)
        pixmap = pixmap.scaled(700, 350, Qt.AspectRatioMode.KeepAspectRatio)
        message.setPixmap(pixmap)
        message.setAlignment(Qt.AlignCenter)
    else:
        message.setText(text)
    layout.addWidget(message)
    layout.addWidget(buttonBox)
    dialog.setLayout(layout)
    dialog.exec()

def error_dialog(handler, text):
    dialog(handler, "Błąd", text, u":/assets/assets/alert.ico")

def success_dialog(handler, text):
    dialog(handler, "Sukces", text, u":/assets/assets/success.ico")

def info_dialog(handler, header, picture):
    dialog(handler, header, "", u":/assets/assets/help.ico", picture)

def get_uint8(data):
    return bin(data)[2:].zfill(8)

def get_uint16(data):
    return get_uint8(data[0]) + get_uint8(data[1])

def get_uint32(data):
    return get_uint16(data) + get_uint16(data[2:])

def int2(uint):
    return int(uint, 2)

def get_float(num):
    return struct.unpack('f', struct.pack('I', num))[0]

def bytes_to_float(byte_array, is_big_endian=True):
    if len(byte_array) != 4:
        raise ValueError("Byte array must be exactly 4 bytes long.")
    
    if is_big_endian:
        byte_array = byte_array[::-1]

    return struct.unpack('f', byte_array)[0]

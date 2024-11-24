# This Python file uses the following encoding: utf-8
from PySide6.QtCore import QIODeviceBase, Slot, QByteArray
from PySide6.QtSerialPort import QSerialPort, QSerialPortInfo
from utils import error_dialog
import time

BLANK_STRING = "N/A"
DEBUG = True

class Serial:
    def __init__(self, handler):
        self.ui = handler.ui
        self.handler = handler
        self._serial = QSerialPort(handler)
        self.settings = Settings()
        self._serial.errorOccurred.connect(self.handle_error)
        self._serial.readyRead.connect(self.read_data)

    """
    PUBLIC
    """
    def open_serial_port(self):
        ports = self.__get_available_ports()
        res = False
        for port in ports:
            if "STMicroelectronics" in port.manufacturer:
                s = Settings()
                self._serial.setPortName(port.name)
                self._serial.setBaudRate(s.baud_rate)
                self._serial.setDataBits(s.data_bits)
                self._serial.setParity(s.parity)
                self._serial.setStopBits(s.stop_bits)
                self._serial.setFlowControl(s.flow_control)
                if self._serial.open(QIODeviceBase.ReadWrite):
                    print(f"Connected to {port.name}")
                    self.write_data(QByteArray("0"))
                    res = True
                    break
                else:
                    print("Serial error\n", self._serial.errorString())
        return res

    def close_serial_port(self):
        #self.ui.btnConnect.setText("Connect")
        #self.ui.btnConnect.setStatusTip("Połącz się z urządzeniem")
        #self.ui.btnConnect.setChecked(False)

        #self.ui.btnStartCoil.setEnabled(False)
        #self.ui.btnStartFan.setEnabled(False)
        #self.ui.btnUpdateCoil.setEnabled(False)
        #self.ui.btnUpdateFan.setEnabled(False)

        if self._serial.isOpen():
            self._serial.close()
            print("Disconnected")

    """
    PRIVATE
    """
    def __get_available_ports(self):
        ports_info = []
        for info in QSerialPortInfo.availablePorts():
            port_info = SerialPortInfo()
            description = info.description()
            manufacturer = info.manufacturer()
            serial_number = info.serialNumber()
            port_info.name = info.portName()
            port_info.desc = description if description else BLANK_STRING
            port_info.manufacturer = manufacturer if manufacturer else BLANK_STRING
            port_info.serial_number = serial_number if serial_number else BLANK_STRING
            port_info.sys_loc = info.systemLocation()
            vid = info.vendorIdentifier()
            port_info.vendor_id = f"{vid:x}" if vid else BLANK_STRING
            pid = info.productIdentifier()
            port_info.product_id = f"{pid:x}" if pid else BLANK_STRING
            ports_info.append(port_info)
        return ports_info

    """
    SLOTs
    """
    @Slot(bool)
    def slot_btnConnect(self, data):
        if data:
            # If data is True, then button was just CHECKED - connect with device
            if not self.open_serial_port():
                self.ui.btnConnect.setChecked(False)
                error_dialog(self.handler, "Nie znaleziono urządzenia")
            else:
                #self.ui.btnStartCoil.setEnabled(True)
                #self.ui.btnStartFan.setEnabled(True)
                #self.ui.btnUpdateCoil.setEnabled(True)
                #self.ui.btnUpdateFan.setEnabled(True)
                pass
        else:
            # If data is False, then button was just UNCHECKED - disconnect with device
            self.close_serial_port()

    @Slot(bytearray)
    def write_data(self, data):
        self._serial.write(data)

    @Slot()
    def read_data(self):
        data = self._serial.readAll().data().decode()
        if data == 'DEV_CON_ACK':
            # Handle successful connection
            self.ui.btnConnect.setText("Disconnect")
            self.ui.btnConnect.setStatusTip("Rozłącz się z urządzeniem")
        elif 'ALLCOIL_' in data:
            if data.index('ALLCOIL_') == 0:
                self.handler.COM.handle_all_heater_data(data)
        elif 'FASTCOIL_' in data:
            if data.index('FASTCOIL_') == 0:
                self.handler.COM.handle_fast_heater_data(data)
        elif 'ALLFAN_' in data:
            if data.index('ALLFAN_') == 0:
                self.handler.COM.handle_all_fan_data(data)
        elif 'FASTFAN_' in data:
            if data.index('FASTFAN') == 0:
                self.handler.COM.handle_fast_fan_data(data)
        if DEBUG:
            print(data)

    @Slot(QSerialPort.SerialPortError)
    def handle_error(self, error):
        if error == QSerialPort.ResourceError:
            print("Serial error\n", self._serial.errorString())
            self.close_serial_port()

"""
UTILS
"""
class Settings:
    def __init__(self):
        self.name = ""
        self.baud_rate = 115200
        self.data_bits = QSerialPort.Data8
        self.parity = QSerialPort.NoParity
        self.stop_bits = QSerialPort.OneStop
        self.flow_control = QSerialPort.SoftwareControl

class SerialPortInfo:
    def __init__(self):
        self.name = ""
        self.desc = ""
        self.manufacturer = ""
        self.serial_number = ""
        self.sys_loc = ""
        self.vendor_id = ""
        self.product_id = ""

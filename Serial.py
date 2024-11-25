# This Python file uses the following encoding: utf-8
from PySide6.QtCore import QIODeviceBase, Slot, QByteArray
from PySide6.QtSerialPort import QSerialPort, QSerialPortInfo
from utilities import error_dialog

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
        self.ui.btnConnect.setText("Connect")
        self.ui.btnConnect.setStatusTip("Połącz się z urządzeniem")
        self.ui.btnConnect.setChecked(False)

        self.ui.btnHeaterControls.setEnabled(False)
        self.ui.btnFanControls.setEnabled(False)
        self.handler.mainMenuHandler.open_help()

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
                self.ui.btnHeaterControls.setEnabled(True)
                self.ui.btnFanControls.setEnabled(True)
        else:
            # If data is False, then button was just UNCHECKED - disconnect with device
            self.close_serial_port()

    @Slot(bytearray)
    def write_data(self, data):
        self._serial.write(data)

    @Slot()
    def read_data(self):
        data = self._serial.readAll().data().decode()
        if 'DEV_CON_ACK' in data:
            # Handle successful connection
            self.ui.btnConnect.setText("Disconnect")
            self.ui.btnConnect.setStatusTip("Rozłącz się z urządzeniem")
        else:
            packets = []
            num_of_packets = data.count('ALLFAN_') + data.count('ALLCOIL_')
            
            for i in range(0, num_of_packets):
                try:
                    idx_fan = data.index('ALLFAN_')
                except ValueError:
                    idx_fan = len(data)
                try:
                    idx_coil = data.index('ALLCOIL_')
                except ValueError:
                    idx_coil = len(data)
                isFan = True if idx_fan < idx_coil else False
                dataToCut = 0
                if isFan:
                    dataToCut = idx_fan + len('ALLFAN_')
                    packets.append({"type": "ALLFAN_", "data": data[idx_fan:idx_coil]})
                else:
                    dataToCut = idx_coil + len('ALLCOIL_')
                    packets.append({"type": "ALLCOIL_", "data": data[idx_coil:idx_fan]})
                data = data[dataToCut:]
            
            for packet in packets:
                if packet["type"] == "ALLFAN_":
                    self.handler.COM.handle_all_fan_data(packet["data"])
                else:
                    self.handler.COM.handle_all_heater_data(packet["data"])

    @Slot(QSerialPort.SerialPortError)
    def handle_error(self, error):
        if error == QSerialPort.ResourceError:
            print("Serial error\n", self._serial.errorString())
            error_dialog(self.handler, "Połączenie z urządzeniem zostało przerwane")
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

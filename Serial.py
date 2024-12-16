# This Python file uses the following encoding: utf-8
from PySide6.QtCore import QIODeviceBase, Slot, QByteArray
from PySide6.QtSerialPort import QSerialPort, QSerialPortInfo
from utilities import error_dialog, get_uint8, get_uint16, get_uint32, get_float, int2

BLANK_STRING = "N/A"
DEBUG = True
DEV_CON_ACK = "10000000"
MSG_ALL_FAST = 0
MSG_FAN_ON_OFF = 1
MSG_HEATER_ON_OFF = 2
MSG_TEMP_REF = 3
MSG_COIL_REF = 4

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
    def send_ack(self):
        self.write_data(QByteArray("0\n"))

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
                    self.send_ack()
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
        self.ui.btnHeaterStart.setChecked(False)
        self.ui.btnFanStart.setChecked(False)
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
            # If data is False, then button was just UNCHECKED - disconnect with device
            self.close_serial_port()

    @Slot(bytearray)
    def write_data(self, data):
        self._serial.write(data)

    @Slot()
    def read_data(self):
        try:
            data = self._serial.readAll().data()
            header = get_uint8(data[0])[::-1]
            data = data[1:]

            # Handle successful connection
            self.ui.btnConnect.setText("Disconnect")
            self.ui.btnConnect.setStatusTip("Rozłącz się z urządzeniem")
            self.ui.btnHeaterControls.setEnabled(True)
            self.ui.btnFanControls.setEnabled(True)

            """
            Byte 0 : 
            0: ALL/FAST | 1: FAN OFF/ON | 2: COIL OFF/ON | 3: TEMP_REF_TOP/TEMP_REF_BOTTOM | 
            4: COIL_REF_TOP/COIL_REF_BOTTOM | 5: NA| 6: NA| 7: NA|
            """
            binarized_data = [bin(elem)[2:].zfill(8) for elem in data]
            # Handle header
            isAllData = header[MSG_ALL_FAST] == '0'
            isFanOn = header[MSG_FAN_ON_OFF] == '1'
            isHeaterOn = header[MSG_HEATER_ON_OFF] == '1'
            refTemp = header[MSG_TEMP_REF]
            refCoil = header[MSG_COIL_REF]
            # Handle data
            timestamp = int2(get_uint32(data))
            data = data[4:]
            binarized_data = binarized_data[4:]
            all_data = []
            fast_data = []
            if isAllData:
                # [ALL]
                """
                    FAN
                """
                # Bang-Bang: cmd: u8 | set_value: u16 | threshold_top: u16 | threshold_bottom: u16 | u_max: u16 | u_min: u16
                all_data.append(int2(get_uint8(data[0])))
                data = data[1:]
                all_data.append(int2(get_uint16(data)))
                data = data[2:]
                all_data.append(int2(get_uint16(data)))
                data = data[2:]
                all_data.append(int2(get_uint16(data)))
                data = data[2:]
                all_data.append(int2(get_uint16(data)))
                data = data[2:]
                all_data.append(int2(get_uint16(data)))
                data = data[2:]
                # PID: set_value: u16 | error: f32 | int_sum: f32 | aw_int_sum: f32 | Kp: f32 | Ki: f32 | Kd: f32 | Kaw: f32 |
                #      u: u16 | u_sat: u16 | u_p: f32 | u_i: f32 | u_d: f32 | max: u16 | min: u16    
                all_data.append(int2(get_uint16(data)))
                data = data[2:]
                all_data.append(get_float(int2(get_uint32(data))))
                data = data[4:]
                all_data.append(get_float(int2(get_uint32(data))))
                data = data[4:]
                all_data.append(get_float(int2(get_uint32(data))))
                data = data[4:]
                all_data.append(get_float(int2(get_uint32(data))))
                data = data[4:]
                all_data.append(get_float(int2(get_uint32(data))))
                data = data[4:]
                all_data.append(get_float(int2(get_uint32(data))))
                data = data[4:]
                all_data.append(get_float(int2(get_uint32(data))))
                data = data[4:]
                all_data.append(int2(get_uint16(data)))
                data = data[2:]
                all_data.append(int2(get_uint16(data)))
                data = data[2:]
                all_data.append(get_float(int2(get_uint32(data))))
                data = data[4:]
                all_data.append(get_float(int2(get_uint32(data))))
                data = data[4:]
                all_data.append(get_float(int2(get_uint32(data))))
                data = data[4:]
                all_data.append(int2(get_uint16(data)))
                data = data[2:]
                all_data.append(int2(get_uint16(data)))
                data = data[2:]
                """
                    HEATER
                """
                # Bang-Bang: cmd: u8 | set_value: u16 | threshold_top: u16 | threshold_bottom: u16 | u_max: u16 | u_min: u16
                all_data.append(int2(get_uint8(data[0])))
                data = data[1:]
                all_data.append(int2(get_uint16(data)))
                data = data[2:]
                all_data.append(int2(get_uint16(data)))
                data = data[2:]
                all_data.append(int2(get_uint16(data)))
                data = data[2:]
                all_data.append(int2(get_uint16(data)))
                data = data[2:]
                all_data.append(int2(get_uint16(data)))
                data = data[2:]
                # PID: set_value: u16 | error: f32 | int_sum: f32 | aw_int_sum: f32 | Kp: f32 | Ki: f32 | Kd: f32 | Kaw: f32 |
                #      u: u16 | u_sat: u16 | u_p: f32 | u_i: f32 | u_d: f32 | max: u16 | min: u16    
                all_data.append(int2(get_uint16(data)))
                data = data[2:]
                all_data.append(get_float(int2(get_uint32(data))))
                data = data[4:]
                all_data.append(get_float(int2(get_uint32(data))))
                data = data[4:]
                all_data.append(get_float(int2(get_uint32(data))))
                data = data[4:]
                all_data.append(get_float(int2(get_uint32(data))))
                data = data[4:]
                all_data.append(get_float(int2(get_uint32(data))))
                data = data[4:]
                all_data.append(get_float(int2(get_uint32(data))))
                data = data[4:]
                all_data.append(get_float(int2(get_uint32(data))))
                data = data[4:]
                all_data.append(int2(get_uint16(data)))
                data = data[2:]
                all_data.append(int2(get_uint16(data)))
                data = data[2:]
                all_data.append(get_float(int2(get_uint32(data))))
                data = data[4:]
                all_data.append(get_float(int2(get_uint32(data))))
                data = data[4:]
                all_data.append(get_float(int2(get_uint32(data))))
                data = data[4:]
                all_data.append(int2(get_uint16(data)))
                data = data[2:]
                all_data.append(int2(get_uint16(data)))
                data = data[2:]
            else:
                # [FAST]
                """
                    FAN
                """
                # Bang-Bang: cmd: u8
                fast_data.append(int2(get_uint8(data[0])))
                data = data[1:]
                # PID      : error: f32 | int_sum: f32 | aw_int_sum: f32 | u: u16 | u_sat: u16 | u_p: f32 | u_i: f32 | u_d: f32   
                fast_data.append(get_float(int2(get_uint32(data))))
                data = data[4:]
                fast_data.append(get_float(int2(get_uint32(data))))
                data = data[4:]
                fast_data.append(get_float(int2(get_uint32(data))))
                data = data[4:]
                fast_data.append(int2(get_uint16(data)))
                data = data[2:]
                fast_data.append(int2(get_uint16(data)))
                data = data[2:]
                fast_data.append(get_float(int2(get_uint32(data))))
                data = data[4:]
                fast_data.append(get_float(int2(get_uint32(data))))
                data = data[4:]
                fast_data.append(get_float(int2(get_uint32(data))))
                data = data[4:]
                """
                    HEATER
                """
                # Bang-Bang: cmd: u8
                fast_data.append(int2(get_uint8(data[0])))
                data = data[1:]
                # PID      : error: f32 | int_sum: f32 | aw_int_sum: f32 | u: u16 | u_sat: u16 | u_p: f32 | u_i: f32 | u_d: f32   
                fast_data.append(get_float(int2(get_uint32(data))))
                data = data[4:]
                fast_data.append(get_float(int2(get_uint32(data))))
                data = data[4:]
                fast_data.append(get_float(int2(get_uint32(data))))
                data = data[4:]
                fast_data.append(int2(get_uint16(data)))
                data = data[2:]
                fast_data.append(int2(get_uint16(data)))
                data = data[2:]
                fast_data.append(get_float(int2(get_uint32(data))))
                data = data[4:]
                fast_data.append(get_float(int2(get_uint32(data))))
                data = data[4:]
                fast_data.append(get_float(int2(get_uint32(data))))
                data = data[4:]

            """
                speed: u16 | temp_top: u16 | temp_bottom: u16
            """
            # Get speed
            speed = int2(get_uint16(data))
            data = data[2:]
            # Get temperatures
            temp_top = int2(get_uint16(data))
            data = data[2:]
            temp_bottom = int2(get_uint16(data))
            data = data[2:]

            if isAllData:
                all_data.append(speed)
                all_data.append(temp_top)
                all_data.append(temp_bottom)
                all_data.append(isFanOn)
                all_data.append(isHeaterOn)
                all_data.append(timestamp)
                self.handler.COM.handle_all_data(all_data)
            else:
                fast_data.append(speed)
                fast_data.append(temp_top)
                fast_data.append(temp_bottom)
                fast_data.append(isFanOn)
                fast_data.append(isHeaterOn)
                fast_data.append(timestamp)
                self.handler.COM.handle_fast_data(fast_data)
        except:
            pass


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

# This Python file uses the following encoding: utf-8
from PySide6.QtCore import QIODeviceBase, Slot, QByteArray
from PySide6.QtSerialPort import QSerialPort, QSerialPortInfo
from utilities import error_dialog, get_uint8, get_uint16, get_uint32, get_float, int2

BLANK_STRING = "N/A"
DEBUG = True
DEV_CON_ACK = "00000001"
MSG_DEVICE_TYPE = 0
MSG_ALL_FAST = 1
MSG_ON_OFF = 2
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
        data = self._serial.readAll().data()
        header = get_uint8(data[0])[::-1]
        data = data[1:]
        if header == DEV_CON_ACK:
            # Handle successful connection
            self.ui.btnConnect.setText("Disconnect")
            self.ui.btnConnect.setStatusTip("Rozłącz się z urządzeniem")
        else:
            """
            0/1
            Byte 0   : 0: FAN/COIL | 1: ALL/FAST | 2: OFF/ON | 3: TEMP_REF_TOP/TEP_REF_BOTTOM | 4: COIL_REF_TOP/COIL_REF_BOTTOM | 5: NA| 6: NA| 7: NA|
            Byte 1-4 : timestamp
            """
            # Handle header
            isFanData = header[MSG_DEVICE_TYPE] == '0'
            isAllData = header[MSG_ALL_FAST] == '0'
            isOn = header[MSG_ON_OFF] == '1'
            refTemp = header[MSG_TEMP_REF]
            refCoil = header[MSG_COIL_REF]
            # Handle data
            timestamp = int2(get_uint32(data))
            data = data[4:]
            if isAllData:
                # Bang-Bang: cmd: u8 | set_value: u16 | threshold_top: u16 | threshold_bottom: u16 | u_max: u16 | u_min: u16
                bb_cmd = int2(get_uint8(data[0]))
                data[1:]
                bb_set_val = int2(get_uint16(data))
                data = data[2:]
                bb_threshold_top = int2(get_uint16(data))
                data = data[2:]
                bb_threshold_bottom = int2(get_uint16(data))
                data = data[2:]
                bb_u_max = int2(get_uint16(data))
                data = data[2:]
                bb_u_min = int2(get_uint16(data))
                data = data[2:]
                # PID: set_value: u16 | error: f32 | int_sum: f32 | aw_int_sum: f32 | Kp: f32 | Ki: f32 | Kd: f32 | Kaw: f32 |
                #      u: u16 | u_sat: u16 | u_p: f32 | u_i: f32 | u_d: f32 | max: u16 | min: u16    
                pid_set_val = int2(get_uint16(data))
                data = data[2:]
                pid_error = get_float(int2(get_uint32(data)))
                data = data[4:]
                pid_int_sum = get_float(int2(get_uint32(data)))
                data = data[4:]
                pid_aw_int_sum = get_float(int2(get_uint32(data)))
                data = data[4:]
                pid_k_p = get_float(int2(get_uint32(data)))
                data = data[4:]
                pid_k_i = get_float(int2(get_uint32(data)))
                data = data[4:]
                pid_k_d = get_float(int2(get_uint32(data)))
                data = data[4:]
                pid_k_aw = get_float(int2(get_uint32(data)))
                data = data[4:]
                pid_u = int2(get_uint16(data))
                data = data[2:]
                pid_u_sat = int2(get_uint16(data))
                data = data[2:]
                pid_u_p = get_float(int2(get_uint32(data)))
                data = data[4:]
                pid_u_i = get_float(int2(get_uint32(data)))
                data = data[4:]
                pid_u_d = get_float(int2(get_uint32(data)))
                data = data[4:]
                pid_max = int2(get_uint16(data))
                data = data[2:]
                pid_min = int2(get_uint16(data))
                data = data[2:]
            else:
                # [FAST]
                # Bang-Bang: cmd: u8
                bb_cmd = int2(get_uint8(data))
                data[1:]
                # PID      : error: f32 | int_sum: f32 | aw_int_sum: f32 | u: u16 | u_sat: u16 | u_p: f32 | u_i: f32 | u_d: f32   
                pid_error = get_float(int2(get_uint32(data)))
                data = data[4:]
                pid_int_sum = get_float(int2(get_uint32(data)))
                data = data[4:]
                pid_aw_int_sum = get_float(int2(get_uint32(data)))
                data = data[4:]
                pid_u = int2(get_uint16(data))
                data = data[2:]
                pid_u_sat = int2(get_uint16(data))
                data = data[2:]
                pid_u_p = get_float(int2(get_uint32(data)))
                data = data[4:]
                pid_u_i = get_float(int2(get_uint32(data)))
                data = data[4:]
                pid_u_d = get_float(int2(get_uint32(data)))
                data = data[4:]

            """
            if [FAN] # 
                speed: u16
            if [COIL]#
                temp_top: u16 | temp_bottom: u16
            """
            if isFanData:
                # Get speed
                speed = int2(get_uint16(data))
                data = data[2:]
                if isAllData:
                    self.handler.COM.handle_all_fan_data(
                        [
                            bb_set_val,
                            bb_threshold_top,
                            bb_threshold_bottom,
                            bb_u_max,
                            bb_u_min,
                            bb_cmd,
                            pid_set_val,
                            pid_error,
                            pid_int_sum,
                            pid_aw_int_sum,
                            pid_k_p,
                            pid_k_i,
                            pid_k_d,
                            pid_k_aw,
                            pid_u,
                            pid_u_sat,
                            pid_u_p,
                            pid_u_i,
                            pid_u_d,
                            pid_max,
                            pid_min,
                            speed,
                            isOn,
                        ]
                    )
                else:
                    self.handler.COM.handle_fast_fan_data(
                        [
                            bb_cmd,
                            pid_error,
                            pid_int_sum,
                            pid_aw_int_sum,
                            pid_u,
                            pid_u_sat,
                            pid_u_p,
                            pid_u_i,
                            pid_u_d,
                            speed,
                            isOn,
                        ]
                    )
            else:
                # Get temperatures
                temp_top = int2(get_uint16(data))
                data = data[2:]
                temp_bottom = int2(get_uint16(data))
                data = data[2:]
                if isAllData:
                    self.handler.COM.handle_all_heater_data(
                        [
                            bb_set_val,
                            bb_threshold_top,
                            bb_threshold_bottom,
                            bb_u_max,
                            bb_u_min,
                            bb_cmd,
                            pid_set_val,
                            pid_error,
                            pid_int_sum,
                            pid_aw_int_sum,
                            pid_k_p,
                            pid_k_i,
                            pid_k_d,
                            pid_k_aw,
                            pid_u,
                            pid_u_sat,
                            pid_u_p,
                            pid_u_i,
                            pid_u_d,
                            pid_max,
                            pid_min,
                            temp_top,
                            temp_bottom,
                            isOn,
                        ]
                    )
                else:
                    self.handler.COM.handle_fast_heater_data(
                        [
                            bb_cmd,
                            pid_error,
                            pid_int_sum,
                            pid_aw_int_sum,
                            pid_u,
                            pid_u_sat,
                            pid_u_p,
                            pid_u_i,
                            pid_u_d,
                            temp_top,
                            temp_bottom,
                            isOn,
                        ]
                    )
                
        
        
        
        
        
        
        
        
        
        
        
        """
        if 'DEV_CON_ACK' in data:
            # Handle successful connection
            idx = data.index('DEV_CON_ACK')
            data = data[:idx] + data[idx+len('DEV_CON_ACK'):]
            self.ui.btnConnect.setText("Disconnect")
            self.ui.btnConnect.setStatusTip("Rozłącz się z urządzeniem")
        if ('ALLFAN_' in data) or ('ALLCOIL_' in data):
            data = data.split('\n')
            for packet in data:
                if 'ALLFAN_' in packet:
                    self.handler.COM.handle_all_fan_data(packet)
                if 'ALLCOIL_' in packet:
                    self.handler.COM.handle_all_heater_data(packet)"""

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

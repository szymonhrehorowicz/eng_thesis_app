# This Python file uses the following encoding: utf-8
from PySide6.QtCore import QByteArray, Slot

MSG_TYPE = {
    "APP_CON_REQ": 0,
    "FAN_CONF_MSG": 1,
    "COIL_CONF_MSG": 2,
    "FAN_DATA_MSG": 3,
    "COIL_DATA_MSG": 4,
}

CONTROL_MSG = {
    "SET_FAN_CONFIG": 39,
    "SET_HEATER_CONFIG": 40,
}

FAN_ALL_DATA = {
    "BB_SET_VALUE": 0,
    "BB_THRESHOLD_TOP": 1,
    "BB_THRESHOLD_BOTTOM": 2,
    "BB_U_MAX": 3,
    "BB_U_MIN": 4,
    "BB_CMD": 5,
    "PID_SET_VALUE": 6,
    "PID_ERROR": 7,
    "PID_INT_ERROR": 8,
    "PID_AW_INT_ERROR": 9,
    "PID_KP": 10,
    "PID_KI": 11,
    "PID_KD": 12,
    "PID_KAW": 13,
    "PID_U": 14,
    "PID_U_SATURATED": 15,
    "PID_U_P": 16,
    "PID_U_I": 17,
    "PID_U_D": 18,
    "PID_MAX": 19,
    "PID_MIN": 20,
    "PID_SPEED": 21,
    "PID_MODE": 22,
}

FAN_FAST_DATA = {
    "BB_CMD": 0,
    "PID_ERROR": 1,
    "PID_INT_ERROR": 2,
    "PID_AW_INT_ERROR": 3,
    "PID_U": 4,
    "PID_U_SATURATED": 5,
    "PID_U_P": 6,
    "PID_U_I": 7,
    "PID_U_D": 8,
    "PID_SPEED": 9,
    "PID_MODE": 10,
}

HEATER_ALL_DATA = {
    "BB_SET_VALUE": 0,
    "BB_THRESHOLD_TOP": 1,
    "BB_THRESHOLD_BOTTOM": 2,
    "BB_U_MAX": 3,
    "BB_U_MIN": 4,
    "BB_CMD": 5,
    "PID_SET_VALUE": 6,
    "PID_ERROR": 7,
    "PID_INT_ERROR": 8,
    "PID_AW_INT_ERROR": 9,
    "PID_KP": 10,
    "PID_KI": 11,
    "PID_KD": 12,
    "PID_KAW": 13,
    "PID_U": 14,
    "PID_U_SATURATED": 15,
    "PID_U_P": 16,
    "PID_U_I": 17,
    "PID_U_D": 18,
    "PID_MAX": 19,
    "PID_MIN": 20,
    "PID_TEMP_LEFT": 21,
    "PID_TEMP_RIGHT": 22,
    "PID_MODE": 23,
}

HEATER_FAST_DATA = {
    "BB_CMD": 0,
    "PID_ERROR": 1,
    "PID_INT_ERROR": 2,
    "PID_AW_INT_ERROR": 3,
    "PID_U": 4,
    "PID_U_SATURATED": 5,
    "PID_U_P": 6,
    "PID_U_I": 7,
    "PID_U_D": 8,
    "PID_TEMP_LEFT": 21,
    "PID_TEMP_RIGHT": 22,
    "PID_MODE": 10,
}

class COM:
    def __init__(self, handler):
        self.handler = handler

    # FAN SETTERS
    @Slot(bool)
    def set_fan_config(self, isOn: bool):
        if isOn:
            self.handler.ui.btnFanStart.setText("STOP")
        else:
            self.handler.ui.btnFanStart.setText("START")
        msg = ""
        msg += str(MSG_TYPE["FAN_CONF_MSG"])
        msg += str(CONTROL_MSG["SET_FAN_CONFIG"])
        # Controller type: 0-PID | 1-BANG BANG
        msg += "0" if self.handler.ui.btnFanControllerSetPID.isChecked() else "1"
        # BB set value: 0000 - 6000
        msg += str(self.handler.ui.inFanBBSetValue.value()).zfill(4)
        # BB hysteresis: 0000 - 6000
        msg += str(self.handler.ui.inFanBBHysteresis.value()).zfill(4)
        # PID set value: 0000 - 6000
        msg += str(self.handler.ui.inFanPIDSetValue.value()).zfill(4)
        # PID Kp: 000.00 - 100.00
        Kp = self.handler.ui.inFanPID_Kp.value()
        Kp = "%.2f"%(Kp)
        for _ in range(0, 6 - len(Kp)):
            Kp = '0' + Kp
        msg += Kp
        # PID Ki: 000.00 - 100.00
        Ki = self.handler.ui.inFanPID_Ki.value()
        Ki = "%.2f"%(Ki)
        for _ in range(0, 6 - len(Ki)):
            Ki = '0' + Ki
        msg += Ki
        # PID Kd: 000.00 - 100.00
        Kd = self.handler.ui.inFanPID_Kd.value()
        Kd = "%.2f"%(Kd)
        for _ in range(0, 6 - len(Kd)):
            Kd = '0' + Kd
        msg += Kd
        # PID Kaw: 000.00 - 100.00
        Kaw = self.handler.ui.inFanPID_Kaw.value()
        Kaw = "%.2f"%(Kaw)
        for _ in range(0, 6 - len(Kaw)):
            Kaw = '0' + Kaw
        msg += Kaw
        # ON/OFF : 0 - OFF | 1 - ON
        msg += '1' if isOn else '0'
        self.handler.serial.write_data(QByteArray(msg))

    # HEATER SETTERS
    @Slot(bool)
    def set_heater_config(self, isOn: bool):
        if isOn:
            self.handler.ui.btnHeaterStart.setText("STOP")
        else:
            self.handler.ui.btnHeaterStart.setText("START")
        msg = ""
        msg += str(MSG_TYPE["FAN_CONF_MSG"])
        msg += str(CONTROL_MSG["SET_FAN_CONFIG"])
        # Controller type: 0-PID | 1-BANG BANG
        msg += "0" if self.handler.ui.btnFanControllerSetPID.isChecked() else "1"
        # BB set value: 0000 - 6000
        msg += str(self.handler.ui.inFanBBSetValue.value()).zfill(4)
        # BB hysteresis: 0000 - 6000
        msg += str(self.handler.ui.inFanBBHysteresis.value()).zfill(4)
        # PID set value: 0000 - 6000
        msg += str(self.handler.ui.inFanPIDSetValue.value()).zfill(4)
        # PID Kp: 000.00 - 100.00
        Kp = self.handler.ui.inFanPID_Kp.value()
        Kp = "%.2f"%(Kp)
        for _ in range(0, 6 - len(Kp)):
            Kp = '0' + Kp
        msg += Kp
        # PID Ki: 000.00 - 100.00
        Ki = self.handler.ui.inFanPID_Ki.value()
        Ki = "%.2f"%(Ki)
        for _ in range(0, 6 - len(Ki)):
            Ki = '0' + Ki
        msg += Ki
        # PID Kd: 000.00 - 100.00
        Kd = self.handler.ui.inFanPID_Kd.value()
        Kd = "%.2f"%(Kd)
        for _ in range(0, 6 - len(Kd)):
            Kd = '0' + Kd
        msg += Kd
        # PID Kaw: 000.00 - 100.00
        Kaw = self.handler.ui.inFanPID_Kaw.value()
        Kaw = "%.2f"%(Kaw)
        for _ in range(0, 6 - len(Kaw)):
            Kaw = '0' + Kaw
        msg += Kaw
        # ON/OFF : 0 - OFF | 1 - ON
        msg += '1' if isOn else '0'
        # 17/33R : 0 - COIL_B | 1 - COIL_A
        msg += '0' if self.handler.ui.btnHeaterControllerSetHighPower.isChecked() else '1'
        # LEFT/RIGHT: 
        msg += '0' if self.handler.ui.btnHeaterControllerSetLeftCoil.isChecked() else '1'
        # POWER: 000 - 100
        msg += str(self.handler.ui.inHeaterBBPower.value()).zfill(3)
        self.handler.serial.write_data(QByteArray(msg))

    # FAN GETTERS
    def handle_all_fan_data(self, data):
        data = data.split('_')[1:]
        self.handler.fanController.update_all({
            "BB_SET_VALUE": int(data[0]),
            "BB_THRESHOLD_TOP": int(data[1]),
            "BB_THRESHOLD_BOTTOM": int(data[2]),
            "BB_U_MAX": int(data[3]),
            "BB_U_MIN": int(data[4]),
            "BB_CMD": int(data[5]),
            "PID_SET_VALUE": int(data[6]),
            "PID_ERROR": float(data[7]),
            "PID_INT_ERROR": float(data[8]),
            "PID_AW_INT_ERROR": float(data[9]),
            "PID_KP": float(data[10]),
            "PID_KI": float(data[11]),
            "PID_KD": float(data[12]),
            "PID_KAW": float(data[13]),
            "PID_U": int(data[14]),
            "PID_U_SATURATED": int(data[15]),
            "PID_U_P": float(data[16]),
            "PID_U_I": float(data[17]),
            "PID_U_D": float(data[18]),
            "PID_MAX": int(data[19]),
            "PID_MIN": int(data[20]),
            "PID_SPEED": int(data[21]),
            "PID_MODE": int(data[22]),
        })

    def handle_fast_fan_data(self, data):
        data = data.split('_')[1:]
        self.handler.fanController.update_fast({
            "BB_CMD": int(data[0]),
            "PID_ERROR": float(data[1]),
            "PID_INT_ERROR": float(data[2]),
            "PID_AW_INT_ERROR": float(data[3]),
            "PID_U": int(data[4]),
            "PID_U_SATURATED": int(data[5]),
            "PID_U_P": float(data[6]),
            "PID_U_I": float(data[7]),
            "PID_U_D": float(data[8]),
            "PID_SPEED": int(data[9]),
            "PID_MODE": int(data[10]),
        })

    # HEATER GETTERS
    def handle_all_heater_data(self, data):
        data = data.split('_')[1:]
        self.handler.heaterController.update_all({
            "BB_SET_VALUE": int(data[0]),
            "BB_THRESHOLD_TOP": int(data[1]),
            "BB_THRESHOLD_BOTTOM": int(data[2]),
            "BB_U_MAX": int(data[3]),
            "BB_U_MIN": int(data[4]),
            "BB_CMD": int(data[5]),
            "PID_SET_VALUE": int(data[6]),
            "PID_ERROR": float(data[7]),
            "PID_INT_ERROR": float(data[8]),
            "PID_AW_INT_ERROR": float(data[9]),
            "PID_KP": float(data[10]),
            "PID_KI": float(data[11]),
            "PID_KD": float(data[12]),
            "PID_KAW": float(data[13]),
            "PID_U": int(data[14]),
            "PID_U_SATURATED": int(data[15]),
            "PID_U_P": float(data[16]),
            "PID_U_I": float(data[17]),
            "PID_U_D": float(data[18]),
            "PID_MAX": int(data[19]),
            "PID_MIN": int(data[20]),
            "PID_TEMP_LEFT": int(data[21]),
            "PID_TEMP_RIGHT": int(data[22]),
            "PID_MODE": int(data[23]),
        })
    
    def handle_fast_heater_data(self, data):
        data = data.split('_')[1:]
        self.handler.heaterController.update_fast({
            "BB_CMD": int(data[0]),
            "PID_ERROR": float(data[1]),
            "PID_INT_ERROR": float(data[2]),
            "PID_AW_INT_ERROR": float(data[3]),
            "PID_U": int(data[4]),
            "PID_U_SATURATED": int(data[5]),
            "PID_U_P": float(data[6]),
            "PID_U_I": float(data[7]),
            "PID_U_D": float(data[8]),
            "PID_TEMP_LEFT": int(data[9]),
            "PID_TEMP_RIGHT": int(data[10]),
            "PID_MODE": int(data[11]),
        }) 

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

ALL_DATA = {
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

FAST_DATA = {
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

class COM:
    def __init__(self, handler):
        self.handler = handler

    # FAN SETTERS
    @Slot(bool)
    def set_fan_config(self, isOn: bool):
        if isOn:
            self.handler.ui.btnFanStart.setText("STOP")
            self.handler.ui.btn_graph_Clear.setEnabled(False)
            # reset graphs size
            self.handler.fanBBgraph.home()
            self.handler.fanPIDgraph.home()
            # if graphs stopped, unstop them
            if self.handler.ui.btn_graph_Stop.isChecked():
                self.handler.ui.btn_graph_Stop.click()
        else:
            self.handler.ui.btnFanStart.setText("START")
            if not self.handler.ui.btnHeaterStart.isChecked():
                self.handler.ui.btn_graph_Clear.setEnabled(True)
            # if graphs stopped, unstop them
            # if self.handler.ui.btn_graph_Stop.isChecked():
            #     self.handler.ui.btn_graph_Stop.click()
        msg = ""
        msg += str(MSG_TYPE["FAN_CONF_MSG"])
        msg += str(CONTROL_MSG["SET_FAN_CONFIG"])
        # Controller type: 0-PID | 1-BANG BANG
        msg += "0" if self.handler.ui.btnFanControllerSetPID.isChecked() else "1"
        # BB set value: 0000 - 6000
        msg += str(self.handler.ui.inFanSetValue.value()).zfill(4)
        # BB hysteresis: 0000 - 6000
        msg += str(self.handler.ui.inFanBBHysteresis.value()).zfill(4)
        # PID set value: 0000 - 6000
        msg += str(self.handler.ui.inFanSetValue.value()).zfill(4)
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
        # REFERENCE TYPE
        isStep = self.handler.ui.btnFanRefStep.isChecked()
        isRamp = self.handler.ui.btnFanRefRamp.isChecked()
        msg += '0' if isStep else ('1' if isRamp else '2')
        # REFERENCE SLOPE
        msg += str(self.handler.ui.inFanRefSlope.value()).zfill(4)
        # REFERENCE AMPLITUDE
        msg += str(self.handler.ui.inFanRefAmplitude.value()).zfill(4)
        # REFERENCE OMEGA
        omega = self.handler.ui.inFanRefOmega.value()
        omega = "%.2f"%(omega)
        for _ in range(0, 6 - len(omega)):
            omega = '0' + omega
        msg += omega

        msg += '\n'
        self.handler.serial.write_data(QByteArray(msg))
        print(msg)

    # HEATER SETTERS
    @Slot(bool)
    def set_heater_config(self, isOn: bool):
        if isOn:
            self.handler.ui.btnHeaterStart.setText("STOP")
            self.handler.ui.btn_graph_Clear.setEnabled(False)
            # reset graphs size
            self.handler.heaterBBgraph.home()
            self.handler.heaterPIDgraph.home()
            # if graphs stopped, unstop them
            if self.handler.ui.btn_graph_Stop.isChecked():
                self.handler.ui.btn_graph_Stop.click()
        else:
            self.handler.ui.btnHeaterStart.setText("START")
            if not self.handler.ui.btnFanStart.isChecked():
                self.handler.ui.btn_graph_Clear.setEnabled(True)
            # if graphs stopped, unstop them
            # if self.handler.ui.btn_graph_Stop.isChecked():
            #     self.handler.ui.btn_graph_Stop.click()
        msg = ""
        msg += str(MSG_TYPE["COIL_CONF_MSG"])
        msg += str(CONTROL_MSG["SET_HEATER_CONFIG"])
        # Controller type: 0-PID | 1-BANG BANG
        msg += "0" if self.handler.ui.btnHeaterControllerSetPID.isChecked() else "1"
        # BB set value: 0000 - 6000
        msg += str(self.handler.ui.inHeaterSetValue.value()).zfill(4)
        # BB hysteresis: 0000 - 6000
        msg += str(self.handler.ui.inHeaterBBHysteresis.value()).zfill(4)
        # PID set value: 0000 - 6000
        msg += str(self.handler.ui.inHeaterSetValue.value()).zfill(4)
        # PID Kp: 000.00 - 100.00
        Kp = self.handler.ui.inHeaterPID_Kp.value()
        Kp = "%.2f"%(Kp)
        for _ in range(0, 6 - len(Kp)):
            Kp = '0' + Kp
        msg += Kp
        # PID Ki: 000.00 - 100.00
        Ki = self.handler.ui.inHeaterPID_Ki.value()
        Ki = "%.2f"%(Ki)
        for _ in range(0, 6 - len(Ki)):
            Ki = '0' + Ki
        msg += Ki
        # PID Kd: 000.00 - 100.00
        Kd = self.handler.ui.inHeaterPID_Kd.value()
        Kd = "%.2f"%(Kd)
        for _ in range(0, 6 - len(Kd)):
            Kd = '0' + Kd
        msg += Kd
        # PID Kaw: 000.00 - 100.00
        Kaw = self.handler.ui.inHeaterPID_Kaw.value()
        Kaw = "%.2f"%(Kaw)
        for _ in range(0, 6 - len(Kaw)):
            Kaw = '0' + Kaw
        msg += Kaw
        # ON/OFF : 0 - OFF | 1 - ON | 2 - COMBINED
        if self.handler.ui.chxFanCooling.isChecked() and isOn:
            msg += '2'
        else:
            msg += '1' if isOn else '0'
        # REFERENCE TYPE
        isStep = self.handler.ui.btnHeaterRefStep.isChecked()
        isRamp = self.handler.ui.btnHeaterRefRamp.isChecked()
        msg += '0' if isStep else ('1' if isRamp else '2')
        # REFERENCE SLOPE
        msg += str(self.handler.ui.inHeaterRefSlope.value()).zfill(4)
        # REFERENCE AMPLITUDE
        msg += str(self.handler.ui.inHeaterRefAmplitude.value()).zfill(4)
        # REFERENCE OMEGA
        omega = self.handler.ui.inHeaterRefOmega.value()
        omega = "%.2f"%(omega)
        for _ in range(0, 6 - len(omega)):
            omega = '0' + omega
        msg += omega
        # 17/33R : 0 - COIL_B | 1 - COIL_A
        msg += '1' if self.handler.ui.btnHeaterControllerSetHighPower.isChecked() else '0'
        # LEFT/RIGHT: 
        msg += '1' if self.handler.ui.btnHeaterControllerSetLeftCoil.isChecked() else '0'
        # POWER: 000 - 100
        msg += str(self.handler.ui.inHeaterBBPower.value()).zfill(3)

        msg += '\n'
        self.handler.serial.write_data(QByteArray(msg))
        print(msg)

    def handle_all_data(self, data):
        # LCD DISPLAYS
        ## BB
        self.handler.ui.lcdFanBB_y.display(data[40])
        self.handler.ui.lcdFanBB_x.display(data[0])
        self.handler.ui.lcdFanBB_x_max.display(data[3])
        self.handler.ui.lcdFanBB_x_min.display(data[4])
        self.handler.ui.lcdFanBB_u_max.display(data[5])
        self.handler.ui.lcdFanBB_u_min.display(data[6])
        self.handler.ui.lcdFanBB_mode.display(data[2])
        
        self.handler.ui.lcdHeaterBB_y_1.display(data[41])
        self.handler.ui.lcdHeaterBB_y_2.display(data[42])
        self.handler.ui.lcdHeaterBB_x.display(data[20])
        self.handler.ui.lcdHeaterBB_x_max.display(data[23])
        self.handler.ui.lcdHeaterBB_x_min.display(data[24])
        self.handler.ui.lcdHeaterBB_u_max.display(data[25])
        self.handler.ui.lcdHeaterBB_u_min.display(data[26])
        self.handler.ui.lcdHeaterBB_mode.display(data[22])
        ## PID
        self.handler.ui.lcdFanPID_y.display(data[40])
        self.handler.ui.lcdFanPID_x.display(data[0])
        self.handler.ui.lcdFanPID_e.display(data[1])
        self.handler.ui.lcdFanPID_int_e.display(data[7])
        self.handler.ui.lcdFanPID_aw_int_e.display(data[8])
        self.handler.ui.lcdFanPID_u.display(data[13])
        self.handler.ui.lcdFanPID_u_sat.display(data[14])
        self.handler.ui.lcdFanPID_u_p.display(data[15])
        self.handler.ui.lcdFanPID_u_i.display(data[16])
        self.handler.ui.lcdFanPID_u_d.display(data[17])
        self.handler.ui.lcdFanPID_u_max.display(data[18])
        self.handler.ui.lcdFanPID_u_min.display(data[19])
        self.handler.ui.lcdFanPID_mode.display(data[43])

        self.handler.ui.lcdHeaterPID_y_1.display(data[41])
        self.handler.ui.lcdHeaterPID_y_2.display(data[42])
        self.handler.ui.lcdHeaterPID_x.display(data[20])
        self.handler.ui.lcdHeaterPID_e.display(data[21])
        self.handler.ui.lcdHeaterPID_int_e.display(data[27])
        self.handler.ui.lcdHeaterPID_aw_int_e.display(data[28])
        self.handler.ui.lcdHeaterPID_u.display(data[33])
        self.handler.ui.lcdHeaterPID_u_sat.display(data[34])
        self.handler.ui.lcdHeaterPID_u_p.display(data[35])
        self.handler.ui.lcdHeaterPID_u_i.display(data[36])
        self.handler.ui.lcdHeaterPID_u_d.display(data[37])
        self.handler.ui.lcdHeaterPID_u_max.display(data[38])
        self.handler.ui.lcdHeaterPID_u_min.display(data[39])
        self.handler.ui.lcdHeaterPID_mode.display(data[44])

        if(not self.handler.areGraphsRunning):
                return

        self.handler.fanController.update_all({
            # COMMON
            "SET_VALUE": data[0],
            "ERROR": data[1],
            # BB
            "BB_CMD": data[2],
            "BB_THRESHOLD_TOP": data[3],
            "BB_THRESHOLD_BOTTOM": data[4],
            "BB_U_MAX": data[5],
            "BB_U_MIN": data[6],
            # PID
            "PID_INT_ERROR": data[7],
            "PID_AW_INT_ERROR": data[8],
            "PID_KP": data[9],
            "PID_KI": data[10],
            "PID_KD": data[11],
            "PID_KAW": data[12],
            "PID_U": data[13],
            "PID_U_SATURATED": data[14],
            "PID_U_P": data[15],
            "PID_U_I": data[16],
            "PID_U_D": data[17],
            "PID_MAX": data[18],
            "PID_MIN": data[19],
            "PID_SPEED": data[40],
            "PID_MODE": data[43],
            # TIMESTAMP
            "TIMESTAMP": data[45],
        })
        self.handler.heaterController.update_all({
            # COMMON
            "SET_VALUE": data[20],
            "ERROR": data[21],
            # BB
            "BB_CMD": data[22],
            "BB_THRESHOLD_TOP": data[23],
            "BB_THRESHOLD_BOTTOM": data[24],
            "BB_U_MAX": data[25],
            "BB_U_MIN": data[26],
            # PID
            "PID_INT_ERROR": data[27],
            "PID_AW_INT_ERROR": data[28],
            "PID_KP": data[29],
            "PID_KI": data[30],
            "PID_KD": data[31],
            "PID_KAW": data[32],
            "PID_U": data[33],
            "PID_U_SATURATED": data[34],
            "PID_U_P": data[35],
            "PID_U_I": data[36],
            "PID_U_D": data[37],
            "PID_MAX": data[38],
            "PID_MIN": data[39],
            "PID_TEMP_LEFT": data[41],
            "PID_TEMP_RIGHT": data[42],
            "PID_MODE": data[44],
            # TIMESTAMP
            "TIMESTAMP": data[45],
        })


    def handle_fast_data(self, data):
        if(not self.handler.areGraphsRunning):
                return
        
        self.handler.fanController.update_fast({
            # BB
            "BB_CMD": data[0],
            # PID
            "PID_ERROR": data[1],
            "PID_INT_ERROR": data[2],
            "PID_AW_INT_ERROR": data[3],
            "PID_U": data[4],
            "PID_U_SATURATED": data[5],
            "PID_U_P": data[6],
            "PID_U_I": data[7],
            "PID_U_D": data[8],
            "PID_SPEED": data[18],
            "PID_MODE": data[21],
            # TIMESTAMP
            "TIMESTAMP": data[23],
        })
        self.handler.heaterController.update_fast({
            # BB
            "BB_CMD": data[9],
            # PID
            "PID_ERROR": data[10],
            "PID_INT_ERROR": data[11],
            "PID_AW_INT_ERROR": data[12],
            "PID_U": data[13],
            "PID_U_SATURATED": data[14],
            "PID_U_P": data[15],
            "PID_U_I": data[16],
            "PID_U_D": data[17],
            "PID_TEMP_LEFT": data[20],
            "PID_TEMP_RIGHT": data[21],
            "PID_MODE": data[22],
            # TIMESTAMP
            "TIMESTAMP": data[23],
        }) 

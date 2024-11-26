# This Python file uses the following encoding: utf-8
from PySide6.QtCore import Slot

class HeaterControlsHandler:
    R17POWER = 9
    R33POWER = 4.5

    def __init__(self, handler, pid, bb):
        self.ui = handler.ui
        self.equation = handler.heaterPIDequation
        self.PID = pid
        self.BB = bb
    
    def _update_equation(self):
        self.equation.update(self.PID.Kp, self.PID.Ki, self.PID.Kd, self.PID.Ti, self.PID.Td)

    # BB
    @Slot(float)
    def bb_setValue(self, value):
        self.BB.set_value = value

    @Slot(float)
    def bb_setHysteresis(self, value):
        self.BB.hysteresis = value

    @Slot(int)
    def bb_setPower(self, value):
        self.BB.power = value / 100 * (self.R17POWER if self.ui.btnHeaterControllerSetHighPower.isChecked() else self.R33POWER)
        power = str(self.BB.power)
        self.ui.lblPower.setText(power[:power.index('.') + 2])

    # PID
    @Slot(int)
    def pid_setValue(self, value):
        self.PID.set_value = value
        self._update_equation()

    @Slot(float)
    def pid_setKp(self, value):
        self.PID.Kp = value
        try:
            self.PID.Ti = self.PID.Kp / self.PID.Ki
        except ZeroDivisionError:
            self.PID.Ti = 0
        try:
            self.PID.Td = self.PID.Kd / self.PID.Kp
        except ZeroDivisionError:
            self.PID.Td = 0
        self.ui.inHeaterPID_Ti.setValue(self.PID.Ti)
        self.ui.inHeaterPID_Td.setValue(self.PID.Td)
        self._update_equation()

    @Slot(float)
    def pid_setKi(self, value):
        # Ti = Kp / Ki
        self.PID.Ki = value
        try:
            self.PID.Ti = self.PID.Kp / self.PID.Ki
        except ZeroDivisionError:
            self.PID.Ti = 0
        self.ui.inHeaterPID_Ti.setValue(self.PID.Ti)
        self._update_equation()

    @Slot(float)
    def pid_setKd(self, value):
        # Td = Kd / Kp
        self.PID.Kd = value
        try:
            self.PID.Td = self.PID.Kd / self.PID.Kp
        except ZeroDivisionError:
            self.PID.Td = 0
        self.ui.inHeaterPID_Td.setValue(self.PID.Td)
        self._update_equation()

    @Slot(float)
    def pid_setKaw(self, value):
        self.PID.Kaw = value

    @Slot(float)
    def pid_setTi(self, value):
        # Ki = Kp / Ti
        self.PID.Ti = value
        try:
            self.PID.Ki = self.PID.Kp / self.PID.Ti
        except ZeroDivisionError:
            self.PID.Ki = 0
        self.ui.inHeaterPID_Ki.setValue(self.PID.Ki)
        self._update_equation()

    @Slot(float)
    def pid_setTd(self, value):
        # Kd = Kp * Td
        self.PID.Td = value
        self.PID.Kd = self.PID.Kp * self.PID.Td
        self.ui.inHeaterPID_Kd.setValue(self.PID.Kd)
        self._update_equation()

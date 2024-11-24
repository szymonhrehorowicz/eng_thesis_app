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
    @Slot()
    def bb_setValue(self):
        self.BB.set_value = self.ui.inHeaterBBSetValue.value()

    @Slot()
    def bb_setHysteresis(self):
        self.BB.hysteresis = self.ui.inHeaterBBHysteresis.value()

    @Slot(int)
    def bb_setPower(self, value):
        self.BB.power = value / 100 * (self.R17POWER if self.ui.btnHeaterControllerSetHighPower.isChecked() else self.R33POWER)
        power = str(self.BB.power)
        self.ui.lblPower.setText(power[:power.index('.') + 2])

    # PID
    @Slot()
    def pid_setValue(self):
        self.PID.set_value = self.ui.inHeaterPIDSetValue.value()
        self._update_equation()

    @Slot()
    def pid_setKp(self):
        self.PID.Kp = self.ui.inHeaterPID_Kp.value()
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

    @Slot()
    def pid_setKi(self):
        # Ti = Kp / Ki
        self.PID.Ki = self.ui.inHeaterPID_Ki.value()
        try:
            self.PID.Ti = self.PID.Kp / self.PID.Ki
        except ZeroDivisionError:
            self.PID.Ti = 0
        self.ui.inHeaterPID_Ti.setValue(self.PID.Ti)
        self._update_equation()

    @Slot()
    def pid_setKd(self):
        # Td = Kd / Kp
        self.PID.Kd = self.ui.inHeaterPID_Kd.value()
        try:
            self.PID.Td = self.PID.Kd / self.PID.Kp
        except ZeroDivisionError:
            self.PID.Td = 0
        self.ui.inHeaterPID_Td.setValue(self.PID.Td)
        self._update_equation()

    @Slot()
    def pid_setKaw(self):
        self.PID.Kaw = self.ui.inHeaterPID_Kaw.value()

    @Slot()
    def pid_setTi(self):
        # Ki = Kp / Ti
        self.PID.Ti = self.ui.inHeaterPID_Ti.value()
        try:
            self.PID.Ki = self.PID.Kp / self.PID.Ti
        except ZeroDivisionError:
            self.PID.Ki = 0
        self.ui.inHeaterPID_Ki.setValue(self.PID.Ki)
        self._update_equation()

    @Slot()
    def pid_setTd(self):
        # Kd = Kp * Td
        self.PID.Td = self.ui.inHeaterPID_Td.value()
        self.PID.Kd = self.PID.Kp * self.PID.Td
        self.ui.inHeaterPID_Kd.setValue(self.PID.Kd)
        self._update_equation()

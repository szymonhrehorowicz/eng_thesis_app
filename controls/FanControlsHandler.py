# This Python file uses the following encoding: utf-8
from PySide6.QtCore import Slot

class FanControlsHandler:
    def __init__(self, handler, pid, bb):
        self.ui = handler.ui
        self.equation = handler.fanPIDequation
        self.PID = pid
        self.BB = bb

    def _update_equation(self) -> None:
        self.equation.update(self.PID.Kp, self.PID.Ki, self.PID.Kd, self.PID.Ti, self.PID.Td)

    @Slot()
    def change_equation_type(self):
        self.equation.set_equation_type()
        if self.equation.eq_type == "parallel":
            self.ui.btnEquationTypeFan.setText("równoległa")
            self.ui.frFanTi.hide()
            self.ui.frFanTd.hide()
            self.ui.frFanKi.show()
            self.ui.frFanKd.show()
        else:
            self.ui.btnEquationTypeFan.setText("akademicka")
            self.ui.frFanTi.show()
            self.ui.frFanTd.show()
            self.ui.frFanKi.hide()
            self.ui.frFanKd.hide()
        self.equation.update(self.PID.Kp, self.PID.Ki, self.PID.Kd, self.PID.Ti, self.PID.Td)

    @Slot()
    def set_value(self):
        self.PID.set_value = self.ui.inFanSetValue.value()
        self.BB.set_value = self.ui.inFanSetValue.value()
        self._update_equation()
    
    @Slot()
    def pwm(self, value):
        self.ui.lblFanPWM.setText(str(value))

    # BB
    @Slot()
    def bb_setValue(self):
        self.BB.set_value = self.ui.inFanBBSetValue.value()
        self.PID.set_value = self.ui.inFanBBSetValue.value()
        self.ui.inFanPIDSetValue.setValue(self.PID.set_value)

    @Slot()
    def bb_setHysteresis(self):
        self.BB.hysteresis = self.ui.inFanBBHysteresis.value()

    # PID
    @Slot()
    def pid_setValue(self):
        self.BB.set_value = self.ui.inFanBBSetValue.value()
        self.PID.set_value = self.ui.inFanBBSetValue.value()
        self.ui.inFanBBSetValue.setValue(self.PID.set_value)
        self._update_equation()

    @Slot()
    def pid_setKp(self):
        self.PID.Kp = self.ui.inFanPID_Kp.value()
        try:
            self.PID.Ti = self.PID.Kp / self.PID.Ki
        except ZeroDivisionError:
            self.PID.Ti = 0
        try:
            self.PID.Td = self.PID.Kd / self.PID.Kp
        except ZeroDivisionError:
            self.PID.Td = 0
        self.ui.inFanPID_Ti.setValue(self.PID.Ti)
        self.ui.inFanPID_Td.setValue(self.PID.Td)
        self._update_equation()

    @Slot()
    def pid_setKi(self):
        # Ti = Kp / Ki
        self.PID.Ki = self.ui.inFanPID_Ki.value()
        try:
            self.PID.Ti = self.PID.Kp / self.PID.Ki
        except ZeroDivisionError:
            self.PID.Ti = 0
        self.ui.inFanPID_Ti.setValue(self.PID.Ti)
        self._update_equation()

    @Slot()
    def pid_setKd(self):
        # Td = Kd / Kp
        self.PID.Kd = self.ui.inFanPID_Kd.value()
        try:
            self.PID.Td = self.PID.Kd / self.PID.Kp
        except ZeroDivisionError:
            self.PID.Td = 0
        self.ui.inFanPID_Td.setValue(self.PID.Td)
        self._update_equation()

    @Slot()
    def pid_setKaw(self):
        self.PID.Kaw = self.ui.inFanPID_Kaw.value()

    @Slot()
    def pid_setTi(self):
        # Ki = Kp / Ti
        self.PID.Ti = self.ui.inFanPID_Ti.value()
        try:
            self.PID.Ki = self.PID.Kp / self.PID.Ti
        except ZeroDivisionError:
            self.PID.Ki = 0
        self.ui.inFanPID_Ki.setValue(self.PID.Ki)
        self._update_equation()

    @Slot()
    def pid_setTd(self):
        # Kd = Kp * Td
        self.PID.Td = self.ui.inFanPID_Td.value()
        self.PID.Kd = self.PID.Kp * self.PID.Td
        self.ui.inFanPID_Kd.setValue(self.PID.Kd)
        self._update_equation()

    @Slot(bool)
    def setRefStep(self, value):
        self.ui.btnFanRefStep.setChecked(True)
        self.ui.btnFanRefRamp.setChecked(False)
        self.ui.btnFanRefSinewave.setChecked(False)

        self.ui.frFanRefSlope.setVisible(False)
        self.ui.frFanRefAmplitude.setVisible(False)
        self.ui.frFanRefOmega.setVisible(False)

    @Slot(bool)
    def setRefRamp(self, value):
        self.ui.btnFanRefStep.setChecked(False)
        self.ui.btnFanRefRamp.setChecked(True)
        self.ui.btnFanRefSinewave.setChecked(False)

        self.ui.frFanRefSlope.setVisible(True)
        self.ui.frFanRefAmplitude.setVisible(False)
        self.ui.frFanRefOmega.setVisible(False)

    @Slot(bool)
    def setRefSinewave(self, value):
        self.ui.btnFanRefStep.setChecked(False)
        self.ui.btnFanRefRamp.setChecked(False)
        self.ui.btnFanRefSinewave.setChecked(True)

        self.ui.frFanRefSlope.setVisible(False)
        self.ui.frFanRefAmplitude.setVisible(True)
        self.ui.frFanRefOmega.setVisible(True)

    @Slot(int)
    def setSlope(self, value):
        pass

    @Slot(int)
    def setAmplitude(self, value):
        pass

    @Slot(int)
    def setOmega(self, value):
        pass
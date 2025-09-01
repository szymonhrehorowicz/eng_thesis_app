# This Python file uses the following encoding: utf-8
from PySide6.QtCore import Slot, QCoreApplication

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
    
    @Slot()
    def change_equation_type(self):
        self.equation.set_equation_type()
        if self.equation.eq_type == "parallel":
            self.ui.btnEquationTypeHeater.setText(QCoreApplication.tr("równoległa"))
            self.ui.frHeaterTi.hide()
            self.ui.frHeaterTd.hide()
            self.ui.frHeaterKi.show()
            self.ui.frHeaterKd.show()
        else:
            self.ui.btnEquationTypeHeater.setText(QCoreApplication.tr("akademicka"))
            self.ui.frHeaterTi.show()
            self.ui.frHeaterTd.show()
            self.ui.frHeaterKi.hide()
            self.ui.frHeaterKd.hide()
        self.equation.update(self.PID.Kp, self.PID.Ki, self.PID.Kd, self.PID.Ti, self.PID.Td)

    @Slot()
    def set_value(self):
        self.PID.set_value = self.ui.inHeaterSetValue.value()
        self.BB.set_value = self.ui.inHeaterSetValue.value()
        self._update_equation()

    # BB
    @Slot()
    def bb_setHysteresis(self):
        self.BB.hysteresis = self.ui.inHeaterBBHysteresis.value()

    @Slot(int)
    def bb_setPower(self, value):
        is_high_power = self.ui.btnHeaterControllerSetHighPower.isChecked()
        coefficient = 0.5 if is_high_power else 1.0
        self.BB.power = value / 100.0 * 12 * coefficient
        power = str(self.BB.power)
        self.ui.lblPower.setText(power[:power.index('.') + 2])

    # PID
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

    @Slot(bool)
    def setRefStep(self, value):
        self.ui.btnHeaterRefStep.setChecked(True)
        self.ui.btnHeaterRefRamp.setChecked(False)
        self.ui.btnHeaterRefSinewave.setChecked(False)

        self.ui.frHeaterRefSlope.setVisible(False)
        self.ui.frHeaterRefAmplitude.setVisible(False)
        self.ui.frHeaterRefOmega.setVisible(False)

    @Slot(bool)
    def setRefRamp(self, value):
        self.ui.btnHeaterRefStep.setChecked(False)
        self.ui.btnHeaterRefRamp.setChecked(True)
        self.ui.btnHeaterRefSinewave.setChecked(False)

        self.ui.frHeaterRefSlope.setVisible(True)
        self.ui.frHeaterRefAmplitude.setVisible(False)
        self.ui.frHeaterRefOmega.setVisible(False)

    @Slot(bool)
    def setRefSinewave(self, value):
        self.ui.btnHeaterRefStep.setChecked(False)
        self.ui.btnHeaterRefRamp.setChecked(False)
        self.ui.btnHeaterRefSinewave.setChecked(True)

        self.ui.frHeaterRefSlope.setVisible(False)
        self.ui.frHeaterRefAmplitude.setVisible(True)
        self.ui.frHeaterRefOmega.setVisible(True)

    @Slot(int)
    def setSlope(self, value):
        pass

    @Slot(int)
    def setAmplitude(self, value):
        pass

    @Slot(int)
    def setOmega(self, value):
        pass
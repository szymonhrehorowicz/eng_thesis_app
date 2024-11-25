# This Python file uses the following encoding: utf-8
from PySide6.QtCore import Slot

class Export:
    def __init__(self, handler):
        self.handler = handler
        self.data_to_export = {
            "Grzalka": {
                "Regulator dwupolozeniowy": {
                    "x(t)": True,
                    "x_max(t)": True,
                    "x_min(t)": True,
                    "u_max(t)": True,
                    "u_min(t)": True,
                    "y_1(t)": True,
                    "y_2(t)": True,
                    "stan": True,
                },
                "Regulator PID": {
                    "x(t)": True,
                    "e(t)": True,
                    "int_e(t)": True,
                    "aw_int_e(t)": True,
                    "k_p(t)": True,
                    "k_i(t)": True,
                    "k_d(t)": True,
                    "k_aw(t)": True,
                    "u(t)": True,
                    "u_sat(t)": True,
                    "u_p(t)": True,
                    "u_i(t)": True,
                    "u_d(t)": True,
                    "u_max(t)": True,
                    "u_min(t)": True,
                    "y_1(t)": True,
                    "y_2(t)": True,
                    "stan": True
                }
            },
            "Wentylator": {
                "Regulator dwupolozeniowy": {
                    "x(t)": True,
                    "x_max(t)": True,
                    "x_min(t)": True,
                    "u_max(t)": True,
                    "u_min(t)": True,
                    "y(t)": True,
                    "stan": True,
                },
                "Regulator PID": {
                    "x(t)": True,
                    "e(t)": True,
                    "int_e(t)": True,
                    "aw_int_e(t)": True,
                    "k_p(t)": True,
                    "k_i(t)": True,
                    "k_d(t)": True,
                    "k_aw(t)": True,
                    "u(t)": True,
                    "u_sat(t)": True,
                    "u_p(t)": True,
                    "u_i(t)": True,
                    "u_d(t)": True,
                    "u_max(t)": True,
                    "u_min(t)": True,
                    "y(t)": True,
                    "stan": True
                }
            }
        }

    # Heater BANG BANG
    @Slot(bool)
    def set_heater_bb_x(self, state):
        self.data_to_export["Grzalka"]["Regulator dwupolozeniowy"]["x(t)"] = state

    @Slot(bool)
    def set_heater_bb_x_max(self, state):
        self.data_to_export["Grzalka"]["Regulator dwupolozeniowy"]["x_max(t)"] = state

    @Slot(bool)
    def set_heater_bb_x_min(self, state):
        self.data_to_export["Grzalka"]["Regulator dwupolozeniowy"]["x_min(t)"] = state

    @Slot(bool)
    def set_heater_bb_u_max(self, state):
        self.data_to_export["Grzalka"]["Regulator dwupolozeniowy"]["u_max(t)"] = state

    @Slot(bool)
    def set_heater_bb_u_min(self, state):
        self.data_to_export["Grzalka"]["Regulator dwupolozeniowy"]["u_min(t)"] = state

    @Slot(bool)
    def set_heater_bb_y_1(self, state):
        self.data_to_export["Grzalka"]["Regulator dwupolozeniowy"]["y_1(t)"] = state

    @Slot(bool)
    def set_heater_bb_y_2(self, state):
        self.data_to_export["Grzalka"]["Regulator dwupolozeniowy"]["y_2(t)"] = state

    @Slot(bool)
    def set_heater_bb_mode(self, state):
        self.data_to_export["Grzalka"]["Regulator dwupolozeniowy"]["stan"] = state

    # Heater PID
    @Slot(bool)
    def set_heater_pid_x(self, state):
        self.data_to_export["Grzalka"]["Regulator PID"]["x(t)"] = state

    @Slot(bool)
    def set_heater_pid_e(self, state):
        self.data_to_export["Grzalka"]["Regulator PID"]["e(t)"] = state

    @Slot(bool)
    def set_heater_pid_int_e(self, state):
        self.data_to_export["Grzalka"]["Regulator PID"]["int_e(t)"] = state

    @Slot(bool)
    def set_heater_pid_aw_int_e(self, state):
        self.data_to_export["Grzalka"]["Regulator PID"]["aw_int_e(t)"] = state

    @Slot(bool)
    def set_heater_pid_k_p(self, state):
        self.data_to_export["Grzalka"]["Regulator PID"]["k_p(t)"] = state

    @Slot(bool)
    def set_heater_pid_k_i(self, state):
        self.data_to_export["Grzalka"]["Regulator PID"]["k_i(t)"] = state

    @Slot(bool)
    def set_heater_pid_k_d(self, state):
        self.data_to_export["Grzalka"]["Regulator PID"]["k_d(t)"] = state

    @Slot(bool)
    def set_heater_pid_k_aw(self, state):
        self.data_to_export["Grzalka"]["Regulator PID"]["k_aw(t)"] = state

    @Slot(bool)
    def set_heater_pid_u(self, state):
        self.data_to_export["Grzalka"]["Regulator PID"]["u(t)"] = state

    @Slot(bool)
    def set_heater_pid_u_sat(self, state):
        self.data_to_export["Grzalka"]["Regulator PID"]["u_sat(t)"] = state

    @Slot(bool)
    def set_heater_pid_u_p(self, state):
        self.data_to_export["Grzalka"]["Regulator PID"]["u_p(t)"] = state

    @Slot(bool)
    def set_heater_pid_u_i(self, state):
        self.data_to_export["Grzalka"]["Regulator PID"]["u_i(t)"] = state

    @Slot(bool)
    def set_heater_pid_u_d(self, state):
        self.data_to_export["Grzalka"]["Regulator PID"]["u_d(t)"] = state

    @Slot(bool)
    def set_heater_pid_u_max(self, state):
        self.data_to_export["Grzalka"]["Regulator PID"]["u_max(t)"] = state

    @Slot(bool)
    def set_heater_pid_u_min(self, state):
        self.data_to_export["Grzalka"]["Regulator PID"]["u_min(t)"] = state

    @Slot(bool)
    def set_heater_pid_y_1(self, state):
        self.data_to_export["Grzalka"]["Regulator PID"]["y_1(t)"] = state

    @Slot(bool)
    def set_heater_pid_y_2(self, state):
        self.data_to_export["Grzalka"]["Regulator PID"]["y_2(t)"] = state

    @Slot(bool)
    def set_heater_pid_mode(self, state):
        self.data_to_export["Grzalka"]["Regulator PID"]["stan"] = state

    # Fan BANG BANG
    @Slot(bool)
    def set_fan_bb_x(self, state):
        self.data_to_export["Wentylator"]["Regulator dwupolozeniowy"]["x(t)"] = state

    @Slot(bool)
    def set_fan_bb_x_max(self, state):
        self.data_to_export["Wentylator"]["Regulator dwupolozeniowy"]["x_max(t)"] = state

    @Slot(bool)
    def set_fan_bb_x_min(self, state):
        self.data_to_export["Wentylator"]["Regulator dwupolozeniowy"]["x_min(t)"] = state

    @Slot(bool)
    def set_fan_bb_u_max(self, state):
        self.data_to_export["Wentylator"]["Regulator dwupolozeniowy"]["u_max(t)"] = state

    @Slot(bool)
    def set_fan_bb_u_min(self, state):
        self.data_to_export["Wentylator"]["Regulator dwupolozeniowy"]["u_min(t)"] = state

    @Slot(bool)
    def set_fan_bb_y(self, state):
        self.data_to_export["Wentylator"]["Regulator dwupolozeniowy"]["y(t)"] = state

    @Slot(bool)
    def set_fan_bb_mode(self, state):
        self.data_to_export["Wentylator"]["Regulator dwupolozeniowy"]["stan"] = state

    # Fan PID
    @Slot(bool)
    def set_fan_pid_x(self, state):
        self.data_to_export["Wentylator"]["Regulator PID"]["x(t)"] = state

    @Slot(bool)
    def set_fan_pid_e(self, state):
        self.data_to_export["Wentylator"]["Regulator PID"]["e(t)"] = state

    @Slot(bool)
    def set_fan_pid_int_e(self, state):
        self.data_to_export["Wentylator"]["Regulator PID"]["int_e(t)"] = state

    @Slot(bool)
    def set_fan_pid_aw_int_e(self, state):
        self.data_to_export["Wentylator"]["Regulator PID"]["aw_int_e(t)"] = state

    @Slot(bool)
    def set_fan_pid_k_p(self, state):
        self.data_to_export["Wentylator"]["Regulator PID"]["k_p(t)"] = state

    @Slot(bool)
    def set_fan_pid_k_i(self, state):
        self.data_to_export["Wentylator"]["Regulator PID"]["k_i(t)"] = state

    @Slot(bool)
    def set_fan_pid_k_d(self, state):
        self.data_to_export["Wentylator"]["Regulator PID"]["k_d(t)"] = state

    @Slot(bool)
    def set_fan_pid_k_aw(self, state):
        self.data_to_export["Wentylator"]["Regulator PID"]["k_aw(t)"] = state

    @Slot(bool)
    def set_fan_pid_u(self, state):
        self.data_to_export["Wentylator"]["Regulator PID"]["u(t)"] = state

    @Slot(bool)
    def set_fan_pid_u_sat(self, state):
        self.data_to_export["Wentylator"]["Regulator PID"]["u_sat(t)"] = state

    @Slot(bool)
    def set_fan_pid_u_p(self, state):
        self.data_to_export["Wentylator"]["Regulator PID"]["u_p(t)"] = state

    @Slot(bool)
    def set_fan_pid_u_i(self, state):
        self.data_to_export["Wentylator"]["Regulator PID"]["u_i(t)"] = state

    @Slot(bool)
    def set_fan_pid_u_d(self, state):
        self.data_to_export["Wentylator"]["Regulator PID"]["u_d(t)"] = state

    @Slot(bool)
    def set_fan_pid_u_max(self, state):
        self.data_to_export["Wentylator"]["Regulator PID"]["u_max(t)"] = state

    @Slot(bool)
    def set_fan_pid_u_min(self, state):
        self.data_to_export["Wentylator"]["Regulator PID"]["u_min(t)"] = state

    @Slot(bool)
    def set_fan_pid_y(self, state):
        self.data_to_export["Wentylator"]["Regulator PID"]["y(t)"] = state

    @Slot(bool)
    def set_fan_pid_mode(self, state):
        self.data_to_export["Wentylator"]["Regulator PID"]["stan"] = state
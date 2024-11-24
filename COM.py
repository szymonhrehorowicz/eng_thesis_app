# This Python file uses the following encoding: utf-8

MSG_TYPE = {
    "APP_CON_REQ": 0,
    "FAN_CONF_MSG": 1,
    "COIL_CONF_MSG": 2,
    "FAN_DATA_MSG": 3,
    "COIL_DATA_MSG": 4,
}

CONTROL_MSG = {
    # Set messages
    "SET_CONTROLLER": 0,
    "SET_REF_VALUE": 1,
    "SET_MODE": 2,
    "SET_REF_TEMP": 3,
    "SET_REF_COIL": 4,
    "SET_KP": 5,
    "SET_KI": 6,
    "SET_KD": 7,
    "SET_HYST": 8,
    "SET_HYST_SHIFT": 9,
    # Data messages
    "GET_BB_SET_VALUE": 10,
    "GET_BB_THRESHOLD_TOP": 11,
    "GET_BB_THRESHOLD_BOTTOM": 12,
    "GET_BB_U_MAX": 13,
    "GET_BB_U_MIN": 14,
    "GET_BB_CMD": 15,
    "GET_PID_SET_VALUE": 16,
    "GET_PID_ERROR": 17,
    "GET_PID_INTEGRAL_ERROR": 18,
    "GET_PID_AW_INTEGRAL_ERROR": 19,
    "GET_PID_KP": 20,
    "GET_PID_KI": 21,
    "GET_PID_KD": 22,
    "GET_PID_KAW": 23,
    "GET_PID_U": 24,
    "GET_PID_U_SATURATED": 25,
    "GET_PID_U_P": 26,
    "GET_PID_U_I": 27,
    "GET_PID_U_D": 28,
    "GET_PID_MAX": 29,
    "GET_PID_MIN": 30,
    "GET_COIL_TEMPERATURES": 31,
    "GET_COIL_MODE": 32,
    "GET_FAN_SPEED": 33,
    "GET_FAN_MODE": 34
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
    def set_fan_controller(value):
        pass

    def set_fan_mode(value):
        pass

    def set_fan_Kp(value):
        pass

    def set_fan_Ki(value):
        pass

    def set_fan_Kd(value):
        pass

    def set_fan_Kaw(value):
        pass

    def set_fan_hysteresis(value):
        pass

    def set_fan_hysteresisShift(value):
        pass

    def set_fan_refValue(value):
        pass

    # HEATER SETTERS
    def set_heater_controller(value):
        pass

    def set_heater_mode(value):
        pass

    def set_heater_Kp(value):
        pass

    def set_heater_Ki(value):
        pass

    def set_heater_Kd(value):
        pass

    def set_heater_Kaw(value):
        pass

    def set_heater_hysteresis(value):
        pass

    def set_heater_hysteresisShift(value):
        pass

    def set_heater_refValue(value):
        pass

    def set_heater_refCoil(value):
        pass

    def set_heater_refTemp(value):
        pass

    # FAN GETTERS
    def get_all_fan_data():
        pass

    def handle_all_fan_data(data):
        data = data.split('_')[1:]
        fan_all_data = {
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
            "PID_KP": float(data[0]),
            "PID_KI": float(data[1]),
            "PID_KD": float(data[2]),
            "PID_KAW": float(data[3]),
            "PID_U": int(data[4]),
            "PID_U_SATURATED": int(data[5]),
            "PID_U_P": float(data[6]),
            "PID_U_I": float(data[7]),
            "PID_U_D": float(data[8]),
            "PID_MAX": int(data[9]),
            "PID_MIN": int(data[0]),
            "PID_SPEED": int(data[1]),
            "PID_MODE": int(data[2]),
        }

    def get_fast_fan_data():
        pass

    def handle_fast_fan_data(self, data):
        data = data.split('_')[1:]
        fan_fast_data = {
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
        }
        print(fan_fast_data)

    # HEATER GETTERS
    def get_all_heater_data():
        pass

    def handle_all_heater_data(data):
        data = data.split('_')[1:]
        
    
    def get_fast_heater_data():
        pass

    def handle_fast_heater_data(self, data):
        data = data.split('_')[1:]
        heater_fast_data = {
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
        }
        print(heater_fast_data)

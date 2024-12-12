# This Python file uses the following encoding: utf-8
import time

class HeaterController:
    def __init__(self):
        # BB
        self.t0_bb = 0
        self.bb_time = []
        self.bb_set_value = []
        self.bb_threshold_top = []
        self.bb_threshold_bottom = []
        self.bb_u_max = []
        self.bb_u_min = []
        self.bb_mode = []
        self.bb_temp_left = []
        self.bb_temp_right = []
        # PID
        self.t0_pid = 0
        self.pid_time = []
        self.pid_set_value = []
        self.pid_error = []
        self.pid_int_error = []
        self.pid_aw_int_error = []
        self.pid_kp = []
        self.pid_ki = []
        self.pid_kd = []
        self.pid_kaw = []
        self.pid_u = []
        self.pid_u_saturated = []
        self.pid_u_p = []
        self.pid_u_i = []
        self.pid_u_d = []
        self.pid_u_max = []
        self.pid_u_min = []
        self.pid_temp_left = []
        self.pid_temp_right = []
        self.pid_mode = []

    def get_bb(self):
        return [
            self.bb_time,
            self.bb_set_value,
            self.bb_threshold_top,
            self.bb_threshold_bottom,
            self.bb_u_max,
            self.bb_u_min,
            self.bb_temp_left,
            self.bb_temp_right,
            self.bb_mode]
    
    def get_pid(self):
        return [
            self.pid_time,
            self.pid_set_value,
            self.pid_error,
            self.pid_int_error,
            self.pid_aw_int_error,
            self.pid_kp,
            self.pid_ki,
            self.pid_kd,
            self.pid_kaw,
            self.pid_u,
            self.pid_u_saturated,
            self.pid_u_p,
            self.pid_u_i,
            self.pid_u_d,
            self.pid_u_max,
            self.pid_u_min,
            self.pid_temp_left,
            self.pid_temp_right,
            self.pid_mode]

    def update_all(self, data):
        # Timestamp - given in [ms]
        if self.t0_bb == 0:
            self.t0_bb = data["TIMESTAMP"]
            self.bb_time.append(0)
        else:
            self.bb_time.append((data["TIMESTAMP"] - self.t0_bb) / 1000)
        if self.t0_pid == 0:
            self.t0_pid = data["TIMESTAMP"]
            self.pid_time.append(0)
        else:
            self.pid_time.append((data["TIMESTAMP"]- self.t0_pid) / 1000)
        # BB
        self.bb_set_value.append(data["BB_SET_VALUE"])
        self.bb_threshold_top.append(data["BB_THRESHOLD_TOP"])
        self.bb_threshold_bottom.append(data["BB_THRESHOLD_BOTTOM"])
        self.bb_u_max.append(data["BB_U_MAX"])
        self.bb_u_min.append(data["BB_U_MIN"])
        self.bb_temp_left.append(data["PID_TEMP_LEFT"])
        self.bb_temp_right.append(data["PID_TEMP_RIGHT"])
        self.bb_mode.append(data["BB_CMD"])
        # PID
        self.pid_set_value.append(data["PID_SET_VALUE"])
        self.pid_error.append(data["PID_ERROR"])
        self.pid_int_error.append(data["PID_INT_ERROR"])
        self.pid_aw_int_error.append(data["PID_AW_INT_ERROR"])
        self.pid_kp.append(data["PID_KP"])
        self.pid_ki.append(data["PID_KI"])
        self.pid_kd.append(data["PID_KD"])
        self.pid_kaw.append(data["PID_KAW"])
        self.pid_u.append(data["PID_U"])
        self.pid_u_saturated.append(data["PID_U_SATURATED"])
        self.pid_u_p.append(data["PID_U_P"])
        self.pid_u_i.append(data["PID_U_I"])
        self.pid_u_d.append(data["PID_U_D"])
        self.pid_u_max.append(data["PID_MAX"])
        self.pid_u_min.append(data["PID_MIN"])
        self.pid_temp_left.append(data["PID_TEMP_LEFT"])
        self.pid_temp_right.append(data["PID_TEMP_RIGHT"])
        self.pid_mode.append(data["PID_MODE"])

    def update_fast(self, data):
        # Timestamp - given in [ms]
        if self.t0_bb == 0:
            self.t0_bb = data["TIMESTAMP"]
            self.bb_time.append(0)
        else:
            self.bb_time.append((data["TIMESTAMP"] - self.t0_bb) / 1000)
        if self.t0_pid == 0:
            self.t0_pid = data["TIMESTAMP"]
            self.pid_time.append(0)
        else:
            self.pid_time.append((data["TIMESTAMP"]- self.t0_pid) / 1000)
        # BB
        self.bb_set_value.append(self.bb_set_value[-1])
        self.bb_threshold_top.append(self.bb_threshold_top[-1])
        self.bb_threshold_bottom.append(self.bb_threshold_bottom[-1])
        self.bb_u_max.append(self.bb_u_max[-1])
        self.bb_u_min.append(self.bb_u_min[-1])
        self.bb_temp_left.append(data["PID_TEMP_LEFT"])
        self.bb_temp_right.append(data["PID_TEMP_RIGHT"])
        self.bb_mode.append(data["BB_CMD"])
        # PID
        self.pid_set_value.append(self.pid_set_value[-1])
        self.pid_error.append(data["PID_ERROR"])
        self.pid_int_error.append(data["PID_INT_ERROR"])
        self.pid_aw_int_error.append(data["PID_AW_INT_ERROR"])
        self.pid_kp.append(self.pid_kp[-1])
        self.pid_ki.append(self.pid_ki[-1])
        self.pid_kd.append(self.pid_kd[-1])
        self.pid_kaw.append(self.pid_kaw[-1])
        self.pid_u.append(data["PID_U"])
        self.pid_u_saturated.append(data["PID_U_SATURATED"])
        self.pid_u_p.append(data["PID_U_P"])
        self.pid_u_i.append(data["PID_U_I"])
        self.pid_u_d.append(data["PID_U_D"])
        self.pid_u_max.append(self.pid_u_max[-1])
        self.pid_u_min.append(self.pid_u_min[-1])
        self.pid_temp_left.append(data["PID_TEMP_LEFT"])
        self.pid_temp_right.append(data["PID_TEMP_RIGHT"])
        self.pid_mode.append(data["PID_MODE"])

    def clear_bb(self):
        self.t0_bb = 0
        self.bb_time = []
        self.bb_set_value = []
        self.bb_threshold_top = []
        self.bb_threshold_bottom = []
        self.bb_u_max = []
        self.bb_u_min = []
        self.bb_temp_left = []
        self.bb_temp_right = []
        self.bb_mode = []

    def clear_pid(self):
        self.t0_pid = 0
        self.pid_time = []
        self.pid_set_value = []
        self.pid_error = []
        self.pid_int_error = []
        self.pid_aw_int_error = []
        self.pid_kp = []
        self.pid_ki = []
        self.pid_kd = []
        self.pid_kaw = []
        self.pid_u = []
        self.pid_u_saturated = []
        self.pid_u_p = []
        self.pid_u_i = []
        self.pid_u_d = []
        self.pid_u_max = []
        self.pid_u_min = []
        self.pid_temp_left = []
        self.pid_temp_right = []
        self.pid_mode = []

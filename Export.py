# This Python file uses the following encoding: utf-8
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QFileDialog
from datetime import datetime
from openpyxl import Workbook
from utilities import error_dialog, success_dialog
from PySide6.QtCore import QCoreApplication
import os

class Export:
    def __init__(self, handler):
        self.handler = handler
        self.data_to_export = {
            "Grzalka": {
                "states": {
                    "Regulator dwupolozeniowy": True,
                    "Regulator PID": True,
                },
                "Regulator dwupolozeniowy": {
                    "r(t)": True,
                    "r_max": True,
                    "r_min": True,
                    "u_max": True,
                    "u_min": True,
                    "y_1(t)": True,
                    "y_2(t)": True,
                    "stan": True,
                },
                "Regulator PID": {
                    "r(t)": True,
                    "e(t)": True,
                    "int_e(t)": True,
                    "aw_int_e(t)": True,
                    "k_p": True,
                    "k_i": True,
                    "k_d": True,
                    "k_aw": True,
                    "u(t)": True,
                    "u_sat(t)": True,
                    "u_p(t)": True,
                    "u_i(t)": True,
                    "u_d(t)": True,
                    "u_max": True,
                    "u_min": True,
                    "y_1(t)": True,
                    "y_2(t)": True,
                    "stan": True
                }
            },
            "Wentylator": {
                "states": {
                    "Regulator dwupolozeniowy": True,
                    "Regulator PID": True,
                },
                "Regulator dwupolozeniowy": {
                    "r(t)": True,
                    "r_max": True,
                    "r_min": True,
                    "u_max": True,
                    "u_min": True,
                    "y(t)": True,
                    "stan": True,
                },
                "Regulator PID": {
                    "r(t)": True,
                    "e(t)": True,
                    "int_e(t)": True,
                    "aw_int_e(t)": True,
                    "k_p": True,
                    "k_i": True,
                    "k_d": True,
                    "k_aw": True,
                    "u(t)": True,
                    "u_sat(t)": True,
                    "u_p(t)": True,
                    "u_i(t)": True,
                    "u_d(t)": True,
                    "u_max": True,
                    "u_min": True,
                    "y(t)": True,
                    "stan": True
                }
            }
        }

    # Export method
    @Slot()
    def export(self):
        date = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
        desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        fileName = QFileDialog.getSaveFileName(None, QCoreApplication.tr("Wybierz lokalizacje oraz nazwe pliku"), f"{desktop}\\DanePomiarowe_{date}.xlsx", "Excel files (*.xlsx)")[0]

        workbook = Workbook()
        sheet = workbook.active

        exportHeater = any(self.data_to_export["Grzalka"]["states"].values())
        exportFan = any(self.data_to_export["Wentylator"]["states"].values())

        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                    'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                    'AA', 'AB', 'AC', 'AD', 'AE', 'AF', 'AG', 'AH', 'AI', 'AJ',
                    'AK', 'AL', 'AM', 'AN', 'AO', 'AP', 'AQ', 'AR', 'AS',
                    'AT', 'AU', 'AV', 'AW', 'AX', 'AY', 'AZ',
                    'BA', 'BB', 'BC', 'BD', 'BE', 'BF', 'BG', 'BH', 'BI', 'BJ',
                    'BK', 'BL', 'BM', 'BN', 'BO', 'BP', 'BQ', 'BR', 'BS',
                    'BT', 'BU', 'BV', 'BW', 'BX', 'BY', 'BZ',
                    'CA', 'CB', 'CC', 'CD', 'CE', 'CF', 'CG', 'CH', 'CI', 'CJ',
                    'CK', 'CL', 'CM', 'CN', 'CO', 'CP', 'CQ', 'CR', 'CS',
                    'CT', 'CU', 'CV', 'CW', 'CX', 'CY', 'CZ',
                    'DA', 'DB', 'DC', 'DD', 'DE', 'DF', 'DG', 'DH', 'DI', 'DJ',
                    'DK', 'DL', 'DM', 'DN', 'DO', 'DP', 'DQ', 'DR', 'DS',
                    'DT', 'DU', 'DV', 'DW', 'DX', 'DY', 'DZ',]
        horizontal_idx = 0
        vertical_idx = 1

        if exportHeater:
            sheet[f'{letters[horizontal_idx]}{vertical_idx}'] = QCoreApplication.tr("Grzalka")
            for master_key in list(self.data_to_export["Grzalka"].keys())[1:]:
                vertical_idx = 2
                if self.data_to_export["Grzalka"]["states"][master_key]:
                    data = self.handler.heaterController.get_bb() if master_key == "Regulator dwupolozeniowy" else self.handler.heaterController.get_pid()
                    if len(data[0]) > 0: 
                        sheet[f'{letters[horizontal_idx]}{vertical_idx}'] = master_key
                        vertical_idx += 1

                        # Add time
                        sheet[f'{letters[horizontal_idx]}{vertical_idx}'] = "t, s"
                        vertical_idx += 1
                        for value in data[0]:
                            sheet[f'{letters[horizontal_idx]}{vertical_idx}'] = value
                            vertical_idx += 1
                        vertical_idx = 3
                        horizontal_idx += 1
                        # Add rest of signals
                        for idx, key in enumerate(self.data_to_export["Grzalka"][master_key]):
                            sheet[f'{letters[horizontal_idx]}{vertical_idx}'] = key
                            vertical_idx += 1
                            for value in data[idx + 1]:
                                sheet[f'{letters[horizontal_idx]}{vertical_idx}'] = value
                                vertical_idx += 1
                            horizontal_idx += 1
                            vertical_idx = 3
        if exportFan:
            vertical_idx = 1
            sheet[f'{letters[horizontal_idx]}{vertical_idx}'] = QCoreApplication.tr("Wentylator")
            for master_key in list(self.data_to_export["Wentylator"].keys())[1:]:
                vertical_idx = 2
                if self.data_to_export["Wentylator"]["states"][master_key]:
                    data = self.handler.fanController.get_bb() if master_key == "Regulator dwupolozeniowy" else self.handler.fanController.get_pid()
                    if len(data[0]) > 0: 
                        sheet[f'{letters[horizontal_idx]}{vertical_idx}'] = master_key
                        vertical_idx += 1

                        # Add time
                        sheet[f'{letters[horizontal_idx]}{vertical_idx}'] = "t, s"
                        vertical_idx += 1
                        for value in data[0]:
                            sheet[f'{letters[horizontal_idx]}{vertical_idx}'] = value
                            vertical_idx += 1
                        vertical_idx = 3
                        horizontal_idx += 1
                        # Add rest of signals
                        for idx, key in enumerate(self.data_to_export["Wentylator"][master_key]):
                            sheet[f'{letters[horizontal_idx]}{vertical_idx}'] = key
                            vertical_idx += 1
                            for value in data[idx + 1]:
                                sheet[f'{letters[horizontal_idx]}{vertical_idx}'] = value
                                vertical_idx += 1
                            horizontal_idx += 1
                            vertical_idx = 3
            
        # Save to file
        try:
            workbook.save(filename=fileName)
            success_dialog(self.handler, QCoreApplication.tr(f"Pomyślnie wyeksportowano dane do pliku:\n{fileName}"))
        except PermissionError:
            error_dialog(self.handler, QCoreApplication.tr("Plik do którego chcesz nadpisać dane jest obecnie otwarty. Zamknij go i spróbuj ponownie."))
        except Exception:
            pass


    # Main selectors
    @Slot(bool)
    def set_heater_bb(self, state):
        self.data_to_export["Grzalka"]["states"]["Regulator dwupolozeniowy"] = state
        keys = self.data_to_export["Grzalka"]["Regulator dwupolozeniowy"].keys()
        for key in keys:
            self.data_to_export["Grzalka"]["Regulator dwupolozeniowy"][key] = state
        self.handler.ui.chxExHeaterBB_x.setChecked(state)
        self.handler.ui.chxExHeaterBB_x_max.setChecked(state)
        self.handler.ui.chxExHeaterBB_x_min.setChecked(state)
        self.handler.ui.chxExHeaterBB_u_max.setChecked(state)
        self.handler.ui.chxExHeaterBB_u_min.setChecked(state)
        self.handler.ui.chxExHeaterBB_y_1.setChecked(state)
        self.handler.ui.chxExHeaterBB_y_2.setChecked(state)
        self.handler.ui.chxExHeaterBB_mode.setChecked(state)
    
    @Slot(bool)
    def set_heater_pid(self, state):
        self.data_to_export["Grzalka"]["states"]["Regulator PID"] = state
        keys = self.data_to_export["Grzalka"]["Regulator PID"].keys()
        for key in keys:
            self.data_to_export["Grzalka"]["Regulator PID"][key] = state
        self.handler.ui.chxExHeaterPID_x.setChecked(state)
        self.handler.ui.chxExHeaterPID_e.setChecked(state)
        self.handler.ui.chxExHeaterPID_int_e.setChecked(state)
        self.handler.ui.chxExHeaterPID_aw_int_e.setChecked(state)
        self.handler.ui.chxExHeaterPID_k_p.setChecked(state)
        self.handler.ui.chxExHeaterPID_k_i.setChecked(state)
        self.handler.ui.chxExHeaterPID_k_d.setChecked(state)
        self.handler.ui.chxExHeaterPID_k_aw.setChecked(state)
        self.handler.ui.chxExHeaterPID_u.setChecked(state)
        self.handler.ui.chxExHeaterPID_u_sat.setChecked(state)
        self.handler.ui.chxExHeaterPID_u_p.setChecked(state)
        self.handler.ui.chxExHeaterPID_u_i.setChecked(state)
        self.handler.ui.chxExHeaterPID_u_d.setChecked(state)
        self.handler.ui.chxExHeaterPID_u_max.setChecked(state)
        self.handler.ui.chxExHeaterPID_u_min.setChecked(state)
        self.handler.ui.chxExHeaterPID_y_1.setChecked(state)
        self.handler.ui.chxExHeaterPID_y_2.setChecked(state)
        self.handler.ui.chxExHeaterPID_mode.setChecked(state)
    
    @Slot(bool)
    def set_fan_bb(self, state):
        self.data_to_export["Wentylator"]["states"]["Regulator dwupolozeniowy"] = state
        keys = self.data_to_export["Wentylator"]["Regulator dwupolozeniowy"].keys()
        for key in keys:
            self.data_to_export["Wentylator"]["Regulator dwupolozeniowy"][key] = state
        self.handler.ui.chxExFanBB_x.setChecked(state)
        self.handler.ui.chxExFanBB_x_max.setChecked(state)
        self.handler.ui.chxExFanBB_x_min.setChecked(state)
        self.handler.ui.chxExFanBB_u_max.setChecked(state)
        self.handler.ui.chxExFanBB_u_min.setChecked(state)
        self.handler.ui.chxExFanBB_y.setChecked(state)
        self.handler.ui.chxExFanBB_mode.setChecked(state)

    @Slot(bool)
    def set_fan_pid(self, state):
        self.data_to_export["Wentylator"]["states"]["Regulator PID"] = state
        keys = self.data_to_export["Wentylator"]["Regulator PID"].keys()
        for key in keys:
            self.data_to_export["Wentylator"]["Regulator PID"][key] = state
        self.handler.ui.chxExFanPID_x.setChecked(state)
        self.handler.ui.chxExFanPID_e.setChecked(state)
        self.handler.ui.chxExFanPID_int_e.setChecked(state)
        self.handler.ui.chxExFanPID_aw_int_e.setChecked(state)
        self.handler.ui.chxExFanPID_k_p.setChecked(state)
        self.handler.ui.chxExFanPID_k_i.setChecked(state)
        self.handler.ui.chxExFanPID_k_d.setChecked(state)
        self.handler.ui.chxExFanPID_k_aw.setChecked(state)
        self.handler.ui.chxExFanPID_u.setChecked(state)
        self.handler.ui.chxExFanPID_u_sat.setChecked(state)
        self.handler.ui.chxExFanPID_u_p.setChecked(state)
        self.handler.ui.chxExFanPID_u_i.setChecked(state)
        self.handler.ui.chxExFanPID_u_d.setChecked(state)
        self.handler.ui.chxExFanPID_u_max.setChecked(state)
        self.handler.ui.chxExFanPID_u_min.setChecked(state)
        self.handler.ui.chxExFanPID_y.setChecked(state)
        self.handler.ui.chxExFanPID_mode.setChecked(state)

    # Heater BANG BANG
    def sub_button_handler(self, state, handle, controller: str, _type: str):
        if state:
            self.data_to_export[controller]["states"][_type] = True
            handle.setChecked(True)
        else:
            if not any(self.data_to_export[controller][_type].values()):
                self.data_to_export[controller]["states"][_type] = False
                handle.setChecked(False)

    @Slot(bool)
    def set_heater_bb_x(self, state):
        self.data_to_export["Grzalka"]["Regulator dwupolozeniowy"]["r(t)"] = state
        self.sub_button_handler(state, self.handler.ui.chxExHeaterBB, "Grzalka", "Regulator dwupolozeniowy")

    @Slot(bool)
    def set_heater_bb_x_max(self, state):
        self.data_to_export["Grzalka"]["Regulator dwupolozeniowy"]["r_max"] = state
        self.sub_button_handler(state, self.handler.ui.chxExHeaterBB, "Grzalka", "Regulator dwupolozeniowy")

    @Slot(bool)
    def set_heater_bb_x_min(self, state):
        self.data_to_export["Grzalka"]["Regulator dwupolozeniowy"]["r_min"] = state
        self.sub_button_handler(state, self.handler.ui.chxExHeaterBB, "Grzalka", "Regulator dwupolozeniowy")

    @Slot(bool)
    def set_heater_bb_u_max(self, state):
        self.data_to_export["Grzalka"]["Regulator dwupolozeniowy"]["u_max"] = state
        self.sub_button_handler(state, self.handler.ui.chxExHeaterBB, "Grzalka", "Regulator dwupolozeniowy")

    @Slot(bool)
    def set_heater_bb_u_min(self, state):
        self.data_to_export["Grzalka"]["Regulator dwupolozeniowy"]["u_min"] = state
        self.sub_button_handler(state, self.handler.ui.chxExHeaterBB, "Grzalka", "Regulator dwupolozeniowy")

    @Slot(bool)
    def set_heater_bb_y_1(self, state):
        self.data_to_export["Grzalka"]["Regulator dwupolozeniowy"]["y_1(t)"] = state
        self.sub_button_handler(state, self.handler.ui.chxExHeaterBB, "Grzalka", "Regulator dwupolozeniowy")

    @Slot(bool)
    def set_heater_bb_y_2(self, state):
        self.data_to_export["Grzalka"]["Regulator dwupolozeniowy"]["y_2(t)"] = state
        self.sub_button_handler(state, self.handler.ui.chxExHeaterBB, "Grzalka", "Regulator dwupolozeniowy")

    @Slot(bool)
    def set_heater_bb_mode(self, state):
        self.data_to_export["Grzalka"]["Regulator dwupolozeniowy"]["stan"] = state
        self.sub_button_handler(state, self.handler.ui.chxExHeaterBB, "Grzalka", "Regulator dwupolozeniowy")

    # Heater PID
    @Slot(bool)
    def set_heater_pid_x(self, state):
        self.data_to_export["Grzalka"]["Regulator PID"]["r(t)"] = state
        self.sub_button_handler(state, self.handler.ui.chxExHeaterPID, "Grzalka", "Regulator PID")

    @Slot(bool)
    def set_heater_pid_e(self, state):
        self.data_to_export["Grzalka"]["Regulator PID"]["e(t)"] = state
        self.sub_button_handler(state, self.handler.ui.chxExHeaterPID, "Grzalka", "Regulator PID")

    @Slot(bool)
    def set_heater_pid_int_e(self, state):
        self.data_to_export["Grzalka"]["Regulator PID"]["int_e(t)"] = state
        self.sub_button_handler(state, self.handler.ui.chxExHeaterPID, "Grzalka", "Regulator PID")

    @Slot(bool)
    def set_heater_pid_aw_int_e(self, state):
        self.data_to_export["Grzalka"]["Regulator PID"]["aw_int_e(t)"] = state
        self.sub_button_handler(state, self.handler.ui.chxExHeaterPID, "Grzalka", "Regulator PID")

    @Slot(bool)
    def set_heater_pid_k_p(self, state):
        self.data_to_export["Grzalka"]["Regulator PID"]["k_p"] = state
        self.sub_button_handler(state, self.handler.ui.chxExHeaterPID, "Grzalka", "Regulator PID")

    @Slot(bool)
    def set_heater_pid_k_i(self, state):
        self.data_to_export["Grzalka"]["Regulator PID"]["k_i"] = state
        self.sub_button_handler(state, self.handler.ui.chxExHeaterPID, "Grzalka", "Regulator PID")

    @Slot(bool)
    def set_heater_pid_k_d(self, state):
        self.data_to_export["Grzalka"]["Regulator PID"]["k_d"] = state
        self.sub_button_handler(state, self.handler.ui.chxExHeaterPID, "Grzalka", "Regulator PID")

    @Slot(bool)
    def set_heater_pid_k_aw(self, state):
        self.data_to_export["Grzalka"]["Regulator PID"]["k_aw"] = state
        self.sub_button_handler(state, self.handler.ui.chxExHeaterPID, "Grzalka", "Regulator PID")

    @Slot(bool)
    def set_heater_pid_u(self, state):
        self.data_to_export["Grzalka"]["Regulator PID"]["u(t)"] = state
        self.sub_button_handler(state, self.handler.ui.chxExHeaterPID, "Grzalka", "Regulator PID")

    @Slot(bool)
    def set_heater_pid_u_sat(self, state):
        self.data_to_export["Grzalka"]["Regulator PID"]["u_sat(t)"] = state
        self.sub_button_handler(state, self.handler.ui.chxExHeaterPID, "Grzalka", "Regulator PID")

    @Slot(bool)
    def set_heater_pid_u_p(self, state):
        self.data_to_export["Grzalka"]["Regulator PID"]["u_p(t)"] = state
        self.sub_button_handler(state, self.handler.ui.chxExHeaterPID, "Grzalka", "Regulator PID")

    @Slot(bool)
    def set_heater_pid_u_i(self, state):
        self.data_to_export["Grzalka"]["Regulator PID"]["u_i(t)"] = state
        self.sub_button_handler(state, self.handler.ui.chxExHeaterPID, "Grzalka", "Regulator PID")

    @Slot(bool)
    def set_heater_pid_u_d(self, state):
        self.data_to_export["Grzalka"]["Regulator PID"]["u_d(t)"] = state
        self.sub_button_handler(state, self.handler.ui.chxExHeaterPID, "Grzalka", "Regulator PID")

    @Slot(bool)
    def set_heater_pid_u_max(self, state):
        self.data_to_export["Grzalka"]["Regulator PID"]["u_max"] = state
        self.sub_button_handler(state, self.handler.ui.chxExHeaterPID, "Grzalka", "Regulator PID")

    @Slot(bool)
    def set_heater_pid_u_min(self, state):
        self.data_to_export["Grzalka"]["Regulator PID"]["u_min"] = state
        self.sub_button_handler(state, self.handler.ui.chxExHeaterPID, "Grzalka", "Regulator PID")

    @Slot(bool)
    def set_heater_pid_y_1(self, state):
        self.data_to_export["Grzalka"]["Regulator PID"]["y_1(t)"] = state
        self.sub_button_handler(state, self.handler.ui.chxExHeaterPID, "Grzalka", "Regulator PID")

    @Slot(bool)
    def set_heater_pid_y_2(self, state):
        self.data_to_export["Grzalka"]["Regulator PID"]["y_2(t)"] = state
        self.sub_button_handler(state, self.handler.ui.chxExHeaterPID, "Grzalka", "Regulator PID")

    @Slot(bool)
    def set_heater_pid_mode(self, state):
        self.data_to_export["Grzalka"]["Regulator PID"]["stan"] = state
        self.sub_button_handler(state, self.handler.ui.chxExHeaterPID, "Grzalka", "Regulator PID")

    # Fan BANG BANG
    @Slot(bool)
    def set_fan_bb_x(self, state):
        self.data_to_export["Wentylator"]["Regulator dwupolozeniowy"]["r(t)"] = state
        self.sub_button_handler(state, self.handler.ui.chxExFanBB, "Wentylator", "Regulator dwupolozeniowy")

    @Slot(bool)
    def set_fan_bb_x_max(self, state):
        self.data_to_export["Wentylator"]["Regulator dwupolozeniowy"]["r_max"] = state
        self.sub_button_handler(state, self.handler.ui.chxExFanBB, "Wentylator", "Regulator dwupolozeniowy")

    @Slot(bool)
    def set_fan_bb_x_min(self, state):
        self.data_to_export["Wentylator"]["Regulator dwupolozeniowy"]["r_min"] = state
        self.sub_button_handler(state, self.handler.ui.chxExFanBB, "Wentylator", "Regulator dwupolozeniowy")

    @Slot(bool)
    def set_fan_bb_u_max(self, state):
        self.data_to_export["Wentylator"]["Regulator dwupolozeniowy"]["u_max"] = state
        self.sub_button_handler(state, self.handler.ui.chxExFanBB, "Wentylator", "Regulator dwupolozeniowy")

    @Slot(bool)
    def set_fan_bb_u_min(self, state):
        self.data_to_export["Wentylator"]["Regulator dwupolozeniowy"]["u_min"] = state
        self.sub_button_handler(state, self.handler.ui.chxExFanBB, "Wentylator", "Regulator dwupolozeniowy")

    @Slot(bool)
    def set_fan_bb_y(self, state):
        self.data_to_export["Wentylator"]["Regulator dwupolozeniowy"]["y(t)"] = state
        self.sub_button_handler(state, self.handler.ui.chxExFanBB, "Wentylator", "Regulator dwupolozeniowy")

    @Slot(bool)
    def set_fan_bb_mode(self, state):
        self.data_to_export["Wentylator"]["Regulator dwupolozeniowy"]["stan"] = state
        self.sub_button_handler(state, self.handler.ui.chxExFanBB, "Wentylator", "Regulator dwupolozeniowy")

    # Fan PID
    @Slot(bool)
    def set_fan_pid_x(self, state):
        self.data_to_export["Wentylator"]["Regulator PID"]["r(t)"] = state
        self.sub_button_handler(state, self.handler.ui.chxExFanPID, "Wentylator", "Regulator PID")

    @Slot(bool)
    def set_fan_pid_e(self, state):
        self.data_to_export["Wentylator"]["Regulator PID"]["e(t)"] = state
        self.sub_button_handler(state, self.handler.ui.chxExFanPID, "Wentylator", "Regulator PID")

    @Slot(bool)
    def set_fan_pid_int_e(self, state):
        self.data_to_export["Wentylator"]["Regulator PID"]["int_e(t)"] = state
        self.sub_button_handler(state, self.handler.ui.chxExFanPID, "Wentylator", "Regulator PID")

    @Slot(bool)
    def set_fan_pid_aw_int_e(self, state):
        self.data_to_export["Wentylator"]["Regulator PID"]["aw_int_e(t)"] = state
        self.sub_button_handler(state, self.handler.ui.chxExFanPID, "Wentylator", "Regulator PID")

    @Slot(bool)
    def set_fan_pid_k_p(self, state):
        self.data_to_export["Wentylator"]["Regulator PID"]["k_p"] = state
        self.sub_button_handler(state, self.handler.ui.chxExFanPID, "Wentylator", "Regulator PID")

    @Slot(bool)
    def set_fan_pid_k_i(self, state):
        self.data_to_export["Wentylator"]["Regulator PID"]["k_i"] = state
        self.sub_button_handler(state, self.handler.ui.chxExFanPID, "Wentylator", "Regulator PID")

    @Slot(bool)
    def set_fan_pid_k_d(self, state):
        self.data_to_export["Wentylator"]["Regulator PID"]["k_d"] = state
        self.sub_button_handler(state, self.handler.ui.chxExFanPID, "Wentylator", "Regulator PID")

    @Slot(bool)
    def set_fan_pid_k_aw(self, state):
        self.data_to_export["Wentylator"]["Regulator PID"]["k_aw"] = state
        self.sub_button_handler(state, self.handler.ui.chxExFanPID, "Wentylator", "Regulator PID")

    @Slot(bool)
    def set_fan_pid_u(self, state):
        self.data_to_export["Wentylator"]["Regulator PID"]["u(t)"] = state
        self.sub_button_handler(state, self.handler.ui.chxExFanPID, "Wentylator", "Regulator PID")

    @Slot(bool)
    def set_fan_pid_u_sat(self, state):
        self.data_to_export["Wentylator"]["Regulator PID"]["u_sat(t)"] = state
        self.sub_button_handler(state, self.handler.ui.chxExFanPID, "Wentylator", "Regulator PID")

    @Slot(bool)
    def set_fan_pid_u_p(self, state):
        self.data_to_export["Wentylator"]["Regulator PID"]["u_p(t)"] = state
        self.sub_button_handler(state, self.handler.ui.chxExFanPID, "Wentylator", "Regulator PID")

    @Slot(bool)
    def set_fan_pid_u_i(self, state):
        self.data_to_export["Wentylator"]["Regulator PID"]["u_i(t)"] = state
        self.sub_button_handler(state, self.handler.ui.chxExFanPID, "Wentylator", "Regulator PID")

    @Slot(bool)
    def set_fan_pid_u_d(self, state):
        self.data_to_export["Wentylator"]["Regulator PID"]["u_d(t)"] = state
        self.sub_button_handler(state, self.handler.ui.chxExFanPID, "Wentylator", "Regulator PID")

    @Slot(bool)
    def set_fan_pid_u_max(self, state):
        self.data_to_export["Wentylator"]["Regulator PID"]["u_max"] = state
        self.sub_button_handler(state, self.handler.ui.chxExFanPID, "Wentylator", "Regulator PID")

    @Slot(bool)
    def set_fan_pid_u_min(self, state):
        self.data_to_export["Wentylator"]["Regulator PID"]["u_min"] = state
        self.sub_button_handler(state, self.handler.ui.chxExFanPID, "Wentylator", "Regulator PID")

    @Slot(bool)
    def set_fan_pid_y(self, state):
        self.data_to_export["Wentylator"]["Regulator PID"]["y(t)"] = state
        self.sub_button_handler(state, self.handler.ui.chxExFanPID, "Wentylator", "Regulator PID")

    @Slot(bool)
    def set_fan_pid_mode(self, state):
        self.data_to_export["Wentylator"]["Regulator PID"]["stan"] = state
        self.sub_button_handler(state, self.handler.ui.chxExFanPID, "Wentylator", "Regulator PID")

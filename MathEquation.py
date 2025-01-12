# This Python file uses the following encoding: utf-8
import re
from bs4 import BeautifulSoup as bs
from PySide6.QtCore import QFile, QIODevice, Slot
import rc_resources

class MathEquation:
    def __init__(self, handler):
        self.template_dir = ":/assets/"
        self.template_name = "template"
        self.handler = handler
        self._load_template()
        self.handler.setHtml(self.template.prettify())
        self.eq_type = "parallel"

    def _load_template(self):
        # Open the file from Qt's resource system
        file_path = self.template_dir + self.template_name
        file = QFile(file_path)
        if not file.open(QIODevice.ReadOnly | QIODevice.Text):
            print("Failed to open resource file:", file_path)
            return

        # Read the content from the file
        html_content = file.readAll().data().decode('utf-8')
        self.template = bs(html_content, "html.parser")

    def update(self, Kp, Ki, Kd, Ti, Td):
        self._load_template()
        Kp = '%.2f'%Kp
        Ki = '%.2f'%Ki
        Kd = '%.2f'%Kd
        Ti = '%.2f'%Ti
        Td = '%.2f'%Td
        if self.eq_type == "parallel":
            equation = self.template.find("mathjax", {"id": "parallel"})
            not_equation = self.template.find("mathjax", {"id": "academic"})
            equation["style"] = "font-size:2.3em; display: block;"
            not_equation["style"] = "font-size:2.3em; display: none;"

            equation.string = r"$$u(t) = K_pe(t) + K_i\int_{0}^{t}e(\tau) d\tau + K_d\frac{de(t)}{dt}$$"
            equation.string = re.sub(r"K_p", "" if Kp == "0.00" else Kp, equation.string)
            if Ki != "0.00":
                equation.string = re.sub(r"K_i", "" if Ki == "0.00" else Ki, equation.string)
            else:
                equation.string = equation.string.replace(r"+ K_i\int_{0}^{t}e(\tau) d\tau", " ")
            if Kd != "0.00":
                equation.string = re.sub(r"K_d", "" if Kd == "0.00" else Kd, equation.string)
            else:
                equation.string = equation.string.replace(r"+ K_d\frac{de(t)}{dt}", "")
        else:
            equation = self.template.find("mathjax", {"id": "academic"})
            not_equation = self.template.find("mathjax", {"id": "parallel"})
            equation["style"] = "font-size:2.3em; display: block;"
            not_equation["style"] = "font-size:2.3em; display: none;"

            equation.string = r"$$u(t) = K_p(e(t) + \frac{1}{T_i}\int_{0}^{t}e(\tau) d\tau + T_d\frac{de(t)}{dt})$$"
            equation.string = re.sub(r"K_p", "" if Kp == "0.00" else Kp, equation.string)
            if Ki == "0.00":
                equation.string = equation.string.replace(r"+ \frac{1}{T_i}\int_{0}^{t}e(\tau) d\tau", " ")
            if Kd == "0.00":
                equation.string = equation.string.replace(r"+ T_d\frac{de(t)}{dt}", "")
            equation.string = re.sub(r"T_i", Ti, equation.string)
            equation.string = re.sub(r"T_d", Td, equation.string)

        self.handler.setHtml(self.template.prettify())

    def set_equation_type(self):
        self.eq_type = "parallel" if self.eq_type == "academic" else "academic"

# This Python file uses the following encoding: utf-8
import re
from bs4 import BeautifulSoup as bs
from PySide6.QtCore import QFile, QIODevice, Slot
import rc_resources

class MathEquation:
    integral = r"\int_{0}^{t}e(\tau) d\tau"
    integral_ti_start = r"\frac{1}{"
    integral_ti_stop = r"}\int_{0}^{t}e(\tau) d\tau"
    derivative = r"\frac{de(t)}{dt}"
    beginning = r"$$u(t) = "
    ending = r"$$"

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

            equation.string = self.beginning
            equation.string += "" if Kp == "0.00" else ("e(t)" if Kp == "1.00" else Kp + "e(t)")
            equation.string += "" if Ki == "0.00" else ((self.integral if 
                                                         equation.string == self.beginning else
                                                           " + " + self.integral) if 
                                                           Ki == "1.00" else 
                                                           (Ki + self.integral if 
                                                            equation.string == self.beginning else 
                                                            " + " + Ki + self.integral))
            equation.string += "" if Kd == "0.00" else ((self.derivative if 
                                                         equation.string == self.beginning else
                                                           " + " + self.derivative) if 
                                                           Kd == "1.00" else 
                                                           (Kd + self.derivative if 
                                                            equation.string == self.beginning else 
                                                            " + " + Kd + self.derivative))
            if equation.string == self.beginning:
                equation.string += "0"
            equation.string += self.ending
        else:
            equation = self.template.find("mathjax", {"id": "academic"})
            not_equation = self.template.find("mathjax", {"id": "parallel"})
            equation["style"] = "font-size:2.3em; display: block;"
            not_equation["style"] = "font-size:2.3em; display: none;"

            equation.string = self.beginning
            if Kp != "0.00":   
                equation.string += "(e(t)" if Kp == "1.00" else Kp + "(e(t)"

                num_of_insides = 0
                
                if Ki != "0.00":
                    equation.string += " + " + self.integral_ti_stop[1:] if Ti == "1.00" else " + " + self.integral_ti_start + Ti + self.integral_ti_stop
                    num_of_insides += 1
                if Kd != "0.00":
                    equation.string += " + " + self.derivative if Td == "1.00" else " + " + Td + self.derivative
                    num_of_insides += 1
                if num_of_insides > 0:
                    equation.string += ")"
                else:
                    equation.string = self.beginning
                    equation.string += "e(t)" if Kp == "1.00" else Kp + "e(t)"
            if equation.string == self.beginning:
                equation.string += "0"
            equation.string += self.ending

        self.handler.setHtml(self.template.prettify())

    def set_equation_type(self):
        self.eq_type = "parallel" if self.eq_type == "academic" else "academic"

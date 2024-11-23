# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QFrame, QHBoxLayout,
    QLabel, QLayout, QMainWindow, QPushButton,
    QSizePolicy, QSlider, QSpacerItem, QSpinBox,
    QStackedWidget, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(1212, 800)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.menubar = QFrame(self.centralwidget)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setFrameShape(QFrame.StyledPanel)
        self.menubar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.menubar)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnHeaterControls = QPushButton(self.menubar)
        self.btnHeaterControls.setObjectName(u"btnHeaterControls")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnHeaterControls.sizePolicy().hasHeightForWidth())
        self.btnHeaterControls.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.btnHeaterControls)

        self.btnFanControls = QPushButton(self.menubar)
        self.btnFanControls.setObjectName(u"btnFanControls")

        self.horizontalLayout.addWidget(self.btnFanControls)

        self.btnDataExport = QPushButton(self.menubar)
        self.btnDataExport.setObjectName(u"btnDataExport")

        self.horizontalLayout.addWidget(self.btnDataExport)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnHelp = QPushButton(self.menubar)
        self.btnHelp.setObjectName(u"btnHelp")

        self.horizontalLayout.addWidget(self.btnHelp)


        self.verticalLayout_2.addWidget(self.menubar)

        self.container = QStackedWidget(self.centralwidget)
        self.container.setObjectName(u"container")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.container.sizePolicy().hasHeightForWidth())
        self.container.setSizePolicy(sizePolicy1)
        self.Controls = QWidget()
        self.Controls.setObjectName(u"Controls")
        self.verticalLayout = QVBoxLayout(self.Controls)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stackControllerDesc = QStackedWidget(self.Controls)
        self.stackControllerDesc.setObjectName(u"stackControllerDesc")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.stackControllerDesc.sizePolicy().hasHeightForWidth())
        self.stackControllerDesc.setSizePolicy(sizePolicy2)
        font = QFont()
        font.setPointSize(12)
        self.stackControllerDesc.setFont(font)
        self.controllerDescHeater = QWidget()
        self.controllerDescHeater.setObjectName(u"controllerDescHeater")
        self.horizontalLayout_17 = QHBoxLayout(self.controllerDescHeater)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.lblControls = QLabel(self.controllerDescHeater)
        self.lblControls.setObjectName(u"lblControls")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(12)
        font1.setBold(False)
        self.lblControls.setFont(font1)

        self.horizontalLayout_17.addWidget(self.lblControls)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_12)

        self.pushButton_7 = QPushButton(self.controllerDescHeater)
        self.pushButton_7.setObjectName(u"pushButton_7")
        font2 = QFont()
        font2.setPointSize(9)
        self.pushButton_7.setFont(font2)
        self.pushButton_7.setCheckable(True)

        self.horizontalLayout_17.addWidget(self.pushButton_7)

        self.stackControllerDesc.addWidget(self.controllerDescHeater)
        self.controllerDescFan = QWidget()
        self.controllerDescFan.setObjectName(u"controllerDescFan")
        self.horizontalLayout_18 = QHBoxLayout(self.controllerDescFan)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_21 = QLabel(self.controllerDescFan)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font)

        self.horizontalLayout_18.addWidget(self.label_21)

        self.horizontalSpacer_13 = QSpacerItem(889, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_13)

        self.pushButton_8 = QPushButton(self.controllerDescFan)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setFont(font2)
        self.pushButton_8.setCheckable(True)

        self.horizontalLayout_18.addWidget(self.pushButton_8)

        self.stackControllerDesc.addWidget(self.controllerDescFan)

        self.verticalLayout.addWidget(self.stackControllerDesc)

        self.stackControllerSelect = QStackedWidget(self.Controls)
        self.stackControllerSelect.setObjectName(u"stackControllerSelect")
        sizePolicy2.setHeightForWidth(self.stackControllerSelect.sizePolicy().hasHeightForWidth())
        self.stackControllerSelect.setSizePolicy(sizePolicy2)
        self.pageHeaterControllerSelect = QWidget()
        self.pageHeaterControllerSelect.setObjectName(u"pageHeaterControllerSelect")
        self.horizontalLayout_3 = QHBoxLayout(self.pageHeaterControllerSelect)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_9 = QFrame(self.pageHeaterControllerSelect)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.lblHeaterController = QLabel(self.frame_9)
        self.lblHeaterController.setObjectName(u"lblHeaterController")

        self.horizontalLayout_14.addWidget(self.lblHeaterController)

        self.btnHeaterControllerSetBB = QPushButton(self.frame_9)
        self.btnHeaterControllerSetBB.setObjectName(u"btnHeaterControllerSetBB")
        self.btnHeaterControllerSetBB.setCheckable(True)
        self.btnHeaterControllerSetBB.setChecked(True)

        self.horizontalLayout_14.addWidget(self.btnHeaterControllerSetBB)

        self.btnHeaterControllerSetPID = QPushButton(self.frame_9)
        self.btnHeaterControllerSetPID.setObjectName(u"btnHeaterControllerSetPID")
        self.btnHeaterControllerSetPID.setCheckable(True)

        self.horizontalLayout_14.addWidget(self.btnHeaterControllerSetPID)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_2)


        self.horizontalLayout_3.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.pageHeaterControllerSelect)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_7 = QLabel(self.frame_10)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_15.addWidget(self.label_7)

        self.btnHeaterControllerSetHighPower = QPushButton(self.frame_10)
        self.btnHeaterControllerSetHighPower.setObjectName(u"btnHeaterControllerSetHighPower")
        self.btnHeaterControllerSetHighPower.setCheckable(True)
        self.btnHeaterControllerSetHighPower.setChecked(True)

        self.horizontalLayout_15.addWidget(self.btnHeaterControllerSetHighPower)

        self.btnHeaterControllerSetLowPower = QPushButton(self.frame_10)
        self.btnHeaterControllerSetLowPower.setObjectName(u"btnHeaterControllerSetLowPower")
        self.btnHeaterControllerSetLowPower.setCheckable(True)

        self.horizontalLayout_15.addWidget(self.btnHeaterControllerSetLowPower)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_10)


        self.horizontalLayout_3.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.pageHeaterControllerSelect)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_20 = QLabel(self.frame_11)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_16.addWidget(self.label_20)

        self.btnHeaterControllerSetLeftCoil = QPushButton(self.frame_11)
        self.btnHeaterControllerSetLeftCoil.setObjectName(u"btnHeaterControllerSetLeftCoil")
        self.btnHeaterControllerSetLeftCoil.setCheckable(True)
        self.btnHeaterControllerSetLeftCoil.setChecked(True)

        self.horizontalLayout_16.addWidget(self.btnHeaterControllerSetLeftCoil)

        self.btnHeaterControllerSetRightCoil = QPushButton(self.frame_11)
        self.btnHeaterControllerSetRightCoil.setObjectName(u"btnHeaterControllerSetRightCoil")
        self.btnHeaterControllerSetRightCoil.setCheckable(True)

        self.horizontalLayout_16.addWidget(self.btnHeaterControllerSetRightCoil)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_11)


        self.horizontalLayout_3.addWidget(self.frame_11)

        self.stackControllerSelect.addWidget(self.pageHeaterControllerSelect)
        self.pageFanControllerSelect = QWidget()
        self.pageFanControllerSelect.setObjectName(u"pageFanControllerSelect")
        self.horizontalLayout_7 = QHBoxLayout(self.pageFanControllerSelect)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_9 = QLabel(self.pageFanControllerSelect)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_7.addWidget(self.label_9)

        self.btnFanControllerSetBB = QPushButton(self.pageFanControllerSelect)
        self.btnFanControllerSetBB.setObjectName(u"btnFanControllerSetBB")
        self.btnFanControllerSetBB.setCheckable(True)
        self.btnFanControllerSetBB.setChecked(True)

        self.horizontalLayout_7.addWidget(self.btnFanControllerSetBB)

        self.btnFanControllerSetPID = QPushButton(self.pageFanControllerSelect)
        self.btnFanControllerSetPID.setObjectName(u"btnFanControllerSetPID")
        self.btnFanControllerSetPID.setCheckable(True)

        self.horizontalLayout_7.addWidget(self.btnFanControllerSetPID)

        self.horizontalSpacer_4 = QSpacerItem(869, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_4)

        self.stackControllerSelect.addWidget(self.pageFanControllerSelect)

        self.verticalLayout.addWidget(self.stackControllerSelect)

        self.stackController = QStackedWidget(self.Controls)
        self.stackController.setObjectName(u"stackController")
        sizePolicy2.setHeightForWidth(self.stackController.sizePolicy().hasHeightForWidth())
        self.stackController.setSizePolicy(sizePolicy2)
        self.pageHeaterControllerConfigBB = QWidget()
        self.pageHeaterControllerConfigBB.setObjectName(u"pageHeaterControllerConfigBB")
        self.horizontalLayout_2 = QHBoxLayout(self.pageHeaterControllerConfigBB)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.frame = QFrame(self.pageHeaterControllerConfigBB)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout_4.addWidget(self.label)

        self.inHeaterBBSetValue = QSpinBox(self.frame)
        self.inHeaterBBSetValue.setObjectName(u"inHeaterBBSetValue")
        self.inHeaterBBSetValue.setMinimumSize(QSize(100, 0))
        self.inHeaterBBSetValue.setMaximum(100)

        self.horizontalLayout_4.addWidget(self.inHeaterBBSetValue)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_4.addWidget(self.label_2)


        self.horizontalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.pageHeaterControllerConfigBB)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_5.addWidget(self.label_3)

        self.inHeaterBBHysteresis = QSpinBox(self.frame_2)
        self.inHeaterBBHysteresis.setObjectName(u"inHeaterBBHysteresis")
        self.inHeaterBBHysteresis.setMinimumSize(QSize(100, 0))
        self.inHeaterBBHysteresis.setMaximum(100)

        self.horizontalLayout_5.addWidget(self.inHeaterBBHysteresis)

        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_5.addWidget(self.label_4)


        self.horizontalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.pageHeaterControllerConfigBB)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_6.addWidget(self.label_5)

        self.inHeaterBBPower = QSlider(self.frame_3)
        self.inHeaterBBPower.setObjectName(u"inHeaterBBPower")
        self.inHeaterBBPower.setMaximumSize(QSize(200, 16777215))
        self.inHeaterBBPower.setMaximum(100)
        self.inHeaterBBPower.setSingleStep(1)
        self.inHeaterBBPower.setPageStep(1)
        self.inHeaterBBPower.setOrientation(Qt.Horizontal)
        self.inHeaterBBPower.setTickPosition(QSlider.NoTicks)
        self.inHeaterBBPower.setTickInterval(1)

        self.horizontalLayout_6.addWidget(self.inHeaterBBPower)

        self.lblPower = QLabel(self.frame_3)
        self.lblPower.setObjectName(u"lblPower")

        self.horizontalLayout_6.addWidget(self.lblPower)

        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_6.addWidget(self.label_6)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)


        self.horizontalLayout_2.addWidget(self.frame_3)

        self.stackController.addWidget(self.pageHeaterControllerConfigBB)
        self.pageHeaterControllerConfigPID = QWidget()
        self.pageHeaterControllerConfigPID.setObjectName(u"pageHeaterControllerConfigPID")
        self.verticalLayout_5 = QVBoxLayout(self.pageHeaterControllerConfigPID)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_22 = QFrame(self.pageHeaterControllerConfigPID)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.frame_4 = QFrame(self.frame_22)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_10 = QLabel(self.frame_4)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_9.addWidget(self.label_10)

        self.inHeaterPIDSetValue = QSpinBox(self.frame_4)
        self.inHeaterPIDSetValue.setObjectName(u"inHeaterPIDSetValue")
        self.inHeaterPIDSetValue.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_9.addWidget(self.inHeaterPIDSetValue)

        self.label_11 = QLabel(self.frame_4)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_9.addWidget(self.label_11)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_5)


        self.horizontalLayout_30.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_22)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_12 = QLabel(self.frame_5)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_10.addWidget(self.label_12)

        self.inHeaterPID_Kp = QDoubleSpinBox(self.frame_5)
        self.inHeaterPID_Kp.setObjectName(u"inHeaterPID_Kp")
        self.inHeaterPID_Kp.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_10.addWidget(self.inHeaterPID_Kp)

        self.label_13 = QLabel(self.frame_5)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_10.addWidget(self.label_13)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_6)


        self.horizontalLayout_30.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_22)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_14 = QLabel(self.frame_6)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_11.addWidget(self.label_14)

        self.inHeaterPID_Ki = QDoubleSpinBox(self.frame_6)
        self.inHeaterPID_Ki.setObjectName(u"inHeaterPID_Ki")
        self.inHeaterPID_Ki.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_11.addWidget(self.inHeaterPID_Ki)

        self.label_15 = QLabel(self.frame_6)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_11.addWidget(self.label_15)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_7)


        self.horizontalLayout_30.addWidget(self.frame_6)

        self.frame_23 = QFrame(self.frame_22)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_38 = QLabel(self.frame_23)
        self.label_38.setObjectName(u"label_38")

        self.horizontalLayout_31.addWidget(self.label_38)

        self.inHeaterPID_Ti = QDoubleSpinBox(self.frame_23)
        self.inHeaterPID_Ti.setObjectName(u"inHeaterPID_Ti")
        self.inHeaterPID_Ti.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_31.addWidget(self.inHeaterPID_Ti)

        self.label_44 = QLabel(self.frame_23)
        self.label_44.setObjectName(u"label_44")

        self.horizontalLayout_31.addWidget(self.label_44)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_23)


        self.horizontalLayout_30.addWidget(self.frame_23)

        self.frame_7 = QFrame(self.frame_22)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_16 = QLabel(self.frame_7)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_12.addWidget(self.label_16)

        self.inHeaterPID_Kd = QDoubleSpinBox(self.frame_7)
        self.inHeaterPID_Kd.setObjectName(u"inHeaterPID_Kd")
        self.inHeaterPID_Kd.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_12.addWidget(self.inHeaterPID_Kd)

        self.label_17 = QLabel(self.frame_7)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_12.addWidget(self.label_17)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_8)


        self.horizontalLayout_30.addWidget(self.frame_7)

        self.frame_24 = QFrame(self.frame_22)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_43 = QLabel(self.frame_24)
        self.label_43.setObjectName(u"label_43")

        self.horizontalLayout_8.addWidget(self.label_43)

        self.inHeaterPID_Td = QDoubleSpinBox(self.frame_24)
        self.inHeaterPID_Td.setObjectName(u"inHeaterPID_Td")
        self.inHeaterPID_Td.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_8.addWidget(self.inHeaterPID_Td)

        self.label_45 = QLabel(self.frame_24)
        self.label_45.setObjectName(u"label_45")

        self.horizontalLayout_8.addWidget(self.label_45)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_24)


        self.horizontalLayout_30.addWidget(self.frame_24)

        self.frame_8 = QFrame(self.frame_22)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_18 = QLabel(self.frame_8)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_13.addWidget(self.label_18)

        self.inHeaterPID_Kaw = QDoubleSpinBox(self.frame_8)
        self.inHeaterPID_Kaw.setObjectName(u"inHeaterPID_Kaw")
        self.inHeaterPID_Kaw.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_13.addWidget(self.inHeaterPID_Kaw)

        self.label_19 = QLabel(self.frame_8)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_13.addWidget(self.label_19)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_9)


        self.horizontalLayout_30.addWidget(self.frame_8)


        self.verticalLayout_5.addWidget(self.frame_22)

        self.frame_25 = QFrame(self.pageHeaterControllerConfigPID)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_25)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.heaterEquation = QVBoxLayout()
        self.heaterEquation.setObjectName(u"heaterEquation")

        self.verticalLayout_6.addLayout(self.heaterEquation)


        self.verticalLayout_5.addWidget(self.frame_25)

        self.stackController.addWidget(self.pageHeaterControllerConfigPID)
        self.pageFanControllerConfigBB = QWidget()
        self.pageFanControllerConfigBB.setObjectName(u"pageFanControllerConfigBB")
        self.horizontalLayout_19 = QHBoxLayout(self.pageFanControllerConfigBB)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.frame_12 = QFrame(self.pageFanControllerConfigBB)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_22 = QLabel(self.frame_12)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_20.addWidget(self.label_22)

        self.inFanBBSetValue = QSpinBox(self.frame_12)
        self.inFanBBSetValue.setObjectName(u"inFanBBSetValue")
        self.inFanBBSetValue.setMinimumSize(QSize(100, 0))
        self.inFanBBSetValue.setMaximum(6000)

        self.horizontalLayout_20.addWidget(self.inFanBBSetValue)

        self.label_23 = QLabel(self.frame_12)
        self.label_23.setObjectName(u"label_23")

        self.horizontalLayout_20.addWidget(self.label_23)

        self.horizontalSpacer_14 = QSpacerItem(318, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_14)


        self.horizontalLayout_19.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.pageFanControllerConfigBB)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_24 = QLabel(self.frame_13)
        self.label_24.setObjectName(u"label_24")

        self.horizontalLayout_21.addWidget(self.label_24)

        self.inFanBBHysteresis = QSpinBox(self.frame_13)
        self.inFanBBHysteresis.setObjectName(u"inFanBBHysteresis")
        self.inFanBBHysteresis.setMinimumSize(QSize(100, 0))
        self.inFanBBHysteresis.setMaximum(500)

        self.horizontalLayout_21.addWidget(self.inFanBBHysteresis)

        self.label_25 = QLabel(self.frame_13)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout_21.addWidget(self.label_25)

        self.horizontalSpacer_15 = QSpacerItem(353, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_15)


        self.horizontalLayout_19.addWidget(self.frame_13)

        self.stackController.addWidget(self.pageFanControllerConfigBB)
        self.pageFanControllerConfigPID = QWidget()
        self.pageFanControllerConfigPID.setObjectName(u"pageFanControllerConfigPID")
        self.verticalLayout_3 = QVBoxLayout(self.pageFanControllerConfigPID)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_20 = QFrame(self.pageFanControllerConfigPID)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.frame_14 = QFrame(self.frame_20)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_26 = QLabel(self.frame_14)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_23.addWidget(self.label_26)

        self.inFanPIDSetValue = QSpinBox(self.frame_14)
        self.inFanPIDSetValue.setObjectName(u"inFanPIDSetValue")
        self.inFanPIDSetValue.setMinimumSize(QSize(80, 0))
        self.inFanPIDSetValue.setMaximum(6000)

        self.horizontalLayout_23.addWidget(self.inFanPIDSetValue)

        self.label_27 = QLabel(self.frame_14)
        self.label_27.setObjectName(u"label_27")

        self.horizontalLayout_23.addWidget(self.label_27)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_16)


        self.horizontalLayout_22.addWidget(self.frame_14)

        self.frame_15 = QFrame(self.frame_20)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_28 = QLabel(self.frame_15)
        self.label_28.setObjectName(u"label_28")

        self.horizontalLayout_24.addWidget(self.label_28)

        self.inFanPID_Kp = QDoubleSpinBox(self.frame_15)
        self.inFanPID_Kp.setObjectName(u"inFanPID_Kp")
        self.inFanPID_Kp.setMinimumSize(QSize(80, 0))
        self.inFanPID_Kp.setMaximum(999.990000000000009)

        self.horizontalLayout_24.addWidget(self.inFanPID_Kp)

        self.label_29 = QLabel(self.frame_15)
        self.label_29.setObjectName(u"label_29")

        self.horizontalLayout_24.addWidget(self.label_29)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_17)


        self.horizontalLayout_22.addWidget(self.frame_15)

        self.frame_16 = QFrame(self.frame_20)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_30 = QLabel(self.frame_16)
        self.label_30.setObjectName(u"label_30")

        self.horizontalLayout_25.addWidget(self.label_30)

        self.inFanPID_Ki = QDoubleSpinBox(self.frame_16)
        self.inFanPID_Ki.setObjectName(u"inFanPID_Ki")
        self.inFanPID_Ki.setMinimumSize(QSize(80, 0))
        self.inFanPID_Ki.setMaximum(999.990000000000009)

        self.horizontalLayout_25.addWidget(self.inFanPID_Ki)

        self.label_31 = QLabel(self.frame_16)
        self.label_31.setObjectName(u"label_31")

        self.horizontalLayout_25.addWidget(self.label_31)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_18)


        self.horizontalLayout_22.addWidget(self.frame_16)

        self.frame_19 = QFrame(self.frame_20)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_40 = QLabel(self.frame_19)
        self.label_40.setObjectName(u"label_40")

        self.horizontalLayout_28.addWidget(self.label_40)

        self.inFanPID_Ti = QDoubleSpinBox(self.frame_19)
        self.inFanPID_Ti.setObjectName(u"inFanPID_Ti")
        self.inFanPID_Ti.setMinimumSize(QSize(80, 0))
        self.inFanPID_Ti.setMaximum(999.990000000000009)

        self.horizontalLayout_28.addWidget(self.inFanPID_Ti)

        self.label_39 = QLabel(self.frame_19)
        self.label_39.setObjectName(u"label_39")

        self.horizontalLayout_28.addWidget(self.label_39)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_21)


        self.horizontalLayout_22.addWidget(self.frame_19)

        self.frame_17 = QFrame(self.frame_20)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_32 = QLabel(self.frame_17)
        self.label_32.setObjectName(u"label_32")

        self.horizontalLayout_26.addWidget(self.label_32)

        self.inFanPID_Kd = QDoubleSpinBox(self.frame_17)
        self.inFanPID_Kd.setObjectName(u"inFanPID_Kd")
        self.inFanPID_Kd.setMinimumSize(QSize(80, 0))
        self.inFanPID_Kd.setMaximum(999.990000000000009)

        self.horizontalLayout_26.addWidget(self.inFanPID_Kd)

        self.label_33 = QLabel(self.frame_17)
        self.label_33.setObjectName(u"label_33")

        self.horizontalLayout_26.addWidget(self.label_33)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_19)


        self.horizontalLayout_22.addWidget(self.frame_17)

        self.frame_21 = QFrame(self.frame_20)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_42 = QLabel(self.frame_21)
        self.label_42.setObjectName(u"label_42")

        self.horizontalLayout_29.addWidget(self.label_42)

        self.inFanPID_Td = QDoubleSpinBox(self.frame_21)
        self.inFanPID_Td.setObjectName(u"inFanPID_Td")
        self.inFanPID_Td.setMinimumSize(QSize(80, 0))
        self.inFanPID_Td.setMaximum(999.990000000000009)

        self.horizontalLayout_29.addWidget(self.inFanPID_Td)

        self.label_41 = QLabel(self.frame_21)
        self.label_41.setObjectName(u"label_41")

        self.horizontalLayout_29.addWidget(self.label_41)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_22)


        self.horizontalLayout_22.addWidget(self.frame_21)

        self.frame_18 = QFrame(self.frame_20)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_34 = QLabel(self.frame_18)
        self.label_34.setObjectName(u"label_34")

        self.horizontalLayout_27.addWidget(self.label_34)

        self.inFanPID_Kaw = QDoubleSpinBox(self.frame_18)
        self.inFanPID_Kaw.setObjectName(u"inFanPID_Kaw")
        self.inFanPID_Kaw.setMinimumSize(QSize(80, 0))
        self.inFanPID_Kaw.setMaximum(1.000000000000000)

        self.horizontalLayout_27.addWidget(self.inFanPID_Kaw)

        self.label_35 = QLabel(self.frame_18)
        self.label_35.setObjectName(u"label_35")

        self.horizontalLayout_27.addWidget(self.label_35)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_20)


        self.horizontalLayout_22.addWidget(self.frame_18)


        self.verticalLayout_3.addWidget(self.frame_20)

        self.frame_26 = QFrame(self.pageFanControllerConfigPID)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_26)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.fanEquation = QVBoxLayout()
        self.fanEquation.setObjectName(u"fanEquation")

        self.verticalLayout_7.addLayout(self.fanEquation)


        self.verticalLayout_3.addWidget(self.frame_26)

        self.stackController.addWidget(self.pageFanControllerConfigPID)

        self.verticalLayout.addWidget(self.stackController)

        self.stackGraphs = QStackedWidget(self.Controls)
        self.stackGraphs.setObjectName(u"stackGraphs")
        sizePolicy1.setHeightForWidth(self.stackGraphs.sizePolicy().hasHeightForWidth())
        self.stackGraphs.setSizePolicy(sizePolicy1)
        self.FanGraphs = QWidget()
        self.FanGraphs.setObjectName(u"FanGraphs")
        self.verticalLayout_4 = QVBoxLayout(self.FanGraphs)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.stackGraphs.addWidget(self.FanGraphs)
        self.HeaterGraphs = QWidget()
        self.HeaterGraphs.setObjectName(u"HeaterGraphs")
        self.stackGraphs.addWidget(self.HeaterGraphs)

        self.verticalLayout.addWidget(self.stackGraphs)

        self.container.addWidget(self.Controls)
        self.Export = QWidget()
        self.Export.setObjectName(u"Export")
        self.label_36 = QLabel(self.Export)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(280, 380, 49, 16))
        self.container.addWidget(self.Export)
        self.Help = QWidget()
        self.Help.setObjectName(u"Help")
        self.label_37 = QLabel(self.Help)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(330, 400, 49, 16))
        self.container.addWidget(self.Help)

        self.verticalLayout_2.addWidget(self.container)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.container.setCurrentIndex(0)
        self.stackControllerDesc.setCurrentIndex(1)
        self.stackControllerSelect.setCurrentIndex(0)
        self.stackController.setCurrentIndex(0)
        self.stackGraphs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sterowanie Procesami Ci\u0105g\u0142ymi", None))
        self.btnHeaterControls.setText(QCoreApplication.translate("MainWindow", u"Grza\u0142ka", None))
        self.btnFanControls.setText(QCoreApplication.translate("MainWindow", u"Wentylator", None))
        self.btnDataExport.setText(QCoreApplication.translate("MainWindow", u"Eksport danych", None))
        self.btnHelp.setText(QCoreApplication.translate("MainWindow", u"Pomoc", None))
        self.lblControls.setText(QCoreApplication.translate("MainWindow", u"Ustawienia grza\u0142ki", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Ustawienia wentylatora", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.lblHeaterController.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Wyb\u00f3r regulatora	</p></body></html>", None))
        self.btnHeaterControllerSetBB.setText(QCoreApplication.translate("MainWindow", u"Dwupo\u0142o\u017ceniowy", None))
        self.btnHeaterControllerSetPID.setText(QCoreApplication.translate("MainWindow", u"PID", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Wyb\u00f3r grza\u0142ki	</p></body></html>", None))
        self.btnHeaterControllerSetHighPower.setText(QCoreApplication.translate("MainWindow", u"17 \u03a9", None))
        self.btnHeaterControllerSetLowPower.setText(QCoreApplication.translate("MainWindow", u"33 \u03a9", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Wyb\u00f3r temperatury odniesienia	</p></body></html>", None))
        self.btnHeaterControllerSetLeftCoil.setText(QCoreApplication.translate("MainWindow", u"Lewa", None))
        self.btnHeaterControllerSetRightCoil.setText(QCoreApplication.translate("MainWindow", u"Prawa", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Wyb\u00f3r regulatora	</p></body></html>", None))
        self.btnFanControllerSetBB.setText(QCoreApplication.translate("MainWindow", u"Dwupo\u0142o\u017ceniowy", None))
        self.btnFanControllerSetPID.setText(QCoreApplication.translate("MainWindow", u"PID", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Warto\u015b\u0107 zadana	</p></body></html>", None))
#if QT_CONFIG(statustip)
        self.inHeaterBBSetValue.setStatusTip(QCoreApplication.translate("MainWindow", u"Min: 0 | Max: 100", None))
#endif // QT_CONFIG(statustip)
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u00b0C</p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Histereza	</p></body></html>", None))
#if QT_CONFIG(statustip)
        self.inHeaterBBHysteresis.setStatusTip(QCoreApplication.translate("MainWindow", u"Min: 0 | Max: 100", None))
#endif // QT_CONFIG(statustip)
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u00b0C</p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Moc	</p></body></html>", None))
        self.lblPower.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"W", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Warto\u015b\u0107 zadana	</p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u00b0C</p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>K<span style=\" vertical-align:sub;\">p</span></p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"jed", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>K<span style=\" vertical-align:sub;\">i</span></p></body></html>", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"jed", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>T<span style=\" vertical-align:sub;\">i</span></p></body></html>", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"jed", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>K<span style=\" vertical-align:sub;\">d</span></p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"jed", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>T<span style=\" vertical-align:sub;\">d</span></p></body></html>", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"jed", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>K<span style=\" vertical-align:sub;\">aw</span></p></body></html>", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"jed", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Warto\u015b\u0107 zadana	</p></body></html>", None))
#if QT_CONFIG(statustip)
        self.inFanBBSetValue.setStatusTip(QCoreApplication.translate("MainWindow", u"Min: 0 | Max: 6000", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.inFanBBSetValue.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"RPM", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Histereza	</p></body></html>", None))
#if QT_CONFIG(statustip)
        self.inFanBBHysteresis.setStatusTip(QCoreApplication.translate("MainWindow", u"Min: 0 | Max: 100", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.inFanBBHysteresis.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"RPM", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Warto\u015b\u0107 zadana	</p></body></html>", None))
#if QT_CONFIG(statustip)
        self.inFanPIDSetValue.setStatusTip(QCoreApplication.translate("MainWindow", u"Min: 0 | Max: 6000", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.inFanPIDSetValue.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"RPM", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>K<span style=\" vertical-align:sub;\">p</span></p></body></html>", None))
#if QT_CONFIG(statustip)
        self.inFanPID_Kp.setStatusTip(QCoreApplication.translate("MainWindow", u"Min: 0.0 | Max: 999.99", None))
#endif // QT_CONFIG(statustip)
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"jed", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>K<span style=\" vertical-align:sub;\">i</span></p></body></html>", None))
#if QT_CONFIG(statustip)
        self.inFanPID_Ki.setStatusTip(QCoreApplication.translate("MainWindow", u"Min: 0.0 | Max: 999.99", None))
#endif // QT_CONFIG(statustip)
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"jed", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>T<span style=\" vertical-align:sub;\">i</span></p></body></html>", None))
#if QT_CONFIG(statustip)
        self.inFanPID_Ti.setStatusTip(QCoreApplication.translate("MainWindow", u"Min: 0.0 | Max: 999.99", None))
#endif // QT_CONFIG(statustip)
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"jed", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>K<span style=\" vertical-align:sub;\">d</span></p></body></html>", None))
#if QT_CONFIG(statustip)
        self.inFanPID_Kd.setStatusTip(QCoreApplication.translate("MainWindow", u"Min: 0.0 | Max: 999.99", None))
#endif // QT_CONFIG(statustip)
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"jed", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>T<span style=\" vertical-align:sub;\">d</span></p></body></html>", None))
#if QT_CONFIG(statustip)
        self.inFanPID_Td.setStatusTip(QCoreApplication.translate("MainWindow", u"Min: 0.0 | Max: 999.99", None))
#endif // QT_CONFIG(statustip)
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"jed", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>K<span style=\" vertical-align:sub;\">aw</span></p></body></html>", None))
#if QT_CONFIG(statustip)
        self.inFanPID_Kaw.setStatusTip(QCoreApplication.translate("MainWindow", u"Min: 0.0 | Max: 1.0", None))
#endif // QT_CONFIG(statustip)
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"jed", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi


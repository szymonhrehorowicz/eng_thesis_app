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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDoubleSpinBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLayout,
    QMainWindow, QPushButton, QSizePolicy, QSlider,
    QSpacerItem, QSpinBox, QStackedWidget, QStatusBar,
    QVBoxLayout, QWidget)

from StackedWidget import StackedWidget
import rc_resources

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(1212, 800)
        icon = QIcon()
        icon.addFile(u":/assets/assets/controller.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"")
        MainWindow.setLocale(QLocale(QLocale.Polish, QLocale.Poland))
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
        self.btnConnect = QPushButton(self.menubar)
        self.btnConnect.setObjectName(u"btnConnect")
        self.btnConnect.setStyleSheet(u"")
        self.btnConnect.setCheckable(True)

        self.horizontalLayout.addWidget(self.btnConnect)

        self.line = QFrame(self.menubar)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.btnHeaterControls = QPushButton(self.menubar)
        self.btnHeaterControls.setObjectName(u"btnHeaterControls")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnHeaterControls.sizePolicy().hasHeightForWidth())
        self.btnHeaterControls.setSizePolicy(sizePolicy)
        self.btnHeaterControls.setCheckable(True)

        self.horizontalLayout.addWidget(self.btnHeaterControls)

        self.btnFanControls = QPushButton(self.menubar)
        self.btnFanControls.setObjectName(u"btnFanControls")
        self.btnFanControls.setCheckable(True)

        self.horizontalLayout.addWidget(self.btnFanControls)

        self.btnDataExport = QPushButton(self.menubar)
        self.btnDataExport.setObjectName(u"btnDataExport")
        self.btnDataExport.setCheckable(True)

        self.horizontalLayout.addWidget(self.btnDataExport)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnHelp = QPushButton(self.menubar)
        self.btnHelp.setObjectName(u"btnHelp")
        self.btnHelp.setCheckable(True)

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

        self.btnHeaterStart = QPushButton(self.controllerDescHeater)
        self.btnHeaterStart.setObjectName(u"btnHeaterStart")
        font2 = QFont()
        font2.setPointSize(9)
        self.btnHeaterStart.setFont(font2)
        self.btnHeaterStart.setCheckable(True)

        self.horizontalLayout_17.addWidget(self.btnHeaterStart)

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

        self.btnFanStart = QPushButton(self.controllerDescFan)
        self.btnFanStart.setObjectName(u"btnFanStart")
        self.btnFanStart.setFont(font2)
        self.btnFanStart.setCheckable(True)

        self.horizontalLayout_18.addWidget(self.btnFanStart)

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

        self.stackController = StackedWidget(self.Controls)
        self.stackController.setObjectName(u"stackController")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.stackController.sizePolicy().hasHeightForWidth())
        self.stackController.setSizePolicy(sizePolicy3)
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
        self.inHeaterPIDSetValue.setFrame(True)
        self.inHeaterPIDSetValue.setKeyboardTracking(True)
        self.inHeaterPIDSetValue.setMaximum(100)

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
        self.inHeaterPID_Kaw.setMaximum(1.000000000000000)

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
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_25.sizePolicy().hasHeightForWidth())
        self.frame_25.setSizePolicy(sizePolicy4)
        self.frame_25.setMaximumSize(QSize(16777215, 120))
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
        self.frame_26.setMaximumSize(QSize(16777215, 120))
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
        self.pageHeaterBBGraph = QWidget()
        self.pageHeaterBBGraph.setObjectName(u"pageHeaterBBGraph")
        self.verticalLayout_9 = QVBoxLayout(self.pageHeaterBBGraph)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.layHeaterBBGraph = QVBoxLayout()
        self.layHeaterBBGraph.setObjectName(u"layHeaterBBGraph")

        self.verticalLayout_9.addLayout(self.layHeaterBBGraph)

        self.frame_29 = QFrame(self.pageHeaterBBGraph)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_29)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.btnHeaterBB_graph_mode = QPushButton(self.frame_29)
        self.btnHeaterBB_graph_mode.setObjectName(u"btnHeaterBB_graph_mode")
        self.btnHeaterBB_graph_mode.setCheckable(True)
        self.btnHeaterBB_graph_mode.setChecked(False)

        self.gridLayout_4.addWidget(self.btnHeaterBB_graph_mode, 0, 7, 1, 1)

        self.btnHeaterBB_graph_u_max = QPushButton(self.frame_29)
        self.btnHeaterBB_graph_u_max.setObjectName(u"btnHeaterBB_graph_u_max")
        self.btnHeaterBB_graph_u_max.setCheckable(True)
        self.btnHeaterBB_graph_u_max.setChecked(False)

        self.gridLayout_4.addWidget(self.btnHeaterBB_graph_u_max, 0, 3, 1, 1)

        self.btnHeaterBB_graph_Stop = QPushButton(self.frame_29)
        self.btnHeaterBB_graph_Stop.setObjectName(u"btnHeaterBB_graph_Stop")
        icon1 = QIcon()
        icon1.addFile(u":/assets/assets/pause.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnHeaterBB_graph_Stop.setIcon(icon1)
        self.btnHeaterBB_graph_Stop.setCheckable(True)

        self.gridLayout_4.addWidget(self.btnHeaterBB_graph_Stop, 0, 9, 1, 1)

        self.btnHeaterBB_graph_y_1 = QPushButton(self.frame_29)
        self.btnHeaterBB_graph_y_1.setObjectName(u"btnHeaterBB_graph_y_1")
        self.btnHeaterBB_graph_y_1.setCheckable(True)
        self.btnHeaterBB_graph_y_1.setChecked(True)

        self.gridLayout_4.addWidget(self.btnHeaterBB_graph_y_1, 0, 5, 1, 1)

        self.btnHeaterBB_graph_u_min = QPushButton(self.frame_29)
        self.btnHeaterBB_graph_u_min.setObjectName(u"btnHeaterBB_graph_u_min")
        self.btnHeaterBB_graph_u_min.setCheckable(True)
        self.btnHeaterBB_graph_u_min.setChecked(False)

        self.gridLayout_4.addWidget(self.btnHeaterBB_graph_u_min, 0, 4, 1, 1)

        self.btnHeaterBB_graph_y_2 = QPushButton(self.frame_29)
        self.btnHeaterBB_graph_y_2.setObjectName(u"btnHeaterBB_graph_y_2")
        self.btnHeaterBB_graph_y_2.setCheckable(True)
        self.btnHeaterBB_graph_y_2.setChecked(True)

        self.gridLayout_4.addWidget(self.btnHeaterBB_graph_y_2, 0, 6, 1, 1)

        self.btnHeaterBB_graph_Clear = QPushButton(self.frame_29)
        self.btnHeaterBB_graph_Clear.setObjectName(u"btnHeaterBB_graph_Clear")
        icon2 = QIcon()
        icon2.addFile(u":/assets/assets/broom.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnHeaterBB_graph_Clear.setIcon(icon2)

        self.gridLayout_4.addWidget(self.btnHeaterBB_graph_Clear, 1, 9, 1, 1)

        self.btnHeaterBB_graph_x = QPushButton(self.frame_29)
        self.btnHeaterBB_graph_x.setObjectName(u"btnHeaterBB_graph_x")
        self.btnHeaterBB_graph_x.setCheckable(True)
        self.btnHeaterBB_graph_x.setChecked(True)

        self.gridLayout_4.addWidget(self.btnHeaterBB_graph_x, 0, 0, 1, 1)

        self.btnHeaterBB_graph_x_min = QPushButton(self.frame_29)
        self.btnHeaterBB_graph_x_min.setObjectName(u"btnHeaterBB_graph_x_min")
        self.btnHeaterBB_graph_x_min.setCheckable(True)
        self.btnHeaterBB_graph_x_min.setChecked(False)

        self.gridLayout_4.addWidget(self.btnHeaterBB_graph_x_min, 0, 2, 1, 1)

        self.btnHeaterBB_graph_x_max = QPushButton(self.frame_29)
        self.btnHeaterBB_graph_x_max.setObjectName(u"btnHeaterBB_graph_x_max")
        self.btnHeaterBB_graph_x_max.setCheckable(True)
        self.btnHeaterBB_graph_x_max.setChecked(False)

        self.gridLayout_4.addWidget(self.btnHeaterBB_graph_x_max, 0, 1, 1, 1)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_26, 0, 8, 1, 1)


        self.verticalLayout_9.addWidget(self.frame_29)

        self.stackGraphs.addWidget(self.pageHeaterBBGraph)
        self.pageHeaterPIDGraph = QWidget()
        self.pageHeaterPIDGraph.setObjectName(u"pageHeaterPIDGraph")
        self.verticalLayout_11 = QVBoxLayout(self.pageHeaterPIDGraph)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.layHeaterPIDGraph = QVBoxLayout()
        self.layHeaterPIDGraph.setObjectName(u"layHeaterPIDGraph")

        self.verticalLayout_11.addLayout(self.layHeaterPIDGraph)

        self.frame_30 = QFrame(self.pageHeaterPIDGraph)
        self.frame_30.setObjectName(u"frame_30")
        sizePolicy2.setHeightForWidth(self.frame_30.sizePolicy().hasHeightForWidth())
        self.frame_30.setSizePolicy(sizePolicy2)
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_30)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.btnHeaterPID_graph_u_p = QPushButton(self.frame_30)
        self.btnHeaterPID_graph_u_p.setObjectName(u"btnHeaterPID_graph_u_p")
        self.btnHeaterPID_graph_u_p.setCheckable(True)
        self.btnHeaterPID_graph_u_p.setChecked(False)

        self.gridLayout_2.addWidget(self.btnHeaterPID_graph_u_p, 2, 1, 1, 1)

        self.btnHeaterPID_graph_k_p = QPushButton(self.frame_30)
        self.btnHeaterPID_graph_k_p.setObjectName(u"btnHeaterPID_graph_k_p")
        self.btnHeaterPID_graph_k_p.setCheckable(True)
        self.btnHeaterPID_graph_k_p.setChecked(False)

        self.gridLayout_2.addWidget(self.btnHeaterPID_graph_k_p, 0, 4, 1, 1)

        self.btnHeaterPID_graph_y_2 = QPushButton(self.frame_30)
        self.btnHeaterPID_graph_y_2.setObjectName(u"btnHeaterPID_graph_y_2")
        self.btnHeaterPID_graph_y_2.setCheckable(True)
        self.btnHeaterPID_graph_y_2.setChecked(True)

        self.gridLayout_2.addWidget(self.btnHeaterPID_graph_y_2, 2, 7, 1, 1)

        self.btnHeaterPID_graph_mode = QPushButton(self.frame_30)
        self.btnHeaterPID_graph_mode.setObjectName(u"btnHeaterPID_graph_mode")
        self.btnHeaterPID_graph_mode.setCheckable(True)
        self.btnHeaterPID_graph_mode.setChecked(False)

        self.gridLayout_2.addWidget(self.btnHeaterPID_graph_mode, 2, 8, 1, 1)

        self.btnHeaterPID_graph_Stop = QPushButton(self.frame_30)
        self.btnHeaterPID_graph_Stop.setObjectName(u"btnHeaterPID_graph_Stop")
        self.btnHeaterPID_graph_Stop.setIcon(icon1)
        self.btnHeaterPID_graph_Stop.setCheckable(True)

        self.gridLayout_2.addWidget(self.btnHeaterPID_graph_Stop, 0, 10, 1, 1)

        self.btnHeaterPID_graph_u_sat = QPushButton(self.frame_30)
        self.btnHeaterPID_graph_u_sat.setObjectName(u"btnHeaterPID_graph_u_sat")
        self.btnHeaterPID_graph_u_sat.setCheckable(True)
        self.btnHeaterPID_graph_u_sat.setChecked(False)

        self.gridLayout_2.addWidget(self.btnHeaterPID_graph_u_sat, 2, 0, 1, 1)

        self.btnHeaterPID_graph_u_i = QPushButton(self.frame_30)
        self.btnHeaterPID_graph_u_i.setObjectName(u"btnHeaterPID_graph_u_i")
        self.btnHeaterPID_graph_u_i.setCheckable(True)
        self.btnHeaterPID_graph_u_i.setChecked(False)

        self.gridLayout_2.addWidget(self.btnHeaterPID_graph_u_i, 2, 2, 1, 1)

        self.btnHeaterPID_graph_y_1 = QPushButton(self.frame_30)
        self.btnHeaterPID_graph_y_1.setObjectName(u"btnHeaterPID_graph_y_1")
        self.btnHeaterPID_graph_y_1.setCheckable(True)
        self.btnHeaterPID_graph_y_1.setChecked(True)

        self.gridLayout_2.addWidget(self.btnHeaterPID_graph_y_1, 2, 6, 1, 1)

        self.btnHeaterPID_graph_aw_int_e = QPushButton(self.frame_30)
        self.btnHeaterPID_graph_aw_int_e.setObjectName(u"btnHeaterPID_graph_aw_int_e")
        self.btnHeaterPID_graph_aw_int_e.setCheckable(True)
        self.btnHeaterPID_graph_aw_int_e.setChecked(False)

        self.gridLayout_2.addWidget(self.btnHeaterPID_graph_aw_int_e, 0, 3, 1, 1)

        self.btnHeaterPID_graph_u_d = QPushButton(self.frame_30)
        self.btnHeaterPID_graph_u_d.setObjectName(u"btnHeaterPID_graph_u_d")
        self.btnHeaterPID_graph_u_d.setCheckable(True)
        self.btnHeaterPID_graph_u_d.setChecked(False)

        self.gridLayout_2.addWidget(self.btnHeaterPID_graph_u_d, 2, 3, 1, 1)

        self.btnHeaterPID_graph_e = QPushButton(self.frame_30)
        self.btnHeaterPID_graph_e.setObjectName(u"btnHeaterPID_graph_e")
        self.btnHeaterPID_graph_e.setCheckable(True)
        self.btnHeaterPID_graph_e.setChecked(False)

        self.gridLayout_2.addWidget(self.btnHeaterPID_graph_e, 0, 1, 1, 1)

        self.btnHeaterPID_graph_u_max = QPushButton(self.frame_30)
        self.btnHeaterPID_graph_u_max.setObjectName(u"btnHeaterPID_graph_u_max")
        self.btnHeaterPID_graph_u_max.setCheckable(True)
        self.btnHeaterPID_graph_u_max.setChecked(False)

        self.gridLayout_2.addWidget(self.btnHeaterPID_graph_u_max, 2, 4, 1, 1)

        self.btnHeaterPID_graph_u = QPushButton(self.frame_30)
        self.btnHeaterPID_graph_u.setObjectName(u"btnHeaterPID_graph_u")
        self.btnHeaterPID_graph_u.setCheckable(True)
        self.btnHeaterPID_graph_u.setChecked(False)

        self.gridLayout_2.addWidget(self.btnHeaterPID_graph_u, 0, 8, 1, 1)

        self.btnHeaterPID_graph_k_aw = QPushButton(self.frame_30)
        self.btnHeaterPID_graph_k_aw.setObjectName(u"btnHeaterPID_graph_k_aw")
        self.btnHeaterPID_graph_k_aw.setCheckable(True)
        self.btnHeaterPID_graph_k_aw.setChecked(False)

        self.gridLayout_2.addWidget(self.btnHeaterPID_graph_k_aw, 0, 7, 1, 1)

        self.btnHeaterPID_graph_Clear = QPushButton(self.frame_30)
        self.btnHeaterPID_graph_Clear.setObjectName(u"btnHeaterPID_graph_Clear")
        self.btnHeaterPID_graph_Clear.setIcon(icon2)

        self.gridLayout_2.addWidget(self.btnHeaterPID_graph_Clear, 2, 10, 1, 1)

        self.btnHeaterPID_graph_k_d = QPushButton(self.frame_30)
        self.btnHeaterPID_graph_k_d.setObjectName(u"btnHeaterPID_graph_k_d")
        self.btnHeaterPID_graph_k_d.setCheckable(True)
        self.btnHeaterPID_graph_k_d.setChecked(False)

        self.gridLayout_2.addWidget(self.btnHeaterPID_graph_k_d, 0, 6, 1, 1)

        self.btnHeaterPID_graph_u_min = QPushButton(self.frame_30)
        self.btnHeaterPID_graph_u_min.setObjectName(u"btnHeaterPID_graph_u_min")
        self.btnHeaterPID_graph_u_min.setCheckable(True)
        self.btnHeaterPID_graph_u_min.setChecked(False)

        self.gridLayout_2.addWidget(self.btnHeaterPID_graph_u_min, 2, 5, 1, 1)

        self.btnHeaterPID_graph_k_i = QPushButton(self.frame_30)
        self.btnHeaterPID_graph_k_i.setObjectName(u"btnHeaterPID_graph_k_i")
        self.btnHeaterPID_graph_k_i.setCheckable(True)
        self.btnHeaterPID_graph_k_i.setChecked(False)

        self.gridLayout_2.addWidget(self.btnHeaterPID_graph_k_i, 0, 5, 1, 1)

        self.btnHeaterPID_graph_int_e = QPushButton(self.frame_30)
        self.btnHeaterPID_graph_int_e.setObjectName(u"btnHeaterPID_graph_int_e")
        self.btnHeaterPID_graph_int_e.setCheckable(True)
        self.btnHeaterPID_graph_int_e.setChecked(False)

        self.gridLayout_2.addWidget(self.btnHeaterPID_graph_int_e, 0, 2, 1, 1)

        self.btnHeaterPID_graph_x = QPushButton(self.frame_30)
        self.btnHeaterPID_graph_x.setObjectName(u"btnHeaterPID_graph_x")
        self.btnHeaterPID_graph_x.setCheckable(True)
        self.btnHeaterPID_graph_x.setChecked(True)

        self.gridLayout_2.addWidget(self.btnHeaterPID_graph_x, 0, 0, 1, 1)

        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_27, 0, 9, 1, 1)


        self.verticalLayout_11.addWidget(self.frame_30)

        self.stackGraphs.addWidget(self.pageHeaterPIDGraph)
        self.pageFanBBGraph = QWidget()
        self.pageFanBBGraph.setObjectName(u"pageFanBBGraph")
        self.verticalLayout_4 = QVBoxLayout(self.pageFanBBGraph)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.layFanBBGraph = QVBoxLayout()
        self.layFanBBGraph.setObjectName(u"layFanBBGraph")

        self.verticalLayout_4.addLayout(self.layFanBBGraph)

        self.frame_27 = QFrame(self.pageFanBBGraph)
        self.frame_27.setObjectName(u"frame_27")
        sizePolicy2.setHeightForWidth(self.frame_27.sizePolicy().hasHeightForWidth())
        self.frame_27.setSizePolicy(sizePolicy2)
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_27)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.btnFanBB_graph_x_max = QPushButton(self.frame_27)
        self.btnFanBB_graph_x_max.setObjectName(u"btnFanBB_graph_x_max")
        self.btnFanBB_graph_x_max.setCheckable(True)
        self.btnFanBB_graph_x_max.setChecked(False)

        self.gridLayout_3.addWidget(self.btnFanBB_graph_x_max, 0, 1, 1, 1)

        self.btnFanBB_graph_Clear = QPushButton(self.frame_27)
        self.btnFanBB_graph_Clear.setObjectName(u"btnFanBB_graph_Clear")
        self.btnFanBB_graph_Clear.setIcon(icon2)

        self.gridLayout_3.addWidget(self.btnFanBB_graph_Clear, 1, 8, 1, 1)

        self.btnFanBB_graph_u_min = QPushButton(self.frame_27)
        self.btnFanBB_graph_u_min.setObjectName(u"btnFanBB_graph_u_min")
        self.btnFanBB_graph_u_min.setCheckable(True)
        self.btnFanBB_graph_u_min.setChecked(False)

        self.gridLayout_3.addWidget(self.btnFanBB_graph_u_min, 0, 4, 1, 1)

        self.btnFanBB_graph_Stop = QPushButton(self.frame_27)
        self.btnFanBB_graph_Stop.setObjectName(u"btnFanBB_graph_Stop")
        self.btnFanBB_graph_Stop.setIcon(icon1)
        self.btnFanBB_graph_Stop.setCheckable(True)

        self.gridLayout_3.addWidget(self.btnFanBB_graph_Stop, 0, 8, 1, 1)

        self.btnFanBB_graph_u_max = QPushButton(self.frame_27)
        self.btnFanBB_graph_u_max.setObjectName(u"btnFanBB_graph_u_max")
        self.btnFanBB_graph_u_max.setCheckable(True)
        self.btnFanBB_graph_u_max.setChecked(False)

        self.gridLayout_3.addWidget(self.btnFanBB_graph_u_max, 0, 3, 1, 1)

        self.btnFanBB_graph_x_min = QPushButton(self.frame_27)
        self.btnFanBB_graph_x_min.setObjectName(u"btnFanBB_graph_x_min")
        self.btnFanBB_graph_x_min.setCheckable(True)
        self.btnFanBB_graph_x_min.setChecked(False)

        self.gridLayout_3.addWidget(self.btnFanBB_graph_x_min, 0, 2, 1, 1)

        self.btnFanBB_graph_y = QPushButton(self.frame_27)
        self.btnFanBB_graph_y.setObjectName(u"btnFanBB_graph_y")
        self.btnFanBB_graph_y.setCheckable(True)
        self.btnFanBB_graph_y.setChecked(True)

        self.gridLayout_3.addWidget(self.btnFanBB_graph_y, 0, 5, 1, 1)

        self.btnFanBB_graph_x = QPushButton(self.frame_27)
        self.btnFanBB_graph_x.setObjectName(u"btnFanBB_graph_x")
        self.btnFanBB_graph_x.setCheckable(True)
        self.btnFanBB_graph_x.setChecked(True)

        self.gridLayout_3.addWidget(self.btnFanBB_graph_x, 0, 0, 1, 1)

        self.btnFanBB_graph_mode = QPushButton(self.frame_27)
        self.btnFanBB_graph_mode.setObjectName(u"btnFanBB_graph_mode")
        self.btnFanBB_graph_mode.setCheckable(True)
        self.btnFanBB_graph_mode.setChecked(False)

        self.gridLayout_3.addWidget(self.btnFanBB_graph_mode, 0, 6, 1, 1)

        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_25, 0, 7, 1, 1)


        self.verticalLayout_4.addWidget(self.frame_27)

        self.stackGraphs.addWidget(self.pageFanBBGraph)
        self.pageFanPIDGraph = QWidget()
        self.pageFanPIDGraph.setObjectName(u"pageFanPIDGraph")
        self.verticalLayout_8 = QVBoxLayout(self.pageFanPIDGraph)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.layFanPIDGraph = QVBoxLayout()
        self.layFanPIDGraph.setObjectName(u"layFanPIDGraph")

        self.verticalLayout_8.addLayout(self.layFanPIDGraph)

        self.frame_28 = QFrame(self.pageFanPIDGraph)
        self.frame_28.setObjectName(u"frame_28")
        sizePolicy2.setHeightForWidth(self.frame_28.sizePolicy().hasHeightForWidth())
        self.frame_28.setSizePolicy(sizePolicy2)
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_28)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btnFanPID_graph_mode = QPushButton(self.frame_28)
        self.btnFanPID_graph_mode.setObjectName(u"btnFanPID_graph_mode")
        self.btnFanPID_graph_mode.setCheckable(True)
        self.btnFanPID_graph_mode.setChecked(False)

        self.gridLayout.addWidget(self.btnFanPID_graph_mode, 3, 7, 1, 1)

        self.btnFanPID_graph_k_d = QPushButton(self.frame_28)
        self.btnFanPID_graph_k_d.setObjectName(u"btnFanPID_graph_k_d")
        self.btnFanPID_graph_k_d.setCheckable(True)
        self.btnFanPID_graph_k_d.setChecked(False)

        self.gridLayout.addWidget(self.btnFanPID_graph_k_d, 0, 6, 1, 1)

        self.btnFanPID_graph_int_e = QPushButton(self.frame_28)
        self.btnFanPID_graph_int_e.setObjectName(u"btnFanPID_graph_int_e")
        self.btnFanPID_graph_int_e.setCheckable(True)
        self.btnFanPID_graph_int_e.setChecked(False)

        self.gridLayout.addWidget(self.btnFanPID_graph_int_e, 0, 2, 1, 1)

        self.btnFanPID_graph_k_aw = QPushButton(self.frame_28)
        self.btnFanPID_graph_k_aw.setObjectName(u"btnFanPID_graph_k_aw")
        self.btnFanPID_graph_k_aw.setCheckable(True)
        self.btnFanPID_graph_k_aw.setChecked(False)

        self.gridLayout.addWidget(self.btnFanPID_graph_k_aw, 0, 7, 1, 1)

        self.btnFanPID_graph_k_i = QPushButton(self.frame_28)
        self.btnFanPID_graph_k_i.setObjectName(u"btnFanPID_graph_k_i")
        self.btnFanPID_graph_k_i.setCheckable(True)
        self.btnFanPID_graph_k_i.setChecked(False)

        self.gridLayout.addWidget(self.btnFanPID_graph_k_i, 0, 5, 1, 1)

        self.btnFanPID_graph_u_i = QPushButton(self.frame_28)
        self.btnFanPID_graph_u_i.setObjectName(u"btnFanPID_graph_u_i")
        self.btnFanPID_graph_u_i.setCheckable(True)
        self.btnFanPID_graph_u_i.setChecked(False)

        self.gridLayout.addWidget(self.btnFanPID_graph_u_i, 3, 2, 1, 1)

        self.btnFanPID_graph_u_min = QPushButton(self.frame_28)
        self.btnFanPID_graph_u_min.setObjectName(u"btnFanPID_graph_u_min")
        self.btnFanPID_graph_u_min.setCheckable(True)
        self.btnFanPID_graph_u_min.setChecked(False)

        self.gridLayout.addWidget(self.btnFanPID_graph_u_min, 3, 5, 1, 1)

        self.btnFanPID_graph_u = QPushButton(self.frame_28)
        self.btnFanPID_graph_u.setObjectName(u"btnFanPID_graph_u")
        self.btnFanPID_graph_u.setCheckable(True)
        self.btnFanPID_graph_u.setChecked(False)

        self.gridLayout.addWidget(self.btnFanPID_graph_u, 0, 8, 1, 1)

        self.btnFanPID_graph_u_max = QPushButton(self.frame_28)
        self.btnFanPID_graph_u_max.setObjectName(u"btnFanPID_graph_u_max")
        self.btnFanPID_graph_u_max.setCheckable(True)
        self.btnFanPID_graph_u_max.setChecked(False)

        self.gridLayout.addWidget(self.btnFanPID_graph_u_max, 3, 4, 1, 1)

        self.btnFanPID_graph_u_p = QPushButton(self.frame_28)
        self.btnFanPID_graph_u_p.setObjectName(u"btnFanPID_graph_u_p")
        self.btnFanPID_graph_u_p.setCheckable(True)
        self.btnFanPID_graph_u_p.setChecked(False)

        self.gridLayout.addWidget(self.btnFanPID_graph_u_p, 3, 1, 1, 1)

        self.btnFanPID_graph_Clear = QPushButton(self.frame_28)
        self.btnFanPID_graph_Clear.setObjectName(u"btnFanPID_graph_Clear")
        self.btnFanPID_graph_Clear.setIcon(icon2)

        self.gridLayout.addWidget(self.btnFanPID_graph_Clear, 3, 10, 1, 1)

        self.btnFanPID_graph_Stop = QPushButton(self.frame_28)
        self.btnFanPID_graph_Stop.setObjectName(u"btnFanPID_graph_Stop")
        self.btnFanPID_graph_Stop.setIcon(icon1)
        self.btnFanPID_graph_Stop.setCheckable(True)

        self.gridLayout.addWidget(self.btnFanPID_graph_Stop, 0, 10, 1, 1)

        self.btnFanPID_graph_u_sat = QPushButton(self.frame_28)
        self.btnFanPID_graph_u_sat.setObjectName(u"btnFanPID_graph_u_sat")
        self.btnFanPID_graph_u_sat.setCheckable(True)
        self.btnFanPID_graph_u_sat.setChecked(False)

        self.gridLayout.addWidget(self.btnFanPID_graph_u_sat, 3, 0, 1, 1)

        self.btnFanPID_graph_x = QPushButton(self.frame_28)
        self.btnFanPID_graph_x.setObjectName(u"btnFanPID_graph_x")
        self.btnFanPID_graph_x.setCheckable(True)
        self.btnFanPID_graph_x.setChecked(True)

        self.gridLayout.addWidget(self.btnFanPID_graph_x, 0, 0, 1, 1)

        self.btnFanPID_graph_e = QPushButton(self.frame_28)
        self.btnFanPID_graph_e.setObjectName(u"btnFanPID_graph_e")
        self.btnFanPID_graph_e.setCheckable(True)
        self.btnFanPID_graph_e.setChecked(False)

        self.gridLayout.addWidget(self.btnFanPID_graph_e, 0, 1, 1, 1)

        self.btnFanPID_graph_u_d = QPushButton(self.frame_28)
        self.btnFanPID_graph_u_d.setObjectName(u"btnFanPID_graph_u_d")
        self.btnFanPID_graph_u_d.setCheckable(True)
        self.btnFanPID_graph_u_d.setChecked(False)

        self.gridLayout.addWidget(self.btnFanPID_graph_u_d, 3, 3, 1, 1)

        self.btnFanPID_graph_y = QPushButton(self.frame_28)
        self.btnFanPID_graph_y.setObjectName(u"btnFanPID_graph_y")
        self.btnFanPID_graph_y.setCheckable(True)
        self.btnFanPID_graph_y.setChecked(True)

        self.gridLayout.addWidget(self.btnFanPID_graph_y, 3, 6, 1, 1)

        self.btnFanPID_graph_aw_int_e = QPushButton(self.frame_28)
        self.btnFanPID_graph_aw_int_e.setObjectName(u"btnFanPID_graph_aw_int_e")
        self.btnFanPID_graph_aw_int_e.setCheckable(True)
        self.btnFanPID_graph_aw_int_e.setChecked(False)

        self.gridLayout.addWidget(self.btnFanPID_graph_aw_int_e, 0, 3, 1, 1)

        self.btnFanPID_graph_k_p = QPushButton(self.frame_28)
        self.btnFanPID_graph_k_p.setObjectName(u"btnFanPID_graph_k_p")
        self.btnFanPID_graph_k_p.setCheckable(True)
        self.btnFanPID_graph_k_p.setChecked(False)

        self.gridLayout.addWidget(self.btnFanPID_graph_k_p, 0, 4, 1, 1)

        self.horizontalSpacer_28 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_28, 0, 9, 1, 1)


        self.verticalLayout_8.addWidget(self.frame_28)

        self.stackGraphs.addWidget(self.pageFanPIDGraph)

        self.verticalLayout.addWidget(self.stackGraphs)

        self.container.addWidget(self.Controls)
        self.Export = QWidget()
        self.Export.setObjectName(u"Export")
        self.verticalLayout_10 = QVBoxLayout(self.Export)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_31 = QFrame(self.Export)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.frame_33 = QFrame(self.frame_31)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_33)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_36 = QLabel(self.frame_33)
        self.label_36.setObjectName(u"label_36")
        font3 = QFont()
        font3.setPointSize(14)
        self.label_36.setFont(font3)

        self.verticalLayout_12.addWidget(self.label_36)

        self.chxExHeaterBB = QCheckBox(self.frame_33)
        self.chxExHeaterBB.setObjectName(u"chxExHeaterBB")
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(False)
        self.chxExHeaterBB.setFont(font4)

        self.verticalLayout_12.addWidget(self.chxExHeaterBB)

        self.line_2 = QFrame(self.frame_33)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_12.addWidget(self.line_2)

        self.frame_35 = QFrame(self.frame_33)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_35)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.chxExHeaterBB_u_min = QCheckBox(self.frame_35)
        self.chxExHeaterBB_u_min.setObjectName(u"chxExHeaterBB_u_min")

        self.gridLayout_6.addWidget(self.chxExHeaterBB_u_min, 1, 1, 1, 1)

        self.chxExHeaterBB_x_max = QCheckBox(self.frame_35)
        self.chxExHeaterBB_x_max.setObjectName(u"chxExHeaterBB_x_max")

        self.gridLayout_6.addWidget(self.chxExHeaterBB_x_max, 1, 0, 1, 1)

        self.chxExHeaterBB_u_max = QCheckBox(self.frame_35)
        self.chxExHeaterBB_u_max.setObjectName(u"chxExHeaterBB_u_max")

        self.gridLayout_6.addWidget(self.chxExHeaterBB_u_max, 0, 1, 1, 1)

        self.chxExHeaterBB_x_min = QCheckBox(self.frame_35)
        self.chxExHeaterBB_x_min.setObjectName(u"chxExHeaterBB_x_min")

        self.gridLayout_6.addWidget(self.chxExHeaterBB_x_min, 2, 0, 1, 1)

        self.chxExHeaterBB_y_1 = QCheckBox(self.frame_35)
        self.chxExHeaterBB_y_1.setObjectName(u"chxExHeaterBB_y_1")

        self.gridLayout_6.addWidget(self.chxExHeaterBB_y_1, 3, 0, 1, 1)

        self.chxExHeaterBB_x = QCheckBox(self.frame_35)
        self.chxExHeaterBB_x.setObjectName(u"chxExHeaterBB_x")

        self.gridLayout_6.addWidget(self.chxExHeaterBB_x, 0, 0, 1, 1)

        self.chxExHeaterBB_y_2 = QCheckBox(self.frame_35)
        self.chxExHeaterBB_y_2.setObjectName(u"chxExHeaterBB_y_2")

        self.gridLayout_6.addWidget(self.chxExHeaterBB_y_2, 4, 0, 1, 1)

        self.chxExHeaterBB_mode = QCheckBox(self.frame_35)
        self.chxExHeaterBB_mode.setObjectName(u"chxExHeaterBB_mode")

        self.gridLayout_6.addWidget(self.chxExHeaterBB_mode, 4, 1, 1, 1)


        self.verticalLayout_12.addWidget(self.frame_35)

        self.chxExHeaterPID = QCheckBox(self.frame_33)
        self.chxExHeaterPID.setObjectName(u"chxExHeaterPID")
        self.chxExHeaterPID.setFont(font4)

        self.verticalLayout_12.addWidget(self.chxExHeaterPID)

        self.line_3 = QFrame(self.frame_33)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_12.addWidget(self.line_3)

        self.frame_36 = QFrame(self.frame_33)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_36)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.chxExHeaterPID_aw_int_e = QCheckBox(self.frame_36)
        self.chxExHeaterPID_aw_int_e.setObjectName(u"chxExHeaterPID_aw_int_e")

        self.gridLayout_7.addWidget(self.chxExHeaterPID_aw_int_e, 3, 0, 1, 1)

        self.chxExHeaterPID_k_i = QCheckBox(self.frame_36)
        self.chxExHeaterPID_k_i.setObjectName(u"chxExHeaterPID_k_i")

        self.gridLayout_7.addWidget(self.chxExHeaterPID_k_i, 5, 0, 1, 1)

        self.chxExHeaterPID_x = QCheckBox(self.frame_36)
        self.chxExHeaterPID_x.setObjectName(u"chxExHeaterPID_x")

        self.gridLayout_7.addWidget(self.chxExHeaterPID_x, 0, 0, 1, 1)

        self.chxExHeaterPID_mode = QCheckBox(self.frame_36)
        self.chxExHeaterPID_mode.setObjectName(u"chxExHeaterPID_mode")

        self.gridLayout_7.addWidget(self.chxExHeaterPID_mode, 8, 0, 1, 1)

        self.chxExHeaterPID_k_d = QCheckBox(self.frame_36)
        self.chxExHeaterPID_k_d.setObjectName(u"chxExHeaterPID_k_d")

        self.gridLayout_7.addWidget(self.chxExHeaterPID_k_d, 6, 0, 1, 1)

        self.chxExHeaterPID_int_e = QCheckBox(self.frame_36)
        self.chxExHeaterPID_int_e.setObjectName(u"chxExHeaterPID_int_e")

        self.gridLayout_7.addWidget(self.chxExHeaterPID_int_e, 2, 0, 1, 1)

        self.chxExHeaterPID_e = QCheckBox(self.frame_36)
        self.chxExHeaterPID_e.setObjectName(u"chxExHeaterPID_e")

        self.gridLayout_7.addWidget(self.chxExHeaterPID_e, 1, 0, 1, 1)

        self.chxExHeaterPID_k_aw = QCheckBox(self.frame_36)
        self.chxExHeaterPID_k_aw.setObjectName(u"chxExHeaterPID_k_aw")

        self.gridLayout_7.addWidget(self.chxExHeaterPID_k_aw, 7, 0, 1, 1)

        self.chxExHeaterPID_k_p = QCheckBox(self.frame_36)
        self.chxExHeaterPID_k_p.setObjectName(u"chxExHeaterPID_k_p")

        self.gridLayout_7.addWidget(self.chxExHeaterPID_k_p, 4, 0, 1, 1)

        self.chxExHeaterPID_u_p = QCheckBox(self.frame_36)
        self.chxExHeaterPID_u_p.setObjectName(u"chxExHeaterPID_u_p")

        self.gridLayout_7.addWidget(self.chxExHeaterPID_u_p, 2, 1, 1, 1)

        self.chxExHeaterPID_u_i = QCheckBox(self.frame_36)
        self.chxExHeaterPID_u_i.setObjectName(u"chxExHeaterPID_u_i")

        self.gridLayout_7.addWidget(self.chxExHeaterPID_u_i, 3, 1, 1, 1)

        self.chxExHeaterPID_u_sat = QCheckBox(self.frame_36)
        self.chxExHeaterPID_u_sat.setObjectName(u"chxExHeaterPID_u_sat")

        self.gridLayout_7.addWidget(self.chxExHeaterPID_u_sat, 1, 1, 1, 1)

        self.chxExHeaterPID_u = QCheckBox(self.frame_36)
        self.chxExHeaterPID_u.setObjectName(u"chxExHeaterPID_u")

        self.gridLayout_7.addWidget(self.chxExHeaterPID_u, 0, 1, 1, 1)

        self.chxExHeaterPID_u_d = QCheckBox(self.frame_36)
        self.chxExHeaterPID_u_d.setObjectName(u"chxExHeaterPID_u_d")

        self.gridLayout_7.addWidget(self.chxExHeaterPID_u_d, 4, 1, 1, 1)

        self.chxExHeaterPID_u_max = QCheckBox(self.frame_36)
        self.chxExHeaterPID_u_max.setObjectName(u"chxExHeaterPID_u_max")

        self.gridLayout_7.addWidget(self.chxExHeaterPID_u_max, 5, 1, 1, 1)

        self.chxExHeaterPID_u_min = QCheckBox(self.frame_36)
        self.chxExHeaterPID_u_min.setObjectName(u"chxExHeaterPID_u_min")

        self.gridLayout_7.addWidget(self.chxExHeaterPID_u_min, 6, 1, 1, 1)

        self.chxExHeaterPID_y_1 = QCheckBox(self.frame_36)
        self.chxExHeaterPID_y_1.setObjectName(u"chxExHeaterPID_y_1")

        self.gridLayout_7.addWidget(self.chxExHeaterPID_y_1, 7, 1, 1, 1)

        self.chxExHeaterPID_y_2 = QCheckBox(self.frame_36)
        self.chxExHeaterPID_y_2.setObjectName(u"chxExHeaterPID_y_2")

        self.gridLayout_7.addWidget(self.chxExHeaterPID_y_2, 8, 1, 1, 1)


        self.verticalLayout_12.addWidget(self.frame_36)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer)


        self.horizontalLayout_32.addWidget(self.frame_33)

        self.frame_34 = QFrame(self.frame_31)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_34)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_46 = QLabel(self.frame_34)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setFont(font3)

        self.verticalLayout_13.addWidget(self.label_46)

        self.chxExFanBB = QCheckBox(self.frame_34)
        self.chxExFanBB.setObjectName(u"chxExFanBB")
        self.chxExFanBB.setFont(font4)

        self.verticalLayout_13.addWidget(self.chxExFanBB)

        self.line_4 = QFrame(self.frame_34)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_13.addWidget(self.line_4)

        self.frame_37 = QFrame(self.frame_34)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_37)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.chxExFanBB_mode = QCheckBox(self.frame_37)
        self.chxExFanBB_mode.setObjectName(u"chxExFanBB_mode")

        self.gridLayout_8.addWidget(self.chxExFanBB_mode, 3, 1, 1, 1)

        self.chxExFanBB_x_max = QCheckBox(self.frame_37)
        self.chxExFanBB_x_max.setObjectName(u"chxExFanBB_x_max")

        self.gridLayout_8.addWidget(self.chxExFanBB_x_max, 1, 0, 1, 1)

        self.chxExFanBB_u_min = QCheckBox(self.frame_37)
        self.chxExFanBB_u_min.setObjectName(u"chxExFanBB_u_min")

        self.gridLayout_8.addWidget(self.chxExFanBB_u_min, 1, 1, 1, 1)

        self.chxExFanBB_x = QCheckBox(self.frame_37)
        self.chxExFanBB_x.setObjectName(u"chxExFanBB_x")

        self.gridLayout_8.addWidget(self.chxExFanBB_x, 0, 0, 1, 1)

        self.chxExFanBB_y = QCheckBox(self.frame_37)
        self.chxExFanBB_y.setObjectName(u"chxExFanBB_y")

        self.gridLayout_8.addWidget(self.chxExFanBB_y, 3, 0, 1, 1)

        self.chxExFanBB_x_min = QCheckBox(self.frame_37)
        self.chxExFanBB_x_min.setObjectName(u"chxExFanBB_x_min")

        self.gridLayout_8.addWidget(self.chxExFanBB_x_min, 2, 0, 1, 1)

        self.chxExFanBB_u_max = QCheckBox(self.frame_37)
        self.chxExFanBB_u_max.setObjectName(u"chxExFanBB_u_max")

        self.gridLayout_8.addWidget(self.chxExFanBB_u_max, 0, 1, 1, 1)


        self.verticalLayout_13.addWidget(self.frame_37)

        self.chxExFanPID = QCheckBox(self.frame_34)
        self.chxExFanPID.setObjectName(u"chxExFanPID")
        self.chxExFanPID.setFont(font4)

        self.verticalLayout_13.addWidget(self.chxExFanPID)

        self.line_5 = QFrame(self.frame_34)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_13.addWidget(self.line_5)

        self.frame_38 = QFrame(self.frame_34)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_38)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.chxExFanPID_x = QCheckBox(self.frame_38)
        self.chxExFanPID_x.setObjectName(u"chxExFanPID_x")

        self.gridLayout_9.addWidget(self.chxExFanPID_x, 0, 0, 1, 1)

        self.chxExFanPID_u = QCheckBox(self.frame_38)
        self.chxExFanPID_u.setObjectName(u"chxExFanPID_u")

        self.gridLayout_9.addWidget(self.chxExFanPID_u, 0, 1, 1, 1)

        self.chxExFanPID_e = QCheckBox(self.frame_38)
        self.chxExFanPID_e.setObjectName(u"chxExFanPID_e")

        self.gridLayout_9.addWidget(self.chxExFanPID_e, 1, 0, 1, 1)

        self.chxExFanPID_u_sat = QCheckBox(self.frame_38)
        self.chxExFanPID_u_sat.setObjectName(u"chxExFanPID_u_sat")

        self.gridLayout_9.addWidget(self.chxExFanPID_u_sat, 1, 1, 1, 1)

        self.chxExFanPID_int_e = QCheckBox(self.frame_38)
        self.chxExFanPID_int_e.setObjectName(u"chxExFanPID_int_e")

        self.gridLayout_9.addWidget(self.chxExFanPID_int_e, 2, 0, 1, 1)

        self.chxExFanPID_u_p = QCheckBox(self.frame_38)
        self.chxExFanPID_u_p.setObjectName(u"chxExFanPID_u_p")

        self.gridLayout_9.addWidget(self.chxExFanPID_u_p, 2, 1, 1, 1)

        self.chxExFanPID_aw_int_e = QCheckBox(self.frame_38)
        self.chxExFanPID_aw_int_e.setObjectName(u"chxExFanPID_aw_int_e")

        self.gridLayout_9.addWidget(self.chxExFanPID_aw_int_e, 3, 0, 1, 1)

        self.chxExFanPID_u_i = QCheckBox(self.frame_38)
        self.chxExFanPID_u_i.setObjectName(u"chxExFanPID_u_i")

        self.gridLayout_9.addWidget(self.chxExFanPID_u_i, 3, 1, 1, 1)

        self.chxExFanPID_k_p = QCheckBox(self.frame_38)
        self.chxExFanPID_k_p.setObjectName(u"chxExFanPID_k_p")

        self.gridLayout_9.addWidget(self.chxExFanPID_k_p, 4, 0, 1, 1)

        self.chxExFanPID_u_d = QCheckBox(self.frame_38)
        self.chxExFanPID_u_d.setObjectName(u"chxExFanPID_u_d")

        self.gridLayout_9.addWidget(self.chxExFanPID_u_d, 4, 1, 1, 1)

        self.chxExFanPID_k_i = QCheckBox(self.frame_38)
        self.chxExFanPID_k_i.setObjectName(u"chxExFanPID_k_i")

        self.gridLayout_9.addWidget(self.chxExFanPID_k_i, 5, 0, 1, 1)

        self.chxExFanPID_u_max = QCheckBox(self.frame_38)
        self.chxExFanPID_u_max.setObjectName(u"chxExFanPID_u_max")

        self.gridLayout_9.addWidget(self.chxExFanPID_u_max, 5, 1, 1, 1)

        self.chxExFanPID_k_d = QCheckBox(self.frame_38)
        self.chxExFanPID_k_d.setObjectName(u"chxExFanPID_k_d")

        self.gridLayout_9.addWidget(self.chxExFanPID_k_d, 6, 0, 1, 1)

        self.chxExFanPID_u_min = QCheckBox(self.frame_38)
        self.chxExFanPID_u_min.setObjectName(u"chxExFanPID_u_min")

        self.gridLayout_9.addWidget(self.chxExFanPID_u_min, 6, 1, 1, 1)

        self.chxExFanPID_k_aw = QCheckBox(self.frame_38)
        self.chxExFanPID_k_aw.setObjectName(u"chxExFanPID_k_aw")

        self.gridLayout_9.addWidget(self.chxExFanPID_k_aw, 7, 0, 1, 1)

        self.chxExFanPID_y = QCheckBox(self.frame_38)
        self.chxExFanPID_y.setObjectName(u"chxExFanPID_y")

        self.gridLayout_9.addWidget(self.chxExFanPID_y, 7, 1, 1, 1)

        self.chxExFanPID_mode = QCheckBox(self.frame_38)
        self.chxExFanPID_mode.setObjectName(u"chxExFanPID_mode")

        self.gridLayout_9.addWidget(self.chxExFanPID_mode, 8, 0, 1, 1)


        self.verticalLayout_13.addWidget(self.frame_38)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_2)


        self.horizontalLayout_32.addWidget(self.frame_34)


        self.verticalLayout_10.addWidget(self.frame_31)

        self.frame_32 = QFrame(self.Export)
        self.frame_32.setObjectName(u"frame_32")
        sizePolicy1.setHeightForWidth(self.frame_32.sizePolicy().hasHeightForWidth())
        self.frame_32.setSizePolicy(sizePolicy1)
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_32)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.horizontalSpacer_29 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_29, 0, 1, 1, 1)

        self.btnExportAction = QPushButton(self.frame_32)
        self.btnExportAction.setObjectName(u"btnExportAction")

        self.gridLayout_5.addWidget(self.btnExportAction, 0, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_3, 1, 0, 1, 1)


        self.verticalLayout_10.addWidget(self.frame_32)

        self.container.addWidget(self.Export)
        self.Help = QWidget()
        self.Help.setObjectName(u"Help")
        self.label_37 = QLabel(self.Help)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(330, 400, 49, 16))
        self.label_8 = QLabel(self.Help)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(490, 450, 261, 31))
        self.container.addWidget(self.Help)

        self.verticalLayout_2.addWidget(self.container)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.container.setCurrentIndex(1)
        self.stackControllerDesc.setCurrentIndex(1)
        self.stackControllerSelect.setCurrentIndex(0)
        self.stackController.setCurrentIndex(1)
        self.stackGraphs.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sterowanie Procesami Ci\u0105g\u0142ymi", None))
#if QT_CONFIG(tooltip)
        self.btnConnect.setToolTip(QCoreApplication.translate("MainWindow", u"Po\u0142\u0105cz lub Roz\u0142\u0105cz si\u0119 z urz\u0105dzeniem", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btnConnect.setStatusTip(QCoreApplication.translate("MainWindow", u"Po\u0142\u0105cz lub Roz\u0142\u0105cz si\u0119 z urz\u0105dzeniem", None))
#endif // QT_CONFIG(statustip)
        self.btnConnect.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
#if QT_CONFIG(tooltip)
        self.btnHeaterControls.setToolTip(QCoreApplication.translate("MainWindow", u"Wybierz regulator grza\u0142ki i zmie\u0144 jego parametry", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btnHeaterControls.setStatusTip(QCoreApplication.translate("MainWindow", u"Wybierz regulator grza\u0142ki i zmie\u0144 jego parametry", None))
#endif // QT_CONFIG(statustip)
        self.btnHeaterControls.setText(QCoreApplication.translate("MainWindow", u"Grza\u0142ka", None))
#if QT_CONFIG(tooltip)
        self.btnFanControls.setToolTip(QCoreApplication.translate("MainWindow", u"Wybierz regulator wentylatora i zmie\u0144 jego parametry", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btnFanControls.setStatusTip(QCoreApplication.translate("MainWindow", u"Wybierz regulator wentylatora i zmie\u0144 jego parametry", None))
#endif // QT_CONFIG(statustip)
        self.btnFanControls.setText(QCoreApplication.translate("MainWindow", u"Wentylator", None))
#if QT_CONFIG(tooltip)
        self.btnDataExport.setToolTip(QCoreApplication.translate("MainWindow", u"Eksportuj dane do pliku .xlsx", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btnDataExport.setStatusTip(QCoreApplication.translate("MainWindow", u"Eksportuj dane do pliku .xlsx", None))
#endif // QT_CONFIG(statustip)
        self.btnDataExport.setText(QCoreApplication.translate("MainWindow", u"Eksport danych", None))
#if QT_CONFIG(tooltip)
        self.btnHelp.setToolTip(QCoreApplication.translate("MainWindow", u"Dowiedz si\u0119 jak korzysta\u0107 z programu", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btnHelp.setStatusTip(QCoreApplication.translate("MainWindow", u"Dowiedz si\u0119 jak korzysta\u0107 z programu", None))
#endif // QT_CONFIG(statustip)
        self.btnHelp.setText(QCoreApplication.translate("MainWindow", u"Pomoc", None))
#if QT_CONFIG(tooltip)
        self.controllerDescHeater.setToolTip(QCoreApplication.translate("MainWindow", u"Uruchom lub zatrzymaj prac\u0119 grza\u0142ki", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.controllerDescHeater.setStatusTip(QCoreApplication.translate("MainWindow", u"Uruchom lub zatrzymaj prac\u0119 grza\u0142ki", None))
#endif // QT_CONFIG(statustip)
        self.lblControls.setText(QCoreApplication.translate("MainWindow", u"Ustawienia grza\u0142ki", None))
        self.btnHeaterStart.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Ustawienia wentylatora", None))
#if QT_CONFIG(tooltip)
        self.btnFanStart.setToolTip(QCoreApplication.translate("MainWindow", u"Uruchom lub zatrzymaj prac\u0119 wentylatora", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btnFanStart.setStatusTip(QCoreApplication.translate("MainWindow", u"Uruchom lub zatrzymaj prac\u0119 wentylatora", None))
#endif // QT_CONFIG(statustip)
        self.btnFanStart.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.lblHeaterController.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Wyb\u00f3r regulatora	</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.btnHeaterControllerSetBB.setToolTip(QCoreApplication.translate("MainWindow", u"Wybierz dwupo\u0142o\u017ceniowy regulator do sterowania grza\u0142k\u0105", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btnHeaterControllerSetBB.setStatusTip(QCoreApplication.translate("MainWindow", u"Wybierz dwupo\u0142o\u017ceniowy regulator do sterowania grza\u0142k\u0105", None))
#endif // QT_CONFIG(statustip)
        self.btnHeaterControllerSetBB.setText(QCoreApplication.translate("MainWindow", u"Dwupo\u0142o\u017ceniowy", None))
#if QT_CONFIG(tooltip)
        self.btnHeaterControllerSetPID.setToolTip(QCoreApplication.translate("MainWindow", u"Wybierz regulator PID do sterowania grza\u0142k\u0105", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btnHeaterControllerSetPID.setStatusTip(QCoreApplication.translate("MainWindow", u"Wybierz regulator PID do sterowania grza\u0142k\u0105", None))
#endif // QT_CONFIG(statustip)
        self.btnHeaterControllerSetPID.setText(QCoreApplication.translate("MainWindow", u"PID", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Wyb\u00f3r grza\u0142ki	</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.btnHeaterControllerSetHighPower.setToolTip(QCoreApplication.translate("MainWindow", u"Wybierz grza\u0142k\u0119 o rezystancji 17\u03a9", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btnHeaterControllerSetHighPower.setStatusTip(QCoreApplication.translate("MainWindow", u"Wybierz grza\u0142k\u0119 o rezystancji 17\u03a9", None))
#endif // QT_CONFIG(statustip)
        self.btnHeaterControllerSetHighPower.setText(QCoreApplication.translate("MainWindow", u"17 \u03a9", None))
#if QT_CONFIG(tooltip)
        self.btnHeaterControllerSetLowPower.setToolTip(QCoreApplication.translate("MainWindow", u"Wybierz grza\u0142k\u0119 o rezystancji 33\u03a9", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btnHeaterControllerSetLowPower.setStatusTip(QCoreApplication.translate("MainWindow", u"Wybierz grza\u0142k\u0119 o rezystancji 33\u03a9", None))
#endif // QT_CONFIG(statustip)
        self.btnHeaterControllerSetLowPower.setText(QCoreApplication.translate("MainWindow", u"33 \u03a9", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Wyb\u00f3r temperatury odniesienia	</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.btnHeaterControllerSetLeftCoil.setToolTip(QCoreApplication.translate("MainWindow", u"Wybierz lewy czujnik temperatury", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btnHeaterControllerSetLeftCoil.setStatusTip(QCoreApplication.translate("MainWindow", u"Wybierz lewy czujnik temperatury", None))
#endif // QT_CONFIG(statustip)
        self.btnHeaterControllerSetLeftCoil.setText(QCoreApplication.translate("MainWindow", u"Lewa", None))
#if QT_CONFIG(tooltip)
        self.btnHeaterControllerSetRightCoil.setToolTip(QCoreApplication.translate("MainWindow", u"Wybierz prawy czujnik temperatury", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btnHeaterControllerSetRightCoil.setStatusTip(QCoreApplication.translate("MainWindow", u"Wybierz prawy czujnik temperatury", None))
#endif // QT_CONFIG(statustip)
        self.btnHeaterControllerSetRightCoil.setText(QCoreApplication.translate("MainWindow", u"Prawa", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Wyb\u00f3r regulatora	</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.btnFanControllerSetBB.setToolTip(QCoreApplication.translate("MainWindow", u"Wybierz dwupo\u0142o\u017ceniowy regulator do sterowania wentylatorem", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btnFanControllerSetBB.setStatusTip(QCoreApplication.translate("MainWindow", u"Wybierz dwupo\u0142o\u017ceniowy regulator do sterowania wentylatorem", None))
#endif // QT_CONFIG(statustip)
        self.btnFanControllerSetBB.setText(QCoreApplication.translate("MainWindow", u"Dwupo\u0142o\u017ceniowy", None))
#if QT_CONFIG(tooltip)
        self.btnFanControllerSetPID.setToolTip(QCoreApplication.translate("MainWindow", u"Wybierz regulator PID do sterowania wentylatorem", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btnFanControllerSetPID.setStatusTip(QCoreApplication.translate("MainWindow", u"Wybierz regulator PID do sterowania wentylatorem", None))
#endif // QT_CONFIG(statustip)
        self.btnFanControllerSetPID.setText(QCoreApplication.translate("MainWindow", u"PID", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Warto\u015b\u0107 zadana	</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.inHeaterBBSetValue.setToolTip(QCoreApplication.translate("MainWindow", u"Min: 0 | Max: 100", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.inHeaterBBSetValue.setStatusTip(QCoreApplication.translate("MainWindow", u"Min: 0 | Max: 100", None))
#endif // QT_CONFIG(statustip)
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u00b0C</p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Histereza	</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.inHeaterBBHysteresis.setToolTip(QCoreApplication.translate("MainWindow", u"Min: 0 | Max: 100", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.inHeaterBBHysteresis.setStatusTip(QCoreApplication.translate("MainWindow", u"Min: 0 | Max: 100", None))
#endif // QT_CONFIG(statustip)
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u00b0C</p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Moc	</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.inHeaterBBPower.setToolTip(QCoreApplication.translate("MainWindow", u"Min: 0 | Max: 100", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.inHeaterBBPower.setStatusTip(QCoreApplication.translate("MainWindow", u"Min: 0 | Max: 100", None))
#endif // QT_CONFIG(statustip)
        self.lblPower.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"W", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Warto\u015b\u0107 zadana	</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.inHeaterPIDSetValue.setToolTip(QCoreApplication.translate("MainWindow", u"Min: 0 | Max: 100", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.inHeaterPIDSetValue.setStatusTip(QCoreApplication.translate("MainWindow", u"Min: 0 | Max: 100", None))
#endif // QT_CONFIG(statustip)
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u00b0C</p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>K<span style=\" vertical-align:sub;\">p</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.inHeaterPID_Kp.setToolTip(QCoreApplication.translate("MainWindow", u"Min: 0.00 | Max: 99.99", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.inHeaterPID_Kp.setStatusTip(QCoreApplication.translate("MainWindow", u"Min: 0.00 | Max: 99.99", None))
#endif // QT_CONFIG(statustip)
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"jed", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>K<span style=\" vertical-align:sub;\">i</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.inHeaterPID_Ki.setToolTip(QCoreApplication.translate("MainWindow", u"Min: 0.00 | Max: 99.99", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.inHeaterPID_Ki.setStatusTip(QCoreApplication.translate("MainWindow", u"Min: 0.00 | Max: 99.99", None))
#endif // QT_CONFIG(statustip)
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"jed", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>T<span style=\" vertical-align:sub;\">i</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.inHeaterPID_Ti.setToolTip(QCoreApplication.translate("MainWindow", u"Min: 0.00 | Max: 99.99", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.inHeaterPID_Ti.setStatusTip(QCoreApplication.translate("MainWindow", u"Min: 0.00 | Max: 99.99", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.inHeaterPID_Ti.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"jed", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>K<span style=\" vertical-align:sub;\">d</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.inHeaterPID_Kd.setToolTip(QCoreApplication.translate("MainWindow", u"Min: 0.00 | Max: 99.99", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.inHeaterPID_Kd.setStatusTip(QCoreApplication.translate("MainWindow", u"Min: 0.00 | Max: 99.99", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.inHeaterPID_Kd.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"jed", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>T<span style=\" vertical-align:sub;\">d</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.inHeaterPID_Td.setToolTip(QCoreApplication.translate("MainWindow", u"Min: 0.00 | Max: 99.99", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.inHeaterPID_Td.setStatusTip(QCoreApplication.translate("MainWindow", u"Min: 0.00 | Max: 99.99", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.inHeaterPID_Td.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"jed", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>K<span style=\" vertical-align:sub;\">aw</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.inHeaterPID_Kaw.setToolTip(QCoreApplication.translate("MainWindow", u"Min: 0.00 | Max: 1.00", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.inHeaterPID_Kaw.setStatusTip(QCoreApplication.translate("MainWindow", u"Min: 0.00 | Max: 1.00", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.inHeaterPID_Kaw.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"jed", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Warto\u015b\u0107 zadana	</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.inFanBBSetValue.setToolTip(QCoreApplication.translate("MainWindow", u"Min: 0 | Max: 6000", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.inFanBBSetValue.setStatusTip(QCoreApplication.translate("MainWindow", u"Min: 0 | Max: 6000", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.inFanBBSetValue.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"RPM", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Histereza	</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.inFanBBHysteresis.setToolTip(QCoreApplication.translate("MainWindow", u"Min: 0 | Max: 100", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.inFanBBHysteresis.setStatusTip(QCoreApplication.translate("MainWindow", u"Min: 0 | Max: 100", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.inFanBBHysteresis.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"RPM", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Warto\u015b\u0107 zadana	</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.inFanPIDSetValue.setToolTip(QCoreApplication.translate("MainWindow", u"Min: 0 | Max: 6000", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.inFanPIDSetValue.setStatusTip(QCoreApplication.translate("MainWindow", u"Min: 0 | Max: 6000", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.inFanPIDSetValue.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"RPM", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>K<span style=\" vertical-align:sub;\">p</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.inFanPID_Kp.setToolTip(QCoreApplication.translate("MainWindow", u"Min: 0.0 | Max: 999.99", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.inFanPID_Kp.setStatusTip(QCoreApplication.translate("MainWindow", u"Min: 0.0 | Max: 999.99", None))
#endif // QT_CONFIG(statustip)
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"jed", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>K<span style=\" vertical-align:sub;\">i</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.inFanPID_Ki.setToolTip(QCoreApplication.translate("MainWindow", u"Min: 0.0 | Max: 999.99", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.inFanPID_Ki.setStatusTip(QCoreApplication.translate("MainWindow", u"Min: 0.0 | Max: 999.99", None))
#endif // QT_CONFIG(statustip)
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"jed", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>T<span style=\" vertical-align:sub;\">i</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.inFanPID_Ti.setToolTip(QCoreApplication.translate("MainWindow", u"Min: 0.0 | Max: 999.99", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.inFanPID_Ti.setStatusTip(QCoreApplication.translate("MainWindow", u"Min: 0.0 | Max: 999.99", None))
#endif // QT_CONFIG(statustip)
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"jed", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>K<span style=\" vertical-align:sub;\">d</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.inFanPID_Kd.setToolTip(QCoreApplication.translate("MainWindow", u"Min: 0.0 | Max: 999.99", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.inFanPID_Kd.setStatusTip(QCoreApplication.translate("MainWindow", u"Min: 0.0 | Max: 999.99", None))
#endif // QT_CONFIG(statustip)
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"jed", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>T<span style=\" vertical-align:sub;\">d</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.inFanPID_Td.setToolTip(QCoreApplication.translate("MainWindow", u"Min: 0.0 | Max: 999.99", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.inFanPID_Td.setStatusTip(QCoreApplication.translate("MainWindow", u"Min: 0.0 | Max: 999.99", None))
#endif // QT_CONFIG(statustip)
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"jed", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>K<span style=\" vertical-align:sub;\">aw</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.inFanPID_Kaw.setToolTip(QCoreApplication.translate("MainWindow", u"Min: 0.0 | Max: 1.0", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.inFanPID_Kaw.setStatusTip(QCoreApplication.translate("MainWindow", u"Min: 0.0 | Max: 1.0", None))
#endif // QT_CONFIG(statustip)
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"jed", None))
        self.btnHeaterBB_graph_mode.setText(QCoreApplication.translate("MainWindow", u"stan", None))
        self.btnHeaterBB_graph_u_max.setText(QCoreApplication.translate("MainWindow", u"u_max(t)", None))
#if QT_CONFIG(tooltip)
        self.btnHeaterBB_graph_Stop.setToolTip(QCoreApplication.translate("MainWindow", u"Zatrzymaj wykres", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btnHeaterBB_graph_Stop.setStatusTip(QCoreApplication.translate("MainWindow", u"Zatrzymaj wykres", None))
#endif // QT_CONFIG(statustip)
        self.btnHeaterBB_graph_Stop.setText("")
        self.btnHeaterBB_graph_y_1.setText(QCoreApplication.translate("MainWindow", u"y_1(t)", None))
        self.btnHeaterBB_graph_u_min.setText(QCoreApplication.translate("MainWindow", u"u_min(t)", None))
        self.btnHeaterBB_graph_y_2.setText(QCoreApplication.translate("MainWindow", u"y_2(t)", None))
#if QT_CONFIG(tooltip)
        self.btnHeaterBB_graph_Clear.setToolTip(QCoreApplication.translate("MainWindow", u"Wyczy\u015b\u0107 wykres", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btnHeaterBB_graph_Clear.setStatusTip(QCoreApplication.translate("MainWindow", u"Wyczy\u015b\u0107 wykres", None))
#endif // QT_CONFIG(statustip)
        self.btnHeaterBB_graph_Clear.setText("")
        self.btnHeaterBB_graph_x.setText(QCoreApplication.translate("MainWindow", u"x(t)", None))
        self.btnHeaterBB_graph_x_min.setText(QCoreApplication.translate("MainWindow", u"x_min(t)", None))
        self.btnHeaterBB_graph_x_max.setText(QCoreApplication.translate("MainWindow", u"x_max(t)", None))
        self.btnHeaterPID_graph_u_p.setText(QCoreApplication.translate("MainWindow", u"u_p(t)", None))
        self.btnHeaterPID_graph_k_p.setText(QCoreApplication.translate("MainWindow", u"k_p(t)", None))
        self.btnHeaterPID_graph_y_2.setText(QCoreApplication.translate("MainWindow", u"y_2(t)", None))
        self.btnHeaterPID_graph_mode.setText(QCoreApplication.translate("MainWindow", u"stan", None))
#if QT_CONFIG(tooltip)
        self.btnHeaterPID_graph_Stop.setToolTip(QCoreApplication.translate("MainWindow", u"Zatrzymaj wykres", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btnHeaterPID_graph_Stop.setStatusTip(QCoreApplication.translate("MainWindow", u"Zatrzymaj wykres", None))
#endif // QT_CONFIG(statustip)
        self.btnHeaterPID_graph_Stop.setText("")
        self.btnHeaterPID_graph_u_sat.setText(QCoreApplication.translate("MainWindow", u"u_sat(t)", None))
        self.btnHeaterPID_graph_u_i.setText(QCoreApplication.translate("MainWindow", u"u_i(t)", None))
        self.btnHeaterPID_graph_y_1.setText(QCoreApplication.translate("MainWindow", u"y_1(t)", None))
        self.btnHeaterPID_graph_aw_int_e.setText(QCoreApplication.translate("MainWindow", u"aw_int_e(t)", None))
        self.btnHeaterPID_graph_u_d.setText(QCoreApplication.translate("MainWindow", u"u_d(t)", None))
        self.btnHeaterPID_graph_e.setText(QCoreApplication.translate("MainWindow", u"e(t)", None))
        self.btnHeaterPID_graph_u_max.setText(QCoreApplication.translate("MainWindow", u"u_max(t)", None))
        self.btnHeaterPID_graph_u.setText(QCoreApplication.translate("MainWindow", u"u(t)", None))
        self.btnHeaterPID_graph_k_aw.setText(QCoreApplication.translate("MainWindow", u"k_aw(t)", None))
#if QT_CONFIG(tooltip)
        self.btnHeaterPID_graph_Clear.setToolTip(QCoreApplication.translate("MainWindow", u"Wyczy\u015b\u0107 wykres", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btnHeaterPID_graph_Clear.setStatusTip(QCoreApplication.translate("MainWindow", u"Wyczy\u015b\u0107 wykres", None))
#endif // QT_CONFIG(statustip)
        self.btnHeaterPID_graph_Clear.setText("")
        self.btnHeaterPID_graph_k_d.setText(QCoreApplication.translate("MainWindow", u"k_d(t)", None))
        self.btnHeaterPID_graph_u_min.setText(QCoreApplication.translate("MainWindow", u"u_min(t)", None))
        self.btnHeaterPID_graph_k_i.setText(QCoreApplication.translate("MainWindow", u"k_i(t)", None))
        self.btnHeaterPID_graph_int_e.setText(QCoreApplication.translate("MainWindow", u"int_e(t)", None))
        self.btnHeaterPID_graph_x.setText(QCoreApplication.translate("MainWindow", u"x(t)", None))
        self.btnFanBB_graph_x_max.setText(QCoreApplication.translate("MainWindow", u"x_max(t)", None))
#if QT_CONFIG(tooltip)
        self.btnFanBB_graph_Clear.setToolTip(QCoreApplication.translate("MainWindow", u"Wyczy\u015b\u0107 wykres", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btnFanBB_graph_Clear.setStatusTip(QCoreApplication.translate("MainWindow", u"Wyczy\u015b\u0107 wykres", None))
#endif // QT_CONFIG(statustip)
        self.btnFanBB_graph_Clear.setText("")
        self.btnFanBB_graph_u_min.setText(QCoreApplication.translate("MainWindow", u"u_min(t)", None))
#if QT_CONFIG(tooltip)
        self.btnFanBB_graph_Stop.setToolTip(QCoreApplication.translate("MainWindow", u"Zatrzymaj wykres", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btnFanBB_graph_Stop.setStatusTip(QCoreApplication.translate("MainWindow", u"Zatrzymaj wykres", None))
#endif // QT_CONFIG(statustip)
        self.btnFanBB_graph_Stop.setText("")
        self.btnFanBB_graph_u_max.setText(QCoreApplication.translate("MainWindow", u"u_max(t)", None))
        self.btnFanBB_graph_x_min.setText(QCoreApplication.translate("MainWindow", u"x_min(t)", None))
        self.btnFanBB_graph_y.setText(QCoreApplication.translate("MainWindow", u"y(t)", None))
        self.btnFanBB_graph_x.setText(QCoreApplication.translate("MainWindow", u"x(t)", None))
        self.btnFanBB_graph_mode.setText(QCoreApplication.translate("MainWindow", u"stan", None))
        self.btnFanPID_graph_mode.setText(QCoreApplication.translate("MainWindow", u"stan", None))
        self.btnFanPID_graph_k_d.setText(QCoreApplication.translate("MainWindow", u"k_d(t)", None))
        self.btnFanPID_graph_int_e.setText(QCoreApplication.translate("MainWindow", u"int_e(t)", None))
        self.btnFanPID_graph_k_aw.setText(QCoreApplication.translate("MainWindow", u"k_aw(t)", None))
        self.btnFanPID_graph_k_i.setText(QCoreApplication.translate("MainWindow", u"k_i(t)", None))
        self.btnFanPID_graph_u_i.setText(QCoreApplication.translate("MainWindow", u"u_i(t)", None))
        self.btnFanPID_graph_u_min.setText(QCoreApplication.translate("MainWindow", u"u_min(t)", None))
        self.btnFanPID_graph_u.setText(QCoreApplication.translate("MainWindow", u"u(t)", None))
        self.btnFanPID_graph_u_max.setText(QCoreApplication.translate("MainWindow", u"u_max(t)", None))
        self.btnFanPID_graph_u_p.setText(QCoreApplication.translate("MainWindow", u"u_p(t)", None))
#if QT_CONFIG(tooltip)
        self.btnFanPID_graph_Clear.setToolTip(QCoreApplication.translate("MainWindow", u"Wyczy\u015b\u0107 wykres", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btnFanPID_graph_Clear.setStatusTip(QCoreApplication.translate("MainWindow", u"Wyczy\u015b\u0107 wykres", None))
#endif // QT_CONFIG(statustip)
        self.btnFanPID_graph_Clear.setText("")
#if QT_CONFIG(tooltip)
        self.btnFanPID_graph_Stop.setToolTip(QCoreApplication.translate("MainWindow", u"Zatrzymaj wykres", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btnFanPID_graph_Stop.setStatusTip(QCoreApplication.translate("MainWindow", u"Zatrzymaj wykres", None))
#endif // QT_CONFIG(statustip)
        self.btnFanPID_graph_Stop.setText("")
        self.btnFanPID_graph_u_sat.setText(QCoreApplication.translate("MainWindow", u"u_sat(t)", None))
        self.btnFanPID_graph_x.setText(QCoreApplication.translate("MainWindow", u"x(t)", None))
        self.btnFanPID_graph_e.setText(QCoreApplication.translate("MainWindow", u"e(t)", None))
        self.btnFanPID_graph_u_d.setText(QCoreApplication.translate("MainWindow", u"u_d(t)", None))
        self.btnFanPID_graph_y.setText(QCoreApplication.translate("MainWindow", u"y(t)", None))
        self.btnFanPID_graph_aw_int_e.setText(QCoreApplication.translate("MainWindow", u"aw_int_e(t)", None))
        self.btnFanPID_graph_k_p.setText(QCoreApplication.translate("MainWindow", u"k_p(t)", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Grza\u0142ka", None))
        self.chxExHeaterBB.setText(QCoreApplication.translate("MainWindow", u"Regulator dwupo\u0142o\u017ceniowy", None))
        self.chxExHeaterBB_u_min.setText(QCoreApplication.translate("MainWindow", u"u_min(t)", None))
        self.chxExHeaterBB_x_max.setText(QCoreApplication.translate("MainWindow", u"x_max(t)", None))
        self.chxExHeaterBB_u_max.setText(QCoreApplication.translate("MainWindow", u"u_max(t)", None))
        self.chxExHeaterBB_x_min.setText(QCoreApplication.translate("MainWindow", u"x_min(t)", None))
        self.chxExHeaterBB_y_1.setText(QCoreApplication.translate("MainWindow", u"y_1(t)", None))
        self.chxExHeaterBB_x.setText(QCoreApplication.translate("MainWindow", u"x(t)", None))
        self.chxExHeaterBB_y_2.setText(QCoreApplication.translate("MainWindow", u"y_2(t)", None))
        self.chxExHeaterBB_mode.setText(QCoreApplication.translate("MainWindow", u"stan", None))
        self.chxExHeaterPID.setText(QCoreApplication.translate("MainWindow", u"Regulator PID", None))
        self.chxExHeaterPID_aw_int_e.setText(QCoreApplication.translate("MainWindow", u"aw_int_e(t)", None))
        self.chxExHeaterPID_k_i.setText(QCoreApplication.translate("MainWindow", u"k_i(t)", None))
        self.chxExHeaterPID_x.setText(QCoreApplication.translate("MainWindow", u"x(t)", None))
        self.chxExHeaterPID_mode.setText(QCoreApplication.translate("MainWindow", u"stan", None))
        self.chxExHeaterPID_k_d.setText(QCoreApplication.translate("MainWindow", u"k_d(t)", None))
        self.chxExHeaterPID_int_e.setText(QCoreApplication.translate("MainWindow", u"int_e(t)", None))
        self.chxExHeaterPID_e.setText(QCoreApplication.translate("MainWindow", u"e(t)", None))
        self.chxExHeaterPID_k_aw.setText(QCoreApplication.translate("MainWindow", u"k_aw(t)", None))
        self.chxExHeaterPID_k_p.setText(QCoreApplication.translate("MainWindow", u"k_p(t)", None))
        self.chxExHeaterPID_u_p.setText(QCoreApplication.translate("MainWindow", u"u_p(t)", None))
        self.chxExHeaterPID_u_i.setText(QCoreApplication.translate("MainWindow", u"u_i(t)", None))
        self.chxExHeaterPID_u_sat.setText(QCoreApplication.translate("MainWindow", u"u_sat(t)", None))
        self.chxExHeaterPID_u.setText(QCoreApplication.translate("MainWindow", u"u(t)", None))
        self.chxExHeaterPID_u_d.setText(QCoreApplication.translate("MainWindow", u"u_d(t)", None))
        self.chxExHeaterPID_u_max.setText(QCoreApplication.translate("MainWindow", u"u_max(t)", None))
        self.chxExHeaterPID_u_min.setText(QCoreApplication.translate("MainWindow", u"u_min(t)", None))
        self.chxExHeaterPID_y_1.setText(QCoreApplication.translate("MainWindow", u"y_1(t)", None))
        self.chxExHeaterPID_y_2.setText(QCoreApplication.translate("MainWindow", u"y_2(t)", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Wentylator", None))
        self.chxExFanBB.setText(QCoreApplication.translate("MainWindow", u"Regulator dwupo\u0142o\u017ceniowy", None))
        self.chxExFanBB_mode.setText(QCoreApplication.translate("MainWindow", u"stan", None))
        self.chxExFanBB_x_max.setText(QCoreApplication.translate("MainWindow", u"x_max(t)", None))
        self.chxExFanBB_u_min.setText(QCoreApplication.translate("MainWindow", u"u_min(t)", None))
        self.chxExFanBB_x.setText(QCoreApplication.translate("MainWindow", u"x(t)", None))
        self.chxExFanBB_y.setText(QCoreApplication.translate("MainWindow", u"y(t)", None))
        self.chxExFanBB_x_min.setText(QCoreApplication.translate("MainWindow", u"x_min(t)", None))
        self.chxExFanBB_u_max.setText(QCoreApplication.translate("MainWindow", u"u_max(t)", None))
        self.chxExFanPID.setText(QCoreApplication.translate("MainWindow", u"Regulator PID", None))
        self.chxExFanPID_x.setText(QCoreApplication.translate("MainWindow", u"x(t)", None))
        self.chxExFanPID_u.setText(QCoreApplication.translate("MainWindow", u"u(t)", None))
        self.chxExFanPID_e.setText(QCoreApplication.translate("MainWindow", u"e(t)", None))
        self.chxExFanPID_u_sat.setText(QCoreApplication.translate("MainWindow", u"u_sat(t)", None))
        self.chxExFanPID_int_e.setText(QCoreApplication.translate("MainWindow", u"int_e(t)", None))
        self.chxExFanPID_u_p.setText(QCoreApplication.translate("MainWindow", u"u_p(t)", None))
        self.chxExFanPID_aw_int_e.setText(QCoreApplication.translate("MainWindow", u"aw_int_e(t)", None))
        self.chxExFanPID_u_i.setText(QCoreApplication.translate("MainWindow", u"u_i(t)", None))
        self.chxExFanPID_k_p.setText(QCoreApplication.translate("MainWindow", u"k_p(t)", None))
        self.chxExFanPID_u_d.setText(QCoreApplication.translate("MainWindow", u"u_d(t)", None))
        self.chxExFanPID_k_i.setText(QCoreApplication.translate("MainWindow", u"k_i(t)", None))
        self.chxExFanPID_u_max.setText(QCoreApplication.translate("MainWindow", u"u_max(t)", None))
        self.chxExFanPID_k_d.setText(QCoreApplication.translate("MainWindow", u"k_d(t)", None))
        self.chxExFanPID_u_min.setText(QCoreApplication.translate("MainWindow", u"u_min(t)", None))
        self.chxExFanPID_k_aw.setText(QCoreApplication.translate("MainWindow", u"k_aw(t)", None))
        self.chxExFanPID_y.setText(QCoreApplication.translate("MainWindow", u"y(t)", None))
        self.chxExFanPID_mode.setText(QCoreApplication.translate("MainWindow", u"stan", None))
        self.btnExportAction.setText(QCoreApplication.translate("MainWindow", u"Eksportuj", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0179r\u00f3d\u0142o wszystkich ikon w aplikacji: Flaticon.com</p></body></html>", None))
    # retranslateUi


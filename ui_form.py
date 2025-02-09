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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QFrame, QGridLayout, QHBoxLayout, QLCDNumber,
    QLabel, QLayout, QMainWindow, QPushButton,
    QSizePolicy, QSlider, QSpacerItem, QSpinBox,
    QStackedWidget, QStatusBar, QVBoxLayout, QWidget)

from StackedWidget import StackedWidget
import rc_resources

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(1688, 939)
        icon = QIcon()
        icon.addFile(u":/assets/assets/oscilloscope.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"")
        MainWindow.setLocale(QLocale(QLocale.Polish, QLocale.Poland))
        MainWindow.setIconSize(QSize(40, 40))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.menubar = QFrame(self.centralwidget)
        self.menubar.setObjectName(u"menubar")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menubar.sizePolicy().hasHeightForWidth())
        self.menubar.setSizePolicy(sizePolicy)
        self.menubar.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout = QHBoxLayout(self.menubar)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnConnect = QPushButton(self.menubar)
        self.btnConnect.setObjectName(u"btnConnect")
        self.btnConnect.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnConnect.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/assets/assets/uC.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnConnect.setIcon(icon1)
        self.btnConnect.setCheckable(True)

        self.horizontalLayout.addWidget(self.btnConnect)

        self.line = QFrame(self.menubar)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.btnHeaterControls = QPushButton(self.menubar)
        self.btnHeaterControls.setObjectName(u"btnHeaterControls")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btnHeaterControls.sizePolicy().hasHeightForWidth())
        self.btnHeaterControls.setSizePolicy(sizePolicy1)
        self.btnHeaterControls.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/assets/assets/heater.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnHeaterControls.setIcon(icon2)
        self.btnHeaterControls.setCheckable(True)

        self.horizontalLayout.addWidget(self.btnHeaterControls)

        self.btnFanControls = QPushButton(self.menubar)
        self.btnFanControls.setObjectName(u"btnFanControls")
        self.btnFanControls.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/assets/assets/fan.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnFanControls.setIcon(icon3)
        self.btnFanControls.setCheckable(True)

        self.horizontalLayout.addWidget(self.btnFanControls)

        self.line_8 = QFrame(self.menubar)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.Shape.VLine)
        self.line_8.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line_8)

        self.btnGraphs = QPushButton(self.menubar)
        self.btnGraphs.setObjectName(u"btnGraphs")
        icon4 = QIcon()
        icon4.addFile(u":/assets/assets/graph.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnGraphs.setIcon(icon4)
        self.btnGraphs.setCheckable(True)

        self.horizontalLayout.addWidget(self.btnGraphs)

        self.btn_graph_Stop = QPushButton(self.menubar)
        self.btn_graph_Stop.setObjectName(u"btn_graph_Stop")
        icon5 = QIcon()
        icon5.addFile(u":/assets/assets/pause.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_graph_Stop.setIcon(icon5)
        self.btn_graph_Stop.setCheckable(True)
        self.btn_graph_Stop.setChecked(True)

        self.horizontalLayout.addWidget(self.btn_graph_Stop)

        self.btn_graph_Clear = QPushButton(self.menubar)
        self.btn_graph_Clear.setObjectName(u"btn_graph_Clear")
        icon6 = QIcon()
        icon6.addFile(u":/assets/assets/broom.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_graph_Clear.setIcon(icon6)
        self.btn_graph_Clear.setFlat(False)

        self.horizontalLayout.addWidget(self.btn_graph_Clear)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnDataExport = QPushButton(self.menubar)
        self.btnDataExport.setObjectName(u"btnDataExport")
        self.btnDataExport.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u":/assets/assets/export.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnDataExport.setIcon(icon7)
        self.btnDataExport.setCheckable(True)

        self.horizontalLayout.addWidget(self.btnDataExport)

        self.btnImport = QPushButton(self.menubar)
        self.btnImport.setObjectName(u"btnImport")
        icon8 = QIcon()
        icon8.addFile(u":/assets/assets/import.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnImport.setIcon(icon8)
        self.btnImport.setCheckable(True)

        self.horizontalLayout.addWidget(self.btnImport)

        self.btnHelp = QPushButton(self.menubar)
        self.btnHelp.setObjectName(u"btnHelp")
        self.btnHelp.setCursor(QCursor(Qt.CursorShape.WhatsThisCursor))
        icon9 = QIcon()
        icon9.addFile(u":/assets/assets/help.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnHelp.setIcon(icon9)
        self.btnHelp.setCheckable(True)

        self.horizontalLayout.addWidget(self.btnHelp)

        self.btnLanguage = QPushButton(self.menubar)
        self.btnLanguage.setObjectName(u"btnLanguage")
        icon10 = QIcon()
        icon10.addFile(u":/assets/assets/pl.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnLanguage.setIcon(icon10)

        self.horizontalLayout.addWidget(self.btnLanguage)


        self.verticalLayout_2.addWidget(self.menubar)

        self.container = QStackedWidget(self.centralwidget)
        self.container.setObjectName(u"container")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.container.sizePolicy().hasHeightForWidth())
        self.container.setSizePolicy(sizePolicy2)
        self.Controls = QWidget()
        self.Controls.setObjectName(u"Controls")
        self.verticalLayout = QVBoxLayout(self.Controls)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stackControllerDesc = QStackedWidget(self.Controls)
        self.stackControllerDesc.setObjectName(u"stackControllerDesc")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.stackControllerDesc.sizePolicy().hasHeightForWidth())
        self.stackControllerDesc.setSizePolicy(sizePolicy3)
        font = QFont()
        font.setPointSize(12)
        self.stackControllerDesc.setFont(font)
        self.controllerDescHeater = QWidget()
        self.controllerDescHeater.setObjectName(u"controllerDescHeater")
        self.horizontalLayout_43 = QHBoxLayout(self.controllerDescHeater)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.lblControls = QLabel(self.controllerDescHeater)
        self.lblControls.setObjectName(u"lblControls")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(12)
        font1.setBold(False)
        self.lblControls.setFont(font1)

        self.horizontalLayout_43.addWidget(self.lblControls)

        self.frame_59 = QFrame(self.controllerDescHeater)
        self.frame_59.setObjectName(u"frame_59")
        self.frame_59.setFrameShape(QFrame.StyledPanel)
        self.frame_59.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_59)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_34 = QSpacerItem(1220, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_34)

        self.btnHeaterStart = QPushButton(self.frame_59)
        self.btnHeaterStart.setObjectName(u"btnHeaterStart")
        font2 = QFont()
        font2.setPointSize(9)
        self.btnHeaterStart.setFont(font2)
        self.btnHeaterStart.setCheckable(True)

        self.horizontalLayout_17.addWidget(self.btnHeaterStart)


        self.horizontalLayout_43.addWidget(self.frame_59)

        self.stackControllerDesc.addWidget(self.controllerDescHeater)
        self.controllerDescFan = QWidget()
        self.controllerDescFan.setObjectName(u"controllerDescFan")
        self.horizontalLayout_42 = QHBoxLayout(self.controllerDescFan)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.label_21 = QLabel(self.controllerDescFan)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font)

        self.horizontalLayout_42.addWidget(self.label_21)

        self.frame_57 = QFrame(self.controllerDescFan)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setFrameShape(QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_57)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_33 = QSpacerItem(1184, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_33)

        self.btnFanStart = QPushButton(self.frame_57)
        self.btnFanStart.setObjectName(u"btnFanStart")
        self.btnFanStart.setFont(font2)
        self.btnFanStart.setCheckable(True)

        self.horizontalLayout_18.addWidget(self.btnFanStart)


        self.horizontalLayout_42.addWidget(self.frame_57)

        self.stackControllerDesc.addWidget(self.controllerDescFan)

        self.verticalLayout.addWidget(self.stackControllerDesc)

        self.stackControllerSelect = QStackedWidget(self.Controls)
        self.stackControllerSelect.setObjectName(u"stackControllerSelect")
        sizePolicy3.setHeightForWidth(self.stackControllerSelect.sizePolicy().hasHeightForWidth())
        self.stackControllerSelect.setSizePolicy(sizePolicy3)
        self.pageHeaterControllerSelect = QWidget()
        self.pageHeaterControllerSelect.setObjectName(u"pageHeaterControllerSelect")
        self.horizontalLayout_3 = QHBoxLayout(self.pageHeaterControllerSelect)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.pageHeaterControllerSelect)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_4)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 26))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_56 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.horizontalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.frame_5)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.lblHeaterController = QLabel(self.frame_9)
        self.lblHeaterController.setObjectName(u"lblHeaterController")

        self.horizontalLayout_14.addWidget(self.lblHeaterController)

        self.btnHeaterControllerSetNone = QPushButton(self.frame_9)
        self.btnHeaterControllerSetNone.setObjectName(u"btnHeaterControllerSetNone")
        self.btnHeaterControllerSetNone.setCheckable(True)

        self.horizontalLayout_14.addWidget(self.btnHeaterControllerSetNone)

        self.btnHeaterControllerSetBB = QPushButton(self.frame_9)
        self.btnHeaterControllerSetBB.setObjectName(u"btnHeaterControllerSetBB")
        self.btnHeaterControllerSetBB.setCheckable(True)
        self.btnHeaterControllerSetBB.setChecked(True)

        self.horizontalLayout_14.addWidget(self.btnHeaterControllerSetBB)

        self.btnHeaterControllerSetPID = QPushButton(self.frame_9)
        self.btnHeaterControllerSetPID.setObjectName(u"btnHeaterControllerSetPID")
        self.btnHeaterControllerSetPID.setCheckable(True)

        self.horizontalLayout_14.addWidget(self.btnHeaterControllerSetPID)


        self.horizontalLayout_56.addWidget(self.frame_9)

        self.line_11 = QFrame(self.frame_5)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.Shape.VLine)
        self.line_11.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_56.addWidget(self.line_11)

        self.frame_10 = QFrame(self.frame_5)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
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


        self.horizontalLayout_56.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.frame_5)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.line_12 = QFrame(self.frame_11)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShape(QFrame.Shape.VLine)
        self.line_12.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_16.addWidget(self.line_12)

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


        self.horizontalLayout_56.addWidget(self.frame_11)

        self.line_13 = QFrame(self.frame_5)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setFrameShape(QFrame.Shape.VLine)
        self.line_13.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_56.addWidget(self.line_13)

        self.frame_64 = QFrame(self.frame_5)
        self.frame_64.setObjectName(u"frame_64")
        self.frame_64.setFrameShape(QFrame.StyledPanel)
        self.frame_64.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_54 = QHBoxLayout(self.frame_64)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.horizontalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame_64)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_6.addWidget(self.label_5)

        self.inHeaterBBPower = QSlider(self.frame_3)
        self.inHeaterBBPower.setObjectName(u"inHeaterBBPower")
        self.inHeaterBBPower.setEnabled(True)
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.inHeaterBBPower.sizePolicy().hasHeightForWidth())
        self.inHeaterBBPower.setSizePolicy(sizePolicy4)
        self.inHeaterBBPower.setMinimumSize(QSize(150, 0))
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


        self.horizontalLayout_54.addWidget(self.frame_3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_54.addItem(self.horizontalSpacer_2)

        self.label_61 = QLabel(self.frame_64)
        self.label_61.setObjectName(u"label_61")

        self.horizontalLayout_54.addWidget(self.label_61)

        self.chxFanCooling = QCheckBox(self.frame_64)
        self.chxFanCooling.setObjectName(u"chxFanCooling")

        self.horizontalLayout_54.addWidget(self.chxFanCooling)


        self.horizontalLayout_56.addWidget(self.frame_64)


        self.verticalLayout_18.addWidget(self.frame_5)

        self.frHeaterConfig = QFrame(self.frame_4)
        self.frHeaterConfig.setObjectName(u"frHeaterConfig")
        self.frHeaterConfig.setFrameShape(QFrame.StyledPanel)
        self.frHeaterConfig.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_49 = QHBoxLayout(self.frHeaterConfig)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.horizontalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.frHeaterSetValue = QFrame(self.frHeaterConfig)
        self.frHeaterSetValue.setObjectName(u"frHeaterSetValue")
        self.frHeaterSetValue.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_9 = QHBoxLayout(self.frHeaterSetValue)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.frHeaterSetValue)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_9.addWidget(self.label_10)

        self.inHeaterSetValue = QSpinBox(self.frHeaterSetValue)
        self.inHeaterSetValue.setObjectName(u"inHeaterSetValue")
        self.inHeaterSetValue.setMinimumSize(QSize(80, 0))
        self.inHeaterSetValue.setFrame(True)
        self.inHeaterSetValue.setKeyboardTracking(True)
        self.inHeaterSetValue.setMaximum(100)

        self.horizontalLayout_9.addWidget(self.inHeaterSetValue)

        self.label_11 = QLabel(self.frHeaterSetValue)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_9.addWidget(self.label_11)


        self.horizontalLayout_49.addWidget(self.frHeaterSetValue)

        self.frame_63 = QFrame(self.frHeaterConfig)
        self.frame_63.setObjectName(u"frame_63")
        self.frame_63.setFrameShape(QFrame.StyledPanel)
        self.frame_63.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_50 = QHBoxLayout(self.frame_63)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.horizontalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.label_54 = QLabel(self.frame_63)
        self.label_54.setObjectName(u"label_54")

        self.horizontalLayout_50.addWidget(self.label_54)

        self.btnHeaterRefStep = QPushButton(self.frame_63)
        self.btnHeaterRefStep.setObjectName(u"btnHeaterRefStep")
        self.btnHeaterRefStep.setCheckable(True)
        self.btnHeaterRefStep.setChecked(True)

        self.horizontalLayout_50.addWidget(self.btnHeaterRefStep)

        self.btnHeaterRefRamp = QPushButton(self.frame_63)
        self.btnHeaterRefRamp.setObjectName(u"btnHeaterRefRamp")
        self.btnHeaterRefRamp.setCheckable(True)

        self.horizontalLayout_50.addWidget(self.btnHeaterRefRamp)

        self.btnHeaterRefSinewave = QPushButton(self.frame_63)
        self.btnHeaterRefSinewave.setObjectName(u"btnHeaterRefSinewave")
        self.btnHeaterRefSinewave.setCheckable(True)

        self.horizontalLayout_50.addWidget(self.btnHeaterRefSinewave)


        self.horizontalLayout_49.addWidget(self.frame_63)

        self.frHeaterRefSlope = QFrame(self.frHeaterConfig)
        self.frHeaterRefSlope.setObjectName(u"frHeaterRefSlope")
        self.frHeaterRefSlope.setFrameShape(QFrame.StyledPanel)
        self.frHeaterRefSlope.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_51 = QHBoxLayout(self.frHeaterRefSlope)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.horizontalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.label_55 = QLabel(self.frHeaterRefSlope)
        self.label_55.setObjectName(u"label_55")

        self.horizontalLayout_51.addWidget(self.label_55)

        self.inHeaterRefSlope = QSpinBox(self.frHeaterRefSlope)
        self.inHeaterRefSlope.setObjectName(u"inHeaterRefSlope")
        self.inHeaterRefSlope.setMinimumSize(QSize(80, 0))
        self.inHeaterRefSlope.setMaximum(9999)

        self.horizontalLayout_51.addWidget(self.inHeaterRefSlope)

        self.label_56 = QLabel(self.frHeaterRefSlope)
        self.label_56.setObjectName(u"label_56")

        self.horizontalLayout_51.addWidget(self.label_56)


        self.horizontalLayout_49.addWidget(self.frHeaterRefSlope)

        self.frHeaterRefAmplitude = QFrame(self.frHeaterConfig)
        self.frHeaterRefAmplitude.setObjectName(u"frHeaterRefAmplitude")
        self.frHeaterRefAmplitude.setFrameShape(QFrame.StyledPanel)
        self.frHeaterRefAmplitude.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_52 = QHBoxLayout(self.frHeaterRefAmplitude)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.horizontalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.label_57 = QLabel(self.frHeaterRefAmplitude)
        self.label_57.setObjectName(u"label_57")

        self.horizontalLayout_52.addWidget(self.label_57)

        self.inHeaterRefAmplitude = QSpinBox(self.frHeaterRefAmplitude)
        self.inHeaterRefAmplitude.setObjectName(u"inHeaterRefAmplitude")
        self.inHeaterRefAmplitude.setMinimumSize(QSize(80, 0))
        self.inHeaterRefAmplitude.setMaximum(9999)

        self.horizontalLayout_52.addWidget(self.inHeaterRefAmplitude)

        self.label_58 = QLabel(self.frHeaterRefAmplitude)
        self.label_58.setObjectName(u"label_58")

        self.horizontalLayout_52.addWidget(self.label_58)


        self.horizontalLayout_49.addWidget(self.frHeaterRefAmplitude)

        self.frHeaterRefOmega = QFrame(self.frHeaterConfig)
        self.frHeaterRefOmega.setObjectName(u"frHeaterRefOmega")
        self.frHeaterRefOmega.setFrameShape(QFrame.StyledPanel)
        self.frHeaterRefOmega.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_53 = QHBoxLayout(self.frHeaterRefOmega)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.horizontalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.label_59 = QLabel(self.frHeaterRefOmega)
        self.label_59.setObjectName(u"label_59")

        self.horizontalLayout_53.addWidget(self.label_59)

        self.inHeaterRefOmega = QDoubleSpinBox(self.frHeaterRefOmega)
        self.inHeaterRefOmega.setObjectName(u"inHeaterRefOmega")
        self.inHeaterRefOmega.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_53.addWidget(self.inHeaterRefOmega)

        self.label_60 = QLabel(self.frHeaterRefOmega)
        self.label_60.setObjectName(u"label_60")

        self.horizontalLayout_53.addWidget(self.label_60)


        self.horizontalLayout_49.addWidget(self.frHeaterRefOmega)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_49.addItem(self.horizontalSpacer_21)


        self.verticalLayout_18.addWidget(self.frHeaterConfig)


        self.horizontalLayout_3.addWidget(self.frame_4)

        self.stackControllerSelect.addWidget(self.pageHeaterControllerSelect)
        self.pageFanControllerSelect = QWidget()
        self.pageFanControllerSelect.setObjectName(u"pageFanControllerSelect")
        self.horizontalLayout_7 = QHBoxLayout(self.pageFanControllerSelect)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.pageFanControllerSelect)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(16777215, 26))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.frame_6)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_4.addWidget(self.label_9)

        self.btnFanControllerSetNone = QPushButton(self.frame_6)
        self.btnFanControllerSetNone.setObjectName(u"btnFanControllerSetNone")
        self.btnFanControllerSetNone.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.btnFanControllerSetNone)

        self.btnFanControllerSetBB = QPushButton(self.frame_6)
        self.btnFanControllerSetBB.setObjectName(u"btnFanControllerSetBB")
        self.btnFanControllerSetBB.setCheckable(True)
        self.btnFanControllerSetBB.setChecked(True)

        self.horizontalLayout_4.addWidget(self.btnFanControllerSetBB)

        self.btnFanControllerSetPID = QPushButton(self.frame_6)
        self.btnFanControllerSetPID.setObjectName(u"btnFanControllerSetPID")
        self.btnFanControllerSetPID.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.btnFanControllerSetPID)

        self.frFanPWM = QFrame(self.frame_6)
        self.frFanPWM.setObjectName(u"frFanPWM")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frFanPWM.sizePolicy().hasHeightForWidth())
        self.frFanPWM.setSizePolicy(sizePolicy5)
        self.frFanPWM.setFrameShape(QFrame.StyledPanel)
        self.frFanPWM.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frFanPWM)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frFanPWM)
        self.label.setObjectName(u"label")

        self.horizontalLayout_20.addWidget(self.label)

        self.inFanPWM = QSlider(self.frFanPWM)
        self.inFanPWM.setObjectName(u"inFanPWM")
        self.inFanPWM.setMinimumSize(QSize(150, 0))
        self.inFanPWM.setMaximumSize(QSize(200, 16777215))
        self.inFanPWM.setMaximum(100)
        self.inFanPWM.setOrientation(Qt.Horizontal)

        self.horizontalLayout_20.addWidget(self.inFanPWM)

        self.lblFanPWM = QLabel(self.frFanPWM)
        self.lblFanPWM.setObjectName(u"lblFanPWM")

        self.horizontalLayout_20.addWidget(self.lblFanPWM)

        self.label_22 = QLabel(self.frFanPWM)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_20.addWidget(self.label_22)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_5)


        self.horizontalLayout_4.addWidget(self.frFanPWM)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)


        self.verticalLayout_19.addWidget(self.frame_6)

        self.frFanConfig = QFrame(self.frame)
        self.frFanConfig.setObjectName(u"frFanConfig")
        self.frFanConfig.setFrameShape(QFrame.StyledPanel)
        self.frFanConfig.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_48 = QHBoxLayout(self.frFanConfig)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.frFanSetValue = QFrame(self.frFanConfig)
        self.frFanSetValue.setObjectName(u"frFanSetValue")
        self.frFanSetValue.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_23 = QHBoxLayout(self.frFanSetValue)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.label_26 = QLabel(self.frFanSetValue)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_23.addWidget(self.label_26)

        self.inFanSetValue = QSpinBox(self.frFanSetValue)
        self.inFanSetValue.setObjectName(u"inFanSetValue")
        self.inFanSetValue.setMinimumSize(QSize(80, 0))
        self.inFanSetValue.setMaximum(6000)

        self.horizontalLayout_23.addWidget(self.inFanSetValue)

        self.label_27 = QLabel(self.frFanSetValue)
        self.label_27.setObjectName(u"label_27")

        self.horizontalLayout_23.addWidget(self.label_27)


        self.horizontalLayout_48.addWidget(self.frFanSetValue)

        self.frame_61 = QFrame(self.frFanConfig)
        self.frame_61.setObjectName(u"frame_61")
        self.frame_61.setFrameShape(QFrame.StyledPanel)
        self.frame_61.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.frame_61)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.label_19 = QLabel(self.frame_61)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_44.addWidget(self.label_19)

        self.btnFanRefStep = QPushButton(self.frame_61)
        self.btnFanRefStep.setObjectName(u"btnFanRefStep")
        self.btnFanRefStep.setCheckable(True)
        self.btnFanRefStep.setChecked(True)

        self.horizontalLayout_44.addWidget(self.btnFanRefStep)

        self.btnFanRefRamp = QPushButton(self.frame_61)
        self.btnFanRefRamp.setObjectName(u"btnFanRefRamp")
        self.btnFanRefRamp.setCheckable(True)

        self.horizontalLayout_44.addWidget(self.btnFanRefRamp)

        self.btnFanRefSinewave = QPushButton(self.frame_61)
        self.btnFanRefSinewave.setObjectName(u"btnFanRefSinewave")
        self.btnFanRefSinewave.setCheckable(True)

        self.horizontalLayout_44.addWidget(self.btnFanRefSinewave)


        self.horizontalLayout_48.addWidget(self.frame_61)

        self.frFanRefSlope = QFrame(self.frFanConfig)
        self.frFanRefSlope.setObjectName(u"frFanRefSlope")
        self.frFanRefSlope.setFrameShape(QFrame.StyledPanel)
        self.frFanRefSlope.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_45 = QHBoxLayout(self.frFanRefSlope)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.label_35 = QLabel(self.frFanRefSlope)
        self.label_35.setObjectName(u"label_35")

        self.horizontalLayout_45.addWidget(self.label_35)

        self.inFanRefSlope = QSpinBox(self.frFanRefSlope)
        self.inFanRefSlope.setObjectName(u"inFanRefSlope")
        self.inFanRefSlope.setMinimumSize(QSize(80, 0))
        self.inFanRefSlope.setMaximum(9999)

        self.horizontalLayout_45.addWidget(self.inFanRefSlope)

        self.label_51 = QLabel(self.frFanRefSlope)
        self.label_51.setObjectName(u"label_51")

        self.horizontalLayout_45.addWidget(self.label_51)


        self.horizontalLayout_48.addWidget(self.frFanRefSlope)

        self.frFanRefAmplitude = QFrame(self.frFanConfig)
        self.frFanRefAmplitude.setObjectName(u"frFanRefAmplitude")
        self.frFanRefAmplitude.setFrameShape(QFrame.StyledPanel)
        self.frFanRefAmplitude.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_46 = QHBoxLayout(self.frFanRefAmplitude)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.label_49 = QLabel(self.frFanRefAmplitude)
        self.label_49.setObjectName(u"label_49")

        self.horizontalLayout_46.addWidget(self.label_49)

        self.inFanRefAmplitude = QSpinBox(self.frFanRefAmplitude)
        self.inFanRefAmplitude.setObjectName(u"inFanRefAmplitude")
        self.inFanRefAmplitude.setMinimumSize(QSize(80, 0))
        self.inFanRefAmplitude.setMaximum(9999)

        self.horizontalLayout_46.addWidget(self.inFanRefAmplitude)

        self.label_52 = QLabel(self.frFanRefAmplitude)
        self.label_52.setObjectName(u"label_52")

        self.horizontalLayout_46.addWidget(self.label_52)


        self.horizontalLayout_48.addWidget(self.frFanRefAmplitude)

        self.frFanRefOmega = QFrame(self.frFanConfig)
        self.frFanRefOmega.setObjectName(u"frFanRefOmega")
        self.frFanRefOmega.setFrameShape(QFrame.StyledPanel)
        self.frFanRefOmega.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_47 = QHBoxLayout(self.frFanRefOmega)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.label_50 = QLabel(self.frFanRefOmega)
        self.label_50.setObjectName(u"label_50")

        self.horizontalLayout_47.addWidget(self.label_50)

        self.inFanRefOmega = QDoubleSpinBox(self.frFanRefOmega)
        self.inFanRefOmega.setObjectName(u"inFanRefOmega")
        self.inFanRefOmega.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_47.addWidget(self.inFanRefOmega)

        self.label_53 = QLabel(self.frFanRefOmega)
        self.label_53.setObjectName(u"label_53")

        self.horizontalLayout_47.addWidget(self.label_53)


        self.horizontalLayout_48.addWidget(self.frFanRefOmega)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_48.addItem(self.horizontalSpacer_12)


        self.verticalLayout_19.addWidget(self.frFanConfig)


        self.horizontalLayout_7.addWidget(self.frame)

        self.stackControllerSelect.addWidget(self.pageFanControllerSelect)

        self.verticalLayout.addWidget(self.stackControllerSelect)

        self.stackController = StackedWidget(self.Controls)
        self.stackController.setObjectName(u"stackController")
        sizePolicy.setHeightForWidth(self.stackController.sizePolicy().hasHeightForWidth())
        self.stackController.setSizePolicy(sizePolicy)
        self.pageHeaterControllerConfigBB = QWidget()
        self.pageHeaterControllerConfigBB.setObjectName(u"pageHeaterControllerConfigBB")
        self.horizontalLayout_2 = QHBoxLayout(self.pageHeaterControllerConfigBB)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.pageHeaterControllerConfigBB)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
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

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.btnBBHeaterHelp = QPushButton(self.frame_2)
        self.btnBBHeaterHelp.setObjectName(u"btnBBHeaterHelp")
        self.btnBBHeaterHelp.setIcon(icon9)

        self.horizontalLayout_5.addWidget(self.btnBBHeaterHelp)


        self.horizontalLayout_2.addWidget(self.frame_2)

        self.stackController.addWidget(self.pageHeaterControllerConfigBB)
        self.pageHeaterControllerConfigPID = QWidget()
        self.pageHeaterControllerConfigPID.setObjectName(u"pageHeaterControllerConfigPID")
        self.verticalLayout_5 = QVBoxLayout(self.pageHeaterControllerConfigPID)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_22 = QFrame(self.pageHeaterControllerConfigPID)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.frHeaterKp = QFrame(self.frame_22)
        self.frHeaterKp.setObjectName(u"frHeaterKp")
        self.frHeaterKp.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_10 = QHBoxLayout(self.frHeaterKp)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.frHeaterKp)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_10.addWidget(self.label_12)

        self.inHeaterPID_Kp = QDoubleSpinBox(self.frHeaterKp)
        self.inHeaterPID_Kp.setObjectName(u"inHeaterPID_Kp")
        self.inHeaterPID_Kp.setMinimumSize(QSize(80, 0))
        self.inHeaterPID_Kp.setMaximum(999.990000000000009)

        self.horizontalLayout_10.addWidget(self.inHeaterPID_Kp)

        self.label_13 = QLabel(self.frHeaterKp)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_10.addWidget(self.label_13)


        self.horizontalLayout_30.addWidget(self.frHeaterKp)

        self.frHeaterKi = QFrame(self.frame_22)
        self.frHeaterKi.setObjectName(u"frHeaterKi")
        self.frHeaterKi.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_11 = QHBoxLayout(self.frHeaterKi)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.line_21 = QFrame(self.frHeaterKi)
        self.line_21.setObjectName(u"line_21")
        self.line_21.setFrameShape(QFrame.Shape.VLine)
        self.line_21.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_11.addWidget(self.line_21)

        self.label_14 = QLabel(self.frHeaterKi)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_11.addWidget(self.label_14)

        self.inHeaterPID_Ki = QDoubleSpinBox(self.frHeaterKi)
        self.inHeaterPID_Ki.setObjectName(u"inHeaterPID_Ki")
        self.inHeaterPID_Ki.setMinimumSize(QSize(80, 0))
        self.inHeaterPID_Ki.setMaximum(999.990000000000009)

        self.horizontalLayout_11.addWidget(self.inHeaterPID_Ki)

        self.label_15 = QLabel(self.frHeaterKi)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_11.addWidget(self.label_15)


        self.horizontalLayout_30.addWidget(self.frHeaterKi)

        self.frHeaterTi = QFrame(self.frame_22)
        self.frHeaterTi.setObjectName(u"frHeaterTi")
        self.frHeaterTi.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_31 = QHBoxLayout(self.frHeaterTi)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.line_22 = QFrame(self.frHeaterTi)
        self.line_22.setObjectName(u"line_22")
        self.line_22.setFrameShape(QFrame.Shape.VLine)
        self.line_22.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_31.addWidget(self.line_22)

        self.label_38 = QLabel(self.frHeaterTi)
        self.label_38.setObjectName(u"label_38")

        self.horizontalLayout_31.addWidget(self.label_38)

        self.inHeaterPID_Ti = QDoubleSpinBox(self.frHeaterTi)
        self.inHeaterPID_Ti.setObjectName(u"inHeaterPID_Ti")
        self.inHeaterPID_Ti.setMinimumSize(QSize(80, 0))
        self.inHeaterPID_Ti.setMaximum(999.990000000000009)

        self.horizontalLayout_31.addWidget(self.inHeaterPID_Ti)

        self.label_44 = QLabel(self.frHeaterTi)
        self.label_44.setObjectName(u"label_44")

        self.horizontalLayout_31.addWidget(self.label_44)


        self.horizontalLayout_30.addWidget(self.frHeaterTi)

        self.frHeaterKd = QFrame(self.frame_22)
        self.frHeaterKd.setObjectName(u"frHeaterKd")
        self.frHeaterKd.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_12 = QHBoxLayout(self.frHeaterKd)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.line_23 = QFrame(self.frHeaterKd)
        self.line_23.setObjectName(u"line_23")
        self.line_23.setFrameShape(QFrame.Shape.VLine)
        self.line_23.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_12.addWidget(self.line_23)

        self.label_16 = QLabel(self.frHeaterKd)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_12.addWidget(self.label_16)

        self.inHeaterPID_Kd = QDoubleSpinBox(self.frHeaterKd)
        self.inHeaterPID_Kd.setObjectName(u"inHeaterPID_Kd")
        self.inHeaterPID_Kd.setMinimumSize(QSize(80, 0))
        self.inHeaterPID_Kd.setMaximum(999.990000000000009)

        self.horizontalLayout_12.addWidget(self.inHeaterPID_Kd)

        self.label_17 = QLabel(self.frHeaterKd)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_12.addWidget(self.label_17)


        self.horizontalLayout_30.addWidget(self.frHeaterKd)

        self.frHeaterTd = QFrame(self.frame_22)
        self.frHeaterTd.setObjectName(u"frHeaterTd")
        self.frHeaterTd.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_8 = QHBoxLayout(self.frHeaterTd)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.line_24 = QFrame(self.frHeaterTd)
        self.line_24.setObjectName(u"line_24")
        self.line_24.setFrameShape(QFrame.Shape.VLine)
        self.line_24.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_8.addWidget(self.line_24)

        self.label_43 = QLabel(self.frHeaterTd)
        self.label_43.setObjectName(u"label_43")

        self.horizontalLayout_8.addWidget(self.label_43)

        self.inHeaterPID_Td = QDoubleSpinBox(self.frHeaterTd)
        self.inHeaterPID_Td.setObjectName(u"inHeaterPID_Td")
        self.inHeaterPID_Td.setMinimumSize(QSize(80, 0))
        self.inHeaterPID_Td.setMaximum(999.990000000000009)

        self.horizontalLayout_8.addWidget(self.inHeaterPID_Td)

        self.label_45 = QLabel(self.frHeaterTd)
        self.label_45.setObjectName(u"label_45")

        self.horizontalLayout_8.addWidget(self.label_45)


        self.horizontalLayout_30.addWidget(self.frHeaterTd)

        self.frHeaterRest = QFrame(self.frame_22)
        self.frHeaterRest.setObjectName(u"frHeaterRest")
        self.frHeaterRest.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_13 = QHBoxLayout(self.frHeaterRest)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.line_25 = QFrame(self.frHeaterRest)
        self.line_25.setObjectName(u"line_25")
        self.line_25.setFrameShape(QFrame.Shape.VLine)
        self.line_25.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_13.addWidget(self.line_25)

        self.label_18 = QLabel(self.frHeaterRest)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_13.addWidget(self.label_18)

        self.inHeaterPID_Kaw = QDoubleSpinBox(self.frHeaterRest)
        self.inHeaterPID_Kaw.setObjectName(u"inHeaterPID_Kaw")
        self.inHeaterPID_Kaw.setMinimumSize(QSize(80, 0))
        self.inHeaterPID_Kaw.setToolTipDuration(0)
        self.inHeaterPID_Kaw.setMaximum(999.990000000000009)

        self.horizontalLayout_13.addWidget(self.inHeaterPID_Kaw)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_24)

        self.label_62 = QLabel(self.frHeaterRest)
        self.label_62.setObjectName(u"label_62")

        self.horizontalLayout_13.addWidget(self.label_62)

        self.btnEquationTypeHeater = QPushButton(self.frHeaterRest)
        self.btnEquationTypeHeater.setObjectName(u"btnEquationTypeHeater")

        self.horizontalLayout_13.addWidget(self.btnEquationTypeHeater)


        self.horizontalLayout_30.addWidget(self.frHeaterRest)


        self.verticalLayout_5.addWidget(self.frame_22)

        self.frame_25 = QFrame(self.pageHeaterControllerConfigPID)
        self.frame_25.setObjectName(u"frame_25")
        sizePolicy5.setHeightForWidth(self.frame_25.sizePolicy().hasHeightForWidth())
        self.frame_25.setSizePolicy(sizePolicy5)
        self.frame_25.setMaximumSize(QSize(16777215, 90))
        self.frame_25.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_6 = QVBoxLayout(self.frame_25)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.heaterEquation = QVBoxLayout()
        self.heaterEquation.setObjectName(u"heaterEquation")

        self.verticalLayout_6.addLayout(self.heaterEquation)


        self.verticalLayout_5.addWidget(self.frame_25)

        self.stackController.addWidget(self.pageHeaterControllerConfigPID)
        self.pageFanControllerConfigBB = QWidget()
        self.pageFanControllerConfigBB.setObjectName(u"pageFanControllerConfigBB")
        self.horizontalLayout_19 = QHBoxLayout(self.pageFanControllerConfigBB)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.pageFanControllerConfigBB)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.label_24 = QLabel(self.frame_13)
        self.label_24.setObjectName(u"label_24")

        self.horizontalLayout_21.addWidget(self.label_24)

        self.inFanBBHysteresis = QSpinBox(self.frame_13)
        self.inFanBBHysteresis.setObjectName(u"inFanBBHysteresis")
        self.inFanBBHysteresis.setMinimumSize(QSize(100, 0))
        self.inFanBBHysteresis.setMaximum(999)

        self.horizontalLayout_21.addWidget(self.inFanBBHysteresis)

        self.label_25 = QLabel(self.frame_13)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout_21.addWidget(self.label_25)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_14)

        self.btnBBFanHelp = QPushButton(self.frame_13)
        self.btnBBFanHelp.setObjectName(u"btnBBFanHelp")
        self.btnBBFanHelp.setIcon(icon9)

        self.horizontalLayout_21.addWidget(self.btnBBFanHelp)


        self.horizontalLayout_19.addWidget(self.frame_13)

        self.stackController.addWidget(self.pageFanControllerConfigBB)
        self.pageFanControllerConfigPID = QWidget()
        self.pageFanControllerConfigPID.setObjectName(u"pageFanControllerConfigPID")
        self.verticalLayout_3 = QVBoxLayout(self.pageFanControllerConfigPID)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_20 = QFrame(self.pageFanControllerConfigPID)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.frFanKp = QFrame(self.frame_20)
        self.frFanKp.setObjectName(u"frFanKp")
        self.frFanKp.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_24 = QHBoxLayout(self.frFanKp)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.label_28 = QLabel(self.frFanKp)
        self.label_28.setObjectName(u"label_28")

        self.horizontalLayout_24.addWidget(self.label_28)

        self.inFanPID_Kp = QDoubleSpinBox(self.frFanKp)
        self.inFanPID_Kp.setObjectName(u"inFanPID_Kp")
        self.inFanPID_Kp.setMinimumSize(QSize(80, 0))
        self.inFanPID_Kp.setMaximum(999.990000000000009)

        self.horizontalLayout_24.addWidget(self.inFanPID_Kp)

        self.label_29 = QLabel(self.frFanKp)
        self.label_29.setObjectName(u"label_29")

        self.horizontalLayout_24.addWidget(self.label_29)


        self.horizontalLayout_22.addWidget(self.frFanKp)

        self.frFanKi = QFrame(self.frame_20)
        self.frFanKi.setObjectName(u"frFanKi")
        self.frFanKi.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_25 = QHBoxLayout(self.frFanKi)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.line_15 = QFrame(self.frFanKi)
        self.line_15.setObjectName(u"line_15")
        self.line_15.setFrameShape(QFrame.Shape.VLine)
        self.line_15.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_25.addWidget(self.line_15)

        self.label_30 = QLabel(self.frFanKi)
        self.label_30.setObjectName(u"label_30")

        self.horizontalLayout_25.addWidget(self.label_30)

        self.inFanPID_Ki = QDoubleSpinBox(self.frFanKi)
        self.inFanPID_Ki.setObjectName(u"inFanPID_Ki")
        self.inFanPID_Ki.setMinimumSize(QSize(80, 0))
        self.inFanPID_Ki.setMaximum(999.990000000000009)

        self.horizontalLayout_25.addWidget(self.inFanPID_Ki)

        self.label_31 = QLabel(self.frFanKi)
        self.label_31.setObjectName(u"label_31")

        self.horizontalLayout_25.addWidget(self.label_31)


        self.horizontalLayout_22.addWidget(self.frFanKi)

        self.frFanTi = QFrame(self.frame_20)
        self.frFanTi.setObjectName(u"frFanTi")
        self.frFanTi.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_28 = QHBoxLayout(self.frFanTi)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.line_16 = QFrame(self.frFanTi)
        self.line_16.setObjectName(u"line_16")
        self.line_16.setFrameShape(QFrame.Shape.VLine)
        self.line_16.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_28.addWidget(self.line_16)

        self.label_40 = QLabel(self.frFanTi)
        self.label_40.setObjectName(u"label_40")

        self.horizontalLayout_28.addWidget(self.label_40)

        self.inFanPID_Ti = QDoubleSpinBox(self.frFanTi)
        self.inFanPID_Ti.setObjectName(u"inFanPID_Ti")
        self.inFanPID_Ti.setMinimumSize(QSize(80, 0))
        self.inFanPID_Ti.setMaximum(999.990000000000009)

        self.horizontalLayout_28.addWidget(self.inFanPID_Ti)

        self.label_39 = QLabel(self.frFanTi)
        self.label_39.setObjectName(u"label_39")

        self.horizontalLayout_28.addWidget(self.label_39)


        self.horizontalLayout_22.addWidget(self.frFanTi)

        self.frFanKd = QFrame(self.frame_20)
        self.frFanKd.setObjectName(u"frFanKd")
        self.frFanKd.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_26 = QHBoxLayout(self.frFanKd)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.line_17 = QFrame(self.frFanKd)
        self.line_17.setObjectName(u"line_17")
        self.line_17.setFrameShape(QFrame.Shape.VLine)
        self.line_17.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_26.addWidget(self.line_17)

        self.label_32 = QLabel(self.frFanKd)
        self.label_32.setObjectName(u"label_32")

        self.horizontalLayout_26.addWidget(self.label_32)

        self.inFanPID_Kd = QDoubleSpinBox(self.frFanKd)
        self.inFanPID_Kd.setObjectName(u"inFanPID_Kd")
        self.inFanPID_Kd.setMinimumSize(QSize(80, 0))
        self.inFanPID_Kd.setMaximum(999.990000000000009)

        self.horizontalLayout_26.addWidget(self.inFanPID_Kd)

        self.label_33 = QLabel(self.frFanKd)
        self.label_33.setObjectName(u"label_33")

        self.horizontalLayout_26.addWidget(self.label_33)


        self.horizontalLayout_22.addWidget(self.frFanKd)

        self.frFanTd = QFrame(self.frame_20)
        self.frFanTd.setObjectName(u"frFanTd")
        self.frFanTd.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_29 = QHBoxLayout(self.frFanTd)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.line_18 = QFrame(self.frFanTd)
        self.line_18.setObjectName(u"line_18")
        self.line_18.setFrameShape(QFrame.Shape.VLine)
        self.line_18.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_29.addWidget(self.line_18)

        self.label_42 = QLabel(self.frFanTd)
        self.label_42.setObjectName(u"label_42")

        self.horizontalLayout_29.addWidget(self.label_42)

        self.inFanPID_Td = QDoubleSpinBox(self.frFanTd)
        self.inFanPID_Td.setObjectName(u"inFanPID_Td")
        self.inFanPID_Td.setMinimumSize(QSize(80, 0))
        self.inFanPID_Td.setMaximum(999.990000000000009)

        self.horizontalLayout_29.addWidget(self.inFanPID_Td)

        self.label_41 = QLabel(self.frFanTd)
        self.label_41.setObjectName(u"label_41")

        self.horizontalLayout_29.addWidget(self.label_41)


        self.horizontalLayout_22.addWidget(self.frFanTd)

        self.frFanRest = QFrame(self.frame_20)
        self.frFanRest.setObjectName(u"frFanRest")
        self.frFanRest.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_27 = QHBoxLayout(self.frFanRest)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.line_19 = QFrame(self.frFanRest)
        self.line_19.setObjectName(u"line_19")
        self.line_19.setFrameShape(QFrame.Shape.VLine)
        self.line_19.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_27.addWidget(self.line_19)

        self.label_34 = QLabel(self.frFanRest)
        self.label_34.setObjectName(u"label_34")

        self.horizontalLayout_27.addWidget(self.label_34)

        self.inFanPID_Kaw = QDoubleSpinBox(self.frFanRest)
        self.inFanPID_Kaw.setObjectName(u"inFanPID_Kaw")
        self.inFanPID_Kaw.setMinimumSize(QSize(80, 0))
        self.inFanPID_Kaw.setMaximum(999.990000000000009)

        self.horizontalLayout_27.addWidget(self.inFanPID_Kaw)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_13)

        self.label_63 = QLabel(self.frFanRest)
        self.label_63.setObjectName(u"label_63")

        self.horizontalLayout_27.addWidget(self.label_63)

        self.btnEquationTypeFan = QPushButton(self.frFanRest)
        self.btnEquationTypeFan.setObjectName(u"btnEquationTypeFan")

        self.horizontalLayout_27.addWidget(self.btnEquationTypeFan)


        self.horizontalLayout_22.addWidget(self.frFanRest)


        self.verticalLayout_3.addWidget(self.frame_20)

        self.frame_26 = QFrame(self.pageFanControllerConfigPID)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setMaximumSize(QSize(16777215, 90))
        self.frame_26.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_7 = QVBoxLayout(self.frame_26)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.fanEquation = QVBoxLayout()
        self.fanEquation.setObjectName(u"fanEquation")

        self.verticalLayout_7.addLayout(self.fanEquation)


        self.verticalLayout_3.addWidget(self.frame_26)

        self.stackController.addWidget(self.pageFanControllerConfigPID)

        self.verticalLayout.addWidget(self.stackController)

        self.stackGraphs = QStackedWidget(self.Controls)
        self.stackGraphs.setObjectName(u"stackGraphs")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.stackGraphs.sizePolicy().hasHeightForWidth())
        self.stackGraphs.setSizePolicy(sizePolicy6)
        self.pageHeaterBBGraph = QWidget()
        self.pageHeaterBBGraph.setObjectName(u"pageHeaterBBGraph")
        sizePolicy6.setHeightForWidth(self.pageHeaterBBGraph.sizePolicy().hasHeightForWidth())
        self.pageHeaterBBGraph.setSizePolicy(sizePolicy6)
        self.verticalLayout_9 = QVBoxLayout(self.pageHeaterBBGraph)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.layHeaterBBGraph = QHBoxLayout()
        self.layHeaterBBGraph.setSpacing(0)
        self.layHeaterBBGraph.setObjectName(u"layHeaterBBGraph")

        self.verticalLayout_9.addLayout(self.layHeaterBBGraph)

        self.frame_29 = QFrame(self.pageHeaterBBGraph)
        self.frame_29.setObjectName(u"frame_29")
        sizePolicy3.setHeightForWidth(self.frame_29.sizePolicy().hasHeightForWidth())
        self.frame_29.setSizePolicy(sizePolicy3)
        self.frame_29.setFrameShape(QFrame.NoFrame)
        self.gridLayout_4 = QGridLayout(self.frame_29)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btnHeaterBB_graph_u_min = QPushButton(self.frame_29)
        self.btnHeaterBB_graph_u_min.setObjectName(u"btnHeaterBB_graph_u_min")
        self.btnHeaterBB_graph_u_min.setCheckable(True)
        self.btnHeaterBB_graph_u_min.setChecked(False)

        self.gridLayout_4.addWidget(self.btnHeaterBB_graph_u_min, 0, 8, 1, 1)

        self.lcdHeaterBB_x_max = QLCDNumber(self.frame_29)
        self.lcdHeaterBB_x_max.setObjectName(u"lcdHeaterBB_x_max")
        self.lcdHeaterBB_x_max.setFrameShadow(QFrame.Plain)
        self.lcdHeaterBB_x_max.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_4.addWidget(self.lcdHeaterBB_x_max, 1, 5, 1, 1)

        self.lcdHeaterBB_y_2 = QLCDNumber(self.frame_29)
        self.lcdHeaterBB_y_2.setObjectName(u"lcdHeaterBB_y_2")
        self.lcdHeaterBB_y_2.setFrameShadow(QFrame.Plain)
        self.lcdHeaterBB_y_2.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_4.addWidget(self.lcdHeaterBB_y_2, 1, 2, 1, 1)

        self.btnHeaterBB_graph_y_2 = QPushButton(self.frame_29)
        self.btnHeaterBB_graph_y_2.setObjectName(u"btnHeaterBB_graph_y_2")
        self.btnHeaterBB_graph_y_2.setCheckable(True)
        self.btnHeaterBB_graph_y_2.setChecked(True)

        self.gridLayout_4.addWidget(self.btnHeaterBB_graph_y_2, 0, 2, 1, 1)

        self.lcdHeaterBB_mode = QLCDNumber(self.frame_29)
        self.lcdHeaterBB_mode.setObjectName(u"lcdHeaterBB_mode")
        self.lcdHeaterBB_mode.setFrameShadow(QFrame.Plain)
        self.lcdHeaterBB_mode.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_4.addWidget(self.lcdHeaterBB_mode, 1, 9, 1, 1)

        self.lcdHeaterBB_u_max = QLCDNumber(self.frame_29)
        self.lcdHeaterBB_u_max.setObjectName(u"lcdHeaterBB_u_max")
        self.lcdHeaterBB_u_max.setFrameShadow(QFrame.Plain)
        self.lcdHeaterBB_u_max.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_4.addWidget(self.lcdHeaterBB_u_max, 1, 7, 1, 1)

        self.btnHeaterBB_graph_u_max = QPushButton(self.frame_29)
        self.btnHeaterBB_graph_u_max.setObjectName(u"btnHeaterBB_graph_u_max")
        self.btnHeaterBB_graph_u_max.setCheckable(True)
        self.btnHeaterBB_graph_u_max.setChecked(False)

        self.gridLayout_4.addWidget(self.btnHeaterBB_graph_u_max, 0, 7, 1, 1)

        self.lcdHeaterBB_x = QLCDNumber(self.frame_29)
        self.lcdHeaterBB_x.setObjectName(u"lcdHeaterBB_x")
        self.lcdHeaterBB_x.setFrameShadow(QFrame.Plain)
        self.lcdHeaterBB_x.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_4.addWidget(self.lcdHeaterBB_x, 1, 0, 1, 1)

        self.btnHeaterBB_graph_x_max = QPushButton(self.frame_29)
        self.btnHeaterBB_graph_x_max.setObjectName(u"btnHeaterBB_graph_x_max")
        self.btnHeaterBB_graph_x_max.setCheckable(True)
        self.btnHeaterBB_graph_x_max.setChecked(False)

        self.gridLayout_4.addWidget(self.btnHeaterBB_graph_x_max, 0, 5, 1, 1)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_22, 0, 12, 1, 1)

        self.btnHeaterBB_graph_x = QPushButton(self.frame_29)
        self.btnHeaterBB_graph_x.setObjectName(u"btnHeaterBB_graph_x")
        self.btnHeaterBB_graph_x.setCheckable(True)
        self.btnHeaterBB_graph_x.setChecked(True)

        self.gridLayout_4.addWidget(self.btnHeaterBB_graph_x, 0, 0, 1, 1)

        self.lcdHeaterBB_x_min = QLCDNumber(self.frame_29)
        self.lcdHeaterBB_x_min.setObjectName(u"lcdHeaterBB_x_min")
        self.lcdHeaterBB_x_min.setFrameShadow(QFrame.Plain)
        self.lcdHeaterBB_x_min.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_4.addWidget(self.lcdHeaterBB_x_min, 1, 6, 1, 1)

        self.lcdHeaterBB_e = QLCDNumber(self.frame_29)
        self.lcdHeaterBB_e.setObjectName(u"lcdHeaterBB_e")
        self.lcdHeaterBB_e.setFrameShadow(QFrame.Plain)
        self.lcdHeaterBB_e.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_4.addWidget(self.lcdHeaterBB_e, 1, 3, 1, 1)

        self.btnHeaterBB_graph_mode = QPushButton(self.frame_29)
        self.btnHeaterBB_graph_mode.setObjectName(u"btnHeaterBB_graph_mode")
        self.btnHeaterBB_graph_mode.setCheckable(True)
        self.btnHeaterBB_graph_mode.setChecked(False)

        self.gridLayout_4.addWidget(self.btnHeaterBB_graph_mode, 0, 9, 1, 1)

        self.btnHeaterBB_graph_x_min = QPushButton(self.frame_29)
        self.btnHeaterBB_graph_x_min.setObjectName(u"btnHeaterBB_graph_x_min")
        self.btnHeaterBB_graph_x_min.setCheckable(True)
        self.btnHeaterBB_graph_x_min.setChecked(False)

        self.gridLayout_4.addWidget(self.btnHeaterBB_graph_x_min, 0, 6, 1, 1)

        self.lcdHeaterBB_u_min = QLCDNumber(self.frame_29)
        self.lcdHeaterBB_u_min.setObjectName(u"lcdHeaterBB_u_min")
        self.lcdHeaterBB_u_min.setFrameShadow(QFrame.Plain)
        self.lcdHeaterBB_u_min.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_4.addWidget(self.lcdHeaterBB_u_min, 1, 8, 1, 1)

        self.btnHeaterBB_graph_y_1 = QPushButton(self.frame_29)
        self.btnHeaterBB_graph_y_1.setObjectName(u"btnHeaterBB_graph_y_1")
        self.btnHeaterBB_graph_y_1.setCheckable(True)
        self.btnHeaterBB_graph_y_1.setChecked(True)

        self.gridLayout_4.addWidget(self.btnHeaterBB_graph_y_1, 0, 1, 1, 1)

        self.lcdHeaterBB_y_1 = QLCDNumber(self.frame_29)
        self.lcdHeaterBB_y_1.setObjectName(u"lcdHeaterBB_y_1")
        self.lcdHeaterBB_y_1.setFrameShadow(QFrame.Plain)
        self.lcdHeaterBB_y_1.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_4.addWidget(self.lcdHeaterBB_y_1, 1, 1, 1, 1)

        self.lcdHeaterBB_u = QLCDNumber(self.frame_29)
        self.lcdHeaterBB_u.setObjectName(u"lcdHeaterBB_u")
        self.lcdHeaterBB_u.setFrameShadow(QFrame.Plain)
        self.lcdHeaterBB_u.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_4.addWidget(self.lcdHeaterBB_u, 1, 4, 1, 1)

        self.btnHeaterBB_graph_e = QPushButton(self.frame_29)
        self.btnHeaterBB_graph_e.setObjectName(u"btnHeaterBB_graph_e")
        self.btnHeaterBB_graph_e.setCheckable(True)

        self.gridLayout_4.addWidget(self.btnHeaterBB_graph_e, 0, 3, 1, 1)

        self.btnHeaterBB_graph_u = QPushButton(self.frame_29)
        self.btnHeaterBB_graph_u.setObjectName(u"btnHeaterBB_graph_u")
        self.btnHeaterBB_graph_u.setCheckable(True)

        self.gridLayout_4.addWidget(self.btnHeaterBB_graph_u, 0, 4, 1, 1)


        self.verticalLayout_9.addWidget(self.frame_29)

        self.stackGraphs.addWidget(self.pageHeaterBBGraph)
        self.pageHeaterPIDGraph = QWidget()
        self.pageHeaterPIDGraph.setObjectName(u"pageHeaterPIDGraph")
        sizePolicy6.setHeightForWidth(self.pageHeaterPIDGraph.sizePolicy().hasHeightForWidth())
        self.pageHeaterPIDGraph.setSizePolicy(sizePolicy6)
        self.verticalLayout_11 = QVBoxLayout(self.pageHeaterPIDGraph)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.layHeaterPIDGraph = QHBoxLayout()
        self.layHeaterPIDGraph.setSpacing(0)
        self.layHeaterPIDGraph.setObjectName(u"layHeaterPIDGraph")

        self.verticalLayout_11.addLayout(self.layHeaterPIDGraph)

        self.frame_30 = QFrame(self.pageHeaterPIDGraph)
        self.frame_30.setObjectName(u"frame_30")
        sizePolicy3.setHeightForWidth(self.frame_30.sizePolicy().hasHeightForWidth())
        self.frame_30.setSizePolicy(sizePolicy3)
        self.frame_30.setFrameShape(QFrame.NoFrame)
        self.gridLayout_2 = QGridLayout(self.frame_30)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btnHeaterPID_graph_u_sat = QPushButton(self.frame_30)
        self.btnHeaterPID_graph_u_sat.setObjectName(u"btnHeaterPID_graph_u_sat")
        self.btnHeaterPID_graph_u_sat.setCheckable(True)
        self.btnHeaterPID_graph_u_sat.setChecked(False)

        self.gridLayout_2.addWidget(self.btnHeaterPID_graph_u_sat, 0, 8, 1, 1)

        self.btnHeaterPID_graph_x = QPushButton(self.frame_30)
        self.btnHeaterPID_graph_x.setObjectName(u"btnHeaterPID_graph_x")
        self.btnHeaterPID_graph_x.setCheckable(True)
        self.btnHeaterPID_graph_x.setChecked(True)

        self.gridLayout_2.addWidget(self.btnHeaterPID_graph_x, 0, 0, 1, 1)

        self.btnHeaterPID_graph_mode = QPushButton(self.frame_30)
        self.btnHeaterPID_graph_mode.setObjectName(u"btnHeaterPID_graph_mode")
        self.btnHeaterPID_graph_mode.setCheckable(True)
        self.btnHeaterPID_graph_mode.setChecked(False)

        self.gridLayout_2.addWidget(self.btnHeaterPID_graph_mode, 0, 18, 1, 1)

        self.btnHeaterPID_graph_aw_int_e = QPushButton(self.frame_30)
        self.btnHeaterPID_graph_aw_int_e.setObjectName(u"btnHeaterPID_graph_aw_int_e")
        self.btnHeaterPID_graph_aw_int_e.setCheckable(True)
        self.btnHeaterPID_graph_aw_int_e.setChecked(False)

        self.gridLayout_2.addWidget(self.btnHeaterPID_graph_aw_int_e, 0, 6, 1, 1)

        self.btnHeaterPID_graph_u = QPushButton(self.frame_30)
        self.btnHeaterPID_graph_u.setObjectName(u"btnHeaterPID_graph_u")
        self.btnHeaterPID_graph_u.setCheckable(True)
        self.btnHeaterPID_graph_u.setChecked(False)

        self.gridLayout_2.addWidget(self.btnHeaterPID_graph_u, 0, 7, 1, 1)

        self.btnHeaterPID_graph_y_1 = QPushButton(self.frame_30)
        self.btnHeaterPID_graph_y_1.setObjectName(u"btnHeaterPID_graph_y_1")
        self.btnHeaterPID_graph_y_1.setCheckable(True)
        self.btnHeaterPID_graph_y_1.setChecked(True)

        self.gridLayout_2.addWidget(self.btnHeaterPID_graph_y_1, 0, 2, 1, 1)

        self.btnHeaterPID_graph_u_max = QPushButton(self.frame_30)
        self.btnHeaterPID_graph_u_max.setObjectName(u"btnHeaterPID_graph_u_max")
        self.btnHeaterPID_graph_u_max.setCheckable(True)
        self.btnHeaterPID_graph_u_max.setChecked(False)

        self.gridLayout_2.addWidget(self.btnHeaterPID_graph_u_max, 0, 9, 1, 1)

        self.btnHeaterPID_graph_int_e = QPushButton(self.frame_30)
        self.btnHeaterPID_graph_int_e.setObjectName(u"btnHeaterPID_graph_int_e")
        self.btnHeaterPID_graph_int_e.setCheckable(True)
        self.btnHeaterPID_graph_int_e.setChecked(False)

        self.gridLayout_2.addWidget(self.btnHeaterPID_graph_int_e, 0, 5, 1, 1)

        self.btnHeaterPID_graph_u_i = QPushButton(self.frame_30)
        self.btnHeaterPID_graph_u_i.setObjectName(u"btnHeaterPID_graph_u_i")
        self.btnHeaterPID_graph_u_i.setCheckable(True)
        self.btnHeaterPID_graph_u_i.setChecked(False)

        self.gridLayout_2.addWidget(self.btnHeaterPID_graph_u_i, 0, 12, 1, 1)

        self.btnHeaterPID_graph_y_2 = QPushButton(self.frame_30)
        self.btnHeaterPID_graph_y_2.setObjectName(u"btnHeaterPID_graph_y_2")
        self.btnHeaterPID_graph_y_2.setCheckable(True)
        self.btnHeaterPID_graph_y_2.setChecked(True)

        self.gridLayout_2.addWidget(self.btnHeaterPID_graph_y_2, 0, 3, 1, 1)

        self.btnHeaterPID_graph_u_p = QPushButton(self.frame_30)
        self.btnHeaterPID_graph_u_p.setObjectName(u"btnHeaterPID_graph_u_p")
        self.btnHeaterPID_graph_u_p.setCheckable(True)
        self.btnHeaterPID_graph_u_p.setChecked(False)

        self.gridLayout_2.addWidget(self.btnHeaterPID_graph_u_p, 0, 11, 1, 1)

        self.btnHeaterPID_graph_u_min = QPushButton(self.frame_30)
        self.btnHeaterPID_graph_u_min.setObjectName(u"btnHeaterPID_graph_u_min")
        self.btnHeaterPID_graph_u_min.setCheckable(True)
        self.btnHeaterPID_graph_u_min.setChecked(False)

        self.gridLayout_2.addWidget(self.btnHeaterPID_graph_u_min, 0, 10, 1, 1)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_26, 0, 19, 1, 1)

        self.btnHeaterPID_graph_u_d = QPushButton(self.frame_30)
        self.btnHeaterPID_graph_u_d.setObjectName(u"btnHeaterPID_graph_u_d")
        self.btnHeaterPID_graph_u_d.setCheckable(True)
        self.btnHeaterPID_graph_u_d.setChecked(False)

        self.gridLayout_2.addWidget(self.btnHeaterPID_graph_u_d, 0, 17, 1, 1)

        self.btnHeaterPID_graph_e = QPushButton(self.frame_30)
        self.btnHeaterPID_graph_e.setObjectName(u"btnHeaterPID_graph_e")
        self.btnHeaterPID_graph_e.setCheckable(True)
        self.btnHeaterPID_graph_e.setChecked(False)

        self.gridLayout_2.addWidget(self.btnHeaterPID_graph_e, 0, 4, 1, 1)

        self.lcdHeaterPID_x = QLCDNumber(self.frame_30)
        self.lcdHeaterPID_x.setObjectName(u"lcdHeaterPID_x")
        self.lcdHeaterPID_x.setFrameShadow(QFrame.Plain)
        self.lcdHeaterPID_x.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_2.addWidget(self.lcdHeaterPID_x, 1, 0, 1, 1)

        self.lcdHeaterPID_y_1 = QLCDNumber(self.frame_30)
        self.lcdHeaterPID_y_1.setObjectName(u"lcdHeaterPID_y_1")
        self.lcdHeaterPID_y_1.setFrameShadow(QFrame.Plain)
        self.lcdHeaterPID_y_1.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_2.addWidget(self.lcdHeaterPID_y_1, 1, 2, 1, 1)

        self.lcdHeaterPID_y_2 = QLCDNumber(self.frame_30)
        self.lcdHeaterPID_y_2.setObjectName(u"lcdHeaterPID_y_2")
        self.lcdHeaterPID_y_2.setFrameShadow(QFrame.Plain)
        self.lcdHeaterPID_y_2.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_2.addWidget(self.lcdHeaterPID_y_2, 1, 3, 1, 1)

        self.lcdHeaterPID_e = QLCDNumber(self.frame_30)
        self.lcdHeaterPID_e.setObjectName(u"lcdHeaterPID_e")
        self.lcdHeaterPID_e.setFrameShadow(QFrame.Plain)
        self.lcdHeaterPID_e.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_2.addWidget(self.lcdHeaterPID_e, 1, 4, 1, 1)

        self.lcdHeaterPID_int_e = QLCDNumber(self.frame_30)
        self.lcdHeaterPID_int_e.setObjectName(u"lcdHeaterPID_int_e")
        self.lcdHeaterPID_int_e.setFrameShadow(QFrame.Plain)
        self.lcdHeaterPID_int_e.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_2.addWidget(self.lcdHeaterPID_int_e, 1, 5, 1, 1)

        self.lcdHeaterPID_aw_int_e = QLCDNumber(self.frame_30)
        self.lcdHeaterPID_aw_int_e.setObjectName(u"lcdHeaterPID_aw_int_e")
        self.lcdHeaterPID_aw_int_e.setFrameShadow(QFrame.Plain)
        self.lcdHeaterPID_aw_int_e.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_2.addWidget(self.lcdHeaterPID_aw_int_e, 1, 6, 1, 1)

        self.lcdHeaterPID_u = QLCDNumber(self.frame_30)
        self.lcdHeaterPID_u.setObjectName(u"lcdHeaterPID_u")
        self.lcdHeaterPID_u.setFrameShadow(QFrame.Plain)
        self.lcdHeaterPID_u.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_2.addWidget(self.lcdHeaterPID_u, 1, 7, 1, 1)

        self.lcdHeaterPID_u_sat = QLCDNumber(self.frame_30)
        self.lcdHeaterPID_u_sat.setObjectName(u"lcdHeaterPID_u_sat")
        self.lcdHeaterPID_u_sat.setFrameShadow(QFrame.Plain)
        self.lcdHeaterPID_u_sat.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_2.addWidget(self.lcdHeaterPID_u_sat, 1, 8, 1, 1)

        self.lcdHeaterPID_u_max = QLCDNumber(self.frame_30)
        self.lcdHeaterPID_u_max.setObjectName(u"lcdHeaterPID_u_max")
        self.lcdHeaterPID_u_max.setFrameShadow(QFrame.Plain)
        self.lcdHeaterPID_u_max.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_2.addWidget(self.lcdHeaterPID_u_max, 1, 9, 1, 1)

        self.lcdHeaterPID_u_min = QLCDNumber(self.frame_30)
        self.lcdHeaterPID_u_min.setObjectName(u"lcdHeaterPID_u_min")
        self.lcdHeaterPID_u_min.setFrameShadow(QFrame.Plain)
        self.lcdHeaterPID_u_min.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_2.addWidget(self.lcdHeaterPID_u_min, 1, 10, 1, 1)

        self.lcdHeaterPID_u_p = QLCDNumber(self.frame_30)
        self.lcdHeaterPID_u_p.setObjectName(u"lcdHeaterPID_u_p")
        self.lcdHeaterPID_u_p.setFrameShadow(QFrame.Plain)
        self.lcdHeaterPID_u_p.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_2.addWidget(self.lcdHeaterPID_u_p, 1, 11, 1, 1)

        self.lcdHeaterPID_u_i = QLCDNumber(self.frame_30)
        self.lcdHeaterPID_u_i.setObjectName(u"lcdHeaterPID_u_i")
        self.lcdHeaterPID_u_i.setFrameShadow(QFrame.Plain)
        self.lcdHeaterPID_u_i.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_2.addWidget(self.lcdHeaterPID_u_i, 1, 12, 1, 1)

        self.lcdHeaterPID_u_d = QLCDNumber(self.frame_30)
        self.lcdHeaterPID_u_d.setObjectName(u"lcdHeaterPID_u_d")
        self.lcdHeaterPID_u_d.setFrameShadow(QFrame.Plain)
        self.lcdHeaterPID_u_d.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_2.addWidget(self.lcdHeaterPID_u_d, 1, 17, 1, 1)

        self.lcdHeaterPID_mode = QLCDNumber(self.frame_30)
        self.lcdHeaterPID_mode.setObjectName(u"lcdHeaterPID_mode")
        self.lcdHeaterPID_mode.setFrameShadow(QFrame.Plain)
        self.lcdHeaterPID_mode.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_2.addWidget(self.lcdHeaterPID_mode, 1, 18, 1, 1)


        self.verticalLayout_11.addWidget(self.frame_30)

        self.stackGraphs.addWidget(self.pageHeaterPIDGraph)
        self.pageFanBBGraph = QWidget()
        self.pageFanBBGraph.setObjectName(u"pageFanBBGraph")
        sizePolicy6.setHeightForWidth(self.pageFanBBGraph.sizePolicy().hasHeightForWidth())
        self.pageFanBBGraph.setSizePolicy(sizePolicy6)
        self.verticalLayout_4 = QVBoxLayout(self.pageFanBBGraph)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.layFanBBGraph = QHBoxLayout()
        self.layFanBBGraph.setSpacing(0)
        self.layFanBBGraph.setObjectName(u"layFanBBGraph")

        self.verticalLayout_4.addLayout(self.layFanBBGraph)

        self.frame_27 = QFrame(self.pageFanBBGraph)
        self.frame_27.setObjectName(u"frame_27")
        sizePolicy3.setHeightForWidth(self.frame_27.sizePolicy().hasHeightForWidth())
        self.frame_27.setSizePolicy(sizePolicy3)
        self.frame_27.setFrameShape(QFrame.NoFrame)
        self.gridLayout_3 = QGridLayout(self.frame_27)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lcdFanBB_mode = QLCDNumber(self.frame_27)
        self.lcdFanBB_mode.setObjectName(u"lcdFanBB_mode")
        self.lcdFanBB_mode.setFrameShadow(QFrame.Plain)
        self.lcdFanBB_mode.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_3.addWidget(self.lcdFanBB_mode, 1, 9, 1, 1)

        self.btnFanBB_graph_y = QPushButton(self.frame_27)
        self.btnFanBB_graph_y.setObjectName(u"btnFanBB_graph_y")
        self.btnFanBB_graph_y.setCheckable(True)
        self.btnFanBB_graph_y.setChecked(True)

        self.gridLayout_3.addWidget(self.btnFanBB_graph_y, 0, 1, 1, 1)

        self.lcdFanBB_u_min = QLCDNumber(self.frame_27)
        self.lcdFanBB_u_min.setObjectName(u"lcdFanBB_u_min")
        self.lcdFanBB_u_min.setFrameShadow(QFrame.Plain)
        self.lcdFanBB_u_min.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_3.addWidget(self.lcdFanBB_u_min, 1, 7, 1, 1)

        self.lcdFanBB_y = QLCDNumber(self.frame_27)
        self.lcdFanBB_y.setObjectName(u"lcdFanBB_y")
        self.lcdFanBB_y.setFrameShadow(QFrame.Plain)
        self.lcdFanBB_y.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_3.addWidget(self.lcdFanBB_y, 1, 1, 1, 1)

        self.lcdFanBB_u_max = QLCDNumber(self.frame_27)
        self.lcdFanBB_u_max.setObjectName(u"lcdFanBB_u_max")
        self.lcdFanBB_u_max.setFrameShadow(QFrame.Plain)
        self.lcdFanBB_u_max.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_3.addWidget(self.lcdFanBB_u_max, 1, 6, 1, 1)

        self.lcdFanBB_x_min = QLCDNumber(self.frame_27)
        self.lcdFanBB_x_min.setObjectName(u"lcdFanBB_x_min")
        self.lcdFanBB_x_min.setFrameShadow(QFrame.Plain)
        self.lcdFanBB_x_min.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_3.addWidget(self.lcdFanBB_x_min, 1, 5, 1, 1)

        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_25, 0, 10, 1, 1)

        self.lcdFanBB_x_max = QLCDNumber(self.frame_27)
        self.lcdFanBB_x_max.setObjectName(u"lcdFanBB_x_max")
        self.lcdFanBB_x_max.setFrameShadow(QFrame.Plain)
        self.lcdFanBB_x_max.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_3.addWidget(self.lcdFanBB_x_max, 1, 4, 1, 1)

        self.btnFanBB_graph_u_max = QPushButton(self.frame_27)
        self.btnFanBB_graph_u_max.setObjectName(u"btnFanBB_graph_u_max")
        self.btnFanBB_graph_u_max.setCheckable(True)
        self.btnFanBB_graph_u_max.setChecked(False)

        self.gridLayout_3.addWidget(self.btnFanBB_graph_u_max, 0, 6, 1, 1)

        self.btnFanBB_graph_x_max = QPushButton(self.frame_27)
        self.btnFanBB_graph_x_max.setObjectName(u"btnFanBB_graph_x_max")
        self.btnFanBB_graph_x_max.setCheckable(True)
        self.btnFanBB_graph_x_max.setChecked(False)

        self.gridLayout_3.addWidget(self.btnFanBB_graph_x_max, 0, 4, 1, 1)

        self.btnFanBB_graph_x_min = QPushButton(self.frame_27)
        self.btnFanBB_graph_x_min.setObjectName(u"btnFanBB_graph_x_min")
        self.btnFanBB_graph_x_min.setCheckable(True)
        self.btnFanBB_graph_x_min.setChecked(False)

        self.gridLayout_3.addWidget(self.btnFanBB_graph_x_min, 0, 5, 1, 1)

        self.btnFanBB_graph_mode = QPushButton(self.frame_27)
        self.btnFanBB_graph_mode.setObjectName(u"btnFanBB_graph_mode")
        self.btnFanBB_graph_mode.setCheckable(True)
        self.btnFanBB_graph_mode.setChecked(False)

        self.gridLayout_3.addWidget(self.btnFanBB_graph_mode, 0, 9, 1, 1)

        self.btnFanBB_graph_e = QPushButton(self.frame_27)
        self.btnFanBB_graph_e.setObjectName(u"btnFanBB_graph_e")
        self.btnFanBB_graph_e.setCheckable(True)

        self.gridLayout_3.addWidget(self.btnFanBB_graph_e, 0, 2, 1, 1)

        self.lcdFanBB_x = QLCDNumber(self.frame_27)
        self.lcdFanBB_x.setObjectName(u"lcdFanBB_x")
        self.lcdFanBB_x.setFrameShadow(QFrame.Plain)
        self.lcdFanBB_x.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_3.addWidget(self.lcdFanBB_x, 1, 0, 1, 1)

        self.btnFanBB_graph_x = QPushButton(self.frame_27)
        self.btnFanBB_graph_x.setObjectName(u"btnFanBB_graph_x")
        self.btnFanBB_graph_x.setCheckable(True)
        self.btnFanBB_graph_x.setChecked(True)

        self.gridLayout_3.addWidget(self.btnFanBB_graph_x, 0, 0, 1, 1)

        self.btnFanBB_graph_u_min = QPushButton(self.frame_27)
        self.btnFanBB_graph_u_min.setObjectName(u"btnFanBB_graph_u_min")
        self.btnFanBB_graph_u_min.setCheckable(True)
        self.btnFanBB_graph_u_min.setChecked(False)

        self.gridLayout_3.addWidget(self.btnFanBB_graph_u_min, 0, 7, 1, 1)

        self.btnFanBB_graph_u = QPushButton(self.frame_27)
        self.btnFanBB_graph_u.setObjectName(u"btnFanBB_graph_u")
        self.btnFanBB_graph_u.setCheckable(True)

        self.gridLayout_3.addWidget(self.btnFanBB_graph_u, 0, 3, 1, 1)

        self.lcdFanBB_e = QLCDNumber(self.frame_27)
        self.lcdFanBB_e.setObjectName(u"lcdFanBB_e")
        self.lcdFanBB_e.setFrameShadow(QFrame.Plain)
        self.lcdFanBB_e.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_3.addWidget(self.lcdFanBB_e, 1, 2, 1, 1)

        self.lcdFanBB_u = QLCDNumber(self.frame_27)
        self.lcdFanBB_u.setObjectName(u"lcdFanBB_u")
        self.lcdFanBB_u.setFrameShadow(QFrame.Plain)
        self.lcdFanBB_u.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_3.addWidget(self.lcdFanBB_u, 1, 3, 1, 1)


        self.verticalLayout_4.addWidget(self.frame_27)

        self.stackGraphs.addWidget(self.pageFanBBGraph)
        self.pageFanPIDGraph = QWidget()
        self.pageFanPIDGraph.setObjectName(u"pageFanPIDGraph")
        sizePolicy6.setHeightForWidth(self.pageFanPIDGraph.sizePolicy().hasHeightForWidth())
        self.pageFanPIDGraph.setSizePolicy(sizePolicy6)
        self.verticalLayout_8 = QVBoxLayout(self.pageFanPIDGraph)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.layFanPIDGraph = QHBoxLayout()
        self.layFanPIDGraph.setSpacing(0)
        self.layFanPIDGraph.setObjectName(u"layFanPIDGraph")

        self.verticalLayout_8.addLayout(self.layFanPIDGraph)

        self.frame_28 = QFrame(self.pageFanPIDGraph)
        self.frame_28.setObjectName(u"frame_28")
        sizePolicy3.setHeightForWidth(self.frame_28.sizePolicy().hasHeightForWidth())
        self.frame_28.setSizePolicy(sizePolicy3)
        self.frame_28.setFrameShape(QFrame.NoFrame)
        self.gridLayout = QGridLayout(self.frame_28)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.lcdFanPID_int_e = QLCDNumber(self.frame_28)
        self.lcdFanPID_int_e.setObjectName(u"lcdFanPID_int_e")
        self.lcdFanPID_int_e.setFrameShadow(QFrame.Plain)
        self.lcdFanPID_int_e.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout.addWidget(self.lcdFanPID_int_e, 1, 4, 1, 1)

        self.btnFanPID_graph_u_sat = QPushButton(self.frame_28)
        self.btnFanPID_graph_u_sat.setObjectName(u"btnFanPID_graph_u_sat")
        self.btnFanPID_graph_u_sat.setCheckable(True)
        self.btnFanPID_graph_u_sat.setChecked(False)

        self.gridLayout.addWidget(self.btnFanPID_graph_u_sat, 0, 8, 1, 1)

        self.btnFanPID_graph_aw_int_e = QPushButton(self.frame_28)
        self.btnFanPID_graph_aw_int_e.setObjectName(u"btnFanPID_graph_aw_int_e")
        self.btnFanPID_graph_aw_int_e.setCheckable(True)
        self.btnFanPID_graph_aw_int_e.setChecked(False)

        self.gridLayout.addWidget(self.btnFanPID_graph_aw_int_e, 0, 5, 1, 1)

        self.btnFanPID_graph_y = QPushButton(self.frame_28)
        self.btnFanPID_graph_y.setObjectName(u"btnFanPID_graph_y")
        self.btnFanPID_graph_y.setCheckable(True)
        self.btnFanPID_graph_y.setChecked(True)

        self.gridLayout.addWidget(self.btnFanPID_graph_y, 0, 1, 1, 1)

        self.btnFanPID_graph_mode = QPushButton(self.frame_28)
        self.btnFanPID_graph_mode.setObjectName(u"btnFanPID_graph_mode")
        self.btnFanPID_graph_mode.setCheckable(True)
        self.btnFanPID_graph_mode.setChecked(False)

        self.gridLayout.addWidget(self.btnFanPID_graph_mode, 0, 14, 1, 1)

        self.btnFanPID_graph_u_max = QPushButton(self.frame_28)
        self.btnFanPID_graph_u_max.setObjectName(u"btnFanPID_graph_u_max")
        self.btnFanPID_graph_u_max.setCheckable(True)
        self.btnFanPID_graph_u_max.setChecked(False)

        self.gridLayout.addWidget(self.btnFanPID_graph_u_max, 0, 12, 1, 1)

        self.lcdFanPID_x = QLCDNumber(self.frame_28)
        self.lcdFanPID_x.setObjectName(u"lcdFanPID_x")
        self.lcdFanPID_x.setFrameShadow(QFrame.Plain)
        self.lcdFanPID_x.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout.addWidget(self.lcdFanPID_x, 1, 0, 1, 1)

        self.lcdFanPID_aw_int_e = QLCDNumber(self.frame_28)
        self.lcdFanPID_aw_int_e.setObjectName(u"lcdFanPID_aw_int_e")
        self.lcdFanPID_aw_int_e.setFrameShadow(QFrame.Plain)
        self.lcdFanPID_aw_int_e.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout.addWidget(self.lcdFanPID_aw_int_e, 1, 5, 1, 1)

        self.btnFanPID_graph_e = QPushButton(self.frame_28)
        self.btnFanPID_graph_e.setObjectName(u"btnFanPID_graph_e")
        self.btnFanPID_graph_e.setCheckable(True)
        self.btnFanPID_graph_e.setChecked(False)

        self.gridLayout.addWidget(self.btnFanPID_graph_e, 0, 2, 1, 1)

        self.btnFanPID_graph_u_i = QPushButton(self.frame_28)
        self.btnFanPID_graph_u_i.setObjectName(u"btnFanPID_graph_u_i")
        self.btnFanPID_graph_u_i.setCheckable(True)
        self.btnFanPID_graph_u_i.setChecked(False)

        self.gridLayout.addWidget(self.btnFanPID_graph_u_i, 0, 10, 1, 1)

        self.btnFanPID_graph_int_e = QPushButton(self.frame_28)
        self.btnFanPID_graph_int_e.setObjectName(u"btnFanPID_graph_int_e")
        self.btnFanPID_graph_int_e.setCheckable(True)
        self.btnFanPID_graph_int_e.setChecked(False)

        self.gridLayout.addWidget(self.btnFanPID_graph_int_e, 0, 4, 1, 1)

        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_27, 0, 21, 1, 1)

        self.btnFanPID_graph_u_d = QPushButton(self.frame_28)
        self.btnFanPID_graph_u_d.setObjectName(u"btnFanPID_graph_u_d")
        self.btnFanPID_graph_u_d.setCheckable(True)
        self.btnFanPID_graph_u_d.setChecked(False)

        self.gridLayout.addWidget(self.btnFanPID_graph_u_d, 0, 11, 1, 1)

        self.lcdFanPID_y = QLCDNumber(self.frame_28)
        self.lcdFanPID_y.setObjectName(u"lcdFanPID_y")
        self.lcdFanPID_y.setFrameShadow(QFrame.Plain)
        self.lcdFanPID_y.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout.addWidget(self.lcdFanPID_y, 1, 1, 1, 1)

        self.btnFanPID_graph_x = QPushButton(self.frame_28)
        self.btnFanPID_graph_x.setObjectName(u"btnFanPID_graph_x")
        self.btnFanPID_graph_x.setCheckable(True)
        self.btnFanPID_graph_x.setChecked(True)

        self.gridLayout.addWidget(self.btnFanPID_graph_x, 0, 0, 1, 1)

        self.btnFanPID_graph_u_min = QPushButton(self.frame_28)
        self.btnFanPID_graph_u_min.setObjectName(u"btnFanPID_graph_u_min")
        self.btnFanPID_graph_u_min.setCheckable(True)
        self.btnFanPID_graph_u_min.setChecked(False)

        self.gridLayout.addWidget(self.btnFanPID_graph_u_min, 0, 13, 1, 1)

        self.btnFanPID_graph_u_p = QPushButton(self.frame_28)
        self.btnFanPID_graph_u_p.setObjectName(u"btnFanPID_graph_u_p")
        self.btnFanPID_graph_u_p.setCheckable(True)
        self.btnFanPID_graph_u_p.setChecked(False)

        self.gridLayout.addWidget(self.btnFanPID_graph_u_p, 0, 9, 1, 1)

        self.lcdFanPID_e = QLCDNumber(self.frame_28)
        self.lcdFanPID_e.setObjectName(u"lcdFanPID_e")
        self.lcdFanPID_e.setFrameShadow(QFrame.Plain)
        self.lcdFanPID_e.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout.addWidget(self.lcdFanPID_e, 1, 2, 1, 1)

        self.btnFanPID_graph_u = QPushButton(self.frame_28)
        self.btnFanPID_graph_u.setObjectName(u"btnFanPID_graph_u")
        self.btnFanPID_graph_u.setCheckable(True)
        self.btnFanPID_graph_u.setChecked(False)

        self.gridLayout.addWidget(self.btnFanPID_graph_u, 0, 7, 1, 1)

        self.lcdFanPID_u = QLCDNumber(self.frame_28)
        self.lcdFanPID_u.setObjectName(u"lcdFanPID_u")
        self.lcdFanPID_u.setFrameShadow(QFrame.Plain)
        self.lcdFanPID_u.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout.addWidget(self.lcdFanPID_u, 1, 7, 1, 1)

        self.lcdFanPID_u_sat = QLCDNumber(self.frame_28)
        self.lcdFanPID_u_sat.setObjectName(u"lcdFanPID_u_sat")
        self.lcdFanPID_u_sat.setFrameShadow(QFrame.Plain)
        self.lcdFanPID_u_sat.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout.addWidget(self.lcdFanPID_u_sat, 1, 8, 1, 1)

        self.lcdFanPID_u_p = QLCDNumber(self.frame_28)
        self.lcdFanPID_u_p.setObjectName(u"lcdFanPID_u_p")
        self.lcdFanPID_u_p.setFrameShadow(QFrame.Plain)
        self.lcdFanPID_u_p.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout.addWidget(self.lcdFanPID_u_p, 1, 9, 1, 1)

        self.lcdFanPID_u_i = QLCDNumber(self.frame_28)
        self.lcdFanPID_u_i.setObjectName(u"lcdFanPID_u_i")
        self.lcdFanPID_u_i.setFrameShadow(QFrame.Plain)
        self.lcdFanPID_u_i.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout.addWidget(self.lcdFanPID_u_i, 1, 10, 1, 1)

        self.lcdFanPID_u_d = QLCDNumber(self.frame_28)
        self.lcdFanPID_u_d.setObjectName(u"lcdFanPID_u_d")
        self.lcdFanPID_u_d.setFrameShadow(QFrame.Plain)
        self.lcdFanPID_u_d.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout.addWidget(self.lcdFanPID_u_d, 1, 11, 1, 1)

        self.lcdFanPID_u_max = QLCDNumber(self.frame_28)
        self.lcdFanPID_u_max.setObjectName(u"lcdFanPID_u_max")
        self.lcdFanPID_u_max.setFrameShadow(QFrame.Plain)
        self.lcdFanPID_u_max.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout.addWidget(self.lcdFanPID_u_max, 1, 12, 1, 1)

        self.lcdFanPID_u_min = QLCDNumber(self.frame_28)
        self.lcdFanPID_u_min.setObjectName(u"lcdFanPID_u_min")
        self.lcdFanPID_u_min.setFrameShadow(QFrame.Plain)
        self.lcdFanPID_u_min.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout.addWidget(self.lcdFanPID_u_min, 1, 13, 1, 1)

        self.lcdFanPID_mode = QLCDNumber(self.frame_28)
        self.lcdFanPID_mode.setObjectName(u"lcdFanPID_mode")
        self.lcdFanPID_mode.setFrameShadow(QFrame.Plain)
        self.lcdFanPID_mode.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout.addWidget(self.lcdFanPID_mode, 1, 14, 1, 1)


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
        self.frame_31.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.frame_33 = QFrame(self.frame_31)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.NoFrame)
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
        self.chxExHeaterBB.setChecked(True)

        self.verticalLayout_12.addWidget(self.chxExHeaterBB)

        self.line_2 = QFrame(self.frame_33)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_12.addWidget(self.line_2)

        self.frame_35 = QFrame(self.frame_33)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.NoFrame)
        self.gridLayout_6 = QGridLayout(self.frame_35)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.chxExHeaterBB_u_min = QCheckBox(self.frame_35)
        self.chxExHeaterBB_u_min.setObjectName(u"chxExHeaterBB_u_min")
        self.chxExHeaterBB_u_min.setChecked(True)

        self.gridLayout_6.addWidget(self.chxExHeaterBB_u_min, 1, 1, 1, 1)

        self.chxExHeaterBB_x_max = QCheckBox(self.frame_35)
        self.chxExHeaterBB_x_max.setObjectName(u"chxExHeaterBB_x_max")
        self.chxExHeaterBB_x_max.setChecked(True)

        self.gridLayout_6.addWidget(self.chxExHeaterBB_x_max, 1, 0, 1, 1)

        self.chxExHeaterBB_u_max = QCheckBox(self.frame_35)
        self.chxExHeaterBB_u_max.setObjectName(u"chxExHeaterBB_u_max")
        self.chxExHeaterBB_u_max.setChecked(True)

        self.gridLayout_6.addWidget(self.chxExHeaterBB_u_max, 0, 1, 1, 1)

        self.chxExHeaterBB_x_min = QCheckBox(self.frame_35)
        self.chxExHeaterBB_x_min.setObjectName(u"chxExHeaterBB_x_min")
        self.chxExHeaterBB_x_min.setChecked(True)

        self.gridLayout_6.addWidget(self.chxExHeaterBB_x_min, 2, 0, 1, 1)

        self.chxExHeaterBB_y_1 = QCheckBox(self.frame_35)
        self.chxExHeaterBB_y_1.setObjectName(u"chxExHeaterBB_y_1")
        self.chxExHeaterBB_y_1.setChecked(True)

        self.gridLayout_6.addWidget(self.chxExHeaterBB_y_1, 3, 0, 1, 1)

        self.chxExHeaterBB_x = QCheckBox(self.frame_35)
        self.chxExHeaterBB_x.setObjectName(u"chxExHeaterBB_x")
        self.chxExHeaterBB_x.setChecked(True)

        self.gridLayout_6.addWidget(self.chxExHeaterBB_x, 0, 0, 1, 1)

        self.chxExHeaterBB_y_2 = QCheckBox(self.frame_35)
        self.chxExHeaterBB_y_2.setObjectName(u"chxExHeaterBB_y_2")
        self.chxExHeaterBB_y_2.setChecked(True)

        self.gridLayout_6.addWidget(self.chxExHeaterBB_y_2, 4, 0, 1, 1)

        self.chxExHeaterBB_mode = QCheckBox(self.frame_35)
        self.chxExHeaterBB_mode.setObjectName(u"chxExHeaterBB_mode")
        self.chxExHeaterBB_mode.setChecked(True)

        self.gridLayout_6.addWidget(self.chxExHeaterBB_mode, 4, 1, 1, 1)


        self.verticalLayout_12.addWidget(self.frame_35)

        self.chxExHeaterPID = QCheckBox(self.frame_33)
        self.chxExHeaterPID.setObjectName(u"chxExHeaterPID")
        self.chxExHeaterPID.setFont(font4)
        self.chxExHeaterPID.setChecked(True)

        self.verticalLayout_12.addWidget(self.chxExHeaterPID)

        self.line_3 = QFrame(self.frame_33)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_12.addWidget(self.line_3)

        self.frame_36 = QFrame(self.frame_33)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFrameShape(QFrame.NoFrame)
        self.gridLayout_7 = QGridLayout(self.frame_36)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.chxExHeaterPID_aw_int_e = QCheckBox(self.frame_36)
        self.chxExHeaterPID_aw_int_e.setObjectName(u"chxExHeaterPID_aw_int_e")
        self.chxExHeaterPID_aw_int_e.setChecked(True)

        self.gridLayout_7.addWidget(self.chxExHeaterPID_aw_int_e, 3, 0, 1, 1)

        self.chxExHeaterPID_k_i = QCheckBox(self.frame_36)
        self.chxExHeaterPID_k_i.setObjectName(u"chxExHeaterPID_k_i")
        self.chxExHeaterPID_k_i.setChecked(True)

        self.gridLayout_7.addWidget(self.chxExHeaterPID_k_i, 5, 0, 1, 1)

        self.chxExHeaterPID_x = QCheckBox(self.frame_36)
        self.chxExHeaterPID_x.setObjectName(u"chxExHeaterPID_x")
        self.chxExHeaterPID_x.setChecked(True)

        self.gridLayout_7.addWidget(self.chxExHeaterPID_x, 0, 0, 1, 1)

        self.chxExHeaterPID_mode = QCheckBox(self.frame_36)
        self.chxExHeaterPID_mode.setObjectName(u"chxExHeaterPID_mode")
        self.chxExHeaterPID_mode.setChecked(True)

        self.gridLayout_7.addWidget(self.chxExHeaterPID_mode, 8, 0, 1, 1)

        self.chxExHeaterPID_k_d = QCheckBox(self.frame_36)
        self.chxExHeaterPID_k_d.setObjectName(u"chxExHeaterPID_k_d")
        self.chxExHeaterPID_k_d.setChecked(True)

        self.gridLayout_7.addWidget(self.chxExHeaterPID_k_d, 6, 0, 1, 1)

        self.chxExHeaterPID_int_e = QCheckBox(self.frame_36)
        self.chxExHeaterPID_int_e.setObjectName(u"chxExHeaterPID_int_e")
        self.chxExHeaterPID_int_e.setChecked(True)

        self.gridLayout_7.addWidget(self.chxExHeaterPID_int_e, 2, 0, 1, 1)

        self.chxExHeaterPID_e = QCheckBox(self.frame_36)
        self.chxExHeaterPID_e.setObjectName(u"chxExHeaterPID_e")
        self.chxExHeaterPID_e.setChecked(True)

        self.gridLayout_7.addWidget(self.chxExHeaterPID_e, 1, 0, 1, 1)

        self.chxExHeaterPID_k_aw = QCheckBox(self.frame_36)
        self.chxExHeaterPID_k_aw.setObjectName(u"chxExHeaterPID_k_aw")
        self.chxExHeaterPID_k_aw.setChecked(True)

        self.gridLayout_7.addWidget(self.chxExHeaterPID_k_aw, 7, 0, 1, 1)

        self.chxExHeaterPID_k_p = QCheckBox(self.frame_36)
        self.chxExHeaterPID_k_p.setObjectName(u"chxExHeaterPID_k_p")
        self.chxExHeaterPID_k_p.setChecked(True)

        self.gridLayout_7.addWidget(self.chxExHeaterPID_k_p, 4, 0, 1, 1)

        self.chxExHeaterPID_u_p = QCheckBox(self.frame_36)
        self.chxExHeaterPID_u_p.setObjectName(u"chxExHeaterPID_u_p")
        self.chxExHeaterPID_u_p.setChecked(True)

        self.gridLayout_7.addWidget(self.chxExHeaterPID_u_p, 2, 1, 1, 1)

        self.chxExHeaterPID_u_i = QCheckBox(self.frame_36)
        self.chxExHeaterPID_u_i.setObjectName(u"chxExHeaterPID_u_i")
        self.chxExHeaterPID_u_i.setChecked(True)

        self.gridLayout_7.addWidget(self.chxExHeaterPID_u_i, 3, 1, 1, 1)

        self.chxExHeaterPID_u_sat = QCheckBox(self.frame_36)
        self.chxExHeaterPID_u_sat.setObjectName(u"chxExHeaterPID_u_sat")
        self.chxExHeaterPID_u_sat.setChecked(True)

        self.gridLayout_7.addWidget(self.chxExHeaterPID_u_sat, 1, 1, 1, 1)

        self.chxExHeaterPID_u = QCheckBox(self.frame_36)
        self.chxExHeaterPID_u.setObjectName(u"chxExHeaterPID_u")
        self.chxExHeaterPID_u.setChecked(True)

        self.gridLayout_7.addWidget(self.chxExHeaterPID_u, 0, 1, 1, 1)

        self.chxExHeaterPID_u_d = QCheckBox(self.frame_36)
        self.chxExHeaterPID_u_d.setObjectName(u"chxExHeaterPID_u_d")
        self.chxExHeaterPID_u_d.setChecked(True)

        self.gridLayout_7.addWidget(self.chxExHeaterPID_u_d, 4, 1, 1, 1)

        self.chxExHeaterPID_u_max = QCheckBox(self.frame_36)
        self.chxExHeaterPID_u_max.setObjectName(u"chxExHeaterPID_u_max")
        self.chxExHeaterPID_u_max.setChecked(True)

        self.gridLayout_7.addWidget(self.chxExHeaterPID_u_max, 5, 1, 1, 1)

        self.chxExHeaterPID_u_min = QCheckBox(self.frame_36)
        self.chxExHeaterPID_u_min.setObjectName(u"chxExHeaterPID_u_min")
        self.chxExHeaterPID_u_min.setChecked(True)

        self.gridLayout_7.addWidget(self.chxExHeaterPID_u_min, 6, 1, 1, 1)

        self.chxExHeaterPID_y_1 = QCheckBox(self.frame_36)
        self.chxExHeaterPID_y_1.setObjectName(u"chxExHeaterPID_y_1")
        self.chxExHeaterPID_y_1.setChecked(True)

        self.gridLayout_7.addWidget(self.chxExHeaterPID_y_1, 7, 1, 1, 1)

        self.chxExHeaterPID_y_2 = QCheckBox(self.frame_36)
        self.chxExHeaterPID_y_2.setObjectName(u"chxExHeaterPID_y_2")
        self.chxExHeaterPID_y_2.setChecked(True)

        self.gridLayout_7.addWidget(self.chxExHeaterPID_y_2, 8, 1, 1, 1)


        self.verticalLayout_12.addWidget(self.frame_36)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer)


        self.horizontalLayout_32.addWidget(self.frame_33)

        self.frame_34 = QFrame(self.frame_31)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_13 = QVBoxLayout(self.frame_34)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_46 = QLabel(self.frame_34)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setFont(font3)

        self.verticalLayout_13.addWidget(self.label_46)

        self.chxExFanBB = QCheckBox(self.frame_34)
        self.chxExFanBB.setObjectName(u"chxExFanBB")
        self.chxExFanBB.setFont(font4)
        self.chxExFanBB.setChecked(True)

        self.verticalLayout_13.addWidget(self.chxExFanBB)

        self.line_4 = QFrame(self.frame_34)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_13.addWidget(self.line_4)

        self.frame_37 = QFrame(self.frame_34)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.NoFrame)
        self.gridLayout_8 = QGridLayout(self.frame_37)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.chxExFanBB_mode = QCheckBox(self.frame_37)
        self.chxExFanBB_mode.setObjectName(u"chxExFanBB_mode")
        self.chxExFanBB_mode.setChecked(True)

        self.gridLayout_8.addWidget(self.chxExFanBB_mode, 3, 1, 1, 1)

        self.chxExFanBB_x_max = QCheckBox(self.frame_37)
        self.chxExFanBB_x_max.setObjectName(u"chxExFanBB_x_max")
        self.chxExFanBB_x_max.setChecked(True)

        self.gridLayout_8.addWidget(self.chxExFanBB_x_max, 1, 0, 1, 1)

        self.chxExFanBB_u_min = QCheckBox(self.frame_37)
        self.chxExFanBB_u_min.setObjectName(u"chxExFanBB_u_min")
        self.chxExFanBB_u_min.setChecked(True)

        self.gridLayout_8.addWidget(self.chxExFanBB_u_min, 1, 1, 1, 1)

        self.chxExFanBB_x = QCheckBox(self.frame_37)
        self.chxExFanBB_x.setObjectName(u"chxExFanBB_x")
        self.chxExFanBB_x.setChecked(True)

        self.gridLayout_8.addWidget(self.chxExFanBB_x, 0, 0, 1, 1)

        self.chxExFanBB_y = QCheckBox(self.frame_37)
        self.chxExFanBB_y.setObjectName(u"chxExFanBB_y")
        self.chxExFanBB_y.setChecked(True)

        self.gridLayout_8.addWidget(self.chxExFanBB_y, 3, 0, 1, 1)

        self.chxExFanBB_x_min = QCheckBox(self.frame_37)
        self.chxExFanBB_x_min.setObjectName(u"chxExFanBB_x_min")
        self.chxExFanBB_x_min.setChecked(True)

        self.gridLayout_8.addWidget(self.chxExFanBB_x_min, 2, 0, 1, 1)

        self.chxExFanBB_u_max = QCheckBox(self.frame_37)
        self.chxExFanBB_u_max.setObjectName(u"chxExFanBB_u_max")
        self.chxExFanBB_u_max.setChecked(True)

        self.gridLayout_8.addWidget(self.chxExFanBB_u_max, 0, 1, 1, 1)


        self.verticalLayout_13.addWidget(self.frame_37)

        self.chxExFanPID = QCheckBox(self.frame_34)
        self.chxExFanPID.setObjectName(u"chxExFanPID")
        self.chxExFanPID.setFont(font4)
        self.chxExFanPID.setChecked(True)

        self.verticalLayout_13.addWidget(self.chxExFanPID)

        self.line_5 = QFrame(self.frame_34)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.Shape.VLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_13.addWidget(self.line_5)

        self.frame_38 = QFrame(self.frame_34)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setFrameShape(QFrame.NoFrame)
        self.gridLayout_9 = QGridLayout(self.frame_38)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.chxExFanPID_x = QCheckBox(self.frame_38)
        self.chxExFanPID_x.setObjectName(u"chxExFanPID_x")
        self.chxExFanPID_x.setChecked(True)

        self.gridLayout_9.addWidget(self.chxExFanPID_x, 0, 0, 1, 1)

        self.chxExFanPID_u = QCheckBox(self.frame_38)
        self.chxExFanPID_u.setObjectName(u"chxExFanPID_u")
        self.chxExFanPID_u.setChecked(True)

        self.gridLayout_9.addWidget(self.chxExFanPID_u, 0, 1, 1, 1)

        self.chxExFanPID_e = QCheckBox(self.frame_38)
        self.chxExFanPID_e.setObjectName(u"chxExFanPID_e")
        self.chxExFanPID_e.setChecked(True)

        self.gridLayout_9.addWidget(self.chxExFanPID_e, 1, 0, 1, 1)

        self.chxExFanPID_u_sat = QCheckBox(self.frame_38)
        self.chxExFanPID_u_sat.setObjectName(u"chxExFanPID_u_sat")
        self.chxExFanPID_u_sat.setChecked(True)

        self.gridLayout_9.addWidget(self.chxExFanPID_u_sat, 1, 1, 1, 1)

        self.chxExFanPID_int_e = QCheckBox(self.frame_38)
        self.chxExFanPID_int_e.setObjectName(u"chxExFanPID_int_e")
        self.chxExFanPID_int_e.setChecked(True)

        self.gridLayout_9.addWidget(self.chxExFanPID_int_e, 2, 0, 1, 1)

        self.chxExFanPID_u_p = QCheckBox(self.frame_38)
        self.chxExFanPID_u_p.setObjectName(u"chxExFanPID_u_p")
        self.chxExFanPID_u_p.setChecked(True)

        self.gridLayout_9.addWidget(self.chxExFanPID_u_p, 2, 1, 1, 1)

        self.chxExFanPID_aw_int_e = QCheckBox(self.frame_38)
        self.chxExFanPID_aw_int_e.setObjectName(u"chxExFanPID_aw_int_e")
        self.chxExFanPID_aw_int_e.setChecked(True)

        self.gridLayout_9.addWidget(self.chxExFanPID_aw_int_e, 3, 0, 1, 1)

        self.chxExFanPID_u_i = QCheckBox(self.frame_38)
        self.chxExFanPID_u_i.setObjectName(u"chxExFanPID_u_i")
        self.chxExFanPID_u_i.setChecked(True)

        self.gridLayout_9.addWidget(self.chxExFanPID_u_i, 3, 1, 1, 1)

        self.chxExFanPID_k_p = QCheckBox(self.frame_38)
        self.chxExFanPID_k_p.setObjectName(u"chxExFanPID_k_p")
        self.chxExFanPID_k_p.setChecked(True)

        self.gridLayout_9.addWidget(self.chxExFanPID_k_p, 4, 0, 1, 1)

        self.chxExFanPID_u_d = QCheckBox(self.frame_38)
        self.chxExFanPID_u_d.setObjectName(u"chxExFanPID_u_d")
        self.chxExFanPID_u_d.setChecked(True)

        self.gridLayout_9.addWidget(self.chxExFanPID_u_d, 4, 1, 1, 1)

        self.chxExFanPID_k_i = QCheckBox(self.frame_38)
        self.chxExFanPID_k_i.setObjectName(u"chxExFanPID_k_i")
        self.chxExFanPID_k_i.setChecked(True)

        self.gridLayout_9.addWidget(self.chxExFanPID_k_i, 5, 0, 1, 1)

        self.chxExFanPID_u_max = QCheckBox(self.frame_38)
        self.chxExFanPID_u_max.setObjectName(u"chxExFanPID_u_max")
        self.chxExFanPID_u_max.setChecked(True)

        self.gridLayout_9.addWidget(self.chxExFanPID_u_max, 5, 1, 1, 1)

        self.chxExFanPID_k_d = QCheckBox(self.frame_38)
        self.chxExFanPID_k_d.setObjectName(u"chxExFanPID_k_d")
        self.chxExFanPID_k_d.setChecked(True)

        self.gridLayout_9.addWidget(self.chxExFanPID_k_d, 6, 0, 1, 1)

        self.chxExFanPID_u_min = QCheckBox(self.frame_38)
        self.chxExFanPID_u_min.setObjectName(u"chxExFanPID_u_min")
        self.chxExFanPID_u_min.setChecked(True)

        self.gridLayout_9.addWidget(self.chxExFanPID_u_min, 6, 1, 1, 1)

        self.chxExFanPID_k_aw = QCheckBox(self.frame_38)
        self.chxExFanPID_k_aw.setObjectName(u"chxExFanPID_k_aw")
        self.chxExFanPID_k_aw.setChecked(True)

        self.gridLayout_9.addWidget(self.chxExFanPID_k_aw, 7, 0, 1, 1)

        self.chxExFanPID_y = QCheckBox(self.frame_38)
        self.chxExFanPID_y.setObjectName(u"chxExFanPID_y")
        self.chxExFanPID_y.setChecked(True)

        self.gridLayout_9.addWidget(self.chxExFanPID_y, 7, 1, 1, 1)

        self.chxExFanPID_mode = QCheckBox(self.frame_38)
        self.chxExFanPID_mode.setObjectName(u"chxExFanPID_mode")
        self.chxExFanPID_mode.setChecked(True)

        self.gridLayout_9.addWidget(self.chxExFanPID_mode, 8, 0, 1, 1)


        self.verticalLayout_13.addWidget(self.frame_38)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_2)


        self.horizontalLayout_32.addWidget(self.frame_34)


        self.verticalLayout_10.addWidget(self.frame_31)

        self.frame_32 = QFrame(self.Export)
        self.frame_32.setObjectName(u"frame_32")
        sizePolicy2.setHeightForWidth(self.frame_32.sizePolicy().hasHeightForWidth())
        self.frame_32.setSizePolicy(sizePolicy2)
        self.frame_32.setFrameShape(QFrame.NoFrame)
        self.gridLayout_5 = QGridLayout(self.frame_32)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_3, 1, 0, 1, 1)

        self.btnExportAction = QPushButton(self.frame_32)
        self.btnExportAction.setObjectName(u"btnExportAction")
        self.btnExportAction.setMaximumSize(QSize(150, 16777215))
        self.btnExportAction.setIcon(icon7)

        self.gridLayout_5.addWidget(self.btnExportAction, 0, 0, 1, 1)

        self.horizontalSpacer_29 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_29, 0, 1, 1, 1)


        self.verticalLayout_10.addWidget(self.frame_32)

        self.container.addWidget(self.Export)
        self.Help = QWidget()
        self.Help.setObjectName(u"Help")
        self.verticalLayout_14 = QVBoxLayout(self.Help)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_37 = QLabel(self.Help)
        self.label_37.setObjectName(u"label_37")

        self.verticalLayout_14.addWidget(self.label_37)

        self.line_6 = QFrame(self.Help)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.Shape.VLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_14.addWidget(self.line_6)

        self.label_8 = QLabel(self.Help)
        self.label_8.setObjectName(u"label_8")
        font5 = QFont()
        font5.setItalic(True)
        self.label_8.setFont(font5)

        self.verticalLayout_14.addWidget(self.label_8)

        self.label_47 = QLabel(self.Help)
        self.label_47.setObjectName(u"label_47")
        font6 = QFont()
        font6.setPointSize(10)
        font6.setItalic(False)
        self.label_47.setFont(font6)

        self.verticalLayout_14.addWidget(self.label_47)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_4)

        self.container.addWidget(self.Help)
        self.Import = QWidget()
        self.Import.setObjectName(u"Import")
        self.verticalLayout_15 = QVBoxLayout(self.Import)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.frame_40 = QFrame(self.Import)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_40)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.btnImportLoad = QPushButton(self.frame_40)
        self.btnImportLoad.setObjectName(u"btnImportLoad")
        self.btnImportLoad.setIcon(icon8)

        self.horizontalLayout_34.addWidget(self.btnImportLoad)

        self.horizontalSpacer_31 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_34.addItem(self.horizontalSpacer_31)


        self.verticalLayout_15.addWidget(self.frame_40)

        self.frame_39 = QFrame(self.Import)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_39)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.label_48 = QLabel(self.frame_39)
        self.label_48.setObjectName(u"label_48")

        self.horizontalLayout_33.addWidget(self.label_48)

        self.cmbImportIdx = QComboBox(self.frame_39)
        self.cmbImportIdx.setObjectName(u"cmbImportIdx")
        self.cmbImportIdx.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_33.addWidget(self.cmbImportIdx)

        self.btnImportAction = QPushButton(self.frame_39)
        self.btnImportAction.setObjectName(u"btnImportAction")
        self.btnImportAction.setEnabled(False)

        self.horizontalLayout_33.addWidget(self.btnImportAction)

        self.horizontalSpacer_30 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_33.addItem(self.horizontalSpacer_30)


        self.verticalLayout_15.addWidget(self.frame_39)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_5)

        self.container.addWidget(self.Import)
        self.Graphs = QWidget()
        self.Graphs.setObjectName(u"Graphs")
        self.verticalLayout_16 = QVBoxLayout(self.Graphs)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.frame_41 = QFrame(self.Graphs)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_38 = QHBoxLayout(self.frame_41)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.btnGraphsPageHeater = QPushButton(self.frame_41)
        self.btnGraphsPageHeater.setObjectName(u"btnGraphsPageHeater")
        self.btnGraphsPageHeater.setIcon(icon2)
        self.btnGraphsPageHeater.setCheckable(True)
        self.btnGraphsPageHeater.setChecked(True)

        self.horizontalLayout_38.addWidget(self.btnGraphsPageHeater)

        self.line_7 = QFrame(self.frame_41)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.Shape.VLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_38.addWidget(self.line_7)

        self.btnGraphsPageFan = QPushButton(self.frame_41)
        self.btnGraphsPageFan.setObjectName(u"btnGraphsPageFan")
        self.btnGraphsPageFan.setIcon(icon3)
        self.btnGraphsPageFan.setCheckable(True)

        self.horizontalLayout_38.addWidget(self.btnGraphsPageFan)

        self.horizontalSpacer_28 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_38.addItem(self.horizontalSpacer_28)

        self.btnGraphsPage_x = QPushButton(self.frame_41)
        self.btnGraphsPage_x.setObjectName(u"btnGraphsPage_x")
        self.btnGraphsPage_x.setCheckable(True)
        self.btnGraphsPage_x.setChecked(True)

        self.horizontalLayout_38.addWidget(self.btnGraphsPage_x)

        self.btnGraphsPage_y_1 = QPushButton(self.frame_41)
        self.btnGraphsPage_y_1.setObjectName(u"btnGraphsPage_y_1")
        self.btnGraphsPage_y_1.setCheckable(True)
        self.btnGraphsPage_y_1.setChecked(True)

        self.horizontalLayout_38.addWidget(self.btnGraphsPage_y_1)

        self.btnGraphsPage_y_2 = QPushButton(self.frame_41)
        self.btnGraphsPage_y_2.setObjectName(u"btnGraphsPage_y_2")
        self.btnGraphsPage_y_2.setCheckable(True)
        self.btnGraphsPage_y_2.setChecked(True)

        self.horizontalLayout_38.addWidget(self.btnGraphsPage_y_2)

        self.btnGraphsPage_y = QPushButton(self.frame_41)
        self.btnGraphsPage_y.setObjectName(u"btnGraphsPage_y")
        self.btnGraphsPage_y.setEnabled(True)
        self.btnGraphsPage_y.setCheckable(True)
        self.btnGraphsPage_y.setChecked(True)

        self.horizontalLayout_38.addWidget(self.btnGraphsPage_y)

        self.line_9 = QFrame(self.frame_41)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.Shape.VLine)
        self.line_9.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_38.addWidget(self.line_9)

        self.btnGraphsPage_u_p = QPushButton(self.frame_41)
        self.btnGraphsPage_u_p.setObjectName(u"btnGraphsPage_u_p")
        self.btnGraphsPage_u_p.setCheckable(True)
        self.btnGraphsPage_u_p.setChecked(True)

        self.horizontalLayout_38.addWidget(self.btnGraphsPage_u_p)

        self.btnGraphsPage_u_i = QPushButton(self.frame_41)
        self.btnGraphsPage_u_i.setObjectName(u"btnGraphsPage_u_i")
        self.btnGraphsPage_u_i.setCheckable(True)
        self.btnGraphsPage_u_i.setChecked(True)

        self.horizontalLayout_38.addWidget(self.btnGraphsPage_u_i)

        self.btnGraphsPage_u_d = QPushButton(self.frame_41)
        self.btnGraphsPage_u_d.setObjectName(u"btnGraphsPage_u_d")
        self.btnGraphsPage_u_d.setCheckable(True)
        self.btnGraphsPage_u_d.setChecked(True)

        self.horizontalLayout_38.addWidget(self.btnGraphsPage_u_d)

        self.line_10 = QFrame(self.frame_41)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.Shape.VLine)
        self.line_10.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_38.addWidget(self.line_10)

        self.btnGraphsPage_u = QPushButton(self.frame_41)
        self.btnGraphsPage_u.setObjectName(u"btnGraphsPage_u")
        self.btnGraphsPage_u.setCheckable(True)
        self.btnGraphsPage_u.setChecked(True)

        self.horizontalLayout_38.addWidget(self.btnGraphsPage_u)

        self.btnGraphsPage_u_sat = QPushButton(self.frame_41)
        self.btnGraphsPage_u_sat.setObjectName(u"btnGraphsPage_u_sat")
        self.btnGraphsPage_u_sat.setCheckable(True)
        self.btnGraphsPage_u_sat.setChecked(True)

        self.horizontalLayout_38.addWidget(self.btnGraphsPage_u_sat)


        self.verticalLayout_16.addWidget(self.frame_41)

        self.stackGraphsPage = QStackedWidget(self.Graphs)
        self.stackGraphsPage.setObjectName(u"stackGraphsPage")
        self.pageGraphsPageHeater = QWidget()
        self.pageGraphsPageHeater.setObjectName(u"pageGraphsPageHeater")
        self.verticalLayout_26 = QVBoxLayout(self.pageGraphsPageHeater)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.frame_44 = QFrame(self.pageGraphsPageHeater)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setFrameShape(QFrame.NoFrame)
        self.frame_44.setLineWidth(0)
        self.horizontalLayout_37 = QHBoxLayout(self.frame_44)
        self.horizontalLayout_37.setSpacing(0)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.frame_45 = QFrame(self.frame_44)
        self.frame_45.setObjectName(u"frame_45")
        sizePolicy6.setHeightForWidth(self.frame_45.sizePolicy().hasHeightForWidth())
        self.frame_45.setSizePolicy(sizePolicy6)
        self.frame_45.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_23 = QVBoxLayout(self.frame_45)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.layGraphsPageHeater_y = QHBoxLayout()
        self.layGraphsPageHeater_y.setObjectName(u"layGraphsPageHeater_y")

        self.verticalLayout_23.addLayout(self.layGraphsPageHeater_y)


        self.horizontalLayout_37.addWidget(self.frame_45)


        self.verticalLayout_26.addWidget(self.frame_44)

        self.frame_43 = QFrame(self.pageGraphsPageHeater)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setFrameShape(QFrame.NoFrame)
        self.frame_43.setLineWidth(0)
        self.horizontalLayout_35 = QHBoxLayout(self.frame_43)
        self.horizontalLayout_35.setSpacing(0)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.frame_49 = QFrame(self.frame_43)
        self.frame_49.setObjectName(u"frame_49")
        sizePolicy6.setHeightForWidth(self.frame_49.sizePolicy().hasHeightForWidth())
        self.frame_49.setSizePolicy(sizePolicy6)
        self.frame_49.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_25 = QVBoxLayout(self.frame_49)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.layGraphsPageHeater_e = QHBoxLayout()
        self.layGraphsPageHeater_e.setObjectName(u"layGraphsPageHeater_e")

        self.verticalLayout_25.addLayout(self.layGraphsPageHeater_e)


        self.horizontalLayout_35.addWidget(self.frame_49)


        self.verticalLayout_26.addWidget(self.frame_43)

        self.frame_42 = QFrame(self.pageGraphsPageHeater)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setFrameShape(QFrame.NoFrame)
        self.frame_42.setLineWidth(0)
        self.horizontalLayout_36 = QHBoxLayout(self.frame_42)
        self.horizontalLayout_36.setSpacing(0)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.frame_47 = QFrame(self.frame_42)
        self.frame_47.setObjectName(u"frame_47")
        sizePolicy6.setHeightForWidth(self.frame_47.sizePolicy().hasHeightForWidth())
        self.frame_47.setSizePolicy(sizePolicy6)
        self.frame_47.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_24 = QVBoxLayout(self.frame_47)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.layGraphsPageHeater_u = QHBoxLayout()
        self.layGraphsPageHeater_u.setObjectName(u"layGraphsPageHeater_u")

        self.verticalLayout_24.addLayout(self.layGraphsPageHeater_u)


        self.horizontalLayout_36.addWidget(self.frame_47)


        self.verticalLayout_26.addWidget(self.frame_42)

        self.stackGraphsPage.addWidget(self.pageGraphsPageHeater)
        self.pageGraphsPageFan = QWidget()
        self.pageGraphsPageFan.setObjectName(u"pageGraphsPageFan")
        self.verticalLayout_22 = QVBoxLayout(self.pageGraphsPageFan)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.frame_50 = QFrame(self.pageGraphsPageFan)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setFrameShape(QFrame.NoFrame)
        self.frame_50.setFrameShadow(QFrame.Plain)
        self.frame_50.setLineWidth(0)
        self.horizontalLayout_39 = QHBoxLayout(self.frame_50)
        self.horizontalLayout_39.setSpacing(0)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.frame_55 = QFrame(self.frame_50)
        self.frame_55.setObjectName(u"frame_55")
        sizePolicy6.setHeightForWidth(self.frame_55.sizePolicy().hasHeightForWidth())
        self.frame_55.setSizePolicy(sizePolicy6)
        self.frame_55.setFrameShape(QFrame.NoFrame)
        self.frame_55.setFrameShadow(QFrame.Plain)
        self.verticalLayout_27 = QVBoxLayout(self.frame_55)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.layGraphsPageFan_y = QHBoxLayout()
        self.layGraphsPageFan_y.setObjectName(u"layGraphsPageFan_y")

        self.verticalLayout_27.addLayout(self.layGraphsPageFan_y)


        self.horizontalLayout_39.addWidget(self.frame_55)


        self.verticalLayout_22.addWidget(self.frame_50)

        self.frame_51 = QFrame(self.pageGraphsPageFan)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setFrameShape(QFrame.NoFrame)
        self.frame_51.setFrameShadow(QFrame.Plain)
        self.frame_51.setLineWidth(0)
        self.horizontalLayout_40 = QHBoxLayout(self.frame_51)
        self.horizontalLayout_40.setSpacing(0)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.frame_54 = QFrame(self.frame_51)
        self.frame_54.setObjectName(u"frame_54")
        sizePolicy6.setHeightForWidth(self.frame_54.sizePolicy().hasHeightForWidth())
        self.frame_54.setSizePolicy(sizePolicy6)
        self.frame_54.setFrameShape(QFrame.NoFrame)
        self.frame_54.setFrameShadow(QFrame.Plain)
        self.verticalLayout_28 = QVBoxLayout(self.frame_54)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.layGraphsPageFan_e = QHBoxLayout()
        self.layGraphsPageFan_e.setObjectName(u"layGraphsPageFan_e")

        self.verticalLayout_28.addLayout(self.layGraphsPageFan_e)


        self.horizontalLayout_40.addWidget(self.frame_54)


        self.verticalLayout_22.addWidget(self.frame_51)

        self.frame_52 = QFrame(self.pageGraphsPageFan)
        self.frame_52.setObjectName(u"frame_52")
        sizePolicy5.setHeightForWidth(self.frame_52.sizePolicy().hasHeightForWidth())
        self.frame_52.setSizePolicy(sizePolicy5)
        self.frame_52.setFrameShape(QFrame.NoFrame)
        self.frame_52.setFrameShadow(QFrame.Plain)
        self.frame_52.setLineWidth(0)
        self.horizontalLayout_41 = QHBoxLayout(self.frame_52)
        self.horizontalLayout_41.setSpacing(0)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.frame_53 = QFrame(self.frame_52)
        self.frame_53.setObjectName(u"frame_53")
        sizePolicy6.setHeightForWidth(self.frame_53.sizePolicy().hasHeightForWidth())
        self.frame_53.setSizePolicy(sizePolicy6)
        self.frame_53.setFrameShape(QFrame.NoFrame)
        self.frame_53.setFrameShadow(QFrame.Plain)
        self.verticalLayout_29 = QVBoxLayout(self.frame_53)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.layGraphsPageFan_u = QHBoxLayout()
        self.layGraphsPageFan_u.setObjectName(u"layGraphsPageFan_u")

        self.verticalLayout_29.addLayout(self.layGraphsPageFan_u)


        self.horizontalLayout_41.addWidget(self.frame_53)


        self.verticalLayout_22.addWidget(self.frame_52)

        self.stackGraphsPage.addWidget(self.pageGraphsPageFan)

        self.verticalLayout_16.addWidget(self.stackGraphsPage)

        self.container.addWidget(self.Graphs)

        self.verticalLayout_2.addWidget(self.container)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.container.setCurrentIndex(0)
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
        self.btnGraphs.setText(QCoreApplication.translate("MainWindow", u"Wykresy", None))
#if QT_CONFIG(tooltip)
        self.btn_graph_Stop.setToolTip(QCoreApplication.translate("MainWindow", u"Zatrzymaj wykres", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btn_graph_Stop.setStatusTip(QCoreApplication.translate("MainWindow", u"Zatrzymaj wykres", None))
#endif // QT_CONFIG(statustip)
        self.btn_graph_Stop.setText("")
#if QT_CONFIG(tooltip)
        self.btn_graph_Clear.setToolTip(QCoreApplication.translate("MainWindow", u"Wyczy\u015b\u0107 wykres", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btn_graph_Clear.setStatusTip(QCoreApplication.translate("MainWindow", u"Wyczy\u015b\u0107 wykres", None))
#endif // QT_CONFIG(statustip)
        self.btn_graph_Clear.setText("")
#if QT_CONFIG(tooltip)
        self.btnDataExport.setToolTip(QCoreApplication.translate("MainWindow", u"Eksportuj dane do pliku .xlsx", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btnDataExport.setStatusTip(QCoreApplication.translate("MainWindow", u"Eksportuj dane do pliku .xlsx", None))
#endif // QT_CONFIG(statustip)
        self.btnDataExport.setText(QCoreApplication.translate("MainWindow", u"Eksport danych", None))
        self.btnImport.setText(QCoreApplication.translate("MainWindow", u"Importuj nastawy", None))
#if QT_CONFIG(tooltip)
        self.btnHelp.setToolTip(QCoreApplication.translate("MainWindow", u"Dowiedz si\u0119 jak korzysta\u0107 z programu", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btnHelp.setStatusTip(QCoreApplication.translate("MainWindow", u"Dowiedz si\u0119 jak korzysta\u0107 z programu", None))
#endif // QT_CONFIG(statustip)
        self.btnHelp.setText(QCoreApplication.translate("MainWindow", u"Pomoc", None))
        self.btnLanguage.setText("")
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
        self.btnHeaterControllerSetNone.setText(QCoreApplication.translate("MainWindow", u"Brak", None))
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
        self.btnHeaterControllerSetLeftCoil.setText(QCoreApplication.translate("MainWindow", u"y1", None))
#if QT_CONFIG(tooltip)
        self.btnHeaterControllerSetRightCoil.setToolTip(QCoreApplication.translate("MainWindow", u"Wybierz prawy czujnik temperatury", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btnHeaterControllerSetRightCoil.setStatusTip(QCoreApplication.translate("MainWindow", u"Wybierz prawy czujnik temperatury", None))
#endif // QT_CONFIG(statustip)
        self.btnHeaterControllerSetRightCoil.setText(QCoreApplication.translate("MainWindow", u"y2", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Napi\u0119cie  </p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.inHeaterBBPower.setToolTip(QCoreApplication.translate("MainWindow", u"Min: 0 | Max: 100", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.inHeaterBBPower.setStatusTip(QCoreApplication.translate("MainWindow", u"Min: 0 | Max: 100", None))
#endif // QT_CONFIG(statustip)
        self.lblPower.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"Ch\u0142odzenie wentylatorem", None))
        self.chxFanCooling.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Warto\u015b\u0107 zadana	</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.inHeaterSetValue.setToolTip(QCoreApplication.translate("MainWindow", u"Min: 0 | Max: 100", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.inHeaterSetValue.setStatusTip(QCoreApplication.translate("MainWindow", u"Min: 0 | Max: 100", None))
#endif // QT_CONFIG(statustip)
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u00b0C</p></body></html>", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Forma sygna\u0142u", None))
        self.btnHeaterRefStep.setText(QCoreApplication.translate("MainWindow", u"Skok", None))
        self.btnHeaterRefRamp.setText(QCoreApplication.translate("MainWindow", u"Rampa", None))
        self.btnHeaterRefSinewave.setText(QCoreApplication.translate("MainWindow", u"Sinusoida", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Nachylenie", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"\u00b0C/s", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Amplituda", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Omega", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"rad/s", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Wyb\u00f3r regulatora	</p></body></html>", None))
        self.btnFanControllerSetNone.setText(QCoreApplication.translate("MainWindow", u"Brak", None))
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
        self.label.setText(QCoreApplication.translate("MainWindow", u"Wype\u0142nienie PWM  ", None))
        self.lblFanPWM.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Warto\u015b\u0107 zadana	</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.inFanSetValue.setToolTip(QCoreApplication.translate("MainWindow", u"Min: 0 | Max: 6000", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.inFanSetValue.setStatusTip(QCoreApplication.translate("MainWindow", u"Min: 0 | Max: 6000", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.inFanSetValue.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"RPM", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Forma sygna\u0142u", None))
        self.btnFanRefStep.setText(QCoreApplication.translate("MainWindow", u"Skok", None))
        self.btnFanRefRamp.setText(QCoreApplication.translate("MainWindow", u"Rampa", None))
        self.btnFanRefSinewave.setText(QCoreApplication.translate("MainWindow", u"Sinusoida", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Nachylenie", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"RPM/s", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Amplituda", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"RPM", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Omega", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"rad/s", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Histereza	</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.inHeaterBBHysteresis.setToolTip(QCoreApplication.translate("MainWindow", u"Min: 0 | Max: 100", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.inHeaterBBHysteresis.setStatusTip(QCoreApplication.translate("MainWindow", u"Min: 0 | Max: 100", None))
#endif // QT_CONFIG(statustip)
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u00b0C</p></body></html>", None))
        self.btnBBHeaterHelp.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">K</span><span style=\" font-weight:700; vertical-align:sub;\">p</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.inHeaterPID_Kp.setToolTip(QCoreApplication.translate("MainWindow", u"Min: 0.00 | Max: 99.99", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.inHeaterPID_Kp.setStatusTip(QCoreApplication.translate("MainWindow", u"Min: 0.00 | Max: 99.99", None))
#endif // QT_CONFIG(statustip)
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"V/\u00b0C", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">K</span><span style=\" font-weight:700; vertical-align:sub;\">i</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.inHeaterPID_Ki.setToolTip(QCoreApplication.translate("MainWindow", u"Min: 0.00 | Max: 99.99", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.inHeaterPID_Ki.setStatusTip(QCoreApplication.translate("MainWindow", u"Min: 0.00 | Max: 99.99", None))
#endif // QT_CONFIG(statustip)
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"V/\u00b0C/s", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">T</span><span style=\" font-weight:700; vertical-align:sub;\">i</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.inHeaterPID_Ti.setToolTip(QCoreApplication.translate("MainWindow", u"Min: 0.00 | Max: 99.99", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.inHeaterPID_Ti.setStatusTip(QCoreApplication.translate("MainWindow", u"Min: 0.00 | Max: 99.99", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.inHeaterPID_Ti.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">K</span><span style=\" font-weight:700; vertical-align:sub;\">d</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.inHeaterPID_Kd.setToolTip(QCoreApplication.translate("MainWindow", u"Min: 0.00 | Max: 99.99", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.inHeaterPID_Kd.setStatusTip(QCoreApplication.translate("MainWindow", u"Min: 0.00 | Max: 99.99", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.inHeaterPID_Kd.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"V*s/\u00b0C", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">T</span><span style=\" font-weight:700; vertical-align:sub;\">d</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.inHeaterPID_Td.setToolTip(QCoreApplication.translate("MainWindow", u"Min: 0.00 | Max: 99.99", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.inHeaterPID_Td.setStatusTip(QCoreApplication.translate("MainWindow", u"Min: 0.00 | Max: 99.99", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.inHeaterPID_Td.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">K</span><span style=\" font-weight:700; vertical-align:sub;\">aw</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.inHeaterPID_Kaw.setToolTip(QCoreApplication.translate("MainWindow", u"Min: 0.00 | Max: 999.99", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.inHeaterPID_Kaw.setStatusTip(QCoreApplication.translate("MainWindow", u"Min: 0.00 | Max: 999.99", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.inHeaterPID_Kaw.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"Forma r\u00f3wnania ", None))
        self.btnEquationTypeHeater.setText(QCoreApplication.translate("MainWindow", u"r\u00f3wnoleg\u0142a", None))
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
        self.btnBBFanHelp.setText("")
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">K</span><span style=\" font-weight:700; vertical-align:sub;\">p</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.inFanPID_Kp.setToolTip(QCoreApplication.translate("MainWindow", u"Min: 0.0 | Max: 999.99", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.inFanPID_Kp.setStatusTip(QCoreApplication.translate("MainWindow", u"Min: 0.0 | Max: 999.99", None))
#endif // QT_CONFIG(statustip)
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>V/RPM</p></body></html>", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">K</span><span style=\" font-weight:700; vertical-align:sub;\">i</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.inFanPID_Ki.setToolTip(QCoreApplication.translate("MainWindow", u"Min: 0.0 | Max: 999.99", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.inFanPID_Ki.setStatusTip(QCoreApplication.translate("MainWindow", u"Min: 0.0 | Max: 999.99", None))
#endif // QT_CONFIG(statustip)
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"V/RPM/s", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">T</span><span style=\" font-weight:700; vertical-align:sub;\">i</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.inFanPID_Ti.setToolTip(QCoreApplication.translate("MainWindow", u"Min: 0.0 | Max: 999.99", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.inFanPID_Ti.setStatusTip(QCoreApplication.translate("MainWindow", u"Min: 0.0 | Max: 999.99", None))
#endif // QT_CONFIG(statustip)
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">K</span><span style=\" font-weight:700; vertical-align:sub;\">d</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.inFanPID_Kd.setToolTip(QCoreApplication.translate("MainWindow", u"Min: 0.0 | Max: 999.99", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.inFanPID_Kd.setStatusTip(QCoreApplication.translate("MainWindow", u"Min: 0.0 | Max: 999.99", None))
#endif // QT_CONFIG(statustip)
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"V*s/RPM", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">T</span><span style=\" font-weight:700; vertical-align:sub;\">d</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.inFanPID_Td.setToolTip(QCoreApplication.translate("MainWindow", u"Min: 0.0 | Max: 999.99", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.inFanPID_Td.setStatusTip(QCoreApplication.translate("MainWindow", u"Min: 0.0 | Max: 999.99", None))
#endif // QT_CONFIG(statustip)
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">K</span><span style=\" font-weight:700; vertical-align:sub;\">aw</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.inFanPID_Kaw.setToolTip(QCoreApplication.translate("MainWindow", u"Min: 0.0 | Max: 999.99", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.inFanPID_Kaw.setStatusTip(QCoreApplication.translate("MainWindow", u"Min: 0.0 | Max: 999.99", None))
#endif // QT_CONFIG(statustip)
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"Forma r\u00f3wnania ", None))
        self.btnEquationTypeFan.setText(QCoreApplication.translate("MainWindow", u"r\u00f3wnoleg\u0142a", None))
        self.btnHeaterBB_graph_u_min.setText(QCoreApplication.translate("MainWindow", u"u_min", None))
        self.btnHeaterBB_graph_y_2.setText(QCoreApplication.translate("MainWindow", u"y_2(t)", None))
        self.btnHeaterBB_graph_u_max.setText(QCoreApplication.translate("MainWindow", u"u_max", None))
        self.btnHeaterBB_graph_x_max.setText(QCoreApplication.translate("MainWindow", u"r_max", None))
        self.btnHeaterBB_graph_x.setText(QCoreApplication.translate("MainWindow", u"r(t)", None))
        self.btnHeaterBB_graph_mode.setText(QCoreApplication.translate("MainWindow", u"stan", None))
        self.btnHeaterBB_graph_x_min.setText(QCoreApplication.translate("MainWindow", u"r_min", None))
        self.btnHeaterBB_graph_y_1.setText(QCoreApplication.translate("MainWindow", u"y_1(t)", None))
        self.btnHeaterBB_graph_e.setText(QCoreApplication.translate("MainWindow", u"e(t)", None))
        self.btnHeaterBB_graph_u.setText(QCoreApplication.translate("MainWindow", u"u(t)", None))
        self.btnHeaterPID_graph_u_sat.setText(QCoreApplication.translate("MainWindow", u"u_sat(t)", None))
        self.btnHeaterPID_graph_x.setText(QCoreApplication.translate("MainWindow", u"r(t)", None))
        self.btnHeaterPID_graph_mode.setText(QCoreApplication.translate("MainWindow", u"stan", None))
        self.btnHeaterPID_graph_aw_int_e.setText(QCoreApplication.translate("MainWindow", u"aw_int_e(t)", None))
        self.btnHeaterPID_graph_u.setText(QCoreApplication.translate("MainWindow", u"u(t)", None))
        self.btnHeaterPID_graph_y_1.setText(QCoreApplication.translate("MainWindow", u"y_1(t)", None))
        self.btnHeaterPID_graph_u_max.setText(QCoreApplication.translate("MainWindow", u"u_max", None))
        self.btnHeaterPID_graph_int_e.setText(QCoreApplication.translate("MainWindow", u"int_e(t)", None))
        self.btnHeaterPID_graph_u_i.setText(QCoreApplication.translate("MainWindow", u"u_i(t)", None))
        self.btnHeaterPID_graph_y_2.setText(QCoreApplication.translate("MainWindow", u"y_2(t)", None))
        self.btnHeaterPID_graph_u_p.setText(QCoreApplication.translate("MainWindow", u"u_p(t)", None))
        self.btnHeaterPID_graph_u_min.setText(QCoreApplication.translate("MainWindow", u"u_min", None))
        self.btnHeaterPID_graph_u_d.setText(QCoreApplication.translate("MainWindow", u"u_d(t)", None))
        self.btnHeaterPID_graph_e.setText(QCoreApplication.translate("MainWindow", u"e(t)", None))
        self.btnFanBB_graph_y.setText(QCoreApplication.translate("MainWindow", u"y(t)", None))
        self.btnFanBB_graph_u_max.setText(QCoreApplication.translate("MainWindow", u"u_max", None))
        self.btnFanBB_graph_x_max.setText(QCoreApplication.translate("MainWindow", u"r_max", None))
        self.btnFanBB_graph_x_min.setText(QCoreApplication.translate("MainWindow", u"r_min", None))
        self.btnFanBB_graph_mode.setText(QCoreApplication.translate("MainWindow", u"stan", None))
        self.btnFanBB_graph_e.setText(QCoreApplication.translate("MainWindow", u"e(t)", None))
        self.btnFanBB_graph_x.setText(QCoreApplication.translate("MainWindow", u"r(t)", None))
        self.btnFanBB_graph_u_min.setText(QCoreApplication.translate("MainWindow", u"u_min", None))
        self.btnFanBB_graph_u.setText(QCoreApplication.translate("MainWindow", u"u(t)", None))
        self.btnFanPID_graph_u_sat.setText(QCoreApplication.translate("MainWindow", u"u_sat(t)", None))
        self.btnFanPID_graph_aw_int_e.setText(QCoreApplication.translate("MainWindow", u"aw_int_e(t)", None))
        self.btnFanPID_graph_y.setText(QCoreApplication.translate("MainWindow", u"y(t)", None))
        self.btnFanPID_graph_mode.setText(QCoreApplication.translate("MainWindow", u"stan", None))
        self.btnFanPID_graph_u_max.setText(QCoreApplication.translate("MainWindow", u"u_max", None))
        self.btnFanPID_graph_e.setText(QCoreApplication.translate("MainWindow", u"e(t)", None))
        self.btnFanPID_graph_u_i.setText(QCoreApplication.translate("MainWindow", u"u_i(t)", None))
        self.btnFanPID_graph_int_e.setText(QCoreApplication.translate("MainWindow", u"int_e(t)", None))
        self.btnFanPID_graph_u_d.setText(QCoreApplication.translate("MainWindow", u"u_d(t)", None))
        self.btnFanPID_graph_x.setText(QCoreApplication.translate("MainWindow", u"r(t)", None))
        self.btnFanPID_graph_u_min.setText(QCoreApplication.translate("MainWindow", u"u_min", None))
        self.btnFanPID_graph_u_p.setText(QCoreApplication.translate("MainWindow", u"u_p(t)", None))
        self.btnFanPID_graph_u.setText(QCoreApplication.translate("MainWindow", u"u(t)", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Grza\u0142ka", None))
        self.chxExHeaterBB.setText(QCoreApplication.translate("MainWindow", u"Regulator dwupo\u0142o\u017ceniowy", None))
        self.chxExHeaterBB_u_min.setText(QCoreApplication.translate("MainWindow", u"u_min", None))
        self.chxExHeaterBB_x_max.setText(QCoreApplication.translate("MainWindow", u"r_max", None))
        self.chxExHeaterBB_u_max.setText(QCoreApplication.translate("MainWindow", u"u_max", None))
        self.chxExHeaterBB_x_min.setText(QCoreApplication.translate("MainWindow", u"r_min", None))
        self.chxExHeaterBB_y_1.setText(QCoreApplication.translate("MainWindow", u"y_1(t)", None))
        self.chxExHeaterBB_x.setText(QCoreApplication.translate("MainWindow", u"r(t)", None))
        self.chxExHeaterBB_y_2.setText(QCoreApplication.translate("MainWindow", u"y_2(t)", None))
        self.chxExHeaterBB_mode.setText(QCoreApplication.translate("MainWindow", u"stan", None))
        self.chxExHeaterPID.setText(QCoreApplication.translate("MainWindow", u"Regulator PID", None))
        self.chxExHeaterPID_aw_int_e.setText(QCoreApplication.translate("MainWindow", u"aw_int_e(t)", None))
        self.chxExHeaterPID_k_i.setText(QCoreApplication.translate("MainWindow", u"k_i", None))
        self.chxExHeaterPID_x.setText(QCoreApplication.translate("MainWindow", u"r(t)", None))
        self.chxExHeaterPID_mode.setText(QCoreApplication.translate("MainWindow", u"stan", None))
        self.chxExHeaterPID_k_d.setText(QCoreApplication.translate("MainWindow", u"k_d", None))
        self.chxExHeaterPID_int_e.setText(QCoreApplication.translate("MainWindow", u"int_e(t)", None))
        self.chxExHeaterPID_e.setText(QCoreApplication.translate("MainWindow", u"e(t)", None))
        self.chxExHeaterPID_k_aw.setText(QCoreApplication.translate("MainWindow", u"k_aw", None))
        self.chxExHeaterPID_k_p.setText(QCoreApplication.translate("MainWindow", u"k_p", None))
        self.chxExHeaterPID_u_p.setText(QCoreApplication.translate("MainWindow", u"u_p(t)", None))
        self.chxExHeaterPID_u_i.setText(QCoreApplication.translate("MainWindow", u"u_i(t)", None))
        self.chxExHeaterPID_u_sat.setText(QCoreApplication.translate("MainWindow", u"u_sat(t)", None))
        self.chxExHeaterPID_u.setText(QCoreApplication.translate("MainWindow", u"u(t)", None))
        self.chxExHeaterPID_u_d.setText(QCoreApplication.translate("MainWindow", u"u_d(t)", None))
        self.chxExHeaterPID_u_max.setText(QCoreApplication.translate("MainWindow", u"u_max", None))
        self.chxExHeaterPID_u_min.setText(QCoreApplication.translate("MainWindow", u"u_min", None))
        self.chxExHeaterPID_y_1.setText(QCoreApplication.translate("MainWindow", u"y_1(t)", None))
        self.chxExHeaterPID_y_2.setText(QCoreApplication.translate("MainWindow", u"y_2(t)", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Wentylator", None))
        self.chxExFanBB.setText(QCoreApplication.translate("MainWindow", u"Regulator dwupo\u0142o\u017ceniowy", None))
        self.chxExFanBB_mode.setText(QCoreApplication.translate("MainWindow", u"stan", None))
        self.chxExFanBB_x_max.setText(QCoreApplication.translate("MainWindow", u"r_max", None))
        self.chxExFanBB_u_min.setText(QCoreApplication.translate("MainWindow", u"u_min", None))
        self.chxExFanBB_x.setText(QCoreApplication.translate("MainWindow", u"r(t)", None))
        self.chxExFanBB_y.setText(QCoreApplication.translate("MainWindow", u"y(t)", None))
        self.chxExFanBB_x_min.setText(QCoreApplication.translate("MainWindow", u"r_min", None))
        self.chxExFanBB_u_max.setText(QCoreApplication.translate("MainWindow", u"u_max", None))
        self.chxExFanPID.setText(QCoreApplication.translate("MainWindow", u"Regulator PID", None))
        self.chxExFanPID_x.setText(QCoreApplication.translate("MainWindow", u"r(t)", None))
        self.chxExFanPID_u.setText(QCoreApplication.translate("MainWindow", u"u(t)", None))
        self.chxExFanPID_e.setText(QCoreApplication.translate("MainWindow", u"e(t)", None))
        self.chxExFanPID_u_sat.setText(QCoreApplication.translate("MainWindow", u"u_sat(t)", None))
        self.chxExFanPID_int_e.setText(QCoreApplication.translate("MainWindow", u"int_e(t)", None))
        self.chxExFanPID_u_p.setText(QCoreApplication.translate("MainWindow", u"u_p(t)", None))
        self.chxExFanPID_aw_int_e.setText(QCoreApplication.translate("MainWindow", u"aw_int_e(t)", None))
        self.chxExFanPID_u_i.setText(QCoreApplication.translate("MainWindow", u"u_i(t)", None))
        self.chxExFanPID_k_p.setText(QCoreApplication.translate("MainWindow", u"k_p", None))
        self.chxExFanPID_u_d.setText(QCoreApplication.translate("MainWindow", u"u_d(t)", None))
        self.chxExFanPID_k_i.setText(QCoreApplication.translate("MainWindow", u"k_i", None))
        self.chxExFanPID_u_max.setText(QCoreApplication.translate("MainWindow", u"u_max", None))
        self.chxExFanPID_k_d.setText(QCoreApplication.translate("MainWindow", u"k_d", None))
        self.chxExFanPID_u_min.setText(QCoreApplication.translate("MainWindow", u"u_min", None))
        self.chxExFanPID_k_aw.setText(QCoreApplication.translate("MainWindow", u"k_aw", None))
        self.chxExFanPID_y.setText(QCoreApplication.translate("MainWindow", u"y(t)", None))
        self.chxExFanPID_mode.setText(QCoreApplication.translate("MainWindow", u"stan", None))
        self.btnExportAction.setText(QCoreApplication.translate("MainWindow", u"Eksportuj", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Jak korzysta\u0107 z aplikacji?</span></p><p><span style=\" font-weight:700;\">1. Po\u0142\u0105cz si\u0119 z urz\u0105dzeniem</span></p><p>Upewnij si\u0119, \u017ce urz\u0105dzenie jest zasilone oraz po\u0142\u0105czone z komputerem za pomoc\u0105 przewodu USB. Nast\u0119pnie, naci\u015bnij przycisk &quot;<img src=\":/assets/assets/uC.ico\"/> Connect&quot;. Je\u015bli urz\u0105dzenie jest poprawnie podpi\u0119te, zak\u0142adki &quot;<img src=\":/assets/assets/heater.ico\"/> Grza\u0142ka&quot; oraz &quot;<img src=\":/assets/assets/fan.ico\"/> Wentylator&quot; powinny sta\u0107 si\u0119 dost\u0119pne.</p><p><span style=\" font-weight:700;\">2. Sterowanie</span></p><p>Aplikacja pozwala sterowa\u0107 grza\u0142k\u0105( w postaci ma\u0142ych rezystor\u00f3w) oraz wentylatorem. Wchodz\u0105c w zak\u0142adk\u0119 &quot;<img src=\":/assets/assets/heater.ico\"/> Grza\u0142ka&quot; lub &quot;<img src=\":/assets/assets/fan.ico\"/> Wentylator&quot; b\u0119dziesz m\u00f3"
                        "g\u0142 wybra\u0107 odpowiadaj\u0105cy Ci regulator oraz zmieni\u0107 jego nastawy. </p><p>Po wybraniu regulatora oraz jego nastaw, mo\u017cesz go uruchomi\u0107 naciskaj\u0105c przycisk &quot;START&quot;, a p\u00f3\u017aniej zatrzyma\u0107 wciskaj\u0105c ten sam przycisk, lecz ze zmienionym napisem - &quot;STOP&quot;.</p><p><span style=\" font-weight:700;\">3. Regulator dwupo\u0142o\u017ceniowy</span></p><p>W przypadku wentylatora, mo\u017cesz wybra\u0107 warto\u015b\u0107 jego pr\u0119dko\u015bci obrotowej oraz szeroko\u015b\u0107 strefy histerezy.</p><p>W przypadku grza\u0142ki, mo\u017cesz wybra\u0107 warto\u015b\u0107 jej temperatury, szeroko\u015b\u0107 strefy histerezy, a tak\u017ce moc grza\u0142ki.</p><p><span style=\" font-weight:700;\">4. Regulator PID</span></p><p>W obu przypadkach( grza\u0142ki i wentylatora), mo\u017cesz wybra\u0107:</p><p>- warto\u015b\u0107 zadan\u0105,</p><p>- wsp\u00f3\u0142czynniki wzmocnienia: proporcjonalnego, ca\u0142kuj\u0105cego i r\u00f3\u017cniczkuj\u0105cego,</p><p>-"
                        " czas zdwojenia i op\u00f3\u017anienia,</p><p>- warto\u015b\u0107 wsp\u00f3\u0142czynnika anti-windup.</p><p><span style=\" font-weight:700;\">5. Sterowanie grza\u0142k\u0105</span></p><p>W zak\u0142adce sterowania grza\u0142k\u0105 znajdziesz dodatkowe przyciski, kt\u00f3re pozwalaj\u0105 na wyb\u00f3r grza\u0142ki( 17 lub 33\u03a9) oraz temperatury odniesienia. </p><p>Obie grza\u0142ki znajduj\u0105 si\u0119 bezpo\u015brednio nad wentylatorem. Lewa to ta, kt\u00f3ra jest nad 17\u03a9 grza\u0142ka, natomiast prawa zlokalizowana nad 33\u03a9 grza\u0142k\u0105.</p><p><span style=\" font-weight:700;\">6. Wykresy</span></p><p>Ka\u017cdy regulator posiada sw\u00f3j wykres, kt\u00f3ry przedstawia przebiegi czasowe wszystkich jego sygna\u0142\u00f3w.</p><p>Wykres ten mo\u017cesz zatrzyma\u0107 naciskaj\u0105c przycisk &quot;<img src=\":/assets/assets/pause.ico\"/>&quot; i uruchomi\u0107 ponownie wciskaj\u0105c przycisk &quot;<img src=\":/assets/assets/play.ico\"/>&quot;.</p><p>Wykres mo\u017cesz r\u00f3wnie\u017c wy"
                        "czy\u015bci\u0107 wciskaj\u0105c przcisk &quot;<img src=\":/assets/assets/broom.ico\"/>&quot;. <span style=\" font-weight:700; color:#ff0000;\">Uwa\u017caj</span>, gdy\u017c wyszyszczenie wykresu powoduje usuni\u0119cie danych o jego dotychczasowych przebiegach z pami\u0119ciu programu.</p><p>Ka\u017cdy regulator posiada w\u0142asn\u0105 przestrze\u0144 w pami\u0119ci programu, wi\u0119c <span style=\" font-weight:700; color:#ffaa00;\">wyczyszczenie jednego z nich nie spowoduje wyszyczenia pozosta\u0142ych</span>.</p><p>Pod ka\u017cdym wykresem znajduj\u0105 si\u0119 dodatkowe przyciski, kt\u00f3re pozwalaj\u0105 na pokazywanie i ukrywanie konkretnych sygna\u0142\u00f3w.</p><p><span style=\" font-weight:700;\">7. Eksport danych do pliku</span></p><p>W zak\u0142adce &quot;<img src=\":/assets/assets/export.ico\"/> Eksport danych&quot; mo\u017cesz \u0142atwo wyeksportowa\u0107 potrzebne Ci dane do pliku .xlsx.</p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Wszystkie ikony w aplikacji pochodz\u0105 z otwartego \u017ar\u00f3d\u0142a: Flaticon.com</p></body></html>", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Autor: Szymon Hrehorowicz", None))
        self.btnImportLoad.setText(QCoreApplication.translate("MainWindow", u"Wczytaj dane", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Nr albumu:", None))
        self.cmbImportIdx.setCurrentText("")
        self.btnImportAction.setText(QCoreApplication.translate("MainWindow", u"Pobierz nastawy", None))
        self.btnGraphsPageHeater.setText(QCoreApplication.translate("MainWindow", u"Wykresy grzalki", None))
        self.btnGraphsPageFan.setText(QCoreApplication.translate("MainWindow", u"Wykresy wentylatora", None))
        self.btnGraphsPage_x.setText(QCoreApplication.translate("MainWindow", u"r(t)", None))
        self.btnGraphsPage_y_1.setText(QCoreApplication.translate("MainWindow", u"y_1(t)", None))
        self.btnGraphsPage_y_2.setText(QCoreApplication.translate("MainWindow", u"y_2(t)", None))
        self.btnGraphsPage_y.setText(QCoreApplication.translate("MainWindow", u"y(t)", None))
        self.btnGraphsPage_u_p.setText(QCoreApplication.translate("MainWindow", u"u_p(t)", None))
        self.btnGraphsPage_u_i.setText(QCoreApplication.translate("MainWindow", u"u_i(t)", None))
        self.btnGraphsPage_u_d.setText(QCoreApplication.translate("MainWindow", u"u_d(t)", None))
        self.btnGraphsPage_u.setText(QCoreApplication.translate("MainWindow", u"u(t)", None))
        self.btnGraphsPage_u_sat.setText(QCoreApplication.translate("MainWindow", u"u_sat(t)", None))
    # retranslateUi


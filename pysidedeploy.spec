[app]

# title of your application
title = SPC

# project directory. the general assumption is that project_dir is the parent directory
# of input_file
project_dir = D:\ENGINEERING\IT\LANGUAGES\CPP\PracaInzV2

# source file path
input_file = D:\ENGINEERING\IT\LANGUAGES\CPP\PracaInzV2\mainwindow.py

# directory where exec is stored
exec_directory = .

# path to .pyproject project file
project_file = PracaInzV2.pyproject

# application icon
icon = D:\ENGINEERING\IT\LANGUAGES\CPP\PracaInzV2\icon.ico

[python]

# python path
python_path = D:\ENGINEERING\IT\LANGUAGES\CPP\PracaInzV2\venv\Scripts\python.exe

# python packages to install
packages = Nuitka==2.4.8

# buildozer = for deploying Android application
android_packages = buildozer==1.5.0,cython==0.29.33

[qt]

# comma separated path to qml files required
# normally all the qml files required by the project are added automatically
qml_files = 

# excluded qml plugin binaries
excluded_qml_plugins = 

# qt modules used. comma separated
modules = WebEngineWidgets,Widgets,SerialPort,Core,Gui

# qt plugins used by the application
plugins = platformthemes,platforminputcontexts,iconengines,accessiblebridge,generic,imageformats,xcbglintegrations,platforms/darwin,egldeviceintegrations,platforms,styles

[android]

# path to pyside wheel
wheel_pyside = 

# path to shiboken wheel
wheel_shiboken = 

# plugins to be copied to libs folder of the packaged application. comma separated
plugins = 

[nuitka]

# usage description for permissions requested by the app as found in the info.plist file
# of the app bundle
# eg = extra_args = --show-modules --follow-stdlib
macos.permissions = 

# mode of using nuitka. accepts standalone or onefile. default is onefile.
mode = onefile

# (str) specify any extra nuitka arguments
extra_args = --quiet --noinclude-qt-translations --windows-console-mode=disable

[buildozer]

# build mode
# possible options = [release, debug]
# release creates an aab, while debug creates an apk
mode = debug

# contrains path to pyside6 and shiboken6 recipe dir
recipe_dir = 

# path to extra qt android jars to be loaded by the application
jars_dir = 

# if empty uses default ndk path downloaded by buildozer
ndk_path = 

# if empty uses default sdk path downloaded by buildozer
sdk_path = 

# other libraries to be loaded. comma separated.
# loaded at app startup
local_libs = 

# architecture of deployed platform
# possible values = ["aarch64", "armv7a", "i686", "x86_64"]
arch = "x86_64"


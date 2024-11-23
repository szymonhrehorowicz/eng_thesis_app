# Resource object code (Python 3)
# Created by: object code
# Created by: The Resource Compiler for Qt version 6.8.0
# WARNING! All changes made in this file will be lost!

from PySide6 import QtCore

qt_resource_data = b"\
\x00\x00\x01\xd4\
<\
html>\x0a <head>\x0a  \
<script src=\x22htt\
ps://cdnjs.cloud\
flare.com/ajax/l\
ibs/mathjax/2.7.\
5/MathJax.js?con\
fig=TeX-AMS-MML_\
HTMLorMML\x22 type=\
\x22text/javascript\
\x22>\x0a  </script>\x0a \
</head>\x0a <body>\x0a\
    <p style=\x22fo\
nt-size:8px\x22>\x0a  \
  <mathjax id=\x22m\
ath\x22 style=\x22font\
-size:2.3em\x22>\x0a  \
  $$u(t) = K_pe(\
t) + K_i\x5cint_{0}\
^{t}e(\x5ctau) d\x5cta\
u + K_d\x5cfrac{de(\
t)}{dt} \x5cLeftrig\
htarrow u(t) = K\
_p(e(t) + \x5cfrac{\
1}{T_i}\x5cint_{0}^\
{t}e(\x5ctau) d\x5ctau\
 + T_d\x5cfrac{de(t\
)}{dt})$$\x0a    </\
mathjax>\x0a    </p\
>\x0a </body>\x0a</htm\
l>\x0a\
"

qt_resource_name = b"\
\x00\x06\
\x06\x8a\x9c\xb3\
\x00a\
\x00s\x00s\x00e\x00t\x00s\
\x00\x08\
\x0cG'\xe5\
\x00t\
\x00e\x00m\x00p\x00l\x00a\x00t\x00e\
"

qt_resource_struct = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x02\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x12\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x01\x93Xo\xd4\x81\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()

#  Author(s):  Roman Shcherbov
#  Created on: 2020-07

# (C) Copyright 2020 VoltBro, All Rights Reserved.

# --- begin cisst license - do not edit ---

# This software is provided "as is" under an open source license, with
# no warranty.  The complete license can be found in license.txt and
# http://www.cisst.org/cisst/license.txt.

# --- end cisst license ---

import easyhid
import rospy
import rospkg
import math
import threading
import ruka


class Controller():
    """Driver controller for RUKA arm, it provides connection to device controller,
    forming command for device controller, and reading position of servos
    """

    def __init__(self):
        self.CMD_SERVO_MOVE = 3
        self.CMD_GET_BATTERY_VOLTAGE = 15
        self.CMD_MULT_SERVO_UNLOAD = 20
        self.CMD_MULT_SERVO_POS_READ = 21

    def converting_integer_to_bits(self, i):
        lsb = i & 0xFF
        msb = i >> 8
        return lsb, msb
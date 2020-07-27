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
import math
import threading
import ruka


class Controller():
    """Driver controller for RUKA arm, it provides connection to device controller,
    forming command for device controller, and reading position of servos
    """

    def __init__(self):
        
        #Commands for Lewansoul Servos
        self.CMD_SERVO_MOVE = 3
        self.CMD_GET_BATTERY_VOLTAGE = 15
        self.CMD_MULT_SERVO_UNLOAD = 20
        self.CMD_MULT_SERVO_POS_READ = 21

        self._lock = threading.RLock()

        self.detecting_and_defining_ruka_controller()

    def __del__(self):
        pass
        """
        print('closing ruka controller')
        self.shutdown()
        self._device.close()
        """
    
    def shutdown(self):
        pass
        """
        Shut down procedure
        """
        """
        for arm in self._arms:
            print('shutting down ' + arm._name)
            self.disable(arm._servo_ids)
        """
    def detecting_and_defining_ruka_controller(self):
        pass
        """
        #searching for all hidraw devices
        en = easyhid.Enumeration()

        # return a list of devices based on the search parameters
        devices = en.find(vid = 1155, pid = 22352)

        # print a description of the devices found
        for dev in devices:
            print(dev.description())

        if len(devices) == 0:
            raise Exception('no device detected, make sure the arm is powered, connected and you have read-write permissions on /dev/hidraw')

        self._device = devices[0]

        # open a device
        self._device.open()
        self._serial_number = self._device.serial_number.encode('ascii')
        print('connected to Ruka controller: ' + self._serial_number)
        """

    def converting_integer_to_bits(self, i):
        # compute bits_to_rads: Lewansoul bits are 1000 for 240 degree
        # range, then convert from degrees to radians
        lsb = i & 0xFF
        msb = i >> 8
        return lsb, msb

    def adding_new_movegroup_to_drivers_namespace(self, name, config_file, urdf_file = ''):
        pass
        """
        Envoking new instance of ruka.movegroup_namespace class, and sending it's config and urdf file as args
        """
        """
        new_movegroup_namespace = ruka.movegroup_namespace(self, name, config_file, urdf_file)
        self._movegroup_namespace.append(new_movegroup_namespace)
        return new_movegroup_namespace
        """

    def measure_current_servos_angles(self):
        pass
        """
        Read the position of all servos
        ServoPositionRead=CMD_MULT_SERVO_POS_READ=21 (byte)count { (byte)id }; (byte)count { (byte)id (ushort)position }
        """

    def sending_command_to_ruka_controller(self, command_to_send):
        pass


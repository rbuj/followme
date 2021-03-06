#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# FollowMe Butia - Robot
# Copyright (C) 2010-2013
# This program was created to use with the robot Butia.
# Butia is a project from Facultad de Ingenieria - Uruguay
# Facultad de Ingenieria web site: <http://www.fing.edu.uy/>
# Butia project web site: <http://www.fing.edu.uy/inco/proyectos/butia/>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Contact information:
# Alan Aguiar <alanjas@gmail.com>
# Aylen Ricca <ar18_90@hotmail.com>
# Rodrigo Dearmas <piegrande46@hotmail.com>

import time
import commands
from pybot import usb4butia
import subprocess
from gettext import gettext as _

class Robot(object):

    def __init__(self, tamanioc):
        self.z1 = tamanioc[0] / 15.0
        self.z2 = tamanioc[1] / 3.0
        self.vel_actual = (0, 0, 0, 0)
        self.butia = None
        self.bobot = None
        self.bobot_launch()

    def bobot_launch(self):

        print 'Initialising butia...'

        self.butia = usb4butia.USB4Butia()

        self.modules = self.butia.getModulesList()

        if (self.modules != []):
            print self.modules
        else:
            print _('Butia robot was not detected')

    def move_robot(self, pos):

        x,y = pos

        if (x >= 0) and (x <= (2*self.z1)):
            if (y >= 0) and (y <= self.z2) :
                vel_actual = (1, 900, 1, 600)
            elif (y > self.z2) and (y < 2*self.z2):
                vel_actual = (0, 900, 1, 900)
            elif (y >= 2*self.z2):
                vel_actual = (0, 900, 0, 600)

        elif (x > (2*self.z1)) and (x <= (4*self.z1)):
            if (y >= 0) and (y <= self.z2) :
                vel_actual = (1, 600, 1, 300)
            elif (y > self.z2) and (y < 2*self.z2):
                vel_actual = (0, 600, 1, 600)
            elif (y >= 2*self.z2):
                vel_actual = (0, 600, 0, 600)


        elif (x > (4*self.z1)) and (x <= (6*self.z1)):
            if (y >= 0) and (y <= self.z2) :
                vel_actual = (1, 300, 1, 0)
            elif (y > self.z2) and (y < 2*self.z2):
                vel_actual = (0, 300, 1, 300)
            elif (y >= 2*self.z2):
                vel_actual = (0, 300, 0, 0)

        elif (x > 6*self.z1) and (x < 9*self.z1):
            if (y >= 0) and (y <= self.z2) :
                vel_actual = (1, 300, 1, 300)
            elif (y > self.z2) and (y < 2*self.z2):
                vel_actual = (0, 0, 0, 0)
            elif (y >= 2*self.z2):
                vel_actual = (0, 300, 0, 300)


        elif (x >= (9*self.z1)) and (x < (11*self.z1)):
            if (y >= 0) and (y <= self.z2) :
                vel_actual = (1, 0, 1, 300)
            elif (y > self.z2) and (y < 2*self.z2):
                vel_actual = (1, 300, 0, 300)
            elif (y >= 2*self.z2):
                vel_actual = (0, 0, 0, 300)


        elif (x >= 11*self.z1) and (x < 13*self.z1):
            if (y >= 0) and (y <= self.z2) :
                vel_actual = (1, 300, 1, 600)
            elif (y > self.z2) and (y < 2*self.z2):
                vel_actual = (1, 600, 0, 600)
            elif (y >= 2*self.z2):
                vel_actual = (0, 300, 0, 600)


        elif (x >= (13*self.z1)):
            if (y >= 0) and (y <= self.z2) :
                vel_actual = (1, 600, 1, 900)
            elif (y > self.z2) and (y < 2*self.z2):
                vel_actual = (1, 900, 0, 900)
            elif (y >= 2*self.z2):
                vel_actual = (0, 600, 0, 900)


        self.butia.set2MotorSpeed(vel_actual[0], vel_actual[1], vel_actual[2], vel_actual[3])

    def stop_robot(self):
        self.butia.set2MotorSpeed(0, 0, 0, 0)


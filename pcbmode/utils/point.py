#!/usr/bin/python

# PCBmodE, a printed circuit design software with a twist
# Copyright (C) 2020 Saar Drimer
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
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


from math import pi, sin, cos
import decimal

from pcbmode.config import config


DEG2RAD = 2 * pi / 360


class Point:
    def __init__(self, xy_list=[0,0]):
        self.set_sig_dig(config.cfg["params"].get("significant-digits", 8))
        self.x = float(xy_list[0])
        self.y = float(xy_list[1])

    def __add__(self, p):
        """ add point 'p' of type Point to current point"""
        return Point(self.x + p.x, self.y + p.y)

    def __sub__(self, p):
        """ subtract point 'p' of type Point to current point"""
        return Point(self.x - p.x, self.y - p.y)

    def __repr__(self, d=2):
        """ 
        return a string representation; 'd' determines amount
        of significant digits to display
        """
        return "[%.*f, %.*f]" % (d, self.x, d, self.y)

    def __eq__(self, p):
        """ equality attribute """
        return (self.x == p.x) and (self.y == p.y)

    def __ne__(self, p):
        """ not equal attribute """
        return not ((self.x == p.x) and (self.y == p.y))

    def set_sig_dig(self, sig_dig):
        """ Set the significant digits to use """
        self._sig_dig = sig_dig

    def assign(self, x=0, y=0):
        self.x = float(x)
        self.y = float(y)

    def rotate(self, deg, p):
        """ rotate the point in degrees around another point """
        rad = deg * DEG2RAD
        x = self.x
        y = self.y
        self.x = x * cos(rad) + y * sin(rad)
        self.y = x * -sin(rad) + y * cos(rad)

    def round(self):
        """ round decimal to nearest 'd' decimal digits """
        self.x = self.x
        self.y = self.y

    def mult(self, scalar):
        """ multiply by scalar """
        self.x *= float(scalar)
        self.y *= float(scalar)

    def px(self):
        """ Apply significant digits and int() floats """
        if self.x.is_integer():
            return int(self.x)
        else:
            return round(self.x, self._sig_dig)

    def py(self):
        """ Apply significant digits and int() floats """
        if self.y.is_integer():
            return int(self.y)
        else:
          return round(self.y, self._sig_dig)

#!/usr/bin/env python3

"""
Active source code installer
Copyright (C) 2021  Hussein Layth Al-Madhachi

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License 
as published by the Free Software Foundation, version 2


This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA

"""

from sys import argv as arguements
from os import system

parameters = ""

for arguement in arguements[ 1 : ]:
    parameters += " " + arguement

system( "/usr/src/active/active.py " + parameters )

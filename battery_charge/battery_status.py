#!/usr/bin/env python3

from enum import Enum


class BatteryStatus(Enum):
    discharging = "discharging"
    charging = "charging"
    ac_power = "ac_power"

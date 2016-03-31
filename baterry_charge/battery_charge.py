#!/usr/bin/env python3

from enum import Enum
import sys


class BatteryStatus(Enum):
    discharging = "discharging"
    charging = "charging"
    ac_power = "ac"


class BatteryCharge:
    def __init__(self):
        pass

    def get_battery_charge(self):
        pass


class BatteryChargeMac(BatteryCharge):
    def __init__(self):
        super().__init__()
        import subprocess
        p = subprocess.Popen(["ioreg", "-rc", "AppleSmartBattery"],
                             stdout=subprocess.PIPE)
        self.battery_info = None
        rtn_val = p.communicate(timeout=0.1)[0]
        if rtn_val:
            self.battery_info = rtn_val.splitlines()

    def get_battery_charge(self):
        if not self.battery_info:
            return None
        max_capacity = self.battery_info


class BatteryChargeWin(BatteryCharge):
    def __init__(self):
        super().__init__()
        import wmi
        c = wmi.WMI()
        t = wmi.WMI(moniker="//./root/wmi")
        w = wmi.WMI()

        # noinspection SqlNoDataSourceInspection
        batteries = w.query("select * from Win32_Battery")

        if batteries:
            # choose the first battery
            self.bat = batteries[0]
        else:
            self.bat = None

    def get_battery_charge(self):
        if not self.bat:
            return None
        val = self.bat.BatteryStatus
        if val == 1 or val == 4 or val == 5:
            # discharging
            status = BatteryStatus.discharging
        elif val == 3 or val == 6 or val == 7 \
                or val == 8 or val == 9:
            # charging
            status = BatteryStatus.charging
        else:
            status = BatteryStatus.ac_power
        level = self.bat.EstimatedChargeRemaining
        if level > 100:
            level = 100
        return level, status


platform = sys.platform


def get_battery_charge():
    battery_charge = None
    if platform == "linux" or platform == "linux2":
        # linux
        pass
    elif platform == "darwin":
        # OS X
        pass
    elif platform == "win32":
        # windows
        battery_charge = BatteryChargeWin()
    if not battery_charge:
        return None
    return battery_charge.get_battery_charge()

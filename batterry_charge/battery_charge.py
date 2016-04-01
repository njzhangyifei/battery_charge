#!/usr/bin/env python3

import sys
from .battery_status import BatteryStatus


class BatteryCharge:
    def __init__(self):
        pass

    def get_battery_charge(self):
        pass


class BatteryChargeLinux(BatteryCharge):
    def __init__(self):
        super().__init__()
        import subprocess
        import re
        command = "upower -i $(upower -e | grep BAT) | grep -E \"state|to\\ full|percentage\""
        rtn_val = subprocess.check_output(["/bin/bash", "-c", command]).splitlines()
        stdout_encoding = sys.stdout.encoding
        self.upower_info = None
        if rtn_val:
            rtn_val = [l.decode(stdout_encoding).strip() for l in rtn_val]
            upower_info = dict()
            for line in rtn_val:
                re_match = re.match(r'([a-zA-Z]+):(.+)', line)
                if not re_match:
                    continue
                upower_info.update(
                    {re_match.group(1).strip(): re_match.group(2).strip()}
                )
            self.upower_info = upower_info

    def get_battery_charge(self):
        if not self.upower_info:
            return None
        upower_state = self.upower_info["state"]
        percentage = int(self.upower_info["percentage"][:-1])
        if upower_state == "discharging":
            status = BatteryStatus.discharging
        elif upower_state == "charging":
            status = BatteryStatus.charging
        else:
            status = BatteryStatus.ac_power
        return percentage, status


class BatteryChargeMac(BatteryCharge):
    def __init__(self):
        super().__init__()
        import subprocess
        import re
        rtn_val = subprocess.check_output(["ioreg", "-r", "-w0", "-cAppleSmartBattery"]).splitlines()
        stdout_encoding = sys.stdout.encoding
        self.battery_info = None
        if rtn_val:
            # parse the ioreg stuff
            rtn_val = [l.decode(stdout_encoding).strip() for l in rtn_val]
            battery_info = dict()
            for line in rtn_val:
                re_match = re.match(r'.*"(.+)" = (.+)', line)
                if not re_match:
                    continue
                battery_info.update(
                    {re_match.group(1): re_match.group(2)}
                )
            self.battery_info = battery_info

    def get_battery_charge(self):
        if not self.battery_info:
            return None
        max_capacity = self.battery_info["MaxCapacity"]
        current_capacity = self.battery_info["CurrentCapacity"]
        if self.battery_info["IsCharging"] == "Yes":
            status = BatteryStatus.charging
        elif self.battery_info["ExternalChargeCapable"] == "Yes":
            status = BatteryStatus.ac_power
        else:
            status = BatteryStatus.discharging
        return round(float(current_capacity) / float(max_capacity) * 100), status


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
        # battery_charge = BatteryChargeMac()
        battery_charge = BatteryChargeLinux()
    elif platform == "win32":
        # window
        battery_charge = BatteryChargeWin()
    if not battery_charge:
        return None
    return battery_charge.get_battery_charge()

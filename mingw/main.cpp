#include <windows.h>
#include <iostream>

int main() {
    SYSTEM_POWER_STATUS test;
    GetSystemPowerStatus(&test);
    int percent  = test.BatteryLifePercent;
    if (percent > 100) percent = 100;
    std::string out;
    if (test.BatteryFlag & 8) {
        out = "charging";
    } else if (test.ACLineStatus == 1) {
        out = "AC";
    } else {
        out = "discharging";
    }
    out += " " + std::to_string(percent);
    std::cout << out << std::endl;
    return 0;
}
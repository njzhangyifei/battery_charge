from baterry_charge import battery_charge

battery_status = battery_charge.get_battery_status()
battery_percentage = battery_charge.get_battery_percentage()

print("{0} {1}".format(battery_percentage, battery_status.value))

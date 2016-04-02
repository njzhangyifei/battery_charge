# ./battery_charge

`battery_charge` is a simple cross-platform command line utility (python3) for checking battery status.

All the script does is to show the current battery percentage and whether it is charging.

### Dependency

- Python 3
- Linux: `upower` UPower command line tool (comes with the system for Ubuntu)
- OS X: `ioreg` (comes with the system)
- Windows: `wmi` python module
    - install with `pip install wmi` using the `pip` from python 3

### Install
- `./setup.py install` (run with `sudo` on Linux)

### Platform Tested
- Windows 10
- OS X 10.10.5 (Yosemite)
- Ubuntu 14.04 (Trusty Tahr)

### Usage
You will need to put "X:/Python3X/Scripts" into your PATH on Windows.
```bash
$ battery_charge
99 ac_power
```
Use `read` command to get both the battery percentage and the status into variables.
```bash
$ bat_info=`battery_charge | tr -d '\r\n'`
$ read bat_percentage bat_status <<< $bat_info
$ echo $bat_percentage
95
$ echo $bat_status
discharging
```

### About Battery Status

| Status Value |          Linux           |      Mac      |                                     Windows                                       |
|--------------|--------------------------|---------------|-----------------------------------------------------------------------------------|
| discharging  | battery is discharging   | same          | same                                                                              |
| charging     | battery is charging      | same          | same                                                                              |
| ac_power     | battery is fully charged | same as Linux | battery is not necessarily fully charged, but the system is running on AC adapter |


### Use with zsh (or any other shell)
You could create a battery segment on $PS1 using this script with Oh-my-zsh + agnoster theme.

Here are some demos. See `demo/zsh_prompt` for more detail.
#### Mac

- Running on AC adapter

![mac ac](https://cloud.githubusercontent.com/assets/2238599/14226482/23d436ee-f916-11e5-98b1-dadbaf90dc45.png)

- Charging

![mac_charging](https://cloud.githubusercontent.com/assets/2238599/14226485/394d959c-f916-11e5-9730-b062d58bda47.png)

#### Windows

- Changing from Battery to AC adapter

![win_battery_ac](https://cloud.githubusercontent.com/assets/2238599/14226519/b609d4ec-f899-11e5-9bb3-92523aa34f61.png)

- Low Battery Warning (<20%)

![win_low_battery](https://cloud.githubusercontent.com/assets/2238599/14226520/b60cf794-f899-11e5-856f-ba37aa66c4bb.png)

### License
The MIT License (MIT)

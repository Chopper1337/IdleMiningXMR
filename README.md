# Idle Mining XMR

Python script which runs XMRig only when your PC has been idle for a specified amount of time.

No Windows version available and I do not have plans to make one.

## Requirements

* Python

* X11 (Unless `xprintidle` works on Wayland somehow)

* XMRig

* `xprintidle`

## Setup

* Create a configuration file for XMRig. ([Wizard](https://xmrig.com/wizard))

* Download the script (clone the repo or direct download)

## Usage

**Note that time is provided in seconds.**

`./IdleMiningXMR.py <idle time> <check delay> </path/to/config.json>`

Example:

Run XMRig when the system has been idle for 5 minutes (300 seconds). Check how long the system has been idle every minute (60 seconds).

`./IdleMiningXMR.py 300 60 /path/to/config.json`


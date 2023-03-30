# Idle Mining XMR

Python script which runs XMRig when your system idle and stops it when it's not.

No Windows version available and I do not have plans to make one as this can be achieved using Task Scheduler.

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

Idle time: The amount of time the system must be idle before running XMRig.

Check delay: The delay between checks of the system's idle time.

Path to config: A full or relative path to your XMRig configuration.

Example:

Run XMRig when the system has been idle for 5 minutes (300 seconds). Check how long the system has been idle every minute (60 seconds).

`./IdleMiningXMR.py 300 60 /path/to/config.json`


#!/usr/bin/env python3

import os
import sys
import time

# Start miner
def start():
    print( current_time() + "Starting miner...")
    os.system("xmrig -c " + config_path + " & disown")
    print( current_time() + "Miner started")

# Stop miner
def stop():
    print( current_time() + "Stopping miner...")
    os.system("killall xmrig")
    print( current_time() + "Miner stopped")

# Determine the period of time the PC has been idle
def idle_time():
    # Get the time the PC has been idle
    idle_time = int(os.popen("xprintidle").read())

    # Convert the time to seconds
    idle_time = idle_time / 1000
    print( current_time() + "Idle time: " + str(idle_time) + " seconds")

    # Return the time
    return idle_time

# Check if the miner is running
def is_running():
    # Get the output of the ps command
    output = os.popen("ps -A").read()
    return "xmrig" in output

def current_time():
        return time.strftime("[%H:%M %Y-%m-%d]", time.localtime()) + " "

# Main

# Take the config path as an argument
if len(sys.argv) != 4:
    print("[ERROR] Invalid arguments.\nUsage: IdleMiningXMR.py <idle time> <check delay> <config path>\n\nExample: IdleMiningXMR.py 300 60 /home/user/.config/xmrig/config.json\nThis would start the miner if the PC has been idle for 5 minutes (300 seconds) and would run the idle time check every minute (60 seconds)")
    exit()

# Set the idle time
time_idle = int(sys.argv[1])

# Set the check delay
delay = int(sys.argv[2])

# Set the config path
config_path = sys.argv[3]

# If the config path does not exist
if os.path.exists(config_path) == False:
    # Print an error message
    print("[ERROR] Config path does not exist")

    # Exit
    exit()

# Run in a loop
while True:

    # If the PC has been idle for X minutes
    if idle_time() > time_idle:
        # If the miner is not running
        if is_running() == False:
            # Start the miner
            start()
        else:
            # Indicate that the miner is already running
            print( current_time() + "Miner is already running")

    # If the PC has not been idle for X minutes
    else:
        # If the miner is running
        if is_running() == True:
            # Stop the miner
            stop()

    # Wait
    time.sleep(delay)

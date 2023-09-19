#!/usr/bin/env python

# Inspired by two talks at DEF CON 31 by Null Agent and Sally, who makes yachts.

# This is a simple script that plays a sound when it detects Axon law enforcement
# equipment; in theory, this includes holsters, bodycams, tasers, etc. They're putting
# tasers on drones next, so we have that to look forward to... It works by using
# BleakScanner (https://pypi.org/project/bleak/) to scan for nearby BLE devices
# that use the organizationally unique identifier (OUI) 00:25:DF. It logs the MAC
# address and time of encounter in cops.log. The range is your Bluetooth range.

import asyncio
import datetime
import os
import bleak
import sys

# 00:25:df is the OUI for Taser International Inc aka Axon. If you're trying to detect another organization, change here.
oui = "00:25:DF"

devices = []

async def scan_for_devices():
    while True:
        current_time = get_current_time()
        sys.stdout.write(f"\rScanning... (Last Scan: {current_time}, Devices In Range: {len(devices)})")
        sys.stdout.flush()

        scanned_devices = await bleak.BleakScanner.discover()
        devices.clear()
        for device in scanned_devices:
            addr_str = device.address.upper()
            devices.append(addr_str)
            if addr_str.startswith(oui):
                notification_message = f"\n\033[1;31mLAW ENFORCEMENT NEARBY: \033[1;37m{addr_str}\033[0m (Time: {current_time})\033[0m"
                print(notification_message)
                log_event(notification_message)
                os.system('paplay /usr/share/sounds/YOUR_SOUND_PATH/YOUR_SOUND.oga') # Change this to whatever sound you'd like. Needs to be done before you'll get sound alerts.


        await asyncio.sleep(12)  # This is the wait between scans in seconds. Adjust as necessary.

def get_current_time():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def log_event(event):
    current_time = get_current_time()
    log_file_path = 'cops.log' # Path to the logfile, change as necessary.
    with open(log_file_path, 'a') as log_file:
        log_file.write(f"{event} (Logged: {current_time})")

if __name__ == "__main__":
    print("\033[1;31m")
    print(" ___                     ___                              ___      ")
    print("(   )                   (   )                            (   )     ")
    print(" | |    .--.     .--.    | |   ___     .--.    ___  ___   | |_     ")
    print(" | |   /    \   /    \   | |  (   )   /    \  (   )(   ) (   __)   ")
    print("\033[1;37m | |  |  .-. ; |  .-. ;  | |  ' /    |  .-. ;  | |  | |   | |      ")
    print(" | |  | |  | | | |  | |  | |,' /     | |  | |  | |  | |   | | ___  ")
    print(" | |  | |0 | | | |0 | |  | .  '.     | |  | |  | |  | |   | |(   ) ")
    print("\033[1;34m | |  | |  | | | |  | |  | | `. \    | |  | |  | |  | |   | | | |  ")
    print(" | |  | '  | | | '  | |  | |   \ \   | '  | |  | |  ; '   | ' | |  ")
    print(" | |  '  `-' / '  `-' /  | |    \ .  '  `-' /  ' `-'  /   ' `-' ;  ")
    print("(___)  `.__.'   `.__.'  (___ ) (___)  `.__.'    '.__.'     `.__.   ")
    print("                                                       \033[1;37mv\033[1;34m0.\033[1;31m9\033[0m")
    print("\nInspired by two talks at DEF CON 31 by Null Agent and Sally, who makes yachts.")
    print("Short range (BLE) scanner that picks up Axon police equipment and alerts with a sound.")

    print("\nPress \033[1;34mEnter\033[0m to start or \033[1;31mQ\033[0m to quit: ")

    try:
        while True:
            user_input = input()
            if user_input.lower() == "q":
                print("\033[1;31mQuitting\033[0m...")
                sys.exit(0)
            else:
                asyncio.run(scan_for_devices())
    except KeyboardInterrupt:
        print("\n\033[0m * Interrupted.")

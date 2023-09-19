# Lookout.py - police detector
## About:
I watched two fun talks back-to-back from DEF CON 31 online: [Nosy Cops: Exposing The Hidden Potential of Police Radio](https://www.reconvillage.org/talks-recon-village-defcon-31/nosy-cops%3A-exposing-the-hidden-potential-of-police-radio) and [Snoop Unto Them, As They Snoop Unto Us](https://blog.dataparty.xyz/blog/snoop-unto-them/). This is a simple script to let you know who is around you. While not nearly as interesting or useful as either [sally, who sells yachts](https://www.atlscanner.com/)' or [Null Agent]'s(https://rfparty.xyz) projects, I thought someone else might want this script.

It's a short range (BLE, max 300ft in optimal conditions) police detector. A super simple Python script that uses [BleakScanner](https://pypi.org/project/bleak/) to discover nearby Bluetooth Low Energy devices. If any of those devices use the organizationally unique identifier (OUI) 00:25:df, which belongs to $16 billion police equipment manufacturer Axon, it plays a sound and records the event with a MAC address in cops.log. This means if someone with an Axon bodycam, taser, holster or Axon Signal Vehicle is within BLE range of the system you're running the script on it will trigger an "alert."

Your actual range is going to depend on a lot of factors like receiver sensitivity, antenna gain and path loss. Anecdotally, sitting in my living room with a cheap laptop running Linux and a $13 USB Bluetooth adapter I can pick up police devices ~100' away, across the street and through horsehair plaster walls. You can edit the 'oui' variable to detect other company's devices instead.

## Before You Run:
For Arch:
`sudo pacman -S python-bleak`
or pip
`pip install bleak`

The script uses paplay to play a sound on ln 38. If you use PulseAudio, just change the path to an appropriate sound file. Alternatively, you can edit this to use beep, or whatever command will play a sound on your system. Or just comment it out for a quiet script; it'll still display the devices and log events.

## Then:
`python lookout.py`

Hit Enter and it will begin scanning. It rests 12 seconds after every scan, which can be changed in the source code. In addition to the time of last scan, it also displays the total number of BLE devices last detected, in the terminal. This is mostly to make sure the script is functioning as intended. If it's been a few scans and you're still showing Devices In Range: 0 (when it shouldn't be), try turning it off and on again. lol

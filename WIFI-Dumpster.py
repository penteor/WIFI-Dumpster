#!/usr/bin/python

import os, re
import plistlib # Generate and parse Mac OS X .plist files¶

# Add a list with networks that you never want to delete from list
WhiteNetworks = []

# Check if script is running as root
if os.getuid() !=0:
    print('[!] Run script as root.')

# List all interaces
ListInterfaces=os.popen("/usr/sbin/networksetup -listallhardwareports").read()


if 'Wi-Fi' not in ListInterfaces:
    print('[!] No Wireless Interface detected.')
    exit()

try:
    with open("/Library/Preferences/SystemConfiguration/com.apple.airport.preferences.plist", 'rb') as f:
        ListNetworks = plistlib.load(f)["KnownNetworks"]
except Exception as err:
    print(str(err))


print('\n' * 2 + '____ List All Connected Networks ____')
OpenSSIDs = []
AllSSIDs = []
for entry in ListNetworks:
    Name = ListNetworks["{0}".format(entry)]
    print("[*] SSID:{0} - Encryption:{1}".format(Name["SSIDString"], Name["SecurityType"]))
    AllSSIDs.append(Name["SSIDString"])
    if (Name["SecurityType"] == "Open"):
        OpenSSIDs.append(Name["SSIDString"])

print('\n' * 5 + '____ Remove from Whitelist or Open Networks ____')
for SSID in AllSSIDs:
    if (SSID not in WhiteNetworks) or (SSID in OpenSSIDs):
        print('[!] Removing {0} network.'.format(SSID))
        #os.popen("/usr/sbin/networksetup -removepreferredwirelessnetwork en0 " +  SSID)


print('\n' * 5 + '____ Scan Air  ____')
out = os.popen("/System/Library/PrivateFrameworks/Apple80211.framework/Versions/A/Resources/airport scan").read()
print(out)

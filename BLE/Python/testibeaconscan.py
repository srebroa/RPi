# test BLE Scanning software
# jcs 6/8/2014

import ibeaconscan
import sys

import bluetooth._bluetooth as bluez

dev_id = 0
try:
	sock = bluez.hci_open_dev(dev_id)
	print "ble thread started"

except:
	print "error accessing bluetooth device..."
    	sys.exit(1)

ibeaconscan.hci_le_set_scan_parameters(sock)
ibeaconscan.hci_enable_le_scan(sock)

while True:
	returnedList = ibeaconscan.parse_events(sock, 10)
	print "----------"
	for beacon in returnedList:
		print beacon


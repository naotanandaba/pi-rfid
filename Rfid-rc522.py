#!/usr/bin/env python

import RPi.GPIO as GPIO
import os
from mfrc522 import SimpleMFRC522

class Rfid_rc522:
        # return uid in hexa str
        def read_uid(self):
                reader = SimpleMFRC522()
                uid = reader.read_uid()
                uid_hex = hex(uid).upper()
                return uid_hex
if __name__ == "__main__":
# rf = Rfid...()
        try:
                rf = Rfid_rc522()
                uid = rf.scan_uid()
	finally:
		GPIO.cleanup()


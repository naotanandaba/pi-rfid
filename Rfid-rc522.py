
#!/usr/bin/env python

import RPi.GPIO as GPIO
import os
from mfrc522 import SimpleMFRC522

class Rfid_rc522:
        def read_uid(self):
                reader = SimpleMFRC522()
                uid = reader.read_uid()
                uid_hex = hex(uid).upper()
                return uid_hex
if __name__ == "__main__":
	str=""
	while(str!="\n"):
		os.system("clear")
		try:
			print("Scan your card","\t")
			rf = Rfid_rc522()
			uid = rf.scan_uid()
			print("Your card number is:","\t")
			print(uid.strip("0X"),"\t")
		finally:
			str="\n"
			str = input("Scan again")
			GPIO.cleanup()

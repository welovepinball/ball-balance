This arduino sketch can be loaded onto an Arduino Mega2560 to turn it into a HID Keyboard.

The sketch turns inputs 2-53 into keyboard keystrokes by grounding the pin.

The onboard USB firmware has to be flashed to a HID firmware.  The firmware and additional information can be downloaded from:
https://github.com/harlequin-tech/arduino-usb

Make sure to put the device in DFU mode for flashing the firmware by momentarily bridging the 2 pins closest to the USB port (in the 6-pin header).
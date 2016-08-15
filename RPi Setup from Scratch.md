These are directions for setting up the RPi from scratch.

Start with the lite version here, save it to an SD card, and insert into RPi:
https://www.raspberrypi.org/downloads/raspbian/

Turn it on and at first it may need to do something to resize if the SD card is larger than the image. This seemed to turn the RPi off when finished and I had to unplug and plug it back in to boot.

Get it booted.
Login credentials: pi/raspberry

-Set up wifi - open wpa_supplicant.conf in the nano editor with the following command:
sudo nano /etc/wpa_supplicant/wpa_supplicant.conf

-add the following to the bottom of the file, replacing SSID and password with your wifi credentials:
network={
ssid="YOUR_SSID"
psk="YOUR_PASSWORD"
}

-CTRL+X to exit. Y save changes and exit.

-Reboot:
sudo reboot

-Log back in after reboot.

-Check that wifi is working:
ifconfig wlan0

-It should show an ip address by "inet addr:"

-You can also ping google.com to verify wifi:
ping -c 4 google.com

At this point you can SSH into the RPi from another computer using an application like PuTTy.  You just need to know the IP address of the RPi.  Using an SSH client will allow you to copy/paste commands remotely.

-Install Python3, agreeing to any prompts:
sudo apt-get install python3

-Install Pygame, agreeing to any prompts:
sudo apt-get install python3-pygame

-Install Git, agreeing to any prompts:
sudo apt-get install git

-Install FadeCandy server using directions on this page:
https://learn.adafruit.com/1500-neopixel-led-curtain-with-raspberry-pi-fadecandy/fadecandy-server-setup

-Download the latest repository for our ICB type game, and it ends up in a directory named "ball-balance":
git clone https://github.com/welovepinball/ball-balance.git

-Navigate to ball-balance directory:
cd ball-balance

-Run game (Escape to exit):
python3 game.py 
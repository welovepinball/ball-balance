# Setting up the RPi from scratch

## Configure OS and Wi-Fi

1. Start with the lite version here, save it to an SD card, and insert into RPi:
https://www.raspberrypi.org/downloads/raspbian/

2. Turn it on and at first it may need to do something to resize if the SD card is larger than the image. This seemed to turn the RPi off when finished and I had to unplug and plug it back in to boot.

3. Get it booted.
   Login credentials: pi/raspberry

4. Set up Wi-Fi - open wpa_supplicant.conf in the nano editor with the following command:
   ```sh
   sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
   ```

5. Add the following to the bottom of the file, replacing SSID and password with your wifi credentials:
   ```
   network={
       ssid="YOUR_SSID"
       psk="YOUR_PASSWORD"
   }
   ```
6. CTRL+X to exit. Y save changes and exit.

7. Reboot:
   ```sh
   sudo reboot
   ```
8. Log back in after reboot.

9. Check that wifi is working:
   ```sh
   ifconfig wlan0
   ```
   It should show an ip address by "inet addr:"

   You can also ping google.com to verify wifi:
   ```sh
   ping -c 4 google.com
   ```

## Install Git, Python, PyGame, and ball-balance

At this point you can SSH into the RPi from another computer using an application like PuTTy.  You just need to know the IP address of the RPi.  Using an SSH client will allow you to copy/paste commands remotely.

1. Install Python3, agreeing to any prompts:
   ```sh
   sudo apt-get install python3
   ```

2. Install Pygame, agreeing to any prompts:
   ```sh
   sudo apt-get install python3-pygame
   ```

3. Install Git, agreeing to any prompts:
   ```sh
   sudo apt-get install git
   ```

4. Install FadeCandy server using directions on this page:
   https://learn.adafruit.com/1500-neopixel-led-curtain-with-raspberry-pi-fadecandy/fadecandy-server-setup

5. Download the latest repository for our ICB type game, and it ends up in a directory named "ball-balance":
   ```sh
   git clone https://github.com/welovepinball/ball-balance.git
   ```

6. Navigate to ball-balance directory:
   ```sh
   cd ball-balance
   ```

7. Run game (Escape to exit):
   ```sh
   python3 game.py 
   ```

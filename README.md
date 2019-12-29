RFID Reader on Raspberry Pi

This program uses the Sunfounder RFID-RC522

Prior to running Need to run:
pip3 install pyusb spidev mfrc522

raspi-config nonint do_spi 0&&reboot

Pinout:

Pin 1 VCC
Pin22 RST
Pin 9 GND
Pin21 MISO
Pin19 MOSI
Pin23 SCK
Pin24 NSS

IRQ unused)

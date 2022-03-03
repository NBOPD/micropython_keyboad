from machine import Pin,SoftI2C
import ssd1306
import keyboard
i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=100000)
lcd=ssd1306.SSD1306_I2C(128,64,i2c)
k=keyboard.keyboard(lcd,entry=True)
k.init()
lcd.show()
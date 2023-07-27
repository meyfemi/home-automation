from my_ip_address import ip_address, device_id, local_key
import tinytuya
import time
import random

d = tinytuya.BulbDevice(device_id, ip_address, local_key)
d.set_version(3.3)
data = d.status()

#generate random colours
def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    d.set_colour(r, g, b, nowait=True)

n = 0
while n <= 20:
    random_colour()
    time.sleep(.5)
    print(n)
    n += 1

print(" back to white ")
d.set_white(225, 225)

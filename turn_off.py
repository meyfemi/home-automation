from my_ip_address import ip_address, device_id, local_key
import tinytuya

d = tinytuya.OutletDevice(device_id, ip_address, local_key)
d.set_version(3.3)
data = d.status()

switch_state = data['dps']['0']
if switch_state:
    d.turn_off()
else:
    d.turn_on()


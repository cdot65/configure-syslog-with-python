from jnpr.junos import Device
from jnpr.junos.utils.config import Config


inventory = [
    'office.dmz.home',
    'office-acx.dmz.home',
    'office-firewall.dmz.home',
    'firewall.dmz.home',
    'garage.dmz.home',
    'gaming.dmz.home',
    'closet.dmz.home'
]

for each_device in inventory:
    device_connection = Device(host=each_device, user='automation', password='juniper123').open()

    with Config(device_connection, mode='exclusive') as device_config:
        device_config.load('set system syslog host 192.168.105.9 kernel warning', format='set')
        device_config.pdiff()
        device_config.commit(timeout=300)

    device_connection.close()

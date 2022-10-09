""" 
    Simple Gamepad to MQTT interface
    Coded by Davide Caminati 10/2022 
    for Luca "Smanettone"
    under MIT licence
    
    
    Prerequisite
    pip install inputs 
    pip install paho-mqtt
    #pip install vgamepad
    git clone https://github.com/piborg/Gamepad
"""

from __future__ import print_function
import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
import time

from inputs import get_gamepad

def pubblica(topic, valore):
    try:
        publish.single(topic=topic, payload=valore, qos=0, retain=False, hostname="192.168.200.23",
                       port=1883, client_id="siemens-", keepalive=60, will=None,
                       tls=None, protocol=mqtt.MQTTv311, transport="tcp")
        print(valore)
    except:
        print("ERRORE in pubblica")
        
def main():
    """Just print out some event infomation when the gamepad is used."""
    while 1:
        events = get_gamepad()
        for event in events:
            if event.ev_type == "Key":
                if event.state == 1:
                    print("1")
                    pubblica(event.ev_type, event.state)
                    time.sleep(0.01)
                elif event.state == 0:
                    print ("0")
                    pubblica(event.ev_type, event.state)
                    time.sleep(0.01)
            
            #print(event.ev_type, event.code, event.state)


if __name__ == "__main__":
    main()

import paho.mqtt.client as mqtt
import time
import json
import paho.mqtt.publish as publish

client_name = 'random'

client = mqtt.Client(client_name)

client.connect('127.0.0.1')
client.subscribe('devices/radebe/32323/mt')

def send_message(client, userdata, message):
    msg = json.loads(str(message.payload.decode('UTF-8')))
    t = m['data']['temperature']
    print(t.encode)

    if t > 30:
        print('temp')


client.on_message = send_message
time.sleep(120)


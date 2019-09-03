import paho.mqtt.client as mqtt
import time

HOST = "192.168.0.20"
TOPIC_1 = "DATA"

print("\nDAQC Server Ready")
print("Waiting to Establish Connection")

def on_connect(client, userdata, flags, rc):
    print("Connected with result code: " + str(rc))
    error = rc
    return error

def on_disconnect(client, userdata, rc=0):
    print("Connection Lost")
    client.loop_stop()

def on_message(client, userdata, msg):
    raw = str(msg.payload)[2:-1] 
    data = raw.split(',')
    
    for i in range(0, len(data)):
        data[i] = data[i].lstrip(" ")
    
    data[-1] = data[-1].rstrip("\\n")

    print(data)
    

    
client = mqtt.Client()    
client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect
client.connect(HOST, 1883, 60)


client.subscribe(TOPIC_1)

print("Connection Established")

client.loop_forever()

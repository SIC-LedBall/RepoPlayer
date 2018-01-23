import paho.mqtt.client as mqtt

topic = "LedBall"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(topic)
    client.publish("LedBall", "Start Publishing Retard PI")

def on_message(client, userdata, msg):
    #print(msg.topic + " " + str(msg.payload))
    client.publish("LedBall","x=1,y=2")

client = mqtt.Client()
client.connect("192.168.1.105", 1883, 60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()


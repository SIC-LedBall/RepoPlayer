#!/usr/bin/env python
import rospy
from std_msgs.msg import String

#MQTT
import paho.mqtt.client as mqtt
topic = "ledball"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(topic)
    client.publish("ledball", "Starting location")

# def on_message(client, userdata, msg, data):
#     #print(msg.topic + " " + str(msg.payload))
#     client.publish("LedBall",data.data)

#ROS LOCATION ESTIMOTE
def callback(data):
    rospy.loginfo(data.data)
    rospy.loginfo(rospy.get_caller_id() + " [Robotics Indoor SDK] x, y = %s", data.data)
    client.publish("ledball", data.data)

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("estimote_position", String, callback)
    rospy.spin()

client = mqtt.Client()
client.connect("192.168.1.103", 1883, 60)

client.on_connect = on_connect

if __name__ == '__main__':
    listener()
    #client.on_message = on_message


#client.loop_forever()
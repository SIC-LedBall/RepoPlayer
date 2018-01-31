import time
from neopixel import *
import paho.mqtt.client as mqtt

# LED strip configuration:
LED_COUNT      = 24      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 100     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0
LED_STRIP      = ws.SK6812_STRIP_RGBW
#LED_STRIP      = ws.SK6812W_STRIP

# Create NeoPixel object with appropriate configuration.
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
# Intialize the library (must be called once before other functions).
strip.begin()

alive = True
lives = 4

topicPlayer1 = "lbplayer1"

def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()

def on_connect(client, userdate, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(topicPlayer1)

#Test msg = hit;3
def on_message(client, userdate, msg):
    if(msg.topic == topicPlayer1):
        payload = msg.payload
        print(msg.topic + " - " + payload)
        lstPayload = payload.split(";")

        if lstPayload[0] == "hit":
            lives = lstPayload[1]

            if lives == "3":
                colorWipe(strip, Color(255, 0, 0))
            if lives == "2":
                colorWipe(strip, Color(153, 255, 0))
            if lives == "1":
                colorWipe(strip, Color(0, 255, 0))
            if lives == "0":
                for i in range(4):
                    colorWipe(strip, Color(0, 255, 0))
                    time.sleep(0.3)
                    colorWipe(strip, Color(0, 0, 0))
                    time.sleep(0.3)
                alive = False

            if lives == "c":
                alive = False

client = mqtt.Client()
client.connect("192.168.1.200", 1883, 60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()

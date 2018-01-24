import time
from neopixel import *

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

alive = True

def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()

# def resetLeds(ring, color, wait_ms=10):
#
#     for i in range(ring.numPixels()):
#         ring.setPixelColor(i, color)
#         ring.show()


# Create NeoPixel object with appropriate configuration.
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
# Intialize the library (must be called once before other functions).
strip.begin()

while alive:
    lives = input("lives?")
    if lives == 3:
        colorWipe(strip, Color(255, 0, 0))
    if lives == 2:
        colorWipe(strip, Color(153, 255, 0))
    if lives == 1:
        colorWipe(strip, Color(0, 255, 0))
    if lives == 0:
        for i in range(4):
            colorWipe(strip, Color(0, 255, 0))
            time.sleep(0.3)
            colorWipe(strip, Color(0, 0, 0))
            time.sleep(0.3)
        alive = False

    if lives == "c":
        alive = False
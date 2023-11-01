# from codelab_adapter_client import send_message
import paho.mqtt.client as mqtt
from octostudio import OctoStudio

# https://adapter.codelab.club/extension_guide/iot/

mqtt_client = mqtt.Client()
mqtt_client.username_pw_set('guest', 'test')
mqtt_client.connect("mqtt.aimaker.space", 1883, 60)

def on_message(shape):
    # send_message(shape)
    mqtt_client.publish("octo_message", shape)

def main():
    print("🐱 ❤️  🐙")
    octo = OctoStudio()
    octo.on_message = on_message
    octo.start()

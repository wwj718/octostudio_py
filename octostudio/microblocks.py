from microblocks_wifi_radio import Radio
from octostudio import OctoStudio

microblocks_radio = Radio(receive_message=False)

def on_message(shape):
    microblocks_radio.send_string(shape)

def main():
    print("🐰 ❤️  🐙")
    octo = OctoStudio()
    octo.on_message = on_message
    octo.start()
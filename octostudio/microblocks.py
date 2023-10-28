from microblocks_wifi_radio import Radio
from octostudio import OctoStudio

microblocks_radio = Radio(receive_message=False)

def on_message(shape_id):
    microblocks_radio.send_string(shape_id)

def main():
    print("🐰 ❤️  🐙")
    octo = OctoStudio()
    octo.on_message = on_message
    octo.start()
from datetime import datetime
from adafruit_ble import BLERadio

radio = BLERadio()
received_ids = set()

class OctoStudio:
    def __init__(self):
        self.on_message = None
        self._shape_map = {
            "00000000": "circle",
            "00000001": "square",
            "00000002": "star",
            "00000003": "heart",
            "00000004": "triangle",
        }

    def start(self):
        print("Start scanning...")
        for entry in radio.start_scan():  # timeout=10, minimum_rssi=-80
            # addr = entry.address
            name = entry.complete_name
            # print(entry.address, entry.data_dict)
            # if addr not in found or True:
            if (
                name not in [None, "0" * 16]
                and len(name) == 16
                and name not in received_ids
            ):
                shape_id = self._shape_map.get(name[8:], None)
                if shape_id:
                    now = datetime.now()
                    timestamp = now.strftime("%H:%M:%S.") + f"{now.microsecond // 100000:1d}"
                    print(shape_id,  timestamp)
                    if callable(self.on_message):
                        self.on_message(shape_id)
                    received_ids.add(name)
                # IPython.embed(); break

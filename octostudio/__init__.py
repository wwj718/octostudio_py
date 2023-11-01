import asyncio
from datetime import datetime
from bleak import BleakScanner

class OctoStudio:
    def __init__(self):
        self.on_message = None
        self._octo_uuids = {
            "iOS": "2540b6b0-0002-4538-bcd7-7ecfb51297c1",
            "Andriod": "2540b6b0-0001-4538-bcd7-7ecfb51297c1",
        }
        self._shape_map = _shape_map = {
            "0": "circle",
            "1": "square",
            "2": "star",
            "3": "heart",
            "4": "triangle",
        }
        self._received_datas = set()
        self._stop_event = asyncio.Event()

    def detection_callback(self, device, advertisement_data):
        shape_id = None
        if advertisement_data.local_name:
            data = advertisement_data.local_name
            if (
                data not in [None, "0" * 16]
                and len(data) == 16
                and data not in self._received_datas
            ):
                # iOS
                shape_id = data[-1]

        if advertisement_data.service_data:
            data = advertisement_data.service_data.get(self._octo_uuids["Andriod"])
            if data and len(data) == 13 and data not in self._received_datas:  # bytes
                # Android
                shape_id = str((data[7]))  # 3

        if shape_id:
            now = datetime.now()
            timestamp = now.strftime("%H:%M:%S.") + f"{now.microsecond // 100000:1d}"
            shape = self._shape_map.get(shape_id)
            print(shape, timestamp)
            if callable(self.on_message):
                self.on_message(shape) # TODO: pass more data: device, advertisement_data
                self._received_datas.add(data)

    async def scan(self):
        # TODO: add something that calls stop_event.set()
        # Maximum rate that advertisements can be scanned/read: https://github.com/hbldh/bleak/discussions/831
        # https://github.com/hbldh/bleak/issues/394
        async with BleakScanner(
            # self.detection_callback, service_uuids=self._octo_uuids.values() 
            # In order to be compatible with Windows & Android combination, do not use service_uuids
            self.detection_callback
        ) as scanner:
            await self._stop_event.wait()

    def stop(self):
        self._stop_event.set()

    def start(self):
        asyncio.run(self.scan())

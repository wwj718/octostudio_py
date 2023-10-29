# OctoStudio

WARNING⚠️ : only tested on windows 11, MacOS and iPhone(Android may not work). More compatibility work is in progress. If you encounter problems, please provide feedback.

This Python library pass messages between Python and [OctoStudio](https://octostudio.org/en/).

Specifically, it works with two blocks of OctoStudio:

- beam to phones
- wait for beam (work-in-progress)


<img width=300 src="./octostudio.png" />


## Install

```
pip install octostudio
```

## Usage

```
from octostudio import OctoStudio

def on_message(shape_id):
    print(shape_id)

octo = OctoStudio()
octo.on_message = on_message
octo.start()
```


## For MicroBlocks users

This library was originally used to bridge OctoStudio's Bluetooth radio with MicroBlocks' wifi radio.

To do this you need to install this package, then run the command: `octostudio-microblocks-bridge`

Take a look at the [inner workings](./octostudio/cli.py)

## For Scrarch users

Install dependencies:

```bash
pip install paho-mqtt octostudio
``` 

run the command: `octostudio-scratch-bridge`

Open [the demo project](https://create.codelab.club/projects/57459/editor/)


### Customize

octostudio-scratch-bridge uses the default MQTT broker and account. Other users may also be using it. If you want to use your own broker and account, you can run the following code instead of the default octostudio-scratch-bridge:

```python
# custom octostudio-scratch-bridge
import paho.mqtt.client as mqtt
from octostudio import OctoStudio

mqtt_client = mqtt.Client()
# You can use other MQTT broker. If you want to use it with Scratch, make sure the MQTT broker supports wss protocol
mqtt_client.username_pw_set('guest', 'test')
mqtt_client.connect("mqtt.aimaker.space", 1883, 60)

def on_message(shape_id):
    mqtt_client.publish("octo_message", shape_id)
octo = OctoStudio()
octo.on_message = on_message
octo.start()
```

## For Snap! users

Install dependencies:

```bash
pip install paho-mqtt octostudio
``` 

run the command: `octostudio-snap-bridge`

Open [the demo project](https://snap.berkeley.edu/project?username=alan_russell&projectname=octostudio%2dsnap%2ddemo)
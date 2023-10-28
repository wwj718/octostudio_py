# OctoStudio

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

def main():
    octo = OctoStudio()
    octo.on_message = on_message
    octo.start()
```


## For MicroBlocks users

This library was originally used to bridge OctoStudio's Bluetooth radio with MicroBlocks' wifi radio.

To do this you need to install this package, then run the command: `octostudio-microblocks-bridge`

Take a look at the [inner workings](./octostudio/cli.py)
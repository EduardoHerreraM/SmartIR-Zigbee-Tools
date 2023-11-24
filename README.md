# SmartIR Zigbee Tools

This tool makes generating the SmartIR codes for a MQTT source easy and simple (for someone with a bit of experience in programming).

It uses `Python` and several packages for making this process less tedious.

My developing was done using a [`MOES UFO-R11`](https://www.zigbee2mqtt.io/devices/UFO-R11.html), `Mosquitto` and `Zigbee2MQTT`.

Feel free to perform a pull request for your feature! :)

## Project capabilities

Right now, the project only works with the following device types:

* `climate`

## System requisites

* Python 3.11 (most likely an older version works too, but needs tweaking the `pyproject.toml` file)
* A MQTT broker (this project provides default support to `Mosquitto`)
* Poetry (as the time of writing this, I've used `1.7.0`)

## Project requisites

When trying to use this project, you must create a new `Controller` class for your specific Zigbee controller.

You have my controller as an example. It's called `MOES_UFO_R11_Controller`.

You must define these two functions:

* `get_learning_mode_message` -> My controller needs an specific message for setting the controller as learning mode. Here you define the message that your controller needs.
* `extract_code_from_message` -> Here you extract the learnt code from the MQTT message. 

My controller payload looks like this:

```json
{
  "battery":36,
  "learn_ir_code":null,
  "learned_ir_code":"CdUR1REgAj4GIAJAAUAHQAPAAeATC8AbQAdAA0ABQAfgCQMCVwIgIAEDPgYgAuAPAeADG0ALwAPgAwHgExMB1RFAAQEgAkAjQAFAB0ADwAHgEwvAG0AHQANAAUAH4AsDQAFAF+APAeADG0ALwAPgAwHgEBMCBiAC",
  "linkquality":134,
  "voltage":1300
}
```

So my `extract_code_from_message` is extracting the value of the `learned_ir_code` field.

## Environment definition

This project needs several environment values for correctly working. Here is the specification:

* **BROKER_ADDRESS** *(string)* (required) -> The direction of your broker.
  * ex: `localhost`, `192.168.31.10`
* **BROKER_PORT** *(integer)* (required) -> Your broker connection port. The default for `Mosquitto` is `1883`.
  * ex: `1883`
* USERNAME -> *(string)* A valid username for your broker connection. `Mosquitto` requires one.
* PASSWORD -> *(string)* The password of the given username.
* **CONTROLLER_FRIENDLY_NAME** *(string)* (required) -> The user-friendly name that your controller devices has inside `Zigbee2MQTT`. This is used for setting the topic name.
  * ex: `IR Remote Living`, `Office IR`
* **MANUFACTURER** *(string)* (required) -> The manufacturer of your climate machine.
  * ex: `Samsung`
* **MODEL** *(string)* (required) -> Yur climate machine model.
  * ex: `AR09TXHQASIN`
* **MINIMUM_TEMPERATURE** *(float)* (required) -> The lowest temperature that your climate machine can go.
  * ex: `18.0`
* **MAXIMUM_TEMPERATURE** *(float)* (required) -> The highest temperature that your climate machine can go. 
  * ex: `30.0`
* **OPERATION_MODES** *(list of strings)* (required) -> The operation modes that your climate machine has. 
  * ex: `["auto", "cool", "dry", "heat"]`, `["cool", "heat"]`
* **FAN_MODES** *(list of strings)* (required) -> The fan modes that your climate machines has. Normally, it sets the speed. If you only have one, name it as you wish.
  * ex: `["auto", "low", "medium", "high"]`
* **SWING_MODES** *(list of strings)* (required) -> The swing modes that your climate machine has. If you have none or only one, name it as you wish.
  * ex: `["on"]`, `["off", "on"]`


## FAQ

### The output says that the learning mode is set, the climate controller is sending the codes, but the project is not registering them.

The cause of this could be one of the following:
* The broker server is not well set up. Check that your broker is accessible, and that the credentials are correct.
* The Zigbee controller has timed out. My `MOES UFO-R11` waits 10 seconds in learning mode before it changes to the operational mode.


## Improvements
- [] Set a timer for deciding to retry setting the controller to learning mode again
- [] Allow switching off the climate controller before trying to get the new set of commands if the something changes besides the temperature (more that 1 button has to be pressed)
- [] Include testing pipelines
- [] Detect when the broker configuration is not valid and alert the user
- [] Support `fan`
- [] Support `media_player`

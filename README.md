<p align="center">
  <img src="UI/icons/logo-icon.svg" alt="logo" width="100">
</p>

<strong>MQTT HUB</strong> is a fully open-source client designed to interact with different MQTT protocol versions. It serves as a powerful debugging tool for IoT services.

MQTT HUB has evolved into a practical and reliable solution for troubleshooting and testing MQTT-based applications.

    GUI built with PyQt5 for an intuitive user experience.
    The Paho library powers MQTT communication.

Whether you're a developer or an IoT enthusiast, MQTT HUB can help streamline your debugging workflow.

https://github.com/user-attachments/assets/85abbec3-e984-4d1a-9df0-c8f1229bc5a8

<strong>How to setup?</strong>

- for Linux, you can open the file ```Linux_mqtt_hub/mqtt_hub```, or write in terminal:
```sh
./Linux_mqtt_hub/mqtt_hub
```
- for macOS, you first need to grant your system permission to open the app:
```sh
sudo xattr -cr "path/to/repo/MacOS_mqtt_hub/MQTT Hub.app"
```
and then, you can simply open the app by double-clicking on: ```MacOS_mqtt_hub/MQTT HUB.app```.

<strong>And of course you can set it up directly from your IDE (the best way for now)</strong>:
```sh
python3 -m venv venv
source venv/bin/activate
.\venv\Scripts\activate
pip install -r requirements.txt
python3 ./main.py
```

<strong>Future updates:</strong>

- CSV logs format.

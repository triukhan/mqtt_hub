<p align="center">
  <img src="UI/icons/logo-icon.svg" alt="logo" width="100">
</p>

<strong>MQTT HUB</strong> is a fully open-source client designed for interacting with different versions of the MQTT protocol. It serves as a powerful debugging tool for IoT services.

MQTT HUB has evolved into a practical and reliable solution for troubleshooting and testing MQTT-based applications.

    GUI built with PyQt5 for an intuitive user experience.
    MQTT communication powered by the Paho library.

Whether you're a developer or an IoT enthusiast, MQTT HUB can help streamline your debugging workflow.

(the picture is clickable and leads to YouTube video presentation)

https://github.com/user-attachments/assets/85abbec3-e984-4d1a-9df0-c8f1229bc5a8

<strong>How to setup?</strong>

- for Linux, you can open the file ```Linux_matt_hub/mqtt_hub```, or write in terminal:
```sh
./Linux_mqtt_hub/mqtt_hub
```
- for macOS, you can open the file ```MacOS_mqtt_hub/MQTT HUB.app```.

<strong>And of course you can set it up directly from your IDE (the best way for now)</strong>:
```sh
python3 -m venv venv
source venv/bin/activate
.\venv\Scripts\activate
pip install -r requirements.txt
python3 ./main.py
```

<strong>Future updates:</strong>

- GUI support for Linux systems.
- CSV logs format.

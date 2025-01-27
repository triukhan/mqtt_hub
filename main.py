from mqtt.connector import MQTTConnector

if __name__ == '__main__':
    mqtt = MQTTConnector(
        [
            'dt/smartis/ajax/hub/00186A94',
            'cmd/smartis/ajax/hub/00186A94/res',
            'cmd/smartis/ajax/hub/',
        ]
    )
    mqtt.start()

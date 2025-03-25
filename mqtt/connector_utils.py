import base64
import binascii
import json

from paho.mqtt.client import MQTTv5

from settings.profile import Profile


def convert_to_format(payload, form):
    if form == 'Plaintext':
        return payload

    if form == 'JSON':
        try:
            json_obj = json.loads(payload)
            return json.dumps(json_obj, indent=4)
        except json.JSONDecodeError:
            return payload

    if form == 'Hex':
        return binascii.hexlify(payload.encode()).decode()

    if form == 'Base64':
        return base64.b64encode(payload.encode()).decode()

    return payload


def validate_start(profile: Profile):
    if not profile.host:
        return 'Error: Host is absent is settings'
    if not profile.port:
        return 'Error: Port is absent is settings'
    if not profile.client_id and profile.mqtt_version != MQTTv5:
        return 'Error: Client ID is absent is settings'
    if profile.self_signed and '' in (
        profile.ca_file,
        profile.crt_file,
        profile.key_file,
    ):
        return 'Error: Some certificates are absent is settings'
    return None

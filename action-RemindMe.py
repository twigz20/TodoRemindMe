#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from hermes_python.hermes import Hermes

MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))


def intent_received(hermes, intent_message):
    sentence = 'You asked for remind me'

    if intent_message.intent.intent_name == 'RemindMe':
        print('RemindMe')
        sentence += ' remind me '

    hermes.publish_end_session(intent_message.session_id, sentence)


with Hermes(MQTT_ADDR) as h:
    h.subscribe_intents(intent_received).start()
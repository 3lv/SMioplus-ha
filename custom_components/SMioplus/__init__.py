"""Sequent Microsystems Home Automation Integration"""

import logging
import voluptuous as vol

from homeassistant.helpers import config_validation as cv
from homeassistant.const import (
	CONF_NAME
)
CONF_NAME = CONF_NAME
CONF_STACK = "stack"
CONF_TYPE = "type"
CONF_CHAN = "chan"

DOMAIN = "SMioplus"
NAME_PREFIX = "smio"
SM_MAP = {
    "sensor":  {
        "opto": {
                "chan_no": 8,
                "uom": "",
                "com": {
                    "get": "getOptoCh",
                },
                "icon": {
                    "on": "mdi:mdi-numeric",
                    "off": "mdi:mdi-numeric"
                }
        },
        "adc": {
                "chan_no": 8,
                "uom": "V",
                "com": {
                    "get": "getAdcV",
                },
                "icon": {
                    "on": "mdi:flash-triangle",
                    "off": "mdi:flash-triangle"
                }
        },
    },
    "switch": {
        "relay": {
                "chan_no": 8,
                "com": {
                    "get": "getRelayCh",
                    "set": "setRelayCh"
                },
                "icon": {
                    "on": "mdi:toggle-switch-variant",
                    "off": "mdi:toggle-switch-variant-off",
                }
        }
    },
    "number": {
        "dac": {
                "chan_no": 4,
                "uom": "V",
                "min_value": 0.0,
                "max_value": 10.0,
                "step": 0.01,
                "com": {
                    "get": "setDacV", # TODO: CHANGE THIS TEMPORARY SOLUTION
                    "set": "setDacV"
                },
                "icon": {
                    "on": "mdi:flash-triangle",
                    "off": "mdi:flash-triangle"
                }
        },
    },
}


CONFIG_SCHEMA = vol.Schema({
    DOMAIN: vol.Schema(vol.Any([vol.Schema({
        vol.Optional(CONF_STACK, default="0"): cv.string,
    }, extra=vol.ALLOW_EXTRA)], {}))
}, extra=vol.ALLOW_EXTRA)

_LOGGER = logging.getLogger(__name__)

def load_platform(hass, entity_config):
        for platform_type, attr in SM_MAP.items():
            if entity_config[CONF_TYPE] in attr:
                hass.helpers.discovery.load_platform(
                        platform_type, DOMAIN, entity_config, entity_config
                )

def load_all_platforms(hass, stack=0):
    for platform_type, platform in SM_MAP.items():
        for type, attr in platform.items():
            if attr.get("optional", False):
                continue
            for chan in range(int(attr["chan_no"])):
                entity_config = {
                        CONF_NAME: NAME_PREFIX+str(stack)+"_"+type+"_"+str(chan+1),
                        CONF_STACK: stack,
                        CONF_TYPE: type,
                        CONF_CHAN: chan+1
                }
                hass.helpers.discovery.load_platform(
                        platform_type, DOMAIN, entity_config, {}
                )


def setup(hass, config):
    hass.data[DOMAIN] = []
    card_configs = config.get(DOMAIN)
    if not card_configs:
        load_all_platforms(hass, stack=0)
        return True
    for card_config in card_configs:
        stack = int(card_config.pop(CONF_STACK, 0))
        if not card_config:
            load_all_platforms(hass, stack=stack)
            continue
        for entity in card_config:
            try:
                [type, chan] = entity.rsplit("_", 1)
                chan = int(chan)
            except:
                _LOGGER.error(entity, " doesn't respect type-chan format")
                continue
            entity_config = card_config[entity] or {}
            entity_config |= {
                    CONF_NAME: NAME_PREFIX + str(stack) + "_" + entity,
                    CONF_STACK: stack,
                    CONF_TYPE: type,
                    CONF_CHAN: chan
            }
            load_platform(hass, entity_config)
        
    return True

DEFAULT_ICONS = {
        "off": "mdi:button-pointer",
}

import voluptuous as vol
import libioplus as SMioplus
import logging
import time

from homeassistant.const import (
	CONF_NAME
)

from homeassistant.components.light import PLATFORM_SCHEMA
import homeassistant.helpers.config_validation as cv
from homeassistant.components.button import ButtonEntity
from homeassistant.helpers.entity import generate_entity_id

from . import (
        DOMAIN, CONF_STACK, CONF_TYPE, CONF_CHAN, CONF_NAME,
        SM_MAP
)
SM_MAP = SM_MAP["button"]

_LOGGER = logging.getLogger(__name__)

def setup_platform(hass, config, add_devices, discovery_info=None):
    # We want this platform to be setup via discovery
    if discovery_info == None:
        return
    # TODO CHECK IF ALREADY CONFIGURED FOR WHATEVER REASON
    add_devices([Button(
		name=discovery_info.get(CONF_NAME, ""),
        stack=discovery_info.get(CONF_STACK, 0),
        type=discovery_info.get(CONF_TYPE),
        chan=discovery_info.get(CONF_CHAN),
        hass=hass,
	)])

class Button(ButtonEntity):
    def __init__(self, name, stack, type, chan, hass):
        self._SM = SMioplus
        generated_name = DOMAIN + str(stack) + "_" + type + "_" + str(chan)
        self._unique_id = generate_entity_id("button.{}", generated_name, hass=hass)
        self._name = name or generated_name
        self._stack = int(stack)
        self._type = type
        self._chan = int(chan)
        com = SM_MAP[self._type]["com"]
        def _aux_SM_set(*args):
            return getattr(self._SM, com["set"])(self._stack, *args)
        self._SM_set = _aux_SM_set
        self._short_timeout = .05
        self._icons = SM_MAP[self._type].get("icon", DEFAULT_ICONS);
        self._icon = self._icons["off"]

    @property
    def unique_id(self):
        return self._unique_id

    @property
    def name(self):
        return self._name

    @property
    def icon(self):
        return self._icon

    def press(self, **kwargs):
        try:
            self._SM_set(self._chan)
        except Exception as ex:
            _LOGGER.error(DOMAIN + " %s turn ON failed, %e", self._type, ex)
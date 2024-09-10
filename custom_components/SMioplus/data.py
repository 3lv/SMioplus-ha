DOMAIN = "SMioplus"
NAME_PREFIX = "smio"
SM_MAP = {
    "button": {
        "opto_cnt_rst": {
            "chan_no": 8,
            "com": {
                "set": "rstOptoCount",
            },
            "icon": {
                "on": "mdi:mdi-button-pointer",
                "off": "mdi:mdi-button-pointer"
            }
        }
    },
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
        "opto_cnt": {
                "chan_no": 8,
                "uom": "",
                "com": {
                    "get": "getOptoCount",
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
                    #"get": "__NOGET__",
                    "get": "getDacV",
                    "set": "setDacV"
                },
                "icon": {
                    "on": "mdi:flash-triangle",
                    "off": "mdi:flash-triangle"
                }
        },
        "od": {
                "chan_no": 4,
                "uom": "%",
                "min_value": 0.0,
                "max_value": 100.0,
                "step": 0.01,
                "com": {
                    "get": "_fixed_getOdPwm",
                    "set": "_fixed_setOdPwm"
                },
                "icon": {
                    "on": "mdi:flash-triangle",
                    "off": "mdi:flash-triangle"
                }
        },
    },
}

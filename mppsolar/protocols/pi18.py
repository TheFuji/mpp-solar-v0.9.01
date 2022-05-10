
import logging

from .abstractprotocol import AbstractProtocol
from .protocol_helpers import crcPI as crc

# from .pi30 import COMMANDS

log = logging.getLogger("pi18")

COMMANDS = {
    "EM": {
        "name": "EM",
        "description": "Query generated energy of month",
        "help": " -- examples: PCP01 (1: enable, 0: disable)",
        "type": "QUERY",
        "response": [
            ["int", "Generated energy month", "Wh" ],
        ],
        "test_responses": [
            b"^1\x0b\xc2\r",
        ],
        "regex": "EM(\\d\\d\\d\\d\\d\\d)$",
    },
    "EY": {
        "name": "EY",
        "description": "Query generated energy of year",
        "help": " -- examples: PCP01 (1: enable, 0: disable)",
        "type": "QUERY",
        "response": [
            ["int", "Generated energy year", "Wh" ],
        ],
        "test_responses": [
            b"^1\x0b\xc2\r",
        ],
        "regex": "EY(\\d\\d\\d\\d)$",
    },

    "ET": {
        "name": "ET",
        "description": "Total Generated Energy query",
        "help": " -- Query total generated energy",
        "type": "QUERY",
        "response": [["int", "Total generated energy", "Wh"]],
        "test_responses": [
            b"",
        ],

    },
    "FLAG": {
        "name": "FLAG",
        "description": "Query enable/disable flag status",
        "help": " -- Query enable/disable flag status",
        "type": "QUERY",
        "response": [
            ["option", "Enable/disable silence buzzer or open buzzer", ["disable", "enable"]],
            ["option", "Enable/Disable overload bypass function", ["disable", "enable"]],
            ["option", "Enable/Disable LCD display escape to default page after 1mintimeout", ["disable", "enable"]],
            ["option", "Enable/Disable overload restart", ["disable", "enable"]],
            ["option", "Enable/Disable over temperature restart", ["disable", "enable"]],
            ["option", "Enable/Disable backlight on", ["disable", "enable"]],
            ["option", "Enable/Disable alarm on when primary source interrupt", ["disable", "enable"]],
            ["option", "Enable/Disable fault code record", ["disable", "enable"]],
            
            
            ],
        "test_responses": [
            b"",
        ],
    },

    "PIRI": {
        "name": "PIRI",
        "description": "Query rated information",
        "help": " -- Query rated information",
        "type": "QUERY",
        "response": [
            ["10int", "AC input rating voltage", "V"],
            ["int", "AC input rating curent", "A"],
            ["10int", "AC output rating voltage", "V"],
            ["10int", "AC output rating frequency", "Hz"],
            ["int", "AC output rating current", "A"],
            ["int", "AC output rating apparent power", "VA"],
            ["int", "AC output rating active power", "W"],
            ["10int", "Battery rating voltage", "V"],
            ["10int", "Battery re-charge voltage", "V"],
            ["10int", "Battery re-discharge voltage", "V"],
            ["10int", "Battery under voltage", "V"],
            ["10int", "Battery bulk voltage", "V"],
            ["10int", "Battery float voltage", "V"],
            [
                "option",
                "Battery type",
                ["AGM", "Flooded", "User"],
            ],
            ["int", "Max AC charging current", "A"],
            ["int", "Max charging current", "A"],
            [
                "option",
                "Input voltage range",
                ["Appliance", "UPS"],
            ],
            [
                "option",
                "Output source priority",
                ["Solar-Utility-Battery", "Solar-Battery-Utility"],
            ],
            [
                "option",
                "Charger source priority",
                ["Solar first", "Solar and Utility", "Only solar"],
            ],
            ["int", "Parallel max num", ""],
            [
                "option",
                "Machine type",
                ["Off-grid Tie", "Grid-Tie"],
            ],
            [
                "option",
                "Topology",
                ["transformerless","transformer"]
            ],
            [
                "option",
                "Output model setting",
                ["Single module", "Parallel output", "Phase 1 of three phaseoutput", "Phase 2 of three phase output", "Phase 3 of three phase"],
            ],
            [
                "option",
                "Solar power priority",
                ["Battery-Load-Utility", "Load-Battery-Utility"],
            ],
            ["int", "MPPT string", ""],
            
            ],
        "test_responses": [
            b"",
        ],
    },
    "DI": {
        "name":"DI",
        "description": "Query default value of changeable parameter",
        "help": "",
        "type": "QUERY",
        "response": [
            ["10int", "AC output voltage", "V"],
            ["10int", "AC output frequency", "Hz"],
            ["option", "AC input voltage range", ["Appliance", "UPS"]],
            ["10int", "Battery Under voltage", "V"],
            ["10int", "Charging float voltage", "V"],
            ["10int", "Charging bulk voltage", "V"],
            ["10int", "Battery default re-charge voltage", "V"],
            ["10int", "Battery re-discharge voltage", "V"],
            ["int", "Max charging current", "A"],
            ["int", "Max AC charging current", "A"],
            ["option", "Battery type", ["AGM", "Flooded", "User"]],
            ["option", "Output source priority", ["Solar-Utility-Battery", "Solar-Battery-Utility"]],
            ["option", "Charger source priority", ["Solar first", "Solar and Utility", "Only solar"]],
            ["option", "Solar power priority", ["Battery-Load-Utility", "Load-Battery-Utility"]],
            ["option", "Machine type", ["Off-grid Tie", "Grid-Tie"]],
            ["option", "Output model setting", ["Single module", "Parallel output", "Phase 1 of three phaseoutput", "Phase 2 of three phase output", "Phase 3 of three phase"]],
            ["option", "Enable/disable silence buzzer or open buzzer", ["disable", "enable"]],
            ["option", "Enable/Disable overload restart", ["disable", "enable"]],
            ["option", "Enable/Disable over temperature restart", ["disable", "enable"]],
            ["option", "Enable/Disable LCD backlight on", ["disable", "enable"]],
            ["option", "Enable/Disable alarm on when primary source interrupt", ["disable", "enable"]],
            ["option", "Enable/Disable fault code record", ["disable", "enable"]],
            ["option", "Enable/Disable overload bypass", ["disable", "enable"]],
            ["option", "Enable/Disable LCD display escape to default page after 1mintimeout", ["disable", "enable"]],
            
            
        ],
        "test_responses": [
            b"",
        ],  
    },
    "GS": {
        "name": "GS",
        "description": "General status query",
        "help": " -- Query general status information",
        "type": "QUERY",
        "response": [
            ["10int", "Grid voltage", "V"],
            ["10int", "Grid frequency", "Hz"],
            ["10int", "AC output voltage", "V"],
            ["10int", "AC output frequency", "Hz"],
            ["int", "AC output apparent power", "VA"],
            ["int", "AC output active power", "W"],
            ["int", "Output load percent", "%"],
            ["10int", "Battery voltage", "V"],
            ["10int", "Battery voltage from SCC", "V"],
            ["10int", "Battery voltage from SCC2", "V"],
            ["int", "Battery discharge current", "A"],
            ["int", "Battery charging current", "A"],
            ["int", "Battery capacity", "%"],
            ["int", "Inverter heat sink temperature", "°C"],
            ["int", "MPPT1 charger temperature", "°C"],
            ["int", "MPPT2 charger temperature", "°C"],
            ["int", "PV1 Input power", "W"],
            ["int", "PV2 Input power", "W"],
            ["10int", "PV1 Input voltage", "V"],
            ["10int", "PV2 Input voltage", "V"],
            [
                "option",
                "Setting value configuration state",
                ["Nothing changed", "Something changed"],
            ],
            [
                "option",
                "MPPT1 charger status",
                ["abnormal", "normal but not charged", "charging"],
            ],
            [
                "option",
                "MPPT2 charger status",
                ["abnormal", "normal but not charged", "charging"],
            ],
            ["option", "Load connection", ["disconnect", "connect"]],
            ["option", "Battery power direction", ["donothing", "charge", "discharge"]],
            ["option", "DC/AC power direction", ["donothing", "AC-DC", "DC-AC"]],
            ["option", "Line power direction", ["donothing", "input", "output"]],
            ["int", "Local parallel ID", ""],
        ],
        "test_responses": [
            b"D1062232,499,2232,499,0971,0710,019,008,000,000,000,000,000,044,000,000,0520,0000,1941,0000,0,2,0,1,0,2,1,0\x09\x7b\r",
            b"^0\x1b\xe3\r",
        ],
    },
    "MOD": {
        "name": "MOD",
        "description": "Working mode query",
        "help": " -- Query the working mode",
        "type": "QUERY",
        "response": [
            [
                "option",
                "Working mode",
                [
                    "Power on mode",
                    "Standby mode",
                    "Bypass mode",
                    "Battery mode",
                    "Fault mode",
                    "Hybrid mode(Line mode, Grid mode)",
                ],
            ]
        ],
        "test_responses": [
            b"",
        ],
    },
    "MCHGCR": {
        "name": "MCHGCR",
        "description": "Query Max. charging current selectable value",
        "help": " -- Query Max. charging current selectable value",
        "type": "QUERY",
        "response": [
            ["int", "Max. charging current selectable value", "A"],
            ["int", "Max. charging current selectable value", "A"],
            ["int", "Max. charging current selectable value", "A"],
            ["int", "Max. charging current selectable value", "A"],
            ["int", "Max. charging current selectable value", "A"],
            ["int", "Max. charging current selectable value", "A"],
            ["int", "Max. charging current selectable value", "A"],
            ],
        "test_responses": [
            b"",
        ],
    },
    "MUCHGCR": {
        "name": "MUCHGCR",
        "description": "Query Max. AC charging current selectable valuee",
        "help": " -- Query Max. AC charging current selectable value",
        "type": "QUERY",
        "response": [
            ["int", "Max. charging current selectable value", "A"],
            ["int", "Max. charging current selectable value", "A"],
            ["int", "Max. charging current selectable value", "A"],
            ["int", "Max. charging current selectable value", "A"],
            ["int", "Max. charging current selectable value", "A"],
            ["int", "Max. charging current selectable value", "A"],
            ["int", "Max. charging current selectable value", "A"],
            ],
        "test_responses": [
            b"",
        ],
    },


    "PI": {
        "name": "PI",
        "description": "Device Protocol Version inquiry",
        "help": " -- queries the device protocol version",
        "type": "QUERY",
        "response": [["string", "Protocol Version", ""]],
        "test_responses": [
            b"",
        ],
    },

    "ED": {
        "name": "ED",
        "description": "Set charging source priority",
        "help": " -- examples: PCP01 (1: enable, 0: disable)",
        "type": "QUERY",
        "response": [
            ["int", "Generated energy day", "Wh" ],
        ],
        "test_responses": [
            b"^1\x0b\xc2\r",
        ],
        "regex": "ED(\\d\\d\\d\\d\\d\\d\\d\\d)$",
    },

    "PI": {
        "name": "PI",
        "description": "Machine type, enable: Grid-Tie, disable: Off-Grid",
        "help": " -- examples: PI1 (1: enable, 0: disable)",
        "type": "SETTER",
        "response": [
            ["ack", "Command execution", {"NAK": "Failed", "ACK": "Successful"}],
        ],
        "test_responses": [
            b"^1\x0b\xc2\r",
            b"^0\x1b\xe3\r",
        ],
        "regex": "P([ED])I$",
    },

        "POP": {
        "name": "POP",
        "description": "Set output souce priority",
        "help": " -- examples: POP1 (1: enable, 0: disable)",
        "type": "SETTER",
        "response": [
            ["ack", "Command execution", {"NAK": "Failed", "ACK": "Successful"}],
        ],
        "test_responses": [
            b"^1\x0b\xc2\r",
            b"^0\x1b\xe3\r",
        ],
        "regex": "POP([01])$",
    },
        
        "PCP": {
        "name": "PCP",
        "description": "Set charging source priority",
        "help": " -- examples: PCP0 (1: enable, 0: disable)",
        "type": "SETTER",
        "response": [
            ["ack", "Command execution", {"NAK": "Failed", "ACK": "Successful"}],
        ],
        "test_responses": [
            b"^1\x0b\xc2\r",
            b"^0\x1b\xe3\r",
        ],
        "regex": "PCP0([012])$",
    },


    "PSP": {
        "name": "PSP",
        "description": "Set solar power priority",
        "help": " -- examples: PSP(0-BLU; 1-LBU)",
        "type": "SETTER",
        "response": [
            ["ack", "Command execution", {"NAK": "Failed", "ACK": "Successful"}],
        ],
        "test_responses": [
            b"^1\x0b\xc2\r",
            b"^0\x1b\xe3\r",
        ],
        "regex": "PSP([01])$",
    },
    "PA": {
        "name": "PA",
        "description": "Mute buzzer beep",
        "help": " -- examples: PA1 (1: enable, 0: disable)",
        "type": "SETTER",
        "response": [
            ["ack", "Command execution", {"NAK": "Failed", "ACK": "Successful"}],
        ],
        "test_responses": [
            b"^1\x0b\xc2\r",
            b"^0\x1b\xe3\r",
        ],
        "regex": "P([ED])A$",
    },
    "MCHGV": {
        "name": "MCHGV",
        "description": "Set battery maximum charge voltage",
        "help": " -- example MCHGV580,580 - set battery float charging voltage to 58V (48.0 - 58.4V for 48V unit)",
        "type": "SETTER",
        "response": [["ack", "Command execution", {"NAK": "Failed", "ACK": "Successful"}]],
        "test_responses": [
            b"(NAK\x73\x73\r",
            b"(ACK\x39\x20\r",
        ],
        "regex": "MCHGV(\\d\\d\\d,\\d\\d\\d)$",
    },

    "MCHGC": {
        "name": "MCHGC",
        "description": "Set Battery Max Charging Current Solar + AC 		(Maunal Option 11)",
        "help": " -- example: MCHGC0,030 	(set unit 0 [0-9] to max charging current of  30A [    010 020 030 040 050 060 070 080])",
        "type": "SETTER",
        "response": [
            ["ack", "Command execution", {"NAK": "Failed", "ACK": "Successful"}],
        ],
        "test_responses": [
            b"(NAK\x73\x73\r",
            b"(ACK\x39\x20\r",
        ],
        "regex": "MCHGC(\\d,0\\d\\d)$",
    },

    "MUCHGC": {
        "name": "MUCHGC",
        "description": "Set Battery Max AC Charging Current 			(Maunal Option 13)",
        "help": " -- example: MUCHGC0,030 	(set unit 0 [0-9] utility charging current to 30A [002 010 020 030 040 050 060 070 080])",
        "type": "SETTER",
        "response": [
             ["ack", "Command execution", {"NAK": "Failed", "ACK": "Successful"}]
        ],
        "test_responses": [
            b"",
        ],
        "regex": "MUCHGC(\\d),(002|0\\d\\d)$",
    },

    "PSDV": {
        "name": "PSDV",
        "description": "Set Battery Cut-off Voltage	 			(Maunal Option 19)",
        "help": " -- example: PSDV450 		(set battery cut-off voltage to 45V [400~480V] for 48V unit)",
        "type": "SETTER",
        "response": [["ack", "Command execution", {"NAK": "Failed", "ACK": "Successful"}]],
        "test_responses": [
            b"(NAK\x73\x73\r",
            b"(ACK\x39\x20\r",
        ],
        "regex": "PSDV(\\d\\d\\d)$",
    },

    "BUCD": {
        "name": "BUCD",
        "description": "Set Battery Stop dis,charging when Grid is available (Maunal Option 20,21)",
        "help": " -- example: BUCD44,48	(set Stop discharge Voltate [440~510] in 0.1V xxx, Stop Charge Voltage [000(Full) or 480~580] in 0.1V yyy)",
        "type": "SETTER",
        "response": [
            ["ack", "Command execution", {"NAK": "Failed", "ACK": "Successful"}]
        ],
        "test_responses": [
            b"(NAK\x73\x73\r",
            b"(ACK\x39\x20\r",
        ],
        "regex": "BUCD(\\d\\d\\d,\\d\\d\\d)$",
    },

}


class pi18(AbstractProtocol):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__()
        self._protocol_id = b"PI18"
        self.COMMANDS = COMMANDS
        self.STATUS_COMMANDS = ["EM", "EY", "PIRI", "MOD", "GS", "ET", "DI", "FLAG", "ED"]
        self.SETTINGS_COMMANDS = [
            "PI", "MCHGCR", "MUCHGCR",
            
        ]
        self.DEFAULT_COMMAND = "PI"
        log.info(f'Using protocol {self._protocol_id} with {len(self.COMMANDS)} commands')

    def get_full_command(self, command) -> bytes:
        """
        Override the default get_full_command as its different for PI18
        """
        log.info(f"Using protocol {self._protocol_id} with {len(self.COMMANDS)} commands")
        # These need to be set to allow other functions to work`
        self._command = command
        self._command_defn = self.get_command_defn(command)
        # End of required variables setting
        if self._command_defn is None:
            return None
            log.debug("e gol")

        _cmd = bytes(self._command, "utf-8")
        _type = self._command_defn["type"]

        data_length = len(_cmd) + 2 + 1
        if _type == "QUERY":
            _prefix = f"^P{data_length:03}"
        else:
            _prefix = f"^S{data_length:03}"
        _pre_cmd = bytes(_prefix, "utf-8") + _cmd
        log.debug(f"_pre_cmd: {_pre_cmd}")
        # calculate the CRC
        crc_high, crc_low = crc(_pre_cmd)
        # combine byte_cmd, CRC , return
        # PI18 full command "^P005GS\x..\x..\r"
        _crc = bytes([crc_high, crc_low, 13])
        full_command = _pre_cmd + _crc
        log.debug(f"full command: {full_command}")
        return full_command

    def get_responses(self, response):
        """
        Override the default get_responses as its different for PI18
        """
        responses = response.split(b",")
        if responses[0] == b"^0\x1b\xe3\r":
            # is a reject response
            return ["NAK"]
        elif responses[0] == b"^1\x0b\xc2\r":
            # is a successful acknowledgement response
            return ["ACK"]
        # Drop ^Dxxx from first response
        responses[0] = responses[0][5:]
        # Remove CRC of last response
        responses[-1] = responses[-1][:-3]
        return responses

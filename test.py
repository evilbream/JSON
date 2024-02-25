from JS_DICT import JSON
import json
from testing.test_dicts import dict1_1
from testing.test_schemas import sch1

test_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
        "complete": {
            "default" : True,
            "description" : "operation completion flag - if true - user balance should be reduced",
            "type": "boolean"

        },
        "valueSec": {
            "default" : 0,
            "description" : "billed data volume in seconds",
            "type": "integer"
        },
        "withdrawal": {
            "type": "array",
            "description" : "table of debits from user accounts",
            "items": {
                "type": "object",
                "properties": {
                    "currency": {
                        "type": "string",
                        "default" : "   ",
                        "enum": ["USD", "RUB"],
                        "minLength": 3,
                        "maxLength": 3
                    },
                    "amount": {
                        "type": "number"
                    }
                },
                "required": ["currency", "amount"]
            }
        },
    "arr": {"type": "array",
            "items": {
                "type": "array",
                "items": {
                    "type": "integer"
                },
            }},
    'withheld': {"type": "object",
                "properties": {
                    "cur": {
                        "type": "string",
                        "default" : "fgggg",
                    },
                    "am": {
                        "type": "number",
                        "default": 12.12
                    }
                },
                "required": ["cur", "am"]
                 },

    "put": {
        "type": "array",
        "description": "table of debits from user accounts",
        "items": {
            "type": "object",
            "properties": {
                "currency": {
                    "type": "string",
                    "default": "   ",
                    "enum": ["USD", "RUB"],
                    "minLength": 3,
                    "maxLength": 3
                },
                "amount": {
                    "type": "number"
                },
                "name": {'type': 'object',
                         "properties": {
                             "cut": {
                                 "type": "number",
                                 "default": "   ",
                             }}
                         }

            },
            "required": ["currency", "amount"]
        }
    },

    'dirty': {'type': 'object'},
        "required": [
            "complete",
            "valueSec", 'dirty'
        ]
}

dic = {'withheld': {'am': 123.12, 'cur': 'fgf'},  'dirty': {12: 23},
       'valueSec': 12, 'arr': [['1', 2, 3], [34, 34]], 'withdrawal':[{'currency': 'RUB', 'amount':567.1}, {'amount': 555.1, 'currency': 'USD'}], 'put': [{'currency': 'RUB', 'amount':567.1, 'name': {'cut':12.11}}]}

dic2 = [1, 2, 3]

def warning(war):
    if war:
        print(war)

def error(error):
    if error:
        print(error)
js_form = json.loads(json.dumps(test_schema))
js = JSON(dict1_1)
correct = js.validate(sch1, warning_callback=warning, error_callback=error)
assert correct is True
print(js)








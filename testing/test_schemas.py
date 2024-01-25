sch1 = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
        "complete": {
            "default" : True,
            "description" : "operation completion flag - if true - user balance should be reduced",
            "type": "boolean"
        },
        "sourceDescription": {
            "description" : "",
            "type": "string"
        },
        "docID": {
            "description" : "",
            "type": "string"
        },
        "integrationID": {
            "description" : "",
            "type": "string"
        },
        "service": {
            "description" : "",
            "type": "string"
        },
        "time": {
            "description" : "time.time() for event",
            "type": "integer"
        },
        "valueSec": {
            "default" : 0,
            "description" : "billed data volume in seconds",
            "type": "integer"
        },
        "valueb": {
            "default" : 0,
            "description" : "billed data volume in bytes",
            "type": "integer"
        },
        "valueMonth": {
            "default" : 0,
            "description" : "",
            "type": "number"
        },
        "valuebMonth": {
            "default" : 0,
            "description" : "",
            "type": "number"
        },
        "valueEvent": {
            "default" : 0,
            "description" : "",
            "type": "integer"
        },
        "currency": {
            "default" : "   ",
            "description" : "default user currency in effect at the time of the transaction",
            "type": "string",
            "enum": ["USD", "RUB"],
            "minLength": 3,
            "maxLength": 3
        },
        "cost": {
            "default" : 0,
            "description" : "debiting funds in the user's default currency",
            "type": "number"
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
        "required": [
            "complete",
            "docID",
            "integrationID",
            "service",
            "valueSec",
            "valueb",
            "valuebMonth",
            "valueMonth",
            "valueEvent",
            "cost",
            "currency"
        ]
}

sch2 = {
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

    'disabled': {'type': 'object'},
        "required": [
            "complete",
            "valueSec", 'disabled'
        ]
}

sch3 =test_schema = {
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

        "billing": {
            "default" : 0,
            "description" : "billed data volume in seconds",
            "type": "integer"
        },

    'disabled': {'type': 'object',
                 'default': False},

    'define': {'type': 'null'},

        "required": [
            "complete",
             'billing'
        ]
}


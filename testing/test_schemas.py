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

sch4 = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "user": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "User's full name"
        },
        "email": {
          "type": "string",
          "description": "User's email address"
        },
        "address": {
          "type": "object",
          "properties": {
            "street": {
              "type": "string",
              "description": "Street name"
            },
            "city": {
              "type": "string",
              "description": "City name"
            },
            "country": {
              "type": "string",
              "description": "Country name"
            }
          },
          "required": ["street", "city", "country"]
        }
      },
      "required": ["name", "email", "address"]
    },
    "products": {
      "type": "array",
      "description": "List of products purchased by the user",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "Product name"
          },
          "price": {
            "type": "number",
            "description": "Product price"
          },
          "quantity": {
            "type": "integer",
            "description": "Quantity of product purchased"
          }
        },
        "required": ["name", "price", "quantity"]
      }
    }
  },
  "required": ["user", "products"]
}

sch5 = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "user": {
      "type": "object",
      "properties": {
        "id": {
          "description": "User's unique identifier",
          "type": "string"
        },
        "name": {
          "description": "User's name",
          "type": "string"
        },
        "email": {
          "description": "User's email",
          "type": "string"
        },
        "address": {
          "type": "object",
          "properties": {
            "street": {
              "description": "Street name",
              "type": "string"
            },
            "city": {
              "description": "City name",
              "type": "string"
            },
            "country": {
              "description": "Country name",
              "type": "string"
            },
            "postalCode": {
              "description": "Postal code",
              "type": "string"
            },
            "coordinates": {
              "type": "object",
              "properties": {
                "latitude": {
                  "description": "Latitude",
                  "type": "number"
                },
                "longitude": {
                  "description": "Longitude",
                  "type": "number"
                }
              },
              "required": ["latitude", "longitude"]
            }
          },
          "required": ["street", "city", "country", "postalCode", "coordinates"]
        }
      },
      "required": ["id", "name", "email", "address"]
    },
    "transaction": {
      "type": "object",
      "properties": {
        "id": {
          "description": "Transaction's unique identifier",
          "type": "string"
        },
        "amount": {
          "description": "Transaction amount",
          "type": "number"
        },
        "currency": {
          "description": "Transaction currency",
          "type": "string",
          "enum": ["USD", "RUB"],
          "minLength": 3,
          "maxLength": 3
        },
        "date": {
          "description": "Transaction date",
          "type": "string",
          "format": "date-time"
        }
      },
      "required": ["id", "amount", "currency", "date"]
    }
  },
  "required": ["user", "transaction"]
}

sch7 = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
        "complete": {
            "default" : True,
            "description" : "operation completion flag - if true - user balance should be reduced",
            "type": "boolean"

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
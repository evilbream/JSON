
dict1_1 = {'complete': 1, 'sourceDescription': 'None', 'docID': '123', 'integrationID': '145g', 'service': 'None',
         'time': 12244, 'valueSec': 1234, 'valueb': 145, 'valuebMonth': 123.12, 'valueEvent': 4, 'currency': 'USD',
         'cost': 23.12, 'withdrawal': [{'currency': 'USD', 'amount': 12.23}, {'currency': 'RUB', 'amount': 45.12},
                                       {'currency': 'RUB', 'amount': 345}, {'currency': 'RUB', 'amount': 12345},
                                       {'currency': 'RUB', 'amount': '66666'}, {'currency': 'RUB', 'amount': '45.12'},
                                       {'currency': 'RUB', 'amount': '45.12'}, {'currency': 'RUB', 'amount': 45.12}]
         }

dict1_2 = {'sourceDescription': 'None', 'docID': '123', 'integrationID': '145g', 'service': 'None',
         'time': 12244, 'valueSec': 2333, 'valueb': 144, 'valuebMonth': 123.12, 'valueEvent': 4, 'currency': 'USD',
         'cost': 23.12, 'withdrawal': [{'currency': 'USD', 'amount': 12.23}, {'currency': 'RUB', 'amount': 45.12}]
         }


dict1_3 = {'docID': '123', 'integrationID': '145g', 'service': 'None', 'currency': 'USD' }


dict1_4 = {'complete': False, 'docID': None, 'service': 'None',
         'time': 12244, 'valueSec': 2333, 'valueb': 145, 'valueMonth': 1.12, 'valuebMonth': 123.12, 'valueEvent': 4, 'currency': 'USD',
         'cost': 23.12, 'withdrawal': [True, False, None, ['RUB', 45.12]]
         }

dict1_5 = {'complete': False, 'sourceDescription': None, 'docID': '123',
         'time': 12244, 'valueSec': 2333, 'valueb': 145, 'valueMonth': 1.12, 'valuebMonth': 123.12, 'valueEvent': 4, 'currency': 'ufg',
         }

dict1_6 = {'docID': '123', 'integrationID': '145g',
         'service': '12244', 'valueSec': None, 'valueb': 145, 'valueMonth': None, 'valuebMonth': None, 'valueEvent': 4, 'currency': 'USD',
           'cost': 12.12 }

dict1_7 = {'complete': False, 'sourceDescription': 'None', 'docID': 123, 'integrationID': '145g', 'service': 'None',
         'time': 12244, 'valueSec': 2333, 'valueb': 145, 'valueMonth': 1.12, 'valuebMonth': 123.12, 'valueEvent': 4, 'currency': 'USD',
         'cost': 23.12, 'withdrawal': [{'currency': 'USD'}, {'currency': 'RUBS', 'amount': 45.12}]
         }

dict1_8 = {'complete': False, 'sourceDescription': 'None', 'docID': '123', 'integrationID': '145g',
         'time': 12244, 'valueSec': 2333, 'valueb': 145, 'valueMonth': 1.12, 'valuebMonth': 123.12, 'valueEvent': 4, 'currency': 'USDT',
         'cost': 23.12, 'withdrawal': ['USD', 4513]
         }

dict1_9 = {'complete': 1, 'sourceDescription': None, 'docID': 123, 'integrationID': 34.12,
         'time': '1233334', 'valueSec': '2333', 'valueb': 1233.12, 'valueMonth': '1.12', 'valuebMonth': 123.12, 'valueEvent': 4, 'currency': 'USD',
         'cost': 23.12, 'withdrawal': [{'currency': 'USDG', 'amount': 4513}]
         }

dict2_1 = {'withheld': {'am': 123.12, 'cur': 'fgf'},  'dirty': {12: 23},
       'valueSec': 12, 'arr': [['1', 2, 3], [34, 34]], 'withdrawal':[{'currency': 'RUB', 'amount':567.1}, {'amount': 555.1, 'currency': 'USD'}], 'put': [{'currency': 'RUB', 'amount':567.1, 'name': {'cut':12.11}}],
           'disabled': {'12': 23}}


dict2_2 = {'withheld': {'cur': 'fgf'},
       'valueSec': 12, 'arr': [['1', 2, 3], [34, 34]], 'withdrawal':[{'currency': 'RUB', 'amount':567.1}, {'amount': 555.1, 'currency': 'USD'}], 'put': [{'currency': 'RUB', 'amount':567.1, 'name': {'cut':'12.11'}}],
           'disabled': {'12': 23}}

dict2_2_1 = {'withheld': {'cur': 'fgf', 'am': 12.12}, 'valueSec': 12, 'arr': [[1, 2, 3], [34, 34]], 'withdrawal': [{'currency': 'RUB', 'amount': 567.1}, {'amount': 555.1, 'currency': 'USD'}], 'put': [{'currency': 'RUB', 'amount': 567.1, 'name': {'cut': 12.11}}], 'disabled': {'12': 23}, 'complete': True}


dict2_3 = {'withheld': {'cur': 'fgf'},
       'valueSec': 12, 'arr': [123, [34, 34]], 'withdrawal': 12, 'put': [{'currency': 'RUB', 'amount':567.1, 'name': 1234}],
           'disabled': {'12': 23}}

dict3_1 = {}
dict3_2 = {'disabled': {'name': 123}, 'define': None}
dict3_3 = {'disabled': [1, 2, 3, 4]}


dict_sh1_correct = [ {"complete": True, "docID": "123", "integrationID": "456", "service": "Netflix", "time": 1633027200, "valueSec": 3600, "valueb": 5000, "valueMonth": 30, "valuebMonth": 150000, "valueEvent": 1, "currency": "USD", "cost": 10, "withdrawal": [{"currency": "USD", "amount": 10}]},
{"complete": False, "docID": "124", "integrationID": "457", "service": "Spotify", "time": 1633113600, "valueSec": 1800, "valueb": 2500, "valueMonth": 15, "valuebMonth": 75000, "valueEvent": 2, "currency": "RUB", "cost": 500, "withdrawal": [{"currency": "RUB", "amount": 500}]},
{"complete": True, "docID": "125", "integrationID": "458", "service": "Amazon Prime", "time": 1633200000, "valueSec": 7200, "valueb": 10000, "valueMonth": 60, "valuebMonth": 300000, "valueEvent": 3, "currency": "USD", "cost": 20, "withdrawal": [{"currency": "USD", "amount": 20}]},
{"complete": False, "docID": "126", "integrationID": "459", "service": "Hulu", "time": 1633286400, "valueSec": 3600, "valueb": 5000, "valueMonth": 30, "valuebMonth": 150000, "valueEvent": 4, "currency": "RUB", "cost": 1000, "withdrawal": [{"currency": "RUB", "amount": '1000'}]},
 {"complete": True, "docID": "127", "integrationID": "460", "service": "Disney+", "time": 1633372800, "valueSec": 1800, "valueb": 2500, "valueMonth": 15, "valuebMonth": 75000, "valueEvent": 5, "currency": "USD", "cost": 5, "withdrawal": [{"currency": "USD", "amount": 5}, {"currency": "USD", "amount": 5}, {"currency": "USD", "amount": 5}]},
 {"complete": False, "docID": "128", "integrationID": "461", "service": "HBO Max", "time": 1633459200, "valueSec": 7200, "valueb": 10000, "valueMonth": 60, "valuebMonth": 300000, "valueEvent": 6, "currency": "RUB", "cost": 1500, "withdrawal": [{"currency": "RUB", "amount": 1500}, {"currency": "USD", "amount": 5}]},
{"complete": True, "docID": "129", "integrationID": "462", "service": "Apple TV+", "time": 1633545600, "valueSec": 3600, "valueb": 5000, "valueMonth": 30, "valuebMonth": 150000, "valueEvent": 7, "currency": "USD", "cost": 7, "withdrawal": [{"currency": "USD", "amount": 7}, {"currency": "USD", "amount": '5'}]},
 {"complete": False, "docID": "130", "integrationID": "463", "service": "Peacock", "time": 1633632000, "valueSec": 1800, "valueb": 2500, "valueMonth": 15, "valuebMonth": 75000, "valueEvent": 8, "currency": "RUB", "cost": 2000, "withdrawal": [{"currency": "RUB", "amount": 2000}]},
 {"complete": True, "docID": "131", "integrationID": "464", "service": "Paramount+", "time": 1633718400, "valueSec": 7200, "valueb": 10000, "valueMonth": 60, "valuebMonth": 300000, "valueEvent": 9, "currency": "USD", "cost": 9, "withdrawal": [{"currency": "USD", "amount": 9}]},
{"complete": False, "docID": "132", "integrationID": "465", "service": "YouTube Premium", "time": 1633804800, "valueSec": 3600, "valueb": 5000, "valueMonth": 30, "valuebMonth": 150000, "valueEvent": 10, "currency": "RUB", "cost": 2500, "withdrawal": [{"currency": "RUB", "amount": 2500}]},
 {"complete": True, "docID": "133", "integrationID": "466", "service": "Twitch", "time": 1633891200, "valueSec": 1800, "valueb": 2500, "valueMonth": 15, "valuebMonth": 75000, "valueEvent": 11, "currency": "USD", "cost": 11, "withdrawal": [{"currency": "USD", "amount": 11}]},
 {"complete": False, "docID": "134", "integrationID": "467", "service": "Vimeo", "time": 1633977600, "valueSec": 7200, "valueb": 10000, "valueMonth": 60, "valuebMonth": 300000, "valueEvent": 12, "currency": "RUB", "cost": '3000', "withdrawal": [{"currency": "RUB", "amount": 3000}]},
 {"complete": True, "docID": "135", "integrationID": "468", "service": "Crunchyroll", "time": 1634064000, "valueSec": 3600, "valueb": 5000, "valueMonth": 30, "valuebMonth": 150000, "valueEvent": 13, "currency": "USD", "cost": 13, "withdrawal": [{"currency": "USD", "amount": 13}]},
 {"complete": False, "docID": "136", "integrationID": "469", "service": "Funimation", "time": 1634150400, "valueSec": 1800, "valueb": 2500, "valueMonth": 15, "valuebMonth": 75000, "valueEvent": 14, "currency": "RUB", "cost": 3500, "withdrawal": [{"currency": "RUB", "amount": 3500}]},
 {"complete": True, "docID": "137", "integrationID": "470", "service": "Tubi", "time": 1634236800, "valueSec": 7200, "valueb": 10000, "valueMonth": 60, "valuebMonth": 300000, "valueEvent": 15, "currency": "USD", "cost": '15', "withdrawal": [{"currency": "USD", "amount": 15}]},
{"complete": False, "docID": "138", "integrationID": "471", "service": "Pluto TV", "time": 1634323200, "valueSec": 3600, "valueb": 5000, "valueMonth": 30, "valuebMonth": 150000, "valueEvent": 16, "currency": "RUB", "cost": 4000, "withdrawal": [{"currency": "RUB", "amount": 4000}]},
{"complete": True, "docID": "139", "integrationID": "472", "service": "Vudu", "time": 1634409600, "valueSec": 1800, "valueb": 2500, "valueMonth": 15, "valuebMonth": 75000, "valueEvent": 17, "currency": "USD", "cost": 17, "withdrawal": [{"currency": "USD", "amount": 17}]},
 {"complete": False, "docID": "140", "integrationID": "473", "service": "Redbox", "time": 1634496000, "valueSec": 7200, "valueb": 10000, "valueMonth": 60, "valuebMonth": 300000, "valueEvent": 18, "currency": "RUB", "cost": '4500', "withdrawal": [{"currency": "RUB", "amount": 4500}]},
 {"complete": True, "docID": "141", "integrationID": "474", "service": "FandangoNOW", "time": 1634582400, "valueSec": 3600, "valueb": 5000, "valueMonth": 30, "valuebMonth": 150000, "valueEvent": 19, "currency": "USD", "cost": 19, "withdrawal": [{"currency": "USD", "amount": 19}]},
 {"complete": False, "docID": "142", "integrationID": "475", "service": "Shudder", "time": 1634668800, "valueSec": 1800, "valueb": 2500, "valueMonth": 15, "valuebMonth": 75000, "valueEvent": 20, "currency": "RUB", "cost": '5000', "withdrawal": [{"currency": "RUB", "amount": 5000}]},
 {"complete": True, "docID": "143", "integrationID": "476", "service": "Sling TV", "time": 1634755200, "valueSec": 7200, "valueb": 10000, "valueMonth": 60, "valuebMonth": 300000, "valueEvent": 21, "currency": "USD", "cost": 21, "withdrawal": [{"currency": "USD", "amount": 21}]},
 {"complete": False, "docID": "144", "integrationID": "477", "service": "Hulu + Live TV", "time": 1634841600, "valueSec": 3600, "valueb": 5000, "valueMonth": 30, "valuebMonth": 150000, "valueEvent": 22, "currency": "RUB", "cost": 5500, "withdrawal": [{"currency": "RUB", "amount": 5500}]},
 {"complete": True, "docID": "145", "integrationID": "478", "service": "YouTube TV", "time": 1634928000, "valueSec": 1800, "valueb": 2500, "valueMonth": 15, "valuebMonth": 75000, "valueEvent": 23, "currency": "USD", "cost": 23, "withdrawal": [{"currency": "USD", "amount": 23}]},
 {"complete": False, "docID": "146", "integrationID": "479", "service": "fuboTV", "time": 1635014400, "valueSec": 7200, "valueb": 10000, "valueMonth": 60, "valuebMonth": 300000, "valueEvent": 24, "currency": "RUB", "cost": 6000, "withdrawal": [{"currency": "RUB", "amount": 6000}]},
 {"complete": True, "docID": "147", "integrationID": "480", "service": "Philo", "time": 1635100800, "valueSec": 3600, "valueb": 5000, "valueMonth": 30, "valuebMonth": 150000, "valueEvent": 25, "currency": "USD", "cost": '25', "withdrawal": [{"currency": "USD", "amount": 25}]},
 {"complete": False, "docID": "148", "integrationID": "481", "service": "AT&T TV", "time": 1635187200, "valueSec": 1800, "valueb": 2500, "valueMonth": 15, "valuebMonth": 75000, "valueEvent": 26, "currency": "RUB", "cost": '6500', "withdrawal": [{"currency": "RUB", "amount": 6500}]},
 {"complete": True, "docID": "149", "integrationID": "482", "service": "Xfinity Stream", "time": 1635273600, "valueSec": 7200, "valueb": 10000, "valueMonth": 60, "valuebMonth": 300000, "valueEvent": 27, "currency": "USD", "cost": 27, "withdrawal": [{"currency": "USD", "amount": 27}]},
 {"complete": False, "docID": "150", "integrationID": "483", "service": "Spectrum TV", "time": 1635360000, "valueSec": 3600, "valueb": 5000, "valueMonth": 30, "valuebMonth": 150000, "valueEvent": 28, "currency": "RUB", "cost": '7000', "withdrawal": [{"currency": "RUB", "amount": 7000}]},
{"complete": True, "docID": "151", "integrationID": "484", "service": "Optimum TV", "time": 1635446400, "valueSec": 1800, "valueb": 2500, "valueMonth": 15, "valuebMonth": 75000, "valueEvent": 29, "currency": "USD", "cost": 29, "withdrawal": [{"currency": "USD", "amount": 29}, {"currency": "USD", "amount": '444'}, {"currency": "USD", "amount": '345'}, {"currency": "USD", "amount": '29'}]},
{"complete": False, "docID": "152", "integrationID": "485", "service": "Cox Contour TV", "time": 1635532800, "valueSec": 7200, "valueb": 10000, "valueMonth": 60, "valuebMonth": 300000, "valueEvent": 30, "currency": "RUB", "cost": '7500', "withdrawal": [{"currency": "RUB", "amount": 7500}]}
]


dict_sh1_incorrect = [{"complete": 'rrrr', "docID": "123", "integrationID": "456", "service": "789", "valueSec": 10, "valueb": 20, "valuebMonth": 30, "valueMonth": 40, "valueEvent": 50, "cost": 60, "currency": "USDu"},
{"complete": True, "docID": "123", "integrationID": 456, "service": "789", "valueSec": 10, "valueb": 20, "valuebMonth": 30, "valueMonth": 40, "valueEvent": 50, "cost": 60},
{"complete": True, "docID": "123", "integrationID": "456", "service": 789, "valueSec": 10, "valueb": 20, "valuebMonth": 30, "valueMonth": 40, "valueEvent": 50, "cost": 60},
{"complete": True, "docID": "123", "integrationID": "456", "service": "789", "valueSec": "10", "valueb": 20, "valuebMonth": 30, "valueMonth": 40, "valueEvent": 50, "currency": "USDl"},
{"complete": True, "docID": "123", "integrationID": "456", "service": "789", "valueSec": 10, "valueb": "20", "valuebMonth": 30, "valueMonth": 40, "valueEvent": 50,  "currency": "USDk"},
{"complete": True, "docID": "123", "integrationID": "456", "service": "789", "valueSec": 10, "valueb": 20, "valuebMonth": "30", "valueMonth": 40, "valueEvent": 50, "currency": "USDo"},
{"complete": True, "docID": "123", "integrationID": "456", "service": "789", "valueSec": 10, "valueb": 20, "valuebMonth": 30, "valueMonth": "40", "valueEvent": 50,  "currency": "USDh"},
{"complete": True, "docID": "123", "integrationID": "456", "service": "789", "valueSec": 10, "valueb": 20, "valuebMonth": 30, "valueMonth": 40, "valueEvent": "50",  "currency": "USDu"},
{"complete": True, "docID": "123", "integrationID": "456", "service": "789", "valueSec": 10, "valueb": 20, "valuebMonth": 30, "valueMonth": 40, "valueEvent": 50, "cost": "60kkkkk", "currency": "USD"},
{"complete": True, "docID": "123", "integrationID": "456", "service": "789", "valueSec": 10, "valueb": 20, "valuebMonth": 30, "valueMonth": 40, "valueEvent": 50, "cost": 'ssssss', "currency": "US"},
{"complete": True, "docID": "123", "integrationID": "456", "service": "789", "valueSec": 10, "valueb": 20, "valuebMonth": 30, "valueMonth": 40, "valueEvent": 50, "cost": 'ssaasasa', "currency": "USDD"},
{"complete": True, "docID": "123", "integrationID": "456", "service": "789", "valueSec": 10, "valueb": 20, "valuebMonth": 30, "valueMonth": 40, "valueEvent": 50, "cost": 'assasasa', "currency": "EURO"},
{"complete": True, "docID": "123", "integrationID": "456", "service": "789", "valueSec": 10, "valueb": 20, "valuebMonth": 30, "valueMonth": 40, "valueEvent": 50, "cost": 'asasaasasaa'},
{"complete": True, "docID": "123", "integrationID": "456", "service": "789", "valueSec": 10, "valueb": 20, "valuebMonth": 30, "valueMonth": 40, "valueEvent": 50},
{"complete": True, "docID": "123", "integrationID": "456", "service": "789", "valueSec": 10, "valueb": 20, "valuebMonth": 30, "valueMonth": 40},
{"complete": True, "docID": "123", "integrationID": "456", "service": "789", "valueSec": 10, "valueb": 20, "valuebMonth": 30},
{"complete": True, "docID": "123", "integrationID": "456", "service": "789", "valueSec": 10, "valueb": 20},
{"complete": True, "docID": "123", "integrationID": "456", "service": "789", "valueSec": 10},
{"complete": True, "docID": "123", "integrationID": "456", "service": "789"},
{"complete": True, "docID": "123", "integrationID": "456"},
{"complete": True, "docID": "123"},
{"complete": True},
{"complete": 'llllll', "docID": "123", "integrationID": "456", "service": "789", "valueSec": 10, "valueb": 20, "valuebMonth": 30, "valueMonth": 40, "valueEvent": 50, "cost": 60, "currency": "USD"},
{"complete": False, "docID": "123", "integrationID": "456", "service": "789", "valueSec": 10, "valueb": 20, "valuebMonth": '78999jjkkk', "valueMonth": 40, "valueEvent": 50, "cost": 60, "currency": "USD"},
{"complete": True, "docID": "123", "integrationID": "456", "service": "789", "valueSec": 10, "valueb": 20, "valuebMonth": 'hhhhhh', "valueMonth": 40, "valueEvent": 50, "cost": 60, "currency": "RUB"},
{"complete": True, "docID": "123", "integrationID": "456", "service": "789", "valueSec": 10, "valueb": 20, "valuebMonth": 'ffdfd', "valueMonth": 40, "valueEvent": 50, "cost": 60, "currency": "USD", "extra": "extra"},
{"complete": True, "docID": "123", "integrationID": "456", "service": "789", "valueSec": 10, "valueb": 20, "valuebMonth": 'dfds', "valueMonth": 40, "valueEvent": 50, "cost": 60, "currency": "USD", "withdrawal": [{"currency": "USD", "amount": 10}]},
{"complete": True, "docID": "123", "integrationID": "456", "service": "789", "valueSec": 10, "valueb": 20, "valuebMonth": 'sdwwww', "valueMonth": 40, "valueEvent": 50, "cost": 60, "currency": "USD", "withdrawal": [{"currency": "USD", "amount": "10"}]}
]

dict_sh2_incorrect = [
    {"complete": "yes", "valueSec": 100, "disabled": {}},
    {"complete": True, "valueSec": "100", "disabled": {}},
    {"complete": True, "valueSec": 100, "disabled": "no"},
    {"complete": True, "valueSec": 100, "withdrawal": [{"currency": "EUR", "amount": 100}], "disabled": {}},
    {"complete": True, "valueSec": 100, "withdrawal": [{"currency": "USD", "amount": "100"}], "disabled": {}},
    {"complete": True, "valueSec": 100, "arr": [[1, 2, 3], ["4", 5, 6]], "disabled": {}},
    {"complete": True, "valueSec": 100, "withheld": {"cur": "USD", "am": "100"}, "disabled": {}},
    {"complete": True, "valueSec": 100, "put": [{"currency": "USD", "amount": 100, "name": {"cut": "50"}}], "disabled": {}},
    {"complete": True, "valueSec": 100, "put": [{"currency": "USD", "amount": 100, "name": {"cut": 50}}], "disabled": "no"},
    {"complete": 'false', "valueSec": 100, "disabled": {"status": "disabled"}},
    {"complete": True, "valueSec": 100, "withdrawal": [{"currency": "USD", "amount": 100}, ['RUB', 115]], "disabled": {"status": "disabled"}},
    {"complete": True, "valueSec": 100, "arr": [[1, 2, 3], [4, 5, 6], 7, 8, 9], "disabled": {"status": "disabled"}},
    {"complete": True, "valueSec": 100, "withheld": {"am": "USD"}, "disabled": {"status": "disabled"}},
    {"complete": True, "valueSec": 100, "put": [{"currency": "USD", "amount": 100, "name": ["cut", 50]}], "disabled": {"status": "disabled"}},
    {"complete": True, "valueSec": 100, "put": [{"currency": "USD", "amount": 100, "name": {"cut": 50}}, ['cut']], "disabled": ["status", "enabled"]}
]

dict_sh2_correct = [{"complete": True, "valueSec": 10, "withdrawal": [{"currency": "USD", "amount": 100}], "arr": [[1, 2, 3], [34, 12]], "withheld": {"cur": "fgggg", "am": 12.12}, "put": [{"currency": "RUB", "amount": 200, "name": {"cut": 1}}], "disabled": {'12': 234}},
{"complete": False, "valueSec": 20, "withdrawal": [{"currency": "RUB", "amount": 200}], "arr": [[4, 5, 6]], "withheld": {"cur": "fgggg", "am": 12.12}, "put": [{"currency": "USD", "amount": 300, "name": {"cut": 2}}], "disabled": {'12': 234}},
{"complete": True, "valueSec": 30, "withdrawal": [{"currency": "USD", "amount": 300}], "arr": [[7, 8, 9]], "withheld": {"cur": "fgggg", "am": 12.12}, "put": [{"currency": "RUB", "amount": 400, "name": {"cut": 3}}], "disabled": {'12': 234}},
{"complete": False, "valueSec": 40, "withdrawal": [{"currency": "RUB", "amount": 400}], "arr": [[10, 11, 12]], "withheld": {"cur": "fgggg", "am": 12.12}, "put": [{"currency": "USD", "amount": 500, "name": {"cut": 4}}], "disabled": {'12': 234}},
{"complete": True, "valueSec": 50, "withdrawal": [{"currency": "USD", "amount": 500}], "arr": [[13, 14, 15]], "withheld": {"cur": "fgggg", "am": 12.12}, "put": [{"currency": "RUB", "amount": 600, "name": {"cut": 5}}], "disabled": {'12': 234}},
{"complete": False, "valueSec": 60, "withdrawal": [{"currency": "RUB", "amount": 600}], "arr": [[16, 17, 18]], "withheld": {"cur": "fgggg", "am": 12.12}, "put": [{"currency": "USD", "amount": 700, "name": {"cut": 6}}], "disabled": {'12': 234}},
{"complete": True, "valueSec": 70, "withdrawal": [{"currency": "USD", "amount": 700}], "arr": [[19, 20, 21]], "withheld": {"cur": "fgggg", "am": 12.12}, "put": [{"currency": "RUB", "amount": 800, "name": {"cut": 7}}], "disabled": {'12': 234}},
{"complete": False, "valueSec": 80, "withdrawal": [{"currency": "RUB", "amount": 800}], "arr": [[22, 23, 24]], "withheld": {"cur": "fgggg", "am": 12.12}, "put": [{"currency": "USD", "amount": 900, "name": {"cut": 8}}], "disabled": {'12': 234}},
{"complete": True, "valueSec": 90, "withdrawal": [{"currency": "USD", "amount": 900}], "arr": [[25, 26, 27]], "withheld": {"cur": "fgggg", "am": 12.12}, "put": [{"currency": "RUB", "amount": 1000, "name": {"cut": 9}}], "disabled": {'12': 234}},
{"complete": False, "valueSec": 100, "withdrawal": [{"currency": "RUB", "amount": 1000}], "arr": [[28, 29, 30]], "withheld": {"cur": "fgggg", "am": 12.12}, "put": [{"currency": "USD", "amount": 1100, "name": {"cut": 10}}], "disabled": {'12': 234}},
 {"complete": True, "valueSec": 110, "withdrawal": [{"currency": "USD", "amount": 1100}], "arr": [[31, 32, 33]], "withheld": {"cur": "fgggg", "am": 12.12}, "put": [{"currency": "RUB", "amount": 1200, "name": {"cut": 11}}], "disabled": {'12': 234}},
{"complete": False, "valueSec": 120, "withdrawal": [{"currency": "RUB", "amount": 1200}], "arr": [[34, 35, 36]], "withheld": {"cur": "fgggg", "am": 12.12}, "put": [{"currency": "USD", "amount": 1300, "name": {"cut": 12}}], "disabled": {'12': 234}},
{"complete": True, "valueSec": 130, "withdrawal": [{"currency": "USD", "amount": 1300}], "arr": [[37, 38, 39]], "withheld": {"cur": "fgggg", "am": 12.12}, "put": [{"currency": "RUB", "amount": 1400, "name": {"cut": 13}}], "disabled": {'12': 234}},
{"complete": False, "valueSec": 140, "withdrawal": [{"currency": "RUB", "amount": 1400}], "arr": [[40, 41, 42]], "withheld": {"cur": "fgggg", "am": 12.12}, "put": [{"currency": "USD", "amount": 1500, "name": {"cut": 14}}], "disabled": {'12': 234}},
{"complete": True, "valueSec": 150, "withdrawal": [{"currency": "USD", "amount": 1500}], "arr": [[43, 44, 45]], "withheld": {"cur": "fgggg", "am": 12.12}, "put": [{"currency": "RUB", "amount": 1600, "name": {"cut": 15}}], "disabled": {'12': 234}},
{"complete": False, "valueSec": 160, "withdrawal": [{"currency": "RUB", "amount": 1600}], "arr": [[46, 47, 48]], "withheld": {"cur": "fgggg", "am": 12.12}, "put": [{"currency": "USD", "amount": 1700, "name": {"cut": 16}}], "disabled": {'12': 234}},
{"complete": True, "valueSec": 170, "withdrawal": [{"currency": "USD", "amount": 1700}], "arr": [[49, 50, 51]], "withheld": {"cur": "fgggg", "am": 12.12}, "put": [{"currency": "RUB", "amount": 1800, "name": {"cut": 17}}], "disabled": {'12': 234}},
{"complete": False, "valueSec": 180, "withdrawal": [{"currency": "RUB", "amount": 1800}], "arr": [[52, 53, 54]], "withheld": {"cur": "fgggg", "am": 12.12}, "put": [{"currency": "USD", "amount": 1900, "name": {"cut": 18}}], "disabled": {'12': 234}},
{"complete": True, "valueSec": 190, "withdrawal": [{"currency": "USD", "amount": 1900}], "arr": [[55, 56, 57]], "withheld": {"cur": "fgggg", "am": 12.12}, "put": [{"currency": "RUB", "amount": 2000, "name": {"cut": 19}}], "disabled": {'12': 234}},
{"complete": False, "valueSec": 200, "withdrawal": [{"currency": "RUB", "amount": 2000}], "arr": [[58, 59, 60]], "withheld": {"cur": "fgggg", "am": 12.12}, "put": [{"currency": "USD", "amount": 2100, "name": {"cut": 20}}], "disabled": {'12': 234}},
{"complete": True, "valueSec": 210, "withdrawal": [{"currency": "USD", "amount": 2100}], "arr": [[61, 62, 63]], "withheld": {"cur": "fgggg", "am": 12.12}, "put": [{"currency": "RUB", "amount": 2200, "name": {"cut": 21}}], "disabled": {'12': 234}},
{"complete": False, "valueSec": 220, "withdrawal": [{"currency": "RUB", "amount": 2200}], "arr": [[64, 65, 66]], "withheld": {"cur": "fgggg", "am": 12.12}, "put": [{"currency": "USD", "amount": 2300, "name": {"cut": 22}}], "disabled": {'12': 234}},
{"complete": True, "valueSec": 230, "withdrawal": [{"currency": "USD", "amount": 2300}], "arr": [[67, 68, 69]], "withheld": {"cur": "fgggg", "am": 12.12}, "put": [{"currency": "RUB", "amount": 2400, "name": {"cut": 23}}], "disabled": {'12': 234}},
 {"complete": False, "valueSec": 240, "withdrawal": [{"currency": "RUB", "amount": 2400}], "arr": [[70, 71, 72]], "withheld": {"cur": "fgggg", "am": 12.12}, "put": [{"currency": "USD", "amount": 2500, "name": {"cut": 24}}], "disabled": {'12': 234}},
{"complete": True, "valueSec": 250, "withdrawal": [{"currency": "USD", "amount": 2500}], "arr": [[73, 74, 75]], "withheld": {"cur": "fgggg", "am": 12.12}, "put": [{"currency": "RUB", "amount": 2600, "name": {"cut": 25}}], "disabled": {'12': 234}},
{"complete": False, "valueSec": 260, "withdrawal": [{"currency": "RUB", "amount": 2600}], "arr": [[76, 77, 78]], "withheld": {"cur": "fgggg", "am": 12.12}, "put": [{"currency": "USD", "amount": 2700, "name": {"cut": 26}}], "disabled": {'12': 234}},
{"complete": True, "valueSec": 270, "withdrawal": [{"currency": "USD", "amount": 2700}], "arr": [[79, 80, 81]], "withheld": {"cur": "fgggg", "am": 12.12}, "put": [{"currency": "RUB", "amount": 2800, "name": {"cut": 27}}], "disabled": {'12': 234}},
{"complete": False, "valueSec": 280, "withdrawal": [{"currency": "RUB", "amount": 2800}], "arr": [[82, 83, 84]], "withheld": {"cur": "fgggg", "am": 12.12}, "put": [{"currency": "USD", "amount": 2900, "name": {"cut": 28}}], "disabled": {'12': 234}},
{"complete": True, "valueSec": 290, "withdrawal": [{"currency": "USD", "amount": 2900}], "arr": [[85, 86, 87]], "withheld": {"cur": "fgggg", "am": 12.12}, "put": [{"currency": "RUB", "amount": 3000, "name": {"cut": 29}}], "disabled": {'12': 234}},
{"complete": False, "valueSec": 300, "withdrawal": [{"currency": "RUB", "amount": 3000}], "arr": [[88, 89, 90]], "withheld": {"cur": "fgggg", "am": 12.12}, "put": [{"currency": "USD", "amount": 3100, "name": {"cut": 30}}], "disabled": {'12': 234}}
]

dict_sh4_correct = [{"user": {"name": "John Doe", "email": "johndoe@gmail.com", "address": {"street": "123 Main St", "city": "New York", "country": "USA"}}, "products": [{"name": "Apple", "price": 1.2, "quantity": 10}]},
{"user": {"name": "Jane Smith", "email": "janesmith@yahoo.com", "address": {"street": "456 Elm St", "city": "Los Angeles", "country": "USA"}}, "products": [{"name": "Banana", "price": 0.5, "quantity": 20}]},
{"user": {"name": "Bob Johnson", "email": "bob.johnson@hotmail.com", "address": {"street": "789 Pine St", "city": "Chicago", "country": "USA"}}, "products": [{"name": "Orange", "price": 0.8, "quantity": 15}]},
{"user": {"name": "Alice Williams", "email": "alice.williams@gmail.com", "address": {"street": "321 Oak St", "city": "Houston", "country": "USA"}}, "products": [{"name": "Pear", "price": 1.5, "quantity": 12}]},
{"user": {"name": "Charlie Brown", "email": "charlie.brown@yahoo.com", "address": {"street": "654 Maple St", "city": "Phoenix", "country": "USA"}}, "products": [{"name": "Grape", "price": 2.0, "quantity": 18}]},
{"user": {"name": "David Davis", "email": "david.davis@hotmail.com", "address": {"street": "987 Cedar St", "city": "Philadelphia", "country": "USA"}}, "products": [{"name": "Strawberry", "price": 2.5, "quantity": 22}]},
{"user": {"name": "Emily Evans", "email": "emily.evans@gmail.com", "address": {"street": "147 Spruce St", "city": "San Antonio", "country": "USA"}}, "products": [{"name": "Blueberry", "price": 3.0, "quantity": 25}]},
{"user": {"name": "Frank Foster", "email": "frank.foster@yahoo.com", "address": {"street": "258 Birch St", "city": "San Diego", "country": "USA"}}, "products": [{"name": "Raspberry", "price": 3.5, "quantity": 28}]},
{"user": {"name": "Grace Green", "email": "grace.green@hotmail.com", "address": {"street": "369 Willow St", "city": "Dallas", "country": "USA"}}, "products": [{"name": "Blackberry", "price": 4.0, "quantity": 30}]},
 {"user": {"name": "Henry Harris", "email": "henry.harris@gmail.com", "address": {"street": "741 Hickory St", "city": "San Jose", "country": "USA"}}, "products": [{"name": "Cherry", "price": 4.5, "quantity": 35}]},
{"user": {"name": "Irene Isaac", "email": "irene.isaac@yahoo.com", "address": {"street": "852 Walnut St", "city": "Austin", "country": "USA"}}, "products": [{"name": "Peach", "price": 5.0, "quantity": 40}]},
{"user": {"name": "Jack Jackson", "email": "jack.jackson@hotmail.com", "address": {"street": "963 Chestnut St", "city": "Jacksonville", "country": "USA"}}, "products": [{"name": "Plum", "price": 5.5, "quantity": 45}]},
{"user": {"name": "Kathy King", "email": "kathy.king@gmail.com", "address": {"street": "147 Aspen St", "city": "San Francisco", "country": "USA"}}, "products": [{"name": "Kiwi", "price": 6.0, "quantity": 50}]},
{"user": {"name": "Larry Lewis", "email": "larry.lewis@yahoo.com", "address": {"street": "258 Beech St", "city": "Indianapolis", "country": "USA"}}, "products": [{"name": "Lemon", "price": 6.5, "quantity": 55}]},
{"user": {"name": "Molly Moore", "email": "molly.moore@hotmail.com", "address": {"street": "369 Cedar St", "city": "Columbus", "country": "USA"}}, "products": [{"name": "Lime", "price": 7.0, "quantity": 60}]},
{"user": {"name": "Nancy Nelson", "email": "nancy.nelson@gmail.com", "address": {"street": "741 Dogwood St", "city": "Fort Worth", "country": "USA"}}, "products": [{"name": "Mango", "price": 7.5, "quantity": 65}]},
{"user": {"name": "Oscar Olson", "email": "oscar.olson@yahoo.com", "address": {"street": "852 Elm St", "city": "Charlotte", "country": "USA"}}, "products": [{"name": "Melon", "price": 8.0, "quantity": 70}]},
{"user": {"name": "Patty Peterson", "email": "patty.peterson@hotmail.com", "address": {"street": "963 Fir St", "city": "Detroit", "country": "USA"}}, "products": [{"name": "Nectarine", "price": 8.5, "quantity": 75}]},
{"user": {"name": "Quincy Quinn", "email": "quincy.quinn@gmail.com", "address": {"street": "147 Gum St", "city": "El Paso", "country": "USA"}}, "products": [{"name": "Papaya", "price": 9.0, "quantity": 80}]},
{"user": {"name": "Randy Robinson", "email": "randy.robinson@yahoo.com", "address": {"street": "258 Holly St", "city": "Memphis", "country": "USA"}}, "products": [{"name": "Pineapple", "price": 9.5, "quantity": 85}]},
{"user": {"name": "Sally Smith", "email": "sally.smith@hotmail.com", "address": {"street": "369 Ivy St", "city": "Baltimore", "country": "USA"}}, "products": [{"name": "Pomegranate", "price": 10.0, "quantity": 90}]},
{"user": {"name": "Tom Thompson", "email": "tom.thompson@gmail.com", "address": {"street": "741 Jasmine St", "city": "Boston", "country": "USA"}}, "products": [{"name": "Raspberry", "price": 10.5, "quantity": 95}]},
{"user": {"name": "Ursula Underwood", "email": "ursula.underwood@yahoo.com", "address": {"street": "852 Kudzu St", "city": "Nashville", "country": "USA"}}, "products": [{"name": "Strawberry", "price": 11.0, "quantity": 100}]},
{"user": {"name": "Victor Vance", "email": "victor.vance@hotmail.com", "address": {"street": "963 Lilac St", "city": "Louisville", "country": "USA"}}, "products": [{"name": "Tangerine", "price": 11.5, "quantity": 105}]},
{"user": {"name": "Wendy White", "email": "wendy.white@gmail.com", "address": {"street": "147 Magnolia St", "city": "Milwaukee", "country": "USA"}}, "products": [{"name": "Ugli Fruit", "price": 12.0, "quantity": 110}]},
{"user": {"name": "Xavier Xiong", "email": "xavier.xiong@yahoo.com", "address": {"street": "258 Nectarine St", "city": "Portland", "country": "USA"}}, "products": [{"name": "Vitamin C", "price": 12.5, "quantity": 115}]},
{"user": {"name": "Yvonne Young", "email": "yvonne.young@hotmail.com", "address": {"street": "369 Olive St", "city": "Las Vegas", "country": "USA"}}, "products": [{"name": "Watermelon", "price": 13.0, "quantity": 120}]},
{"user": {"name": "Zachary Zimmerman", "email": "zachary.zimmerman@gmail.com", "address": {"street": "741 Peach St", "city": "Oklahoma City", "country": "USA"}}, "products": [{"name": "Xigua", "price": 13.5, "quantity": 125}]},
{"user": {"name": "Amy Adams", "email": "amy.adams@yahoo.com", "address": {"street": "852 Quince St", "city": "Albuquerque", "country": "USA"}}, "products": [{"name": "Yam", "price": 14.0, "quantity": 130}]},
{"user": {"name": "Brian Brown", "email": "brian.brown@hotmail.com", "address": {"street": "963 Raspberry St", "city": "Tucson", "country": "USA"}}, "products": [{"name": "Zucchini", "price": 14.5, "quantity": 135}]}
]

dict_sh4_incorrect = [{"user": {"name": {}, "email": "john@example.com", "address": {"street": "Main St", "city": "New York", "country": "USA"}}, "products": [{"name": "Apple", "price": 1.2, "quantity": 10}]},
{"user": {"name": None, "email": "john@example.com", "address": {"street": ['Main St'], "city": "New York", "country": "USA"}}, "products": [{"name": "Apple", "price": 1.2, "quantity": 10}]},
{"user": {"name": "John Doe", "email": "john@example.com", "address": {"street": "Main St", "city": [123], "country": "USA"}}, "products": [{"name": "Apple", "price": 1.2, "quantity": 10}]},
{"user": {"name": "John Doe", "email": "john@example.com", "address": {"street": "Main St", "city": "New York", "country": [123]}}, "products": [{"name": "Apple", "price": 1.2, "quantity": 10}]},
{"user": {"name": "John Doe", "email": "john@example.com", "address": {"street": "Main St", "city": "New York", "country": "USA"}}, "products": [{"name": [123], "price": 1.2, "quantity": 10}]},
{"user": {"name": "John Doe", "email": "john@example.com", "address": {"street": "Main St", "city": "New York", "country": "USA"}}, "products": [{"name": "Apple", "price": ["1.2"], "quantity": 10}]},
{"user": {"name": "John Doe", "email": "john@example.com", "address": {"street": "Main St", "city": "New York", "country": "USA"}}, "products": [{"name": "Apple", "price": 1.2, "quantity": ["10"]}]},
{"user": {"name": "John Doe", "email": "john@example.com", "address": {"street": "Main St", "city": "New York", "country": "USA"}}, "products": [{"name": "Apple", "price": 1.2}]},
{"user": {"name": "John Doe", "email": "john@example.com", "address": {"street": "Main St", "city": "New York"}}, "products": [{"name": "Apple", "price": 1.2, "quantity": 10}]},
{"user": {"name": "John Doe", "email": "john@example.com", "address": {"street": "Main St"}}, "products": [{"name": "Apple", "price": 1.2, "quantity": 10}]},
{"user": {"name": "John Doe", "email": "john@example.com"}, "products": [{"name": "Apple", "price": 1.2, "quantity": 10}]},
{"user": {"name": "John Doe"}, "products": [{"name": "Apple", "price": 1.2, "quantity": 10}]},
{"user": {}, "products": [{"name": "Apple", "price": 1.2, "quantity": 10}]},
{"products": [{"name": "Apple", "price": 1.2, "quantity": 10}]},
{"user": {"name": "John Doe", "email": False, "address": {"street": "Main St", "city": "New York", "country": "USA"}}, "products": []},
{"user": {"name": "John Doe", "email": "john@example.com", "address": {"street": "Main St", "city": "New York", "country": "USA"}}},
{"user": {"name": "John Doe", "email": None, "address": {"street": "Main St", "city": "New York", "country": "USA"}}, "products": [{}]},
{"user": {"name": "John Doe", "email": "john@example.com", "address": {"street": "Main St", "city": "New York", "country": "USA"}}, "products": [{"name": "Apple"}]},
{"user": {"name": "John Doe", "email": "john@example.com", "address": {"street": "Main St", "city": "New York", "country": "USA"}}, "products": [{"price": 1.2}]},
{"user": {"name": "John Doe", "email": "john@example.com", "address": {"street": "Main St", "city": "New York", "country": "USA"}}, "products": [{"quantity": 10}]},
{"user": {"name": "John Doe", "email": None, "address": {"street": "Main St", "city": "New York", "country": "USA"}}, "products": [{"name": "Apple", "price": ';;;;;', "quantity": 10,}]}
]


dict_sh5_incorrect = [
    {"user": {"id": "123", "name": "John", "email": "john@gmail.com", "address": {"street": "Main", "city": "New York", "country": "USA", "postalCode": "10001", "coordinates": {"latitude": 40.7128, "longitude": 74.0060}}}, "transaction": {"id": "456", "amount": 1000, "currency": "EUR", "date": None}},
    {"user": {"id": "123", "name": "John", "email": "john@gmail.com", "address": {"street": "Main", "city": "New York", "country": "USA", "postalCode": "10001", "coordinates": {"latitude": 40.7128, "longitude": 74.0060}}}, "transaction": {"id": "456", "amount": 1000, "currency": "USD"}},
    {"user": {"id": "123", "name": "John", "email": "john@gmail.com", "address": {"street": "Main", "city": "New York", "country": "USA", "postalCode": "10001", "coordinates": {"latitude": 40.7128, "longitude": 74.0060}}}, "transaction": {"id": "456", "amount": 1000, "currency": "USDT", "date": "2022-01-01T00:00:00Z"}},
    {"user": {"id": "123", "name": "John", "email": "john@gmail.com", "address": {"street": "Main", "city": "New York", "country": "USA", "postalCode": "10001", "coordinates": {"longitude": 74.0060}}}, "transaction": {"id": "456", "amount": 1000, "currency": "USD", "date": "2022-01-01T00:00:00Z"}},
    {"user": {"id": "123", "name": "John", "email": "john@gmail.com", "address": {"street": "Main", "city": "New York", "country": "USA", "postalCode": "10001", "coordinates": {"latitude": 40.7128, "longitude": 74.0060}}}, "transaction": {"amount": 1000, "currency": "USD", "date": "2022-01-01T00:00:00Z"}},
    {"user": {"id": "123", "name": "John", "email": "john@gmail.com", "address": {"street": "Main", "city": "New York", "country": "USA", "postalCode": "10001", "coordinates": {"latitude": 40.7128, "longitude": 74.0060}}}, "transaction": {"id": ["456"], "amount": 1000, "currency": "USD", "date": "2022-01-01T00:00:00Z"}},
    {"user": {"id": "123", "name": "John", "email": "john@gmail.com", "address": {"street": "Main", "city": "New York", "country": "USA", "postalCode": "10001", "coordinates": {"latitude": 40.7128, "longitude": 74.0060}}}, "transaction": {"id": "456", "amount": 1000, "date": "2022-01-01T00:00:00Z"}},
    {"user": {"id": "123", "name": "John", "email": "john@gmail.com", "address": {"street": "Main", "city": "New York", "country": "USA", "coordinates": {"latitude": 40.7128, "longitude": 74.0060}}}, "transaction": {"id": "456", "amount": 1000, "currency": "USD"}},
    {"user": {"id": "123", "name": "John", "email": "john@gmail.com", "address": {"street": "Main", "city": "New York", "postalCode": "10001", "coordinates": {"latitude": 40.7128, "longitude": 74.0060}}}, "transaction": {"id": "456", "amount": 1000, "currency": "USD", "date": "2022-01-01T00:00:00Z"}},
    {"user": {"id": "123", "name": "John", "email": "john@gmail.com", "address": {"street": "Main", "city": "New York", "country": "USA", "postalCode": "10001", "coordinates": {"latitude": 40.7128, "longitude": 74.0060}}}},
    {"user": {"id": "123", "name": "John", "email": "john@gmail.com", "address": {"street": ["Main"], "city": "New York", "country": "USA", "postalCode": "10001r", "coordinates": {"latitude": 40.7128, "longitude": 74.0060}}}, "transaction": {"id": "456", "amount": 1000, "currency": "USD", "date": "2022-01-01T00:00:00Z"}},
    {"user": {"id": "123", "name": "John", "email": "john@gmail.com", "address": {"street": "Main", "city": ["New York"], "country": "USA", "postalCode": "10001", "coordinates": {"latitude": 'rival', "longitude": 74.0060}}}, "transaction": {"id": "456", "amount": 1000, "currency": "USD", "date": "2022-01-01T00:00:00Z"}},
    {"user": {"id": "123", "name": "John", "email": "john@gmail.com", "address": {"street": "Main", "city": "New York", "country": "USA", "postalCode": "10001", "coordinates": {"latitude": 40.7128, "longitude": 74.0060}}}, "transaction": {"id": "456", "amount": 'iii', "currency": "USD", "date": "2022-01-01T00:00:00Z"}},
    {"user": {"id": "123", "name": "John", "email": "john@gmail.com", "address": {"street": "Main", "city": "New York", "country": "USA", "postalCode": "10001", "coordinates": {"latitude": 40.7128, "longitude": '34hamp'}}}, "transaction": {"id": "456", "amount": 1000, "currency": "USD", "date": "2022-01-01T00:00:00Z"}},
    {"user": {"id": "123", "name": "John", "email": "john@gmail.com", "address": ["Main", "New York","USA", "10001"], "transaction": {"id": "456", "amount": 1000, "currency": "USD", "date": False}}}]


dict_sh5_correct = [
    {"user": {"id": 'None', "name": "John", "email": "john@gmail.com", "address": {"street": 567839034, "city": "New York", "country": "USA", "postalCode": "10001", "coordinates": {"latitude": 40.7128, "longitude": 74.0060}}}, "transaction": {"id": "123", "amount": 100.0, "currency": "USD", "date": "2021-01-01T00:00:00Z"}},
    {"user": {"id": "123", "name": 123, "email": "john@gmail.com", "address": {"street": "Main St", "city": "New York", "country": "USA", "postalCode": "10001", "coordinates": {"latitude": 40.7128, "longitude": 74.0060}}}, "transaction": {"id": "123", "amount": 100.0, "currency": "USD", "date": "2021-01-01T00:00:00Z"}},
    {"user": {"id": "123", "name": "John", "email": 123, "address": {"street": "Main St", "city": "New York", "country": "USA", "postalCode": "10001", "coordinates": {"latitude": 40.7128, "longitude": 74.0060}}}, "transaction": {"id": "123", "amount": 100.0, "currency": "USD", "date": "2021-01-01T00:00:00Z"}},
    {"user": {"id": "123", "name": "John", "email": "john@gmail.com", "address": {"street": 123, "city": "New York", "country": "USA", "postalCode": "10001", "coordinates": {"latitude": 40.7128, "longitude": 74.0060}}}, "transaction": {"id": "123", "amount": 100.0, "currency": "USD", "date": "2021-01-01T00:00:00Z"}},
    {"user": {"id": "123", "name": "John", "email": "john@gmail.com", "address": {"street": "Main St", "city": 123, "country": "USA", "postalCode": "10001", "coordinates": {"latitude": 40.7128, "longitude": 74.0060}}}, "transaction": {"id": "123", "amount": 100.0, "currency": "USD", "date": "2021-01-01T00:00:00Z"}},
    {"user": {"id": "123", "name": "John", "email": "john@gmail.com", "address": {"street": "Main St", "city": "New York", "country": 123, "postalCode": "10001", "coordinates": {"latitude": 40.7128, "longitude": 74.0060}}}, "transaction": {"id": "123", "amount": 100.0, "currency": "USD", "date": "2021-01-01T00:00:00Z"}},
    {"user": {"id": "123", "name": "John", "email": "john@gmail.com", "address": {"street": "Main St", "city": "New York", "country": "USA", "postalCode": 123, "coordinates": {"latitude": 40.7128, "longitude": 74.0060}}}, "transaction": {"id": "123", "amount": 100.0, "currency": "USD", "date": "2021-01-01T00:00:00Z"}},
    {"user": {"id": "123", "name": "John", "email": "john@gmail.com", "address": {"street": "Main St", "city": "New York", "country": "USA", "postalCode": "10001", "coordinates": {"latitude": "40.7128", "longitude": 74.0060}}}, "transaction": {"id": "123", "amount": 100.0, "currency": "USD", "date": "2021-01-01T00:00:00Z"}},
    {"user": {"id": "123", "name": "John", "email": "john@gmail.com", "address": {"street": "Main St", "city": "New York", "country": "USA", "postalCode": "10001", "coordinates": {"latitude": 40.7128, "longitude": "74.0060"}}}, "transaction": {"id": "123", "amount": 100.0, "currency": "USD", "date": "2021-01-01T00:00:00Z"}},
    {"user": {"id": "123", "name": "John", "email": "john@gmail.com", "address": {"street": "Main St", "city": "New York", "country": "USA", "postalCode": "10001", "coordinates": {"latitude": 40.7128, "longitude": 74.0060}}}, "transaction": {"id": 123, "amount": 100.0, "currency": "USD", "date": "2021-01-01T00:00:00Z"}},
    {"user": {"id": "123", "name": "John", "email": "john@gmail.com", "address": {"street": "Main St", "city": "New York", "country": "USA", "postalCode": "10001", "coordinates": {"latitude": 40.7128, "longitude": 74.0060}}}, "transaction": {"id": "123", "amount": "100.0", "currency": "USD", "date": "2021-01-01T00:00:00Z"}},
    {"user": {"id": "123", "name": 12344567, "email": "john@gmail.com", "address": {"street": "Main St", "city": "New York", "country": "USA", "postalCode": "10001", "coordinates": {"latitude": 40.7128, "longitude": 74.0060}}}, "transaction": {"id": "123", "amount": 100.0, "currency": 'RUB', "date": "2021-01-01T00:00:00Z"}},
    {"user": {"id": "123", "name": "John", "email": "john@gmail.com", "address": {"street": "Main St", "city": "New York", "country": "USA", "postalCode": "10001", "coordinates": {"latitude": 40.7128, "longitude": 74.0060}}}, "transaction": {"id": "123", "amount": 100.0, "currency": "USD", "date": 123}},
    {"user": {"id": "123", "name": "John", "email": "john@gmail.com", "address": {"street": "Main St", "city": "New York", "country": "USA", "postalCode": "10001", "coordinates": {"latitude": 40.7128, "longitude": 74.0060}}}, "transaction": {"id": "123", "amount": '345.234', "currency": "USD", "date": 'False'}},
    {"user": {"id": "123", "name": "John", "email": "john@gmail.com", "address": {"street": "Main St", "city": "New York", "country": "USA", "postalCode": 10001, "coordinates": {"latitude": 40.7128, "longitude": 74.0060}}}, "transaction": {"id": "123", "amount": 100.0, "currency": "USD", "date": 'None'}} # correct cuz required type str
]
from JS_DICT import JSON
from test_dicts import *
from test_schemas import *


def warning(warn):
    print (warn)


def error(err):
    print (err)

def assert_true(test_dict, schema):
    print ('\n***')
    js = JSON (test_dict)
    correct = js.validate (schema, warning_callback=warning, error_callback=error)
    print(js)
    assert correct
    print(f'{"_"*20} if there are no warnings under the line, then the dictionary has been successfully corrected {"_"*20}')
    assert js.validate(schema, warning_callback=warning, error_callback=error) # assert dict is corrected according to the scheme and types required

def assert_false(test_dict, schema):
    print ('\n***')
    js = JSON (test_dict)
    incorrect = js.validate (schema, warning_callback=warning, error_callback=error)
    assert incorrect is False



def assert_valid():
    """ all testing dicts is placed in test_dicts file
        all testing schemas is placed in test_schemas"""

    assert_true(dict1_1, sch1)
    assert_true(dict1_2, sch1)
    assert_true(dict1_3, sch1)

    assert_false(dict1_4, sch1)
    assert_false(dict1_5, sch1)
    assert_false(dict1_6, sch1)
    assert_false(dict1_7, sch1)
    assert_false(dict1_9, sch1)
    assert_false(dict1_8, sch1)

    assert_true(dict2_1, sch2)
    assert_true(dict2_2, sch2)
    assert_true(dict2_2_1, sch2)

    assert_false(dict2_3, sch2)

    assert_true(dict3_1, sch3)
    assert_true(dict3_2, sch3)

    assert_false(dict3_3, sch3)


def assert_json_dict():
    test = JSON ({'12': {'1212': [7889, 34], '288282': {'00': [9999, 89]}}, '12121': 111111})

    test['lsrt.78.345'] = 44
    test[['34', '14', '56', '666']] = 'fast light'
    # set or get value using testing['a.b'] or testing['a','b'] or testing[['a','b']] or testing[('a','b')]. if no value is given None is returned
    test[('9', '22', '11', '666', '14', '14')] = [12, 23, 44]
    test[('mkdir', '9', '22', '11', 'ls', '14', '14')] = [12, 23, 44]

    assert test['lsrt.78.345'] == 44
    assert test['lsrt', '78', '345'] == 44
    assert test[('lsrt', '78', '345')] == 44
    assert test[['lsrt', '78', '345']] == 44
    assert test[['lsrt', '78', '2222']] is None
    assert test['lsrt', '444', '345'] is None
    assert test['33.78.345'] is None

    assert test['9', '22', '11', '666', '14', '14'] == [12, 23, 44]
    assert test['9.22.11.666.14.14'] == [12, 23, 44]

    assert test == {'12': {'1212': [7889, 34], '288282': {'00': [9999, 89]}}, '12121': 111111, 'lsrt': {'78': {'345': 44}},
                    '34': {'14': {'56': {'666': 'fast light'}}}, '9': {'22': {'11': {'666': {'14': {'14': [12, 23, 44]}}}}},
                    'mkdir': {'9': {'22': {'11': {'ls': {'14': {'14': [12, 23, 44]}}}}}}}

    tst_similar_val = JSON({}, no_replacement_for_the_first=True) # doesnt work yet with the dicts with dimensions less then 3!
    tst_similar_val['lsrt.78.345'] = 44
    tst_similar_val['lsrt.33.345'] = 23
    tst_similar_val['lsrt', '12', '345'] = 44
    tst_similar_val['lsrt.78.355'] = 44
    tst_similar_val['lsrt.355.2222.222212.lll.221'] = 11

    assert tst_similar_val == {'lsrt': {'78': {'355': 44}, '33': {'345': 23}, '12': {'345': 44}, '355': {'2222': {'222212': {'lll': {'221': 11}}}}}}

    tst_not_sim = JSON ({})
    tst_not_sim['lsrt.355.2222.222212.lll.221'] = 11
    tst_not_sim['lsrt.78.345'] = 44
    tst_not_sim['lsrt.33.345'] = 23
    tst_not_sim['lsrt.12.345'] = 44
    tst_not_sim['lsrt.78.355'] = 44

    assert tst_not_sim == {'lsrt': {'78': {'355': 44}}}






def assert_gpt_test():
    for i in dict_sh1_correct: # 30 test dicts tested on sch1
        assert_true(i, sch1)

    for i in dict_sh1_incorrect:
        assert_false(i, sch1)

    for i in dict_sh2_incorrect:
        assert_false (i, sch2)

    for i in dict_sh2_correct:
        assert_true(i, sch2)

    for i in dict_sh4_correct:
        assert_true(i, sch4)

    for i in dict_sh4_incorrect:
        assert_false(i, sch4)

    for i in dict_sh5_incorrect:
        assert_false(i, sch5)

    for i in dict_sh5_correct:
        assert_true(i, sch5)


if __name__ == '__main__':
    assert_valid()
    assert_json_dict()
    assert_gpt_test()















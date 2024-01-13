""""надо создать класс JSON который расширяет возможности dict:

test = JSON(some dict)

* можно обращаться (читать/писать) к вложенным элементам любым способом: test['a.b'] или test['a','b'] или test[['a','b']] или test[('a','b')].
Если элемента/пути нет вернёт None, если производим запись - создаст весь путь

* есть свойство plain - все поля в одном массиве формате {"full_path" : value}

* класс запоминает все изменения вносимые в данные после инициализации

* в классе не используется обработка исключений"""

def one_dimension_dic(muldd, prt_key:str='', sep:str='.'):
    array = []
    for k, v in muldd.items():
        k = str(k)
        new_key = prt_key + sep + k if prt_key else k
        if isinstance(v, dict):
            array.extend(one_dimension_dic(v, new_key, sep=sep).items())
        else:
            array.append((new_key, v))
    return dict(array)

def get_plain(muldd):
    result = [{key: value} for key, value in one_dimension_dic(muldd).items()]
    return result

class JSON(dict):
    def __init__(self, some_dict: dict):
        super ().__init__ ()
        self.update(some_dict)

    def __missing__(self, key):
        if isinstance(key, tuple):
            res = self[key[0]]
            for num in range (1, len (key)):
                if not res:
                    return None
                if (res is None) or ((num != (len(key))) and (not isinstance(res, dict))):
                    return None
                if res.__contains__(key[num]):
                    res = res.__getitem__(key[num])
                else:
                    return None
            return res
        return None

    def new_dic(self, key, val):
        mew_dic = {}
        mew_dic[key] = val
        return mew_dic

    def plain(self):
        res = [{key: value} for key, value in one_dimension_dic (self).items ()]
        return res

    def __setitem__(self, key, value):
        if '.' in key:
            item = tuple (reversed([i for i in key.split ('.')]))
            new_dic = {}
            new_dic[item[0]] = value
            for i in item[1:-1]:
                new_dic = self.new_dic(i, new_dic)
            super (JSON, self).__setitem__ (item[-1], new_dic)
        elif isinstance (key, list|tuple):
            item = tuple (reversed([i for i in key]))
            new_dic = {}
            new_dic[item[0]] = value
            for i in item[1:-1]:
                new_dic = self.new_dic (i, new_dic)
            super (JSON, self).__setitem__ (item[-1], new_dic)

        else:
            super(JSON, self).__setitem__(key, value)

    def __getitem__(self, item):
        if '.' in item:
            item = tuple(i for i in item.split('.'))
        if isinstance(item, list):
            item = tuple(i for i in item)
        return super(JSON, self).__getitem__(item)


if __name__ == '__main__':
    test = JSON({'12': {'1212': [7889, 34], '288282': {'00': [9999, 89]}}, '12121': 111111})

    test['lsrt.78.345'] = 44
    test[['34', '14', '56', '666']] = 'fast light'
    # test['a.b'] или test['a','b'] или test[['a','b']] или test[('a','b')].
    test[('9', '22', '11', '666', '14', '14')] = [12, 23, 44]
    test[('mkdir', '9', '22', '11', 'ls', '14', '14')] = [12, 23, 44]
    print(test, '\n')
    print(test['mkdir.9.22'], '\n')
    print (test['lsrt', '78'], '\n')
    print(test.plain())




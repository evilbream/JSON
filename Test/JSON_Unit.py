import unittest

from firebase_admin import firestore
from google.cloud.firestore_v1 import ArrayUnion, ArrayRemove

from JS_DICT import JSON

class TestJSON(unittest.TestCase):
    def setUp(self):
        self.json = JSON({
            "a": 1,
            "b": {
                "c":
                    {"e": 11,
                     "f":
                         {"j": 12, "k": 13}},
                "d": [3, 4, 5]
            }
        })

    def test_plain(self):
        expected = [{'a': 1}, {'b.c.e': 11}, {'b.c.f.j': 12}, {'b.c.f.k': 13}, {'b.d': [3, 4, 5]}]
        self.assertEqual(self.json.plain(), expected)

    def test_get_existing_key(self):
        self.assertEqual(self.json.get("a"), 1)
        self.assertEqual (self.json.get ("b.d"), [3, 4, 5])
        self.assertEqual (self.json.get (["b", "d"]), [3, 4, 5])
        self.assertEqual (self.json.get ("b.c.f.j"), 12)
        self.assertEqual (self.json.get ("b"), {'c': {'e': 11, 'f': {'j': 12, 'k': 13}}, "d": [3, 4, 5]})
        self.assertEqual (self.json.get ("b.c.f"), {'j': 12, 'k': 13})

    def test_get_nonexistent_key(self):
        self.assertIsNone (self.json.get ("a.f"))
        self.assertIsNone (self.json.get ("a.f"))
        self.assertIsNone (self.json.get ("r.f"))
        self.assertIsNone (self.json.get (['a', 'b']))
        self.assertIsNone (self.json.get (['g', 'd', '45']))

    def test_get_nonexistent_key_with_default_value(self):
        self.assertEqual(self.json.get("nonexistent_key", "default_value"), "default_value")
        self.assertEqual (self.json.get ("a.f", {}), {})
        self.assertEqual (self.json.get ("r.f", {}), {})
        self.assertEqual (self.json.get (['a', 'b'], '56'), '56')
        self.assertEqual (self.json.get (['g', 'd', '45'], '22'), '22')

    def test_contains_existent(self):
        self.assertTrue(["b", "d"] in self.json)
        self.assertTrue ("b" in self.json)
        self.assertTrue (["b", "d"] in self.json)
        self.assertTrue ("b.c.f.j" in self.json)
        self.assertTrue (["b.c.f"] in self.json)


    def test_contains_nonexistent(self):
        self.assertFalse("k" in self.json)
        self.assertFalse ("b.c.l.j" in self.json)
        self.assertFalse ("b.l" in self.json)
        self.assertFalse ("p" in self.json)
        self.assertFalse (["b", "c", "v"] in self.json)

    def test__fb_update_mask(self):
        oldValue = {'12': {'1212': [7889, 34], '288282': {'00': [9999, 89]}}, '12121': 111111}
        value = {'12': {'1212': [234, 34], '288282': {'00': [9999, 89]}}, '12121': 111111}
        js = JSON(value, oldValue=oldValue)
        self.assertEqual({'12.1212': [234, 34]}, js._fb_update_mask)

    def test_fb_update_mask_add_key(self):
        oldValue = {'a': 123, 'b': {'c': [1, 2, 3, 4, 5], 'd': [3, 4, 5], 'e': {}}, 1: {1: 123}}
        value = {'n': None, 'a': 123, 'b': {'c': [1, 2, 3, 4, 5], 'd': [3, 4, 5], 'e': {}}, 1: {1: 123}}
        json = JSON(value, oldValue=oldValue)
        self.assertEqual(json._fb_update_mask, {'n': None})

    def test_fb_update_mask_update_array(self):
        oldValue = {'a': 123, 'b': {'c': [1, 2, 3, 4, 5], 'd': [3, 4, 5], 'e': {}}, 1: {1: 123}}
        value = {'a': 123, 'b': {'c': [1, 2, 3, 4, 5, 6]}, 1: {1: 123}, 'd': None}
        json = JSON(value, oldValue=oldValue)
        self.assertEqual(
            json._fb_update_mask,
            {'b.c': ArrayUnion([6]),
             'b.d': firestore.DELETE_FIELD,
             'b.e': firestore.DELETE_FIELD,
             'd': None}
        )

    def test_fb_update_mask_element(self):
        oldValue= {'a': 123, 'b': {'c': [1, 2, 3, 4, 5], 'd': [3, 4, 5], 'e': {}}, 1: {1: 123}}
        value = {'a': 123, 'b': {'c': [1, 2, 3, 4, 5], 'd': [3, 4, 5], 'e': {}}, 1: {1: 123}, 'z': {'c': {}}}
        json = JSON(value, oldValue=oldValue)
        self.assertEqual(json._fb_update_mask, {'z.c': {}})

    def test_remove_from_array(self):
        oldValue = {'a': 123, 'b': {'c': [1, 2, 3, 4, 5], 'd': [3, 4, 5], 'e': {1, 2}}, 1: {1: 123}}
        value = {'a': 123, 'b': {'c': [1, 2, 3], 'd': [3, 4, 5], 'e': {1, 2}}, 1: {1: 123}}
        json = JSON(value, oldValue=oldValue)
        self.assertEqual(json._fb_update_mask, {'b.c': ArrayRemove([4, 5])})

    def test_add_to_array(self):
        oldValue = {'a': 123, 'b': {'c': [1, 2, 3, 4, 5], 'd': [3, 4, 5], 'e': {1, 2}}, 1: {1: 123}}
        value = {'a': 123, 'b': {'c': [1, 2, 3, 4, 5, 6, 7, 8], 'd': [3, 4, 5], 'e': {1, 2}}, 1: {1: 123}}
        json = JSON(value, oldValue=oldValue)
        self.assertEqual(json._fb_update_mask, {'b.c': ArrayUnion([6, 7, 8])})

    def test_remove_and_add_to_array(self):
        oldValue = {'a': 123, 'b': {'c': [1, 2, 3, 4, 5], 'd': [3, 4, 5], 'e': {1, 2}}, 1: {1: 123}}
        value = {'a': 123, 'b': {'c': [3, 4, 5, 6, 7, 8], 'd': [3, 4, 5], 'e': {1, 2}}, 1: {1: 123}}
        json = JSON(value, oldValue=oldValue)
        self.assertEqual(json._fb_update_mask, {'b.c': [3, 4, 5, 6, 7, 8]})


    def tearDown(self):
        del self.json

if __name__ == "__main__":
    unittest.main()
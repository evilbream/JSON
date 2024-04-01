import unittest
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


    def tearDown(self):
        del self.json

if __name__ == "__main__":
    unittest.main()
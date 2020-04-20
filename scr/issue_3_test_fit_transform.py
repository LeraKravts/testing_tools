import unittest

from scr.issue_4_one_hot_encode import fit_transform


class TestFitTransform(unittest.TestCase):

    def test_equal(self):
        self.assertEqual(fit_transform(['Moscow']), [('Moscow', [1])])

    def test_not_equal(self):
        self.assertNotEqual((fit_transform('Moscow')), (fit_transform('New York')))

    def test_type(self):
        self.assertIsInstance(fit_transform('Moscow'), list)

    def test_if_none(self):
        self.assertIsNotNone(fit_transform('New York'))

    def test_raise_type_error(self):
        self.assertRaises(TypeError, fit_transform([2, 3, 4]))
        self.assertRaises(TypeError, fit_transform({'Moscow': 'Russia'}))
        self.assertRaises(TypeError, fit_transform('Moscow, New York'))


if __name__ == '__main__':
    unittest.main()

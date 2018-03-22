import unittest


class TestStudent(unittest.TestCase):
    def test_80_to_100(self):
        a = Student('wjt', 80)
        b = Student('zs', 100)
        self.assertEqual(a.get_grate(), 'A')
        self.assertEqual(b.get_grate(), 'A')

    def test_60_to_80(self):
        a = Student('wjt', 60)
        b = Student('zs', 79)
        self.assertEqual(a.get_grate(), 'B')
        self.assertEqual(b.get_grate(), 'B')

    def test_0_to_60(self):
        s1 = Student('Bart', 0)
        s2 = Student('Lisa', 59)
        self.assertEqual(s1.get_grate(), 'C')
        self.assertEqual(s2.get_grate(), 'C')

    def setUp(self):
        print('print self: ', self)

    def tearDown(self):
        print('print self: ', self)

    # def test_invalid(self):
    #     s1 = Student('Bart', -1)
    #     s2 = Student('Lisa', 101)
    #     with self.assertRaises(ValueError):
    #         s1.get_grate()
    #     with self.assertRaises(ValueError):
    #         s2.get_grate()

    # def test_test(self):
    #     s1 = Student('WJT', 80)
    #     print(s1.get_grate())

if __name__ == '__main__':
    unittest.main()


class Student:
    def __init__(self, name, score):

        if 0 > score or 100 < score:
            raise ValueError('invalid value')

        self.name = name
        self.score = score

    def get_grate(self):

        if 60 <= self.score < 80:
            return 'B'
        elif 80 <= self.score <= 100:
            return 'A'
        else:
            return 'C'


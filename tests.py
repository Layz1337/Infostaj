import unittest
import server


class TestServer(unittest.TestCase):
    def test_answer(self):
        testvalues = {1: [1], 2: [2], 3: [3],
                      4: [2, 2], 8: [2, 2, 2], 16: [2, 2, 2, 2],
                      1024: [2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 54689: [17, 3217],
                      8888456231: [8888456231]}
        for i in range(len(testvalues)):
            temp = testvalues.popitem()
            with self.subTest():
                self.assertEqual(server.answer(temp[0]),temp[1])

    def test_failure(self):
        with self.assertRaises(TypeError):
            server.answer('s')


if __name__ == '__main__':
    unittest.main()

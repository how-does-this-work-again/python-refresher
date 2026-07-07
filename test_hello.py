import unittest
import hello
import numpy as np

class TestHello(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello.hello(), "Hello, world!")

    def test_sin(self):
        self.assertEqual(hello.sin(0), 0)
        self.assertEqual(hello.sin(1), 0.841470984807896)
        self.assertEqual(hello.sin(np.pi), 0.0)

    def test_cos(self):
        self.assertEqual(hello.cos(0), 1)
        self.assertEqual(hello.cos(1), 0.5403023058681398)
        self.assertEqual(hello.cos(np.pi), -1.0)

    def test_tan(self):
        self.assertEqual(hello.tan(0), 0)
        self.assertEqual(hello.tan(1), 1.557407724654902)
        self.assertEqual(hello.tan(np.pi), 0.0)

    def test_cot(self):
        self.assertEqual(hello.cot(0), float("inf"))
        self.assertEqual(hello.cot(1), 0.6420926159343308)
        self.assertEqual(hello.cot(np.pi), float("inf"))

if __name__ == "__main__":
    unittest.main()

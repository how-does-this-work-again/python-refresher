import unittest
import hello
import numpy as np

class TestHello(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello.hello(), "Hello, world!")

    def test_add(self):
        self.assertEqual(hello.add(1, 2), 3)
        self.assertEqual(hello.add(-1, 1), 0)
        self.assertEqual(hello.add(0, 0), 0)
        self.assertEqual(hello.add(1.5, 2.5), 4.0)
        self.assertEqual(hello.add(1.5, -2.5), -1.0)
        with self.assertRaises(TypeError):
            hello.add("hi", 0)

    def test_sub(self):
        self.assertEqual(hello.sub(1, 2), -1)
        self.assertEqual(hello.sub(-1, 1), -2)
        self.assertEqual(hello.sub(0, 0), 0)
        self.assertEqual(hello.sub(1.5, 2.5), -1.0)
        self.assertEqual(hello.sub(1.5, -2.5), 4.0)
        with self.assertRaises(TypeError):
            hello.sub("hi", 0)

    def test_mul(self):
        self.assertEqual(hello.mul(1, 2), 2)
        self.assertEqual(hello.mul(-1, 1), -1)
        self.assertEqual(hello.mul(0, 0), 0)
        self.assertEqual(hello.mul(1.5, 2.5), 3.75)
        self.assertEqual(hello.mul(1.5, -2.5), -3.75)
        with self.assertRaises(TypeError):
            hello.mul("hi", 0)

    def test_div(self):
        self.assertEqual(hello.div(1, 2), 0.5)
        self.assertEqual(hello.div(-1, 1), -1)
        self.assertEqual(hello.div(0, 1), 0)
        self.assertEqual(hello.div(1.5, 2.5), 0.6)
        self.assertEqual(hello.div(1.5, -2.5), -0.6)
        with self.assertRaises(ValueError):
            hello.div(1, 0)
        with self.assertRaises(TypeError):
            hello.div("hi", 0)

    def test_sqrt(self):  
        self.assertEqual(hello.sqrt(4), 2.0)
        self.assertEqual(hello.sqrt(0), 0.0)
        with self.assertRaises(ValueError):
            hello.div(1, 0)
        with self.assertRaises(TypeError):
            hello.sqrt("hi", 0)
    
    def test_power(self):
        self.assertEqual(hello.power(2, 3), 8)
        self.assertEqual(hello.power(2, 0), 1)
        self.assertEqual(hello.power(0, 2), 0)
        self.assertEqual(hello.power(2, -1), 0.5)
        self.assertEqual(hello.power(-2, 3), -8)
        self.assertEqual(hello.power(4, 0.5), 2)
        self.assertEqual(hello.power(4, 1.5), 8)
        self.assertEqual(hello.power(4, -0.5), 0.5)
        with self.assertRaises(TypeError):
            hello.power("hi", 0)

    def test_log(self):
        self.assertEqual(hello.log(1), 0)
        self.assertEqual(hello.log(np.e), 1)
        self.assertEqual(hello.log(np.e * np.e), 2)
        self.assertAlmostEqual(hello.log(10), 2.302585092994046)
        with self.assertRaises(TypeError):
            hello.div("hi", 0)

    def test_exp(self):
        self.assertEqual(hello.exp(0), 1)
        self.assertEqual(hello.exp(1), np.e)
        self.assertEqual(hello.exp(-1), 1/(np.e))
        with self.assertRaises(TypeError):
            hello.exp("hi", 0)

    def test_sin(self):
        self.assertEqual(hello.sin(0), 0)
        self.assertAlmostEqual(hello.sin(1), 0.841470984807896)
        self.assertAlmostEqual(hello.sin(np.pi), 0.0)
        with self.assertRaises(TypeError):
            hello.sin("hi", 0)

    def test_cos(self):
        self.assertEqual(hello.cos(0), 1)
        self.assertAlmostEqual(hello.cos(1), 0.5403023058681398)
        self.assertAlmostEqual(hello.cos(np.pi), -1.0)
        with self.assertRaises(TypeError):
            hello.cos("hi", 0)

    def test_tan(self):
        self.assertEqual(hello.tan(0), 0)
        self.assertAlmostEqual(hello.tan(1), 1.557407724654902)
        self.assertAlmostEqual(hello.tan(np.pi), 0)
        with self.assertRaises(TypeError):
            hello.tan("hi", 0)

    def test_cot(self):
        self.assertEqual(hello.cot(0), float("inf"))
        self.assertAlmostEqual(hello.cot(1), 0.6420926159343308)
        self.assertAlmostEqual(hello.cot(np.pi), float("-inf"))
        with self.assertRaises(TypeError):
            hello.cot("hi", 0)

if __name__ == "__main__":
    unittest.main()

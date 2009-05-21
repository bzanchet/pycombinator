import unittest
import pycombinator

class TestPycombinator(unittest.TestCase):
    def test_tail(self):
        self.assertEquals([], pycombinator.tail([]))
        self.assertEquals([2], pycombinator.tail([1,2]))
        self.assertEquals([2, 3], pycombinator.tail([1,2, 3]))
        
    def test_length_0(self):
        self.assertEquals(1, pycombinator.length_0([]))
        self.assertRaises(TypeError, pycombinator.length_0, ['a'])
        
    def test_length_1(self):
        self.assertEquals(1, pycombinator.length_1([]))
        self.assertEquals(2, pycombinator.length_1(['a']))
        self.assertRaises(TypeError, pycombinator.length_0, ['a', 'b'])

    def test_mlength_0(self):
        self.assertEquals(1, pycombinator.mlength_0([]))
        self.assertRaises(TypeError, pycombinator.mlength_0, ['a'])
        
    def test_mlength_1(self):
        self.assertEquals(1, pycombinator.mlength_1([]))
        self.assertEquals(2, pycombinator.mlength_1(['a']))
        self.assertRaises(TypeError, pycombinator.mlength_1, ['a', 'b'])

    def test_mlength_2(self):
        self.assertEquals(1, pycombinator.mlength_2([]))
        self.assertEquals(2, pycombinator.mlength_2(['a']))
        self.assertEquals(3, pycombinator.mlength_2(['a', 'b']))
        self.assertRaises(TypeError, pycombinator.mlength_2, ['a', 'b', 'c'])

if __name__ == '__main__':
    unittest.main()

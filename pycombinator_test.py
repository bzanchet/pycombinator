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

    def test_mmlength_0(self):
        self.assertEquals(1, pycombinator.mmlength_0([]))
        self.assertRaises(TypeError, pycombinator.mmlength_0, ['a'])
        
    def test_mmlength_1(self):
        self.assertEquals(1, pycombinator.mmlength_1([]))
        self.assertEquals(2, pycombinator.mmlength_1(['a']))
        self.assertRaises(TypeError, pycombinator.mmlength_1, ['a', 'b'])

    def test_mmlength_2(self):
        self.assertEquals(1, pycombinator.mmlength_2([]))
        self.assertEquals(2, pycombinator.mmlength_2(['a']))
        self.assertEquals(3, pycombinator.mmlength_2(['a', 'b']))
        self.assertRaises(TypeError, pycombinator.mmlength_2, ['a', 'b', 'c'])

    def test_mmmlength_1(self):
        self.assertEquals(1, pycombinator.mmmlength_1([]))
        self.assertEquals(2, pycombinator.mmmlength_1(['a']))
        self.assertRaises(TypeError, pycombinator.mmmlength_1, ['a', 'b'])

    def test_mmmlength(self):
        self.assertEquals(1, pycombinator.mmmlength([]))
        self.assertEquals(2, pycombinator.mmmlength(['a']))
        self.assertEquals(3, pycombinator.mmmlength(['a', 'b']))
        self.assertEquals(8, pycombinator.mmmlength(range(7)))

    def test_length_y(self):
        self.assertEquals(1, pycombinator.length_y([]))
        self.assertEquals(2, pycombinator.length_y(['a']))
        self.assertEquals(3, pycombinator.length_y(['a', 'b']))
        self.assertEquals(8, pycombinator.length_y(range(7)))

if __name__ == '__main__':
    unittest.main()

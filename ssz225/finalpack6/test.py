import unittest
from finalpack6.exceptions import *
from finalpack6.interval import *

class TestInterval(unittest.TestCase):
    def setUp(self):
        self.interval1 = Interval('[1, 4]')
        self.interval2 = Interval('(-2, 5]')
        self.interval3 = Interval('[4, 8)')
        self.interval4 = Interval('(5, 9)')
        self.interval5 = '[-5, -3]'
        self.interval6 = '[-100, 100]'
        self.intlist = [Interval('[1, 4]'),Interval('(-2, 5]'),Interval('[4, 8)'),Interval('(5, 9)')]
        self.string1 = 'wrong'
        self.string2 = '[2,1)'
        self.string3 = '$3,4)'
        
    def test_isValidInterval(self):
        self.assertEqual(self.interval1.getActuallower(), 1)
        self.assertEqual(self.interval1.getActualupper(), 4)
        self.assertEqual(self.interval2.getActuallower(), -1)
        self.assertEqual(self.interval2.getActualupper(), 5)
        self.assertEqual(self.interval3.getActuallower(), 4)
        self.assertEqual(self.interval3.getActualupper(), 7)
        self.assertEqual(self.interval4.getActuallower(), 6)
        self.assertEqual(self.interval4.getActualupper(), 8)
       
    def test_error(self):
        self.assertRaises(InvalidIntervalError, Interval, self.string1)
        self.assertRaises(InvalidIntervalError, Interval, self.string2)
        self.assertRaises(InvalidIntervalError, Interval, self.string3)

    def test_mergeIntervals(self):
        self.assertEqual(str(mergeIntervals(self.interval1, self.interval2)), '(-2,5]')
        self.assertEqual(str(mergeIntervals(self.interval2, self.interval3)), '(-2,8)')
        self.assertRaises(notOverlappingError, mergeIntervals,self.interval2, self.interval4)  
        self.assertRaises(notOverlappingError, mergeIntervals,self.interval1, self.interval4)
        
    def test_mergeOverlapping(self):
        self.assertEqual(str(mergeOverlapping(self.intlist)), '[(-2,9)]')
        
    def test_insert(self):
        self.assertEqual(str(insert(self.intlist, self.interval5)),'[[-5,-3], (-2,9)]')
        self.assertEqual(str(insert(self.intlist, self.interval6)),'[[-100,100]]')

if __name__=='__main__':
    unittest.main()

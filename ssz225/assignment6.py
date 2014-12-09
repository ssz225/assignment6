from finalpack6.exceptions import *
from finalpack6.interval import *
import sys
"""This program is written to take user input for:
1. string = a list of intervals
2. newint = an interval they would like to insert into the intervals list
and merge the intervals if they overlap.

The result is:
newlist = a list of merged and non-overlapping intervals.

To accomplish this task:
1. A class Interval is written to check user input for validity
and to parse the input strings. Raises InvalidIntervalError if not valid.
2. Function mergeIntervals(int1, int2) takes two valid intervals
and checks if they can be merged, raising notOverlappingError if not.
3. Function mergeOverlapping(intlist) loops mergeIntervals for a
list of intervals.
4. Function insert(intlist, newint) inserts user input newint into
intlist and calls mergeOverlapping."""

def main():
    while True:
        try:
            #obtain inputer intervals list and split string into each interval
            string = raw_input('List of intervals?').split(', ')
            #search string input for 'quit' and exit if found
            for x in string: 
                if x.lower().strip() == 'quit':
                    print 'Quitting. Bye!'
                    sys.exit()
        #sys exit if KeyboardInterrupt
        except KeyboardInterrupt:
            print 'KeyboardInterrupt. Bye!'
            sys.exit()  
        #check each item in string is a correct Interval,
        #and store each Interval in input_list
        try:
            input_list = [Interval(x) for x in string]
            break 
            #once correct input verified, break raw_input loop
        #catch InvalidIntervalError
        #prompt for user intervals list input again
        except InvalidIntervalError:
            print 'Invalid Interval'
        
    while True:
        try:
            #obtain input for Interval to insert
            newint = raw_input('Interval?')
            #quit if input = 'quit'
            if newint.lower().strip() == 'quit':
                print 'Quitting. Bye!'
                sys.exit()
        #quit if KeyboardInterrupt
        except KeyboardInterrupt:
            print 'KeyboardInterrupt. Bye!'
            sys.exit()   
        try:
            #insert newint into input_list and attempt merge
            newlist = insert(input_list, newint)
            print newlist      
        #catch InvalidIntervalError   
        #loop to ask user to input newint   
        except InvalidIntervalError:
            print 'Invalid Interval'
        
if __name__=='__main__':
    main()
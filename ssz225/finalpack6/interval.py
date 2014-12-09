from finalpack6.exceptions import *

class Interval:
    def __init__(self, string):
        """check interval for validity, defined by:
        int, int bounded left by [ or ( and right byt ) or ];
        parse interval if format is valid and checks that the 
        interval has a valid set of values"""
        try:
            #remove all whitespace
            self.string = string.replace(' ', '')
            #lower_bracket should equal [ or (
            self.lower_bracket = string[0]
            #upper_bracket should equal ] or )
            self.upper_bracket = string[-1]
            comma = self.string.index(',')
            #displayed lower and upper bounds
            self.lowerbound = int(self.string[1:comma])
            self.upperbound = int(self.string[comma+1:-1])
            #actual bounds = closed bounds (inclusive)
            if self.lower_bracket == '[':
                self.actuallower=self.lowerbound
            elif self.lower_bracket == '(':
                self.actuallower=self.lowerbound+1
            if self.upper_bracket == ']':
                self.actualupper=self.upperbound
            elif self.upper_bracket == ')':
                self.actualupper=self.upperbound-1
            #interval is not valid if lower bound is > upper bound
            if self.actuallower > self.actualupper:
                raise InvalidIntervalError('Invalid Interval Error')
        except:
            raise InvalidIntervalError('Invalid Interval Error')
        
    def getActuallower(self):
    #returns inclusive lower bound
        return self.actuallower
    
    def getActualupper(self):
    #returns inclusive upper bound
        return self.actualupper
    
    def __repr__(self):
        return self.lower_bracket + str(self.lowerbound) + ',' \
            + str(self.upperbound) + self.upper_bracket

def mergeIntervals(int1, int2):
    #if inclusive lower of either interval is great than
    #the inclusive upper of the other interval, they do not overlap
    if int1.actuallower > int2.actualupper or int2.actuallower > int1.actualupper:
        raise notOverlappingError('No interval overlap')
    else:
        #return bounds and brackets
        if int1.actuallower < int2.actuallower:
            newlower = int1.lowerbound
            new_lowerbracket = int1.lower_bracket
        else:
            newlower = int2.lowerbound
            new_lowerbracket = int2.lower_bracket
        if int1.actualupper > int2.actualupper:
            newupper = int1.upperbound
            new_upperbracket = int1.upper_bracket
        else:
            newupper = int2.upperbound
            new_upperbracket = int2.upper_bracket
    #concatenates pieces to form merged interval string
    merged = new_lowerbracket + str(newlower) + ',' + str(newupper) + new_upperbracket
    #convert merged interval string to Interval
    merged_int = Interval(merged)
    return merged_int

def int_key(x):
    return x.actuallower

def mergeOverlapping(intlist):
    #sort intlist by inclusive lower bound
    intlist.sort(key=int_key)
    #set first item in intlist to merged
    merged = intlist[0]
    #create new list to store results
    mergedlist = []
    for i in range(0, len(intlist)):
        try:
            #loop through items in intlist and attempt to merge
            merged = mergeIntervals(merged, intlist[i])
        except notOverlappingError:
            #append object to mergedlist if it cannot merge
            mergedlist.append(merged)
            merged = intlist[i]
    #append final object to merged list
    mergedlist.append(merged)
    return mergedlist

def insert(intlist, newint):
    #Convert newint string to Interval and add to intlist
    intlist.append(Interval(newint))
    #see if intervals in list can merge
    intlist = mergeOverlapping(intlist)
    return intlist

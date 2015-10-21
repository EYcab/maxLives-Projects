__author__ = 'Chenxi'
#!/usr/bin/py
import unittest
import mostlyAlive


class myTest(unittest.TestCase):
    # The first test is to test the maximum population between 1900 and 2000 when it has only one peak
    # How to know there is only one peak? see my ipython notebook graphic-testing
    def test_onePeak(self):
        folder1 = 'C:\\Users\\Chenxi\\Desktop\\python\\Projects\\testStar.csv'
        #folder1 = 'C:\\Users\\Chenxi\\Desktop\\python\\Projects\\testStar.csv'

        # the testCase1 is the targeted result, and result1 is the expected result
        # the next test follows the same procedures
        testCase1=mostlyAlive.year_with_max_population(folder1)
        #print testCase1
        result1 = mostlyAlive.test_result(folder1)
        self.assertEquals(testCase1,result1)
    #the second test is to test the maximum population between 1900 and 2000 when it has more than one peak
    def test_Peaks(self):
        #folder2 = 'C:\\Users\\Chenxi\\Desktop\\python\\Projects\\test.csv'
        folder2 = 'C:\\Users\\Chenxi\\Desktop\\python\\Projects\\testMultiplePeaks.csv'
        testCase2=mostlyAlive.year_with_max_population(folder2)
        #print testCase2
        result2 = mostlyAlive.test_result(folder2)
        self.assertEquals(testCase2,result2)

if __name__ == "__main__":
    unittest.main(exit=False)

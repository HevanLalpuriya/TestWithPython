import unittest, logging
from loggerpackage import customLogger as cl
from commandexecution import executecommand, sortingPython
from Helpers import helpermethods

file = "C:/Users/hlalpuriya/Documents/MyPersonalSpace/AllOther/Learning/swarm64/tsk1/DemoFileText.txt"
numfile = "C:/Users/hlalpuriya/Documents/MyPersonalSpace/AllOther/Learning/swarm64/tsk1/NumericFileText.txt"
log = cl.custom_logger(logging.DEBUG)


class TestClassSortingTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("sortingCmd test class started..")

    def setUp(self):
        print("setup")

    def test_simpleSorting(self):
        """
        Verifying default sorting without any explicit command

        :return: test 1: simple sorting
        """
        log = cl.custom_logger( logging.DEBUG )

        # getting list from unix command
        sortResultCmd = executecommand.commandExecutionCygwin( "sort " + file)

        # getting list from python sorted() method for verification
        sortResultPy = sortingPython.sortFileContent(file, lambda v: (v.lower(), v[0].isupper()), False)

        # verifying both the lists
        TestClassSortingTest.verification( self, sortResultCmd, sortResultPy, log )

    def test_reverseSorting(self):
        """

        Verifying reverse sorting with any '--reverse' command

        :return:Reverse sorting
        """
        log = cl.custom_logger( logging.DEBUG )

        # getting list from unix command
        sortResultCmd = executecommand.commandExecutionCygwin( "sort -r " + file)

        # getting list from python sorted() method for verification
        sortResultPy = sortingPython.sortFileContent(file, lambda v: (v.lower(), v[0].isupper()), True)

        # verifying both the lists
        TestClassSortingTest.verification( self, sortResultCmd, sortResultPy, log )

    def test_generalNumericAndDictionarySorting(self):
        """
        verifying combination of --general-numeric-sort and --dictionary-order

        :return:Alpha Numeric sorting
        """
        log = cl.custom_logger( logging.DEBUG )

        # getting list from unix command
        sortResultCmd = executecommand.commandExecutionCygwin("sort -g "+file+" | sort -d "+file+"")

        # getting list from python sorted() method for verification
        sortResultPy = sortingPython.sortFileContent(file, lambda v: (v.lower(), v[0].isupper()), False)

        # verifying both the lists
        TestClassSortingTest.verification( self, sortResultCmd, sortResultPy, log )

    def test_numericSorting(self):
        """
        Verifying reverse sorting with any '--numeric-sort or -n' command
        :return:
        """
        log = cl.custom_logger( logging.DEBUG )

        # getting list from unix command
        sortResultCmd = executecommand.commandExecutionCygwin( "sort -n " + numfile)

        # getting list from python sorted() method for verification
        sortResultPy = sortingPython.sortFileContent( numfile, int, False )

        # verifying both the lists
        TestClassSortingTest.verification( self, sortResultCmd, sortResultPy, log )

    def test_uniqueSorting(self):
        """
        Verifying reverse sorting with any '--unique or -u' command
        :return:
        """
        log = cl.custom_logger( logging.DEBUG )

        # getting list from unix command
        sortResultCmd = executecommand.commandExecutionCygwin( "sort -u " + file)

        # getting list from python sorted() method for verification
        sortResultPy = sortingPython.sortFileContentUnique( file, lambda v: (v.lower(), v[0].isupper()), False )

        # verifying both the lists
        TestClassSortingTest.verification( self, sortResultCmd, sortResultPy, log )

    def verification(self, firstList, secondList, vlog):

        firstList = helpermethods.removespace( firstList )
        secondList = helpermethods.removespace( secondList )

        vlog.debug( firstList )
        vlog.debug( secondList )

        for i in range( 0, len( firstList ) ):
            self.assertEqual( firstList[i], secondList[i], "error at " + str( i ) )

    def tearDown(self):
        print("teardown")

    @classmethod
    def tearDownClass(cls):
        print("sortingCmd test class ended..")


if __name__ == '__main__':
    unittest.main(verbosity=2)




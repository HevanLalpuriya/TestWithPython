"""

This file contains all the test suites created for project
mainly three test suites
1) task01:
2) task02:
3) task03:
"""

import unittest
from projectswarm64.test_sortingtestclass import TestClassSortingTest

tc1 = unittest.TestLoader().loadTestsFromTestCase(TestClassSortingTest)

smokeTest = unittest.TestSuite([tc1])

unittest.TextTestRunner(verbosity=2).run(smokeTest)

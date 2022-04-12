from tests.class_tests import *

opts = "".join(sys.argv[1:])

tests = {
    "1": TestHuman,
    "2": TestSniper, 
    "3": TestAlien, 
    "4": TestSquad, 
    "5": TestBattle
}

if __name__ == '__main__':
    sys.stdout = open(os.devnull, 'w')
    for test in [tests[i] for i in opts if i in tests]:
        suite = unittest.suite.BaseTestSuite()
        suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(test))
        unittest.TextTestRunner(verbosity=2).run(suite)
    sys.stdout = sys.__stdout__
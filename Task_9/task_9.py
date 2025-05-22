'''
For the odd_indexes() function written below, which for a given string returns letters with odd indexes, for example:

    "game show" → "aeso",
    "computer" → "optr".

    Write tests for the argument, which will be a string.
    Run functions passing int.
    Observe what happened.
    Write tests for arguments that are int.
    Fix the functions to make them work properly by making the tests pass.
'''

import unittest

def odd_indexes(string):
    return string[1::2]

class TestOddIndexes(unittest.TestCase):
    #primele 5 teste respecta partial cerinta
    #verifica practic decat corectitudinea functiei, nu si tipul datei
    def test_1(self):
        self.assertEqual(odd_indexes("game show") , "aeso")

    def test_2(self):
        self.assertEqual(odd_indexes("computer") , "optr")

    def test_3(self):
        self.assertEqual(odd_indexes([0,1,2,3,4,5,6]) , [1,3,5])

    #intentionat eroare pentru test_4, dar functia merge bine, este eroarea asteptata
    def test_4(self):
        self.assertEqual(odd_indexes([0,1,2,3,4,5,6]) , [2,4,6])

    def test_5(self):
        self.assertNotEqual(odd_indexes("python") , "pto")

    #daca respectam cerinta, ar trebui sa includem si teste in care sa verificam tipul de data
    #scrie in cerinta ca functia accepta doar string-uri
    def test_6(self):
        with self.assertRaises(TypeError):
          odd_indexes([0, 1, 2, 3, 4, 5, 6])

    def test_7(self):
        with self.assertRaises(TypeError):
          odd_indexes(100)

if __name__ == "__main__":
    #2 tests failed(test_4 and test_6), 5 passed, this is the result
    #How about test_7? Why not raised error?
    #Because it is giving error before even the test to be run
    #Actually, when calling the function it gives error because you can not iterate through an integer
    #So, firtsly the error it is raised by the fact that you can not iterate through the number
    #And this error it is not TypeError, and blocks the next phase( which is assertion testing)
    #So, because of that error the test will not be made, because that call was broken
    unittest.main()
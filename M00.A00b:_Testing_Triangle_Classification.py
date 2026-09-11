import unittest

def classifyTriangle(s1,s2,s3):
    if(s1 == s2 and s1 == s3):
        type = "Equilateral"
    elif(s1 == s2 and s1 != s3 and s2 != s3):
        type = "Isosceles"
    elif(s1 != s2 and s2 != s3 and s1 != s3):
        type = "Scalene"
    if(s1**2 + s2**2 == s3**2):
        type = "Right"
    elif(s2**2 + s3**2 == s1**2):
        type = "Right"
    elif(s3**2 + s1**2 == s2**2):
        type = "Right"
    

    return type

class TriangleTestCase(unittest.TestCase):
    def testtriangles(self):
        self.assertEqual(classifyTriangle(3, 3, 8), "Isosceles")
    def testtriangles2(self):
        self.assertEqual(classifyTriangle(3, 4, 5), "Right")
    def testtriangles3(self):
        self.assertEqual(classifyTriangle(7, 3, 1), "Scalene")
    def testtriangles4(self):
        self.assertEqual(classifyTriangle(3, 3, 3), "Equilateral")
if __name__ == '__main__':
    unittest.main()
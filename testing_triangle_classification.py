'''
What this code does is take triangle side
amounts and determines what type of
triangle it is.
'''
import unittest

def classify_triangle(s1,s2,s3):
    '''
    Defines what fits into what paremeters
    that define specific triangle types,
    like if all sides are equal then the
    triangle is equilateral.
    '''
    if s1 == s2 and s1 == s3:
        type = "Equilateral"
    elif s1 == s2 and s1 != s3 and s2 != s3:
        type = "Isosceles"
    elif s1 != s2 and s2 != s3 and s1 != s3:
        type = "Scalene"
    if s1**2 + s2**2 == s3**2:
        type = "Right"
    elif s2**2 + s3**2 == s1**2:
        type = "Right"
    elif s3**2 + s1**2 == s2**2:
        type = "Right"
    return type

class TriangleTestCase(unittest.TestCase):
    '''
    Tests four different types of triangles
    to make sure that the code outputs
    correctly.
    '''
    def testtriangles(self):
        '''
        Asserts that if a triangle has those sides that then
        it is isosceles.
        '''
        self.assertEqual(classify_triangle(3, 3, 8), "Isosceles")

    def testtriangles2(self):
        '''
        Asserts that if a triangle has those sides that then
        it is a right triangle.
        '''
        self.assertEqual(classify_triangle(3, 4, 5), "Right")

    def testtriangles3(self):
        '''
        Asserts that if a triangle has those sides that then
        it is scalene.
        '''
        self.assertEqual(classify_triangle(7, 3, 1), "Scalene")

    def testtriangles4(self):
        '''
        Asserts that if a triangle has those sides that then
        it is equilateral.
        '''
        self.assertEqual(classify_triangle(3, 3, 3), "Equilateral")

if __name__ == '__main__':
    unittest.main()

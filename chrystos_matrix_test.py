import unittest
from chrystos_matrix import Matrix_representator, print_matrix, sum_of_matrices, multiply_of_matrices


class MyTest1(unittest.TestCase):

    def setUp(self):
        self.l1 = [[1, 1], [1, 1]]
        self.l2 = [[2, 3], [4, 5]]

    def test_init(self):
        m1 = Matrix_representator(self.l1)
        m2 = Matrix_representator(self.l2)
        self.assertEqual(self.l1[0],m1.matrix_data[0])
        self.assertEqual(self.l1[1],m1.matrix_data[1])

        self.assertEqual(self.l2[0],m2.matrix_data[0])
        self.assertEqual(self.l2[1],m2.matrix_data[1])

class MyTest2(unittest.TestCase):

    def setUp(self):
        self.l1 = [[1, 1], [1, 1]]
        self.l2 = [[2, 3], [4, 5]]
        self.m1 = Matrix_representator(self.l1)
        self.m2 = Matrix_representator(self.l2)
        #self.m3 = Matrix_representator()

    def test_add(self):
        m3 = self.m1.add(self.m2)
        self.assertEqual(m3.matrix_data[0][0],3)
        self.assertEqual(m3.matrix_data[0][1],4)
        self.assertEqual(m3.matrix_data[1][0],5)
        self.assertEqual(m3.matrix_data[1][1],6)



    


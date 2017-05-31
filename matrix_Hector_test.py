import unittest
from matrix_Hector import Matrix


class MyTest1(unittest.TestCase):
    def setUp(self):
        self.l1 = [[1, 2], [3, 4]]
        self.l2 = [[5, 6], [7, 8]]
        self.l3 = [(0, 0), (0, 1), (1, 0), (1, 1)]

    def test_init(self):
        m1 = Matrix(self.l1)

        self.assertEqual(self.l1[0], m1.rows[0])
        self.assertEqual(self.l1[1], m1.rows[1])

        self.assertEqual(2, m1.nrows)
        self.assertEqual(2, m1.ncols)

        self.assertEqual(self.l3, m1.coordinates_vector)

    def test_add_matrix(self):
        m1 = Matrix(self.l1)
        m2 = Matrix(self.l2)

        m3 = m1 + m2

        self.assertEqual(m3.rows[0][0], 6)
        self.assertEqual(m3.rows[0][1], 8)
        self.assertEqual(m3.rows[1][0], 10)
        self.assertEqual(m3.rows[1][1], 12)

    def test_add_scalar(self):
        m1 = Matrix(self.l1)

        m2 = m1 + 3

        self.assertEqual(m2.rows[0][0], 4)
        self.assertEqual(m2.rows[0][1], 5)
        self.assertEqual(m2.rows[1][0], 6)
        self.assertEqual(m2.rows[1][1], 7)

    def test_radd_scalar(self):
        m1 = Matrix(self.l1)

        m2 = 3 + m1

        self.assertEqual(m2.rows[0][0], 4)
        self.assertEqual(m2.rows[0][1], 5)
        self.assertEqual(m2.rows[1][0], 6)
        self.assertEqual(m2.rows[1][1], 7)


    def test_sub_matrix(self):
        m1 = Matrix(self.l1)
        m2 = Matrix(self.l2)

        m3 = m2 - m1

        self.assertEqual(m3.rows[0][0], 4)
        self.assertEqual(m3.rows[0][1], 4)
        self.assertEqual(m3.rows[1][0], 4)
        self.assertEqual(m3.rows[1][1], 4)

    def test_sub_scalar(self):
        m1 = Matrix(self.l1)

        m2 = m1 - 3

        self.assertEqual(m2.rows[0][0], -2)
        self.assertEqual(m2.rows[0][1], -1)
        self.assertEqual(m2.rows[1][0], 0)
        self.assertEqual(m2.rows[1][1], 1)

    def test_rsub_scalar(self):
        m1 = Matrix(self.l1)

        m2 = 3 - m1

        self.assertEqual(m2.rows[0][0], 2)
        self.assertEqual(m2.rows[0][1], 1)
        self.assertEqual(m2.rows[1][0], 0)
        self.assertEqual(m2.rows[1][1], -1)

    def test_prod(self):
        m1 = Matrix(self.l1)
        m2 = Matrix(self.l2)
        m3 = m1.prod(m2)

        self.assertEqual(m3.rows[0][0], 19)
        self.assertEqual(m3.rows[0][1], 22)
        self.assertEqual(m3.rows[1][0], 43)
        self.assertEqual(m3.rows[1][1], 50)

    def test_prod_scalar(self):
        m1 = Matrix(self.l1)
        m2 = m1.prod_scalar(3)

        self.assertEqual(m2.rows[0][0], 3)
        self.assertEqual(m2.rows[0][1], 6)
        self.assertEqual(m2.rows[1][0], 9)
        self.assertEqual(m2.rows[1][1], 12)

    def test_iter(self):
        m1 = Matrix(self.l1)
        l3 = []

        for elem in m1:
            l3.append(elem)

        self.assertEqual(l3[0], 1)
        self.assertEqual(l3[1], 2)
        self.assertEqual(l3[2], 3)
        self.assertEqual(l3[3], 4)
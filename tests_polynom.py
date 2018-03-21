import unittest
from polynom import Polynomial


class Tests_polynom(unittest.TestCase):
    # ============= init tests =============
    def test_ConstructorSeq(self):
        p1 = Polynomial([4, 3.3, 2, 1])
        self.assertEqual(p1.coeffs, [4, 3.3, 2, 1])
        self.assertEqual(p1.degree, 3)
        p2 = Polynomial([0])
        self.assertEqual(p2.coeffs, [0])
        self.assertEqual(p2.degree, 0)

    def test_ConstructorSeqBad(self):
        with self.assertRaises(Exception) as context:
            p1 = Polynomial([4, 3, 'a', 1])
        self.assertEqual(str(context.exception),
                         "('Bad parameters in Polynomial constructor', 'a', [4, 3, 'a', 1])")
        with self.assertRaises(Exception) as context:
            p2 = Polynomial(['a'])
        self.assertEqual(str(context.exception),
                         "('Bad parameters in Polynomial constructor', 'a', ['a'])")

    def test_ConstructorScalar(self):
        p1 = Polynomial(5, 2, 1.0)
        self.assertEqual(p1.coeffs, [5, 2, 1.0])
        self.assertEqual(p1.degree, 2)
        p2 = Polynomial(0)
        self.assertEqual(p2.coeffs, [0])
        self.assertEqual(p2.degree, 0)

    def test_ConstructorScalarBad(self):
        with self.assertRaises(Exception) as context:
            p1 = Polynomial(4, [3, 2], 2, 'b')
        self.assertEqual(str(context.exception),
                         "('Bad parameters in Polynomial constructor', [3, 2], (4, [3, 2], 2, 'b'))")
        with self.assertRaises(Exception) as context:
            p2 = Polynomial('a')
        self.assertEqual(str(context.exception),
                         "('Bad parameters in Polynomial constructor', 'a', ('a',))")

    def test_ConstructorCopy(self):
        q = Polynomial([4, 3, 2, 1])
        p = Polynomial(q)
        self.assertEqual(p.coeffs, [4, 3, 2, 1])
        self.assertEqual(p.degree, 3)

    def test_ConstructorEmpty(self):
        p1 = Polynomial([])
        self.assertEqual(p1.coeffs, [])
        self.assertEqual(p1.degree, 0)
        self.assertEqual(str(p1), '0')
        p2 = Polynomial()
        self.assertEqual(p2.coeffs, [])
        self.assertEqual(p2.degree, 0)
        self.assertEqual(str(p2), '0')

    # ============= trim tests =============
    def test_Trim(self):
        p1 = Polynomial([0, 3, 2, 1])
        self.assertEqual(p1.coeffs, [3, 2, 1])
        self.assertEqual(p1.degree, 2)
        p2 = Polynomial([0, 0, 2, 0, 1])
        self.assertEqual(p2.coeffs, [2, 0, 1])
        self.assertEqual(p2.degree, 2)
        p3 = Polynomial([0, 0, 0, 0, 1])
        self.assertEqual(p3.coeffs, [1])
        self.assertEqual(p3.degree, 0)
        p4 = Polynomial([0, 0, 0, 0, 0])
        self.assertEqual(p4.coeffs, [0])
        self.assertEqual(p4.degree, 0)

    # ============= str tests =============
    def test_StrBase(self):
        p0 = Polynomial([1, 1, 1, 1])
        p1 = Polynomial([4, 3, 2, 1])
        p2 = Polynomial([-4, -3, -2, -1])
        p3 = Polynomial([-4, 3.3, 2, -1])
        p4 = Polynomial([2, 1])
        p5 = Polynomial([2])
        p6 = Polynomial([])
        p7 = Polynomial()

        self.assertEqual(str(p0), "X3+X2+X+1")
        self.assertEqual(str(p1), "4X3+3X2+2X+1")
        self.assertEqual(str(p2), "-4X3-3X2-2X-1")
        self.assertEqual(str(p3), "-4X3+3.3X2+2X-1")
        self.assertEqual(str(p4), "2X+1")
        self.assertEqual(str(p5), "2")
        self.assertEqual(str(p6), "0")
        self.assertEqual(str(p7), "0")

    def test_StrPlusWithNull(self):
        p1 = Polynomial([4, 3, 2, 0])
        p2 = Polynomial([4, 3, 0, 1])
        p3 = Polynomial([4, 0, 0, 1])
        p4 = Polynomial([4, 0, 0, 0])
        p5 = Polynomial([0, 3, 2, 0])
        p6 = Polynomial([0, 0, 0, 1])

        self.assertEqual(str(p1), "4X3+3X2+2X")
        self.assertEqual(str(p2), "4X3+3X2+1")
        self.assertEqual(str(p3), "4X3+1")
        self.assertEqual(str(p4), "4X3")
        self.assertEqual(str(p5), "3X2+2X")
        self.assertEqual(str(p6), "1")

    def test_StrMinusWithNull(self):
        p1 = Polynomial([-4, -3, -2, 0])
        p2 = Polynomial([-4, -3, 0, -1])
        p3 = Polynomial([-4, 0, 0, -1])
        p4 = Polynomial([-4, 0, 0, 0])
        p5 = Polynomial([0, -3, -2, 0])
        p6 = Polynomial([0, 0, 0, -1])

        self.assertEqual(str(p1), "-4X3-3X2-2X")
        self.assertEqual(str(p2), "-4X3-3X2-1")
        self.assertEqual(str(p3), "-4X3-1")
        self.assertEqual(str(p4), "-4X3")
        self.assertEqual(str(p5), "-3X2-2X")
        self.assertEqual(str(p6), "-1")

    # ============= equal tests =============
    def test_Equal(self):
        p0 = Polynomial([3, 2, 1])
        p1 = Polynomial([3, 2, 1])
        p2 = Polynomial([-3, -2, -1])
        p3 = Polynomial([-3, 2, -1])
        p4 = "3X2+2X+1"
        p5 = Polynomial(3)
        p6 = 3

        self.assertTrue(p0 == p1)
        self.assertTrue(p0 == p0)
        self.assertFalse(p0 == p2)
        self.assertFalse(p0 == p3)
        self.assertTrue(p0 == p4)
        self.assertTrue(p5 == p6)

    def test_NotEqual(self):
        p0 = Polynomial([3, 2, 1])
        p1 = Polynomial([3, 2, 1])
        p2 = Polynomial([-3, -2, -1])
        p3 = Polynomial([-3, 2, -1])
        p4 = "3X2+2X+1"
        p5 = Polynomial(3)
        p6 = 3

        self.assertFalse(p0 != p1)
        self.assertFalse(p0 != p0)
        self.assertTrue(p0 != p2)
        self.assertTrue(p0 != p3)
        self.assertFalse(p0 != p4)
        self.assertFalse(p5 != p6)

    # ============= add tests =============
    def test_AddBase(self):
        p0 = Polynomial([3, 2, 1])
        p1 = Polynomial([2, 1])
        p2 = Polynomial([4, -3, -2.5, 1])

        res = p0 + p1
        self.assertEqual(res.coeffs, [3, 4, 2])

        res = p0 + p2
        self.assertEqual(res.coeffs, [4, 0, -0.5, 2])

    def test_AddWithNull(self):
        p0 = Polynomial([3, 2, 1])
        p3 = Polynomial([-3, -2, -1])
        p4 = Polynomial([4.4, -3, -2, -1])

        res = p0 + p3
        self.assertEqual(res.coeffs, [0])

        res = p0 + p4
        self.assertEqual(res.coeffs, [4.4, 0, 0, 0])

    def test_AddBad(self):
        p0 = Polynomial([3, 2, 1])
        p5 = "3X2+2X+1"

        with self.assertRaises(Exception) as context:
            res = p0 + p5
        self.assertEqual(str(context.exception),
                         "('Bad arg in Polynomial add function', '3X2+2X+1')")

    def test_AddWithOneValue(self):
        p0 = Polynomial([3, 2, 1])
        p6 = Polynomial(3)
        p7 = 3
        p8 = Polynomial([])

        res = p0 + p6
        self.assertEqual(res.coeffs, [3, 2, 4])

        res = p6 + p7
        self.assertEqual(res.coeffs, [6])

        res = p0 + p7
        self.assertEqual(res.coeffs, [3, 2, 4])

        res = p8 + p7
        self.assertEqual(res.coeffs, [3])

    # ============= neg tests =============
    def test_Neg(self):
        p0 = Polynomial([3, 2, 1])
        p1 = Polynomial([-3, -2, -1])
        p2 = Polynomial(-p0)
        p3 = Polynomial([])
        p4 = Polynomial(-p3)

        self.assertTrue(p0 == -p1)
        self.assertTrue(-p0 == p1)
        self.assertTrue(p2 == p1)
        self.assertTrue(p3 == p4)

    # ============= sub tests =============
    def test_SubBase(self):
        p0 = Polynomial([3, 2, 1])
        p1 = Polynomial([2, 1])
        p2 = Polynomial([4, 3, 2.5, 1])

        res = p0 - p1
        self.assertEqual(res.coeffs, [3, 0, 0])

        res = p2 - p0
        self.assertEqual(res.coeffs, [4, 0, 0.5, 0])

    def test_SubBad(self):
        p0 = Polynomial([3, 2, 1])
        p5 = "3X2+2X+1"

        with self.assertRaises(Exception) as context:
            res = p0 - p5
        self.assertEqual(str(context.exception),
                         "('Bad arg in Polynomial sub function', '3X2+2X+1')")

    # ============= mul tests =============
    def test_MulBase(self):
        p0 = Polynomial([3, 2, 1])
        p1 = Polynomial([2, 1])
        p2 = Polynomial([-1, -1])

        res = p0 * p1
        self.assertEqual(res.coeffs, [6, 7, 4, 1])

        res = p0 * p2
        self.assertEqual(res.coeffs, [-3, -5, -3, -1])

    def test_MulWithNull(self):
        p0 = Polynomial([3, 2, 1])
        p3 = Polynomial([1, 0])
        p4 = Polynomial([0, 1, 0, 1])

        res = p0 * p3
        self.assertEqual(res.coeffs, [3, 2, 1, 0])

        res = p0 * p4
        self.assertEqual(res.coeffs, [3, 2, 4, 2, 1])

    def test_MulBad(self):
        p0 = Polynomial([3, 2, 1])
        p5 = "3X2+2X+1"

        with self.assertRaises(Exception) as context:
            res = p0 * p5
        self.assertEqual(str(context.exception),
                         "('Bad arg in Polynomial mul function', '3X2+2X+1')")

    def test_MulWithOneValue(self):
        p0 = Polynomial([3, 2, 1])
        p6 = Polynomial(3)
        p7 = 3
        p8 = 0
        p9 = Polynomial([])

        res = p0 * p6
        self.assertEqual(res.coeffs, [9, 6, 3])

        res = p6 * p7
        self.assertEqual(res.coeffs, [9])

        res = p0 * p7
        self.assertEqual(res.coeffs, [9, 6, 3])

        res = p0 * p8
        self.assertEqual(res.coeffs, [0])

        res = p9 * p8
        self.assertEqual(res.coeffs, [])


if __name__ == '__main__':
    unittest.main()

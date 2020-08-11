import unittest
import ComplexLibrary
import math 

class pruebaComplejos(unittest.TestCase):

    def test_sum(self):
        ans1 = ComplexLibrary.complexSum((10,10),(20,20))
        ans2 = ComplexLibrary.complexSum((-2,-3),(-5,-3))
        ans3 = ComplexLibrary.complexSum((-1,9),(1,3))
        self.assertEqual(ans1,(30, 30))
        self.assertEqual(ans2,(-7, -6))
        self.assertEqual(ans3,(0, 12))
        
    def test_resta(self):
        ans1 = ComplexLibrary.complexRest((10,10),(20,20))
        ans2 = ComplexLibrary.complexRest((-2,-3),(-5,-3))
        ans3 = ComplexLibrary.complexRest((-1,9),(1,3))
        self.assertEqual(ans1,(-10, -10))
        self.assertEqual(ans2,(3, 0))
        self.assertEqual(ans3,(-2, 6))

    def test_Product(self):
        ans = ComplexLibrary.complexProduct((4,6),(1,4))
        self.assertEqual(ans,(-20,22))

    def test_div(self):
        ans = ComplexLibrary.complexDiv((100,20),(2,4))
        self.assertEqual(ans,(14.0, -18.0))

    def test_mod(self):
        self.assertEqual(ComplexLibrary.complexMod((5,5)),25)
        self.assertEqual(ComplexLibrary.complexMod((3,9)),45)
        self.assertEqual(ComplexLibrary.complexMod((-3,-6)),22.5)

    def test_conjugado(self):
        self.assertEqual(ComplexLibrary.complexConj((3,21)),(3,-21))
        self.assertEqual(ComplexLibrary.complexConj((6,-76)),(6,76))
        self.assertEqual(ComplexLibrary.complexConj((5,16)),(5,-16))

    def test_polarCartesiano(self):
        self.assertEqual(ComplexLibrary.polarCartesiano((13,23)),(11.966563094881725,5.079504670360558))
        self.assertEqual(ComplexLibrary.polarCartesiano((2,120)),(-0.9999999999999996,1.7320508075688774))
        self.assertEqual(ComplexLibrary.polarCartesiano((1,0)),(1,0))
        
    def test_cartesianoPolar(self):
        self.assertEqual(ComplexLibrary.cartesianoPolar((1,2)),(2.23606797749979,63.43494882292201))
        self.assertEqual(ComplexLibrary.cartesianoPolar((-3,1)),(3.1622776601683795,18.43494882292201))
        self.assertEqual(ComplexLibrary.cartesianoPolar((2,2)),(2.8284271247461903,45.0))

    def test_argu(self):
        self.assertEqual(ComplexLibrary.complexArg((3,21)),1.4288992721907328)
        self.assertEqual(ComplexLibrary.complexArg((6,-76)),-1.492012365805753)
        self.assertEqual(ComplexLibrary.complexArg((5,16)),1.2679114584199251)
if __name__ == "__main__":
    unittest.main()

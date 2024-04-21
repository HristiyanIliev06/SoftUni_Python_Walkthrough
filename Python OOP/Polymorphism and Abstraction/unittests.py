from Vehicle import Car
import unittest

class VehiclesTests(unittest.TestCase):
    def test_first_zero(self):
        car = Car(20, 5)
        car.drive(3)
        self.assertEqual(car.fuel_quantity, 2.299999999999997)
        car.refuel(10)
        self.assertEqual(car.fuel_quantity, 12.299999999999997)


if __name__ == '__main__':
    unittest.main()
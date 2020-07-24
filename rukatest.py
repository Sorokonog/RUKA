import unittest
from ruka import controller as cont

class TestRUKAMethods(unittest.TestCase):
    """Class testing TurtleBro RUKA project"""


    def test_RUKA_driver_controller_for_connect_to_device(self):
        """Testing RUKA driver controller for proper connect to device"""
        c = cont.Controller()
        self.assertTrue(c.converting_integer_to_bits(1), True)

if __name__ == '__main__':
    unittest.main()
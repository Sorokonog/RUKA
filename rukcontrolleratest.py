import unittest
from ruka import controller as cont

class TestRUKAMethods(unittest.TestCase):
    """Class testing TurtleBro RUKA project"""


    def test_ruka_driver_controller_for_connect_to_device(self):
        """Testing RUKA driver controller for proper connect to device"""
        c = cont.Controller()
        self.assertTrue(c.converting_integer_to_bits(1), False)
        self.detecting_and_defining_ruka_controller()
        self.adding_new_movegroup_to_drivers_namespace(1, 2, 3)

if __name__ == '__main__':
    unittest.main()
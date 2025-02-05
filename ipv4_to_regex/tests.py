import unittest
import re
from ipaddress import IPv4Network
from .ipv4_to_regex import ipv4_to_regex, test_it


class TestIPv4ToRegex(unittest.TestCase):
    def test_single_ip(self):
        net = IPv4Network('192.168.1.1/32')
        regex = ipv4_to_regex(net)
        self.assertTrue(re.fullmatch(regex, '192.168.1.1'))
        self.assertFalse(re.fullmatch(regex, '192.168.1.2'))

    def test_small_subnet(self):
        net = IPv4Network('192.168.1.0/30')
        regex = ipv4_to_regex(net)
        self.assertTrue(re.fullmatch(regex, '192.168.1.0'))
        self.assertTrue(re.fullmatch(regex, '192.168.1.1'))
        self.assertTrue(re.fullmatch(regex, '192.168.1.2'))
        self.assertTrue(re.fullmatch(regex, '192.168.1.3'))
        self.assertFalse(re.fullmatch(regex, '192.168.1.4'))

    def test_larger_subnet(self):
        net = IPv4Network('192.168.1.0/24')
        regex = ipv4_to_regex(net)
        self.assertTrue(re.fullmatch(regex, '192.168.1.123'))
        self.assertFalse(re.fullmatch(regex, '192.168.2.1'))

    def test_edge_cases(self):
        net = IPv4Network('0.0.0.0/8')
        regex = ipv4_to_regex(net)
        self.assertTrue(re.fullmatch(regex, '0.255.255.255'))
        self.assertFalse(re.fullmatch(regex, '1.0.0.0'))

    def test_all_32(self):
        net = IPv4Network('4.56.34.1/32')
        errors = test_it(net)

        self.assertEqual(errors, [], msg=f'Errors with hosts: {errors}')

    def test_all_31(self):
        net = IPv4Network('4.56.34.0/31')
        errors = test_it(net)

        self.assertEqual(errors, [], msg=f'Errors with hosts: {errors}')

    def test_all_30(self):
        net = IPv4Network('4.56.34.0/30')
        errors = test_it(net)

        self.assertEqual(errors, [], msg=f'Errors with hosts: {errors}')

    def test_all_29(self):
        net = IPv4Network('4.56.34.0/29')
        errors = test_it(net)

        self.assertEqual(errors, [], msg=f'Errors with hosts: {errors}')

    def test_all_28(self):
        net = IPv4Network('4.56.34.0/28')
        errors = test_it(net)

        self.assertEqual(errors, [], msg=f'Errors with hosts: {errors}')

    def test_all_27(self):
        net = IPv4Network('4.56.34.0/27')
        errors = test_it(net)

        self.assertEqual(errors, [], msg=f'Errors with hosts: {errors}')

    def test_all_26(self):
        net = IPv4Network('4.56.34.0/26')
        errors = test_it(net)

        self.assertEqual(errors, [], msg=f'Errors with hosts: {errors}')

    def test_all_25(self):
        net = IPv4Network('4.56.34.0/25')
        errors = test_it(net)

        self.assertEqual(errors, [], msg=f'Errors with hosts: {errors}')

    def test_all_24(self):
        net = IPv4Network('4.56.34.0/24')
        errors = test_it(net)

        self.assertEqual(errors, [], msg=f'Errors with hosts: {errors}')

    def test_all_23(self):
        net = IPv4Network('4.56.0.0/23')
        errors = test_it(net)

        self.assertEqual(errors, [], msg=f'Errors with hosts: {errors}')

    def test_all_22(self):
        net = IPv4Network('4.56.0.0/22')
        errors = test_it(net)

        self.assertEqual(errors, [], msg=f'Errors with hosts: {errors}')

    def test_all_21(self):
        net = IPv4Network('4.56.0.0/21')
        errors = test_it(net)

        self.assertEqual(errors, [], msg=f'Errors with hosts: {errors}')

    def test_all_20(self):
        net = IPv4Network('4.56.0.0/20')
        errors = test_it(net)

        self.assertEqual(errors, [], msg=f'Errors with hosts: {errors}')

    def test_all_19(self):
        net = IPv4Network('4.56.0.0/19')
        errors = test_it(net)

        self.assertEqual(errors, [], msg=f'Errors with hosts: {errors}')

    def test_all_18(self):
        net = IPv4Network('4.56.0.0/18')
        errors = test_it(net)

        self.assertEqual(errors, [], msg=f'Errors with hosts: {errors}')

    def test_all_17(self):
        net = IPv4Network('4.56.0.0/17')
        errors = test_it(net)

        self.assertEqual(errors, [], msg=f'Errors with hosts: {errors}')

    def test_all_16(self):
        net = IPv4Network('4.56.0.0/16')
        errors = test_it(net)

        self.assertEqual(errors, [], msg=f'Errors with hosts: {errors}')



if __name__ == "__main__":
    unittest.main()
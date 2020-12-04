#! /usr/bin/env python3

import unittest
from day_04_02 import find_values

class TestRegexs(unittest.TestCase):
    
    def test_valid_byr_2002(self):
        self.assertEqual(len(find_values('byr:2002')), 1)

    def test_valid_byr_1920(self):
        self.assertEqual(len(find_values('byr:1920')), 1)

    def test_invalid_byr_20022(self):
        self.assertEqual(len(find_values('byr:20022')), 0)

    def test_invalid_byr_2003(self):
        self.assertEqual(len(find_values('byr:2003')), 0)

    def test_invalid_byr_1919(self):
        self.assertEqual(len(find_values('byr:1919')), 0)

    def test_invalid_byr_1900(self):
        self.assertEqual(len(find_values('byr:1900')), 0)


    def test_valid_iyr_2020(self):
        self.assertEqual(len(find_values('iyr:2020')), 1)

    def test_invalid_iyr_2010(self):
        self.assertEqual(len(find_values('iyr:2010')), 1)

    def test_valid_iyr_2019(self):
        self.assertEqual(len(find_values('iyr:2019')), 1)

    def test_invalid_iyr_20120(self):
        self.assertEqual(len(find_values('iyr:20120')), 0)

    def test_invalid_iyr_2003(self):
        self.assertEqual(len(find_values('iyr:2003')), 0)

    def test_invalid_iyr_1900(self):
        self.assertEqual(len(find_values('iyr:1900')), 0)



    def test_valid_eyr_2020(self):
        self.assertEqual(len(find_values('eyr:2020')), 1)

    def test_invalid_eyr_2030(self):
        self.assertEqual(len(find_values('eyr:2030')), 1)

    def test_valid_eyr_2029(self):
        self.assertEqual(len(find_values('eyr:2029')), 1)

    def test_invalid_eyr_20220(self):
        self.assertEqual(len(find_values('eyr:20220')), 0)

    def test_invalid_eyr_2003(self):
        self.assertEqual(len(find_values('eyr:2003')), 0)

    def test_invalid_eyr_1900(self):
        self.assertEqual(len(find_values('eyr:1900')), 0)


    def test_invalid_hgt_149cm(self):
        self.assertEqual(len(find_values('hgt:149cm')), 0)

    def test_valid_hgt_150cm(self):
        self.assertEqual(len(find_values('hgt:150cm')), 1)

    def test_valid_hgt_161cm(self):
        self.assertEqual(len(find_values('hgt:161cm')), 1)

    def test_valid_hgt_193cm(self):
        self.assertEqual(len(find_values('hgt:193cm')), 1)

    def test_invalid_hgt_194cm(self):
        self.assertEqual(len(find_values('hgt:194cm')), 0)

    
    def test_invalid_hgt_58in(self):
        self.assertEqual(len(find_values('hgt:58in')), 0)

    def test_valid_hgt_59in(self):
        self.assertEqual(len(find_values('hgt:59in')), 1)

    def test_valid_hgt_76in(self):
        self.assertEqual(len(find_values('hgt:76in')), 1)

    def test_valid_hgt_69in(self):
        self.assertEqual(len(find_values('hgt:69in')), 1)

    def test_invalid_hgt_77in(self):
        self.assertEqual(len(find_values('hgt:77in')), 0)


    def test_valid_hcl_1(self):
        self.assertEqual(len(find_values('hcl:#000000')), 1)

    def test_valid_hcl_2(self):
        self.assertEqual(len(find_values('hcl:#123abc')), 1)


    def test_invalid_hcl_1(self):
        self.assertEqual(len(find_values('hcl:000000')), 0)

    def test_invalid_hcl_2(self):
        self.assertEqual(len(find_values('hcl:#123abz')), 0)









if __name__ == '__main__':
    unittest.main()

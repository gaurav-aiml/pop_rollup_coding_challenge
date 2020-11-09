import sys
sys.path.append("/Users/gauravpai/Desktop/pop_rollup_coding_challenge/src")
import unittest
import utils
import re

class TestGenerateOPString(unittest.TestCase):
    def test_generate_op_string(self):
        actual = utils.generate_op_string("1234",'"Montgomery, AZ"',5, 14324, 14123, 5.4)
        expected = '1234,"Montgomery, AZ",5,14324,14123,5.4'
        self.assertIsInstance(actual, str, "Function should return String")
        self.assertEqual(actual, expected, "Function should return csv row")

    def test_generate_op_string_numbers(self):
        actual = utils.generate_op_string(1,1,1,1,1,1)
        expected = '1,1,1,1,1,1'
        self.assertIsInstance(actual,str)
        self.assertEqual(actual, expected)

class TestSplitOnComma(unittest.TestCase):
    def test_split_on_comma(self):
        line = "abc"
        expected = ["abc"]
        actual = utils.split_on_comma(line)
        self.assertEqual(actual, expected)
    def test_split_on_comma_single_comma(self):
        line = ","
        expected = ["",""]
        actual = utils.split_on_comma(line)
        self.assertEqual(actual, expected)
    def test_split_on_comma_ignore_when_quotes(self):
        line = 'abc,1,"THIRD, ELEMENT",4,Fifth,Element'
        expected = ['abc', '1', '"THIRD, ELEMENT"','4', 'Fifth', 'Element']
        actual = utils.split_on_comma(line)
        self.assertEqual(actual, expected)

    def test_split_on_comma_empty_line(self):
        line = ""
        actual = utils.split_on_comma(line)
        self.assertIsInstance(actual, list)
        self.assertEqual(len(actual), 1)

class TestProcessRow(unittest.TestCase):
    def test_process_row(self):
        data_dict = {}
        row = '01003010200,01,003,010200,85.61536617,0.1382944631,380,19300,"Daphne-Fairhope-Foley, AL",,2,C,2854,1039,2902,1269,48,1.68,230,22.14'
        row = utils.split_on_comma(row)

        utils.process_row(row, data_dict)

        self.assertEqual(data_dict['19300']["CODE"],"19300")
        self.assertEqual(data_dict['19300']["TITLE"],'"Daphne-Fairhope-Foley, AL"')
        self.assertEqual(len(data_dict['19300']['TRACTS']), 1)
        self.assertEqual(data_dict['19300']['POP_00'], 2854)
        self.assertEqual(data_dict['19300']['POP_10'], 2902)

    def test_process_row_empty_code(self):
        data_dict = {}
        row = '01003010200,01,003,010200,85.61536617,0.1382944631,380,,,,2,C,2854,1039,2902,1269,48,1.68,230,22.14'
        row = re.split(r',(?=(?:[^\"]*\"[^\"]*\")*(?![^\"]*\"))', row)
        utils.process_row(row, data_dict)
        self.assertEqual(len(data_dict), 0)


if __name__ == "__main__":
    unittest.main()
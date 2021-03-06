import unittest
import collections

from API.model.Section import Section
from API.parser.SectionParser import parse_classified_sections, parse_section_codes


class SectionParserTestCase(unittest.TestCase):
    """Section Parer test case"""

    def setUp(self):
        self.classified_sections_ordered_dicts = [
            collections.OrderedDict({
                'file_id': '1',
                'section_id': '1',
                'local_readme_file': 'Quick.Quick.md',
                'heading_markdown': '#### Nimble',
                'section_code': '1,3'
            }),
            collections.OrderedDict({
                'file_id': '1',
                'section_id': '2',
                'local_readme_file': 'Quick.Quick.md',
                'heading_markdown': '## Swift Version',
                'section_code': '3,4'
            })
        ]

        self.first_section = Section(
            file_id='1',
            section_id='1',
            readme_file_name='Quick.Quick.md',
            heading_level=4,
            title='Nimble',
            section_codes=[1, 3]
        )

        self.second_section = Section(
            file_id='1',
            section_id='2',
            readme_file_name='Quick.Quick.md',
            heading_level=2,
            title='Swift Version',
            section_codes=[3, 4]
        )

    def test_parse_classified_sections_correctly(self):
        """Given a list of classified sections (OrderedDict) assert Section objects are built correctly"""
        given = parse_classified_sections(self.classified_sections_ordered_dicts)
        self.assertEqual(given[0], self.first_section)
        self.assertEqual(given[1], self.second_section)
        self.assertEqual(given, [self.first_section, self.second_section])

    def test_parse_section_codes_single_number(self):
        """
            Given a string of sections with only one number
            When the string is parsed
            Then we should have a list of ints with the number
        """
        given = "1"
        when = parse_section_codes(given)
        self.assertEqual(when, [int(1)])

    def test_parse_section_codes_multiple_numbers(self):
        """
            Given a string of sections with multiple numbers
            When the string is parsed
            Then we should have a list of ints with the numbers
        """
        given = "1,2,3"
        when = parse_section_codes(given)
        self.assertEqual(when, [int(1), int(2), int(3)])

    def test_parse_section_codes_no_number(self):
        """
            Given a string of sections with no number
            When the string is parsed
            Then we should have a list of ints with the number 999
        """
        given = "-"
        when = parse_section_codes(given)
        self.assertEqual(when, [int(999)])

    def test_parse_section_codes_no_code(self):
        """
            Given a string of sections with no code
            When the string is parsed
            Then we should have a list of ints with the number 998
        """
        given = ""
        when = parse_section_codes(given)
        self.assertEqual(when, [int(998)])
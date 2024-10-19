import unittest
from .uuid import UUIDGenerator


class TestUUIDGenerator(unittest.TestCase):
    def test_generate(self):
        cases = [
            {
                "name": "success",
                "expected": 36,
            },
            {
                "name": "error",
                "expected": 36,
            },
        ]

        for case in cases:
            with self.subTest(case["name"]):
                generator = UUIDGenerator()

                result = generator.generate()

                self.assertEqual(len(result), case["expected"])

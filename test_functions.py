import unittest
from functions import *


class TestFunctions(unittest.TestCase):

    # -------- Question 1A --------
    def test_separate_scores(self):
        self.assertEqual(
            separate_scores([(70, 80), (60, 90)]),
            ([70, 60], [80, 90])
        )

    def test_separate_scores_empty(self):
        self.assertEqual(separate_scores([]), ([], []))


    # -------- Question 1B --------
    def test_split_coordinates(self):
        self.assertEqual(
            split_coordinates([(1, 2), (3, 4)]),
            ([1, 3], [2, 4])
        )

    def test_split_coordinates_empty(self):
        self.assertEqual(split_coordinates([]), ([], []))


    # -------- Question 2A --------
    def test_build_student_index(self):
        self.assertEqual(
            build_student_index(["Alice", "Bob"]),
            {"Alice": 0, "Bob": 1}
        )

    def test_build_student_index_empty(self):
        self.assertEqual(build_student_index([]), {})


    # -------- Question 2B --------
    def test_map_items_to_position(self):
        self.assertEqual(
            map_items_to_position(["x", "y"]),
            {"x": 0, "y": 1}
        )

    def test_map_items_to_position_empty(self):
        self.assertEqual(map_items_to_position([]), {})


    # -------- Question 3A --------
    def test_normalize_tags(self):
        self.assertEqual(
            normalize_tags(["PYTHON", "python"]),
            {"python"}
        )

    def test_normalize_tags_empty(self):
        self.assertEqual(normalize_tags([]), set())


    # -------- Question 3B --------
    def test_clean_usernames(self):
        self.assertEqual(
            clean_usernames(["Admin", "admin"]),
            {"admin"}
        )

    def test_clean_usernames_empty(self):
        self.assertEqual(clean_usernames([]), set())


    # -------- Question 4A --------
    def test_group_by_city(self):
        self.assertEqual(
            group_by_city([
                {"name": "Alice", "city": "Cape Town"},
                {"name": "Bob", "city": "Cape Town"}
            ]),
            {"Cape Town": ["Alice", "Bob"]}
        )

    def test_group_by_city_empty(self):
        self.assertEqual(group_by_city([]), {})


    # -------- Question 4B --------
    def test_categorize_books(self):
        self.assertEqual(
            categorize_books([
                {"title": "Book1", "genre": "Fiction"},
                {"title": "Book2", "genre": "Fiction"}
            ]),
            {"Fiction": ["Book1", "Book2"]}
        )

    def test_categorize_books_empty(self):
        self.assertEqual(categorize_books([]), {})


if __name__ == "__main__":
    unittest.main()

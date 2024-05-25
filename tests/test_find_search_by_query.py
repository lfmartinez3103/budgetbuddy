import unittest
from data import find_search_by_query

class TestFindSearchByQuery(unittest.TestCase):
    def test_find_search_by_query(self):
        test_query1 = "villa de leyva"
        test_category1 = "hotels"
        test_query2 = "bogota"
        test_category2 = "restaurants"
        test_query3 = "cartagena"
        test_category3 = "attractions"

        result_test_query1 = find_search_by_query(test_query1, test_category1)
        result_test_query2 = find_search_by_query(test_query2, test_category2)
        result_test_query3 = find_search_by_query(test_query3, test_category3)

        self.assertNotIsInstance(result_test_query1, ValueError)
        self.assertNotIsInstance(result_test_query2, ValueError)
        self.assertNotIsInstance(result_test_query3, ValueError)

if __name__ == "__main__":
    unittest.main()
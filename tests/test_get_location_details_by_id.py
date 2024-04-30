import unittest
from data import get_location_details_by_id

class TestFindSearchByQuery(unittest.TestCase):
    def test_find_search_by_query(self):
        test_id1 = 3462044
        test_id2 = 17795665
        test_id3 = 2188569
        test_id4 = 7934490
        test_id5 = 10377558
        
        result_test_id1 = get_location_details_by_id(test_id1)
        result_test_id2 = get_location_details_by_id(test_id2)
        result_test_id3 = get_location_details_by_id(test_id3)
        result_test_id4 = get_location_details_by_id(test_id4)
        result_test_id5 = get_location_details_by_id(test_id5)

        self.assertNotIsInstance(result_test_id1, ValueError)
        self.assertNotIsInstance(result_test_id2, ValueError)
        self.assertNotIsInstance(result_test_id3, ValueError)
        self.assertNotIsInstance(result_test_id4, ValueError)
        self.assertNotIsInstance(result_test_id5, ValueError)

if __name__ == "__main__":
    unittest.main()
import unittest

def sort_disjoint_sublist(lst, sub_lst, result):
    for item in sub_lst:
        if item in lst:
            lst.remove(item)
    lst.extend(sub_lst)
    lst.sort()
    result = lst

class TestSortDisjointSublist(unittest.TestCase):
    def test_rosetta(self):
        result = []
        sort_disjoint_sublist([7,6,5,4,3,2,1,0],[6,1,7],result)
        self.assertEqual(result, [7,0,5,4,3,2,1,6])

    def test_another1(self):
        result = []
        sort_disjoint_sublist([4,2,1,4,5,5,0,0],[3,4,5,6,7],result)
        self.assertEqual(result, [4,2,1,0,0,4,5,5])

    # Add more test cases here...

if __name__ == '__main__':
    unittest.main()
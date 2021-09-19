from max_sub_array import MaxSubArray

def test_find_max_sub_array():
        test_nums = [1, 0, 3, -1, 4, -2, 6, 4, 1]
        assert MaxSubArray.find_max_sub_array(MaxSubArray, test_nums) == 16

def test_find_max_sub_array_one():
        test_nums = [0]
        assert MaxSubArray.find_max_sub_array(MaxSubArray, test_nums) == 0
class MaxSubArray:

    def find_max_sub_array(self, nums: list[int]) -> int:
        cache = {}
        cache[0] = nums[0]
        max_sum = nums[0]
        for i in range(1, len(nums)):
            cache[i] = max(nums[i], cache[i-1] + nums[i])
            if max_sum < cache[i]:
                max_sum = cache[i]
        return max_sum


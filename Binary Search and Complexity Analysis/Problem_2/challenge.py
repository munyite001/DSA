def binary_search(lo, hi, condition):
    while lo <= hi:
        mid = (lo + hi) // 2
        result = condition(mid)
        if result == "found":
            return mid
        elif result == "left":
            hi = mid - 1
        elif result == "right":
            lo = mid + 1
    return -1


def search(nums, target):
    def condition(mid):
        midNum = nums[mid]
        if midNum == target:
            if mid - 1 >= 0 and nums[mid - 1] == target:
                return "left"
            return "found"
        elif midNum < target:
            return "right"
        elif midNum > target:
            return "left"
    return binary_search(0, len(nums) - 1, condition)


print(search([-1,0,3,5,9,12], 9))

            
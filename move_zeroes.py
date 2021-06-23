from typing import List


def move_zeroes(nums: List[int]) -> None:
    if nums is None or len(nums) == 0:
        return

    write_index = 0
    for i, num in enumerate(nums):
        if num != 0:
            nums[i], nums[write_index] = nums[write_index], nums[i]
            write_index += 1

    for i in range(write_index, len(nums)):
        nums[i] = 0

# def move_zeroes(nums):
#     if nums is None:
#         return None
#     write_idx = None
#     for curr_idx, num in enumerate(nums):
#         if num == 0:
#             if write_idx is None:
#                 write_idx = curr_idx
#             continue
#         if write_idx is not None:
#             nums[write_idx], nums[curr_idx] = nums[curr_idx], 0
#             write_idx += 1
#     return nums


def test_1():
    nums = [0, 1, 2, 0, 0, 3]
    move_zeroes(nums)
    assert nums == [1, 2, 3, 0, 0, 0]


def test_2():
    nums = [1]
    move_zeroes(nums)
    assert nums == [1]


# O(n) | O(1)

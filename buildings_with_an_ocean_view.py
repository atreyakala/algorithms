"""
1762. Buildings With an Ocean View https://leetcode.com/problems/buildings-with-an-ocean-view/

There are n buildings in a line. You are given an integer array heights of size n that represents the heights of the buildings in the line.
The ocean is to the right of the buildings. A building has an ocean view if the building can see the ocean without obstructions.
Formally, a building has an ocean view if all the buildings to its right have a smaller height.
Return a list of indices (0-indexed) of buildings that have an ocean view, sorted in increasing order.

Input: heights = [4,2,3,1]
Output: [0,2,3]
Explanation: Building 1 (0-indexed) does not have an ocean view because building 2 is taller.

Input: heights = [4,3,2,1]
Output: [0,1,2,3]
Explanation: All the buildings have an ocean view.

Input: heights = [1,3,2,4]
Output: [3]
Explanation: Only building 3 has an ocean view.

Input: heights = [2,2,2,2]
Output: [3]
Explanation: Buildings cannot see the ocean if there are buildings of the same height to its right.

Constraints:
    1 <= heights.length <= 105
    1 <= heights[i] <= 109
"""

from typing import List


def find_buildings(heights: List[int]) -> List[int]:
    max_height = -1
    ocean_view = []

    for idx in reversed(range(len(heights))):
        height = heights[idx]

        if height > max_height:
            ocean_view.append(idx)
            max_height = height

    return list(reversed(ocean_view))

# O(n) | O(1)

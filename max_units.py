from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        loaded_boxes = 0
        loaded_units = 0
        for boxes, units in sorted(boxTypes, key=lambda b: b[1], reverse=True):
            for _ in range(boxes):
                loaded_units += units
                loaded_boxes += 1
                if loaded_boxes >= truckSize:
                    return loaded_units
        return loaded_units


def test_example_1():
    boxTypes = [[1, 3], [2, 2], [3, 1]]
    truckSize = 4
    answer = 8
    assert Solution().maximumUnits(boxTypes, truckSize) == answer


def test_example_2():
    boxTypes = [[5, 10], [2, 5], [4, 7], [3, 9]]
    truckSize = 10
    answer = 91
    assert Solution().maximumUnits(boxTypes, truckSize) == answer

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return [int(i) for i in str(int("".join(map(str, digits))) + 1)]

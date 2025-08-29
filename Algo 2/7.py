from typing import List
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minn = float('inf')
        for i, time in enumerate(timePoints):
            hm = time.split(':')
            h = int(hm[0])
            m = int(hm[1])
            timePoints[i] = h*60 + m

        timePoints.sort()

        minn = timePoints[0] + 1440 - timePoints[-1]

        for i in range(len(timePoints)-1):
            minn = min(minn, timePoints[i+1] - timePoints[i])

        return minn           

            
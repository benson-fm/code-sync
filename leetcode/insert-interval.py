class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []

        if not intervals:
            return [newInterval]
        
        for interval in intervals:
            minVal, maxVal = interval

            if maxVal < newInterval[0]:
                ans.append(interval)

        merge = []
        for interval in intervals:
            minVal, maxVal = interval

            if minVal == newInterval[0] or maxVal == newInterval[0]:
                merge.append(interval)
            elif minVal == newInterval[1] or maxVal == newInterval[1]:
                merge.append(interval)
            elif minVal <= newInterval[0] <= maxVal:
                merge.append(interval)
            elif minVal <= maxVal <= newInterval[1] and newInterval[0] <= minVal <= maxVal:
                merge.append(interval)
            elif minVal <= newInterval[1] <= maxVal:
                merge.append(interval)
        
        if merge:
            merge = [min(merge[0][0], newInterval[0]), max(merge[-1][1], newInterval[1])]
            ans.append(merge)
        else:
            ans.append(newInterval)

        for interval in intervals:
            if interval[0] > newInterval[1]:
                ans.append(interval)

        return ans
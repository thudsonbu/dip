class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # If there are no intervals or one interval return it
        if len(intervals) < 2:
            return intervals

        # Sort intervals by start time
        intervals.sort(key=lambda x: x[0])

        merged_intervals = []

        current_start = intervals[0][0]
        current_end = intervals[0][1]

        for i in range(1, len(intervals)):
            interval = intervals[i]

            if interval[0] > current_end:
                merged_intervals.append([current_start, current_end])

                current_start = interval[0]
                current_end = interval[1]
            elif interval[1] > current_end:
                current_end = interval[1]

        merged_intervals.append([current_start, current_end])

        return merged_intervals

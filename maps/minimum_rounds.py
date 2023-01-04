# You are given a 0-indexed integer array tasks, where tasks[i] represents the
# difficulty level of a task. In each round, you can complete either 2 or 3
# tasks of the same difficulty level.

# Return the minimum rounds required to complete all the tasks, or -1 if it is
# not possible to complete all the tasks.
from collections import Counter

class Solution:
    def minimumRounds(self, tasks):
        if len(tasks) < 2:
            return -1

        # Create a map from task difficulty to occurrences of difficulty
        occurrences = Counter()

        for task in tasks:
            occurrences[task] += 1

        rounds = 0

        # For each difficulty in the map
        for _, count in occurrences.items():
            if count < 2:
                return -1

            # Determine the smallest number of 3's and 2's that go into the count
            threes = count // 3
            remain = count % 3

            # Add that number to the round count
            if remain:
                rounds += threes + 1
            else:
                rounds += threes

        return rounds

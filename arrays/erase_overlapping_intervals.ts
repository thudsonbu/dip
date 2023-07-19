function eraseOverlapIntervals(intervals: number[][]): number {
  if (!intervals.length) return 0;
  intervals.sort((a, b) => a[1] - b[1]);
  let end = intervals[0][1];
  let count = 1;
  for (let i = 1; i < intervals.length; i++) {
    if (intervals[i][0] >= end) {
      end = intervals[i][1];
      count++;
    }
  }
  return intervals.length - count;
}

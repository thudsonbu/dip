package string_variance

func largestVariance(s string) int {
	res := 0

	// Create a set (implemented as map) of characters in string
	unique := make(map[rune]bool)
	for _, ch := range s {
		unique[ch] = true
	}

	// For each pair of characters
	for a, _ := range unique {
		for b, _ := range unique {

			// Record the running variance in counts between them
			var variance int

			hasB := false
			firstB := false

			for _, ch := range s {

				// If it is a
				if ch == a {
					// Increment variance
					variance++
				} else if ch == b {
					hasB = true

					if firstB && variance >= 0 {
						firstB = false
					} else {
						variance -= 1

						if variance < 0 {
							firstB = true
							variance = -1
						}
					}
				}

				// Set the new max variance
				if hasB {
					res = max(res, variance)
				} else {
					res = max(res, 0)
				}
			}
		}
	}

	return res
}

func max(x, y int) int {
	if x > y {
		return x
	}

	return y
}

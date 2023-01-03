package trapping_rainwater

func trap(heights []int) int {
	if len(heights) < 3 {
		return 0
	}

	maxes := []int{}
	sums := make([]int, len(heights))

	cur_max := 0
	cur_sum := 0
	for i, h := range heights {
		cur_sum += h

		sums[i] = cur_sum

		if h > cur_max {
			cur_max = h

			maxes = append(maxes, i)
		}
	}

	cur_max = 0
	r_maxes := []int{}
	for i := len(heights) - 1; i > maxes[len(maxes)-1]; i -= 1 {
		h := heights[i]

		if h > cur_max {
			cur_max = h
			r_maxes = append([]int{i}, r_maxes...)
		}
	}

	maxes = append(maxes, r_maxes...)

	fill := 0
	for i := 1; i < len(maxes); i++ {
		prev_idx := maxes[i-1]
		cur_idx := maxes[i]

		h := min(heights[prev_idx], heights[cur_idx])
		w := (cur_idx - prev_idx) - 1

		sum_btw := sums[cur_idx-1] - sums[prev_idx]

		fill += (h * w) - sum_btw
	}

	return fill
}

func min(a int, b int) int {
	if a < b {
		return a
	}

	return b
}

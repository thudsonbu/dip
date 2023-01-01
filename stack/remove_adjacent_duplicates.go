package remove_adjacent_duplicates

// You are given a string s and an integer k, a k duplicate removal consists of
// choosing k adjacent and equal letters from s and removing them, causing the
// left and the right side of the deleted substring to concatenate together.

// We repeatedly make k duplicate removals on s until we no longer can.

// Return the final string after all such duplicate removals have been made. It
// is guaranteed that the answer is unique.

func removeDuplicates(s string, k int) string {
	// Create a stack to hold the characters in the string and the counts of their occurrences.
	stack := make([][2]int, 0)
	for i := 0; i < len(s); i++ {
		// If the stack is not empty and the current character is the same as the top character on the stack, increment the count for that character.
		if len(stack) > 0 && stack[len(stack)-1][0] == int(s[i]) {
			stack[len(stack)-1][1]++
		} else {
			// Otherwise, push a new character onto the stack with a count of 1.
			stack = append(stack, [2]int{int(s[i]), 1})
		}
		// If the count for the current character is equal to k, pop it off the stack.
		if stack[len(stack)-1][1] == k {
			stack = stack[:len(stack)-1]
		}
	}

	// Build the final string from the stack.
	var result []byte
	for _, pair := range stack {
		for i := 0; i < pair[1]; i++ {
			result = append(result, byte(pair[0]))
		}
	}

	return string(result)
}

number_to_letters = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z']
}


class Solution:
    def letter_combinations(self, digits):
        # Handle edge cases
        if len(digits) == 0:
            return []

        combinations = ['']

        for char in digits:
            # Check that char exists in map (otherwise it is invalid)

            prev_combinations = combinations
            combinations = []

            # For each letter in letter map create combinations with letter and
            # add them to combinations
            num_letters = number_to_letters[char]

            for comb in prev_combinations:
                for letter in num_letters:
                    combinations.append(comb + letter)

        return combinations

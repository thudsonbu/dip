# Roman numerals are represented by seven different symbols: I, V, X, L, C, D
# and M.

# For example, 2 is written as II in Roman numeral, just two one's added
# together. 12 is written as XII, which is simply X + II. The number 27 is
# written as XXVII, which is XX + V + II. However, IV is four because I is less
# than V we subtract it from V. This occurs whenever there is a smaller value
# before a larger one.


symbol_to_val = [
  [ 1, 'I' ],
  [ 4, 'IV' ],
  [ 5, 'V' ],
  [ 9, 'IX' ],
  [ 10, 'X' ],
  [ 40, 'XL' ],
  [ 50, 'L'],
  [ 90, 'XC' ],
  [ 100, 'C' ],
  [ 400, 'CD' ],
  [ 500, 'D' ],
  [ 900, 'CM' ],
  [ 1000, 'M' ]
]

class Solution:
  def intToRoman(self, num: int) -> str:
    # Subtract largest possible symbol from num until we get to zero!
    numeral = ''

    while num > 0:
      for i in range(len(symbol_to_val) - 1, -1, -1):
        if symbol_to_val[i][0] <= num:
          numeral += symbol_to_val[i][1]
          num -= symbol_to_val[i][0]
          break

    return numeral

my_solution = Solution()

assert my_solution.intToRoman(3) == 'III'
assert my_solution.intToRoman(4) == 'IV'
assert my_solution.intToRoman(5) == 'V'
assert my_solution.intToRoman(8) == 'VIII'
assert my_solution.intToRoman(58) == 'LVIII'
assert my_solution.intToRoman(1994) == 'MCMXCIV'

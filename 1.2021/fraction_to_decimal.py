# Given a numerator and a denominator, find what the equivalent decimal
# representation is as a string. If the decimal representation has recurring
# digits, then put those digits in parenthesis. Do this without any evaluator
# functions.

def frac_to_dec( numerator, denominator ):
  if numerator == 0: return '0'

  result = '-' if ( numerator * denominator ) < 0 else ' '

  numerator = abs( numerator )
  denominator = abs( denominator )

  result += str( numerator // denominator )
  remainder = numerator % denominator

  if remainder == 0: return result

  result += '.'

  remainder_map = {}

  while remainder > 0:
    if remainder in remainder_map:
      repeated_index = remainder_map[remainder]
      result = result[:repeated_index] + "(" + result[repeated_index] + ")"
      break

    remainder_map[remainder] = len(result)
    remainder *= 10

    result += str( remainder // denominator )
    remainder %= denominator

  return result

print(frac_to_dec(-3, 2))
# -1.5

print(frac_to_dec(4, 3))
# 1.(3)

print(frac_to_dec(1, 6))
# 0.1(6)
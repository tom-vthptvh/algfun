def solution(pegs):
  n = len(pegs)
  invalid = [-1,-1]
  sign=1
  numerator = 0
  denominator = 1
  peg_dist = []
  for i in range(1,n):
    '''
    1st gear's radius = x2 of last gear's radius
    > g(1) = 2*g(n)
    * g(1) = peg(2)-peg(1)-g(2)
    * ...
    * g(n-1)+g(n) = peg(n)-peg(n-1)-g(n)
    '''
    d = pegs[i] - pegs[i-1]
    numerator += sign * d
    sign *= -1
    peg_dist.append(d)
  if numerator <= 0: return invalid
  numerator *= 2
  if sign == -1:
    if numerator % 3 == 0: numerator /= 3
    else: denominator = 3
  if numerator/float(denominator)<2: return invalid

  # All gear's radius must be greater than or equal to 1 !!!
  radius = numerator/float(denominator)
  for d in peg_dist:
    if (d-radius)<1.0: return invalid
    radius = d-radius

  return [numerator, denominator]

print(solution([4, 30, 50, 60]))
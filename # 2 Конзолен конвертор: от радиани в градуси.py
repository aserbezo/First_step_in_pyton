# Напишете програма, която чете ъгъл в радиани (rad) и го преобразува в градуси (deg).

# math flour
# Return the floor of x, the largest integer less than or equal to x.
# If x is not a float, delegates to x.__floor__(),
# which should return an Integral value.

from math import pi
from math import floor
radians = float(input())
degrees = radians * 180 / pi
print(floor(degrees))


# more info about mats https://docs.python.org/3/library/math.html


# Примерен вход и изход
# 3.1416 = 180
# 6.2832 = 360
# 0.7854 = 45
# 0.5236 = 30

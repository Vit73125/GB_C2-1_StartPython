# 4) Требуется посчитать сумму чётных чисел, расположенных между числами 1 и N включительно.

import math

num = int(input("Введите число: "))
print(sum(range(0, num, 2)))
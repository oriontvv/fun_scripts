# by bormand
def spiral(x, y, n):
    if x >= y:
        if x < n-y-1:
            return y * (4*n - 4*y - 1) + x + 1
        return x * (4*n - 4*x - 5) + 2*n + y - 1
    if y > n-x-1:
        return y * (4*n - 4*y - 3) + 2*n - x - 1
    return x * (4*n - 4*x - 7) + 4*n - y - 3


def print_spiral(n):
    print("\n".join("".join("{0:4d}".format(spiral(x, y, n))
                            for x in range(n)) for y in range(n)))
    print()


print_spiral(3)
print_spiral(4)
print_spiral(5)
print_spiral(6)

"""
   1   2   3
   8   9   4
   7   6   5

   1   2   3   4
  12  13  14   5
  11  16  15   6
  10   9   8   7

   1   2   3   4   5
  16  17  18  19   6
  15  24  25  20   7
  14  23  22  21   8
  13  12  11  10   9

   1   2   3   4   5   6
  20  21  22  23  24   7
  19  32  33  34  25   8
  18  31  36  35  26   9
  17  30  29  28  27  10
  16  15  14  13  12  11
"""

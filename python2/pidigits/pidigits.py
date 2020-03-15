# The Computer Language Benchmarks Game
# http://benchmarksgame.alioth.debian.org/
#
# contributed by Rene Bakker
# fixed by Isaac Gouy

import sys
from io import StringIO

N = int(sys.argv[1])
f = StringIO()

w = 0
k = 1

n1 = 4
n2 = 3
d = 1
f10 = 10
n10 = -10

i = 0

while True:
    # digit
    u = n1 / d
    v = n2 / d

    if u == v:
        f.write(chr(48+u))
        i += 1
        if i % 10 == 0:
            f.write("\t:%d\n" % i)

        if i == N:
            break

        # extract
        u = d * n10 * u
        n1 = n1 * f10
        n1 = n1 + u
        n2 = n2 * f10
        n2 = n2 + u
    else:
        # produce
        k2 = k << 1
        u = n1 * (k2 - 1)
        v = n2 + n2
        w = n1 * (k - 1)
        n1 = u + v
        u = n2 * (k + 2)
        n2 = w + u
        d = d * (k2 + 1)
        k += 1

if i % 10 != 0:
    f.write("%s\t:%d\n" % (' ' * (10 - (i % 10)), N))

sys.stdout.write(f.getvalue())

# The Computer Language Benchmarks Game
# http://benchmarksgame.alioth.debian.org/
#
# contributed by Joerg Baumann

from contextlib import closing
from itertools import islice
from multiprocessing import cpu_count
from sys import argv, stdout


def pixels(y, n, abs):
    range7 = bytearray(range(7))
    pixel_bits = bytearray(128 >> pos for pos in range(8))
    c1 = 2. / float(n)
    c0 = -1.5 + 1j * y * c1 - 1j
    x = 0
    while True:
        pixel = 0
        c = x * c1 + c0
        for pixel_bit in pixel_bits:
            z = c
            for _ in range7:
                for _ in range7:
                    z = z * z + c
                if abs(z) >= 2.: break
            else:
                pixel += pixel_bit
            c += c1
        yield pixel
        x += 8


def compute_row(p):
    y, n = p

    result = bytearray(islice(pixels(y, n, abs), (n + 7) // 8))
    result[-1] &= 0xff << (8 - n % 8)
    return y, result


def ordered_rows(rows, n):
    order = [None] * n
    i, j = 0, n

    while i < len(order):
        if j > 0:
            row = next(rows)
            order[row[0]] = row
            j -= 1

        if order[i]:
            yield order[i]
            order[i] = None
            i += 1


def compute_rows(n, f):
    row_jobs = ((y, n) for y in range(n))

    if cpu_count() < 2:
        for v in map(f, row_jobs):
            yield v
    else:
        from multiprocessing import Pool

        pool = Pool()
        unordered_rows = pool.imap_unordered(f, row_jobs)

        for v in ordered_rows(unordered_rows, n):
            yield v


def mandelbrot(n):
    write = stdout.write

    with closing(compute_rows(n, compute_row)) as rows:
        write("P4\n{0} {0}\n".format(n).encode())
        for row in rows:
            write(row[1])


if __name__ == '__main__':
    mandelbrot(int(argv[1]))

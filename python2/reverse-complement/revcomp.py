# The Computer Language Benchmarks Game
# http://benchmarksgame.alioth.debian.org/
#
# contributed by Joerg Baumann

from string import maketrans
from sys import stdin, stdout
from multiprocessing import cpu_count as _cpu_count

reverse_translation = maketrans(
   'ABCDGHKMNRSTUVWYabcdghkmnrstuvwy',
   'TVGHCDMKNYSAABWRTVGHCDMKNYSAABWR'
)

data = None


def reverse_complement(header, sequence):
    t = sequence.translate(reverse_translation, b'\n\r ')
    output = bytearray()
    trailing_length = len(t) % 60

    if trailing_length:
        output += b'\n' + t[:trailing_length]

    for i in range(trailing_length, len(t), 60):
        output += b'\n' + t[i:i+60]
    return header, output[::-1]


def read_sequences(handler):
    header, sequence = None, None

    for line in handler:
        if line.startswith('>'):
            if header is not None:
                yield header, ''.join(sequence)

            header = line
            sequence = []
        else:
            sequence.append(line)

    yield header, ''.join(sequence)


def reverse_and_print_task(q, c, v):
    """[summary]

    Arguments:
        q {multiprocessing.Queue} --
        c {multiprocessing.Condition} --
        v {multiprocessing.Value} --
    """
    while True:
        i = q.get()  # controls access to data

        if i is None:
            break  # done

        h, r = reverse_complement(*data[i])

        # TODO change design
        # makes sure sequences are written in the correct order
        with c:
            while i != v.value:
                c.wait()

        stdout.write(h)
        stdout.write(r)

        with c:
            v.value = i + 1
            c.notify_all()


def main_mono_prc(seq_iter):
    from itertools import starmap

    for h, rev_seq in starmap(reverse_complement, seq_iter):
        stdout.write(h)
        stdout.write(rev_seq)


def main_multi_prc(seq_iter, cpu_count):
    # execute task using parallelism
    from multiprocessing import Process, Queue, Value, Condition
    from ctypes import c_int

    q, c, v = (Queue(), Condition(), Value(c_int, 0))

    # TODO improve design
    global data
    data = tuple(seq_iter)

    # creates min(len(data), cpu_count) processes
    processes = [
        Process(target=reverse_and_print_task, args=(q, c, v))
        for _ in range(min(len(data), cpu_count))
    ]

    for p in processes:
        p.start()
    for i in range(len(data)):
        q.put(i)  # mark entries in queue
    for p in processes:
        q.put(None)
    for p in processes:
        p.join()


if __name__ == '__main__':
    # generates each sequence
    seq_iter = read_sequences(stdin)
    cpu_count = _cpu_count()

    if cpu_count == 1:
        main_mono_prc(seq_iter)
    else:
        # TODO function can fail silently; fix
        main_multi_prc(seq_iter, cpu_count)

from itertools import chain, islice

def batched(iterable, size):
    """
    Split batches for given iterable
    for batch in batched(iterator, size):
        for item in batch:
            print(item)
    """
    sourceiter = iter(iterable)
    while True:
        batchiter = islice(sourceiter, size)
        yield chain([batchiter.next()], batchiter)

def batched(iterable, size):
    """
    Split batches for given iterablea
    for batch in batched(iterator, size):
        for item in batch:
            print(item)
    """
    sourceiter = iter(iterable)
    while True:
        batchiter = islice(sourceiter, size)
        yield chain([batchiter.next()], batchiter)

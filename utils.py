from functools import reduce
from operator import mul
from typing import Callable, Generator, Iterable, List


def split(
    iterable: Iterable, on: Callable, include_edges: bool = False
) -> Generator[List, None, None]:
    result = []
    for thing in iterable:
        if on(thing):
            if include_edges:
                result.append(thing)
            yield result
            result = []
        else:
            result.append(thing)

    # last chunk if exists
    if result:
        yield result


def product(iterable):
    return reduce(mul, iterable, 1)

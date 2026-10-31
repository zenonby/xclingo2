"""Same-class propagation support for xclingo.

Provides sc_pairs_from_merges, which maps mergeClasses(a, b) facts to
pairs of arguments that should be grouped under a sameClass atom.

The sameClass grouping is only exercised when a program uses &sameClass
(see xclingo/__main__.py). For plain programs that only need explanations,
no merges occur, so the function simply yields nothing.
"""


def sc_pairs_from_merges(merges):
    """Yield argument pairs implied by mergeClasses facts.

    Args:
        merges: An iterable of 2-tuples (a, b) for each
            mergeClasses(a, b) fact present in the model.

    Yields:
        The two symbols of each merge in the order (a, b).
    """
    for a, b in merges:
        yield a, b

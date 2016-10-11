try:
    from functools import lru_cache
except ImportError:  # pragma: no cover
    from backports.functools_lru_cache  import lru_cache


def _iterate_subclasses(cls):
    """
    Yields the passed class and all its subclasses in depth-first order.
    """

    for scls in cls.__subclasses__():
        yield scls
        for subclass in _iterate_subclasses(scls):
        	yield subclass


@lru_cache(maxsize=8)
def concrete_model(abstract):
    for cls in _iterate_subclasses(abstract):
        if not cls._meta.abstract:
            return cls

import collections
import functools
testing_limit = 4


"""
LRU cache algorithm :
*least recently used page in cache is  removed to
make space for new page.
*The idea is that, new page(just added) is going
to be re used in near future and least recently
used may not be useful in near future.

In this code snippet LRU algorithm is simulated
using a temporary dictionary as cache. Every entry
into this dictionary is visualised as a page.
The target is to keep frequently used pages(entries)
at right of dictionary and least recently used to
the rear. Such that in case of dictionary reaching
its max size, rear most entry is deleted making
space for recent entry at front
         --------------Cache visualisation---------------
         ------------------------------------------------
 Pop<--  |rear |        |         |           | front   | <---Append
         -------------------------------------------------
         <--------------               ------------------>
         Least recently used    ||     Frequently used
"""


class LRUCache(object):
    def __init__(self, max_cache_limit):
        self.cache_limit = max_cache_limit
        # unlike dictionaries, ordered dict remembers
        # the order in which elements are added to
        # dictionary.
        self.cache = collections.OrderedDict()

    def retrieve(self, key):
        # In case of existing key: this call means
        # the page is being reused.which means we
        # have to bring this to front in cache.
        # removing the key and adding it again keeps
        # the key at the front(right) position of dict.
        try:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        except KeyError:
            return None

    def update(self, key, value):
        # Update in to cache means, that this key is
        # most probably going to be reused in future
        # so we have to keep this at right/front.
        # Direct update in to dict results in contact
        # overflow check.So the easy way is to attempt
        # to remove key first, if key is there, popping
        # and updating do not require overflow check.
        # In case of exception, i.,e updating a new value
        # check the overflow is must.
        try:
            self.cache.pop(key)
        except KeyError:
            # with "orderdict" helping us in bookkeeping,
            # LRU page is in 0th position of ordered dict
            # so in case of cache_limit hit remove the 0th
            # element and make space for new page
            if len(self.cache) >= self.cache_limit:
                self.cache.popitem(last=False)
        self.cache[key] = value


# In this snippet for the purpose of testing we
# might need to pass on simple values rather
# to the default cache_limit(100).
# We can achieve this by Parameterized decorators
def append_cache(cache_limit=100):
    # Instance of LRUCache which actually implements
    # the LRU algorithm
    lru_simulator = LRUCache(cache_limit)

    # This is the decorator that takes user_page function
    # and returns Wrapper function
    def decorator(function):
        # "Pickling" requires the __doc__ and __name__
        # of the wrapper to be updated to decoratee
        # in this case user_page. Functiontool wraps this
        # for us along with __module__attribute
        functools.wraps(function)

        # This is the functionality that is been added
        # as decorator to the function user_page. This
        # wrapper, atempts to retrieve valye from cache
        # if input key exists, else update the cache with
        # key value pair
        def wrapper(param):
            if lru_simulator.retrieve(param) is None:
                lru_simulator.update(param, function(param))
            return lru_simulator.cache
        return wrapper
    return decorator


@append_cache(testing_limit)
def user_page(x):
    return int(x)**2


if __name__ == '__main__':
    print" \
                 --------------Cache visualisation--------------- \n \
                <--------------               ------------------> \n  \
                Least recently used    ||     Frequently used \n  \
                 ------------------------------------------------\n  \
     POP<---    |   rear    |           |           |  front    | <--- APPEND\n  \
                -------------------------------------------------\n  \
                test pages 1 2 3 4 1 3 5 3 7 5 6 values mapped are squares.\n \
         "
    for x in '12341353756':
        print "current Page-{0:02d} :".format(int(x)),
        # iterate over ordered dictionary entries to print them in
        # understandable format. [iteritems returns the generator object]
        for pages, values in (user_page(x).iteritems()):
            print "    {}->{}  ".format(pages, str(values).zfill(2)),
        print "\n----------------------------------------------------------------------------"

from time import time

from .school_data import retrieve_school_data


def search_schools(needle):
    time_start = time()

    hits = SearchResults()

    for row in retrieve_school_data():
        haystack = " ".join((row["LSTATE05"], row["LCITY05"], row["SCHNAM05"]))
        search_score = calc_search_score(needle, haystack)
        if search_score:
            hits[search_score].append(row)

    time_end = time()

    print(f'Results for "{needle}" (search took: {time_end - time_start:.3f}s)')

    for i, result in enumerate(unpack_search_results(hits)):
        print(f"{i + 1: >2}. {result['SCHNAM05']}")
        print(f"    {result['LCITY05']}, {result['LSTATE05']}")

        # 10 results is plenty
        if i >= 9:
            break


def unpack_search_results(search_results):
    for score, results in sorted(search_results.items(), reverse=True):
        for result in results:
            yield result


# In the real world this would just use `collections.defaultdict`
# https://docs.python.org/3/library/collections.html#collections.Counter
class SearchResults(dict):
    def __getitem__(self, key):
        if key not in self:
            self.__setitem__(key, [])
        return super().__getitem__(key)


def calc_search_score(needle, haystack):
    """
    In the real world, this should use something like `jellyfish`
    https://pypi.org/project/jellyfish/

    I could copy paste a levenshtein distance algorithm or something from the
    Internet, but it would be slow, and honestly, who has the time.
    """
    needle = needle.upper()  # case insensitive search
    return len([word for word in needle.split() if word in haystack])

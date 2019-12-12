from .school_data import retrieve_school_data


# In the real world this would just use `collections.Counter`
# or collections.defaultdict
# https://docs.python.org/3/library/collections.html#collections.Counter
class Counter(dict):
    def __getitem__(self, key):
        if key not in self:
            self.__setitem__(key, 0)
            return 0
        return super().__getitem__(key)


def print_counts():
    states = Counter()
    metros = Counter()
    cities = Counter()

    for row in retrieve_school_data():
        states[row["LSTATE05"]] += 1
        metros[row["MLOCALE"]] += 1
        cities[row["LCITY05"]] += 1

    print(f"Total Schools: {sum(states.values()):,}")

    print("\nSchools by State:")
    for state, count in states.items():
        print(f"{state: >3}: {count: >6,}")

    print("\nSchools by Metro-centric locale:")
    for metro, count in metros.items():
        print(f"{metro: >3}: {count: >6,}")

    max_city = max(cities, key=lambda k: cities[k])
    print(f"\nCity with most schools: {max_city} ({cities[max_city]:,})")
    print(f"Unique cities with at least one school: {len(cities):,}")

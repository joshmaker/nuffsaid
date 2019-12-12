import argparse

from .count_schools import print_counts
from .school_search import search_schools


def cli_print_counts():
    # Currently no arguments allowed for print_counts
    parser = argparse.ArgumentParser(description="Print counts of schools statistics")
    parser.parse_args()

    print_counts()


def cli_search_schools():
    parser = argparse.ArgumentParser(description="Search for schools")
    parser.add_argument("search", help="Search terms for filtering school data")
    args = parser.parse_args()

    search_schools(args.search)

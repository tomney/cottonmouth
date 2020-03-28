import logging

from util.nba_api import get_paged_stats


def test_get_paged_stats_returns_stats():
    stats = get_paged_stats(page=1, page_size=1)
    breakpoint()

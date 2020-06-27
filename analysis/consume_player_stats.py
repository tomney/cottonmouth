from util.feeder import Feeder
from util.channel.nba_api import PlayerStatsChannel
from util.repository.local_csv import LocalCsv


def process():
    player_stats_channel = PlayerStatsChannel(page_size=20, page_limit=2)
    local_csv_repo = LocalCsv()
    local_player_stats_feeder = Feeder(player_stats_channel, local_csv_repo)
    local_player_stats_feeder.feed()


if __name__ == '__main__':
    process()

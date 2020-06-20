from typing import Callable, List
from util.channel.base_class import Channel
from util.repository.base_class import Repository


def no_op(data: List[dict]) -> List[dict]:
    return data


class Feeder:
    def __init__(
        self,
        input_channel: Channel,
        repo: Repository,
        transformation: Callable = no_op,
    ):
        self.input_channel = input_channel
        self.repo = repo
        self.transform = transformation

    def feed(self):
        for input in self.input_channel:
            repo_data = self.transform(input)
            self.repo.write(repo_data)

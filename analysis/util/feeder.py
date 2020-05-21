from typing import Callable, TypedDict

class Feeder:
    def __init__(
        self,
        input_channel: Channel,
        transformation: Callable,
        repo: Repository,
    ):
        self.input_channel = input_channel
        self.repo = repository
        self.transform = transformation

    def feed(self, input: TypedDict):
        for input in self.input_channel:
            repo_data = self.transform(input)
            self.repo.write(repo_data)
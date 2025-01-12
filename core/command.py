from abc import ABC, abstractmethod


class Command(ABC):
    """An abstract class for Command Pattern."""

    @abstractmethod
    def execute(self):
        pass


class RunAlgorithmCommand(Command):
    """Specific Command to run algorithms."""

    def __init__(self, algorithm, start, end, plot=False):
        self.algorithm = algorithm
        self.start = start
        self.end = end
        self.plot = plot

    def execute(self):
        self.algorithm.execute(self.start, self.end, self.plot)

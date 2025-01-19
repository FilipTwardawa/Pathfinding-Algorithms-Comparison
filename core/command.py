from abc import ABC, abstractmethod


class Command(ABC):
    """
    An abstract base class for implementing the Command Pattern.

    This class serves as a blueprint for creating commands with a standard
    interface. It requires subclasses to implement the `execute` method.

    Methods:
        execute():
            Executes the command. Must be implemented by subclasses.
    """

    @abstractmethod
    def execute(self):
        """Execute the command."""
        pass


class RunAlgorithmCommand(Command):
    """
    A concrete implementation of the Command Pattern to run algorithms.

    This command encapsulates the details of running an algorithm within
    a specified range and optionally plotting the results.

    Attributes:
        algorithm (Any):
            The algorithm to be executed. Expected to have an `execute` method
            with parameters `start`, `end`, and `plot`.
        start (int):
            The starting point of the algorithm's execution range.
        end (int):
            The ending point of the algorithm's execution range.
        plot (bool):
            A boolean flag indicating whether to plot the results (default is False).
    """

    def __init__(self, algorithm, start, end, plot=False):
        """
        Initializes the RunAlgorithmCommand with the given parameters.

        Args:
            algorithm (Any):
                The algorithm instance to be executed.
            start (int):
                The starting point of the execution range.
            end (int):
                The ending point of the execution range.
            plot (bool, optional):
                Whether to plot the algorithm's results. Defaults to False.
        """
        self.algorithm = algorithm
        self.start = start
        self.end = end
        self.plot = plot

    def execute(self):
        """
        Executes the encapsulated algorithm with the specified parameters.

        This method calls the `execute` method of the provided algorithm
        instance with `start`, `end`, and `plot` as arguments.
        """
        self.algorithm.execute(self.start, self.end, self.plot)

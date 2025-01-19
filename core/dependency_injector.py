class DependencyInjector:
    """A simple container for dependency management.

    This class provides a mechanism for registering and resolving
    dependencies within an application. It acts as a service container
    for managing dependencies and ensuring that they are properly
    instantiated and available for use.
    """

    def __init__(self):
        """Initializes a new instance of the DependencyInjector class.

        Attributes:
            _services (dict): A dictionary to store service names as keys
                and their respective instances or factories as values.
        """
        self._services = {}

    def register(self, name, service):
        """Registers a dependency in the container.

        Args:
            name (str): The unique identifier for the dependency.
            service (Any): The instance or factory function of the dependency
                to be registered.

        Raises:
            ValueError: If a service with the given name is already registered.
        """
        if name in self._services:
            raise ValueError(f"A service with the name '{name}' is already registered.")
        self._services[name] = service

    def resolve(self, name):
        """Resolves a registered dependency by its name.

        Args:
            name (str): The unique identifier for the dependency to resolve.

        Returns:
            Any: The instance or factory function of the resolved dependency.

        Raises:
            ValueError: If no service is registered under the given name.
        """
        service = self._services.get(name)
        if not service:
            raise ValueError(f"No service is registered with the name: {name}")
        return service

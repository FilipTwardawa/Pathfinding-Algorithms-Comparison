class DependencyInjector:
    """A simple container for dependency management."""

    def __init__(self):
        self._services = {}

    def register(self, name, service):
        """Registers dependency."""
        self._services[name] = service

    def resolve(self, name):
        """Solves the relationship."""
        service = self._services.get(name)
        if not service:
            raise ValueError(f"No correlation was registered: {name}")
        return service

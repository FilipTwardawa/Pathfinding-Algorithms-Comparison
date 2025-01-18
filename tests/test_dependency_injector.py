from core.dependency_injector import DependencyInjector


def test_dependency_injection():
    """Test the dependency injection mechanism.

    This function tests the `DependencyInjector` class to ensure that:
    1. Services can be registered correctly.
    2. Registered services can be resolved accurately.

    The test performs the following steps:
    - Creates an instance of `DependencyInjector`.
    - Registers a test service with the injector.
    - Resolves the registered service and verifies that it matches the original object.

    Raises:
        AssertionError: If the resolved service does not match the registered object.
    """
    injector = DependencyInjector()
    service = object()

    injector.register("test_service", service)
    resolved_service = injector.resolve("test_service")

    assert resolved_service is service, "Failed to correctly resolve dependencies"

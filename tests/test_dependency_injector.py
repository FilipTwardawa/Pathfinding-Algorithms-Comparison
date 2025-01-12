from core.dependency_injector import DependencyInjector


def test_dependency_injection():
    injector = DependencyInjector()
    service = object()

    injector.register("test_service", service)
    resolved_service = injector.resolve("test_service")

    assert resolved_service is service, "Failed to correctly resolve dependencies"

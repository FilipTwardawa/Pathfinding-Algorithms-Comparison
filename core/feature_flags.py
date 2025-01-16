from abc import ABC, abstractmethod
from typing import Any, Dict

import flagsmith


class FeatureFlagProvider(ABC):
    """Abstract class for feature flag providers."""

    @abstractmethod
    def is_feature_enabled(self, feature_name: str, user_context: Dict[str, Any] = None) -> bool:
        """Checks if a feature is enabled."""
        pass

    @abstractmethod
    def get_feature_value(self, feature_name: str, user_context: Dict[str, Any] = None) -> Any:
        """Gets the value of a feature flag."""
        pass


class FlagsmithProvider(FeatureFlagProvider):
    """Feature Flag Provider for Flagsmith."""

    def __init__(self, environment_key: str):
        self.client = flagsmith.Flagsmith(environment_key=environment_key)

    def is_feature_enabled(self, feature_name: str, user_context: Dict[str, Any] = None) -> bool:
        flags = self.client.get_environment_flags()
        return flags.is_feature_enabled(feature_name)

    def get_feature_value(self, feature_name: str, user_context: Dict[str, Any] = None) -> Any:
        flags = self.client.get_environment_flags()
        return flags.get_feature_value(feature_name)


class FeatureFlagManager:
    """Manages feature flags dynamically."""

    def __init__(self, provider: FeatureFlagProvider):
        self.provider = provider

    def is_enabled(self, feature_name: str, user_context: Dict[str, Any] = None) -> bool:
        """Checks if a feature is enabled."""
        return self.provider.is_feature_enabled(feature_name, user_context)

    def get_value(self, feature_name: str, user_context: Dict[str, Any] = None) -> Any:
        """Gets the value of a feature flag."""
        return self.provider.get_feature_value(feature_name, user_context)

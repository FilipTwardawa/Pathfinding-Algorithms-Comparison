from abc import ABC, abstractmethod
from typing import Any, Dict

import flagsmith


class FeatureFlagProvider(ABC):
    """Abstract base class for feature flag providers.

    This class defines the interface that all feature flag providers must implement.

    Methods:
        is_feature_enabled(feature_name, user_context): Checks if a feature is enabled.
        get_feature_value(feature_name, user_context): Retrieves the value of a feature flag.
    """

    @abstractmethod
    def is_feature_enabled(self, feature_name: str, user_context: Dict[str, Any] = None) -> bool:
        """Checks if a feature is enabled.

        Args:
            feature_name (str): The name of the feature to check.
            user_context (Dict[str, Any], optional): Additional context about the user. Defaults to None.

        Returns:
            bool: True if the feature is enabled, False otherwise.
        """
        pass

    @abstractmethod
    def get_feature_value(self, feature_name: str, user_context: Dict[str, Any] = None) -> Any:
        """Gets the value of a feature flag.

        Args:
            feature_name (str): The name of the feature to retrieve.
            user_context (Dict[str, Any], optional): Additional context about the user. Defaults to None.

        Returns:
            Any: The value of the feature flag.
        """
        pass


class FlagsmithProvider(FeatureFlagProvider):
    """Feature flag provider implementation for Flagsmith.

    This class integrates with the Flagsmith service to manage feature flags.

    Attributes:
        client (flagsmith.Flagsmith): The Flagsmith client instance used to interact with the service.

    Methods:
        is_feature_enabled(feature_name, user_context): Checks if a feature is enabled.
        get_feature_value(feature_name, user_context): Retrieves the value of a feature flag.
    """

    def __init__(self, environment_key: str):
        """Initializes the FlagsmithProvider.

        Args:
            environment_key (str): The environment key for the Flagsmith client.
        """
        self.client = flagsmith.Flagsmith(environment_key=environment_key)

    def is_feature_enabled(self, feature_name: str, user_context: Dict[str, Any] = None) -> bool:
        """Checks if a feature is enabled.

        Args:
            feature_name (str): The name of the feature to check.
            user_context (Dict[str, Any], optional): Additional context about the user. Defaults to None.

        Returns:
            bool: True if the feature is enabled, False otherwise.
        """
        flags = self.client.get_environment_flags()
        return flags.is_feature_enabled(feature_name)

    def get_feature_value(self, feature_name: str, user_context: Dict[str, Any] = None) -> Any:
        """Gets the value of a feature flag.

        Args:
            feature_name (str): The name of the feature to retrieve.
            user_context (Dict[str, Any], optional): Additional context about the user. Defaults to None.

        Returns:
            Any: The value of the feature flag.
        """
        flags = self.client.get_environment_flags()
        return flags.get_feature_value(feature_name)


class FeatureFlagManager:
    """Manages feature flags dynamically through a specified provider.

    Attributes:
        provider (FeatureFlagProvider): The feature flag provider used for managing feature flags.

    Methods:
        is_enabled(feature_name, user_context): Checks if a feature is enabled.
        get_value(feature_name, user_context): Retrieves the value of a feature flag.
    """

    def __init__(self, provider: FeatureFlagProvider):
        """Initializes the FeatureFlagManager.

        Args:
            provider (FeatureFlagProvider): An instance of a feature flag provider.
        """
        self.provider = provider

    def is_enabled(self, feature_name: str, user_context: Dict[str, Any] = None) -> bool:
        """Checks if a feature is enabled.

        Args:
            feature_name (str): The name of the feature to check.
            user_context (Dict[str, Any], optional): Additional context about the user. Defaults to None.

        Returns:
            bool: True if the feature is enabled, False otherwise.
        """
        return self.provider.is_feature_enabled(feature_name, user_context)

    def get_value(self, feature_name: str, user_context: Dict[str, Any] = None) -> Any:
        """Gets the value of a feature flag.

        Args:
            feature_name (str): The name of the feature to retrieve.
            user_context (Dict[str, Any], optional): Additional context about the user. Defaults to None.

        Returns:
            Any: The value of the feature flag.
        """
        return self.provider.get_feature_value(feature_name, user_context)

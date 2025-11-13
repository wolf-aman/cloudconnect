from typing import Dict, Type, Any
from domain.cloud_resource import CloudResource
from resources import get

class ResourceFactory:
    """Simple registry-based factory."""

    @staticmethod
    def create(resource_type: str, name: str, config: Dict[str, Any]) -> CloudResource:
        cls = get(resource_type)
        if not cls:
            raise ValueError(f"Unknown resource type: {resource_type}")
        instance = cls(name, config)
        instance.validate_config()
        return instance

class AppResourceFactory(ResourceFactory):
    """Example of a specialized factory for app-related resources."""
    @staticmethod
    def create(resource_type: str, name: str, config: Dict[str, Any]) -> CloudResource:
        if resource_type.lower() == "appservice":
            config.setdefault("replica_count", 1)
        return super(AppResourceFactory, AppResourceFactory).create(resource_type, name, config)
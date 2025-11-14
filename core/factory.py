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

class DatabaseResourceFactory(ResourceFactory):
    """Specialized factory for database-related resources."""
    @staticmethod
    def create(resource_type: str, name: str, config: Dict[str, Any]) -> CloudResource:
        if resource_type.lower() == "cachedb":
            config.setdefault("eviction_policy", "LRU")
        return super(DatabaseResourceFactory, DatabaseResourceFactory).create(resource_type, name, config)

class StorageResourceFactory(ResourceFactory):
    """Factory for storage-related resources like StorageAccount."""
    @staticmethod
    def create(resource_type: str, name: str, config: Dict[str, Any]) -> CloudResource:
        if resource_type.lower() == "storageaccount":
            config.setdefault("encryption_enabled", True)
            config.setdefault("max_size_gb", 100)
            if config.get("max_size_gb") > 1024:
                raise ValueError("max_size_gb cannot exceed 1024 GB.")
        return super(StorageResourceFactory, StorageResourceFactory).create(resource_type, name, config)

class CacheResourceFactory(ResourceFactory):
    """Factory for cache-related resources like CacheDB."""
    @staticmethod
    def create(resource_type: str, name: str, config: Dict[str, Any]) -> CloudResource:
        if resource_type.lower() == "cachedb":
            config.setdefault("eviction_policy", "LRU")
            config.setdefault("ttl_seconds", 3600)
            if config.get("ttl_seconds") < 300:
                raise ValueError("ttl_seconds must be at least 300 seconds.")
        return super(CacheResourceFactory, CacheResourceFactory).create(resource_type, name, config)
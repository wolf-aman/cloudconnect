from typing import Dict, Any, Type, Optional
from domain.cloud_resource import CloudResource
from core.decorator import LoggingDecorator
from core.factory import ResourceFactory
from utils.logger_utils import now_ts, write_log

class ResourceManager:
    """
    Facade class that orchestrates all operations.
    Follows Single Responsibility Principle - manages resource lifecycle.
    Follows Open/Closed Principle - extensible via factory pattern.
    """

    def __init__(self, factory: Optional[Type[ResourceFactory]] = None, use_decorator: bool = True):
        self._resources: Dict[str, CloudResource] = {}
        self._factory_class = factory or ResourceFactory
        self._use_decorator = use_decorator

    def create_resource(self, resource_type: str, name: str, config: Dict[str, Any]) -> str:
        """
        Create a new resource using Factory pattern.
        Follows Dependency Inversion - depends on abstraction (factory).
        """
        self._validate_resource_creation(name)
        
        try:
            # Use factory to create resource (Factory pattern)
            resource = self._factory_class.create(resource_type, name, config)
            
            # Apply decorator if needed (Decorator pattern)
            decorated_resource = LoggingDecorator(resource) if self._use_decorator else resource
            
            # Store the resource
            self._resources[name] = decorated_resource
            
            # Log creation
            write_log(name, f"[{now_ts()}] {resource_type} '{name}' created with config {config}")
            
            return f"{resource_type} '{name}' created successfully."
            
        except Exception as e:
            error_msg = f"Failed to create {resource_type} '{name}': {str(e)}"
            write_log(name, f"[{now_ts()}] {error_msg}")
            raise RuntimeError(error_msg)

    def start_resource(self, name: str) -> str:
        """Start a resource with proper error handling."""
        resource = self._get_resource(name)
        try:
            return resource.start()
        except Exception as e:
            raise RuntimeError(f"Failed to start '{name}': {str(e)}")

    def stop_resource(self, name: str) -> str:
        """Stop a resource with proper error handling."""
        resource = self._get_resource(name)
        try:
            return resource.stop()
        except Exception as e:
            raise RuntimeError(f"Failed to stop '{name}': {str(e)}")

    def delete_resource(self, name: str) -> str:
        """Delete a resource with proper error handling."""
        resource = self._get_resource(name)
        try:
            return resource.delete()
        except Exception as e:
            raise RuntimeError(f"Failed to delete '{name}': {str(e)}")

    def list_resources(self) -> Dict[str, Dict[str, Any]]:
        """List all resources with their metadata."""
        return {name: resource.to_dict() for name, resource in self._resources.items()}

    def get_resource_count(self) -> Dict[str, int]:
        """Get count of resources by type and status."""
        counts = {
            "total": len(self._resources), 
            "active": 0,
            "deleted": 0,
            "by_type": {}, 
            "by_status": {}
        }
        
        for resource in self._resources.values():
            resource_data = resource.to_dict()
            resource_type = resource_data["type"]
            status = resource_data["status"]
            is_deleted = resource_data.get("deleted", False)
            
            # Count by type
            counts["by_type"][resource_type] = counts["by_type"].get(resource_type, 0) + 1
            
            # Count by status
            counts["by_status"][status] = counts["by_status"].get(status, 0) + 1
            
            # Count active vs deleted
            if is_deleted:
                counts["deleted"] += 1
            else:
                counts["active"] += 1
        
        return counts

    def _validate_resource_creation(self, name: str) -> None:
        """Validate resource creation prerequisites."""
        if name in self._resources:
            raise RuntimeError(f"Resource '{name}' already exists")

    def _get_resource(self, name: str) -> CloudResource:
        """Get resource by name with validation."""
        if name not in self._resources:
            raise RuntimeError(f"Resource '{name}' not found")
        return self._resources[name]

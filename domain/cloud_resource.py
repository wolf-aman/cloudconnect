from abc import ABC, abstractmethod
from typing import Dict, Any
from domain.state import CreatedState

class CloudResource(ABC):
    """Abstract base class for all cloud resources following OOP principles."""
    
    def __init__(self, name: str, config: Dict[str, Any]):
        self._name = self._validate_name(name)
        self._config = config.copy()  # Defensive copying
        self._deleted = False
        self._state = CreatedState(self)
    
    @property
    def name(self) -> str:
        """Getter for resource name (encapsulation)."""
        return self._name
    
    @property
    def config(self) -> Dict[str, Any]:
        """Getter for resource configuration (encapsulation)."""
        return self._config.copy()  # Return copy to prevent external modification
    
    @property
    def deleted(self) -> bool:
        """Getter for deletion status."""
        return self._deleted
    
    @deleted.setter
    def deleted(self, value: bool):
        """Setter for deletion status with validation."""
        if not isinstance(value, bool):
            raise ValueError("Deleted status must be boolean")
        self._deleted = value
    
    def set_state(self, state):
        """Set the current state (State pattern)."""
        self._state = state
    
    def start(self) -> str:
        """Delegate to current state (State pattern)."""
        return self._state.start()
    
    def stop(self) -> str:
        """Delegate to current state (State pattern)."""
        return self._state.stop()
    
    def delete(self) -> str:
        """Delegate to current state (State pattern)."""
        return self._state.delete()
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert resource to dictionary representation."""
        return {
            "name": self._name,
            "type": self.__class__.__name__,
            "status": self._state.name,
            "deleted": self._deleted,
            "details": self.get_details(),
            "config": self._config.copy()
        }
    
    @staticmethod
    def _validate_name(name: str) -> str:
        """Validate resource name following business rules."""
        if not name or not isinstance(name, str):
            raise ValueError("Resource name must be a non-empty string")
        if len(name.strip()) == 0:
            raise ValueError("Resource name cannot be empty or whitespace")
        if len(name) > 50:
            raise ValueError("Resource name cannot exceed 50 characters")
        return name.strip()
    
    @abstractmethod
    def validate_config(self) -> None:
        """Validate resource-specific configuration (Template Method pattern)."""
        pass
    
    @abstractmethod
    def get_details(self) -> str:
        """Get resource-specific details (Template Method pattern)."""
        pass

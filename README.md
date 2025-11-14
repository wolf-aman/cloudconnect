# CloudConnect

CloudConnect is a modular and extensible system designed to manage cloud resources efficiently. It provides a Command-Line Interface (CLI) for creating, starting, stopping, deleting, and managing various cloud resources such as App Services, Storage Accounts, and Cache Databases. The system is built using modern software design principles, making it highly maintainable and extensible.

---

## Key Features

- **User Authentication**: Secure user authentication with signup, login, and logout features.
- **Resource Lifecycle Management**: Manage the lifecycle of cloud resources with states like `created`, `started`, `stopped`, and `deleted`.
- **Extensibility**: Add new resource types easily using the `@register` decorator.
- **Factory Pattern**: Centralized resource creation using specialized factories for different resource types.
- **State Pattern**: Resources follow a state-driven lifecycle.
- **Logging**: Detailed logging of all resource operations for auditing and debugging.
- **Decorator Pattern**: Add logging functionality dynamically to resource operations.
- **CLI Interface**: User-friendly CLI for managing resources interactively.

---

## Resource Factories

### 1. `AppResourceFactory`
Handles app-related resources like `AppService`. It applies app-specific defaults such as setting a minimum replica count.

### 2. `StorageResourceFactory`
Handles the creation of storage-related resources like `StorageAccount`. It applies storage-specific defaults such as enabling encryption by default or validating storage size limits.

### 3. `CacheResourceFactory`
Creates caching systems such as `CacheDB`. It enforces cache-related defaults, including setting a fallback eviction policy (e.g., LRU) and minimum TTL values.

---

## Resource Types

### AppService
- **Runtime**: `python`, `nodejs`, `dotnet`
- **Region**: `EastUS`, `WestEurope`, `CentralIndia`
- **Replica Count**: `1`, `2`, `3`

### StorageAccount
- **Encryption Enabled**: `True` or `False`
- **Access Key**: Minimum 8 characters
- **Max Size (GB)**: Positive integer

### CacheDB
- **Eviction Policy**: `LRU`, `FIFO`
- **TTL (seconds)**: Positive integer
- **Capacity (MB)**: Positive integer

---

## Usage

### Running the CLI

1. Start the CLI:
   ```bash
   python run_cloudconnect.py
   ```

2. Follow the on-screen instructions to manage resources.

---

### Example Workflows

#### 1. User Authentication

- **Signup**: Provide a unique username, name, email, and password. If the username already exists, signup will fail.
- **Login**: Use your username and password to log in. Only one user can be logged in at a time.
- **Logout**: Users can log out from the main menu.

#### 2. Create a Resource

- Select the resource type (e.g., AppService, StorageAccount, CacheDB).
- Provide the required configuration (e.g., runtime, region, encryption settings).
- The resource will be created and logged.

#### 3. Start, Stop, or Delete a Resource

- Choose the operation from the main menu.
- Select the resource by name.
- The operation will be performed, and the state will be updated.

#### 4. View Logs

- Select "View Logs" from the main menu.
- Choose a specific log file or view all logs.

---

## Design Principles

### 1. Factory Pattern
The `ResourceFactory` class centralizes the creation of resources, ensuring that the creation logic is decoupled from the rest of the system.

### 2. State Pattern
Each resource has a state (`Created`, `Started`, `Stopped`, `Deleted`) that governs its behavior. This ensures that operations are only allowed in valid states.

### 3. Decorator Pattern
The `LoggingDecorator` dynamically adds logging functionality to resource operations without modifying the resource classes.

### 4. Single Responsibility Principle
The `ResourceManager` class acts as a facade, managing the lifecycle of resources while delegating specific tasks to other components.

---

## Adding New Resource Types

1. Create a new file in the `resources` directory.
2. Define a class that inherits from `CloudResource`.
3. Implement the `validate_config` and `get_details` methods.
4. Use the `@register` decorator to register the resource.

Example:
```python
from domain.cloud_resource import CloudResource
from resources import register

@register("NewResource")
class NewResource(CloudResource):
    def validate_config(self):
        # Validate configuration
        pass

    def get_details(self):
        # Return resource details
        return "Details about NewResource"
```

---

## Logs

Logs are stored in the `cloudconnect/logs` directory. Each resource has its own log file, which records all operations performed on it.

---

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

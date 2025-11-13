<<<<<<< HEAD
# CloudConnect

CloudConnect is a modular and extensible system designed to manage cloud resources efficiently. It provides a Command-Line Interface (CLI) for creating, starting, stopping, deleting, and managing various cloud resources such as App Services, Storage Accounts, and Cache Databases. The system is built using modern software design principles, making it highly maintainable and extensible.

---

## Key Features

- **Resource Lifecycle Management**: Manage the lifecycle of cloud resources with states like `created`, `started`, `stopped`, and `deleted`.
- **Extensibility**: Add new resource types easily using the `@register` decorator.
- **Factory Pattern**: Centralized resource creation using a factory pattern.
- **State Pattern**: Resources follow a state-driven lifecycle.
- **Logging**: Detailed logging of all resource operations for auditing and debugging.
- **Decorator Pattern**: Add logging functionality dynamically to resource operations.
- **CLI Interface**: User-friendly CLI for managing resources interactively.
- **User Authentication**: Secure user authentication with signup, login, and logout features.

---

## Project Structure

```
CloudConnect/
├── application/
│   └── resource_manager.py  # Facade for managing resources
├── cloudconnect/
│   ├── __init__.py          # Package initialization
│   └── main.py              # CLI entry point
├── core/
│   ├── __init__.py          # Package initialization
│   ├── decorator.py         # Logging decorator for resources
│   └── factory.py           # Factory for creating resources
├── domain/
│   ├── __init__.py          # Package initialization
│   ├── cloud_resource.py    # Abstract base class for resources
│   └── state.py             # State pattern implementation
├── resources/
│   ├── __init__.py          # Resource registry
│   ├── app_service.py       # AppService resource
│   ├── cache_db.py          # CacheDB resource
│   └── storage_account.py   # StorageAccount resource
├── utils/
│   ├── __init__.py          # Package initialization
│   └── logger_utils.py      # Utility for logging
└── run_cloudconnect.py      # Script to run the CLI
```

---

## File Descriptions

### `application/`
- **`resource_manager.py`**: Acts as a facade for managing the lifecycle of resources. It handles operations like creating, starting, stopping, and deleting resources.

### `cloudconnect/`
- **`__init__.py`**: Marks the `cloudconnect` directory as a Python package.
- **`main.py`**: The entry point for the CLI. It provides an interactive interface for managing resources.

### `core/`
- **`__init__.py`**: Marks the `core` directory as a Python package.
- **`decorator.py`**: Implements the `LoggingDecorator` class, which adds logging functionality to resource operations.
- **`factory.py`**: Contains the `ResourceFactory` class for creating resources and the `AppResourceFactory` for app-specific resources.

### `domain/`
- **`__init__.py`**: Marks the `domain` directory as a Python package.
- **`cloud_resource.py`**: Defines the abstract base class `CloudResource`, which all resource types inherit from.
- **`state.py`**: Implements the State pattern for managing resource states (`Created`, `Started`, `Stopped`, `Deleted`).

### `resources/`
- **`__init__.py`**: Contains the resource registry and the `@register` decorator for registering new resource types.
- **`app_service.py`**: Defines the `AppService` resource, which represents web applications.
- **`cache_db.py`**: Defines the `CacheDB` resource, which represents in-memory cache databases.
- **`storage_account.py`**: Defines the `StorageAccount` resource, which represents cloud storage accounts.

### `utils/`
- **`__init__.py`**: Marks the `utils` directory as a Python package.
- **`logger_utils.py`**: Provides utility functions for logging, including writing logs to files and generating timestamps.

### Root Directory
- **`run_cloudconnect.py`**: The main script to run the CloudConnect CLI. It imports and invokes the `cli_main` function from `cloudconnect.main`.

---

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Ensure you have the required permissions to create directories and files for logging.

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd CloudConnect
   ```

2. Install dependencies (if any):
   ```bash
   pip install -r requirements.txt
   ```

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

#### 1. Create a Resource

- Select the resource type (e.g., AppService, StorageAccount, CacheDB).
- Provide the required configuration (e.g., runtime, region, encryption settings).
- The resource will be created and logged.

#### 2. Start, Stop, or Delete a Resource

- Choose the operation from the main menu.
- Select the resource by name.
- The operation will be performed, and the state will be updated.

#### 3. View Logs

- Select "View Logs" from the main menu.
- Choose a specific log file or view all logs.

#### 4. User Authentication

- **Signup**: Provide a unique username, name, email, and password. If the username already exists, signup will fail.
- **Login**: Use your username and password to log in. Only one user can be logged in at a time.
- **Logout**: Users can log out from the main menu.

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
=======
# CloudConnect

CloudConnect is a modular and extensible system designed to manage cloud resources efficiently. It provides a Command-Line Interface (CLI) for creating, starting, stopping, deleting, and managing various cloud resources such as App Services, Storage Accounts, and Cache Databases. The system is built using modern software design principles, making it highly maintainable and extensible.

---

## Key Features

- **Resource Lifecycle Management**: Manage the lifecycle of cloud resources with states like `created`, `started`, `stopped`, and `deleted`.
- **Extensibility**: Add new resource types easily using the `@register` decorator.
- **Factory Pattern**: Centralized resource creation using a factory pattern.
- **State Pattern**: Resources follow a state-driven lifecycle.
- **Logging**: Detailed logging of all resource operations for auditing and debugging.
- **Decorator Pattern**: Add logging functionality dynamically to resource operations.
- **CLI Interface**: User-friendly CLI for managing resources interactively.

---

## Project Structure

```
CloudConnect/
├── application/
│   └── resource_manager.py  # Facade for managing resources
├── cloudconnect/
│   ├── __init__.py          # Package initialization
│   └── main.py              # CLI entry point
├── core/
│   ├── __init__.py          # Package initialization
│   ├── decorator.py         # Logging decorator for resources
│   └── factory.py           # Factory for creating resources
├── domain/
│   ├── __init__.py          # Package initialization
│   ├── cloud_resource.py    # Abstract base class for resources
│   └── state.py             # State pattern implementation
├── resources/
│   ├── __init__.py          # Resource registry
│   ├── app_service.py       # AppService resource
│   ├── cache_db.py          # CacheDB resource
│   └── storage_account.py   # StorageAccount resource
├── utils/
│   ├── __init__.py          # Package initialization
│   └── logger_utils.py      # Utility for logging
└── run_cloudconnect.py      # Script to run the CLI
```

---

## File Descriptions

### `application/`
- **`resource_manager.py`**: Acts as a facade for managing the lifecycle of resources. It handles operations like creating, starting, stopping, and deleting resources.

### `cloudconnect/`
- **`__init__.py`**: Marks the `cloudconnect` directory as a Python package.
- **`main.py`**: The entry point for the CLI. It provides an interactive interface for managing resources.

### `core/`
- **`__init__.py`**: Marks the `core` directory as a Python package.
- **`decorator.py`**: Implements the `LoggingDecorator` class, which adds logging functionality to resource operations.
- **`factory.py`**: Contains the `ResourceFactory` class for creating resources and the `AppResourceFactory` for app-specific resources.

### `domain/`
- **`__init__.py`**: Marks the `domain` directory as a Python package.
- **`cloud_resource.py`**: Defines the abstract base class `CloudResource`, which all resource types inherit from.
- **`state.py`**: Implements the State pattern for managing resource states (`Created`, `Started`, `Stopped`, `Deleted`).

### `resources/`
- **`__init__.py`**: Contains the resource registry and the `@register` decorator for registering new resource types.
- **`app_service.py`**: Defines the `AppService` resource, which represents web applications.
- **`cache_db.py`**: Defines the `CacheDB` resource, which represents in-memory cache databases.
- **`storage_account.py`**: Defines the `StorageAccount` resource, which represents cloud storage accounts.

### `utils/`
- **`__init__.py`**: Marks the `utils` directory as a Python package.
- **`logger_utils.py`**: Provides utility functions for logging, including writing logs to files and generating timestamps.

### Root Directory
- **`run_cloudconnect.py`**: The main script to run the CloudConnect CLI. It imports and invokes the `cli_main` function from `cloudconnect.main`.

---

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Ensure you have the required permissions to create directories and files for logging.

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd CloudConnect
   ```

2. Install dependencies (if any):
   ```bash
   pip install -r requirements.txt
   ```

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

#### 1. Create a Resource

- Select the resource type (e.g., AppService, StorageAccount, CacheDB).
- Provide the required configuration (e.g., runtime, region, encryption settings).
- The resource will be created and logged.

#### 2. Start, Stop, or Delete a Resource

- Choose the operation from the main menu.
- Select the resource by name.
- The operation will be performed, and the state will be updated.

#### 3. View Logs

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
>>>>>>> 56a5158a845bb6724b37a31a8c35e029df882027
